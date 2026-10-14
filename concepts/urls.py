from django.urls import path

from .views import ConceptDetailView, ConceptGraphView, ConceptListView

urlpatterns = [
    path("", ConceptListView.as_view(), name="concept-list"),
    path("<slug:slug>/", ConceptDetailView.as_view(), name="concept-detail"),
    path("<slug:slug>/graph/", ConceptGraphView.as_view(), name="concept-graph"),
]
