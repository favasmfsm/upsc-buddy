from rest_framework import serializers

from concepts.models import Concept

from .models import Chapter, Section, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", "slug", "description", "sort_order", "is_active")


class ChapterListSerializer(serializers.ModelSerializer):
    subject_slug = serializers.CharField(source="subject.slug", read_only=True)
    section_slug = serializers.SerializerMethodField()
    section_title = serializers.SerializerMethodField()
    concept_count = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = (
            "id",
            "title",
            "slug",
            "sort_order",
            "book_ref",
            "summary",
            "is_published",
            "subject_slug",
            "section_slug",
            "section_title",
            "concept_count",
            "updated_at",
        )

    def get_section_slug(self, obj):
        return obj.section.slug if obj.section_id else None

    def get_section_title(self, obj):
        return obj.section.title if obj.section_id else None

    def get_concept_count(self, obj):
        if hasattr(obj, "published_concept_count"):
            return obj.published_concept_count
        return obj.concepts.filter(status=Concept.Status.PUBLISHED).count()


class ChapterConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ("id", "title", "slug", "summary", "sort_order")


class ChapterDetailSerializer(serializers.ModelSerializer):
    subject_slug = serializers.CharField(source="subject.slug", read_only=True)
    section_slug = serializers.SerializerMethodField()
    section_title = serializers.SerializerMethodField()
    concepts = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = (
            "id",
            "title",
            "slug",
            "sort_order",
            "book_ref",
            "summary",
            "is_published",
            "subject_slug",
            "section_slug",
            "section_title",
            "concepts",
            "created_at",
            "updated_at",
        )

    def get_section_slug(self, obj):
        return obj.section.slug if obj.section_id else None

    def get_section_title(self, obj):
        return obj.section.title if obj.section_id else None

    def get_concepts(self, obj):
        qs = obj.concepts.filter(status=Concept.Status.PUBLISHED).order_by(
            "sort_order", "title"
        )
        return ChapterConceptSerializer(qs, many=True).data


class SectionListSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = (
            "id",
            "title",
            "slug",
            "sort_order",
            "summary",
            "is_published",
            "chapters",
        )

    def get_chapters(self, obj):
        chapters = getattr(obj, "prefetched_published_chapters", None)
        if chapters is None:
            chapters = (
                obj.chapters.filter(is_published=True)
                .select_related("subject", "section")
                .order_by("sort_order", "title")
            )
        return ChapterListSerializer(chapters, many=True).data
