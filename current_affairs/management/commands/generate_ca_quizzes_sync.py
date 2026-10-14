from __future__ import annotations

import time
from datetime import date

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from academies.models import Academy
from current_affairs.models import CADocument, CAQuestion
from current_affairs.services.gemini_quiz import generate_mcqs_from_text, model_name
from current_affairs.services.pdf_extract import extract_pdf_text, split_monthly_sections
from current_affairs.subjects import normalize_subject_tag


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise CommandError(f"Invalid date {value!r}; use YYYY-MM-DD") from exc


def generate_for_document(doc: CADocument) -> int:
    text = extract_pdf_text(doc.file.path)
    if len(text) < 100:
        raise RuntimeError("PDF text extraction returned almost no content")

    generated: list[dict] = []
    if doc.doc_type == CADocument.DocType.DAILY:
        target = getattr(settings, "CA_DAILY_QUESTION_TARGET", 12)
        generated = generate_mcqs_from_text(text, target_count=target)
    else:
        per_section = getattr(settings, "CA_MONTHLY_QUESTIONS_PER_SECTION", 4)
        for section_name, body in split_monthly_sections(text):
            chunk_qs = generate_mcqs_from_text(
                body,
                target_count=per_section,
                section_label=section_name,
            )
            for q in chunk_qs:
                if not q.get("subject_tag") or q.get("subject_tag") == "Other":
                    normalized_section = normalize_subject_tag(section_name)
                    if normalized_section != "Other":
                        q["subject_tag"] = normalized_section
                generated.append(q)

    if not generated:
        raise RuntimeError("Gemini returned no usable questions")

    with transaction.atomic():
        CAQuestion.objects.filter(document=doc).delete()
        rows = [
            CAQuestion(
                document=doc,
                stem=q["stem"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"],
                explanation=q["explanation"],
                subject_tag=normalize_subject_tag(q["subject_tag"]),
                source_topic=q["source_topic"],
                is_published=True,
                sort_order=i,
            )
            for i, q in enumerate(generated)
        ]
        CAQuestion.objects.bulk_create(rows)
        CADocument.objects.filter(pk=doc.pk).update(
            status=CADocument.Status.READY,
            error_message="",
            gemini_model=model_name(),
            generated_at=timezone.now(),
        )
    return len(generated)


class Command(BaseCommand):
    help = (
        "Synchronously generate quizzes for daily CA documents (no Celery). "
        "Useful when rate limits make a worker queue unreliable."
    )

    def add_arguments(self, parser):
        parser.add_argument("--start", type=parse_date, required=True)
        parser.add_argument("--end", type=parse_date, required=True)
        parser.add_argument("--academy", default="fortuneias")
        parser.add_argument(
            "--force",
            action="store_true",
            help="Also regenerate documents that are already ready.",
        )
        parser.add_argument(
            "--sleep",
            type=float,
            default=2.0,
            help="Seconds to sleep between documents (default: 2).",
        )
        parser.add_argument(
            "--max-retries",
            type=int,
            default=5,
            help="Retries per document on transient Gemini errors.",
        )

    def handle(self, *args, **options):
        start: date = options["start"]
        end: date = options["end"]
        if start > end:
            raise CommandError("--start must be on or before --end")

        academy = Academy.objects.filter(slug=options["academy"]).first()
        if academy is None:
            raise CommandError(f"Academy not found: {options['academy']}")

        qs = CADocument.objects.filter(
            academy=academy,
            doc_type=CADocument.DocType.DAILY,
            source_date__gte=start,
            source_date__lte=end,
        ).order_by("source_date", "id")
        if not options["force"]:
            qs = qs.exclude(status=CADocument.Status.READY)

        docs = list(qs)
        self.stdout.write(
            f"Generating for {len(docs)} document(s) with model={model_name()}"
        )

        ok = 0
        failed = 0
        for doc in docs:
            CADocument.objects.filter(pk=doc.pk).update(
                status=CADocument.Status.PROCESSING,
                error_message="",
            )
            success = False
            last_error = ""
            for attempt in range(1, options["max_retries"] + 1):
                try:
                    count = generate_for_document(doc)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"READY {doc.source_date} id={doc.pk} qs={count}"
                        )
                    )
                    ok += 1
                    success = True
                    break
                except Exception as exc:
                    last_error = str(exc)
                    transient = any(
                        token in last_error
                        for token in ("429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE")
                    )
                    self.stdout.write(
                        f"  attempt {attempt}/{options['max_retries']} "
                        f"{doc.source_date}: {last_error[:160].replace(chr(10), ' ')}"
                    )
                    if not transient or attempt >= options["max_retries"]:
                        break
                    time.sleep(min(60, 10 * attempt))

            if not success:
                CADocument.objects.filter(pk=doc.pk).update(
                    status=CADocument.Status.FAILED,
                    error_message=last_error[:2000],
                )
                self.stdout.write(
                    self.style.ERROR(f"FAIL {doc.source_date} id={doc.pk}")
                )
                failed += 1

            time.sleep(max(0.0, options["sleep"]))

        self.stdout.write("")
        self.stdout.write(f"Done. ready={ok} failed={failed}")
