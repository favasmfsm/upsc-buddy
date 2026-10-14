from django.db.models import Count

from rest_framework import serializers

from questions.serializers import PYQSerializer

from .models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)

ALLOWED_BLOCK_TYPES = frozenset(
    {
        "markdown",
        "map",
        "image",
        "annotated_image",
        "flowchart",
        "comparison",
        "callout",
        "mental_model",
        "pillars",
        "pyq_heatmap",
        "tree",
        "timeline",
        "relation_graph",
        "journey",
        "article_explorer",
        "case_network",
        "memory_palace",
        "simulator",
    }
)


def validate_visual_blocks(blocks):
    """Light shape check; returns sanitized list or raises ValidationError."""
    if blocks is None:
        return []
    if not isinstance(blocks, list):
        raise serializers.ValidationError("visual_blocks must be a list.")
    cleaned = []
    for i, block in enumerate(blocks):
        if not isinstance(block, dict):
            raise serializers.ValidationError(
                f"visual_blocks[{i}] must be an object."
            )
        block_id = block.get("id")
        block_type = block.get("type")
        if not block_id or not isinstance(block_id, str):
            raise serializers.ValidationError(
                f"visual_blocks[{i}] requires a string id."
            )
        if block_type not in ALLOWED_BLOCK_TYPES:
            raise serializers.ValidationError(
                f"visual_blocks[{i}] type must be one of "
                f"{sorted(ALLOWED_BLOCK_TYPES)}."
            )
        cleaned.append(block)
    return cleaned


def enrich_visual_blocks(blocks, subject):
    """Attach live PYQ counts to pyq_heatmap blocks."""
    if not isinstance(blocks, list):
        return []
    enriched = []
    for block in blocks:
        if not isinstance(block, dict):
            continue
        if (
            not isinstance(block.get("id"), str)
            or block.get("type") not in ALLOWED_BLOCK_TYPES
        ):
            continue
        if block.get("type") != "pyq_heatmap":
            enriched.append(block)
            continue

        items = block.get("items") or []
        if not isinstance(items, list):
            enriched.append({**block, "items": []})
            continue

        slugs = [
            item.get("concept_slug")
            for item in items
            if isinstance(item, dict) and isinstance(item.get("concept_slug"), str)
        ]
        counts = {
            row["slug"]: row["pyq_count"]
            for row in Concept.objects.filter(subject=subject, slug__in=slugs)
            .annotate(pyq_count=Count("pyqs", distinct=True))
            .values("slug", "pyq_count")
        }
        enriched_items = []
        for item in items:
            if not isinstance(item, dict):
                continue
            slug = item.get("concept_slug")
            enriched_items.append(
                {
                    **item,
                    "count": counts.get(slug, 0) if isinstance(slug, str) else 0,
                }
            )
        enriched.append({**block, "items": enriched_items})
    return enriched


class ConceptArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptArticle
        fields = ("id", "ref", "excerpt", "sort_order")


class RelatedConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ("id", "title", "slug", "summary")


class ConceptEdgeSerializer(serializers.ModelSerializer):
    target = RelatedConceptSerializer(read_only=True)

    class Meta:
        model = ConceptEdge
        fields = ("id", "relation_type", "target")


class CaseLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseLaw
        fields = (
            "id",
            "title",
            "slug",
            "parties",
            "year",
            "court",
            "summary",
            "holding",
        )


class ConstitutionalAmendmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstitutionalAmendment
        fields = (
            "id",
            "number",
            "year",
            "title",
            "summary",
            "effect",
        )


class ConceptListSerializer(serializers.ModelSerializer):
    subject_slug = serializers.CharField(source="subject.slug", read_only=True)
    chapter_slug = serializers.CharField(
        source="chapter.slug", read_only=True, allow_null=True
    )

    class Meta:
        model = Concept
        fields = (
            "id",
            "title",
            "slug",
            "summary",
            "subject_slug",
            "chapter_slug",
            "sort_order",
            "status",
            "updated_at",
        )


class ConceptDetailSerializer(serializers.ModelSerializer):
    subject_slug = serializers.CharField(source="subject.slug", read_only=True)
    chapter_slug = serializers.CharField(
        source="chapter.slug", read_only=True, allow_null=True
    )
    chapter_title = serializers.CharField(
        source="chapter.title", read_only=True, allow_null=True
    )
    articles = ConceptArticleSerializer(many=True, read_only=True)
    related = serializers.SerializerMethodField()
    pyqs = serializers.SerializerMethodField()
    visual_blocks = serializers.SerializerMethodField()
    case_laws = CaseLawSerializer(many=True, read_only=True)
    amendments = ConstitutionalAmendmentSerializer(many=True, read_only=True)

    class Meta:
        model = Concept
        fields = (
            "id",
            "title",
            "slug",
            "summary",
            "body",
            "visual_blocks",
            "subject_slug",
            "chapter_slug",
            "chapter_title",
            "sort_order",
            "status",
            "articles",
            "related",
            "pyqs",
            "case_laws",
            "amendments",
            "created_at",
            "updated_at",
        )

    def get_visual_blocks(self, obj):
        return enrich_visual_blocks(obj.visual_blocks or [], obj.subject)

    def get_related(self, obj):
        edges = obj.outgoing_edges.select_related("target").all()
        return ConceptEdgeSerializer(edges, many=True).data

    def get_pyqs(self, obj):
        return PYQSerializer(obj.pyqs.all(), many=True).data


class GraphNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ("id", "title", "slug", "summary")


class GraphEdgeSerializer(serializers.ModelSerializer):
    source_slug = serializers.CharField(source="source.slug", read_only=True)
    target_slug = serializers.CharField(source="target.slug", read_only=True)

    class Meta:
        model = ConceptEdge
        fields = ("id", "source_slug", "target_slug", "relation_type")
