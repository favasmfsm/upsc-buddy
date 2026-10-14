"""Seed Laxmikanth Ch.5 Preamble of the Constitution (visual chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "preamble"
CHAPTER_SLUG = "preamble"

REVISION_PILLARS = [
    {
        "id": "ingredients",
        "articles": "4 components",
        "label": "Text & Ingredients",
        "slug": "pre-ingredients",
        "detail": "Source · Nature · Objectives · Date of adoption.",
        "tone": "teal",
    },
    {
        "id": "nature",
        "articles": "5 words",
        "label": "Nature of Indian State",
        "slug": "pre-nature-of-state",
        "detail": "Sovereign · Socialist · Secular · Democratic · Republic.",
        "tone": "olive",
    },
    {
        "id": "objectives",
        "articles": "JLEF",
        "label": "Objectives",
        "slug": "pre-objectives",
        "detail": "Justice · Liberty · Equality · Fraternity.",
        "tone": "gold",
    },
    {
        "id": "significance",
        "articles": "Quotes",
        "label": "Significance",
        "slug": "pre-significance",
        "detail": "Identity card · soul · key-note — match author to phrase.",
        "tone": "orange",
    },
    {
        "id": "part-of",
        "articles": "Cases",
        "label": "Part of the Constitution?",
        "slug": "pre-part-of-constitution",
        "detail": "Berubari → Kesavananda → LIC; non-justiciable.",
        "tone": "terracotta",
    },
    {
        "id": "amend",
        "articles": "Art. 368 · 42nd",
        "label": "Amendability",
        "slug": "pre-amendability",
        "detail": "Amendable, but basic features in the Preamble cannot be destroyed.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pre-identity-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Identity card",
        "topic_label": "Preamble",
        "subject_label": "Indian Constitution",
        "relation_label": "Helps you recall",
        "protects_from": [
            "Mixing adoption vs commencement dates",
            "Berubari vs Kesavananda on ‘part of’",
            "Forgetting 42nd words (Socialist, Secular, Integrity)",
            "Treating Preamble as justiciable",
        ],
        "insight": (
            "Palkhivala called the Preamble the identity card of the Constitution — "
            "scan ingredients and key words first, then part-of and amendability."
        ),
    },
    {
        "id": "pre-six-pillars",
        "type": "pillars",
        "title": "Six revision clusters",
        "items": REVISION_PILLARS,
    },
    {
        "id": "pre-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Route: Identity card → Ingredients → Nature (5) → Objectives (JLEF) → "
            "Significance quotes → Part of (Berubari/Kesavananda) → Amendability (42nd). "
            "Objectives Resolution (Nehru) is the source text; 42nd added Socialist, Secular, Integrity."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Text & Ingredients",
        "slug": "pre-ingredients",
        "sort_order": 1,
        "summary": "Four components: source of authority, nature of State, objectives, and date of adoption.",
        "body": (
            "## Text & ingredients\n\n"
            "The Preamble is the preface to the Constitution — based on the **Objectives Resolution** "
            "(Nehru; moved 13 Dec 1946, adopted 22 Jan 1947). "
            "It has been amended once by the **42nd Amendment (1976)**.\n\n"
            "### Four ingredients\n\n"
            "1. **Source of authority** — the people of India.\n"
            "2. **Nature of the Indian State** — sovereign, socialist, secular, democratic, republic.\n"
            "3. **Objectives** — justice, liberty, equality, fraternity.\n"
            "4. **Date of adoption** — 26 November 1949."
        ),
        "articles": [
            (
                "Preamble",
                "We, the people of India… adopt, enact and give to ourselves this Constitution.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pre-ing-pillars",
                "type": "pillars",
                "title": "Four ingredients",
                "items": [
                    {
                        "id": "source",
                        "articles": "We the People",
                        "label": "Source of authority",
                        "slug": "pre-ingredients",
                        "detail": "Constitution derives authority from the people of India.",
                        "tone": "teal",
                    },
                    {
                        "id": "nature",
                        "articles": "5 words",
                        "label": "Nature of State",
                        "slug": "pre-nature-of-state",
                        "detail": "Sovereign Socialist Secular Democratic Republic.",
                        "tone": "olive",
                    },
                    {
                        "id": "objectives",
                        "articles": "JLEF",
                        "label": "Objectives",
                        "slug": "pre-objectives",
                        "detail": "Justice, Liberty, Equality, Fraternity.",
                        "tone": "gold",
                    },
                    {
                        "id": "date",
                        "articles": "26 Nov 1949",
                        "label": "Date of adoption",
                        "slug": "pre-ingredients",
                        "detail": "Adopted/enacted on 26 November 1949 in the Constituent Assembly.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pre-ing-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Date trap",
                "body": (
                    "Preamble date = **26 Nov 1949** (adoption/enactment). "
                    "Constitution commenced = **26 Jan 1950**. Do not mix them."
                ),
            },
        ],
    },
    {
        "title": "Nature of the Indian State",
        "slug": "pre-nature-of-state",
        "sort_order": 2,
        "summary": "Five polity words: Sovereign, Socialist, Secular, Democratic, Republic.",
        "body": (
            "## Nature of the Indian State\n\n"
            "The Preamble declares India a **Sovereign Socialist Secular Democratic Republic**.\n\n"
            "- **Sovereign** — independent; no authority above; can acquire or cede territory. "
            "Commonwealth / UNO membership does **not** limit sovereignty.\n"
            "- **Socialist** — added by 42nd; made explicit what DPSP already implied. "
            "Indian brand = **democratic socialism** (mixed economy), not state socialism.\n"
            "- **Secular** — added by 42nd; positive secularism (equal status/support to all religions); "
            "Arts 25–28 already embodied it.\n"
            "- **Democratic** — popular sovereignty; India = **representative parliamentary** democracy; "
            "term covers political + social + economic democracy.\n"
            "- **Republic** — elected head (President) for a fixed term; sovereignty in the people; "
            "public offices open to all.\n\n"
            "Direct democracy devices (elsewhere, e.g. Switzerland): Referendum, Initiative, Recall, Plebiscite."
        ),
        "articles": [
            (
                "Articles 25–28",
                "Freedom of religion — secular content was in the Constitution before the word ‘secular’.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pre-nature-pillars",
                "type": "pillars",
                "title": "Five key words",
                "items": [
                    {
                        "id": "sovereign",
                        "articles": "External + internal",
                        "label": "Sovereign",
                        "slug": "pre-nature-of-state",
                        "detail": "Neither dependency nor dominion — free in internal and external affairs.",
                        "tone": "teal",
                    },
                    {
                        "id": "socialist",
                        "articles": "42nd",
                        "label": "Socialist",
                        "slug": "pre-nature-of-state",
                        "detail": "Democratic socialism / mixed economy; DPSP had socialist content already.",
                        "tone": "olive",
                    },
                    {
                        "id": "secular",
                        "articles": "42nd · 25–28",
                        "label": "Secular",
                        "slug": "pre-nature-of-state",
                        "detail": "Positive secularism — all religions equal status and support from the State.",
                        "tone": "gold",
                    },
                    {
                        "id": "democratic",
                        "articles": "Popular sovereignty",
                        "label": "Democratic",
                        "slug": "pre-nature-of-state",
                        "detail": "Representative parliamentary democracy; political + social + economic.",
                        "tone": "orange",
                    },
                    {
                        "id": "republic",
                        "articles": "Elected head",
                        "label": "Republic",
                        "slug": "pre-nature-of-state",
                        "detail": "President elected (indirectly) for 5 years — not a hereditary monarch.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "pre-nature-compare",
                "type": "comparison",
                "title": "Democratic socialism vs state socialism",
                "columns": [
                    {
                        "id": "demo",
                        "heading": "Democratic socialism (India)",
                        "points": [
                            "Mixed economy — public + private coexist",
                            "Ends poverty, ignorance, disease, inequality of opportunity",
                            "Blend of Marxism + Gandhism (lean Gandhian)",
                        ],
                    },
                    {
                        "id": "state",
                        "heading": "State / communistic socialism",
                        "points": [
                            "Nationalisation of all means of production",
                            "Abolition of private property",
                            "Not the Indian constitutional brand",
                        ],
                    },
                ],
            },
            {
                "id": "pre-nature-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Common traps",
                "body": (
                    "Commonwealth / UNO ≠ loss of sovereignty. "
                    "‘Socialist’ and ‘Secular’ were **added by 42nd** but the ideas were already "
                    "implicit (DPSP; Arts 25–28). Republic ≠ monarchy (Britain)."
                ),
            },
        ],
    },
    {
        "title": "Objectives — Justice, Liberty, Equality, Fraternity",
        "slug": "pre-objectives",
        "sort_order": 3,
        "summary": "JLEF goals secured mainly via Fundamental Rights and Directive Principles.",
        "body": (
            "## Objectives (JLEF)\n\n"
            "- **Justice** — social, economic, political (from the **Russian Revolution, 1917**); "
            "secured through FR + DPSP. Social + economic = distributive justice.\n"
            "- **Liberty** — thought, expression, belief, faith, worship (FR); "
            "qualified, not license. Liberty–Equality–Fraternity from the **French Revolution**.\n"
            "- **Equality** — status and opportunity: civic (Arts 14–18), political (Arts 325–326), "
            "economic (Art. 39 DPSP).\n"
            "- **Fraternity** — brotherhood via single citizenship + Art. 51A; assures dignity of the "
            "individual and **unity and integrity** of the nation (**integrity** added by 42nd).\n\n"
            "Ambedkar: liberty, equality, and fraternity form a **trinity** — divorce one and democracy fails."
        ),
        "articles": [
            (
                "Articles 14–18",
                "Civic equality — equality before law, non-discrimination, public employment, untouchability, titles.",
            ),
            (
                "Articles 325–326",
                "Political equality — electoral rolls; adult suffrage for Lok Sabha and assemblies.",
            ),
            (
                "Article 39",
                "DPSP — equal livelihood and equal pay for equal work (economic equality).",
            ),
            (
                "Article 51A",
                "Fundamental Duties — common brotherhood; dignity of women; unity and integrity.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pre-obj-pillars",
                "type": "pillars",
                "title": "Four objectives",
                "items": [
                    {
                        "id": "justice",
                        "articles": "SEP · Russia 1917",
                        "label": "Justice",
                        "slug": "pre-objectives",
                        "detail": "Social, economic, political — FR + DPSP; distributive justice.",
                        "tone": "teal",
                    },
                    {
                        "id": "liberty",
                        "articles": "FR · France",
                        "label": "Liberty",
                        "slug": "pre-objectives",
                        "detail": "Thought, expression, belief, faith, worship — qualified, not absolute.",
                        "tone": "olive",
                    },
                    {
                        "id": "equality",
                        "articles": "14–18 · 325–326 · 39",
                        "label": "Equality",
                        "slug": "pre-objectives",
                        "detail": "Civic, political, economic dimensions of status and opportunity.",
                        "tone": "gold",
                    },
                    {
                        "id": "fraternity",
                        "articles": "51A · 42nd",
                        "label": "Fraternity",
                        "slug": "pre-objectives",
                        "detail": "Dignity of individual + unity and integrity of the nation.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pre-obj-equality",
                "type": "comparison",
                "title": "Equality — three dimensions",
                "columns": [
                    {
                        "id": "civic",
                        "heading": "Civic (FR)",
                        "points": [
                            "Arts 14–18",
                            "Equality before law; no discrimination",
                            "Public employment; abolish untouchability & titles",
                        ],
                    },
                    {
                        "id": "pol-eco",
                        "heading": "Political & economic",
                        "points": [
                            "Political: Arts 325–326 (rolls; adult suffrage)",
                            "Economic: Art. 39 (livelihood; equal pay)",
                            "Status + opportunity in the Preamble",
                        ],
                    },
                ],
            },
            {
                "id": "pre-obj-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision anchors",
                "body": (
                    "Justice ← Russian Revolution. Liberty–Equality–Fraternity ← French Revolution. "
                    "Ambedkar trinity: do not divorce L–E–F. "
                    "**Integrity** rides with Fraternity via the 42nd Amendment."
                ),
            },
        ],
    },
    {
        "title": "Significance of the Preamble",
        "slug": "pre-significance",
        "sort_order": 4,
        "summary": "Philosophy and values of the Constitution — match famous labels to authors.",
        "body": (
            "## Significance\n\n"
            "The Preamble embodies the basic philosophy and fundamental values on which the "
            "Constitution rests — the vision of the Constituent Assembly.\n\n"
            "For prelims, lock **author → phrase** (below). Do not memorise full speeches."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pre-sig-pillars",
                "type": "pillars",
                "title": "Author → phrase (scan)",
                "items": [
                    {
                        "id": "palkhivala",
                        "articles": "Palkhivala",
                        "label": "Identity card",
                        "slug": "pre-significance",
                        "detail": "N.A. Palkhivala — identity card of the Constitution.",
                        "tone": "teal",
                    },
                    {
                        "id": "munshi",
                        "articles": "K.M. Munshi",
                        "label": "Horoscope",
                        "slug": "pre-significance",
                        "detail": "Horoscope of our sovereign democratic republic.",
                        "tone": "olive",
                    },
                    {
                        "id": "bhargava",
                        "articles": "Thakur Das Bhargava",
                        "label": "Soul / key / jewel",
                        "slug": "pre-significance",
                        "detail": "Soul, key, jewel, yardstick of the Constitution.",
                        "tone": "gold",
                    },
                    {
                        "id": "barker",
                        "articles": "Ernest Barker",
                        "label": "Key-note",
                        "slug": "pre-significance",
                        "detail": "Key-note to the Constitution; quoted at opening of his book.",
                        "tone": "orange",
                    },
                    {
                        "id": "hidayatullah",
                        "articles": "Hidayatullah",
                        "label": "Soul + solemn resolve",
                        "slug": "pre-significance",
                        "detail": "More than a US-style declaration — soul; alterable only by revolution.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "pre-sig-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Quote trap",
                "body": (
                    "UPSC loves matching lists. Remember the **short label**, not the paragraph. "
                    "‘Identity card’ = Palkhivala; ‘horoscope’ = Munshi; ‘key-note’ = Barker."
                ),
            },
        ],
    },
    {
        "title": "Preamble as Part of the Constitution",
        "slug": "pre-part-of-constitution",
        "sort_order": 5,
        "summary": "Berubari said not a part; Kesavananda and LIC held it is — still non-justiciable.",
        "body": (
            "## Is the Preamble part of the Constitution?\n\n"
            "- **Berubari Union (1960)** — Preamble is a key to the makers’ minds and may aid "
            "interpretation, but is **not** a part of the Constitution.\n"
            "- **Kesavananda Bharati (1973)** — rejected Berubari on this point; Preamble **is** a part; "
            "read the Constitution in its light.\n"
            "- **LIC of India (1995)** — reaffirmed: integral part of the Constitution.\n\n"
            "Historically the Assembly enacted the Preamble **after** the rest (to keep it in conformity) "
            "and adopted the motion that it ‘stands part of the Constitution’.\n\n"
            "### Two hard limits\n\n"
            "1. Neither a **source of power** nor a **prohibition** on the legislature.\n"
            "2. **Non-justiciable** — not enforceable in courts."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pre-part-timeline",
                "type": "timeline",
                "title": "Part of the Constitution? — case path",
                "events": [
                    {
                        "id": "e1960",
                        "year": 1960,
                        "label": "Berubari Union",
                        "detail": "Key to makers’ minds — but not a part of the Constitution.",
                    },
                    {
                        "id": "e1973",
                        "year": 1973,
                        "label": "Kesavananda Bharati",
                        "detail": "Preamble is a part; interpret Constitution in its light.",
                    },
                    {
                        "id": "e1995",
                        "year": 1995,
                        "label": "LIC of India",
                        "detail": "Reaffirmed — integral part of the Constitution.",
                    },
                ],
            },
            {
                "id": "pre-part-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Two limits (always)",
                "body": (
                    "Even as a part of the Constitution: Preamble is **non-justiciable**, and it is "
                    "**neither** a source of legislative power **nor** a prohibition on legislature."
                ),
            },
        ],
    },
    {
        "title": "Amendability of the Preamble",
        "slug": "pre-amendability",
        "sort_order": 6,
        "summary": "Amendable under Art. 368, but basic features in the Preamble cannot be destroyed; 42nd is the only amendment.",
        "body": (
            "## Amendability\n\n"
            "Issue first raised in **Kesavananda Bharati (1973)**. "
            "Court held: Preamble **is** a part → it **can** be amended under Art. 368, "
            "but **basic features / elements** reflected in the Preamble cannot be altered so as to "
            "destroy the Constitution’s identity.\n\n"
            "Amended **only once** — **42nd Constitutional Amendment Act, 1976** — added "
            "**Socialist, Secular, Integrity**. That amendment was held valid."
        ),
        "articles": [
            (
                "Article 368",
                "Power of Parliament to amend the Constitution — subject to basic structure limits.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pre-amd-compare",
                "type": "comparison",
                "title": "What Kesavananda allows",
                "columns": [
                    {
                        "id": "can",
                        "heading": "Can amend",
                        "points": [
                            "Preamble is part of the Constitution",
                            "Art. 368 can amend the Preamble",
                            "42nd CAA (1976) held valid",
                        ],
                    },
                    {
                        "id": "cannot",
                        "heading": "Cannot destroy",
                        "points": [
                            "Basic elements / features in the Preamble",
                            "Removing them would change the Constitution’s identity",
                            "Basic structure limit on constituent power",
                        ],
                    },
                ],
            },
            {
                "id": "pre-amd-timeline",
                "type": "timeline",
                "title": "Only amendment so far",
                "events": [
                    {
                        "id": "e1949",
                        "year": 1949,
                        "label": "Original Preamble",
                        "detail": "No Socialist / Secular / Integrity in the text yet.",
                    },
                    {
                        "id": "e1973",
                        "year": 1973,
                        "label": "Kesavananda",
                        "detail": "Amendable, but basic features cannot be destroyed.",
                    },
                    {
                        "id": "e1976",
                        "year": 1976,
                        "label": "42nd Amendment",
                        "detail": "Added Socialist, Secular, Integrity — only amendment; valid.",
                    },
                ],
            },
            {
                "id": "pre-amd-tip",
                "type": "callout",
                "tone": "tip",
                "title": "42nd trio",
                "body": (
                    "Memorise the three words: **Socialist · Secular · Integrity**. "
                    "Only amendment to the Preamble so far."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pre-ingredients"),
    (HUB_SLUG, "parent", "pre-nature-of-state"),
    (HUB_SLUG, "parent", "pre-objectives"),
    (HUB_SLUG, "parent", "pre-significance"),
    (HUB_SLUG, "parent", "pre-part-of-constitution"),
    (HUB_SLUG, "parent", "pre-amendability"),
    ("pre-ingredients", "related", "pre-nature-of-state"),
    ("pre-ingredients", "related", "pre-objectives"),
    ("pre-nature-of-state", "related", "pre-objectives"),
    ("pre-part-of-constitution", "related", "pre-amendability"),
    ("pre-objectives", "related", "fundamental-rights"),
    ("pre-objectives", "related", "directive-principles"),
    ("pre-nature-of-state", "related", "salient-features-constitution"),
    (HUB_SLUG, "related", "salient-features-constitution"),
]

SAMPLE_PYQS = [
    (
        2015,
        "The Preamble to the Constitution of India is:",
        "A part of the Constitution (Kesavananda; LIC) — but non-justiciable.",
        ["pre-part-of-constitution", HUB_SLUG],
    ),
    (
        2017,
        "Which one of the following objectives is not embodied in the Preamble to the Constitution of India?",
        "Scan JLEF + nature words; anything outside that set is the distractor.",
        ["pre-objectives", "pre-nature-of-state"],
    ),
    (
        2020,
        "The Preamble of the Constitution of India has been amended:",
        "Only once — 42nd Amendment (1976) — Socialist, Secular, Integrity.",
        ["pre-amendability", HUB_SLUG],
    ),
    (
        2013,
        "Which of the following are included in the original Constitution of India as Directive Principles / ideals later made explicit in the Preamble?",
        "Socialist and Secular content existed before 42nd; words were added later.",
        ["pre-nature-of-state"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Berubari Union Reference",
        "slug": "berubari-union",
        "parties": "Reference by the President of India (Berubari Union)",
        "year": 1960,
        "court": CaseLaw.Court.SC,
        "summary": "Preamble aids interpretation but was held not to be a part of the Constitution.",
        "holding": (
            "The Preamble shows the general purposes behind the Constitution and may assist "
            "interpretation, but (as then held) it is not a part of the Constitution."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "pre-part-of-constitution",
        ],
    },
    {
        "title": "Kesavananda Bharati v. State of Kerala",
        "slug": "kesavananda-bharati",
        "parties": "Kesavananda Bharati v. State of Kerala",
        "year": 1973,
        "court": CaseLaw.Court.SC,
        "summary": "Preamble is part of the Constitution; amendable but basic features cannot be destroyed.",
        "holding": (
            "The Preamble is a part of the Constitution. It can be amended under Art. 368, "
            "but the basic elements or fundamental features contained in the Preamble cannot be altered."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "pre-part-of-constitution",
            "pre-amendability",
        ],
    },
    {
        "title": "LIC of India v. Consumer Education & Research Centre",
        "slug": "lic-of-india-preamble",
        "parties": "LIC of India v. Consumer Education and Research Centre",
        "year": 1995,
        "court": CaseLaw.Court.SC,
        "summary": "Reaffirmed that the Preamble is an integral part of the Constitution.",
        "holding": (
            "The Preamble is an integral part of the Constitution."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "pre-part-of-constitution",
        ],
    },
]

AMENDMENTS = [
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Only amendment to the Preamble so far — added Socialist, Secular, and Integrity."
        ),
        "effect": (
            "Preamble text gained Socialist and Secular in the nature clause, "
            "and Integrity alongside unity of the nation."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "pre-nature-of-state",
            "pre-objectives",
            "pre-amendability",
            "pre-ingredients",
        ],
    },
]


class Command(BaseCommand):
    help = "Seed Preamble of the Constitution chapter (Laxmikanth Ch.5)."

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
                "title": "Preamble of the Constitution",
                "sort_order": 5,
                "book_ref": "Laxmikanth 8th Ed, Ch. 5",
                "summary": (
                    "Visual revision of Ch.5 — identity-card mental model, ingredients, "
                    "key words, significance, part-of controversy, and amendability."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Preamble of the Constitution",
                "summary": (
                    "Identity card of the Constitution — ingredients, key words, "
                    "significance, part-of status, and amendability."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **identity-card mental model** (Palkhivala), then scan "
                    "**ingredients** and the **nine key words** (Nature + Objectives). "
                    "Lock Berubari → Kesavananda → LIC and the **42nd trio**. "
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
            ref="Laxmikanth Ch. 5",
            excerpt="Preamble of the Constitution — text, key words, significance, part-of, amendability.",
            sort_order=0,
        )

        pre_slugs = set(by_slug.keys())
        related_outside = {
            "fundamental-rights",
            "directive-principles",
            "salient-features-constitution",
        }
        ConceptEdge.objects.filter(
            source__slug__in=pre_slugs, source__subject=subject
        ).filter(
            target__slug__in=pre_slugs | related_outside
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

        for year, question, answer, slugs in SAMPLE_PYQS:
            pyq, _ = PYQ.objects.get_or_create(
                academy=academy,
                year=year,
                question=question,
                defaults={"answer_key": answer},
            )
            if not pyq.answer_key and answer:
                pyq.answer_key = answer
                pyq.save(update_fields=["answer_key"])
            concepts = [by_slug[s] for s in slugs if s in by_slug]
            if concepts:
                pyq.concepts.add(*concepts)

        for case_data in LANDMARK_CASES:
            payload = {k: v for k, v in case_data.items() if k != "concept_slugs"}
            case, _ = CaseLaw.objects.update_or_create(
                academy=academy,
                slug=payload["slug"],
                defaults=payload,
            )
            concepts = [
                by_slug[s]
                for s in case_data["concept_slugs"]
                if s in by_slug
            ]
            if concepts:
                existing = list(case.concepts.all())
                case.concepts.set({*existing, *concepts})

        for amd_data in AMENDMENTS:
            payload = {k: v for k, v in amd_data.items() if k != "concept_slugs"}
            amendment, _ = ConstitutionalAmendment.objects.update_or_create(
                academy=academy,
                number=payload["number"],
                defaults=payload,
            )
            concepts = [
                by_slug[s]
                for s in amd_data["concept_slugs"]
                if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Preamble chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments."
            )
        )
