"""Extract plain text from CA PDFs."""

from __future__ import annotations

from pathlib import Path


def extract_pdf_text(path: str | Path) -> str:
    """Return concatenated page text from a PDF file."""
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    parts: list[str] = []
    for page in reader.pages:
        text = page.extract_text() or ""
        text = text.strip()
        if text:
            parts.append(text)
    return "\n\n".join(parts).strip()


# Fortune IAS monthly magazine section headings (order matters for splitting).
MONTHLY_SECTION_MARKERS = [
    "Polity & Governance",
    "Economy",
    "International Relations",
    "History & Culture",
    "Geography",
    "Environment & Ecology",
    "Science & Technology",
    "Defence",
    "Military Exercises",
    "Miscellaneous",
    "Places in News",
    "Species in News",
    "Keywords",
]


def split_monthly_sections(full_text: str) -> list[tuple[str, str]]:
    """
    Split monthly magazine text into (section_name, body) chunks.
    Prefers matches after the INDEX block when present.
    Falls back to a single 'Full document' chunk if markers are missing.
    """
    import re

    # Skip TOC: start search after last "INDEX" heading when possible
    search_from = 0
    for m in re.finditer(r"\bINDEX\b", full_text, re.IGNORECASE):
        search_from = m.end()

    body_text = full_text[search_from:] if search_from else full_text
    offset = search_from

    hits: list[tuple[int, str]] = []
    for marker in MONTHLY_SECTION_MARKERS:
        pattern = re.compile(re.escape(marker), re.IGNORECASE)
        match = pattern.search(body_text)
        if match:
            hits.append((offset + match.start(), marker))

    hits.sort(key=lambda x: x[0])
    if not hits:
        return [("Full document", full_text)]

    chunks: list[tuple[str, str]] = []
    for i, (start, name) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(full_text)
        body = full_text[start:end].strip()
        if len(body) > 200:
            chunks.append((name, body))
    return chunks or [("Full document", full_text)]
