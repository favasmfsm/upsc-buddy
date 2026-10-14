from django.contrib import admin

from .models import PYQ


@admin.register(PYQ)
class PYQAdmin(admin.ModelAdmin):
    list_display = ("year", "short_question", "academy", "updated_at")
    list_filter = ("academy", "year")
    search_fields = ("question", "answer_key")
    filter_horizontal = ("concepts",)
    autocomplete_fields = ("academy",)

    @admin.display(description="Question")
    def short_question(self, obj):
        return obj.question[:80]
