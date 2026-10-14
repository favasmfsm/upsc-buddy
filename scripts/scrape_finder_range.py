#!/usr/bin/env python3
"""Download daily FINDER PDFs into data/daily/finder/ for a date range."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

# Allow running without Django when invoked as a standalone script.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

try:
    import django
    from django.conf import settings as dj_settings

    if not dj_settings.configured:
        import os

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
        django.setup()
except Exception:
    django = None  # type: ignore


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Invalid date {value!r}; use YYYY-MM-DD"
        ) from exc


def main(argv: list[str] | None = None) -> int:
    from current_affairs.services.finder_scrape import default_pdf_dir, scrape_range

    parser = argparse.ArgumentParser(description="Download FINDER daily PDFs.")
    parser.add_argument("--start", type=parse_date, required=True)
    parser.add_argument("--end", type=parse_date, required=True)
    parser.add_argument("--pdf-dir", type=Path, default=None)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args(argv)

    if args.start > args.end:
        print("Error: --start must be on or before --end", file=sys.stderr)
        return 1

    pdf_dir = args.pdf_dir or default_pdf_dir()
    print(f"Downloading FINDER PDFs from {args.start} to {args.end} → {pdf_dir}")
    stats = scrape_range(
        args.start, args.end, pdf_dir=pdf_dir, workers=args.workers
    )

    print()
    print("Summary")
    for key in ("cached", "downloaded", "skipped", "failed"):
        print(f"  {key.capitalize():12} {stats[key]}")
    print(f"  PDF dir:     {pdf_dir}")
    return 1 if stats["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
