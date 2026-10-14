from django.contrib import admin

from .models import Academy, AcademyMembership


@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "display_name",
        "invite_code",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "slug", "display_name", "invite_code")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "display_name",
                    "tagline",
                    "invite_code",
                    "is_active",
                )
            },
        ),
        (
            "Branding",
            {
                "fields": (
                    "logo",
                    "logo_url",
                    "favicon",
                    "primary_color",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


@admin.register(AcademyMembership)
class AcademyMembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "academy", "role", "is_active", "created_at")
    list_filter = ("role", "is_active", "academy")
    search_fields = ("user__email", "academy__slug", "academy__name")
    autocomplete_fields = ("user", "academy")
    readonly_fields = ("created_at", "updated_at")
