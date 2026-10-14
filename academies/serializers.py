import re

from rest_framework import serializers

from .models import Academy, AcademyMembership

HEX_COLOR_RE = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def _absolute_media_url(request, url: str) -> str:
    if not url:
        return ""
    if url.startswith("http://") or url.startswith("https://"):
        return url
    if request is not None:
        return request.build_absolute_uri(url)
    return url


class AcademyBrandingSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    favicon_url = serializers.SerializerMethodField()

    class Meta:
        model = Academy
        fields = (
            "id",
            "name",
            "slug",
            "display_name",
            "tagline",
            "logo_url",
            "favicon_url",
            "primary_color",
            "is_active",
        )
        read_only_fields = fields

    def get_logo_url(self, obj: Academy) -> str:
        request = self.context.get("request")
        if obj.logo:
            return _absolute_media_url(request, obj.logo.url)
        return obj.logo_url or ""

    def get_favicon_url(self, obj: Academy) -> str:
        request = self.context.get("request")
        if obj.favicon:
            return _absolute_media_url(request, obj.favicon.url)
        return ""


class AcademyBrandingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academy
        fields = (
            "display_name",
            "tagline",
            "primary_color",
            "logo",
            "favicon",
        )

    def validate_primary_color(self, value: str) -> str:
        if not value:
            return value
        if not HEX_COLOR_RE.fullmatch(value):
            raise serializers.ValidationError(
                "Use a hex color like #1a4d3e or #1a4."
            )
        return value

    def validate_display_name(self, value: str) -> str:
        value = (value or "").strip()
        if not value:
            raise serializers.ValidationError("Display name is required.")
        return value


class AcademyMembershipSerializer(serializers.ModelSerializer):
    academy = AcademyBrandingSerializer(read_only=True)

    class Meta:
        model = AcademyMembership
        fields = ("id", "academy", "role", "is_active")
        read_only_fields = fields
