"""Ingest local FINDER PDFs into CADocument rows and enqueue generation."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from django.core.files import File
from django.db.models.signals import post_save

from academies.models import Academy
from current_affairs.models import CADocument
from current_affairs.services.finder_scrape import (
    default_pdf_dir,
    is_valid_cached_pdf,
    iter_dates,
)
from current_affairs.signals import _enqueue, enqueue_generation

FINDER_SYNC_MAX_DAYS = 62


def inclusive_day_count(start: date, end: date) -> int:
    return (end - start).days + 1


def ingest_range(
    academy: Academy,
    start: date,
    end: date,
    *,
    pdf_dir: Path | None = None,
    regenerate: bool = False,
    enqueue: bool = True,
) -> dict[str, int]:
    """
    Hybrid ingest for [start, end]:

    - Always create docs for days with a PDF and no existing document.
    - Without regenerate: skip ready docs; enqueue pending/failed.
    - With regenerate: replace PDF when available, force-enqueue all existing docs.
    """
    if start > end:
        raise ValueError("start must be on or before end")

    target = pdf_dir or default_pdf_dir()
    stats = {
        "created": 0,
        "replaced": 0,
        "skipped_ready": 0,
        "skipped_no_pdf": 0,
        "skipped_processing": 0,
        "enqueued": 0,
        "regenerate_only": 0,
    }

    # Manage enqueue ourselves so replace + force and fill-pending are consistent.
    post_save.disconnect(enqueue_generation, sender=CADocument)
    try:
        for day in iter_dates(start, end):
            pdf_path = target / f"{day.isoformat()}.pdf"
            has_pdf = is_valid_cached_pdf(pdf_path)
            existing = CADocument.objects.filter(
                academy=academy,
                doc_type=CADocument.DocType.DAILY,
                source_date=day,
            ).first()

            title = f"FINDER {day.strftime('%d-%m-%Y')}"
            upload_name = f"FINDER_{day.strftime('%d-%m-%Y')}.pdf"

            if existing is None:
                if not has_pdf:
                    stats["skipped_no_pdf"] += 1
                    continue
                doc = CADocument(
                    academy=academy,
                    doc_type=CADocument.DocType.DAILY,
                    title=title,
                    source_date=day,
                    status=CADocument.Status.PENDING,
                )
                with pdf_path.open("rb") as handle:
                    doc.file.save(upload_name, File(handle), save=False)
                doc.save()
                stats["created"] += 1
                if enqueue:
                    _enqueue(doc.pk, force=False)
                    stats["enqueued"] += 1
                continue

            if existing.status == CADocument.Status.PROCESSING:
                stats["skipped_processing"] += 1
                continue

            if regenerate:
                if has_pdf:
                    if existing.file:
                        existing.file.delete(save=False)
                    with pdf_path.open("rb") as handle:
                        existing.file.save(upload_name, File(handle), save=False)
                    existing.title = title
                    existing.status = CADocument.Status.PENDING
                    existing.error_message = ""
                    existing.save()
                    stats["replaced"] += 1
                else:
                    CADocument.objects.filter(pk=existing.pk).update(
                        status=CADocument.Status.PENDING,
                        error_message="",
                    )
                    stats["regenerate_only"] += 1
                if enqueue:
                    _enqueue(existing.pk, force=True)
                    stats["enqueued"] += 1
                continue

            # Fill gaps only: skip ready; re-queue pending/failed.
            if existing.status == CADocument.Status.READY:
                stats["skipped_ready"] += 1
                continue

            CADocument.objects.filter(pk=existing.pk).update(
                status=CADocument.Status.PENDING,
                error_message="",
            )
            if enqueue:
                _enqueue(existing.pk, force=False)
                stats["enqueued"] += 1
    finally:
        post_save.connect(enqueue_generation, sender=CADocument)

    return stats
