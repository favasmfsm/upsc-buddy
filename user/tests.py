from datetime import timedelta
from unittest.mock import patch

from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from academies.models import Academy, AcademyMembership

from .models import UserAccount


def _expired_access_for(user) -> AccessToken:
    expired = AccessToken()
    expired["user_id"] = user.id
    # Must be older than SIMPLE_JWT LEEWAY (30s).
    expired.set_exp(lifetime=timedelta(seconds=-120))
    return expired


@patch("user.throttles.LoginRateThrottle.allow_request", return_value=True)
@patch("user.throttles.SignupRateThrottle.allow_request", return_value=True)
class AuthQaTests(TestCase):
    """QA coverage for login, logout, access timeout, and refresh."""

    def setUp(self):
        self.client = APIClient()
        self.academy, _ = Academy.objects.get_or_create(
            slug="fortuneias",
            defaults={
                "name": "Fortune IAS",
                "invite_code": "FORTUNE01",
            },
        )
        # Ensure a known invite code for join tests.
        if self.academy.invite_code != "FORTUNE01":
            self.academy.invite_code = "FORTUNE01"
            self.academy.save(update_fields=["invite_code", "updated_at"])
        self.user = UserAccount.objects.create_user(
            email="student@example.com",
            password="securepass123",
            username="student",
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.user,
            role=AcademyMembership.Role.STUDENT,
            is_active=True,
        )
        self.outsider = UserAccount.objects.create_user(
            email="outsider@example.com",
            password="securepass123",
            username="outsider",
        )
        self.headers = {"HTTP_X_ACADEMY_SLUG": self.academy.slug}

    def _login(self, email="student@example.com", password="securepass123"):
        return self.client.post(
            reverse("token_obtain_pair"),
            {"email": email, "password": password},
            format="json",
            **self.headers,
        )

    def test_login_returns_tokens_user_role_and_academy(self, *_mocks):
        response = self._login()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["role"], AcademyMembership.Role.STUDENT)
        self.assertEqual(response.data["academy"]["slug"], self.academy.slug)
        self.assertEqual(response.data["user"]["email"], "student@example.com")

    def test_login_requires_academy_header(self, *_mocks):
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "student@example.com", "password": "securepass123"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_rejects_wrong_password(self, *_mocks):
        response = self._login(password="wrong-password")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_rejects_user_without_membership(self, *_mocks):
        response = self._login(email="outsider@example.com")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("membership", str(response.data).lower())

    def test_login_rejects_inactive_membership(self, *_mocks):
        AcademyMembership.objects.filter(user=self.user).update(is_active=False)
        response = self._login()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_requires_auth(self, *_mocks):
        response = self.client.get(reverse("profile"), **self.headers)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_with_valid_access_token(self, *_mocks):
        tokens = self._login().data
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
        response = self.client.get(reverse("profile"), **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"]["email"], "student@example.com")
        self.assertEqual(response.data["role"], AcademyMembership.Role.STUDENT)

    def test_expired_access_token_is_rejected(self, *_mocks):
        expired = _expired_access_for(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {expired}")
        response = self.client.get(reverse("profile"), **self.headers)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_issues_new_access_after_access_expires(self, *_mocks):
        tokens = self._login().data
        self.assertIn("refresh", tokens)

        expired = _expired_access_for(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {expired}")
        self.assertEqual(
            self.client.get(reverse("profile"), **self.headers).status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

        refresh_response = self.client.post(
            reverse("token_refresh"),
            {"refresh": tokens["refresh"]},
            format="json",
        )
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh_response.data['access']}"
        )
        me = self.client.get(reverse("profile"), **self.headers)
        self.assertEqual(me.status_code, status.HTTP_200_OK)

    def test_refresh_rotates_and_blacklists_old_refresh(self, *_mocks):
        tokens = self._login().data
        self.assertIn("refresh", tokens)
        first = self.client.post(
            reverse("token_refresh"),
            {"refresh": tokens["refresh"]},
            format="json",
        )
        self.assertEqual(first.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", first.data)

        reuse_old = self.client.post(
            reverse("token_refresh"),
            {"refresh": tokens["refresh"]},
            format="json",
        )
        self.assertEqual(reuse_old.status_code, status.HTTP_401_UNAUTHORIZED)

        second = self.client.post(
            reverse("token_refresh"),
            {"refresh": first.data["refresh"]},
            format="json",
        )
        self.assertEqual(second.status_code, status.HTTP_200_OK)

    def test_logout_blacklists_refresh_token(self, *_mocks):
        tokens = self._login().data
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")

        logout = self.client.post(
            reverse("logout"),
            {"refresh": tokens["refresh"]},
            format="json",
        )
        self.assertEqual(logout.status_code, status.HTTP_204_NO_CONTENT)

        refresh_after = self.client.post(
            reverse("token_refresh"),
            {"refresh": tokens["refresh"]},
            format="json",
        )
        self.assertEqual(refresh_after.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_requires_authentication(self, *_mocks):
        tokens = self._login().data
        self.client.credentials()
        response = self.client.post(
            reverse("logout"),
            {"refresh": tokens["refresh"]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_rejects_invalid_refresh(self, *_mocks):
        tokens = self._login().data
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
        response = self.client.post(
            reverse("logout"),
            {"refresh": "not-a-valid-refresh-token"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_access_lifetime_setting_is_thirty_minutes(self, *_mocks):
        from django.conf import settings

        self.assertEqual(
            settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            timedelta(minutes=30),
        )
        self.assertEqual(
            settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
            timedelta(days=7),
        )

    def test_fresh_access_token_exp_matches_configured_lifetime(self, *_mocks):
        tokens = self._login().data
        access = AccessToken(tokens["access"])
        lifetime = access["exp"] - access["iat"]
        self.assertAlmostEqual(lifetime, 30 * 60, delta=5)

    @override_settings(ALLOW_PUBLIC_REGISTRATION=False)
    def test_public_signup_disabled_by_default(self, *_mocks):
        response = self.client.post(
            reverse("signup"),
            {
                "email": "new@example.com",
                "password": "securepass123",
                "first_name": "New",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(UserAccount.objects.filter(email="new@example.com").exists())

    def test_join_returns_tokens_and_membership(self, *_mocks):
        response = self.client.post(
            reverse("join_academy"),
            {
                "email": "joined@example.com",
                "password": "securepass123",
                "invite_code": "FORTUNE01",
            },
            format="json",
            **self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["role"], AcademyMembership.Role.STUDENT)
        self.assertTrue(
            AcademyMembership.objects.filter(
                user__email="joined@example.com",
                academy=self.academy,
                is_active=True,
            ).exists()
        )

    def test_refresh_token_lifetime_allows_session_after_access_expiry(
        self, *_mocks
    ):
        """Documents intended session model: short access, long refresh."""
        refresh = RefreshToken.for_user(self.user)
        refresh_lifetime = refresh["exp"] - refresh["iat"]
        access_lifetime = refresh.access_token["exp"] - refresh.access_token["iat"]
        self.assertGreater(refresh_lifetime, access_lifetime)
        self.assertAlmostEqual(refresh_lifetime, 7 * 24 * 60 * 60, delta=5)
