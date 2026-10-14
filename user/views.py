from django.conf import settings
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from academies.models import AcademyMembership
from academies.serializers import AcademyBrandingSerializer
from academies.utils import get_membership, require_academy, resolve_academy

from .serializers import (
    CustomTokenObtainPairSerializer,
    JoinAcademySerializer,
    LogOutSerializer,
    SignUpSerializer,
    UserProfileSerializer,
)
from .throttles import LoginRateThrottle, SignupRateThrottle


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    throttle_classes = [LoginRateThrottle]


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [SignupRateThrottle]

    def create(self, request, *args, **kwargs):
        if not settings.ALLOW_PUBLIC_REGISTRATION:
            return Response(
                {"detail": "Public registration is disabled. Use invite join."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserProfileSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class JoinAcademyView(generics.CreateAPIView):
    serializer_class = JoinAcademySerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [SignupRateThrottle]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        academy = require_academy(request)
        membership = get_membership(user, academy)
        refresh = RefreshToken.for_user(user)
        refresh["email"] = user.email
        refresh["academy_id"] = academy.id
        refresh["academy_slug"] = academy.slug
        refresh["role"] = membership.role if membership else "student"
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserProfileSerializer(user).data,
                "academy": AcademyBrandingSerializer(
                    academy, context={"request": request}
                ).data,
                "role": membership.role if membership else "student",
            },
            status=status.HTTP_201_CREATED,
        )


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        academy = resolve_academy(request)
        membership = get_membership(request.user, academy) if academy else None
        role = None
        if membership:
            role = membership.role
        elif request.user.is_superuser and academy:
            role = AcademyMembership.Role.ADMIN
        return Response(
            {
                "user": UserProfileSerializer(request.user).data,
                "academy": (
                    AcademyBrandingSerializer(
                        academy, context={"request": request}
                    ).data
                    if academy
                    else None
                ),
                "role": role,
            }
        )


class LogOutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            token = RefreshToken(serializer.validated_data["refresh"])
            token.blacklist()
        except Exception:
            return Response(
                {"detail": "Invalid refresh token."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)


# Re-export refresh for urls
TokenRefreshView = TokenRefreshView
