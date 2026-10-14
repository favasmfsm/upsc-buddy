from academies.utils import require_academy


class AcademyScopedQuerysetMixin:
    """Filter queryset by request.academy; requires X-Academy-Slug."""

    academy_lookup = "academy"

    def get_academy(self):
        return require_academy(self.request)

    def filter_by_academy(self, qs):
        academy = self.get_academy()
        return qs.filter(**{self.academy_lookup: academy})

    def get_queryset(self):
        qs = super().get_queryset()
        return self.filter_by_academy(qs)
