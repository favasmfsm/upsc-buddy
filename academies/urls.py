from django.urls import path

from .views import AcademyBrandingView, CurrentAcademyView

urlpatterns = [
    path("current/", CurrentAcademyView.as_view(), name="academy-current"),
    path(
        "current/branding/",
        AcademyBrandingView.as_view(),
        name="academy-current-branding",
    ),
]
