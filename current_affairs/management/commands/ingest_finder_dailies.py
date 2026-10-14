from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from django.db.models.signals import post_save

from academies.models import Academy
from current_affairs.models import CADocument
from current_affairs.signals import _enqueue, enqueue_generation


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise CommandError(f"Invalid date {value!r}; use YYYY-MM-DD") from exc


def iter_dates(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


class Command(BaseCommand):
    help = (
        "Bulk-create daily CADocument rows from local FINDER PDFs "
        "(YYYY-MM-DD.pdf) and enqueue Gemini quiz generation."
    )

    def add_arguments(self, parser):
        parser.add_argument("--start", type=parse_date, required=True)
        parser.add_argument("--end", type=parse_date, required=True)
        parser.add_argument(
            "--pdf-dir",
            type=Path,
            default=Path("data/daily/finder"),
            help="Directory of YYYY-MM-DD.pdf files (default: data/daily/finder)",
        )
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug (default: fortuneias)",
        )
        parser.add_argument(
            "--replace-existing",
            action="store_true",
            help="Replace PDF on existing daily docs and re-enqueue generation.",
        )
        parser.add_argument(
            "--skip-enqueue",
            action="store_true",
            help="Create/update documents without enqueueing Celery generation.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print actions without writing.",
        )

    def handle(self, *args, **options):
        start: date = options["start"]
        end: date = options["end"]
        pdf_dir: Path = options["pdf_dir"]
        if not pdf_dir.is_absolute():
            pdf_dir = Path.cwd() / pdf_dir

        if start > end:
            raise CommandError("--start must be on or before --end")
        if not pdf_dir.is_dir():
            raise CommandError(f"PDF directory not found: {pdf_dir}")

        academy = Academy.objects.filter(slug=options["academy"]).first()
        if academy is None:
            raise CommandError(f"Academy not found: {options['academy']}")

        created = 0
        replaced = 0
        skipped_existing = 0
        missing_pdf = 0
        enqueued = 0

        # Avoid double-enqueue when we manage queueing ourselves for replaces.
        if options["skip_enqueue"] or options["replace_existing"]:
            post_save.disconnect(enqueue_generation, sender=CADocument)

        try:
            for day in iter_dates(start, end):
                pdf_path = pdf_dir / f"{day.isoformat()}.pdf"
                if not pdf_path.is_file() or pdf_path.stat().st_size == 0:
                    missing_pdf += 1
                    self.stdout.write(f"MISSING {day.isoformat()}")
                    continue

                existing = CADocument.objects.filter(
                    academy=academy,
                    doc_type=CADocument.DocType.DAILY,
                    source_date=day,
                ).first()

                title = f"FINDER {day.strftime('%d-%m-%Y')}"
                upload_name = f"FINDER_{day.strftime('%d-%m-%Y')}.pdf"

                if existing and not options["replace_existing"]:
                    skipped_existing += 1
                    self.stdout.write(
                        f"SKIP {day.isoformat()} (exists id={existing.pk} "
                        f"status={existing.status})"
                    )
                    continue

                if options["dry_run"]:
                    action = "REPLACE" if existing else "CREATE"
                    self.stdout.write(f"{action} {day.isoformat()} ← {pdf_path.name}")
                    if existing:
                        replaced += 1
                    else:
                        created += 1
                    continue

                if existing:
                    if existing.file:
                        existing.file.delete(save=False)
                    with pdf_path.open("rb") as handle:
                        existing.file.save(upload_name, File(handle), save=False)
                    existing.title = title
                    existing.status = CADocument.Status.PENDING
                    existing.error_message = ""
                    existing.save()
                    replaced += 1
                    self.stdout.write(f"REPLACED {day.isoformat()} id={existing.pk}")
                    doc = existing
                else:
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
                    created += 1
                    self.stdout.write(f"CREATED {day.isoformat()} id={doc.pk}")

                if options["skip_enqueue"]:
                    continue

                # Creates enqueue via post_save signal when connected.
                # Replaces (signal disconnected) need an explicit force enqueue.
                if options["replace_existing"]:
                    _enqueue(doc.pk, force=True)
                    enqueued += 1
                elif existing is None:
                    enqueued += 1
        finally:
            if options["skip_enqueue"] or options["replace_existing"]:
                post_save.connect(enqueue_generation, sender=CADocument)

        self.stdout.write("")
        self.stdout.write("Summary")
        self.stdout.write(f"  Created:           {created}")
        self.stdout.write(f"  Replaced:          {replaced}")
        self.stdout.write(f"  Skipped existing:  {skipped_existing}")
        self.stdout.write(f"  Missing PDF:       {missing_pdf}")
        self.stdout.write(f"  Enqueued:          {enqueued}")
        self.stdout.write(f"  Academy:           {academy.slug}")
        self.stdout.write(f"  PDF dir:           {pdf_dir}")
        if options["dry_run"]:
            self.stdout.write(self.style.WARNING("Dry run — no changes written."))
