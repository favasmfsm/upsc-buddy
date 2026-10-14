"""Seed Laxmikanth Ch.13 Parliamentary System (visual revision)."""

from django.core.management.base import BaseCommand

from concepts.models import (
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from subjects.models import Chapter, Subject

HUB_SLUG = "parliamentary-system"
CHAPTER_SLUG = "parliamentary-system"

ENTRY_PILLARS = [
    {
        "id": "meaning",
        "articles": "Names",
        "label": "Meaning & names",
        "slug": "ps-meaning",
        "detail": "Cabinet / responsible / Westminster — and PM-dominant practice.",
        "tone": "teal",
    },
    {
        "id": "features",
        "articles": "8 features",
        "label": "Features (India)",
        "slug": "ps-features",
        "detail": "Nominal–real executives through secrecy — Art. 74–75 & 163–164.",
        "tone": "olive",
    },
    {
        "id": "vs-pres",
        "articles": "Table 13.1",
        "label": "vs Presidential",
        "slug": "ps-vs-presidential",
        "detail": "Dual vs single executive; fusion vs separation; dissolution vs fixed.",
        "tone": "gold",
    },
    {
        "id": "balance",
        "articles": "Merits ↔ Demerits",
        "label": "Merits & demerits",
        "slug": "ps-merits-demerits",
        "detail": "Responsibility and harmony vs instability and cabinet dictatorship.",
        "tone": "orange",
    },
    {
        "id": "why",
        "articles": "CA reasons",
        "label": "Why India chose it",
        "slug": "ps-why-adopted",
        "detail": "Familiarity; responsibility over stability; avoid conflict; plural society.",
        "tone": "terracotta",
    },
    {
        "id": "vs-uk",
        "articles": "6 diffs",
        "label": "India ≠ Britain",
        "slug": "ps-vs-british",
        "detail": "Republic, limited Parliament, either House PM, no shadow cabinet.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "ps-team-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Team accountable to the House",
        "topic_label": "Parliamentary System",
        "subject_label": "Arts 74–75 · 163–164",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating the President as the real executive",
            "Confusing with US separation of powers",
            "Calling Indian Parliament sovereign like Britain",
            "Forgetting collective responsibility is to the Lok Sabha",
        ],
        "insight": (
            "Real executive is a Council of Ministers that stays only while "
            "it commands the confidence of the lower House."
        ),
    },
    {
        "id": "ps-entry-pillars",
        "type": "pillars",
        "title": "Six revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "ps-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Parliamentary = responsible / Cabinet / Westminster model at Centre and in states. "
            "Scan Features → vs Presidential → India ≠ Britain. "
            "Exam traps: Art. 75 collective responsibility to Lok Sabha; PM from either House; "
            "advice to President binding (42nd/44th)."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Meaning & Names",
        "slug": "ps-meaning",
        "sort_order": 1,
        "summary": (
            "Parliamentary government = executive responsible to the legislature — "
            "also called Cabinet, responsible, or Westminster model."
        ),
        "body": (
            "## Meaning (revision spine)\n\n"
            "- Classified by **executive–legislature relation**: parliamentary vs presidential.\n"
            "- **Parliamentary:** executive responsible to legislature for policies and acts.\n"
            "- **Presidential:** executive not responsible; constitutionally independent of tenure.\n\n"
            "### Names to recall\n"
            "- **Cabinet system** (Ivor Jennings) — cabinet is the nucleus of power.\n"
            "- **Responsible government** — stays while it enjoys Parliament’s confidence.\n"
            "- **Westminster model** — after the British Parliament’s location.\n"
            "- Practice often called **prime ministerial government** (PM dominant vs cabinet equals).\n\n"
            "India: Arts **74–75** (Centre), **163–164** (states)."
        ),
        "articles": [
            (
                "Art. 74 & 75",
                "Council of Ministers to aid and advise the President; collective responsibility at the Centre.",
            ),
            (
                "Art. 163 & 164",
                "Parallel parliamentary executive in the states (Governor / CM / Council of Ministers).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ps-meaning-pillars",
                "type": "pillars",
                "title": "Four names, one idea",
                "items": [
                    {
                        "id": "cabinet",
                        "articles": "Jennings",
                        "label": "Cabinet system",
                        "slug": "ps-meaning",
                        "detail": "Cabinet is the nucleus of power in a parliamentary system.",
                        "tone": "teal",
                    },
                    {
                        "id": "responsible",
                        "articles": "Confidence",
                        "label": "Responsible government",
                        "slug": "ps-meaning",
                        "detail": "Real executive accountable to Parliament; stays on confidence.",
                        "tone": "olive",
                    },
                    {
                        "id": "westminster",
                        "articles": "UK origin",
                        "label": "Westminster model",
                        "slug": "ps-meaning",
                        "detail": "Named after the seat of the British Parliament.",
                        "tone": "gold",
                    },
                    {
                        "id": "pm-gov",
                        "articles": "Practice",
                        "label": "PM-dominant practice",
                        "slug": "ps-meaning",
                        "detail": "From ‘first among equals’ to prime ministerial government (India too).",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "ps-meaning-callout",
                "type": "callout",
                "tone": "tip",
                "title": "One-liner",
                "body": (
                    "If the executive must answer daily to the legislature and can fall by "
                    "no-confidence — it is parliamentary, not presidential."
                ),
            },
        ],
    },
    {
        "title": "Features of Parliamentary Government",
        "slug": "ps-features",
        "sort_order": 2,
        "summary": (
            "Eight features of India’s parliamentary system — from nominal/real executives "
            "to secrecy of cabinet procedure."
        ),
        "body": (
            "## Eight features (India)\n\n"
            "1. **Nominal & real executives** — President (de jure) vs PM (de facto); Art. 74 advice "
            "binding (42nd/44th).\n"
            "2. **Majority party rule** — majority in Lok Sabha forms government; coalitions if hung.\n"
            "3. **Collective responsibility** — bedrock; to Parliament generally, **Lok Sabha** "
            "particularly (Art. 75); no-confidence removes the ministry.\n"
            "4. **Political homogeneity** — same party ideology; coalitions bound by consensus.\n"
            "5. **Double membership** — ministers are legislators; non-MP minister max **6 months**.\n"
            "6. **Leadership of the PM** — leader of CoM, Parliament, and party in power.\n"
            "7. **Dissolution of lower House** — President dissolves Lok Sabha on PM’s advice.\n"
            "8. **Secrecy** — oath of secrecy; cabinet proceedings confidential.\n"
        ),
        "articles": [
            (
                "Art. 74",
                "Council of Ministers headed by the PM to aid and advise the President; advice binding.",
            ),
            (
                "Art. 75",
                "Collective responsibility of the Council of Ministers to the Lok Sabha.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ps-features-pillars",
                "type": "pillars",
                "title": "Eight features of parliamentary government in India",
                "items": [
                    {
                        "id": "nominal-real",
                        "articles": "Art. 74",
                        "label": "Nominal & real executives",
                        "slug": "ps-features",
                        "detail": "President = head of State; PM = head of government. Advice binding.",
                        "tone": "teal",
                    },
                    {
                        "id": "majority",
                        "articles": "2",
                        "label": "Majority party rule",
                        "slug": "ps-features",
                        "detail": "Majority in Lok Sabha forms government; hung House → coalition.",
                        "tone": "olive",
                    },
                    {
                        "id": "collective",
                        "articles": "Art. 75",
                        "label": "Collective responsibility",
                        "slug": "ps-features",
                        "detail": "Swim and sink together; accountable especially to Lok Sabha.",
                        "tone": "gold",
                    },
                    {
                        "id": "homogeneity",
                        "articles": "4",
                        "label": "Political homogeneity",
                        "slug": "ps-features",
                        "detail": "Same party ideology; coalitions operate by consensus.",
                        "tone": "orange",
                    },
                    {
                        "id": "double",
                        "articles": "6 months",
                        "label": "Double membership",
                        "slug": "ps-features",
                        "detail": "Ministers are legislators; non-MP ceases after six consecutive months.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "pm-lead",
                        "articles": "6",
                        "label": "Leadership of the PM",
                        "slug": "ps-features",
                        "detail": "Leads CoM, Parliament, and the party in power.",
                        "tone": "maroon",
                    },
                    {
                        "id": "dissolve",
                        "articles": "7",
                        "label": "Dissolution of lower House",
                        "slug": "ps-features",
                        "detail": "PM can advise President to dissolve Lok Sabha early.",
                        "tone": "teal",
                    },
                    {
                        "id": "secrecy",
                        "articles": "8",
                        "label": "Secrecy",
                        "slug": "ps-features",
                        "detail": "Oath of secrecy; cabinet proceedings stay confidential.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "ps-features-callout",
                "type": "callout",
                "tone": "warning",
                "title": "Exam traps",
                "body": (
                    "Collective responsibility → Lok Sabha (not both Houses equally). "
                    "Non-MP minister → max 6 months. "
                    "42nd & 44th Amendments made ministerial advice binding on the President."
                ),
            },
        ],
    },
    {
        "title": "Parliamentary vs Presidential",
        "slug": "ps-vs-presidential",
        "sort_order": 3,
        "summary": (
            "Table 13.1 spine — India’s dual, responsible, fused executive vs USA’s single, "
            "fixed, separated executive."
        ),
        "body": (
            "## Features contrast (Table 13.1)\n\n"
            "| Parliamentary (India) | Presidential (USA) |\n"
            "|---|---|\n"
            "| Dual executive | Single executive |\n"
            "| Majority party rule | Separate elections; fixed term |\n"
            "| Collective responsibility | Non-responsibility to Congress |\n"
            "| Political homogeneity (usual) | May not exist |\n"
            "| Double membership | Single membership (secretaries ≠ Congress) |\n"
            "| Leadership of PM | Domination of President |\n"
            "| Dissolution of lower House | No dissolution of House of Representatives |\n"
            "| Fusion of powers | Separation of powers |\n\n"
            "US President = head of State **and** government; Kitchen Cabinet is advisory only."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "ps-vs-pres-compare",
                "type": "comparison",
                "title": "Parliamentary (India) vs Presidential (USA)",
                "columns": [
                    {
                        "id": "parl",
                        "heading": "Parliamentary (India)",
                        "points": [
                            "Dual executive (nominal + real)",
                            "Majority party / coalition rule",
                            "Collective responsibility to legislature",
                            "Ministers are legislators (double membership)",
                            "PM leadership; lower House can be dissolved",
                            "Fusion of powers",
                        ],
                    },
                    {
                        "id": "pres",
                        "heading": "Presidential (USA)",
                        "points": [
                            "Single executive (President)",
                            "Separate elections; fixed four-year term",
                            "Executive not responsible to Congress daily",
                            "Secretaries are not legislators",
                            "President dominates; no House dissolution",
                            "Separation of powers",
                        ],
                    },
                ],
            },
            {
                "id": "ps-vs-pres-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Quick tell",
                "body": (
                    "Can the lower House sack the executive by no-confidence, and can the executive "
                    "dissolve that House? Yes → parliamentary. Fixed tenure + impeachment only → presidential."
                ),
            },
        ],
    },
    {
        "title": "Merits & Demerits",
        "slug": "ps-merits-demerits",
        "sort_order": 4,
        "summary": (
            "Responsibility, harmony, and wide representation vs instability, policy churn, "
            "and cabinet dictatorship."
        ),
        "body": (
            "## Merits\n"
            "1. Harmony between legislature and executive\n"
            "2. Responsible government (questions, adjournment, no-confidence)\n"
            "3. Prevents despotism — authority in a group, removable by House\n"
            "4. Ready alternative government (opposition leader as alternative PM — Jennings)\n"
            "5. Wide representation across sections and regions\n\n"
            "## Demerits\n"
            "1. Unstable government (no-confidence, defections, coalitions)\n"
            "2. No continuity of policies when parties change\n"
            "3. Dictatorship of the cabinet (Laski; Ramsay Muir) when majority is huge\n"
            "4. Against separation of powers — Bagehot: cabinet is the hyphen that joins\n"
            "5. Government by amateurs — ministers limited to MPs, not outside experts\n"
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "ps-merits-demerits-compare",
                "type": "comparison",
                "title": "Merits vs demerits",
                "columns": [
                    {
                        "id": "merits",
                        "heading": "Merits",
                        "points": [
                            "Harmony of legislature & executive",
                            "Responsible government (House control)",
                            "Checks despotism; group executive",
                            "Ready alternative government",
                            "Wide sectional / regional representation",
                        ],
                    },
                    {
                        "id": "demerits",
                        "heading": "Demerits",
                        "points": [
                            "Unstable government",
                            "Weak continuity of long-term policies",
                            "Cabinet dictatorship with absolute majority",
                            "Fusion against separation of powers",
                            "Government by amateurs (MP-only pool)",
                        ],
                    },
                ],
            },
            {
                "id": "ps-merits-demerits-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Named hooks",
                "body": (
                    "Bagehot — cabinet as hyphen joining legislature and executive. "
                    "Laski / Ramsay Muir — tyranny / dictatorship of the cabinet. "
                    "Mirror for USA: presidential gains stability and experts, loses daily responsibility."
                ),
            },
        ],
    },
    {
        "title": "Why India Adopted It",
        "slug": "ps-why-adopted",
        "sort_order": 5,
        "summary": (
            "Constituent Assembly preferred British parliamentary form for familiarity, "
            "responsibility, harmony, and plural representation."
        ),
        "body": (
            "## Four reasons (revision)\n\n"
            "1. **Familiarity** — parliamentary tradition under British rule (K.M. Munshi).\n"
            "2. **More responsibility than stability** — Ambedkar: US = more stable, less responsible; "
            "Britain = more responsible, less stable; Draft preferred responsibility.\n"
            "3. **Avoid legislature–executive conflicts** — infant democracy could not risk US-style feuds "
            "(K.T. Shah had favoured presidential).\n"
            "4. **Nature of Indian society** — heterogeneous / plural; easier to give sectional and "
            "regional representation in a ministry.\n\n"
            "**Swaran Singh Committee (1975):** system working well — no switch to presidential."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "ps-why-pillars",
                "type": "pillars",
                "title": "Why the founding fathers chose parliamentary form",
                "items": [
                    {
                        "id": "familiar",
                        "articles": "Munshi",
                        "label": "Familiarity",
                        "slug": "ps-why-adopted",
                        "detail": "Decades of responsible government under British rule — known path.",
                        "tone": "teal",
                    },
                    {
                        "id": "responsibility",
                        "articles": "Ambedkar",
                        "label": "Responsibility > stability",
                        "slug": "ps-why-adopted",
                        "detail": "US more stable; Britain more responsible — Draft chose responsibility.",
                        "tone": "olive",
                    },
                    {
                        "id": "harmony",
                        "articles": "3",
                        "label": "Avoid organ conflicts",
                        "slug": "ps-why-adopted",
                        "detail": "Infant democracy should not risk perpetual legislature–executive feud.",
                        "tone": "gold",
                    },
                    {
                        "id": "plural",
                        "articles": "4",
                        "label": "Plural society",
                        "slug": "ps-why-adopted",
                        "detail": "Ministry can mirror sections, interests, and regions — builds unity.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "ps-why-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Debate closure",
                "body": (
                    "Presidential plea existed in the CA (e.g. K.T. Shah). "
                    "Swaran Singh Committee (1975) reviewed and retained the parliamentary system."
                ),
            },
        ],
    },
    {
        "title": "India vs British Model",
        "slug": "ps-vs-british",
        "sort_order": 6,
        "summary": (
            "Same family, not a replica — republic, limited Parliament, flexible PM House, "
            "no legal responsibility, no shadow cabinet."
        ),
        "body": (
            "## Six differences\n\n"
            "1. **Republic vs monarchy** — elected President vs hereditary Crown.\n"
            "2. **Limited vs sovereign Parliament** — India limited by written Constitution, federalism, "
            "judicial review, FR; Britain has parliamentary sovereignty.\n"
            "3. **PM’s House** — Britain: must be Commons; India: **either House** "
            "(e.g. Indira 1966, Deve Gowda 1996, Manmohan Singh 2004 from Rajya Sabha).\n"
            "4. **Non-MP ministers** — India allows up to **6 months**; Britain usually MPs only.\n"
            "5. **Legal responsibility** — Britain: ministers countersign Head of State acts; "
            "India: no such system.\n"
            "6. **Shadow cabinet** — British opposition institution; **none in India**.\n"
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "ps-vs-uk-compare",
                "type": "comparison",
                "title": "Indian model vs British model",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Republican head of State (elected President)",
                            "Parliament not sovereign — constitutional limits",
                            "PM may be from either House",
                            "Non-MP minister allowed for 6 months",
                            "No legal responsibility / countersignature",
                            "No shadow cabinet",
                        ],
                    },
                    {
                        "id": "britain",
                        "heading": "Britain",
                        "points": [
                            "Monarchical head of State (hereditary)",
                            "Sovereignty of Parliament",
                            "PM must be from House of Commons",
                            "Ministers usually from Parliament only",
                            "Legal responsibility of ministers",
                            "Shadow cabinet of the opposition",
                        ],
                    },
                ],
            },
            {
                "id": "ps-vs-uk-callout",
                "type": "callout",
                "tone": "warning",
                "title": "Do not say",
                "body": (
                    "Do not call the Indian Parliament ‘sovereign’ like Britain. "
                    "Written Constitution + judicial review + FR + federalism limit it."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "ps-meaning"),
    (HUB_SLUG, "parent", "ps-features"),
    (HUB_SLUG, "parent", "ps-vs-presidential"),
    (HUB_SLUG, "parent", "ps-merits-demerits"),
    (HUB_SLUG, "parent", "ps-why-adopted"),
    (HUB_SLUG, "parent", "ps-vs-british"),
    ("ps-meaning", "related", "ps-features"),
    ("ps-features", "related", "ps-vs-presidential"),
    ("ps-vs-presidential", "related", "ps-merits-demerits"),
    ("ps-why-adopted", "related", "ps-vs-british"),
    ("ps-features", "related", "ps-vs-british"),
    ("sf-parliamentary", "related", HUB_SLUG),
]

AMENDMENTS = [
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Among other changes, strengthened the position that the President acts on "
            "the aid and advice of the Council of Ministers."
        ),
        "effect": "With the 44th Amendment, ministerial advice to the President is binding.",
        "concept_slugs": [HUB_SLUG, "ps-features"],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": (
            "Restored and clarified the binding character of ministerial advice to the President "
            "after Emergency-era changes."
        ),
        "effect": "Together with the 42nd Amendment, advice under Art. 74 is binding.",
        "concept_slugs": [HUB_SLUG, "ps-features"],
    },
]


class Command(BaseCommand):
    help = "Seed Parliamentary System chapter (Laxmikanth Ch.13)."

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
                "title": "Parliamentary System",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 13",
                "summary": (
                    "Visual revision of Ch.13 — meaning, eight features, India vs USA, "
                    "merits/demerits, why adopted, and India vs Britain."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Parliamentary System",
                "summary": (
                    "Responsible / Cabinet / Westminster government at Centre and in the states — "
                    "real executive accountable to the lower House."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **team accountable to the House** mental model, then "
                    "**Meaning** → **Features** → **vs Presidential**. "
                    "Finish with **Merits & demerits**, **Why adopted**, and **India ≠ Britain**. "
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
            ref="Laxmikanth Ch. 13",
            excerpt=(
                "Parliamentary System — Arts 74–75 & 163–164; features, contrasts, "
                "why adopted, India vs Britain."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 74 & 75",
            excerpt="Centre: Council of Ministers to aid and advise; collective responsibility to Lok Sabha.",
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 163 & 164",
            excerpt="States: parallel parliamentary executive (Governor / CM / Council of Ministers).",
            sort_order=2,
        )

        ps_slugs = set(by_slug.keys())
        related_outside = {"sf-parliamentary"}
        ConceptEdge.objects.filter(
            source__slug__in=ps_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=ps_slugs | related_outside).delete()

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

        for amd_data in AMENDMENTS:
            # Do not overwrite shared amendment blurbs owned by other chapter seeds.
            amendment = ConstitutionalAmendment.objects.filter(
                academy=academy, number=amd_data["number"]
            ).first()
            if amendment is None:
                payload = {k: v for k, v in amd_data.items() if k != "concept_slugs"}
                amendment = ConstitutionalAmendment.objects.create(
                    academy=academy, **payload
                )
            concepts = [
                by_slug[s] for s in amd_data["concept_slugs"] if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        # Ensure chapter sits under Part II if syllabus already created the section.
        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="system-of-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Parliamentary System chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(AMENDMENTS)} amendments linked."
            )
        )
