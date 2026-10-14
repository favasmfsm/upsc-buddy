import logging
from datetime import date

from celery import shared_task
from celery.exceptions import MaxRetriesExceededError, Retry
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from academies.models import Academy

from .models import CADocument, CAQuestion
from .services.finder_ingest import ingest_range
from .services.finder_scrape import scrape_range
from .services.gemini_quiz import generate_mcqs_from_text, model_name
from .services.pdf_extract import extract_pdf_text, split_monthly_sections
from .subjects import normalize_subject_tag

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    soft_time_limit=1800,
    time_limit=2100,
)
def sync_finder_range(
    self,
    academy_id: int,
    start_iso: str,
    end_iso: str,
    regenerate: bool = False,
):
    """
    Scrape FINDER PDFs for a date range, ingest into CADocuments, and enqueue
    per-document Gemini generation (fill gaps; optionally regenerate existing).
    """
    try:
        academy = Academy.objects.get(pk=academy_id)
    except Academy.DoesNotExist:
        logger.warning("Academy %s missing for FINDER sync", academy_id)
        return {"status": "missing_academy"}

    start = date.fromisoformat(start_iso)
    end = date.fromisoformat(end_iso)
    scrape_stats = scrape_range(start, end)
    ingest_stats = ingest_range(
        academy,
        start,
        end,
        regenerate=regenerate,
        enqueue=True,
    )
    summary = {
        "status": "ok",
        "academy_id": academy_id,
        "start": start_iso,
        "end": end_iso,
        "regenerate": regenerate,
        "scrape": scrape_stats,
        "ingest": ingest_stats,
    }
    logger.info("FINDER sync complete: %s", summary)
    return summary



@shared_task(
    bind=True,
    max_retries=12,
    soft_time_limit=1500,
    time_limit=1800,
    # Free-tier Gemini Flash is ~5 RPM; keep headroom for other calls.
    rate_limit="4/m",
)
def generate_questions_for_document(self, document_id: int, force: bool = False):
    """
    Run Gemini once (or once per monthly section) for a CA document.
    Stores MCQs in the bank for reuse by all students — never called per quiz.
    """
    try:
        doc = CADocument.objects.get(pk=document_id)
    except CADocument.DoesNotExist:
        logger.warning("CADocument %s missing", document_id)
        return {"status": "missing"}

    existing = doc.questions.exists()
    if (
        not force
        and doc.status == CADocument.Status.READY
        and existing
    ):
        return {"status": "skipped", "reason": "already_ready"}

    CADocument.objects.filter(pk=doc.pk).update(
        status=CADocument.Status.PROCESSING,
        error_message="",
    )

    try:
        path = doc.file.path
        text = extract_pdf_text(path)
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
            # Replace only after successful generation
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

        return {"status": "ready", "count": len(generated)}
    except Retry:
        raise
    except Exception as exc:
        message = str(exc)
        is_transient = (
            "429" in message
            or "RESOURCE_EXHAUSTED" in message
            or "503" in message
            or "UNAVAILABLE" in message
            or "high demand" in message.lower()
        )
        if is_transient:
            countdown = min(60, 15 + (self.request.retries * 5))
            logger.warning(
                "CA generation transient error for document %s; retry in %ss",
                document_id,
                countdown,
            )
            CADocument.objects.filter(pk=doc.pk).update(
                status=CADocument.Status.PENDING,
                error_message=message[:2000],
            )
            try:
                raise self.retry(exc=exc, countdown=countdown)
            except MaxRetriesExceededError:
                logger.error(
                    "CA generation exhausted retries for document %s", document_id
                )

        logger.exception("CA generation failed for document %s", document_id)
        CADocument.objects.filter(pk=doc.pk).update(
            status=CADocument.Status.FAILED,
            error_message=message[:2000],
        )
        return {"status": "failed", "error": message}
