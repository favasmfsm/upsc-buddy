from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from academies.models import Academy, AcademyMembership, generate_invite_code
from concepts.models import CaseLaw, ConstitutionalAmendment
from current_affairs.models import CADocument, QuizAttempt
from learning.models import UserConceptProgress
from questions.models import PYQ
from subjects.models import Subject

User = get_user_model()

FORTUNEIAS_SLUG = "fortuneias"
FORTUNEIAS_NAME = "Fortune IAS"


class Command(BaseCommand):
    help = "Create Fortune IAS academy and backfill unscoped content onto it."

    def add_arguments(self, parser):
        parser.add_argument(
            "--admin-email",
            default="",
            help="Email for academy admin membership (must already exist).",
        )
        parser.add_argument(
            "--invite-code",
            default="",
            help="Optional fixed invite code (otherwise generated).",
        )

    def handle(self, *args, **options):
        invite = options["invite_code"] or generate_invite_code()
        academy, created = Academy.objects.get_or_create(
            slug=FORTUNEIAS_SLUG,
            defaults={
                "name": FORTUNEIAS_NAME,
                "display_name": FORTUNEIAS_NAME,
                "invite_code": invite,
                "is_active": True,
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created academy {academy.slug}"))
        else:
            self.stdout.write(f"Academy {academy.slug} already exists")
            if not academy.invite_code:
                academy.invite_code = invite
                academy.save(update_fields=["invite_code", "updated_at"])

        backfill_counts = {
            "subjects": Subject.objects.filter(academy__isnull=True).update(
                academy=academy
            ),
            "case_laws": CaseLaw.objects.filter(academy__isnull=True).update(
                academy=academy
            ),
            "amendments": ConstitutionalAmendment.objects.filter(
                academy__isnull=True
            ).update(academy=academy),
            "pyqs": PYQ.objects.filter(academy__isnull=True).update(academy=academy),
            "ca_documents": CADocument.objects.filter(academy__isnull=True).update(
                academy=academy
            ),
            "progress": UserConceptProgress.objects.filter(academy__isnull=True).update(
                academy=academy
            ),
            "quiz_attempts": QuizAttempt.objects.filter(academy__isnull=True).update(
                academy=academy
            ),
        }
        for label, count in backfill_counts.items():
            if count:
                self.stdout.write(f"  Backfilled {count} {label} → {academy.slug}")

        admin_email = (options["admin_email"] or "").strip()
        if admin_email:
            user = User.objects.filter(email__iexact=admin_email).first()
            if not user:
                self.stderr.write(
                    self.style.ERROR(f"No user with email {admin_email}")
                )
            else:
                membership, m_created = AcademyMembership.objects.update_or_create(
                    academy=academy,
                    user=user,
                    defaults={
                        "role": AcademyMembership.Role.ADMIN,
                        "is_active": True,
                    },
                )
                action = "Created" if m_created else "Updated"
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{action} academy admin membership for {user.email}"
                    )
                )

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"Academy: {academy.display_name}"))
        self.stdout.write(f"  slug:        {academy.slug}")
        self.stdout.write(f"  invite_code: {academy.invite_code}")
        self.stdout.write(
            f"  local URL:   http://{academy.slug}.localhost:3000"
        )
