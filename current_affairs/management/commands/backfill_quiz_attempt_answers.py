from django.core.management.base import BaseCommand
from django.db import transaction

from current_affairs.models import QuizAttempt
from current_affairs.services.attempt_answers import (
    normalize_question_subject_tags,
    replace_answer_rows,
)


class Command(BaseCommand):
    help = (
        "Normalize CAQuestion.subject_tag values and backfill QuizAttemptAnswer "
        "rows from completed QuizAttempt JSON answers."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-questions",
            action="store_true",
            help="Do not rewrite CAQuestion.subject_tag values.",
        )
        parser.add_argument(
            "--skip-answers",
            action="store_true",
            help="Do not backfill QuizAttemptAnswer rows.",
        )

    def handle(self, *args, **options):
        if not options["skip_questions"]:
            updated = normalize_question_subject_tags()
            self.stdout.write(self.style.SUCCESS(f"Normalized {updated} question tag(s)."))

        if options["skip_answers"]:
            return

        completed = QuizAttempt.objects.filter(completed_at__isnull=False).order_by("id")
        total = completed.count()
        created_total = 0
        processed = 0
        for attempt in completed.iterator(chunk_size=100):
            with transaction.atomic():
                created_total += replace_answer_rows(attempt)
            processed += 1
            if processed % 100 == 0:
                self.stdout.write(f"Backfilled {processed}/{total} attempts…")

        self.stdout.write(
            self.style.SUCCESS(
                f"Backfilled answer rows for {processed} attempt(s) "
                f"({created_total} row(s))."
            )
        )
