from django.urls import path

from .views import (
    AcademyAnalyticsView,
    AcademyStudentAnalyticsView,
    AttemptListView,
    DocumentListView,
    MyAnalyticsView,
    QuizDetailView,
    QuizStartView,
    QuizSubmitView,
    StaffDocumentDetailView,
    StaffDocumentListCreateView,
    StaffDocumentQuestionsView,
    StaffDocumentRegenerateView,
    StaffFinderSyncView,
    StaffQuestionPatchView,
)

urlpatterns = [
    path("documents/", DocumentListView.as_view(), name="ca-documents"),
    path("quizzes/start/", QuizStartView.as_view(), name="ca-quiz-start"),
    path("quizzes/<int:pk>/", QuizDetailView.as_view(), name="ca-quiz-detail"),
    path(
        "quizzes/<int:pk>/submit/",
        QuizSubmitView.as_view(),
        name="ca-quiz-submit",
    ),
    path("attempts/", AttemptListView.as_view(), name="ca-attempts"),
    path("analytics/me/", MyAnalyticsView.as_view(), name="ca-analytics-me"),
    path(
        "analytics/academy/",
        AcademyAnalyticsView.as_view(),
        name="ca-analytics-academy",
    ),
    path(
        "analytics/academy/students/<int:user_id>/",
        AcademyStudentAnalyticsView.as_view(),
        name="ca-analytics-academy-student",
    ),
    path(
        "staff/documents/",
        StaffDocumentListCreateView.as_view(),
        name="ca-staff-documents",
    ),
    path(
        "staff/documents/<int:pk>/",
        StaffDocumentDetailView.as_view(),
        name="ca-staff-document-detail",
    ),
    path(
        "staff/documents/<int:pk>/regenerate/",
        StaffDocumentRegenerateView.as_view(),
        name="ca-staff-document-regenerate",
    ),
    path(
        "staff/finder/sync/",
        StaffFinderSyncView.as_view(),
        name="ca-staff-finder-sync",
    ),
    path(
        "staff/documents/<int:pk>/questions/",
        StaffDocumentQuestionsView.as_view(),
        name="ca-staff-document-questions",
    ),
    path(
        "staff/questions/<int:pk>/",
        StaffQuestionPatchView.as_view(),
        name="ca-staff-question-patch",
    ),
]
