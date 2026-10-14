from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from academies.models import AcademyMembership
from academies.serializers import AcademyBrandingSerializer
from academies.utils import get_membership, require_academy

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        request = self.context.get("request")
        academy = require_academy(request)
        membership = get_membership(self.user, academy)
        if membership is None and not self.user.is_superuser:
            raise AuthenticationFailed(
                "No active membership for this academy."
            )
        role = (
            membership.role
            if membership
            else AcademyMembership.Role.ADMIN
        )
        refresh = self.get_token(self.user)
        refresh["academy_id"] = academy.id
        refresh["academy_slug"] = academy.slug
        refresh["role"] = role
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = UserProfileSerializer(self.user).data
        data["academy"] = AcademyBrandingSerializer(
            academy, context=self.context
        ).data
        data["role"] = role
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "email_verified",
            "date_joined",
        )
        read_only_fields = fields


class MeSerializer(serializers.Serializer):
    user = UserProfileSerializer()
    academy = AcademyBrandingSerializer(allow_null=True)
    role = serializers.CharField(allow_null=True)


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    username = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name", "username")

    def validate(self, attrs):
        if not settings.ALLOW_PUBLIC_REGISTRATION:
            raise serializers.ValidationError("Public registration is disabled.")
        return attrs

    def create(self, validated_data):
        username = validated_data.get("username") or validated_data["email"]
        return User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=username,
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )


class JoinAcademySerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    invite_code = serializers.CharField(max_length=32)
    username = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        request = self.context["request"]
        academy = require_academy(request)
        code = attrs["invite_code"].strip().upper()
        if academy.invite_code.upper() != code:
            raise serializers.ValidationError(
                {"invite_code": "Invalid invite code for this academy."}
            )
        email = attrs["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                {"email": "An account with this email already exists. Log in instead."}
            )
        attrs["academy"] = academy
        attrs["email"] = email
        attrs["invite_code"] = code
        return attrs

    def create(self, validated_data):
        academy = validated_data.pop("academy")
        validated_data.pop("invite_code")
        username = validated_data.get("username") or validated_data["email"]
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=username,
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        AcademyMembership.objects.create(
            academy=academy,
            user=user,
            role=AcademyMembership.Role.STUDENT,
            is_active=True,
        )
        return user


class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
