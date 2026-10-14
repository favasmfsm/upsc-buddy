"""Seed a clickable catalog of all visual grammar templates."""

from django.core.management.base import BaseCommand

from concepts.models import Concept
from subjects.models import Subject

CATALOG_SLUG = "visual-grammar-catalog"

CATALOG_BLOCKS = [
    {
        "id": "demo-mental-model",
        "type": "mental_model",
        "title": "1. Mental model",
        "metaphor": "Shield",
        "topic_label": "Fundamental Rights",
        "subject_label": "Citizen",
        "relation_label": "Protects you from",
        "protects_from": [
            "State abuse",
            "Discrimination",
            "Arbitrary arrest",
        ],
        "insight": "Template for first-impression metaphors before Articles.",
    },
    {
        "id": "demo-tree",
        "type": "tree",
        "title": "2. Hierarchy / constitution map",
        "root": {
            "id": "constitution",
            "label": "Constitution",
            "detail": "Supreme law",
            "children": [
                {
                    "id": "fr",
                    "label": "Fundamental Rights",
                    "slug": "fundamental-rights",
                    "detail": "Part III",
                    "children": [
                        {
                            "id": "eq",
                            "label": "Equality",
                            "slug": "fr-equality-14-18",
                        },
                        {
                            "id": "free",
                            "label": "Freedom",
                            "slug": "fr-right-to-freedom",
                        },
                    ],
                },
                {
                    "id": "dpsp",
                    "label": "DPSP",
                    "slug": "directive-principles",
                    "detail": "Part IV",
                },
                {
                    "id": "fd",
                    "label": "Fundamental Duties",
                    "detail": "Part IVA",
                },
            ],
        },
    },
    {
        "id": "demo-pillars",
        "type": "pillars",
        "title": "3. Pillars",
        "items": [
            {
                "id": "eq",
                "articles": "Arts 14–18",
                "label": "Equality",
                "slug": "fr-equality-14-18",
                "detail": "Expandable pillar example.",
                "tone": "teal",
            },
            {
                "id": "free",
                "articles": "Arts 19–22",
                "label": "Freedom",
                "slug": "fr-right-to-freedom",
                "detail": "Open the freedom umbrella.",
                "tone": "olive",
            },
            {
                "id": "rem",
                "articles": "Art. 32",
                "label": "Remedies",
                "slug": "fr-remedies-32",
                "detail": "Heart and soul.",
                "tone": "maroon",
            },
        ],
    },
    {
        "id": "demo-timeline",
        "type": "timeline",
        "title": "4. Timeline",
        "events": [
            {
                "id": "e1",
                "year": 1950,
                "label": "Constitution in force",
                "detail": "Property as a Fundamental Right.",
            },
            {
                "id": "e2",
                "year": 1978,
                "label": "44th Amendment",
                "detail": "Property shifted out of Part III.",
            },
            {
                "id": "e3",
                "year": 1978,
                "label": "Legal right (Art. 300A)",
                "detail": "Present framing — constitutional/legal right.",
            },
        ],
    },
    {
        "id": "demo-relation-graph",
        "type": "relation_graph",
        "title": "5. Relationship graph",
        "root_slug": "fundamental-rights",
        "depth": 2,
    },
    {
        "id": "demo-decision",
        "type": "flowchart",
        "title": "6. Decision tree",
        "root": "problem",
        "steps": [
            {
                "id": "problem",
                "label": "What is the problem?",
                "detail": "Pick a branch.",
                "options": [
                    {"label": "Arrest", "next": "arrest"},
                    {"label": "Speech", "next": "speech"},
                ],
            },
            {
                "id": "arrest",
                "label": "Article 22",
                "detail": "Safeguards in arrest / detention.",
            },
            {
                "id": "speech",
                "label": "Article 19",
                "detail": "Then test 19(2) grounds.",
            },
        ],
    },
    {
        "id": "demo-journey",
        "type": "journey",
        "title": "7. Citizen journey",
        "stages": [
            {"id": "s1", "label": "Citizen", "detail": "Wants public employment."},
            {
                "id": "s2",
                "label": "Article 16",
                "detail": "Equality of opportunity.",
                "slug": "fr-equality-14-18",
            },
            {
                "id": "s3",
                "label": "Reservation / exceptions",
                "detail": "Special provisions and limits.",
            },
            {
                "id": "s4",
                "label": "Case law",
                "detail": "Indra Sawhney themes.",
                "case_slug": "indra-sawhney",
            },
        ],
    },
    {
        "id": "demo-comparison",
        "type": "comparison",
        "title": "8. Compare view",
        "columns": [
            {
                "id": "fr",
                "heading": "Fundamental Rights",
                "points": ["Enforceable", "Negative obligations", "Courts protect"],
            },
            {
                "id": "dpsp",
                "heading": "DPSP",
                "points": [
                    "Not enforceable",
                    "Positive obligations",
                    "Government implements",
                ],
            },
        ],
    },
    {
        "id": "demo-restriction",
        "type": "flowchart",
        "title": "9. Restriction visualization",
        "root": "speech",
        "steps": [
            {
                "id": "speech",
                "label": "Freedom of speech",
                "detail": "Art. 19(1)(a)",
                "options": [
                    {"label": "Allowed", "next": "ok"},
                    {"label": "Restricted by", "next": "grounds"},
                ],
            },
            {
                "id": "ok",
                "label": "Protected expression",
                "detail": "Unless a listed reasonable restriction applies.",
            },
            {
                "id": "grounds",
                "label": "19(2) grounds",
                "detail": "Security, public order, morality, contempt, defamation…",
                "options": [
                    {"label": "Public order", "next": "po"},
                    {"label": "Defamation", "next": "def"},
                ],
            },
            {
                "id": "po",
                "label": "Public order",
                "detail": "Listed ground — still must be reasonable.",
            },
            {
                "id": "def",
                "label": "Defamation",
                "detail": "Listed ground — still must be reasonable.",
            },
        ],
    },
    {
        "id": "demo-heatmap",
        "type": "pyq_heatmap",
        "title": "10. PYQ heatmap",
        "items": [
            {"concept_slug": "fr-equality-14-18", "label": "Equality"},
            {"concept_slug": "fr-right-to-freedom", "label": "Freedom"},
            {"concept_slug": "fr-remedies-32", "label": "Remedies"},
        ],
    },
    {
        "id": "demo-article-explorer",
        "type": "article_explorer",
        "title": "11. Article explorer",
        "article_ref": "Article 19",
        "stages": [
            {
                "id": "topic",
                "label": "Freedom of Speech",
                "detail": "Citizens — six freedoms under 19(1).",
            },
            {
                "id": "exceptions",
                "label": "Exceptions",
                "detail": "Reasonable restrictions under 19(2)–(6).",
            },
            {
                "id": "cases",
                "label": "Landmark Cases",
                "detail": "Authored stage — wire cases later.",
            },
            {
                "id": "pyqs",
                "label": "PYQs",
                "detail": "Authored stage — link PYQs later.",
            },
            {
                "id": "ca",
                "label": "Current Affairs",
                "detail": "Placeholder until CA module.",
            },
        ],
    },
    {
        "id": "demo-case-network",
        "type": "case_network",
        "title": "12. Court cases network",
        "hub_label": "Article 21",
        "cases": [
            {
                "id": "mg",
                "label": "Maneka Gandhi",
                "year": 1978,
                "detail": "Fair, just, reasonable procedure.",
                "case_slug": "maneka-gandhi",
            },
            {
                "id": "putt",
                "label": "Puttaswamy",
                "year": 2017,
                "detail": "Privacy as FR.",
                "case_slug": "puttaswamy",
            },
            {
                "id": "olga",
                "label": "Olga Tellis",
                "year": 1985,
                "detail": "Livelihood facet of life.",
                "case_slug": "olga-tellis",
            },
        ],
    },
    {
        "id": "demo-memory-palace",
        "type": "memory_palace",
        "title": "13. Memory palace",
        "setting": "Supreme Court courtroom",
        "loci": [
            {
                "id": "l1",
                "place": "Judge's bench",
                "association": "Article 32",
                "detail": "Move the Court to enforce FR.",
            },
            {
                "id": "l2",
                "place": "Ambedkar bust",
                "association": "Heart and soul",
                "detail": "Classic Prelims one-liner for Art. 32.",
            },
            {
                "id": "l3",
                "place": "Writ tray",
                "association": "Five writs",
                "detail": "Habeas, mandamus, prohibition, certiorari, quo warranto.",
            },
        ],
    },
    {
        "id": "demo-simulator",
        "type": "simulator",
        "title": "14. What-if simulator",
        "start": "q1",
        "nodes": {
            "q1": {
                "prompt": "Government bans a newspaper. Which right is primarily engaged?",
                "choices": [
                    {"label": "Article 19(1)(a)", "next": "q2"},
                    {"label": "Article 21 only", "next": "wrong1"},
                ],
            },
            "q2": {
                "prompt": "Can Government do this?",
                "choices": [
                    {
                        "label": "Yes, if a reasonable restriction under 19(2)",
                        "next": "end_ok",
                    },
                    {"label": "Never, under any circumstances", "next": "wrong2"},
                ],
            },
            "end_ok": {
                "prompt": "Correct path — check listed ground + reasonableness.",
                "choices": [],
            },
            "wrong1": {
                "prompt": "Press/speech is classically Art. 19 — try again.",
                "choices": [{"label": "Back", "next": "q1"}],
            },
            "wrong2": {
                "prompt": "FR speech is not absolute — 19(2) exists. Try again.",
                "choices": [{"label": "Back", "next": "q2"}],
            },
        },
    },
]


class Command(BaseCommand):
    help = "Seed visual-grammar-catalog concept (all 14 grammar demos)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug to seed into (default: fortuneias).",
        )

    def handle(self, *args, **options):
        from academies.seed_utils import get_academy_or_fail

        academy = get_academy_or_fail(options["academy"])
        subject, _ = Subject.objects.get_or_create(
            academy=academy,
            slug="polity",
            defaults={
                "name": "Polity",
                "description": "Indian Constitution and political system for UPSC.",
                "is_active": True,
            },
        )

        concept, created = Concept.objects.update_or_create(
            subject=subject,
            slug=CATALOG_SLUG,
            defaults={
                "title": "Visual grammar catalog",
                "summary": (
                    "Authoring gallery of every visual template. "
                    "Pick 1 primary + ≤2 support grammars per concept."
                ),
                "body": (
                    "## How to use\n\n"
                    "This page is a **template catalog**, not a study topic. "
                    "See `docs/VISUAL_GRAMMARS.md` for schemas. "
                    "Open each block to see the interaction pattern."
                ),
                "visual_blocks": CATALOG_BLOCKS,
                "chapter": None,
                "sort_order": 9000,
                "status": Concept.Status.PUBLISHED,
            },
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{'Created' if created else 'Updated'} {concept.slug} "
                f"({academy.slug}) with {len(CATALOG_BLOCKS)} demo blocks."
            )
        )
