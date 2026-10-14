from academies.models import Academy

DEFAULT_ACADEMY_SLUG = "fortuneias"


def get_academy_or_fail(slug: str = DEFAULT_ACADEMY_SLUG) -> Academy:
    academy = Academy.objects.filter(slug=slug).first()
    if academy is None:
        raise SystemExit(
            f"Academy '{slug}' not found. Run: "
            f"python manage.py seed_academy_fortuneias"
        )
    return academy
