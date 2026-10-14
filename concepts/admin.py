from django.contrib import admin

from .models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)


class ConceptArticleInline(admin.TabularInline):
    model = ConceptArticle
    extra = 0


class ConceptEdgeOutgoingInline(admin.TabularInline):
    model = ConceptEdge
    fk_name = "source"
    extra = 0
    verbose_name = "Outgoing edge"
    verbose_name_plural = "Outgoing edges"


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subject",
        "chapter",
        "sort_order",
        "slug",
        "status",
        "updated_at",
    )
    list_filter = ("subject", "chapter", "status")
    search_fields = ("title", "slug", "summary")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("subject", "chapter")
    inlines = [ConceptArticleInline, ConceptEdgeOutgoingInline]


@admin.register(ConceptEdge)
class ConceptEdgeAdmin(admin.ModelAdmin):
    list_display = ("source", "relation_type", "target")
    list_filter = ("relation_type",)
    search_fields = ("source__title", "target__title")
    autocomplete_fields = ("source", "target")


@admin.register(ConceptArticle)
class ConceptArticleAdmin(admin.ModelAdmin):
    list_display = ("ref", "concept", "sort_order")
    search_fields = ("ref", "concept__title")
    autocomplete_fields = ("concept",)


@admin.register(CaseLaw)
class CaseLawAdmin(admin.ModelAdmin):
    list_display = ("title", "academy", "year", "court", "updated_at")
    list_filter = ("academy", "court", "year")
    search_fields = ("title", "slug", "parties", "holding")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("concepts",)
    autocomplete_fields = ("academy",)


@admin.register(ConstitutionalAmendment)
class ConstitutionalAmendmentAdmin(admin.ModelAdmin):
    list_display = ("number", "year", "title", "academy", "updated_at")
    list_filter = ("academy", "year")
    search_fields = ("title", "summary", "effect")
    filter_horizontal = ("concepts",)
    autocomplete_fields = ("academy",)
