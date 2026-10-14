from rest_framework import serializers

from .models import CADocument, CAQuestion, QuizAttempt
from .services.finder_ingest import FINDER_SYNC_MAX_DAYS, inclusive_day_count
from .subjects import SUBJECT_TAGS


class CADocumentSerializer(serializers.ModelSerializer):
    question_count = serializers.IntegerField(
        source="published_question_count", read_only=True
    )

    class Meta:
        model = CADocument
        fields = (
            "id",
            "doc_type",
            "title",
            "source_date",
            "period_start",
            "period_end",
            "status",
            "question_count",
            "generated_at",
        )


class StaffCADocumentSerializer(serializers.ModelSerializer):
    question_count = serializers.IntegerField(read_only=True)
    published_question_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = CADocument
        fields = (
            "id",
            "doc_type",
            "title",
            "source_date",
            "period_start",
            "period_end",
            "status",
            "error_message",
            "question_count",
            "published_question_count",
            "generated_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "period_start",
            "period_end",
            "status",
            "error_message",
            "question_count",
            "published_question_count",
            "generated_at",
            "created_at",
            "updated_at",
        )


class StaffFinderSyncSerializer(serializers.Serializer):
    start = serializers.DateField()
    end = serializers.DateField()
    regenerate = serializers.BooleanField(required=False, default=False)

    def validate(self, attrs):
        start = attrs["start"]
        end = attrs["end"]
        if start > end:
            raise serializers.ValidationError(
                {"end": "end must be on or after start."}
            )
        days = inclusive_day_count(start, end)
        if days > FINDER_SYNC_MAX_DAYS:
            raise serializers.ValidationError(
                {
                    "end": (
                        f"Date range cannot exceed {FINDER_SYNC_MAX_DAYS} days "
                        f"(got {days})."
                    )
                }
            )
        return attrs


class StaffCADocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CADocument
        fields = ("doc_type", "title", "source_date", "file")

    def validate(self, attrs):
        academy = self.context["academy"]
        doc_type = attrs["doc_type"]
        source_date = attrs["source_date"]
        if doc_type == CADocument.DocType.MONTHLY:
            source_date = source_date.replace(day=1)
            attrs["source_date"] = source_date
        exists = CADocument.objects.filter(
            academy=academy,
            doc_type=doc_type,
            source_date=source_date,
        ).exists()
        if exists:
            raise serializers.ValidationError(
                {
                    "source_date": (
                        "A document already exists for this type and date. "
                        "Replace its PDF, regenerate, or delete it first."
                    )
                }
            )
        return attrs

    def create(self, validated_data):
        validated_data["academy"] = self.context["academy"]
        return super().create(validated_data)


class StaffCADocumentReplaceSerializer(serializers.ModelSerializer):
    """Replace PDF (and optionally title) on an existing staff document."""

    class Meta:
        model = CADocument
        fields = ("file", "title")
        extra_kwargs = {
            "file": {"required": True},
            "title": {"required": False},
        }

    def update(self, instance, validated_data):
        if "title" in validated_data and validated_data["title"] is not None:
            instance.title = validated_data["title"]
        if "file" in validated_data:
            # Remove previous file from storage before assigning the new one.
            if instance.file:
                instance.file.delete(save=False)
            instance.file = validated_data["file"]
        instance.save()
        return instance


class StaffCAQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAQuestion
        fields = (
            "id",
            "stem",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "correct_option",
            "explanation",
            "subject_tag",
            "source_topic",
            "is_published",
            "sort_order",
        )
        read_only_fields = (
            "id",
            "stem",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "correct_option",
            "explanation",
            "subject_tag",
            "source_topic",
            "sort_order",
        )


class CAQuestionPublicSerializer(serializers.ModelSerializer):
    """Student-facing question — no correct answer until submit."""

    class Meta:
        model = CAQuestion
        fields = (
            "id",
            "stem",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "subject_tag",
            "source_topic",
            "sort_order",
        )


class QuizStartSerializer(serializers.Serializer):
    mode = serializers.ChoiceField(choices=QuizAttempt.Mode.choices)
    date = serializers.DateField(required=False)
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    limit = serializers.IntegerField(required=False, min_value=1, max_value=200)
    subject_tags = serializers.ListField(
        child=serializers.ChoiceField(choices=SUBJECT_TAGS),
        required=False,
        allow_empty=False,
    )

    def validate(self, attrs):
        mode = attrs["mode"]
        if mode in (QuizAttempt.Mode.DAILY, QuizAttempt.Mode.MONTHLY):
            if not attrs.get("date"):
                raise serializers.ValidationError(
                    {"date": "Required for daily and monthly modes."}
                )
        elif mode == QuizAttempt.Mode.RANGE:
            if not attrs.get("start") or not attrs.get("end"):
                raise serializers.ValidationError(
                    {"start": "start and end are required for range mode."}
                )
            if attrs["start"] > attrs["end"]:
                raise serializers.ValidationError(
                    {"end": "end must be on or after start."}
                )
        tags = attrs.get("subject_tags")
        if tags is not None:
            # Deduplicate while preserving order
            seen: set[str] = set()
            unique: list[str] = []
            for tag in tags:
                if tag not in seen:
                    seen.add(tag)
                    unique.append(tag)
            attrs["subject_tags"] = unique
        return attrs


class QuizSubmitSerializer(serializers.Serializer):
    answers = serializers.DictField(
        child=serializers.ChoiceField(choices=["A", "B", "C", "D"]),
        allow_empty=True,
    )


class QuizAttemptListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = (
            "id",
            "mode",
            "period_start",
            "period_end",
            "score",
            "total",
            "completed_at",
            "created_at",
        )


def ordered_questions(question_ids: list[int]) -> list[CAQuestion]:
    qs = CAQuestion.objects.filter(id__in=question_ids)
    by_id = {q.id: q for q in qs}
    return [by_id[i] for i in question_ids if i in by_id]


class QuizAttemptDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    results = serializers.SerializerMethodField()

    class Meta:
        model = QuizAttempt
        fields = (
            "id",
            "mode",
            "period_start",
            "period_end",
            "score",
            "total",
            "completed_at",
            "created_at",
            "questions",
            "results",
            "answers",
        )

    def get_questions(self, obj: QuizAttempt):
        if obj.is_completed:
            return []
        return CAQuestionPublicSerializer(
            ordered_questions(obj.question_ids), many=True
        ).data

    def get_results(self, obj: QuizAttempt):
        if not obj.is_completed:
            return None
        answers = obj.answers or {}
        out = []
        for q in ordered_questions(obj.question_ids):
            selected = answers.get(str(q.id))
            out.append(
                {
                    "id": q.id,
                    "stem": q.stem,
                    "option_a": q.option_a,
                    "option_b": q.option_b,
                    "option_c": q.option_c,
                    "option_d": q.option_d,
                    "correct_option": q.correct_option,
                    "explanation": q.explanation,
                    "subject_tag": q.subject_tag,
                    "source_topic": q.source_topic,
                    "selected": selected,
                    "is_correct": selected == q.correct_option,
                }
            )
        return out
