"""Download daily FINDER PDFs for a date range."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from pathlib import Path

import requests
from django.conf import settings

BASE_URL = "https://fortuneiascircle.com/uploads/download/FINDER_{slug}.pdf"
PDF_MAGIC = b"%PDF"
REQUEST_TIMEOUT = 30


def default_pdf_dir() -> Path:
    return Path(settings.BASE_DIR) / "data" / "daily" / "finder"


def iter_dates(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def build_url_slugs(day: date) -> list[str]:
    slug = day.strftime("%d-%m-%Y")
    return [slug, f"{slug}_(1)", f"{slug}(1)"]


def is_valid_cached_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size == 0:
        return False
    with path.open("rb") as handle:
        return handle.read(len(PDF_MAGIC)) == PDF_MAGIC


def download_one(
    day: date, pdf_dir: Path, session: requests.Session
) -> tuple[date, str]:
    destination = pdf_dir / f"{day.isoformat()}.pdf"
    if is_valid_cached_pdf(destination):
        return day, "cached"

    network_error = False
    for slug in build_url_slugs(day):
        url = BASE_URL.format(slug=slug)
        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT)
        except requests.RequestException:
            network_error = True
            continue
        if response.status_code != 200 or not response.content.startswith(PDF_MAGIC):
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        temp_path = destination.with_suffix(".part")
        temp_path.write_bytes(response.content)
        temp_path.replace(destination)
        return day, "downloaded"

    if destination.exists():
        destination.unlink()
    return day, "failed" if network_error else "skipped"


def scrape_range(
    start: date,
    end: date,
    pdf_dir: Path | None = None,
    workers: int = 4,
) -> dict[str, int]:
    """
    Download FINDER PDFs for [start, end] into pdf_dir.

    Returns counts: cached, downloaded, skipped, failed.
    """
    if start > end:
        raise ValueError("start must be on or before end")

    target = pdf_dir or default_pdf_dir()
    target.mkdir(parents=True, exist_ok=True)
    days = list(iter_dates(start, end))
    stats = {"cached": 0, "downloaded": 0, "skipped": 0, "failed": 0}

    with requests.Session() as session:
        session.headers.update({"User-Agent": "UPSC-FINDER-scraper/1.0"})
        with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
            futures = {
                executor.submit(download_one, day, target, session): day
                for day in days
            }
            for future in as_completed(futures):
                _day, status = future.result()
                stats[status] += 1

    return stats
