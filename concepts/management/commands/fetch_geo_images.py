"""Fetch Geography diagram/map images for the visual-revision pilot.

Primary source: Wikimedia Commons (licence-clean, downloaded + self-hosted under
``frontend/public/geo/<chapter>/``). Fallback: extract an embedded figure from
the Vision IAS source PDF via poppler ``pdfimages`` when a good Commons match is
unavailable.

This is an AUTHORING-TIME command. It only proposes/downloads candidates and
records attribution; a human reviews the files before they are wired into a seed
command. Network access is required for the Wikimedia step.

Examples::

    python manage.py fetch_geo_images
    python manage.py fetch_geo_images --only earth-interior,rock-cycle --force
    python manage.py fetch_geo_images --list
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

WIKIMEDIA_API = "https://commons.wikimedia.org/w/api.php"
# Wikimedia asks all clients to send a descriptive User-Agent.
USER_AGENT = "UPSCBuddy-GeoImageFetcher/1.0 (educational; contact: admin@upscbuddy.local)"
RASTER_MIME = {"image/png": ".png", "image/jpeg": ".jpg", "image/jpg": ".jpg"}


@dataclass
class Figure:
    """One diagram to source for a chapter."""

    key: str
    query: str = ""
    # PDF page (1-indexed physical page) for the pdfimages fallback/extraction.
    pdf_page: int | None = None
    # Which image on that page (0-indexed, in extraction order). None -> largest.
    pdf_image_index: int | None = None
    # If True, extract from the PDF instead of querying Wikimedia.
    prefer_pdf: bool = False


# Geomorphology (Ch. 1) figure set. Keys match the `src` filenames referenced by
# the seed_geomorphology visual blocks: /geo/geomorphology/<key>.<ext>.
# Diagrams that are clearest / most UPSC-aligned in the source book are pulled
# from the PDF (prefer_pdf); generic physical-process diagrams come from the
# licence-clean Wikimedia Commons.
GEOMORPHOLOGY_FIGURES: list[Figure] = [
    Figure("earth-interior", pdf_page=10, pdf_image_index=0, prefer_pdf=True),
    Figure("seismic-discontinuity", pdf_page=10, pdf_image_index=1, prefer_pdf=True),
    Figure("seismic-shadow-zone", query="seismic wave shadow zone earth diagram", pdf_page=12, pdf_image_index=0),
    Figure("plate-boundaries", query="tectonic plate boundaries types USGS diagram"),
    Figure("fold-types", query="fold geology anticline syncline diagram"),
    Figure("fault-types", pdf_page=33, pdf_image_index=2, prefer_pdf=True),
    Figure("volcano-types", pdf_page=37, pdf_image_index=0, prefer_pdf=True),
    Figure("world-seismic-belts", pdf_page=35, pdf_image_index=0, prefer_pdf=True),
    Figure("india-seismic-zones", pdf_page=36, pdf_image_index=0, prefer_pdf=True),
    Figure("rock-cycle", query="rock cycle diagram igneous sedimentary metamorphic"),
    Figure("soil-profile", query="soil horizon profile diagram"),
]

CHAPTER_FIGURES: dict[str, list[Figure]] = {
    "geomorphology": GEOMORPHOLOGY_FIGURES,
}

DEFAULT_PDF = "books/ccab2-geography.pdf"


@dataclass
class Result:
    key: str
    status: str
    path: str = ""
    attribution: dict = field(default_factory=dict)
    note: str = ""


class Command(BaseCommand):
    help = "Download Geography diagrams from Wikimedia Commons (PDF fallback) for a chapter."

    def add_arguments(self, parser):
        parser.add_argument(
            "--chapter",
            default="geomorphology",
            help="Chapter key to fetch figures for (default: geomorphology).",
        )
        parser.add_argument(
            "--only",
            default="",
            help="Comma-separated figure keys to limit to (default: all).",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Re-download even if the target file already exists.",
        )
        parser.add_argument(
            "--search-limit",
            type=int,
            default=8,
            help="Max Wikimedia candidates to consider per figure.",
        )
        parser.add_argument(
            "--pdf",
            default=DEFAULT_PDF,
            help=f"Source PDF for the fallback extractor (default: {DEFAULT_PDF}).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Resolve candidates but do not download or write files.",
        )
        parser.add_argument(
            "--list",
            action="store_true",
            help="List the figure keys for the chapter and exit.",
        )

    def handle(self, *args, **options):
        chapter = options["chapter"]
        figures = CHAPTER_FIGURES.get(chapter)
        if not figures:
            raise CommandError(
                f"No figure set defined for chapter '{chapter}'. "
                f"Known: {', '.join(sorted(CHAPTER_FIGURES))}."
            )

        if options["list"]:
            for fig in figures:
                self.stdout.write(f"{fig.key}\t{fig.query}")
            return

        only = {k.strip() for k in options["only"].split(",") if k.strip()}
        if only:
            figures = [f for f in figures if f.key in only]
            if not figures:
                raise CommandError(f"No figures match --only={options['only']}.")

        out_dir = Path(settings.BASE_DIR) / "frontend" / "public" / "geo" / chapter
        out_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = out_dir / "_attributions.json"
        manifest = self._load_manifest(manifest_path)

        dry_run = options["dry_run"]
        force = options["force"]
        pdf_path = Path(settings.BASE_DIR) / options["pdf"]

        results: list[Result] = []
        for fig in figures:
            existing = self._existing_file(out_dir, fig.key)
            if existing and not force:
                results.append(
                    Result(fig.key, "skipped", str(existing), note="already present")
                )
                continue

            result = self._fetch_one(
                fig,
                out_dir=out_dir,
                pdf_path=pdf_path,
                search_limit=options["search_limit"],
                dry_run=dry_run,
            )
            results.append(result)
            if result.status == "downloaded" and result.attribution:
                manifest[fig.key] = result.attribution

        if not dry_run:
            self._write_manifest(manifest_path, manifest)

        self._report(results, out_dir, dry_run)

    # ---- fetching -------------------------------------------------------

    def _fetch_one(self, fig, *, out_dir, pdf_path, search_limit, dry_run):
        if fig.prefer_pdf and fig.pdf_page:
            pdf_result = self._extract_from_pdf(fig, out_dir, pdf_path, dry_run)
            if pdf_result.status == "downloaded":
                return pdf_result

        candidate = self._search_wikimedia(fig.query, search_limit) if fig.query else None
        if candidate:
            if dry_run:
                return Result(
                    fig.key,
                    "candidate",
                    candidate["url"],
                    note=f"{candidate['title']} ({candidate['license']})",
                )
            downloaded = self._download(candidate["url"], out_dir, fig.key)
            if downloaded:
                return Result(
                    fig.key,
                    "downloaded",
                    str(downloaded),
                    attribution={
                        "source": "Wikimedia Commons",
                        "title": candidate["title"],
                        "license": candidate["license"],
                        "artist": candidate["artist"],
                        "descriptionurl": candidate["descriptionurl"],
                    },
                    note=candidate["license"],
                )

        # Wikimedia miss -> try the PDF fallback if a page is provided.
        if fig.pdf_page:
            return self._extract_from_pdf(fig, out_dir, pdf_path, dry_run)

        return Result(fig.key, "missing", note="no Wikimedia match and no pdf_page")

    def _search_wikimedia(self, query: str, limit: int) -> dict | None:
        import requests

        params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": query,
            "gsrnamespace": 6,  # File:
            "gsrlimit": limit,
            "prop": "imageinfo",
            "iiprop": "url|mime|extmetadata|size",
            "iiurlwidth": 1200,
        }
        try:
            resp = requests.get(
                WIKIMEDIA_API,
                params=params,
                headers={"User-Agent": USER_AGENT},
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:  # noqa: BLE001 - authoring tool, log and continue
            self.stderr.write(self.style.WARNING(f"  Wikimedia query failed: {exc}"))
            return None

        pages = (data.get("query") or {}).get("pages") or {}
        query_words = {w for w in re.findall(r"[a-z]+", query.lower()) if len(w) > 2}

        scored = []
        for page in pages.values():
            info_list = page.get("imageinfo") or []
            if not info_list:
                continue
            info = info_list[0]
            mime = info.get("mime", "")
            if mime not in RASTER_MIME:
                continue  # skip SVG/other to keep next/image config simple
            url = info.get("thumburl") or info.get("url")
            if not url:
                continue
            title = page.get("title", "")
            title_words = set(re.findall(r"[a-z]+", title.lower()))
            # Rank by how many query terms appear in the file title so an
            # off-topic file that merely shares one keyword does not win.
            overlap = len(query_words & title_words)
            bonus = 1 if {"diagram", "cross", "cutaway", "schematic"} & title_words else 0
            scored.append(
                (overlap + bonus, -page.get("index", 1_000_000), page, info, mime, url)
            )

        if not scored:
            return None
        scored.sort(key=lambda t: (t[0], t[1]), reverse=True)
        _, _, page, info, mime, url = scored[0]
        meta = info.get("extmetadata") or {}
        return {
            "url": url,
            "mime": mime,
            "title": page.get("title", ""),
            "license": self._meta_value(meta, "LicenseShortName") or "See source",
            "artist": self._strip_html(self._meta_value(meta, "Artist")),
            "descriptionurl": info.get("descriptionurl", ""),
        }

    def _download(self, url: str, out_dir: Path, key: str) -> Path | None:
        import requests

        try:
            resp = requests.get(
                url, headers={"User-Agent": USER_AGENT}, timeout=60, stream=True
            )
            resp.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            self.stderr.write(self.style.WARNING(f"  Download failed for {key}: {exc}"))
            return None

        ext = RASTER_MIME.get(resp.headers.get("Content-Type", "").split(";")[0], ".png")
        # Clean any stale variant of this key before writing the new file.
        for old in out_dir.glob(f"{key}.*"):
            old.unlink()
        target = out_dir / f"{key}{ext}"
        with open(target, "wb") as fh:
            for chunk in resp.iter_content(chunk_size=1 << 15):
                fh.write(chunk)
        return target

    def _extract_from_pdf(self, fig, out_dir: Path, pdf_path: Path, dry_run: bool) -> Result:
        if not fig.pdf_page:
            return Result(fig.key, "missing", note="no pdf_page for fallback")
        if not pdf_path.exists():
            return Result(fig.key, "missing", note=f"PDF not found: {pdf_path}")
        if not shutil.which("pdfimages"):
            return Result(
                fig.key, "missing", note="pdfimages (poppler) not installed"
            )
        if dry_run:
            return Result(
                fig.key, "candidate", note=f"PDF page {fig.pdf_page} fallback"
            )

        with tempfile.TemporaryDirectory() as tmp:
            prefix = Path(tmp) / "img"
            try:
                subprocess.run(
                    [
                        "pdfimages", "-png",
                        "-f", str(fig.pdf_page),
                        "-l", str(fig.pdf_page),
                        str(pdf_path), str(prefix),
                    ],
                    check=True,
                    capture_output=True,
                )
            except subprocess.CalledProcessError as exc:  # noqa: PERF203
                return Result(
                    fig.key, "missing", note=f"pdfimages failed: {exc.stderr[:120]!r}"
                )
            in_order = sorted(Path(tmp).glob("img-*.png"))
            if not in_order:
                return Result(fig.key, "missing", note="no images on that PDF page")
            if fig.pdf_image_index is not None:
                if fig.pdf_image_index >= len(in_order):
                    return Result(
                        fig.key,
                        "missing",
                        note=f"page {fig.pdf_page} has {len(in_order)} images, "
                        f"index {fig.pdf_image_index} out of range",
                    )
                chosen = in_order[fig.pdf_image_index]
            else:
                # No explicit index -> the biggest image is usually the figure.
                chosen = max(in_order, key=lambda p: p.stat().st_size)
            for old in out_dir.glob(f"{fig.key}.*"):
                old.unlink()
            target = out_dir / f"{fig.key}.png"
            shutil.copyfile(chosen, target)
            return Result(
                fig.key,
                "downloaded",
                str(target),
                attribution={
                    "source": "Vision IAS CCAB-2 Geography (PDF extract)",
                    "title": f"Page {fig.pdf_page}",
                    "license": "Copyrighted — private revision use only",
                    "artist": "Vision IAS",
                    "descriptionurl": "",
                },
                note=f"PDF page {fig.pdf_page}",
            )

    # ---- helpers --------------------------------------------------------

    @staticmethod
    def _existing_file(out_dir: Path, key: str) -> Path | None:
        for ext in (".png", ".jpg", ".jpeg"):
            candidate = out_dir / f"{key}{ext}"
            if candidate.exists():
                return candidate
        return None

    @staticmethod
    def _meta_value(meta: dict, field_name: str) -> str:
        entry = meta.get(field_name)
        if isinstance(entry, dict):
            return str(entry.get("value", "")).strip()
        return ""

    @staticmethod
    def _strip_html(text: str) -> str:
        return re.sub(r"<[^>]+>", "", text).strip()

    @staticmethod
    def _load_manifest(path: Path) -> dict:
        if path.exists():
            try:
                return json.loads(path.read_text())
            except json.JSONDecodeError:
                return {}
        return {}

    def _write_manifest(self, path: Path, manifest: dict):
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    def _report(self, results: list[Result], out_dir: Path, dry_run: bool):
        for r in results:
            style = {
                "downloaded": self.style.SUCCESS,
                "candidate": self.style.HTTP_INFO,
                "skipped": self.style.NOTICE,
                "missing": self.style.WARNING,
            }.get(r.status, self.style.NOTICE)
            self.stdout.write(style(f"[{r.status}] {r.key} — {r.note}"))
        downloaded = sum(1 for r in results if r.status == "downloaded")
        missing = [r.key for r in results if r.status == "missing"]
        self.stdout.write(
            self.style.SUCCESS(
                f"\n{('DRY-RUN ' if dry_run else '')}Done. "
                f"{downloaded} downloaded into {out_dir}."
            )
        )
        if missing:
            self.stdout.write(
                self.style.WARNING(
                    "Needs manual sourcing (add pdf_page or refine query): "
                    + ", ".join(missing)
                )
            )
