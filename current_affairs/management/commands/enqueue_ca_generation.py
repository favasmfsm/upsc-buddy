from __future__ import annotations

from datetime import date

from django.core.management.base import BaseCommand, CommandError

from academies.models import Academy
from current_affairs.models import CADocument
from current_affairs.tasks import generate_questions_for_document


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise CommandError(f"Invalid date {value!r}; use YYYY-MM-DD") from exc


class Command(BaseCommand):
    help = (
        "Re-enqueue Gemini quiz generation for daily CA documents that are "
        "pending/failed/processing (or all with --force), staggered to respect "
        "API rate limits."
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
            "--stagger-seconds",
            type=int,
            default=18,
            help="Delay between task starts (default: 18s ≈ 3–4 RPM).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
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
        stagger = max(0, options["stagger_seconds"])
        self.stdout.write(f"Queueing {len(docs)} document(s), stagger={stagger}s")

        for i, doc in enumerate(docs):
            countdown = i * stagger
            self.stdout.write(
                f"  {doc.source_date} id={doc.pk} status={doc.status} "
                f"countdown={countdown}s"
            )
            if options["dry_run"]:
                continue
            CADocument.objects.filter(pk=doc.pk).update(
                status=CADocument.Status.PENDING,
                error_message="",
            )
            generate_questions_for_document.apply_async(
                args=[doc.pk],
                kwargs={"force": True},
                countdown=countdown,
                ignore_result=True,
            )

        if options["dry_run"]:
            self.stdout.write(self.style.WARNING("Dry run — nothing enqueued."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Enqueued {len(docs)} task(s)."))
