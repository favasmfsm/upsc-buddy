"""Seed Laxmikanth Ch.12 Basic Structure of the Constitution (visual revision)."""

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

HUB_SLUG = "basic-structure"
CHAPTER_SLUG = "basic-structure"

ENTRY_PILLARS = [
    {
        "id": "emergence",
        "articles": "1951 → 1980",
        "label": "Emergence",
        "slug": "bs-emergence",
        "detail": "Case ping-pong with Parliament until Kesavananda → Minerva → Waman Rao.",
        "tone": "teal",
    },
    {
        "id": "present",
        "articles": "Art. 368",
        "label": "Present rule",
        "slug": "bs-present-rule",
        "detail": "Amend any part incl. FR — but not the basic structure.",
        "tone": "olive",
    },
    {
        "id": "elements",
        "articles": "20 → 5 themes",
        "label": "Elements",
        "slug": "bs-elements",
        "detail": "Scan themed groups; SC never gave an exhaustive closed list.",
        "tone": "gold",
    },
    {
        "id": "case-map",
        "articles": "Table 12.1",
        "label": "Case → element map",
        "slug": "bs-case-element-map",
        "detail": "Core cases expanded; remaining Table 12.1 cases as one-liners.",
        "tone": "orange",
    },
    {
        "id": "anchors",
        "articles": "Prelims / Mains",
        "label": "Exam anchors",
        "slug": "bs-exam-anchors",
        "detail": "Golak vs Kesavananda; 24th vs 42nd vs Minerva; 24 Apr 1973 cut-off.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "bs-foundation-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Foundation",
        "topic_label": "Basic Structure",
        "subject_label": "Article 368",
        "relation_label": "Blocks you from",
        "protects_from": [
            "Treating Art. 368 as unlimited",
            "Saying FR can never be amended",
            "Memorising 20 features as a closed list",
            "Mixing Golak Nath with Kesavananda",
        ],
        "insight": (
            "The Constitution can be renovated under Art. 368 — "
            "but Parliament cannot dig out the foundation (basic structure)."
        ),
    },
    {
        "id": "bs-entry-pillars",
        "type": "pillars",
        "title": "Five revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "bs-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Present position: Parliament may amend any part including Fundamental Rights "
            "under Art. 368, but not the basic structure. "
            "The Supreme Court has not exhaustively defined the list — features emerge case by case. "
            "Start with Emergence, then Present rule."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Emergence of the Doctrine",
        "slug": "bs-emergence",
        "sort_order": 1,
        "summary": (
            "From Shankari Prasad to Waman Rao — Parliament vs SC ping-pong that birthed "
            "and locked the basic structure doctrine."
        ),
        "body": (
            "## Emergence (revision spine)\n\n"
            "**Question:** Can Parliament amend Fundamental Rights under Art. 368?\n\n"
            "- **Shankari Prasad (1951) / Sajjan Singh (1964):** Yes. Art. 13 ‘law’ = ordinary laws only; "
            "amendment Acts are not void under Art. 13.\n"
            "- **Golak Nath (1967):** No. FR are transcendental; amendment Act is also ‘law’ under Art. 13.\n"
            "- **24th Amendment (1971):** Parliament’s reply — Art. 13 & 368 amended to allow abridging FR.\n"
            "- **Kesavananda Bharati (1973):** Overrules Golak; upholds 24th; invents **basic structure** limit.\n"
            "- **Indira Nehru Gandhi (1975):** Applies doctrine; strikes 39th Amdt clause shielding PM/Speaker elections.\n"
            "- **42nd Amendment (1976):** Claims unlimited amending power; bars court challenge.\n"
            "- **Minerva Mills (1980):** Invalidates that claim — limited amending power is itself basic.\n"
            "- **Waman Rao (1980):** Doctrine applies to amendments **after 24 April 1973**.\n\n"
            "Scan the timeline; drill exam traps in Exam anchors."
        ),
        "articles": [
            (
                "Art. 13 & Art. 368",
                "Emergence turns on whether amendment Acts are ‘law’ under Art. 13 and how far Art. 368 reaches.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "bs-emergence-timeline",
                "type": "timeline",
                "title": "Doctrine birth (1951 → 1980)",
                "events": [
                    {
                        "id": "e1951",
                        "year": 1951,
                        "label": "Shankari Prasad",
                        "detail": "FR amendable; Art. 13 ≠ constitutional amendments.",
                    },
                    {
                        "id": "e1964",
                        "year": 1964,
                        "label": "Sajjan Singh",
                        "detail": "Reaffirms Shankari — amendment not ‘law’ under Art. 13.",
                    },
                    {
                        "id": "e1967",
                        "year": 1967,
                        "label": "Golak Nath",
                        "detail": "FR immutable via amendment; amendment = law under Art. 13.",
                    },
                    {
                        "id": "e1971",
                        "year": 1971,
                        "label": "24th Amendment",
                        "detail": "Parliament restores power to abridge FR under Art. 368.",
                    },
                    {
                        "id": "e1973",
                        "year": 1973,
                        "label": "Kesavananda Bharati",
                        "detail": "24th upheld; Golak overruled; basic structure doctrine born.",
                    },
                    {
                        "id": "e1975",
                        "year": 1975,
                        "label": "Indira Gandhi (Election Case)",
                        "detail": "39th Amdt clause on PM/Speaker elections struck — basic structure.",
                    },
                    {
                        "id": "e1976",
                        "year": 1976,
                        "label": "42nd Amendment",
                        "detail": "Claims no limit on constituent power; bars judicial challenge.",
                    },
                    {
                        "id": "e1980a",
                        "year": 1980,
                        "label": "Minerva Mills",
                        "detail": "Unlimited power clause void; limited amending power is basic.",
                    },
                    {
                        "id": "e1980b",
                        "year": 1980,
                        "label": "Waman Rao",
                        "detail": "Basic structure test for amendments after 24 Apr 1973.",
                    },
                ],
            },
            {
                "id": "bs-emergence-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Memory chain",
                "body": (
                    "Shankari/Sajjan → Golak → 24th → Kesavananda → Indira → 42nd → Minerva → Waman Rao. "
                    "Parliament reacts; Court redraws the line."
                ),
            },
        ],
    },
    {
        "title": "Present Rule under Article 368",
        "slug": "bs-present-rule",
        "sort_order": 2,
        "summary": (
            "Parliament can amend any part of the Constitution including FR — without destroying "
            "the basic structure."
        ),
        "body": (
            "## Present position (exam one-liner)\n\n"
            "Under **Article 368**, Parliament may amend **any part** of the Constitution — "
            "including Fundamental Rights — **but not** the **basic structure**.\n\n"
            "- A Fundamental Right that is part of the basic structure cannot be abridged/taken away "
            "in a way that destroys that structure.\n"
            "- The Supreme Court has **not** given an exhaustive closed list of basic features; "
            "elements emerge from judgements.\n"
            "- **Minerva line:** the amending power is limited; Parliament cannot enlarge that limited "
            "power into an unlimited one.\n\n"
            "Use the flowchart: amendability ≠ immunity from basic-structure review."
        ),
        "articles": [
            (
                "Article 368",
                "Constituent power to amend — limited by the basic structure doctrine.",
            ),
            (
                "Article 13",
                "After 24th Amdt / Kesavananda: FR can be amended by constitutional amendment, "
                "subject to basic structure.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "bs-present-flow",
                "type": "flowchart",
                "title": "Can Parliament amend this?",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "Proposed Art. 368 amendment",
                        "detail": "Any part of the Constitution, including FR.",
                        "options": [
                            {"label": "Does it touch the foundation?", "next": "test"},
                        ],
                    },
                    {
                        "id": "test",
                        "label": "Basic structure test",
                        "detail": "Would it alter / destroy a basic feature?",
                        "options": [
                            {"label": "No — only ordinary change", "next": "ok"},
                            {"label": "Yes — hits a basic feature", "next": "void"},
                        ],
                    },
                    {
                        "id": "ok",
                        "label": "Valid (in principle)",
                        "detail": "Amendable under Art. 368 — still open to other constitutional tests.",
                    },
                    {
                        "id": "void",
                        "label": "Beyond amending power",
                        "detail": "Invalid to the extent it damages the basic structure (Kesavananda / Minerva).",
                    },
                ],
            },
            {
                "id": "bs-present-compare",
                "type": "comparison",
                "title": "What Parliament can vs cannot do",
                "columns": [
                    {
                        "id": "can",
                        "heading": "Can (Art. 368)",
                        "points": [
                            "Amend any part of the Constitution",
                            "Abridge or take away FR (post-Kesavananda)",
                            "Rewrite procedures within amending power",
                        ],
                    },
                    {
                        "id": "cannot",
                        "heading": "Cannot",
                        "points": [
                            "Destroy / alter the basic structure",
                            "Convert limited amending power into unlimited power",
                            "Exclude judicial review of that core limit (Minerva)",
                        ],
                    },
                ],
            },
            {
                "id": "bs-present-tip",
                "type": "callout",
                "tone": "warning",
                "title": "Trap",
                "body": (
                    "Do not say ‘FR cannot be amended’ (that was Golak Nath). "
                    "Say: FR can be amended, but not if it destroys the basic structure."
                ),
            },
        ],
    },
    {
        "title": "Elements of the Basic Structure",
        "slug": "bs-elements",
        "sort_order": 3,
        "summary": (
            "Twenty features from judgements, grouped into five themes for scanning — not a closed list."
        ),
        "body": (
            "## Elements (scan, don’t dump)\n\n"
            "Laxmikanth lists ~20 features drawn from various judgements. "
            "Treat them as **illustrative**, not a statute schedule.\n\n"
            "### Theme map\n"
            "1. **Polity identity** — supremacy; sovereign/democratic/republic; secular; federal; "
            "unity & integrity; welfare state; parliamentary system.\n"
            "2. **Rights & justice** — essence of FR; FR–DPSP harmony; equality; freedom & dignity; "
            "effective access to justice.\n"
            "3. **Judicial core** — judicial review; independence of judiciary; SC powers "
            "(Arts 32, 136, 141, 142); HC powers (Arts 226, 227).\n"
            "4. **Democratic process** — free & fair elections; rule of law; separation of powers.\n"
            "5. **Amending limit** — limited power of Parliament to amend the Constitution.\n\n"
            "Open the case→element map when a Prelims question names a judgement."
        ),
        "articles": [
            (
                "Arts 32, 136, 141, 142",
                "SC powers repeatedly treated as basic (e.g. Delhi Judicial Service; Ram Jethmalani).",
            ),
            (
                "Arts 226 & 227",
                "HC writ / supervisory powers as basic (L. Chandra Kumar; Madras Bar Association).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "bs-element-themes",
                "type": "pillars",
                "title": "Five theme groups (20 features)",
                "items": [
                    {
                        "id": "polity",
                        "articles": "Theme 1",
                        "label": "Polity identity",
                        "slug": "bs-elements",
                        "detail": (
                            "Supremacy of Constitution · Sovereign democratic republic · Secular · "
                            "Federal · Unity & integrity · Welfare state · Parliamentary system"
                        ),
                        "tone": "teal",
                    },
                    {
                        "id": "rights",
                        "articles": "Theme 2",
                        "label": "Rights & justice",
                        "slug": "bs-elements",
                        "detail": (
                            "Essence of FR · FR–DPSP harmony · Equality · Freedom & dignity · "
                            "Effective access to justice"
                        ),
                        "tone": "olive",
                    },
                    {
                        "id": "judicial",
                        "articles": "Theme 3",
                        "label": "Judicial core",
                        "slug": "bs-elements",
                        "detail": (
                            "Judicial review · Independence of judiciary · SC Arts 32/136/141/142 · "
                            "HC Arts 226/227"
                        ),
                        "tone": "gold",
                    },
                    {
                        "id": "demo",
                        "articles": "Theme 4",
                        "label": "Democratic process",
                        "slug": "bs-elements",
                        "detail": "Free & fair elections · Rule of law · Separation of powers",
                        "tone": "orange",
                    },
                    {
                        "id": "amend",
                        "articles": "Theme 5",
                        "label": "Amending limit",
                        "slug": "bs-elements",
                        "detail": "Limited power of Parliament to amend the Constitution (Minerva)",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "bs-elements-callout",
                "type": "callout",
                "tone": "note",
                "title": "Authoring rule for exams",
                "body": (
                    "Never claim the Court published one fixed list of 20. "
                    "Say: ‘Among features recognised in judgements are…’ then pick the relevant ones."
                ),
            },
        ],
    },
    {
        "title": "Case → Element Map",
        "slug": "bs-case-element-map",
        "sort_order": 4,
        "summary": (
            "Compressed Table 12.1 — core cases with elements; remaining cases as one-line pegs."
        ),
        "body": (
            "## Table 12.1 compressed\n\n"
            "### Core (memorise elements)\n"
            "- **Kesavananda (1973):** supremacy; separation of powers; republic & democracy; secular; "
            "federal; sovereignty & unity; freedom & dignity; welfare state; parliamentary system.\n"
            "- **Indira Gandhi (1975):** sovereign democratic republic; equality; secularism & freedom "
            "of religion; rule of law; judicial review; free & fair elections.\n"
            "- **Minerva Mills (1980):** limited amending power; judicial review; FR–DPSP harmony.\n"
            "- **S.R. Bommai (1994):** federalism; secularism; democracy; unity & integrity; social justice; "
            "judicial review.\n"
            "- **I.R. Coelho (2007) — IX Schedule Case:** rule of law; separation of powers; essence of FR; "
            "judicial review; equality.\n\n"
            "### One-liners (recognition)\n"
            "Central Coal Fields — access to justice · Bhim Singhji — welfare state · "
            "Sampath Kumar / Sambamurthy — rule of law + JR · Delhi Judicial Service — SC 32/136/141/142 · "
            "Indra Sawhney — rule of law · Kumar Padma Prasad / All India Judges — independence of judiciary · "
            "Kihoto Hollohan — free & fair elections + SDR structure · Raghunath Rao — equality + unity · "
            "L. Chandra Kumar — HC 226/227 · Indra Sawhney II / Nagaraj — equality · "
            "Kuldip Nayar — democracy + elections · Ram Jethmalani — Art. 32 · "
            "Namit Sharma — freedom & dignity · Madras Bar — JR + HC 226/227.\n\n"
            "Drill only the core five for recall; use one-liners for match-the-following."
        ),
        "articles": [
            (
                "Laxmikanth Table 12.1",
                "Evolution of basic structure elements as declared case by case.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "bs-core-case-pillars",
                "type": "pillars",
                "title": "Core cases → key elements",
                "items": [
                    {
                        "id": "kesavananda",
                        "articles": "1973",
                        "label": "Kesavananda Bharati",
                        "slug": "bs-case-element-map",
                        "detail": (
                            "Supremacy · SoP · Republic/democracy · Secular · Federal · Unity · "
                            "Dignity · Welfare · Parliamentary system"
                        ),
                        "tone": "teal",
                    },
                    {
                        "id": "indira",
                        "articles": "1975",
                        "label": "Indira Nehru Gandhi",
                        "slug": "bs-case-element-map",
                        "detail": (
                            "Sovereign democratic republic · Equality · Secularism · Rule of law · "
                            "Judicial review · Free & fair elections"
                        ),
                        "tone": "olive",
                    },
                    {
                        "id": "minerva",
                        "articles": "1980",
                        "label": "Minerva Mills",
                        "slug": "bs-case-element-map",
                        "detail": "Limited amending power · Judicial review · FR–DPSP harmony",
                        "tone": "gold",
                    },
                    {
                        "id": "bommai",
                        "articles": "1994",
                        "label": "S.R. Bommai",
                        "slug": "bs-case-element-map",
                        "detail": (
                            "Federalism · Secularism · Democracy · Unity & integrity · "
                            "Social justice · Judicial review"
                        ),
                        "tone": "orange",
                    },
                    {
                        "id": "coelho",
                        "articles": "2007",
                        "label": "I.R. Coelho (IX Schedule)",
                        "slug": "bs-case-element-map",
                        "detail": (
                            "Rule of law · Separation of powers · Essence of FR · "
                            "Judicial review · Equality"
                        ),
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "bs-map-timeline",
                "type": "timeline",
                "title": "High-yield extras after 1980",
                "events": [
                    {
                        "id": "t1986",
                        "year": 1986,
                        "label": "Sampath Kumar / Sambamurthy",
                        "detail": "Rule of law + judicial review.",
                    },
                    {
                        "id": "t1992",
                        "year": 1992,
                        "label": "Indra Sawhney / Kihoto",
                        "detail": "Rule of law; free & fair elections (defection case).",
                    },
                    {
                        "id": "t1994",
                        "year": 1994,
                        "label": "S.R. Bommai",
                        "detail": "Federalism + secularism package.",
                    },
                    {
                        "id": "t1997",
                        "year": 1997,
                        "label": "L. Chandra Kumar",
                        "detail": "HC powers under Arts 226 & 227.",
                    },
                    {
                        "id": "t2007",
                        "year": 2007,
                        "label": "I.R. Coelho",
                        "detail": "IX Schedule laws open to basic-structure review.",
                    },
                ],
            },
            {
                "id": "bs-map-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims peg",
                "body": (
                    "If the question says ‘IX Schedule Case’, think Coelho — rule of law, SoP, "
                    "essence of FR, JR, equality."
                ),
            },
        ],
    },
    {
        "title": "Exam Anchors",
        "slug": "bs-exam-anchors",
        "sort_order": 5,
        "summary": (
            "High-yield contrasts: Golak vs Kesavananda, 24th vs 42nd vs Minerva, and the "
            "24 April 1973 cut-off."
        ),
        "body": (
            "## Exam anchors\n\n"
            "### Golak Nath vs Kesavananda\n"
            "- **Golak:** FR cannot be abridged by amendment (amendment = Art. 13 law).\n"
            "- **Kesavananda:** Golak overruled; 24th upheld; FR amendable **subject to** basic structure.\n\n"
            "### 24th vs 42nd vs Minerva\n"
            "- **24th (1971):** Restores power to amend FR — **upheld** in Kesavananda.\n"
            "- **42nd (1976):** Claims unlimited constituent power; bars court challenge — "
            "**struck** in Minerva (limited power cannot be made unlimited).\n\n"
            "### Waman Rao date\n"
            "- Basic structure doctrine applies to constitutional amendments enacted **after "
            "24 April 1973** (date of Kesavananda judgement).\n\n"
            "### Popular names\n"
            "- Kesavananda = Fundamental Rights Case · Indira Gandhi = Election Case · "
            "Coelho = IX Schedule Case · Indra Sawhney = Mandal Case · Kihoto = Defection Case."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "bs-golak-kesavananda",
                "type": "comparison",
                "title": "Golak Nath vs Kesavananda",
                "columns": [
                    {
                        "id": "golak",
                        "heading": "Golak Nath (1967)",
                        "points": [
                            "FR transcendental / immutable via amendment",
                            "Amendment Act = ‘law’ under Art. 13",
                            "Parliament cannot abridge FR by Art. 368",
                        ],
                    },
                    {
                        "id": "kesavananda",
                        "heading": "Kesavananda (1973)",
                        "points": [
                            "Overrules Golak; upholds 24th Amendment",
                            "Parliament may abridge FR",
                            "But cannot alter the basic structure",
                        ],
                    },
                ],
            },
            {
                "id": "bs-amd-compare",
                "type": "comparison",
                "title": "24th vs 42nd (and Minerva)",
                "columns": [
                    {
                        "id": "a24",
                        "heading": "24th Amendment (1971)",
                        "points": [
                            "Amends Arts 13 & 368",
                            "Explicit power to abridge FR",
                            "Upheld in Kesavananda",
                        ],
                    },
                    {
                        "id": "a42",
                        "heading": "42nd Amendment (1976)",
                        "points": [
                            "Claims no limit on constituent power",
                            "Bars judicial challenge to amendments",
                            "Key clause invalidated in Minerva Mills",
                        ],
                    },
                ],
            },
            {
                "id": "bs-anchors-callout",
                "type": "callout",
                "tone": "warning",
                "title": "Date to lock",
                "body": (
                    "Waman Rao: basic structure review for amendments after **24 April 1973**. "
                    "Minerva one-liner: donee of a limited power cannot convert it into an unlimited one."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "bs-emergence"),
    (HUB_SLUG, "parent", "bs-present-rule"),
    (HUB_SLUG, "parent", "bs-elements"),
    (HUB_SLUG, "parent", "bs-case-element-map"),
    (HUB_SLUG, "parent", "bs-exam-anchors"),
    ("bs-emergence", "related", "bs-present-rule"),
    ("bs-emergence", "related", "bs-exam-anchors"),
    ("bs-present-rule", "related", "bs-elements"),
    ("bs-elements", "related", "bs-case-element-map"),
    ("bs-case-element-map", "related", "bs-exam-anchors"),
    (HUB_SLUG, "related", "article-368"),
    (HUB_SLUG, "related", "judicial-review"),
    (HUB_SLUG, "related", "fundamental-rights"),
    ("bs-present-rule", "related", "article-368"),
    ("bs-elements", "related", "judicial-review"),
]

SAMPLE_PYQS = [
    (
        2021,
        "Constitutional government means...",
        "Limited government; supremacy of constitution; often linked to basic structure and judicial review.",
        [HUB_SLUG, "bs-present-rule"],
    ),
    (
        2019,
        "Which of the following are regarded as basic features / basic structure themes in Indian constitutional law?",
        "Illustrative: supremacy of Constitution, judicial review, federalism, secularism, free & fair elections, "
        "limited amending power — list is judicial, not exhaustive.",
        ["bs-elements", HUB_SLUG],
    ),
    (
        2013,
        "The basic structure doctrine was propounded / crystallised by the Supreme Court in:",
        "Kesavananda Bharati v. State of Kerala (1973). Golak Nath (1967) restricted FR amendment but did not "
        "lay down the basic structure doctrine as such.",
        ["bs-emergence", "bs-exam-anchors"],
    ),
    (
        2006,
        "Consider statements on the amending power of Parliament under Article 368 and judicial review.",
        "Parliament’s amending power is wide but not unlimited — basic structure; Minerva Mills struck attempts "
        "to exclude judicial review of that limit.",
        ["bs-present-rule", "bs-exam-anchors"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Shankari Prasad v. Union of India",
        "slug": "shankari-prasad",
        "parties": "Shankari Prasad v. Union of India",
        "year": 1951,
        "court": CaseLaw.Court.SC,
        "summary": "First round on amending FR — Parliament can amend FR under Art. 368.",
        "holding": (
            "‘Law’ in Art. 13 means ordinary laws, not constitutional amendment Acts; "
            "Parliament may abridge FR by amendment."
        ),
        "concept_slugs": [HUB_SLUG, "bs-emergence"],
    },
    {
        "title": "Sajjan Singh v. State of Rajasthan",
        "slug": "sajjan-singh",
        "parties": "Sajjan Singh v. State of Rajasthan",
        "year": 1964,
        "court": CaseLaw.Court.SC,
        "summary": "Reaffirms Shankari Prasad on amendability of Fundamental Rights.",
        "holding": (
            "A constitutional amendment under Art. 368 is not a ‘law’ within Art. 13."
        ),
        "concept_slugs": [HUB_SLUG, "bs-emergence"],
    },
    {
        "title": "Golak Nath v. State of Punjab",
        "slug": "golak-nath",
        "parties": "Golak Nath v. State of Punjab",
        "year": 1967,
        "court": CaseLaw.Court.SC,
        "summary": "FR given transcendental status — Parliament cannot abridge them by amendment.",
        "holding": (
            "Constitutional amendment Acts are ‘law’ under Art. 13; Parliament cannot abridge "
            "or take away Fundamental Rights."
        ),
        "concept_slugs": [HUB_SLUG, "bs-emergence", "bs-exam-anchors"],
    },
    {
        "title": "Kesavananda Bharati v. State of Kerala",
        "slug": "kesavananda-bharati",
        "parties": "Kesavananda Bharati v. State of Kerala",
        "year": 1973,
        "court": CaseLaw.Court.SC,
        "summary": "Birth of the basic structure doctrine; Fundamental Rights Case.",
        "holding": (
            "Parliament may amend FR (24th upheld; Golak overruled), but Art. 368 does not "
            "enable altering the basic structure of the Constitution."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "bs-emergence",
            "bs-present-rule",
            "bs-case-element-map",
            "bs-exam-anchors",
        ],
    },
    {
        "title": "Indira Nehru Gandhi v. Raj Narain",
        "slug": "indira-nehru-gandhi",
        "parties": "Indira Nehru Gandhi v. Raj Narain",
        "year": 1975,
        "court": CaseLaw.Court.SC,
        "summary": "Election Case — applies basic structure; voids 39th Amdt election-shield clause.",
        "holding": (
            "Putting election disputes of the PM/Speaker beyond all courts violated the basic structure."
        ),
        "concept_slugs": [HUB_SLUG, "bs-emergence", "bs-case-element-map"],
    },
    {
        "title": "Minerva Mills v. Union of India",
        "slug": "minerva-mills",
        "parties": "Minerva Mills Ltd. v. Union of India",
        "year": 1980,
        "court": CaseLaw.Court.SC,
        "summary": "Strikes 42nd Amdt attempt to make amending power unlimited; FR–DPSP balance.",
        "holding": (
            "Limited amending power is a basic feature; Parliament cannot convert it into an "
            "unlimited power. Judicial review and FR–DPSP harmony are basic."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "bs-emergence",
            "bs-present-rule",
            "bs-exam-anchors",
            "bs-case-element-map",
        ],
    },
    {
        "title": "Waman Rao v. Union of India",
        "slug": "waman-rao",
        "parties": "Waman Rao v. Union of India",
        "year": 1980,
        "court": CaseLaw.Court.SC,
        "summary": "Clarifies temporal reach of the basic structure doctrine.",
        "holding": (
            "Basic structure doctrine applies to constitutional amendments enacted after "
            "24 April 1973 (Kesavananda judgement date)."
        ),
        "concept_slugs": [HUB_SLUG, "bs-emergence", "bs-exam-anchors"],
    },
    {
        "title": "S.R. Bommai v. Union of India",
        "slug": "sr-bommai",
        "parties": "S.R. Bommai v. Union of India",
        "year": 1994,
        "court": CaseLaw.Court.SC,
        "summary": "Federalism, secularism, democracy and related features as basic.",
        "holding": (
            "Federalism, secularism, democracy, unity and integrity, social justice, and "
            "judicial review recognised among basic features."
        ),
        "concept_slugs": [HUB_SLUG, "bs-case-element-map", "bs-elements"],
    },
    {
        "title": "I.R. Coelho v. State of Tamil Nadu",
        "slug": "ir-coelho",
        "parties": "I.R. Coelho v. State of Tamil Nadu",
        "year": 2007,
        "court": CaseLaw.Court.SC,
        "summary": "IX Schedule Case — laws in Ninth Schedule open to basic-structure review.",
        "holding": (
            "Rule of law, separation of powers, essence of FR, judicial review, and equality "
            "are basic; IX Schedule insertion after Kesavananda is open to basic-structure scrutiny."
        ),
        "concept_slugs": [HUB_SLUG, "bs-case-element-map", "bs-elements"],
    },
]

AMENDMENTS = [
    {
        "number": 1,
        "year": 1951,
        "title": "First Amendment",
        "summary": (
            "Curtailed the right to property among other changes; validity challenged in Shankari Prasad."
        ),
        "effect": "Triggered the first Art. 368 vs Art. 13 debate on amending FR.",
        "concept_slugs": [HUB_SLUG, "bs-emergence"],
    },
    {
        "number": 17,
        "year": 1964,
        "title": "Seventeenth Amendment",
        "summary": "Inserted certain state Acts in the Ninth Schedule; challenged in Golak Nath.",
        "effect": "Immediate backdrop to the Golak Nath ruling on FR amendability.",
        "concept_slugs": [HUB_SLUG, "bs-emergence"],
    },
    {
        "number": 24,
        "year": 1971,
        "title": "Twenty-fourth Amendment",
        "summary": (
            "Amended Arts 13 and 368 to affirm Parliament’s power to abridge or take away FR."
        ),
        "effect": "Parliament’s reply to Golak Nath; upheld in Kesavananda Bharati.",
        "concept_slugs": [HUB_SLUG, "bs-emergence", "bs-present-rule", "bs-exam-anchors"],
    },
    {
        "number": 39,
        "year": 1975,
        "title": "Thirty-ninth Amendment",
        "summary": (
            "Among other things, sought to keep election disputes of the PM and Speaker "
            "outside the jurisdiction of all courts."
        ),
        "effect": "Relevant clause invalidated in Indira Nehru Gandhi as violating basic structure.",
        "concept_slugs": [HUB_SLUG, "bs-emergence", "bs-case-element-map"],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Attempted to remove limits on constituent power and bar judicial challenge to amendments."
        ),
        "effect": "Key Art. 368 clause invalidated in Minerva Mills — limited amending power is basic.",
        "concept_slugs": [HUB_SLUG, "bs-emergence", "bs-exam-anchors", "bs-present-rule"],
    },
]


class Command(BaseCommand):
    help = "Seed Basic Structure of the Constitution chapter (Laxmikanth Ch.12)."

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
                "title": "Basic Structure of the Constitution",
                "sort_order": 12,
                "book_ref": "Laxmikanth 8th Ed, Ch. 12",
                "summary": (
                    "Visual revision of Ch.12 — foundation mental model, emergence timeline, "
                    "Art. 368 present rule, themed elements, and Table 12.1 case map."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Basic Structure of the Constitution",
                "summary": (
                    "Parliament’s Art. 368 power is wide but not unlimited — the basic structure "
                    "is the unamendable foundation."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **foundation mental model**, then **Emergence** → **Present rule**. "
                    "Scan **Elements** by theme, use the **case map** for named judgements, "
                    "finish with **Exam anchors**. "
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
            ref="Laxmikanth Ch. 12",
            excerpt=(
                "Basic Structure — emergence, Art. 368 limit, elements, and Table 12.1."
            ),
            sort_order=0,
        )

        bs_slugs = set(by_slug.keys())
        related_outside = {"article-368", "judicial-review", "fundamental-rights"}
        ConceptEdge.objects.filter(
            source__slug__in=bs_slugs, source__subject=subject
        ).filter(target__slug__in=bs_slugs | related_outside).delete()

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
                by_slug[s] for s in case_data["concept_slugs"] if s in by_slug
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
                by_slug[s] for s in amd_data["concept_slugs"] if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Basic Structure chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs."
            )
        )
