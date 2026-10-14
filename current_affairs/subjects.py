"""Canonical subject tags for Current Affairs MCQs."""

from __future__ import annotations

SUBJECT_TAGS: tuple[str, ...] = (
    "Polity",
    "Economy",
    "IR",
    "Environment",
    "S&T",
    "Geography",
    "Defence",
    "History",
    "Society",
    "Other",
)

SUBJECT_TAG_SET = frozenset(SUBJECT_TAGS)

_ALIASES: dict[str, str] = {
    # Exact allowlist (lowercase keys)
    "polity": "Polity",
    "economy": "Economy",
    "ir": "IR",
    "environment": "Environment",
    "s&t": "S&T",
    "geography": "Geography",
    "defence": "Defence",
    "defense": "Defence",
    "history": "History",
    "society": "Society",
    "other": "Other",
    # Common Gemini / editorial variants
    "international relations": "IR",
    "international relation": "IR",
    "intl relations": "IR",
    "science and technology": "S&T",
    "science & technology": "S&T",
    "sci & tech": "S&T",
    "sci and tech": "S&T",
    "s and t": "S&T",
    "science": "S&T",
    "technology": "S&T",
    "indian polity": "Polity",
    "constitution": "Polity",
    "governance": "Polity",
    "indian economy": "Economy",
    "economics": "Economy",
    "ecology": "Environment",
    "climate": "Environment",
    "biodiversity": "Environment",
    "social issues": "Society",
    "social justice": "Society",
    "art and culture": "History",
    "art & culture": "History",
    "culture": "History",
    "ancient history": "History",
    "medieval history": "History",
    "modern history": "History",
    "security": "Defence",
    "internal security": "Defence",
    "military": "Defence",
}


def normalize_subject_tag(raw: str | None) -> str:
    """Map free-text subject labels onto the canonical allowlist."""
    text = (raw or "").strip()
    if not text:
        return "Other"
    if text in SUBJECT_TAG_SET:
        return text
    key = " ".join(text.lower().split())
    if key in _ALIASES:
        return _ALIASES[key]
    # Strip common punctuation noise
    key = key.replace("-", " ").replace("/", " ")
    key = " ".join(key.split())
    if key in _ALIASES:
        return _ALIASES[key]
    return "Other"
