from django.urls import path

from .views import ProgressListUpdateView, ReviseNextView

urlpatterns = [
    path("progress/", ProgressListUpdateView.as_view(), name="learning-progress"),
    path("revise-next/", ReviseNextView.as_view(), name="learning-revise-next"),
]
