"""Seed Laxmikanth Ch.6 Union and Its Territory (visual revision chapter)."""

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

HUB_SLUG = "union-and-its-territory"
CHAPTER_SLUG = "union-and-its-territory"

THEME_PILLARS = [
    {
        "id": "art1",
        "articles": "Art. 1",
        "label": "Name & Union of States",
        "slug": "uit-art1-name-polity",
        "detail": "India, that is, Bharat — Union, not Federation.",
        "tone": "teal",
    },
    {
        "id": "territory",
        "articles": "Art. 1",
        "label": "Three-fold Territory",
        "slug": "uit-territory-three-fold",
        "detail": "States · UTs · acquired — Territory of India ≠ Union of India.",
        "tone": "olive",
    },
    {
        "id": "art2",
        "articles": "Art. 2",
        "label": "Admit or Establish",
        "slug": "uit-art2-admit-establish",
        "detail": "External — new states not already in the Union.",
        "tone": "gold",
    },
    {
        "id": "art3",
        "articles": "Art. 3",
        "label": "Reorganise States",
        "slug": "uit-art3-reorganise",
        "detail": "Indestructible Union of destructible States.",
        "tone": "orange",
    },
    {
        "id": "art4",
        "articles": "Art. 4",
        "label": "Not Art. 368",
        "slug": "uit-art4-simple-majority",
        "detail": "Arts 2/3 laws = ordinary legislation / simple majority.",
        "tone": "terracotta",
    },
    {
        "id": "cession",
        "articles": "Berubari · 100th",
        "label": "Cession vs Boundary",
        "slug": "uit-cession-boundary",
        "detail": "Cession needs Art. 368; boundary settlement can be executive.",
        "tone": "maroon",
    },
    {
        "id": "integration",
        "articles": "1950",
        "label": "Integration & Parts A–D",
        "slug": "uit-integration-1950",
        "detail": "Princely modes + four-fold 1950 classification.",
        "tone": "teal",
    },
    {
        "id": "reorg",
        "articles": "1953–56",
        "label": "Reorganisation Path",
        "slug": "uit-reorganisation-path",
        "detail": "Dhar → JVP → Andhra → Fazl Ali → 14+6.",
        "tone": "olive",
    },
    {
        "id": "map",
        "articles": "After 1956",
        "label": "Map After 1956",
        "slug": "uit-map-after-1956",
        "detail": "Compressed milestones from Bombay split to DNH+DD merge.",
        "tone": "gold",
    },
    {
        "id": "jk",
        "articles": "2019",
        "label": "J&K & Ladakh",
        "slug": "uit-jk-ladakh-2019",
        "detail": "Art. 370 order + Reorganisation Act → two UTs; 28+8.",
        "tone": "orange",
    },
    {
        "id": "ref",
        "articles": "Tables",
        "label": "Reference Tables",
        "slug": "uit-reference-tables",
        "detail": "Present map, high-yield Acts, rename anchors.",
        "tone": "terracotta",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "uit-mental-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Redrawable map",
        "topic_label": "Union & Territory",
        "subject_label": "Part I · Arts 1–4",
        "relation_label": "Means Parliament can",
        "protects_from": [
            "State secession claims",
            "Confusing Union with Federation",
            "Treating Art. 3 as Art. 368",
            "Mixing cession with boundary settlement",
        ],
        "insight": (
            "Indestructible Union of destructible States — Parliament can redraw the map; "
            "states cannot exit the Union."
        ),
    },
    {
        "id": "uit-theme-pillars",
        "type": "pillars",
        "title": "Revision map — open a cluster",
        "items": THEME_PILLARS,
    },
    {
        "id": "uit-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "**Territory of India** is wider than **Union of India** (states only). "
            "Art. 2 = external admit/establish; Art. 3 = internal reorganisation. "
            "Cession of territory ≠ Art. 3 — needs Art. 368."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Art. 1 — Name & Union of States",
        "slug": "uit-art1-name-polity",
        "sort_order": 1,
        "summary": (
            "India, that is, Bharat — described as a Union of States, not a Federation of States."
        ),
        "body": (
            "## Article 1 — name and polity\n\n"
            "Art. 1 does two jobs: **name** of the country and **type** of polity.\n\n"
            "### Name\n"
            "- Constituent Assembly mixed traditional (**Bharat**) and modern (**India**).\n"
            "- Formula: **India, that is, Bharat**.\n\n"
            "### Union, not Federation\n"
            "Ambedkar’s two reasons for ‘Union of States’:\n"
            "1. Indian federation is **not** the result of an agreement among states (unlike USA).\n"
            "2. States have **no right to secede** — the Union is indestructible.\n\n"
            "States exist for administrative convenience within an integral whole."
        ),
        "articles": [
            (
                "Article 1",
                "India, that is, Bharat, shall be a Union of States.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-art1-compare",
                "type": "comparison",
                "title": "Name + polity in one Article",
                "columns": [
                    {
                        "id": "name",
                        "heading": "Name",
                        "points": [
                            "India (modern)",
                            "Bharat (traditional)",
                            "Adopted together: India, that is, Bharat",
                        ],
                    },
                    {
                        "id": "polity",
                        "heading": "Polity label",
                        "points": [
                            "Called Union of States",
                            "Not ‘Federation of States’",
                            "Federal structure, unitary spirit on exit",
                        ],
                    },
                ],
            },
            {
                "id": "uit-art1-pillars",
                "type": "pillars",
                "title": "Why ‘Union’ (Ambedkar)",
                "items": [
                    {
                        "id": "no-agreement",
                        "articles": "Reason 1",
                        "label": "No state compact",
                        "slug": "uit-art1-name-polity",
                        "detail": "Not born from an agreement among states (unlike USA).",
                        "tone": "teal",
                    },
                    {
                        "id": "no-secession",
                        "articles": "Reason 2",
                        "label": "No secession",
                        "slug": "uit-art1-name-polity",
                        "detail": "States cannot leave — Union is indestructible.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "uit-art1-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Remember the phrase: **indestructible Union of destructible States** "
                    "(Art. 3 power completes this picture)."
                ),
            },
        ],
    },
    {
        "title": "Three-fold Territory",
        "slug": "uit-territory-three-fold",
        "sort_order": 2,
        "summary": (
            "Territory of India = states + UTs + acquired territories; Union of India = states only."
        ),
        "body": (
            "## Three categories under Art. 1\n\n"
            "1. Territories of the **states**\n"
            "2. **Union territories**\n"
            "3. Territories that may be **acquired** by the Government of India\n\n"
            "Names and extent sit in the **First Schedule**. Present count: **28 states + 8 UTs**.\n\n"
            "### Territory of India vs Union of India\n"
            "- **Union of India** → only states (federal members sharing powers with the Centre).\n"
            "- **Territory of India** → states + UTs + acquired territories (wider).\n"
            "- UTs and acquired territories are administered by the Centre.\n\n"
            "### Acquisition modes (international law)\n"
            "Cession, occupation, conquest/subjugation — e.g. DNH, Goa/Daman/Diu, Puducherry, Sikkim.\n\n"
            "Part XXI special provisions and Schedules 5–6 override/generalise state administration "
            "for listed states and scheduled/tribal areas."
        ),
        "articles": [
            (
                "Article 1 · First Schedule",
                "Three-fold territory; names and territorial extent in Schedule I.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-territory-tree",
                "type": "tree",
                "title": "Territory of India (wider)",
                "root": {
                    "id": "toi",
                    "label": "Territory of India",
                    "detail": "Wider expression",
                    "children": [
                        {
                            "id": "states",
                            "label": "States",
                            "detail": "Union of India = these only",
                            "slug": "uit-territory-three-fold",
                        },
                        {
                            "id": "uts",
                            "label": "Union territories",
                            "detail": "Centre-administered",
                            "slug": "uit-territory-three-fold",
                        },
                        {
                            "id": "acquired",
                            "label": "Acquired territories",
                            "detail": "Future / historical acquisitions",
                            "slug": "uit-territory-three-fold",
                        },
                    ],
                },
            },
            {
                "id": "uit-territory-compare",
                "type": "comparison",
                "title": "Territory of India vs Union of India",
                "columns": [
                    {
                        "id": "toi",
                        "heading": "Territory of India",
                        "points": [
                            "States + UTs + acquired",
                            "Wider expression",
                            "Includes Centre-run units",
                        ],
                    },
                    {
                        "id": "uoi",
                        "heading": "Union of India",
                        "points": [
                            "States only",
                            "Federal members",
                            "Share distribution of powers with Centre",
                        ],
                    },
                ],
            },
            {
                "id": "uit-territory-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Do not treat ‘Union of India’ and ‘Territory of India’ as synonyms — "
                    "Territory is the wider set."
                ),
            },
        ],
    },
    {
        "title": "Art. 2 — Admit or Establish",
        "slug": "uit-art2-admit-establish",
        "sort_order": 3,
        "summary": (
            "Parliament may admit existing states or establish new ones not already in the Union."
        ),
        "body": (
            "## Article 2 — external to the Union\n\n"
            "Parliament may **admit into** the Union, or **establish**, new states on such terms "
            "and conditions as it thinks fit.\n\n"
            "- **Admit** → states already in existence (outside the Union).\n"
            "- **Establish** → states that did not exist before.\n\n"
            "Art. 2 is about units **not part of** the Union of India. "
            "Art. 3 handles internal readjustment among existing constituent units."
        ),
        "articles": [
            (
                "Article 2",
                "Admit into the Union, or establish, new states on such terms and conditions as Parliament thinks fit.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-art2-compare",
                "type": "comparison",
                "title": "Admit vs establish (Art. 2)",
                "columns": [
                    {
                        "id": "admit",
                        "heading": "Admit",
                        "points": [
                            "State already exists",
                            "Brought into the Union",
                            "Terms & conditions as Parliament thinks fit",
                        ],
                    },
                    {
                        "id": "establish",
                        "heading": "Establish",
                        "points": [
                            "State did not exist before",
                            "Created and brought in",
                            "Same flexible terms power",
                        ],
                    },
                ],
            },
            {
                "id": "uit-art2-vs3",
                "type": "comparison",
                "title": "Art. 2 vs Art. 3",
                "columns": [
                    {
                        "id": "a2",
                        "heading": "Article 2",
                        "points": [
                            "External",
                            "New states not already in the Union",
                            "Admit or establish",
                        ],
                    },
                    {
                        "id": "a3",
                        "heading": "Article 3",
                        "points": [
                            "Internal",
                            "Among existing states/UTs of the Union",
                            "Form, alter area/boundary/name",
                        ],
                    },
                ],
            },
            {
                "id": "uit-art2-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": "Art. 2 = outside → in. Art. 3 = rearrange what is already in.",
            },
        ],
    },
    {
        "title": "Art. 3 — Reorganise States",
        "slug": "uit-art3-reorganise",
        "sort_order": 4,
        "summary": (
            "Parliament may form/alter states without their consent — indestructible Union "
            "of destructible States."
        ),
        "body": (
            "## Article 3 — five powers\n\n"
            "Parliament may:\n"
            "1. Form a new state (separation / union of states or parts / uniting territory to a part).\n"
            "2. Increase the area of any state.\n"
            "3. Diminish the area of any state.\n"
            "4. Alter the boundaries of any state.\n"
            "5. Alter the name of any state.\n\n"
            "Also covers forming a new state or UT by uniting parts of states/UTs.\n\n"
            "### Two conditions\n"
            "1. Bill only with **prior recommendation of the President**.\n"
            "2. Before recommending, President refers the bill to the **concerned state legislature** "
            "for views within a specified period.\n\n"
            "- Views are **not binding**; no fresh reference needed for every amendment to the bill.\n"
            "- For a **UT**, no reference to a legislature is required.\n\n"
            "### India vs USA\n"
            "India: territorial integrity of a state is **not** guaranteed. "
            "USA: indestructible Union of **indestructible** states (consent required)."
        ),
        "articles": [
            (
                "Article 3",
                "Form new states; increase/diminish area; alter boundaries or names — with Presidential recommendation and state views (non-binding).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-art3-flow",
                "type": "flowchart",
                "title": "Art. 3 bill — which path?",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "Want to reorganise a state/UT?",
                        "detail": "Form, area, boundary, or name change under Art. 3.",
                        "options": [
                            {"label": "Affects a State", "next": "state"},
                            {"label": "Affects only a UT", "next": "ut"},
                        ],
                    },
                    {
                        "id": "state",
                        "label": "State path",
                        "detail": (
                            "President’s prior recommendation → refer to state legislature "
                            "for views → Parliament may accept or reject views."
                        ),
                        "options": [
                            {"label": "Next: India vs USA takeaway", "next": "takeaway"},
                        ],
                    },
                    {
                        "id": "ut",
                        "label": "UT path",
                        "detail": "No reference to a UT legislature — Parliament acts as it deems fit.",
                        "options": [
                            {"label": "Next: India vs USA takeaway", "next": "takeaway"},
                        ],
                    },
                    {
                        "id": "takeaway",
                        "label": "Indestructible Union of destructible States",
                        "detail": (
                            "Parliament can redraw the map without state consent. "
                            "USA needs state consent — indestructible states."
                        ),
                    },
                ],
            },
            {
                "id": "uit-art3-compare",
                "type": "comparison",
                "title": "India vs USA on state integrity",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Indestructible Union",
                            "Destructible States",
                            "No guaranteed territorial integrity of a state",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Indestructible Union",
                            "Indestructible States",
                            "Consent of states required to alter",
                        ],
                    },
                ],
            },
            {
                "id": "uit-art3-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "State legislature’s views are **ascertained**, not decisive. "
                    "Also: diminishing area under Art. 3 ≠ ceding territory to a foreign country."
                ),
            },
        ],
    },
    {
        "title": "Art. 4 — Not Art. 368",
        "slug": "uit-art4-simple-majority",
        "sort_order": 5,
        "summary": (
            "Laws under Arts 2 and 3 are not constitutional amendments — ordinary process, "
            "simple majority."
        ),
        "body": (
            "## Article 4\n\n"
            "Laws for admission/establishment (Art. 2) and formation/alteration (Art. 3) "
            "**are not** amendments under Art. 368.\n\n"
            "They pass by **simple majority** and the ordinary legislative process "
            "(plus Art. 3’s Presidential recommendation / reference rules)."
        ),
        "articles": [
            (
                "Article 4",
                "Arts 2 and 3 laws shall not be deemed amendments of the Constitution for Art. 368.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-art4-compare",
                "type": "comparison",
                "title": "Art. 4 path vs Art. 368 path",
                "columns": [
                    {
                        "id": "art4",
                        "heading": "Arts 2 / 3 (+ Art. 4)",
                        "points": [
                            "Ordinary legislation",
                            "Simple majority",
                            "Redraw internal map / admit-establish",
                        ],
                    },
                    {
                        "id": "art368",
                        "heading": "Art. 368",
                        "points": [
                            "Constitutional amendment",
                            "Special majority (+ ratification when required)",
                            "Needed for cession of Indian territory abroad",
                        ],
                    },
                ],
            },
            {
                "id": "uit-art4-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "New state by Art. 3 Act ≠ constitutional amendment. "
                    "Ceding land to a foreign country ≠ Art. 3 — use Art. 368."
                ),
            },
        ],
    },
    {
        "title": "Cession vs Boundary Settlement",
        "slug": "uit-cession-boundary",
        "sort_order": 6,
        "summary": (
            "Berubari: cession needs Art. 368 (9th CAA). Boundary settlement can be executive. "
            "100th CAA settled Bangladesh enclaves."
        ),
        "body": (
            "## Cession of territory\n\n"
            "**Berubari Union (1960) Presidential Reference:** power to diminish area under Art. 3 "
            "does **not** cover ceding Indian territory to a foreign country. "
            "Cession requires a **constitutional amendment** (Art. 368). "
            "→ **9th Constitutional Amendment Act (1960)** for transfer to Pakistan.\n\n"
            "## Boundary settlement (1969)\n\n"
            "Settling a boundary dispute with another country **without** ceding territory "
            "can be done by **executive action** — no constitutional amendment.\n\n"
            "## 100th Amendment (2015)\n\n"
            "Land Boundary Agreement with Bangladesh: India transferred 111 enclaves; "
            "Bangladesh transferred 51. Also adverse possessions and a 6.1 km undemarcated stretch. "
            "Modified First Schedule entries for **Assam, West Bengal, Meghalaya, Tripura**.\n\n"
            "Path in brief: Radcliffe disputes → efforts including Nehru–Noon → 9th CAA "
            "(Berubari) → 1974 Agreement + 2011 Protocol → **100th CAA**."
        ),
        "articles": [
            (
                "Art. 3 vs Art. 368",
                "Diminish area ≠ cession abroad. Cession needs Art. 368; pure boundary settlement may be executive.",
            ),
            (
                "100th Amendment",
                "India–Bangladesh enclave exchange; First Schedule tweaks for four states.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-cession-flow",
                "type": "flowchart",
                "title": "Territory to a foreign country?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What kind of change?",
                        "detail": "Pick the correct constitutional path.",
                        "options": [
                            {
                                "label": "Ceding Indian territory abroad",
                                "next": "cession",
                            },
                            {
                                "label": "Settling boundary (no cession)",
                                "next": "boundary",
                            },
                            {
                                "label": "India–Bangladesh enclaves deal",
                                "next": "hundred",
                            },
                        ],
                    },
                    {
                        "id": "cession",
                        "label": "Need Art. 368",
                        "detail": (
                            "Berubari (1960): Art. 3 cannot cede territory. "
                            "Example: 9th CAA (1960)."
                        ),
                    },
                    {
                        "id": "boundary",
                        "label": "Executive action enough",
                        "detail": (
                            "1969 SC ruling: boundary dispute settlement without cession "
                            "needs no constitutional amendment."
                        ),
                    },
                    {
                        "id": "hundred",
                        "label": "100th CAA (2015)",
                        "detail": (
                            "111 enclaves out / 51 in; Assam, West Bengal, Meghalaya, Tripura "
                            "in First Schedule."
                        ),
                    },
                ],
            },
            {
                "id": "uit-cession-compare",
                "type": "comparison",
                "title": "Cession vs boundary settlement",
                "columns": [
                    {
                        "id": "cession",
                        "heading": "Cession (Berubari)",
                        "points": [
                            "Transfer of Indian territory abroad",
                            "Art. 3 not enough",
                            "Amend Constitution (Art. 368)",
                        ],
                    },
                    {
                        "id": "boundary",
                        "heading": "Boundary settlement (1969)",
                        "points": [
                            "Clarify/settle line",
                            "No cession of territory",
                            "Executive action permissible",
                        ],
                    },
                ],
            },
            {
                "id": "uit-cession-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "9th CAA = Berubari/Pakistan path. "
                    "100th CAA = Bangladesh enclaves (four states in Schedule I)."
                ),
            },
        ],
    },
    {
        "title": "Princely Integration & 1950 Parts A–D",
        "slug": "uit-integration-1950",
        "sort_order": 7,
        "summary": (
            "549 princely states joined; Hyderabad, Junagarh, Kashmir by distinct modes; "
            "1950 four-fold Parts A–D."
        ),
        "body": (
            "## At independence\n\n"
            "British provinces + princely states. Independence Act options: India / Pakistan / independent. "
            "Of 552 within India’s geography, **549 joined**; three held out then integrated:\n"
            "- **Hyderabad** — police action\n"
            "- **Junagarh** — referendum\n"
            "- **Kashmir** — Instrument of Accession\n\n"
            "## 1950 four-fold classification (29 units)\n\n"
            "- **Part A** — erstwhile governors’ provinces (9)\n"
            "- **Part B** — erstwhile princely states with legislatures (9)\n"
            "- **Part C** — chief commissioners’ provinces + some princely states (10), centrally administered\n"
            "- **Part D** — Andaman and Nicobar Islands alone\n\n"
            "Abolished in 1956 (States Reorganisation Act + 7th CAA)."
        ),
        "articles": [
            (
                "Original Constitution · Schedule I (1950)",
                "Part A / B / C states and Part D territories — four-fold classification.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-integration-pillars",
                "type": "pillars",
                "title": "Three holdouts — how integrated",
                "items": [
                    {
                        "id": "hyd",
                        "articles": "Police action",
                        "label": "Hyderabad",
                        "slug": "uit-integration-1950",
                        "detail": "Integrated by police action.",
                        "tone": "teal",
                    },
                    {
                        "id": "jun",
                        "articles": "Referendum",
                        "label": "Junagarh",
                        "slug": "uit-integration-1950",
                        "detail": "Integrated by referendum.",
                        "tone": "olive",
                    },
                    {
                        "id": "jk",
                        "articles": "Accession",
                        "label": "Kashmir",
                        "slug": "uit-integration-1950",
                        "detail": "Instrument of Accession.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "uit-1950-timeline",
                "type": "timeline",
                "title": "1950 Parts A–D (snapshot)",
                "events": [
                    {
                        "id": "a",
                        "year": 1950,
                        "label": "Part A (9)",
                        "detail": "Former governors’ provinces — e.g. Assam, Bombay, Madras, UP, WB.",
                    },
                    {
                        "id": "b",
                        "year": 1950,
                        "label": "Part B (9)",
                        "detail": "Princely states with legislatures — e.g. Hyderabad, Mysore, J&K, Rajasthan.",
                    },
                    {
                        "id": "c",
                        "year": 1950,
                        "label": "Part C (10)",
                        "detail": "Centrally administered — e.g. Delhi, Himachal, Manipur, Tripura.",
                    },
                    {
                        "id": "d",
                        "year": 1950,
                        "label": "Part D (1)",
                        "detail": "Andaman and Nicobar Islands only.",
                    },
                ],
            },
            {
                "id": "uit-integration-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": "Police action / referendum / Instrument of Accession — map each to Hyderabad / Junagarh / Kashmir.",
            },
        ],
    },
    {
        "title": "Reorganisation Path (Dhar → 1956)",
        "slug": "uit-reorganisation-path",
        "sort_order": 8,
        "summary": (
            "Dhar rejected language; JVP rejected language; Andhra 1953 forced the issue; "
            "Fazl Ali accepted language (not one-language–one-state); 14 states + 6 UTs in 1956."
        ),
        "body": (
            "## Commissions and the first linguistic state\n\n"
            "- **Dhar Commission (1948):** prefer administrative convenience over language.\n"
            "- **JVP Committee (1948–49):** Nehru, Patel, Pattabhi — rejected language as basis.\n"
            "- **Andhra (Oct 1953):** first linguistic state after Potti Sriramulu’s death "
            "(Telugu areas from Madras).\n\n"
            "## Fazl Ali Commission (1953–55)\n\n"
            "Members: Fazl Ali (chair), K.M. Panikkar, H.N. Kunzru. "
            "Accepted language broadly; **rejected** ‘one language–one state’. "
            "Unity of India primary.\n\n"
            "Four factors: unity & security; linguistic/cultural homogeneity; "
            "financial/economic/administrative; planning & welfare.\n\n"
            "## 1956 outcome\n\n"
            "**States Reorganisation Act (1956)** + **7th CAA**: abolished Part A/B distinction "
            "and Part C states → **14 states + 6 UTs** (1 Nov 1956)."
        ),
        "articles": [
            (
                "States Reorganisation Act, 1956 · 7th CAA",
                "Ended Parts A–D scheme; created 14 states and 6 union territories.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-reorg-timeline",
                "type": "timeline",
                "title": "Path to 1956 reorganisation",
                "events": [
                    {
                        "id": "dhar",
                        "year": 1948,
                        "label": "Dhar Commission",
                        "detail": "Administrative convenience > language.",
                    },
                    {
                        "id": "jvp",
                        "year": 1949,
                        "label": "JVP Committee",
                        "detail": "Nehru–Patel–Pattabhi; rejected linguistic basis.",
                    },
                    {
                        "id": "andhra",
                        "year": 1953,
                        "label": "Andhra State",
                        "detail": "First linguistic state; Potti Sriramulu agitation.",
                    },
                    {
                        "id": "fazl",
                        "year": 1955,
                        "label": "Fazl Ali report",
                        "detail": "Language yes; one-language–one-state no; four factors.",
                    },
                    {
                        "id": "sra",
                        "year": 1956,
                        "label": "SRA + 7th CAA",
                        "detail": "14 states + 6 UTs; Parts A–D abolished.",
                    },
                ],
            },
            {
                "id": "uit-fazl-pillars",
                "type": "pillars",
                "title": "Fazl Ali — four factors",
                "items": [
                    {
                        "id": "unity",
                        "articles": "1",
                        "label": "Unity & security",
                        "slug": "uit-reorganisation-path",
                        "detail": "Preservation and strengthening of the country’s unity.",
                        "tone": "teal",
                    },
                    {
                        "id": "lang",
                        "articles": "2",
                        "label": "Language & culture",
                        "slug": "uit-reorganisation-path",
                        "detail": "Linguistic and cultural homogeneity.",
                        "tone": "olive",
                    },
                    {
                        "id": "admin",
                        "articles": "3",
                        "label": "Admin & economy",
                        "slug": "uit-reorganisation-path",
                        "detail": "Financial, economic, and administrative considerations.",
                        "tone": "gold",
                    },
                    {
                        "id": "welfare",
                        "articles": "4",
                        "label": "Welfare & planning",
                        "slug": "uit-reorganisation-path",
                        "detail": "Welfare of people in each state and the nation.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "uit-reorg-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Fazl Ali accepted language as a basis but **rejected** "
                    "the theory of one language–one state."
                ),
            },
        ],
    },
    {
        "title": "Map After 1956",
        "slug": "uit-map-after-1956",
        "sort_order": 9,
        "summary": (
            "Compressed milestones from Maharashtra–Gujarat (1960) through Telangana (2014) "
            "and the 2020 UT merger — see J&K 2019 cluster for the latest count shift."
        ),
        "body": (
            "## High-yield milestones (scan, don’t memorise every Act)\n\n"
            "- **1960:** Bombay → Maharashtra + Gujarat.\n"
            "- **1961–62:** DNH (10th CAA); Goa/Daman/Diu (12th); Puducherry (14th, 1962).\n"
            "- **1963:** Nagaland (from Assam).\n"
            "- **1966 / 1971:** Punjab → Haryana + Chandigarh UT; HP statehood 1971.\n"
            "- **1972:** Manipur, Tripura, Meghalaya statehood; Mizoram & Arunachal as UTs.\n"
            "- **1974–75:** Sikkim associate (35th) → full state (36th); Art. 371-F.\n"
            "- **1987:** Mizoram, Arunachal Pradesh, Goa — states.\n"
            "- **2000:** Chhattisgarh, Uttarakhand, Jharkhand.\n"
            "- **2014:** Telangana (29th state) from Andhra Pradesh.\n"
            "- **2020:** DNH merged with Daman & Diu → one UT.\n\n"
            "Renames (scan): UP (1950), Tamil Nadu (1969), Karnataka & Lakshadweep (1973), "
            "NCT Delhi (69th), Uttarakhand & Puducherry (2006), Odisha (2011)."
        ),
        "articles": [
            (
                "Art. 3 Acts (selected)",
                "Post-1956 map changes via ordinary Art. 3 legislation and related CAAs.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-map-timeline",
                "type": "timeline",
                "title": "Map milestones after 1956",
                "events": [
                    {
                        "id": "bom",
                        "year": 1960,
                        "label": "Maharashtra + Gujarat",
                        "detail": "Bilingual Bombay split.",
                    },
                    {
                        "id": "acq",
                        "year": 1962,
                        "label": "Goa / DNH / Puducherry track",
                        "detail": "Acquired territories → UT path (10th/12th/14th CAAs).",
                    },
                    {
                        "id": "nag",
                        "year": 1963,
                        "label": "Nagaland",
                        "detail": "16th state from Assam (Naga Hills–Tuensang).",
                    },
                    {
                        "id": "pun",
                        "year": 1966,
                        "label": "Haryana + Chandigarh",
                        "detail": "Punjab trifurcation path; HP statehood 1971.",
                    },
                    {
                        "id": "ne",
                        "year": 1972,
                        "label": "Northeast redraw",
                        "detail": "Manipur, Tripura, Meghalaya states; Mizoram & Arunachal UTs.",
                    },
                    {
                        "id": "sik",
                        "year": 1975,
                        "label": "Sikkim full state",
                        "detail": "35th associate → 36th full state; Art. 371-F.",
                    },
                    {
                        "id": "87",
                        "year": 1987,
                        "label": "Mizoram · Arunachal · Goa",
                        "detail": "Three new states.",
                    },
                    {
                        "id": "2000",
                        "year": 2000,
                        "label": "CG · UK · JH",
                        "detail": "From MP, UP, Bihar.",
                    },
                    {
                        "id": "tel",
                        "year": 2014,
                        "label": "Telangana",
                        "detail": "29th state; AP Reorganisation Act.",
                    },
                    {
                        "id": "merge",
                        "year": 2020,
                        "label": "DNH + DD merge",
                        "detail": "Single UT: Dadra and Nagar Haveli and Daman and Diu.",
                    },
                ],
            },
            {
                "id": "uit-map-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "For Prelims, lock years of first linguistic state (1953), SRA (1956), "
                    "Bombay split (1960), Sikkim (1975), 2000 trio, Telangana (2014), J&K/Ladakh (2019)."
                ),
            },
            {
                "id": "uit-map-note",
                "type": "callout",
                "tone": "note",
                "title": "Continue to J&K 2019",
                "body": (
                    "The 2019 reorganisation changes the headline count to **28 states + 8 UTs** — "
                    "open the next cluster."
                ),
            },
        ],
    },
    {
        "title": "J&K & Ladakh (2019)",
        "slug": "uit-jk-ladakh-2019",
        "sort_order": 10,
        "summary": (
            "2019 presidential order ended Art. 370 special status; Reorganisation Act created "
            "UT of J&K and UT of Ladakh — present 28 states + 8 UTs."
        ),
        "body": (
            "## Till 2019\n\n"
            "Erstwhile State of J&K had its own constitution and special status under **Art. 370**.\n\n"
            "## 2019 steps\n\n"
            "1. **Constitution (Application to Jammu and Kashmir) Order, 2019** — superseded the 1954 order; "
            "extended all provisions of the Constitution of India to J&K.\n"
            "2. **Jammu and Kashmir Reorganisation Act, 2019** — bifurcated the state into:\n"
            "   - **UT of Jammu and Kashmir** (all districts except Kargil & Leh)\n"
            "   - **UT of Ladakh** (Kargil + Leh)\n\n"
            "## Present count\n\n"
            "From 14 states + 6 UTs (1956) → **28 states + 8 UTs** now."
        ),
        "articles": [
            (
                "Art. 370 · J&K Reorganisation Act, 2019",
                "Special status ended via 2019 Order; state bifurcated into two UTs.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-jk-flow",
                "type": "flowchart",
                "title": "2019 J&K path",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "Erstwhile State of J&K",
                        "detail": "Own constitution + Art. 370 special status (till 2019).",
                        "options": [
                            {"label": "What changed in 2019?", "next": "order"},
                        ],
                    },
                    {
                        "id": "order",
                        "label": "Presidential Order 2019",
                        "detail": (
                            "Superseded 1954 Order; extended full Constitution of India to J&K."
                        ),
                        "options": [
                            {"label": "Then the Reorganisation Act?", "next": "act"},
                        ],
                    },
                    {
                        "id": "act",
                        "label": "Two union territories",
                        "detail": (
                            "UT J&K (minus Kargil/Leh) + UT Ladakh (Kargil + Leh). "
                            "Headline map: 28 states + 8 UTs."
                        ),
                    },
                ],
            },
            {
                "id": "uit-jk-pillars",
                "type": "pillars",
                "title": "Two UTs from one state",
                "items": [
                    {
                        "id": "jkut",
                        "articles": "2019",
                        "label": "UT of J&K",
                        "slug": "uit-jk-ladakh-2019",
                        "detail": "All districts of erstwhile state except Kargil and Leh.",
                        "tone": "teal",
                    },
                    {
                        "id": "ladakh",
                        "articles": "2019",
                        "label": "UT of Ladakh",
                        "slug": "uit-jk-ladakh-2019",
                        "detail": "Kargil and Leh districts.",
                        "tone": "olive",
                    },
                    {
                        "id": "count",
                        "articles": "Now",
                        "label": "28 + 8",
                        "slug": "uit-jk-ladakh-2019",
                        "detail": "Present states and union territories.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "uit-jk-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Order ended special status application path; Reorganisation Act drew the two UTs. "
                    "Ladakh = Kargil + Leh only."
                ),
            },
        ],
    },
    {
        "title": "Reference — Acts & Present Map",
        "slug": "uit-reference-tables",
        "sort_order": 11,
        "summary": (
            "Scan cards: present 28+8, high-yield Art. 3 Acts, and major renames — not a full Table 6.4 dump."
        ),
        "body": (
            "## Present map (as of now)\n\n"
            "**28 states** and **8 UTs**: Andaman & Nicobar; Chandigarh; Dadra and Nagar Haveli and "
            "Daman and Diu; Delhi (NCT); Jammu & Kashmir; Ladakh; Lakshadweep; Puducherry.\n\n"
            "## High-yield Art. 3 / related Acts\n\n"
            "- Andhra State Act, 1953 — first linguistic state.\n"
            "- States Reorganisation Act, 1956 — 14+6.\n"
            "- Andhra Pradesh Reorganisation Act, 2014 — Telangana.\n"
            "- J&K Reorganisation Act, 2019 — two UTs.\n\n"
            "## Renames (quick)\n\n"
            "United Provinces → UP (1950); Madras → Tamil Nadu (1969); Mysore → Karnataka (1973); "
            "Laccadive etc. → Lakshadweep (1973); Delhi → NCT (69th CAA); Uttaranchal → Uttarakhand; "
            "Pondicherry → Puducherry (2006); Orissa → Odisha (2011)."
        ),
        "articles": [
            (
                "First Schedule",
                "Names and territorial extent of states and union territories.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "uit-ref-pillars",
                "type": "pillars",
                "title": "High-yield Acts to recall",
                "items": [
                    {
                        "id": "andhra53",
                        "articles": "1953",
                        "label": "Andhra State Act",
                        "slug": "uit-reference-tables",
                        "detail": "First linguistic state from Madras; capital Kurnool.",
                        "tone": "teal",
                    },
                    {
                        "id": "sra56",
                        "articles": "1956",
                        "label": "States Reorganisation Act",
                        "slug": "uit-reference-tables",
                        "detail": "14 states + 6 UTs; with 7th CAA ended Parts A–D.",
                        "tone": "olive",
                    },
                    {
                        "id": "ap14",
                        "articles": "2014",
                        "label": "AP Reorganisation Act",
                        "slug": "uit-reference-tables",
                        "detail": "Telangana carved from Andhra Pradesh.",
                        "tone": "gold",
                    },
                    {
                        "id": "jk19",
                        "articles": "2019",
                        "label": "J&K Reorganisation Act",
                        "slug": "uit-reference-tables",
                        "detail": "UT of J&K + UT of Ladakh.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "uit-ref-timeline",
                "type": "timeline",
                "title": "Rename anchors",
                "events": [
                    {
                        "id": "up",
                        "year": 1950,
                        "label": "Uttar Pradesh",
                        "detail": "United Provinces renamed.",
                    },
                    {
                        "id": "tn",
                        "year": 1969,
                        "label": "Tamil Nadu",
                        "detail": "Madras renamed.",
                    },
                    {
                        "id": "kar",
                        "year": 1973,
                        "label": "Karnataka · Lakshadweep",
                        "detail": "Mysore and Laccadive/Minicoy/Amindivi renamed.",
                    },
                    {
                        "id": "nct",
                        "year": 1991,
                        "label": "NCT of Delhi",
                        "detail": "69th CAA redesignation (not full statehood).",
                    },
                    {
                        "id": "06",
                        "year": 2006,
                        "label": "Uttarakhand · Puducherry",
                        "detail": "Uttaranchal and Pondicherry renamed.",
                    },
                    {
                        "id": "od",
                        "year": 2011,
                        "label": "Odisha",
                        "detail": "Orissa renamed.",
                    },
                ],
            },
            {
                "id": "uit-ref-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "Do not rebuild Table 6.4 from memory. "
                    "Know the four Acts above + 28/8 + cession vs Art. 3."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "uit-art1-name-polity"),
    (HUB_SLUG, "parent", "uit-territory-three-fold"),
    (HUB_SLUG, "parent", "uit-art2-admit-establish"),
    (HUB_SLUG, "parent", "uit-art3-reorganise"),
    (HUB_SLUG, "parent", "uit-art4-simple-majority"),
    (HUB_SLUG, "parent", "uit-cession-boundary"),
    (HUB_SLUG, "parent", "uit-integration-1950"),
    (HUB_SLUG, "parent", "uit-reorganisation-path"),
    (HUB_SLUG, "parent", "uit-map-after-1956"),
    (HUB_SLUG, "parent", "uit-jk-ladakh-2019"),
    (HUB_SLUG, "parent", "uit-reference-tables"),
    ("uit-art2-admit-establish", "related", "uit-art3-reorganise"),
    ("uit-art3-reorganise", "related", "uit-art4-simple-majority"),
    ("uit-art3-reorganise", "related", "uit-cession-boundary"),
    ("uit-art1-name-polity", "related", "uit-territory-three-fold"),
    ("uit-integration-1950", "related", "uit-reorganisation-path"),
    ("uit-reorganisation-path", "related", "uit-map-after-1956"),
    ("uit-map-after-1956", "related", "uit-jk-ladakh-2019"),
    ("uit-jk-ladakh-2019", "related", "uit-reference-tables"),
    ("uit-art1-name-polity", "related", "sf-federal-unitary"),
]

SAMPLE_PYQS = [
    (
        2015,
        "The provisions in the Fifth Schedule and Sixth Schedule in the Constitution of India are made in order to:",
        "Protect the interests of Scheduled Tribes (linked to territorial administration within states — Part I context + Schedules).",
        ["uit-territory-three-fold"],
    ),
    (
        2017,
        "Which of the following are not necessarily the consequences of the proclamation of the President’s rule in a State?",
        "Art. 3 reorganisation is a separate ordinary power — do not confuse emergency consequences with map-redraw power.",
        ["uit-art3-reorganise"],
    ),
    (
        2018,
        "India is described as an ‘indestructible Union of destructible States’. This idea is closest to:",
        "Parliament’s Art. 3 power to alter states without their consent; states cannot secede (Art. 1 Union).",
        ["uit-art1-name-polity", "uit-art3-reorganise"],
    ),
    (
        2020,
        "Cession of Indian territory to a foreign country requires:",
        "A constitutional amendment under Art. 368 (Berubari) — not a mere Art. 3 law.",
        ["uit-cession-boundary", "uit-art4-simple-majority"],
    ),
    (
        2021,
        "The Constitution (100th Amendment) Act, 2015 is related to:",
        "India–Bangladesh land boundary / enclave exchange affecting Assam, West Bengal, Meghalaya, Tripura.",
        ["uit-cession-boundary"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Berubari Union Reference",
        "slug": "berubari-union",
        "parties": "In re: The Berubari Union and Exchange of Enclaves",
        "year": 1960,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Presidential Reference on whether Art. 3 covers ceding Indian territory to a foreign country."
        ),
        "holding": (
            "Parliament’s power to diminish the area of a state under Art. 3 does not include "
            "cession of Indian territory to a foreign state; that requires a constitutional "
            "amendment under Art. 368."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "uit-cession-boundary",
            "uit-art3-reorganise",
            "uit-art4-simple-majority",
        ],
    },
    {
        "title": "Boundary Dispute Settlement (1969)",
        "slug": "boundary-dispute-settlement-1969",
        "parties": "Supreme Court ruling on Indo-foreign boundary settlement (1969)",
        "year": 1969,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Clarified that settling a boundary dispute without ceding territory differs from cession."
        ),
        "holding": (
            "Settlement of a boundary dispute between India and another country does not require "
            "a constitutional amendment and may be done by executive action when it does not "
            "involve cession of Indian territory."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "uit-cession-boundary",
        ],
    },
]

AMENDMENTS = [
    {
        "number": 7,
        "year": 1956,
        "title": "Seventh Amendment",
        "summary": (
            "Implemented States Reorganisation — ended Part A/B distinction and Part C states."
        ),
        "effect": "Enabled 14 states + 6 UTs framework with the States Reorganisation Act, 1956.",
        "concept_slugs": [
            HUB_SLUG,
            "uit-reorganisation-path",
            "uit-integration-1950",
            "uit-reference-tables",
        ],
    },
    {
        "number": 9,
        "year": 1960,
        "title": "Ninth Amendment",
        "summary": "Gave effect to cession of Berubari Union territory to Pakistan after the SC opinion.",
        "effect": "Showed cession abroad needs Art. 368, not Art. 3 alone.",
        "concept_slugs": ["uit-cession-boundary", HUB_SLUG],
    },
    {
        "number": 10,
        "year": 1961,
        "title": "Tenth Amendment",
        "summary": "Dadra and Nagar Haveli incorporated as a union territory.",
        "effect": "Acquired territory → UT route.",
        "concept_slugs": ["uit-map-after-1956", "uit-territory-three-fold"],
    },
    {
        "number": 12,
        "year": 1962,
        "title": "Twelfth Amendment",
        "summary": "Goa, Daman and Diu constituted as a union territory.",
        "effect": "Portuguese territories on the UT path (Goa later a state in 1987).",
        "concept_slugs": ["uit-map-after-1956"],
    },
    {
        "number": 14,
        "year": 1962,
        "title": "Fourteenth Amendment",
        "summary": "Puducherry (former French establishments) made a union territory.",
        "effect": "Acquired territory → UT.",
        "concept_slugs": ["uit-map-after-1956", "uit-territory-three-fold"],
    },
    {
        "number": 22,
        "year": 1969,
        "title": "Twenty-second Amendment",
        "summary": "Created Meghalaya as an autonomous state (sub-state) within Assam.",
        "effect": "Stepping stone to full Meghalaya statehood in 1972.",
        "concept_slugs": ["uit-map-after-1956"],
    },
    {
        "number": 35,
        "year": 1974,
        "title": "Thirty-fifth Amendment",
        "summary": "Sikkim as ‘associate state’; inserted Art. 2-A and a (then) 10th Schedule of terms.",
        "effect": "Short-lived associate-state experiment.",
        "concept_slugs": ["uit-map-after-1956", "uit-art2-admit-establish"],
    },
    {
        "number": 36,
        "year": 1975,
        "title": "Thirty-sixth Amendment",
        "summary": "Sikkim became a full state; Art. 371-F; repealed Art. 2-A and that 10th Schedule.",
        "effect": "22nd state of the Union.",
        "concept_slugs": ["uit-map-after-1956", HUB_SLUG],
    },
    {
        "number": 69,
        "year": 1991,
        "title": "Sixty-ninth Amendment",
        "summary": "Redesignated Delhi as the National Capital Territory (not full statehood).",
        "effect": "NCT label for Delhi UT.",
        "concept_slugs": ["uit-reference-tables", "uit-map-after-1956"],
    },
    {
        "number": 100,
        "year": 2015,
        "title": "One Hundredth Amendment",
        "summary": (
            "India–Bangladesh land boundary agreement — enclaves and related First Schedule changes."
        ),
        "effect": "Modified territories of Assam, West Bengal, Meghalaya, and Tripura.",
        "concept_slugs": ["uit-cession-boundary", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed Union and Its Territory chapter (Laxmikanth Ch.6)."

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
                "title": "Union and Its Territory",
                "sort_order": 6,
                "book_ref": "Laxmikanth 8th Ed, Ch. 6",
                "summary": (
                    "Visual revision of Ch.6 — Arts 1–4, indestructible Union of destructible States, "
                    "reorganisation path, and the present 28+8 map."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Union and Its Territory",
                "summary": (
                    "Part I (Arts 1–4) — Union of States, three-fold territory, Parliament’s power "
                    "to redraw the map, and how India reached 28 states + 8 UTs."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **redrawable-map mental model**, then Arts **1 → 4**. "
                    "Lock **cession ≠ Art. 3**, then skim the reorganisation timeline and J&K 2019. "
                    "Use Reference Tables only as a scan deck — not a re-read of Laxmikanth."
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
            ref="Laxmikanth Ch. 6",
            excerpt="Union and Its Territory — Part I, Articles 1 to 4.",
            sort_order=0,
        )

        uit_slugs = set(by_slug.keys())
        related_outside = {"sf-federal-unitary"}
        ConceptEdge.objects.filter(
            source__slug__in=uit_slugs, source__subject=subject
        ).filter(target__slug__in=uit_slugs | related_outside).delete()

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
                f"Union and Its Territory chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments."
            )
        )
