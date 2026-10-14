from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from academies.models import Academy, AcademyMembership
from user.models import UserAccount


class AcademyBrandingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.academy = Academy.objects.create(
            name="Test Academy",
            slug="testacademy",
            invite_code="TESTCODE01",
        )
        self.admin = UserAccount.objects.create_user(
            email="admin@example.com",
            password="securepass123",
            username="admin",
        )
        self.staff = UserAccount.objects.create_user(
            email="staff@example.com",
            password="securepass123",
            username="staff",
        )
        self.student = UserAccount.objects.create_user(
            email="student@example.com",
            password="securepass123",
            username="student",
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.admin,
            role=AcademyMembership.Role.ADMIN,
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.staff,
            role=AcademyMembership.Role.STAFF,
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.student,
            role=AcademyMembership.Role.STUDENT,
        )
        self.headers = {"HTTP_X_ACADEMY_SLUG": self.academy.slug}
        self.url = reverse("academy-current-branding")
        self.public_url = reverse("academy-current")

    def _auth(self, user):
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")

    def test_public_current_includes_branding_fields(self):
        response = self.client.get(self.public_url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("tagline", response.data)
        self.assertIn("favicon_url", response.data)
        self.assertIn("logo_url", response.data)

    def test_admin_can_patch_branding_text(self):
        self._auth(self.admin)
        response = self.client.patch(
            self.url,
            {
                "display_name": "Renamed Academy",
                "tagline": "Learn visually",
                "primary_color": "#1a4d3e",
            },
            format="multipart",
            **self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display_name"], "Renamed Academy")
        self.assertEqual(response.data["tagline"], "Learn visually")
        self.assertEqual(response.data["primary_color"], "#1a4d3e")
        self.academy.refresh_from_db()
        self.assertEqual(self.academy.display_name, "Renamed Academy")

    def test_staff_cannot_patch_branding(self):
        self._auth(self.staff)
        response = self.client.patch(
            self.url,
            {"tagline": "Nope"},
            format="multipart",
            **self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_student_cannot_get_branding_admin(self):
        self._auth(self.student)
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid_primary_color_rejected(self):
        self._auth(self.admin)
        response = self.client.patch(
            self.url,
            {"primary_color": "red"},
            format="multipart",
            **self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_admin_can_upload_logo(self):
        self._auth(self.admin)
        from io import BytesIO

        from PIL import Image

        buf = BytesIO()
        Image.new("RGB", (8, 8), (26, 77, 62)).save(buf, format="PNG")
        logo = SimpleUploadedFile(
            "logo.png",
            buf.getvalue(),
            content_type="image/png",
        )
        response = self.client.patch(
            self.url,
            {"logo": logo},
            format="multipart",
            **self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertTrue(response.data["logo_url"])
        self.academy.refresh_from_db()
        self.assertTrue(self.academy.logo)
