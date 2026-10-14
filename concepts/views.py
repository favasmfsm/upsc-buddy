from collections import deque

from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from academies.utils import require_academy

from .models import Concept, ConceptEdge
from .serializers import (
    ConceptDetailSerializer,
    ConceptListSerializer,
    GraphEdgeSerializer,
    GraphNodeSerializer,
)


class ConceptListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ConceptListSerializer

    def get_queryset(self):
        academy = require_academy(self.request)
        qs = Concept.objects.filter(
            status=Concept.Status.PUBLISHED,
            subject__academy=academy,
        ).select_related("subject", "chapter")
        subject = self.request.query_params.get("subject")
        q = self.request.query_params.get("q")
        if subject:
            qs = qs.filter(subject__slug=subject)
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(summary__icontains=q)
                | Q(slug__icontains=q)
            )
        return qs


class ConceptDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ConceptDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        academy = require_academy(self.request)
        return (
            Concept.objects.filter(
                status=Concept.Status.PUBLISHED,
                subject__academy=academy,
            )
            .select_related("subject", "chapter")
            .prefetch_related(
                "articles",
                "outgoing_edges__target",
                "pyqs",
                "case_laws",
                "amendments",
            )
        )


class ConceptGraphView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        academy = require_academy(request)
        try:
            depth = int(request.query_params.get("depth", 2))
        except (TypeError, ValueError):
            depth = 2
        depth = max(0, min(depth, 4))

        root = (
            Concept.objects.filter(
                status=Concept.Status.PUBLISHED,
                slug=slug,
                subject__academy=academy,
            )
            .select_related("subject")
            .first()
        )
        if not root:
            return Response({"detail": "Not found."}, status=404)

        visited_ids = {root.id}
        frontier = deque([(root.id, 0)])
        edge_ids = set()

        while frontier:
            concept_id, dist = frontier.popleft()
            if dist >= depth:
                continue
            edges = ConceptEdge.objects.filter(
                Q(source_id=concept_id) | Q(target_id=concept_id),
                source__status=Concept.Status.PUBLISHED,
                target__status=Concept.Status.PUBLISHED,
                source__subject__academy=academy,
                target__subject__academy=academy,
            ).select_related("source", "target")
            for edge in edges:
                edge_ids.add(edge.id)
                for other_id in (edge.source_id, edge.target_id):
                    if other_id not in visited_ids:
                        visited_ids.add(other_id)
                        frontier.append((other_id, dist + 1))

        nodes = Concept.objects.filter(id__in=visited_ids).order_by("title")
        edges_qs = ConceptEdge.objects.filter(id__in=edge_ids).select_related(
            "source", "target"
        )
        return Response(
            {
                "root": root.slug,
                "depth": depth,
                "nodes": GraphNodeSerializer(nodes, many=True).data,
                "edges": GraphEdgeSerializer(edges_qs, many=True).data,
            }
        )
