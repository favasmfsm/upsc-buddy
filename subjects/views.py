from django.db.models import Count, Prefetch, Q
from rest_framework import generics
from rest_framework.permissions import AllowAny

from academies.mixins import AcademyScopedQuerysetMixin
from academies.utils import require_academy

from .models import Chapter, Section, Subject
from .serializers import (
    ChapterDetailSerializer,
    ChapterListSerializer,
    SectionListSerializer,
    SubjectSerializer,
)


class SubjectListView(AcademyScopedQuerysetMixin, generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.filter(is_active=True)
    pagination_class = None


class SubjectChapterListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ChapterListSerializer
    pagination_class = None

    def get_queryset(self):
        academy = require_academy(self.request)
        subject_slug = self.kwargs["slug"]
        return (
            Chapter.objects.filter(
                subject__academy=academy,
                subject__slug=subject_slug,
                subject__is_active=True,
                is_published=True,
            )
            .select_related("subject", "section")
            .annotate(
                published_concept_count=Count(
                    "concepts",
                    filter=Q(concepts__status="published"),
                )
            )
            .order_by("sort_order", "title")
        )


class SubjectSectionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SectionListSerializer
    pagination_class = None

    def get_queryset(self):
        academy = require_academy(self.request)
        subject_slug = self.kwargs["slug"]
        published_chapters = (
            Chapter.objects.filter(is_published=True)
            .select_related("subject", "section")
            .annotate(
                published_concept_count=Count(
                    "concepts",
                    filter=Q(concepts__status="published"),
                )
            )
            .order_by("sort_order", "title")
        )
        return (
            Section.objects.filter(
                subject__academy=academy,
                subject__slug=subject_slug,
                subject__is_active=True,
                is_published=True,
            )
            .select_related("subject")
            .prefetch_related(
                Prefetch(
                    "chapters",
                    queryset=published_chapters,
                    to_attr="prefetched_published_chapters",
                )
            )
            .order_by("sort_order", "title")
        )


class ChapterDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ChapterDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        academy = require_academy(self.request)
        return (
            Chapter.objects.filter(
                is_published=True,
                subject__academy=academy,
            )
            .select_related("subject", "section")
            .prefetch_related("concepts")
        )
