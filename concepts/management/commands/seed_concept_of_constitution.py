"""Seed Laxmikanth Ch.3 Concept of the Constitution (visual revision chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from subjects.models import Chapter, Subject

HUB_SLUG = "concept-of-constitution"
CHAPTER_SLUG = "concept-of-constitution"

ENTRY_PILLARS = [
    {
        "id": "what",
        "articles": "Meaning · Functions · Qualities",
        "label": "What a constitution is",
        "slug": "coc-what-constitution-is",
        "detail": "Definition, Bulmer’s purposes, and seven qualities of a good constitution.",
        "tone": "teal",
    },
    {
        "id": "classification",
        "articles": "5 axes",
        "label": "Classification",
        "slug": "coc-classification",
        "detail": "Evolved/enacted, written/unwritten, rigid/flexible, federal/unitary, procedural/prescriptive.",
        "tone": "gold",
    },
    {
        "id": "constitutionalism",
        "articles": "Limited government",
        "label": "Constitutionalism",
        "slug": "coc-constitutionalism",
        "detail": "Constitution ≠ constitutionalism — limited government and Henkin’s eight elements.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "coc-rulebook-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Rulebook",
        "topic_label": "Concept of the Constitution",
        "subject_label": "The polity",
        "relation_label": "Sets up",
        "protects_from": [
            "Confusion of constitution with constitutionalism",
            "Mixing classification axes",
            "Memorising country lists instead of labels",
        ],
        "insight": (
            "A constitution is the polity’s rulebook — organisation of power, "
            "rights and duties, and (ideally) limits on government."
        ),
    },
    {
        "id": "coc-entry-pillars",
        "type": "pillars",
        "title": "Three revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "coc-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Scan the hub, then open Classification first (highest Prelims yield). "
            "Finish with Constitutionalism (Mains distinction). "
            "This is a visual revision layer — not a substitute for Laxmikanth."
        ),
    },
]

CLUSTERS = [
    {
        "title": "What a Constitution Is",
        "slug": "coc-what-constitution-is",
        "sort_order": 1,
        "summary": (
            "Meaning, Bulmer’s eight functions, and seven qualities of a good constitution."
        ),
        "body": (
            "## Meaning, functions, qualities\n\n"
            "**Latin root:** *constituere* — to establish or set up.\n\n"
            "A constitution is the set of principles that specify how government is organised, "
            "how it works, and the rights and duties linking government and people. "
            "Also called the fundamental / supreme / basic law of the land.\n\n"
            "**Wheare (one-liner):** the whole system of government — the rules that establish "
            "and regulate the government.\n\n"
            "Scan **functions** (what it does) and **qualities** (what makes it good). "
            "Stability vs adaptability = living document without easy tampering."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 3 — Meaning / Functions / Qualities",
                "constituere; fundamental law; Bulmer 8; seven qualities.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "coc-meaning-callout",
                "type": "callout",
                "tone": "info",
                "title": "Meaning (exam-core)",
                "body": (
                    "*Constituere* = establish. Constitution = rules organising government "
                    "and linking it to the people (rights & duties). "
                    "Wheare: the whole system of government — rules that establish and regulate it."
                ),
            },
            {
                "id": "coc-functions-pillars",
                "type": "pillars",
                "title": "Eight functions (Bulmer)",
                "items": [
                    {
                        "id": "f1",
                        "articles": "1",
                        "label": "Political community",
                        "slug": "coc-what-constitution-is",
                        "detail": "Declare and define its boundaries.",
                        "tone": "teal",
                    },
                    {
                        "id": "f2",
                        "articles": "2",
                        "label": "Authority",
                        "slug": "coc-what-constitution-is",
                        "detail": "Declare and define nature and authority of the community.",
                        "tone": "olive",
                    },
                    {
                        "id": "f3",
                        "articles": "3",
                        "label": "Identity & values",
                        "slug": "coc-what-constitution-is",
                        "detail": "Express national identity and values.",
                        "tone": "gold",
                    },
                    {
                        "id": "f4",
                        "articles": "4",
                        "label": "Rights & duties",
                        "slug": "coc-what-constitution-is",
                        "detail": "Declare and define citizens’ rights and duties.",
                        "tone": "orange",
                    },
                    {
                        "id": "f5",
                        "articles": "5",
                        "label": "Institutions",
                        "slug": "coc-what-constitution-is",
                        "detail": "Establish and regulate political institutions.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "f6",
                        "articles": "6",
                        "label": "Power-sharing",
                        "slug": "coc-what-constitution-is",
                        "detail": "Divide or share power across layers / sub-state communities.",
                        "tone": "maroon",
                    },
                    {
                        "id": "f7",
                        "articles": "7",
                        "label": "Sacred & secular",
                        "slug": "coc-what-constitution-is",
                        "detail": "Official religious identity; sacred–secular boundaries.",
                        "tone": "teal",
                    },
                    {
                        "id": "f8",
                        "articles": "8",
                        "label": "Socio-economic goals",
                        "slug": "coc-what-constitution-is",
                        "detail": "Commit the state to social, economic, or developmental goals.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "coc-qualities-pillars",
                "type": "pillars",
                "title": "Seven qualities of a good constitution",
                "items": [
                    {
                        "id": "q1",
                        "articles": "1",
                        "label": "Brevity",
                        "slug": "coc-what-constitution-is",
                        "detail": "Precise — avoid unwanted detail that confuses interpretation.",
                        "tone": "teal",
                    },
                    {
                        "id": "q2",
                        "articles": "2",
                        "label": "Clarity",
                        "slug": "coc-what-constitution-is",
                        "detail": "Clear wording; complicated language reduces understanding.",
                        "tone": "olive",
                    },
                    {
                        "id": "q3",
                        "articles": "3",
                        "label": "Definiteness",
                        "slug": "coc-what-constitution-is",
                        "detail": "One definite meaning — ambiguity widens judicial discretion.",
                        "tone": "gold",
                    },
                    {
                        "id": "q4",
                        "articles": "4",
                        "label": "Comprehensiveness",
                        "slug": "coc-what-constitution-is",
                        "detail": "Powers of government + rights/duties of citizens.",
                        "tone": "orange",
                    },
                    {
                        "id": "q5",
                        "articles": "5",
                        "label": "Suitability",
                        "slug": "coc-what-constitution-is",
                        "detail": "Fit the nation’s history, society, economy, and politics.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "q6",
                        "articles": "6",
                        "label": "Stability",
                        "slug": "coc-what-constitution-is",
                        "detail": "Hard to tamper — strengthens citizen obedience.",
                        "tone": "maroon",
                    },
                    {
                        "id": "q7",
                        "articles": "7",
                        "label": "Adaptability",
                        "slug": "coc-what-constitution-is",
                        "detail": "Living document — can adapt to changing needs.",
                        "tone": "teal",
                    },
                ],
            },
        ],
    },
    {
        "title": "Classification of Constitutions",
        "slug": "coc-classification",
        "sort_order": 2,
        "summary": (
            "Five axes — evolved/enacted, written/unwritten, rigid/flexible, "
            "federal/unitary, procedural/prescriptive — with India’s label on each."
        ),
        "body": (
            "## Five classification axes\n\n"
            "Memorise **axis + India’s label**, not long country lists.\n\n"
            "| Axis | India’s label |\n"
            "|---|---|\n"
            "| Evolved / Enacted | Enacted |\n"
            "| Unwritten / Written | Written (≈ enacted) |\n"
            "| Flexible / Rigid (Bryce) | **Synthesis of both** |\n"
            "| Unitary / Federal | **Quasi-federal** (Wheare) |\n"
            "| Procedural / Prescriptive | Has both flavours (structures + goals) |\n\n"
            "Depth on rigidity and federalism → Salient Features chapter."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 3 — Classification",
                "Bryce (rigid/flexible); Wheare (quasi-federal); Bulmer (procedural/prescriptive).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "coc-evolved-enacted",
                "type": "comparison",
                "title": "1. Evolved ↔ Enacted",
                "columns": [
                    {
                        "id": "evolved",
                        "heading": "Evolved (cumulative)",
                        "points": [
                            "Slow historical growth",
                            "Conventions, practices, judicial decisions",
                            "Example: UK",
                        ],
                    },
                    {
                        "id": "enacted",
                        "heading": "Enacted (conventional)",
                        "points": [
                            "Deliberately made (assembly / council / statute)",
                            "In a document or series of documents",
                            "Examples: USA, India",
                        ],
                    },
                    {
                        "id": "india-1",
                        "heading": "India",
                        "points": [
                            "Enacted",
                            "Framed by the Constituent Assembly",
                        ],
                    },
                ],
            },
            {
                "id": "coc-written-unwritten",
                "type": "comparison",
                "title": "2. Unwritten ↔ Written",
                "columns": [
                    {
                        "id": "unwritten",
                        "heading": "Unwritten (uncodified)",
                        "points": [
                            "Mostly not in one book",
                            "Conventions, statutes, judicial decisions",
                            "Examples: UK, New Zealand, Israel",
                        ],
                    },
                    {
                        "id": "written",
                        "heading": "Written (codified)",
                        "points": [
                            "Provisions in a document / series",
                            "Consciously adopted by a constituent body",
                            "Examples: USA, India",
                        ],
                    },
                    {
                        "id": "india-2",
                        "heading": "India",
                        "points": [
                            "Written",
                            "Same distinction ≈ evolved vs enacted",
                        ],
                    },
                ],
            },
            {
                "id": "coc-rigid-flexible",
                "type": "comparison",
                "title": "3. Flexible ↔ Rigid (Bryce)",
                "columns": [
                    {
                        "id": "flexible",
                        "heading": "Flexible (elastic)",
                        "points": [
                            "Amended like ordinary law",
                            "No special amendment procedure",
                            "Example: UK",
                        ],
                    },
                    {
                        "id": "rigid",
                        "heading": "Rigid (inelastic)",
                        "points": [
                            "Special amendment procedure",
                            "Constitutional law ≠ ordinary law",
                            "Example: USA",
                        ],
                    },
                    {
                        "id": "india-3",
                        "heading": "India",
                        "points": [
                            "Neither purely rigid nor flexible",
                            "Synthesis of both",
                            "See Salient Features → Art. 368 pathways",
                        ],
                    },
                ],
            },
            {
                "id": "coc-federal-unitary",
                "type": "comparison",
                "title": "4. Unitary ↔ Federal",
                "columns": [
                    {
                        "id": "unitary",
                        "heading": "Unitary",
                        "points": [
                            "Power concentrated at the centre",
                            "Regions are subordinate / delegated",
                            "Example: UK",
                        ],
                    },
                    {
                        "id": "federal",
                        "heading": "Federal",
                        "points": [
                            "Division of power Centre ↔ regions",
                            "Each operates in its own jurisdiction",
                            "Example: USA",
                        ],
                    },
                    {
                        "id": "india-4",
                        "heading": "India",
                        "points": [
                            "Federal + unitary provisions",
                            "Quasi-federal (K.C. Wheare)",
                            "Depth → Salient Features",
                        ],
                    },
                ],
            },
            {
                "id": "coc-procedural-prescriptive",
                "type": "comparison",
                "title": "5. Procedural ↔ Prescriptive (Bulmer)",
                "columns": [
                    {
                        "id": "procedural",
                        "heading": "Procedural",
                        "points": [
                            "Legal/political structures of institutions",
                            "Limits on government power",
                            "Protects process and basic rights",
                        ],
                    },
                    {
                        "id": "prescriptive",
                        "heading": "Prescriptive",
                        "points": [
                            "Also how government functions",
                            "Assumes / imposes shared societal goals",
                            "Public authorities must strive to achieve them",
                        ],
                    },
                    {
                        "id": "india-5",
                        "heading": "India",
                        "points": [
                            "Structures + limits (procedural)",
                            "Also goals (e.g. DPSP flavour — prescriptive)",
                        ],
                    },
                ],
            },
            {
                "id": "coc-classification-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Axis + India label: Enacted · Written · Synthesis (rigid/flexible) · "
                    "Quasi-federal (Wheare) · Procedural + prescriptive flavours. "
                    "Do not memorise every foreign example."
                ),
            },
        ],
    },
    {
        "title": "Constitutionalism",
        "slug": "coc-constitutionalism",
        "sort_order": 3,
        "summary": (
            "Constitution ≠ constitutionalism — limited government, rule of law, "
            "and Henkin’s eight elements."
        ),
        "body": (
            "## Constitution vs constitutionalism\n\n"
            "A country may have a **constitution** but not **constitutionalism** "
            "(e.g. a dictatorship).\n\n"
            "**Constitutionalism** = limited government + rule of law — "
            "the antithesis of arbitrary power. "
            "Arbitrary power written into a document still negates constitutionalism.\n\n"
            "Scan Henkin’s eight elements; link to Salient Features for how India "
            "institutionalises many of them."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 3 — Constitutionalism",
                "Limited government; Henkin’s eight elements.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "coc-vs-constitutionalism",
                "type": "comparison",
                "title": "Constitution vs constitutionalism",
                "columns": [
                    {
                        "id": "constitution",
                        "heading": "Constitution",
                        "points": [
                            "Document / set of rules exists",
                            "May organise unlimited power",
                            "Dictatorship can still have one",
                        ],
                    },
                    {
                        "id": "constitutionalism",
                        "heading": "Constitutionalism",
                        "points": [
                            "Limited government + rule of law",
                            "Restraints, decentralisation, fair play",
                            "Antithesis of arbitrary / despotic rule",
                        ],
                    },
                ],
            },
            {
                "id": "coc-henkin-pillars",
                "type": "pillars",
                "title": "Eight elements (Henkin) — scan only",
                "items": [
                    {
                        "id": "h1",
                        "articles": "1",
                        "label": "Popular sovereignty",
                        "slug": "coc-constitutionalism",
                        "detail": "Ultimate authority rests with the people.",
                        "tone": "teal",
                    },
                    {
                        "id": "h2",
                        "articles": "2",
                        "label": "Rule of law",
                        "slug": "coc-constitutionalism",
                        "detail": "Government bound by law, not will alone.",
                        "tone": "olive",
                    },
                    {
                        "id": "h3",
                        "articles": "3",
                        "label": "Democratic government",
                        "slug": "coc-constitutionalism",
                        "detail": "Responsible and accountable government.",
                        "tone": "gold",
                    },
                    {
                        "id": "h4",
                        "articles": "4",
                        "label": "Separation of powers",
                        "slug": "coc-constitutionalism",
                        "detail": "Checks and balances among organs.",
                        "tone": "orange",
                    },
                    {
                        "id": "h5",
                        "articles": "5",
                        "label": "Independent judiciary",
                        "slug": "coc-constitutionalism",
                        "detail": "Courts free to enforce constitutional limits.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "h6",
                        "articles": "6",
                        "label": "Civilian control of military",
                        "slug": "coc-constitutionalism",
                        "detail": "Armed forces under civilian authority.",
                        "tone": "maroon",
                    },
                    {
                        "id": "h7",
                        "articles": "7",
                        "label": "Police under law",
                        "slug": "coc-constitutionalism",
                        "detail": "Police governed by law and judicial control.",
                        "tone": "teal",
                    },
                    {
                        "id": "h8",
                        "articles": "8",
                        "label": "Individual rights",
                        "slug": "coc-constitutionalism",
                        "detail": "Respect for individual rights.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "coc-constitutionalism-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "Constitutionalism = limited, civilized government under rules. "
                    "Arbitrary power — even if conferred by a constitutional document — "
                    "is a negation of constitutionalism."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "coc-what-constitution-is"),
    (HUB_SLUG, "parent", "coc-classification"),
    (HUB_SLUG, "parent", "coc-constitutionalism"),
    ("coc-classification", "related", "salient-features-constitution"),
    ("coc-constitutionalism", "related", "salient-features-constitution"),
]


class Command(BaseCommand):
    help = "Seed Concept of the Constitution chapter (Laxmikanth Ch.3)."

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

        chapter, _ = Chapter.objects.update_or_create(
            subject=subject,
            slug=CHAPTER_SLUG,
            defaults={
                "title": "Concept of the Constitution",
                "sort_order": 3,
                "book_ref": "Laxmikanth 8th Ed, Ch. 3",
                "summary": (
                    "Visual revision of Ch.3 — rulebook mental model, meaning/functions/qualities, "
                    "five classification axes, and constitutionalism."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Concept of the Constitution",
                "summary": (
                    "What a constitution is, how constitutions are classified, "
                    "and why constitutionalism means limited government."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **rulebook mental model**, then the **three stops**. "
                    "Open **Classification** first (axis + India label). "
                    "Finish with **Constitutionalism** (constitution ≠ limited government). "
                    "This is a visual revision layer — not a substitute for Laxmikanth."
                ),
                "visual_blocks": HUB_VISUAL_BLOCKS,
                "chapter": chapter,
                "sort_order": 0,
                "status": Concept.Status.PUBLISHED,
            },
        )

        by_slug = {HUB_SLUG: hub}

        for cluster in CLUSTERS:
            concept, _ = Concept.objects.update_or_create(
                subject=subject,
                slug=cluster["slug"],
                defaults={
                    "title": cluster["title"],
                    "summary": cluster["summary"],
                    "body": cluster["body"],
                    "visual_blocks": cluster["visual_blocks"],
                    "chapter": chapter,
                    "sort_order": cluster["sort_order"],
                    "status": Concept.Status.PUBLISHED,
                },
            )
            by_slug[cluster["slug"]] = concept
            ConceptArticle.objects.filter(concept=concept).delete()
            for i, (ref, excerpt) in enumerate(cluster["articles"]):
                ConceptArticle.objects.create(
                    concept=concept,
                    ref=ref,
                    excerpt=excerpt,
                    sort_order=i,
                )

        ConceptArticle.objects.filter(concept=hub).delete()
        ConceptArticle.objects.create(
            concept=hub,
            ref="Laxmikanth Ch. 3",
            excerpt=(
                "Concept of the Constitution — meaning, functions, qualities, "
                "classification, and constitutionalism."
            ),
            sort_order=0,
        )

        coc_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=coc_slugs, source__subject=subject
        ).filter(
            target__slug__in=coc_slugs | {"salient-features-constitution"}
        ).delete()

        created_edges = 0
        for src, rel, tgt in EDGES:
            source = by_slug.get(src) or Concept.objects.filter(
                subject=subject, slug=src
            ).first()
            target = by_slug.get(tgt) or Concept.objects.filter(
                subject=subject, slug=tgt
            ).first()
            if not source or not target:
                self.stdout.write(
                    self.style.WARNING(f"Skip edge {src} → {tgt} (missing concept)")
                )
                continue
            _, was_created = ConceptEdge.objects.get_or_create(
                source=source,
                target=target,
                relation_type=rel,
            )
            if was_created:
                created_edges += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Concept of the Constitution seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges."
            )
        )
