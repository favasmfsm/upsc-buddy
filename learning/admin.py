from django.contrib import admin

from .models import UserConceptProgress


@admin.register(UserConceptProgress)
class UserConceptProgressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "academy",
        "concept",
        "status",
        "is_difficult",
        "last_studied_at",
        "updated_at",
    )
    list_filter = ("academy", "status", "is_difficult")
    search_fields = ("user__email", "concept__title")
    autocomplete_fields = ("user", "concept", "academy")
