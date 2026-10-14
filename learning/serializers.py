from django.utils import timezone
from rest_framework import serializers

from concepts.models import Concept

from .models import UserConceptProgress


class ProgressSerializer(serializers.ModelSerializer):
    concept_slug = serializers.SlugField(source="concept.slug", read_only=True)
    concept_title = serializers.CharField(source="concept.title", read_only=True)

    class Meta:
        model = UserConceptProgress
        fields = (
            "id",
            "concept",
            "concept_slug",
            "concept_title",
            "status",
            "is_difficult",
            "last_studied_at",
            "updated_at",
        )
        read_only_fields = ("id", "last_studied_at", "updated_at")


class ProgressUpdateSerializer(serializers.Serializer):
    concept_slug = serializers.SlugField()
    status = serializers.ChoiceField(
        choices=UserConceptProgress.Status.choices, required=False
    )
    is_difficult = serializers.BooleanField(required=False)

    def validate(self, attrs):
        if "status" not in attrs and "is_difficult" not in attrs:
            raise serializers.ValidationError(
                "Provide status and/or is_difficult."
            )
        return attrs

    def validate_concept_slug(self, value):
        from academies.utils import require_academy

        academy = require_academy(self.context["request"])
        concept = Concept.objects.filter(
            slug=value,
            status=Concept.Status.PUBLISHED,
            subject__academy=academy,
        ).first()
        if not concept:
            raise serializers.ValidationError("Concept not found.")
        self.context["concept"] = concept
        self.context["academy"] = academy
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        concept = self.context["concept"]
        academy = self.context["academy"]
        progress, _ = UserConceptProgress.objects.get_or_create(
            user=user,
            academy=academy,
            concept=concept,
            defaults={"status": UserConceptProgress.Status.NOT_STARTED},
        )
        update_fields = []
        if "status" in self.validated_data:
            status = self.validated_data["status"]
            progress.status = status
            if status == UserConceptProgress.Status.STUDIED:
                progress.last_studied_at = timezone.now()
                update_fields.extend(["status", "last_studied_at", "updated_at"])
            else:
                update_fields.extend(["status", "updated_at"])
        if "is_difficult" in self.validated_data:
            progress.is_difficult = self.validated_data["is_difficult"]
            update_fields.extend(["is_difficult", "updated_at"])
        if update_fields:
            progress.save(update_fields=list(dict.fromkeys(update_fields)))
        return progress


class ReviseNextSerializer(serializers.ModelSerializer):
    concept_slug = serializers.SlugField(source="concept.slug", read_only=True)
    concept_title = serializers.CharField(source="concept.title", read_only=True)
    summary = serializers.CharField(source="concept.summary", read_only=True)

    class Meta:
        model = UserConceptProgress
        fields = (
            "concept_slug",
            "concept_title",
            "summary",
            "status",
            "is_difficult",
            "last_studied_at",
        )
