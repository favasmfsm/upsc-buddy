"""Gemini-backed MCQ generation for current affairs PDFs (ingest only)."""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from django.conf import settings

from current_affairs.subjects import SUBJECT_TAGS, normalize_subject_tag

logger = logging.getLogger(__name__)

QUESTION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "stem": {"type": "string"},
                    "option_a": {"type": "string"},
                    "option_b": {"type": "string"},
                    "option_c": {"type": "string"},
                    "option_d": {"type": "string"},
                    "correct_option": {
                        "type": "string",
                        "enum": ["A", "B", "C", "D"],
                    },
                    "explanation": {"type": "string"},
                    "subject_tag": {"type": "string"},
                    "source_topic": {"type": "string"},
                },
                "required": [
                    "stem",
                    "option_a",
                    "option_b",
                    "option_c",
                    "option_d",
                    "correct_option",
                    "explanation",
                    "subject_tag",
                    "source_topic",
                ],
            },
        }
    },
    "required": ["questions"],
}

SYSTEM_INSTRUCTIONS = f"""You are an expert UPSC Civil Services Prelims (GS Paper 1) question setter.
Generate factual multiple-choice questions ONLY from the provided current affairs material.
Rules:
- Exactly 4 options (A-D); one unambiguously correct answer grounded in the text.
- Focus on concepts, events/happenings, and institutional knowledge: persons (who said/led/appointed),
  ministries/departments, organisations/bodies, schemes, constitutional provisions, reports,
  locations, definitions, cause-effect, and comparisons — not rote memorisation of crude numbers.
- Do NOT ask for isolated figures (exact amounts, percentages, rankings, year counts, budgets,
  or other statistics) unless the number itself is the core conceptual point in the source.
  Prefer what/why/which body/who over how much/how many.
- Avoid vague opinion questions; avoid inventing facts not in the source.
- Keep stems clear and self-contained as standalone current-affairs questions for that day;
  never phrase stems or options as referring to the source (avoid "according to the material/passage/text/document",
  "as mentioned above", "based on the excerpt", etc.). Write as if testing real-world knowledge from the day's news.
- Explanations cite the key fact briefly.
- For multi-statement stems, put each numbered statement on its own line (newline before 1., 2., 3., …)
  and a newline before the final ask (e.g. "Which of the statements given above are correct?").
  Never jam statements into one paragraph.
- subject_tag: one of: {", ".join(SUBJECT_TAGS)}. Prefer exact labels; do not invent others.
- source_topic: short topic title from the material.
"""


def format_mcq_stem(stem: str) -> str:
    """Insert line breaks before jammed numbered statements in UPSC-style stems."""
    text = (stem or "").strip()
    if not text:
        return text
    # "...statements:1. Foo" / "...text?1. Foo" / "...grounds.2. Bar"
    text = re.sub(
        r"([:?.\)\"'”’])\s*(\d{1,2})\.\s+(?=[A-Z\"'“‘])",
        r"\1\n\2. ",
        text,
    )
    # Closing ask only when it follows end of a prior sentence/statement
    text = re.sub(
        r'(?<=[.!"\'”’])\s*(?=(?:Which of the (?:statements|above)|Select the correct|Choose the correct|Codes?\s*:))',
        "\n",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _client():
    from google import genai

    api_key = getattr(settings, "GEMINI_API_KEY", "") or ""
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")
    return genai.Client(api_key=api_key)


def _parse_response(raw: str) -> list[dict[str, Any]]:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    data = json.loads(raw)
    if isinstance(data, list):
        questions = data
    else:
        questions = data.get("questions") or []
    cleaned: list[dict[str, Any]] = []
    for q in questions:
        opt = str(q.get("correct_option", "")).strip().upper()
        if opt not in {"A", "B", "C", "D"}:
            continue
        stem = format_mcq_stem(q.get("stem") or "")
        if not stem:
            continue
        cleaned.append(
            {
                "stem": stem,
                "option_a": (q.get("option_a") or "").strip(),
                "option_b": (q.get("option_b") or "").strip(),
                "option_c": (q.get("option_c") or "").strip(),
                "option_d": (q.get("option_d") or "").strip(),
                "correct_option": opt,
                "explanation": (q.get("explanation") or "").strip(),
                "subject_tag": normalize_subject_tag(q.get("subject_tag")),
                "source_topic": (q.get("source_topic") or "").strip()[:255],
            }
        )
    return cleaned


def generate_mcqs_from_text(
    text: str,
    *,
    target_count: int,
    section_label: str = "",
) -> list[dict[str, Any]]:
    """Call Gemini once and return normalized MCQ dicts."""
    from google.genai import types

    model = getattr(settings, "GEMINI_MODEL", "gemini-2.5-flash")
    section_note = f" Section focus: {section_label}." if section_label else ""
    # Cap context to keep tokens reasonable
    body = text[:60000]
    prompt = (
        f"{SYSTEM_INSTRUCTIONS}\n"
        f"Generate about {target_count} prelims MCQs grounded only in the source below. Phrase each question as a standalone current-affairs MCQ (do not refer to the source/material in the stem)."
        f"{section_note}\n\n"
        f"--- SOURCE MATERIAL ---\n{body}\n--- END ---"
    )

    client = _client()
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=QUESTION_SCHEMA,
            temperature=0.4,
        ),
    )
    raw = getattr(response, "text", None) or ""
    if not raw and response.candidates:
        parts = response.candidates[0].content.parts
        raw = "".join(getattr(p, "text", "") or "" for p in parts)
    return _parse_response(raw)


def model_name() -> str:
    return getattr(settings, "GEMINI_MODEL", "gemini-2.5-flash")
