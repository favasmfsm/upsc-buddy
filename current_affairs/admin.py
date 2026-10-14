from datetime import date

from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html

from academies.models import Academy

from .models import CADocument, CAQuestion, QuizAttempt, QuizAttemptAnswer
from .services.finder_ingest import FINDER_SYNC_MAX_DAYS, inclusive_day_count


class CAQuestionInline(admin.TabularInline):
    model = CAQuestion
    extra = 0
    fields = (
        "sort_order",
        "stem",
        "option_a",
        "option_b",
        "option_c",
        "option_d",
        "correct_option",
        "subject_tag",
        "is_published",
    )
    show_change_link = True


@admin.register(CADocument)
class CADocumentAdmin(admin.ModelAdmin):
    change_list_template = "admin/current_affairs/cadocument/change_list.html"
    list_display = (
        "title",
        "academy",
        "doc_type",
        "source_date",
        "status",
        "question_count",
        "generated_at",
        "updated_at",
    )
    list_filter = ("academy", "doc_type", "status")
    search_fields = ("title",)
    readonly_fields = (
        "period_start",
        "period_end",
        "status",
        "error_message",
        "gemini_model",
        "generated_at",
        "created_at",
        "updated_at",
        "questions_link",
    )
    actions = ["regenerate_questions"]
    inlines = [CAQuestionInline]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "academy",
                    "doc_type",
                    "title",
                    "source_date",
                    "file",
                )
            },
        ),
        (
            "Period (auto)",
            {"fields": ("period_start", "period_end")},
        ),
        (
            "Generation",
            {
                "fields": (
                    "status",
                    "error_message",
                    "gemini_model",
                    "generated_at",
                    "questions_link",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "finder-sync/",
                self.admin_site.admin_view(self.finder_sync_view),
                name="current_affairs_cadocument_finder_sync",
            ),
        ]
        return custom + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["finder_academies"] = Academy.objects.order_by("name")
        return super().changelist_view(request, extra_context=extra_context)

    def finder_sync_view(self, request):
        changelist_url = reverse("admin:current_affairs_cadocument_changelist")
        if request.method != "POST":
            return HttpResponseRedirect(changelist_url)

        academy_id = request.POST.get("academy_id")
        start_raw = request.POST.get("start", "").strip()
        end_raw = request.POST.get("end", "").strip()
        regenerate = request.POST.get("regenerate") == "1"

        try:
            academy = Academy.objects.get(pk=academy_id)
        except (Academy.DoesNotExist, ValueError, TypeError):
            self.message_user(request, "Select a valid academy.", messages.ERROR)
            return HttpResponseRedirect(changelist_url)

        try:
            start = date.fromisoformat(start_raw)
            end = date.fromisoformat(end_raw)
        except ValueError:
            self.message_user(
                request, "From and To must be valid dates (YYYY-MM-DD).", messages.ERROR
            )
            return HttpResponseRedirect(changelist_url)

        if start > end:
            self.message_user(
                request, "From date must be on or before To date.", messages.ERROR
            )
            return HttpResponseRedirect(changelist_url)

        days = inclusive_day_count(start, end)
        if days > FINDER_SYNC_MAX_DAYS:
            self.message_user(
                request,
                f"Date range cannot exceed {FINDER_SYNC_MAX_DAYS} days (got {days}).",
                messages.ERROR,
            )
            return HttpResponseRedirect(changelist_url)

        processing = CADocument.objects.filter(
            academy=academy,
            doc_type=CADocument.DocType.DAILY,
            source_date__gte=start,
            source_date__lte=end,
            status=CADocument.Status.PROCESSING,
        ).exists()
        if processing:
            self.message_user(
                request,
                "One or more documents in this range are currently generating. "
                "Try again when finished.",
                messages.ERROR,
            )
            return HttpResponseRedirect(changelist_url)

        from .tasks import sync_finder_range

        async_result = sync_finder_range.apply_async(
            args=[academy.pk, start.isoformat(), end.isoformat()],
            kwargs={"regenerate": regenerate},
        )
        mode = "fill + regenerate" if regenerate else "fill gaps"
        self.message_user(
            request,
            (
                f"Queued FINDER sync ({mode}) for {academy.slug}: "
                f"{start.isoformat()} → {end.isoformat()} "
                f"({days} day(s), task {async_result.id})."
            ),
            messages.SUCCESS,
        )
        return HttpResponseRedirect(changelist_url)

    @admin.display(description="Questions")
    def question_count(self, obj):
        return obj.questions.count()

    @admin.display(description="Questions admin")
    def questions_link(self, obj):
        if not obj.pk:
            return "—"
        return format_html(
            '<a href="/admin/current_affairs/caquestion/?document__id__exact={}">'
            "View {} questions</a>",
            obj.pk,
            obj.questions.count(),
        )

    @admin.action(description="Regenerate questions (Gemini)")
    def regenerate_questions(self, request, queryset):
        from .signals import _enqueue

        for doc in queryset:
            CADocument.objects.filter(pk=doc.pk).update(
                status=CADocument.Status.PENDING,
                error_message="",
            )
            _enqueue(doc.pk, force=True)
        self.message_user(
            request,
            f"Queued regeneration for {queryset.count()} document(s).",
            messages.SUCCESS,
        )


@admin.register(CAQuestion)
class CAQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "short_stem",
        "document",
        "subject_tag",
        "correct_option",
        "is_published",
        "sort_order",
    )
    list_filter = ("is_published", "subject_tag", "document__doc_type", "document")
    search_fields = ("stem", "source_topic", "subject_tag", "document__title")
    list_editable = ("is_published", "sort_order")
    autocomplete_fields = ()
    raw_id_fields = ("document",)
    actions = ["publish_selected", "unpublish_selected"]

    @admin.display(description="Stem")
    def short_stem(self, obj):
        return obj.stem[:72]

    @admin.action(description="Publish selected")
    def publish_selected(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"Published {updated} question(s).", messages.SUCCESS)

    @admin.action(description="Unpublish selected")
    def unpublish_selected(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(
            request, f"Unpublished {updated} question(s).", messages.SUCCESS
        )


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "academy",
        "mode",
        "period_start",
        "period_end",
        "score",
        "total",
        "completed_at",
        "created_at",
    )
    list_filter = ("academy", "mode")
    search_fields = ("user__email",)
    readonly_fields = (
        "user",
        "academy",
        "mode",
        "period_start",
        "period_end",
        "question_ids",
        "answers",
        "score",
        "total",
        "completed_at",
        "created_at",
        "updated_at",
    )


@admin.register(QuizAttemptAnswer)
class QuizAttemptAnswerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "attempt",
        "question",
        "selected_option",
        "is_correct",
        "subject_tag",
        "source_topic",
    )
    list_filter = ("is_correct", "subject_tag")
    search_fields = ("source_topic", "attempt__user__email")
    raw_id_fields = ("attempt", "question")
    readonly_fields = (
        "attempt",
        "question",
        "selected_option",
        "is_correct",
        "subject_tag",
        "source_topic",
        "created_at",
    )
