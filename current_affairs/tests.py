from datetime import date

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from academies.models import Academy, AcademyMembership
from current_affairs.models import (
    CADocument,
    CAQuestion,
    QuizAttempt,
    QuizAttemptAnswer,
)
from current_affairs.subjects import normalize_subject_tag

User = get_user_model()


class NormalizeSubjectTagTests(TestCase):
    def test_aliases_and_fallback(self):
        self.assertEqual(normalize_subject_tag("International Relations"), "IR")
        self.assertEqual(normalize_subject_tag("science & technology"), "S&T")
        self.assertEqual(normalize_subject_tag("Polity"), "Polity")
        self.assertEqual(normalize_subject_tag("weird topic"), "Other")
        self.assertEqual(normalize_subject_tag(""), "Other")


class CAAnalyticsAPITests(TestCase):
    def setUp(self):
        self.academy = Academy.objects.create(
            name="Test Academy",
            slug="test-academy",
            invite_code="TESTCODE01",
        )
        self.student = User.objects.create_user(
            email="student@example.com", password="pass12345"
        )
        self.staff = User.objects.create_user(
            email="staff@example.com", password="pass12345"
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.student,
            role=AcademyMembership.Role.STUDENT,
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.staff,
            role=AcademyMembership.Role.STAFF,
        )

        pdf = SimpleUploadedFile(
            "d.pdf", b"%PDF-1.4 test", content_type="application/pdf"
        )
        self.doc = CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.DAILY,
            title="Day 1",
            source_date=date(2026, 7, 1),
            file=pdf,
            status=CADocument.Status.READY,
        )
        self.q1 = CAQuestion.objects.create(
            document=self.doc,
            stem="Q1?",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="A",
            subject_tag="International Relations",
            source_topic="UNSC reform",
            sort_order=0,
        )
        self.q2 = CAQuestion.objects.create(
            document=self.doc,
            stem="Q2?",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="B",
            subject_tag="Polity",
            source_topic="Article 21",
            sort_order=1,
        )
        self.q3 = CAQuestion.objects.create(
            document=self.doc,
            stem="Q3?",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="C",
            subject_tag="Polity",
            source_topic="Article 21",
            sort_order=2,
        )

        self.client = APIClient()
        self.headers = {"HTTP_X_ACADEMY_SLUG": self.academy.slug}

    def _auth(self, user):
        self.client.force_authenticate(user=user)

    def test_submit_writes_answer_rows_with_normalized_tags(self):
        attempt = QuizAttempt.objects.create(
            academy=self.academy,
            user=self.student,
            mode=QuizAttempt.Mode.DAILY,
            period_start=date(2026, 7, 1),
            period_end=date(2026, 7, 1),
            question_ids=[self.q1.id, self.q2.id, self.q3.id],
            total=3,
        )
        self._auth(self.student)
        res = self.client.post(
            f"/api/current_affairs/quizzes/{attempt.id}/submit/",
            {
                "answers": {
                    str(self.q1.id): "A",
                    str(self.q2.id): "A",
                    # q3 skipped
                }
            },
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["score"], 1)
        self.assertEqual(QuizAttemptAnswer.objects.filter(attempt=attempt).count(), 3)

        rows = {
            r.question_id: r
            for r in QuizAttemptAnswer.objects.filter(attempt=attempt)
        }
        self.assertTrue(rows[self.q1.id].is_correct)
        self.assertEqual(rows[self.q1.id].subject_tag, "IR")
        self.assertFalse(rows[self.q2.id].is_correct)
        self.assertEqual(rows[self.q3.id].selected_option, "")
        self.assertFalse(rows[self.q3.id].is_correct)

    def test_my_analytics_accuracy(self):
        attempt = QuizAttempt.objects.create(
            academy=self.academy,
            user=self.student,
            mode=QuizAttempt.Mode.DAILY,
            period_start=date(2026, 7, 1),
            period_end=date(2026, 7, 1),
            question_ids=[self.q1.id, self.q2.id, self.q3.id],
            total=3,
        )
        self._auth(self.student)
        self.client.post(
            f"/api/current_affairs/quizzes/{attempt.id}/submit/",
            {
                "answers": {
                    str(self.q1.id): "A",
                    str(self.q2.id): "B",
                    str(self.q3.id): "A",
                }
            },
            format="json",
            **self.headers,
        )

        # Add two more Polity/Article 21 answers so weak_topics min_total=3 is met
        for correct in (True, False):
            a = QuizAttempt.objects.create(
                academy=self.academy,
                user=self.student,
                mode=QuizAttempt.Mode.DAILY,
                period_start=date(2026, 7, 1),
                period_end=date(2026, 7, 1),
                question_ids=[self.q2.id],
                answers={str(self.q2.id): "B" if correct else "A"},
                score=1 if correct else 0,
                total=1,
                completed_at=timezone.now(),
            )
            QuizAttemptAnswer.objects.create(
                attempt=a,
                question=self.q2,
                selected_option="B" if correct else "A",
                is_correct=correct,
                subject_tag="Polity",
                source_topic="Article 21",
            )

        res = self.client.get(
            "/api/current_affairs/analytics/me/",
            **self.headers,
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["summary"]["attempts"], 3)
        # 2 correct of 3 on first attempt + 1 correct of 1 + 0 of 1 = 3/5
        self.assertEqual(res.data["summary"]["questions_answered"], 5)
        self.assertEqual(res.data["summary"]["accuracy_pct"], 60.0)

        subjects = {r["subject_tag"]: r for r in res.data["by_subject"]}
        self.assertIn("IR", subjects)
        self.assertIn("Polity", subjects)
        self.assertEqual(subjects["IR"]["correct"], 1)
        self.assertEqual(subjects["IR"]["total"], 1)

        weak = res.data["weak_topics"]
        self.assertTrue(any(t["source_topic"] == "Article 21" for t in weak))

    def test_academy_analytics_staff_only(self):
        attempt = QuizAttempt.objects.create(
            academy=self.academy,
            user=self.student,
            mode=QuizAttempt.Mode.DAILY,
            period_start=date(2026, 7, 1),
            period_end=date(2026, 7, 1),
            question_ids=[self.q1.id],
            total=1,
        )
        self._auth(self.student)
        self.client.post(
            f"/api/current_affairs/quizzes/{attempt.id}/submit/",
            {"answers": {str(self.q1.id): "A"}},
            format="json",
            **self.headers,
        )

        denied = self.client.get(
            "/api/current_affairs/analytics/academy/",
            **self.headers,
        )
        self.assertEqual(denied.status_code, 403)

        self._auth(self.staff)
        ok = self.client.get(
            "/api/current_affairs/analytics/academy/",
            **self.headers,
        )
        self.assertEqual(ok.status_code, 200)
        self.assertEqual(ok.data["summary"]["active_students"], 1)
        self.assertEqual(ok.data["summary"]["total_attempts"], 1)
        self.assertEqual(len(ok.data["students"]), 1)
        self.assertEqual(ok.data["students"][0]["email"], self.student.email)

        drill = self.client.get(
            f"/api/current_affairs/analytics/academy/students/{self.student.id}/",
            **self.headers,
        )
        self.assertEqual(drill.status_code, 200)
        self.assertEqual(drill.data["summary"]["attempts"], 1)
        self.assertEqual(drill.data["summary"]["accuracy_pct"], 100.0)


class QuizStartFilterTests(TestCase):
    def setUp(self):
        self.academy = Academy.objects.create(
            name="Start Academy",
            slug="start-academy",
            invite_code="STARTCODE1",
        )
        self.student = User.objects.create_user(
            email="starter@example.com", password="pass12345"
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.student,
            role=AcademyMembership.Role.STUDENT,
        )
        pdf = SimpleUploadedFile(
            "d.pdf", b"%PDF-1.4 test", content_type="application/pdf"
        )
        self.doc = CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.DAILY,
            title="Day Start",
            source_date=date(2026, 7, 2),
            file=pdf,
            status=CADocument.Status.READY,
        )
        for i, tag in enumerate(["Polity", "Polity", "Geography", "Economy"]):
            CAQuestion.objects.create(
                document=self.doc,
                stem=f"Q{i}?",
                option_a="A",
                option_b="B",
                option_c="C",
                option_d="D",
                correct_option="A",
                subject_tag=tag,
                source_topic=tag,
                sort_order=i,
            )
        self.client = APIClient()
        self.headers = {"HTTP_X_ACADEMY_SLUG": self.academy.slug}
        self.client.force_authenticate(user=self.student)

    def test_start_respects_subject_tags_and_limit(self):
        res = self.client.post(
            "/api/current_affairs/quizzes/start/",
            {
                "mode": "daily",
                "date": "2026-07-02",
                "subject_tags": ["Polity"],
                "limit": 1,
            },
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["total"], 1)
        self.assertEqual(res.data["questions"][0]["subject_tag"], "Polity")

    def test_start_all_subjects_without_limit(self):
        res = self.client.post(
            "/api/current_affairs/quizzes/start/",
            {"mode": "daily", "date": "2026-07-02"},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["total"], 4)

    def test_start_empty_match_returns_404(self):
        res = self.client.post(
            "/api/current_affairs/quizzes/start/",
            {
                "mode": "daily",
                "date": "2026-07-02",
                "subject_tags": ["History"],
            },
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 404)


class QuizRangeMonthlyGateTests(TestCase):
    def setUp(self):
        self.academy = Academy.objects.create(
            name="Range Academy",
            slug="range-academy",
            invite_code="RANGECODE1",
        )
        self.student = User.objects.create_user(
            email="ranger@example.com", password="pass12345"
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.student,
            role=AcademyMembership.Role.STUDENT,
        )
        daily_pdf = SimpleUploadedFile(
            "d.pdf", b"%PDF-1.4 daily", content_type="application/pdf"
        )
        monthly_pdf = SimpleUploadedFile(
            "m.pdf", b"%PDF-1.4 monthly", content_type="application/pdf"
        )
        self.daily = CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.DAILY,
            title="May 3 Daily",
            source_date=date(2026, 5, 3),
            file=daily_pdf,
            status=CADocument.Status.READY,
        )
        self.monthly = CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.MONTHLY,
            title="May Monthly",
            source_date=date(2026, 5, 1),
            file=monthly_pdf,
            status=CADocument.Status.READY,
        )
        self.daily_q = CAQuestion.objects.create(
            document=self.daily,
            stem="Daily Q?",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="A",
            subject_tag="Polity",
            source_topic="Daily",
            sort_order=0,
        )
        self.monthly_q = CAQuestion.objects.create(
            document=self.monthly,
            stem="Monthly Q?",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="A",
            subject_tag="Economy",
            source_topic="Monthly",
            sort_order=0,
        )
        self.client = APIClient()
        self.headers = {"HTTP_X_ACADEMY_SLUG": self.academy.slug}
        self.client.force_authenticate(user=self.student)

    def test_partial_range_excludes_monthly(self):
        res = self.client.post(
            "/api/current_affairs/quizzes/start/",
            {"mode": "range", "start": "2026-05-01", "end": "2026-05-07"},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["total"], 1)
        self.assertEqual(res.data["questions"][0]["id"], self.daily_q.id)

    def test_full_month_range_includes_monthly_and_daily(self):
        res = self.client.post(
            "/api/current_affairs/quizzes/start/",
            {"mode": "range", "start": "2026-05-01", "end": "2026-05-31"},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["total"], 2)
        ids = {q["id"] for q in res.data["questions"]}
        self.assertEqual(ids, {self.daily_q.id, self.monthly_q.id})

    def test_non_overlapping_month_excludes_monthly(self):
        res = self.client.post(
            "/api/current_affairs/quizzes/start/",
            {"mode": "range", "start": "2026-07-01", "end": "2026-07-07"},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 404)


class StaffDocumentLifecycleTests(TestCase):
    def setUp(self):
        self.academy = Academy.objects.create(
            name="Staff Academy",
            slug="staff-academy",
            invite_code="STAFFCODE1",
        )
        self.staff = User.objects.create_user(
            email="stafflife@example.com", password="pass12345"
        )
        AcademyMembership.objects.create(
            academy=self.academy,
            user=self.staff,
            role=AcademyMembership.Role.STAFF,
        )
        pdf = SimpleUploadedFile(
            "life.pdf", b"%PDF-1.4 life", content_type="application/pdf"
        )
        self.doc = CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.DAILY,
            title="Life Doc",
            source_date=date(2026, 6, 1),
            file=pdf,
            status=CADocument.Status.READY,
        )
        CAQuestion.objects.create(
            document=self.doc,
            stem="Keep?",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="A",
            subject_tag="Polity",
            source_topic="T",
            sort_order=0,
        )
        self.client = APIClient()
        self.headers = {"HTTP_X_ACADEMY_SLUG": self.academy.slug}
        self.client.force_authenticate(user=self.staff)

    def test_delete_removes_document_and_questions(self):
        doc_id = self.doc.pk
        res = self.client.delete(
            f"/api/current_affairs/staff/documents/{doc_id}/",
            **self.headers,
        )
        self.assertEqual(res.status_code, 204)
        self.assertFalse(CADocument.objects.filter(pk=doc_id).exists())
        self.assertEqual(CAQuestion.objects.filter(document_id=doc_id).count(), 0)

    def test_delete_blocked_while_processing(self):
        self.doc.status = CADocument.Status.PROCESSING
        self.doc.save(update_fields=["status"])
        res = self.client.delete(
            f"/api/current_affairs/staff/documents/{self.doc.pk}/",
            **self.headers,
        )
        self.assertEqual(res.status_code, 409)
        self.assertTrue(CADocument.objects.filter(pk=self.doc.pk).exists())

    def test_regenerate_blocked_while_processing(self):
        self.doc.status = CADocument.Status.PROCESSING
        self.doc.save(update_fields=["status"])
        res = self.client.post(
            f"/api/current_affairs/staff/documents/{self.doc.pk}/regenerate/",
            {},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 409)

    def test_replace_pdf_sets_pending(self):
        new_pdf = SimpleUploadedFile(
            "replaced.pdf", b"%PDF-1.4 replaced", content_type="application/pdf"
        )
        res = self.client.patch(
            f"/api/current_affairs/staff/documents/{self.doc.pk}/",
            {"file": new_pdf, "title": "Replaced Title"},
            format="multipart",
            **self.headers,
        )
        self.assertEqual(res.status_code, 200)
        self.doc.refresh_from_db()
        self.assertEqual(self.doc.title, "Replaced Title")
        self.assertEqual(self.doc.status, CADocument.Status.PENDING)
        self.assertTrue(self.doc.file.name.endswith("replaced.pdf"))

    def test_replace_blocked_while_processing(self):
        self.doc.status = CADocument.Status.PROCESSING
        self.doc.save(update_fields=["status"])
        new_pdf = SimpleUploadedFile(
            "nope.pdf", b"%PDF-1.4 nope", content_type="application/pdf"
        )
        res = self.client.patch(
            f"/api/current_affairs/staff/documents/{self.doc.pk}/",
            {"file": new_pdf},
            format="multipart",
            **self.headers,
        )
        self.assertEqual(res.status_code, 409)


class FinderIngestServiceTests(TestCase):
    def setUp(self):
        self.academy = Academy.objects.create(
            name="Finder Academy",
            slug="finder-academy",
            invite_code="FINDERCODE1",
        )

    def _write_pdf(self, directory, day: date, body: bytes = b"%PDF-1.4 test"):
        path = directory / f"{day.isoformat()}.pdf"
        path.write_bytes(body)
        return path

    def test_fill_creates_missing_docs_and_skips_ready(self):
        from pathlib import Path
        from tempfile import TemporaryDirectory
        from unittest.mock import patch

        from current_affairs.services.finder_ingest import ingest_range

        day_new = date(2026, 7, 21)
        day_ready = date(2026, 7, 20)
        existing = CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.DAILY,
            title="FINDER 20-07-2026",
            source_date=day_ready,
            file=SimpleUploadedFile(
                "ready.pdf", b"%PDF-1.4 ready", content_type="application/pdf"
            ),
            status=CADocument.Status.READY,
        )
        CAQuestion.objects.create(
            document=existing,
            stem="Q?",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="A",
            subject_tag="Polity",
            source_topic="T",
            sort_order=0,
        )

        with TemporaryDirectory() as tmp:
            pdf_dir = Path(tmp)
            self._write_pdf(pdf_dir, day_new)
            self._write_pdf(pdf_dir, day_ready, b"%PDF-1.4 ignored")
            with patch("current_affairs.services.finder_ingest._enqueue") as enqueue:
                stats = ingest_range(
                    self.academy,
                    day_ready,
                    day_new,
                    pdf_dir=pdf_dir,
                    regenerate=False,
                    enqueue=True,
                )

        self.assertEqual(stats["created"], 1)
        self.assertEqual(stats["skipped_ready"], 1)
        self.assertEqual(stats["enqueued"], 1)
        self.assertTrue(
            CADocument.objects.filter(
                academy=self.academy, source_date=day_new
            ).exists()
        )
        enqueue.assert_called_once()
        existing.refresh_from_db()
        self.assertEqual(existing.status, CADocument.Status.READY)

    def test_regenerate_replaces_and_force_enqueues(self):
        from pathlib import Path
        from tempfile import TemporaryDirectory
        from unittest.mock import patch

        from current_affairs.services.finder_ingest import ingest_range

        day = date(2026, 7, 22)
        doc = CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.DAILY,
            title="FINDER 22-07-2026",
            source_date=day,
            file=SimpleUploadedFile(
                "old.pdf", b"%PDF-1.4 old", content_type="application/pdf"
            ),
            status=CADocument.Status.READY,
        )

        with TemporaryDirectory() as tmp:
            pdf_dir = Path(tmp)
            self._write_pdf(pdf_dir, day, b"%PDF-1.4 newfile")
            with patch("current_affairs.services.finder_ingest._enqueue") as enqueue:
                stats = ingest_range(
                    self.academy,
                    day,
                    day,
                    pdf_dir=pdf_dir,
                    regenerate=True,
                    enqueue=True,
                )

        self.assertEqual(stats["replaced"], 1)
        self.assertEqual(stats["enqueued"], 1)
        enqueue.assert_called_once_with(doc.pk, force=True)
        doc.refresh_from_db()
        self.assertEqual(doc.status, CADocument.Status.PENDING)
        self.assertIn("FINDER_22-07-2026", doc.file.name)


class StaffFinderSyncAPITests(TestCase):
    def setUp(self):
        self.academy = Academy.objects.create(
            name="Sync Academy",
            slug="sync-academy",
            invite_code="SYNCCODE01",
        )
        self.staff = User.objects.create_user(
            email="syncstaff@example.com", password="pass12345"
        )
        self.student = User.objects.create_user(
            email="syncstudent@example.com", password="pass12345"
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
        self.client = APIClient()
        self.headers = {"HTTP_X_ACADEMY_SLUG": self.academy.slug}
        self.url = "/api/current_affairs/staff/finder/sync/"

    def test_student_forbidden(self):
        self.client.force_authenticate(user=self.student)
        res = self.client.post(
            self.url,
            {"start": "2026-07-21", "end": "2026-07-22"},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 403)

    def test_rejects_inverted_range(self):
        self.client.force_authenticate(user=self.staff)
        res = self.client.post(
            self.url,
            {"start": "2026-07-25", "end": "2026-07-21"},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn("end", res.data)

    def test_rejects_range_over_62_days(self):
        self.client.force_authenticate(user=self.staff)
        res = self.client.post(
            self.url,
            {"start": "2026-01-01", "end": "2026-03-15"},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn("end", res.data)

    def test_rejects_when_processing_in_range(self):
        CADocument.objects.create(
            academy=self.academy,
            doc_type=CADocument.DocType.DAILY,
            title="Busy",
            source_date=date(2026, 7, 21),
            file=SimpleUploadedFile(
                "busy.pdf", b"%PDF-1.4 busy", content_type="application/pdf"
            ),
            status=CADocument.Status.PROCESSING,
        )
        self.client.force_authenticate(user=self.staff)
        res = self.client.post(
            self.url,
            {"start": "2026-07-21", "end": "2026-07-22", "regenerate": False},
            format="json",
            **self.headers,
        )
        self.assertEqual(res.status_code, 409)

    def test_queues_sync_task(self):
        from unittest.mock import MagicMock, patch

        self.client.force_authenticate(user=self.staff)
        mock_result = MagicMock()
        mock_result.id = "task-abc"
        with patch(
            "current_affairs.tasks.sync_finder_range.apply_async",
            return_value=mock_result,
        ) as apply_async:
            res = self.client.post(
                self.url,
                {
                    "start": "2026-07-21",
                    "end": "2026-07-22",
                    "regenerate": True,
                },
                format="json",
                **self.headers,
            )
        self.assertEqual(res.status_code, 202)
        self.assertEqual(res.data["task_id"], "task-abc")
        self.assertTrue(res.data["regenerate"])
        apply_async.assert_called_once_with(
            args=[self.academy.pk, "2026-07-21", "2026-07-22"],
            kwargs={"regenerate": True},
            ignore_result=False,
        )
