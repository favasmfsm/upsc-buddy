from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from academies.utils import require_academy
from concepts.models import Concept
from concepts.serializers import ConceptListSerializer

from .models import UserConceptProgress
from .serializers import ProgressSerializer, ProgressUpdateSerializer


class ProgressListUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        academy = require_academy(request)
        qs = (
            UserConceptProgress.objects.filter(user=request.user, academy=academy)
            .filter(
                Q(is_difficult=True)
                | ~Q(status=UserConceptProgress.Status.NOT_STARTED)
            )
            .select_related("concept")
        )
        return Response(ProgressSerializer(qs, many=True).data)

    def patch(self, request):
        require_academy(request)
        serializer = ProgressUpdateSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        progress = serializer.save()
        return Response(ProgressSerializer(progress).data, status=status.HTTP_200_OK)


class ReviseNextView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConceptListSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        academy = require_academy(self.request)
        progress = {
            p.concept_id: p
            for p in UserConceptProgress.objects.filter(
                user=user, academy=academy
            ).select_related("concept")
        }
        published = list(
            Concept.objects.filter(
                status=Concept.Status.PUBLISHED,
                subject__academy=academy,
            ).select_related("subject")
        )

        revise = []
        not_started = []
        for concept in published:
            p = progress.get(concept.id)
            if p and p.status == UserConceptProgress.Status.REVISE_LATER:
                revise.append(concept)
            elif not p or p.status == UserConceptProgress.Status.NOT_STARTED:
                not_started.append(concept)

        return (revise + not_started)[:24]

    def list(self, request, *args, **kwargs):
        academy = require_academy(request)
        concepts = self.get_queryset()
        progress_map = {
            p.concept_id: p
            for p in UserConceptProgress.objects.filter(
                user=request.user,
                academy=academy,
                concept_id__in=[c.id for c in concepts],
            )
        }
        data = ConceptListSerializer(concepts, many=True).data
        for item, concept in zip(data, concepts):
            p = progress_map.get(concept.id)
            item["progress_status"] = (
                p.status if p else UserConceptProgress.Status.NOT_STARTED
            )
            item["is_difficult"] = bool(p and p.is_difficult)
        return Response(data)
