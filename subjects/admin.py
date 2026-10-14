from django.contrib import admin

from .models import Chapter, Section, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("sort_order", "name", "slug", "academy", "is_active", "updated_at")
    list_filter = ("academy", "is_active")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ("academy",)
    ordering = ("sort_order", "name")


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "sort_order",
        "title",
        "subject",
        "slug",
        "is_published",
        "updated_at",
    )
    list_filter = ("subject", "is_published")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("subject",)
    ordering = ("sort_order", "title")


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        "sort_order",
        "title",
        "subject",
        "section",
        "slug",
        "is_published",
        "updated_at",
    )
    list_filter = ("subject", "section", "is_published")
    search_fields = ("title", "slug", "book_ref")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("subject", "section")
    ordering = ("sort_order", "title")
