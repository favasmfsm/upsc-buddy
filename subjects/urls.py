from django.urls import path

from .views import (
    ChapterDetailView,
    SubjectChapterListView,
    SubjectListView,
    SubjectSectionListView,
)

urlpatterns = [
    path("", SubjectListView.as_view(), name="subject-list"),
    path(
        "<slug:slug>/chapters/",
        SubjectChapterListView.as_view(),
        name="subject-chapter-list",
    ),
    path(
        "<slug:slug>/sections/",
        SubjectSectionListView.as_view(),
        name="subject-section-list",
    ),
]

chapter_urlpatterns = [
    path(
        "<slug:slug>/",
        ChapterDetailView.as_view(),
        name="chapter-detail",
    ),
]
