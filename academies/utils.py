from django.http import HttpRequest

from .models import Academy, AcademyMembership

ACADEMY_HEADER = "HTTP_X_ACADEMY_SLUG"


def get_academy_slug_from_request(request: HttpRequest) -> str | None:
    raw = request.META.get(ACADEMY_HEADER) or request.headers.get("X-Academy-Slug")
    if not raw:
        return None
    slug = str(raw).strip().lower()
    return slug or None


def resolve_academy(request: HttpRequest) -> Academy | None:
    """Return active academy from X-Academy-Slug, or None."""
    existing = getattr(request, "academy", None)
    if existing is not None:
        return existing if existing else None

    slug = get_academy_slug_from_request(request)
    if not slug:
        request.academy = None
        return None

    academy = Academy.objects.filter(slug=slug, is_active=True).first()
    request.academy = academy
    return academy


def require_academy(request: HttpRequest) -> Academy:
    academy = resolve_academy(request)
    if academy is None:
        from rest_framework.exceptions import NotFound, ValidationError

        slug = get_academy_slug_from_request(request)
        if not slug:
            raise ValidationError(
                {"detail": "X-Academy-Slug header is required."}
            )
        raise NotFound(detail="Academy not found.")
    return academy


def get_membership(
    user, academy: Academy
) -> AcademyMembership | None:
    if not user or not user.is_authenticated:
        return None
    return (
        AcademyMembership.objects.filter(
            user=user, academy=academy, is_active=True
        )
        .select_related("academy")
        .first()
    )
