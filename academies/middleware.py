from .utils import resolve_academy


class AcademyMiddleware:
    """Attach request.academy from X-Academy-Slug (may be None)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolve_academy(request)
        return self.get_response(request)
