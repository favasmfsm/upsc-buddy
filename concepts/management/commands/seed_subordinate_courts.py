"""Seed Laxmikanth Ch.35 Subordinate Courts (visual revision)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import (
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "subordinate-courts"
CHAPTER_SLUG = "subordinate-courts"

ENTRY_PILLARS = [
    {
        "id": "const-map",
        "articles": "233–237",
        "label": "Constitutional map",
        "slug": "sc-constitutional-map",
        "detail": "Part VI — organise lower courts + keep them free of executive grip.",
        "tone": "teal",
    },
    {
        "id": "dj",
        "articles": "Art. 233",
        "label": "District Judges",
        "slug": "sc-district-judges",
        "detail": "Governor appoints/posts/promotes — after HC consultation + recommendation.",
        "tone": "olive",
    },
    {
        "id": "other",
        "articles": "Art. 234",
        "label": "Other judges",
        "slug": "sc-other-judges",
        "detail": "Governor + SPSC + HC — SPSC exam in practice.",
        "tone": "gold",
    },
    {
        "id": "control",
        "articles": "Art. 235",
        "label": "HC control",
        "slug": "sc-hc-control",
        "detail": "Posting, promotion, leave of officers below district judge — HC’s reins.",
        "tone": "orange",
    },
    {
        "id": "hierarchy",
        "articles": "3 tiers",
        "label": "Court hierarchy",
        "slug": "sc-hierarchy",
        "detail": "HC → District & Sessions → civil/criminal middle → lowest courts.",
        "tone": "terracotta",
    },
    {
        "id": "sessions",
        "articles": "Dual hat",
        "label": "District & Sessions",
        "slug": "sc-district-sessions",
        "detail": "Same person; death sentence needs HC confirmation.",
        "tone": "maroon",
    },
    {
        "id": "tiers",
        "articles": "Limits",
        "label": "Tier jurisdiction",
        "slug": "sc-tiers-jurisdiction",
        "detail": "CJM ≤7 yrs · JM ≤3 yrs · Sub-Judge unlimited pecuniary.",
        "tone": "teal",
    },
    {
        "id": "special",
        "articles": "Local",
        "label": "Special courts",
        "slug": "sc-special-courts",
        "detail": "City civil / Metro Mag · Small Causes · Panchayat Courts.",
        "tone": "olive",
    },
    {
        "id": "glance",
        "articles": "Table 35.1",
        "label": "Articles glance",
        "slug": "sc-articles-glance",
        "detail": "233 · 233A · 234 · 235 · 236 · 237 — one-line each.",
        "tone": "gold",
    },
    {
        "id": "exam",
        "articles": "Prelims · Mains",
        "label": "Exam kit",
        "slug": "sc-exam-kit",
        "detail": "Traps, PYQ themes, memory palace, mains value-adds.",
        "tone": "orange",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "sc-mental-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "HC’s lower arm",
        "topic_label": "Subordinate Courts",
        "subject_label": "Part VI · Arts 233–237 · Ch. 35",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating lower courts as executive departments",
            "Confusing Art. 233 vs 234 consultees",
            "Forgetting District Judge = Sessions Judge",
            "Skipping HC confirmation for death sentence",
        ],
        "insight": (
            "State judiciary = High Court + subordinate courts. "
            "Governor appoints; High Court recommends and controls — independence by design."
        ),
    },
    {
        "id": "sc-entry-pillars",
        "type": "pillars",
        "title": "Ten revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "sc-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Governor appoints · High Court recommends/controls · "
            "District Judge = Sessions Judge. "
            "Scan 233 → 234 → 235 → hierarchy → death-sentence confirm."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Constitutional Map (Arts 233–237)",
        "slug": "sc-constitutional-map",
        "sort_order": 1,
        "summary": (
            "Part VI provisions that organise subordinate courts and keep them "
            "independent of the executive."
        ),
        "body": (
            "## What ‘subordinate’ means\n\n"
            "State judiciary = **High Court** + a hierarchy of **lower courts**. "
            "They are ‘subordinate’ because they function **below and under** the High Court "
            "at district and lower levels.\n\n"
            "## Why Arts 233–237 exist\n\n"
            "Two jobs:\n"
            "1. **Organise** appointment, recruitment, control, and definitions.\n"
            "2. **Insulate** the lower judiciary from executive dominance.\n\n"
            "### Memory cue\n"
            "**O-I** — Organise + Independence. Same spine as the integrated judiciary theme "
            "(SC → HC → subordinate courts)."
        ),
        "articles": [
            (
                "Arts 233–237",
                "Part VI Chapter VI — organisation and independence of subordinate courts.",
            ),
            (
                "Laxmikanth Ch. 35",
                "Constitutional provisions opening the Subordinate Courts chapter.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-map-explorer",
                "type": "article_explorer",
                "title": "Arts 233–237 spine",
                "article_ref": "Part VI · Arts 233–237",
                "stages": [
                    {
                        "id": "a233",
                        "label": "233 — District Judges",
                        "detail": "Appointment, posting, promotion by Governor in consultation with HC.",
                    },
                    {
                        "id": "a233a",
                        "label": "233A — Validation",
                        "detail": "20th Amendment (1966) — retrospective validation of certain DJ appointments/judgements.",
                    },
                    {
                        "id": "a234",
                        "label": "234 — Other judges",
                        "detail": "Recruitment below DJ — Governor after consulting SPSC + HC.",
                    },
                    {
                        "id": "a235",
                        "label": "235 — Control",
                        "detail": "HC controls posting, promotion, leave of officers inferior to DJ.",
                    },
                    {
                        "id": "a236",
                        "label": "236 — Interpretation",
                        "detail": "Defines ‘district judge’ and ‘judicial service’.",
                    },
                    {
                        "id": "a237",
                        "label": "237 — Magistrates",
                        "detail": "Governor may apply these provisions to classes of magistrates.",
                    },
                ],
            },
            {
                "id": "sc-map-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Constitution sets the **independence spine**; states set structure, "
                    "jurisdiction, and nomenclature of lower courts (slight interstate variation)."
                ),
            },
        ],
    },
    {
        "title": "Appointment of District Judges",
        "slug": "sc-district-judges",
        "sort_order": 2,
        "summary": (
            "Art. 233 — Governor appoints, posts, and promotes district judges "
            "in consultation with the High Court; three eligibility conditions."
        ),
        "body": (
            "## Who decides\n\n"
            "**Governor** of the state makes appointment, posting, and promotion of district judges "
            "**in consultation with the High Court**.\n\n"
            "## Three qualifications\n\n"
            "1. **Not already** in the service of the Central or the state government.\n"
            "2. Advocate or pleader for **seven years**.\n"
            "3. **Recommended by the High Court** for appointment.\n\n"
            "### Memory aid — N-7-R\n"
            "**N**ot in govt service · **7** years bar · **R**ecommended by HC.\n\n"
            "### Who consults whom?\n"
            "**G + HC** only — no SPSC in Art. 233 (contrast Art. 234)."
        ),
        "articles": [
            (
                "Art. 233",
                "Appointment, posting and promotion of district judges by the Governor in consultation with the High Court.",
            ),
            (
                "Art. 233A",
                "Validation of appointments of, and judgements delivered by, certain district judges (20th Amendment).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-dj-flow",
                "type": "flowchart",
                "title": "Path to District Judge",
                "root": "elig",
                "steps": [
                    {
                        "id": "elig",
                        "label": "Eligibility check",
                        "detail": "Not in Central/state service + 7 years as advocate/pleader.",
                        "options": [
                            {"label": "Eligible", "next": "rec"},
                            {"label": "In govt service / <7 yrs", "next": "fail"},
                        ],
                    },
                    {
                        "id": "rec",
                        "label": "High Court recommends",
                        "detail": "HC recommendation is a constitutional condition for appointment.",
                        "options": [{"label": "Recommended", "next": "gov"}],
                    },
                    {
                        "id": "gov",
                        "label": "Governor appoints / posts / promotes",
                        "detail": "Art. 233 — after consultation with the High Court.",
                    },
                    {
                        "id": "fail",
                        "label": "Cannot appoint under Art. 233 route",
                        "detail": "Fails the three-fold qualification test.",
                    },
                ],
            },
            {
                "id": "sc-dj-233a",
                "type": "callout",
                "tone": "tip",
                "title": "Art. 233A · 20th Amendment (1966)",
                "body": (
                    "Retrospectively validated certain district-judge appointments and the "
                    "judgements delivered by them — classic amendment–article pairing for Prelims."
                ),
            },
        ],
    },
    {
        "title": "Appointment of Other Judges",
        "slug": "sc-other-judges",
        "sort_order": 3,
        "summary": (
            "Art. 234 — persons other than district judges enter the state judicial service "
            "via Governor after consulting SPSC and the High Court."
        ),
        "body": (
            "## Art. 234 rule\n\n"
            "Appointment of persons **other than district judges** to the judicial service of a state "
            "is made by the **Governor** after consultation with:\n"
            "1. the **State Public Service Commission**, and\n"
            "2. the **High Court**.\n\n"
            "## Practice note\n\n"
            "In practice, the SPSC conducts a **competitive examination** for recruitment to the "
            "state judicial service.\n\n"
            "### Trap\n"
            "Do **not** mix consultees: **233 = HC only**; **234 = SPSC + HC**."
        ),
        "articles": [
            (
                "Art. 234",
                "Recruitment of persons other than district judges to the judicial service.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-233-vs-234",
                "type": "comparison",
                "title": "Art. 233 vs Art. 234",
                "columns": [
                    {
                        "id": "a233",
                        "heading": "Art. 233 — District Judges",
                        "points": [
                            "Post: District Judge",
                            "Appointing authority: Governor",
                            "Consults: High Court only",
                            "HC recommendation required",
                            "Quals: not in service + 7 yrs bar",
                            "Also covers posting & promotion",
                        ],
                    },
                    {
                        "id": "a234",
                        "heading": "Art. 234 — Other judges",
                        "points": [
                            "Post: below District Judge",
                            "Appointing authority: Governor",
                            "Consults: SPSC + High Court",
                            "SPSC competitive exam in practice",
                            "Entry to state judicial service",
                            "Later control shifts under Art. 235",
                        ],
                    },
                ],
            },
            {
                "id": "sc-234-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims trap",
                "body": (
                    "If a statement says ‘SPSC consults for district judges’ — false. "
                    "SPSC enters only for **other than** district judges (Art. 234)."
                ),
            },
        ],
    },
    {
        "title": "Control over Subordinate Courts",
        "slug": "sc-hc-control",
        "sort_order": 4,
        "summary": (
            "Art. 235 — High Court controls district courts and other subordinate courts, "
            "including posting, promotion, and leave of officers below district judge."
        ),
        "body": (
            "## What Art. 235 vests in the High Court\n\n"
            "Control over **district courts and other subordinate courts**, including:\n"
            "- **posting**,\n"
            "- **promotion**, and\n"
            "- **leave**\n"
            "of persons belonging to the judicial service of a state and holding any post "
            "**inferior to the post of district judge**.\n\n"
            "### Why it matters\n"
            "Administrative supremacy of the HC over the lower judiciary is the operational "
            "guarantee of **independence from the executive**.\n\n"
            "### Memory\n"
            "**235 = HC holds the reins below DJ.**"
        ),
        "articles": [
            (
                "Art. 235",
                "Control over subordinate courts vested in the High Court.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-control-pillars",
                "type": "pillars",
                "title": "HC control bundle (Art. 235)",
                "items": [
                    {
                        "id": "posting",
                        "articles": "235",
                        "label": "Posting",
                        "detail": "Where officers below DJ serve.",
                        "tone": "teal",
                    },
                    {
                        "id": "promo",
                        "articles": "235",
                        "label": "Promotion",
                        "detail": "Career movement within posts inferior to DJ.",
                        "tone": "olive",
                    },
                    {
                        "id": "leave",
                        "articles": "235",
                        "label": "Leave",
                        "detail": "Leave control of the same class of officers.",
                        "tone": "gold",
                    },
                    {
                        "id": "scope",
                        "articles": "Below DJ",
                        "label": "Scope cue",
                        "detail": "District courts + other subordinate courts — officers below DJ.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "sc-control-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "Appointment (233/234) may involve the Governor — day-to-day "
                    "**control below DJ** sits with the **High Court**, not the executive."
                ),
            },
        ],
    },
    {
        "title": "Court Hierarchy",
        "slug": "sc-hierarchy",
        "sort_order": 5,
        "summary": (
            "Three tiers of civil and criminal courts below the High Court — "
            "structure set by states, with slight interstate variation."
        ),
        "body": (
            "## Who designs the map?\n\n"
            "Organisational structure, jurisdiction, and **nomenclature** of the subordinate "
            "judiciary are laid down by the **states** — hence slight differences across states.\n\n"
            "## Exam map (broad)\n\n"
            "Three tiers below the High Court on both **civil** and **criminal** sides.\n\n"
            "```\n"
            "High Court\n"
            "└── District & Sessions Court\n"
            "    ├── Civil: Subordinate Judge → Munsiff\n"
            "    └── Criminal: CJM → Judicial Magistrate\n"
            "```\n\n"
            "Use this tree for last-minute recall; local names may vary (Civil Judge Sr/Jr, etc.)."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 35",
                "Structure and jurisdiction — three tiers below the High Court.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-hierarchy-tree",
                "type": "tree",
                "title": "Subordinate court hierarchy",
                "root": {
                    "id": "hc",
                    "label": "High Court",
                    "detail": "Apex of state judicial administration",
                    "children": [
                        {
                            "id": "dist",
                            "label": "District & Sessions Court",
                            "detail": "Highest authority in the district",
                            "slug": "sc-district-sessions",
                            "children": [
                                {
                                    "id": "civil-mid",
                                    "label": "Subordinate Judge (civil)",
                                    "detail": "Also Civil Judge (Sr) / Class I",
                                    "children": [
                                        {
                                            "id": "munsiff",
                                            "label": "Munsiff (civil)",
                                            "detail": "Civil Judge (Jr) / Class II",
                                        }
                                    ],
                                },
                                {
                                    "id": "crm-mid",
                                    "label": "Chief Judicial Magistrate",
                                    "detail": "Criminal middle tier",
                                    "children": [
                                        {
                                            "id": "jm",
                                            "label": "Judicial Magistrate",
                                            "detail": "Lowest criminal tier",
                                        }
                                    ],
                                },
                            ],
                        }
                    ],
                },
            },
            {
                "id": "sc-hierarchy-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "Constitution = independence spine (233–237). "
                    "States = structure, names, and exact jurisdiction limits."
                ),
            },
        ],
    },
    {
        "title": "District & Sessions Judge",
        "slug": "sc-district-sessions",
        "sort_order": 6,
        "summary": (
            "Highest judicial authority in the district — dual civil/criminal hat, "
            "supervisory powers, and death sentence subject to HC confirmation."
        ),
        "body": (
            "## Dual hat\n\n"
            "The **district judge** is the highest judicial authority in the district.\n"
            "- Civil matters → called **District Judge**\n"
            "- Criminal matters → called **Sessions Judge**\n\n"
            "## Powers pack\n\n"
            "- **Original + appellate** jurisdiction (civil and criminal)\n"
            "- **Judicial + administrative** powers\n"
            "- **Supervisory** powers over all subordinate courts in the district\n"
            "- Appeals against orders/judgements → **High Court**\n\n"
            "## Death sentence rule\n\n"
            "Sessions Judge may impose **any sentence**, including life and capital punishment. "
            "A **death sentence must be confirmed by the High Court**, whether or not there is an appeal.\n\n"
            "## Art. 236 definitions (revision)\n\n"
            "- **‘District judge’** includes: city civil court judge, ADJ, joint/assistant DJ, "
            "chief judge of small causes court, chief / additional chief presidency magistrate, "
            "sessions / additional / assistant sessions judge.\n"
            "- **‘Judicial service’** = service consisting exclusively of persons intended to fill "
            "the post of district judge and other **civil** judicial posts inferior to DJ."
        ),
        "articles": [
            (
                "Art. 236",
                "Interpretation of ‘district judge’ and ‘judicial service’.",
            ),
            (
                "Laxmikanth Ch. 35",
                "District and Sessions Court — dual hat, supervision, death sentence confirmation.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-dual-hat",
                "type": "comparison",
                "title": "Same person — two hats",
                "columns": [
                    {
                        "id": "civil",
                        "heading": "As District Judge",
                        "points": [
                            "Civil side of the district court",
                            "Original + appellate civil jurisdiction",
                            "Supervises subordinate civil courts in district",
                            "Appeals lie to the High Court",
                        ],
                    },
                    {
                        "id": "criminal",
                        "heading": "As Sessions Judge",
                        "points": [
                            "Criminal side of the same court",
                            "Can impose any sentence including death",
                            "Death sentence → mandatory HC confirmation",
                            "Appeals lie to the High Court",
                        ],
                    },
                ],
            },
            {
                "id": "sc-death-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor — death sentence",
                "body": (
                    "Sessions Judge can award death — but the sentence does **not** become final "
                    "without **High Court confirmation**, even if nobody appeals."
                ),
            },
        ],
    },
    {
        "title": "Three-Tier Jurisdiction",
        "slug": "sc-tiers-jurisdiction",
        "sort_order": 7,
        "summary": (
            "Middle and lowest civil/criminal tiers — pecuniary and imprisonment limits "
            "that UPSC loves to mix up."
        ),
        "body": (
            "## Middle tier\n\n"
            "- **Civil:** Court of Subordinate Judges (also Civil Judge Sr / Class I) — "
            "**unlimited pecuniary** jurisdiction over civil suits.\n"
            "- **Criminal:** Chief Judicial Magistrate — offences punishable with imprisonment "
            "up to **seven years**.\n\n"
            "A subordinate judge may also be given **assistant sessions** powers → combines "
            "civil + criminal powers (DJ pattern at a lower level).\n\n"
            "## Lowest tier\n\n"
            "- **Civil:** Court of Munsiff (Civil Judge Jr / Class II) — **limited** pecuniary "
            "jurisdiction; small-stake civil cases.\n"
            "- **Criminal:** Judicial Magistrate — imprisonment up to **three years**.\n\n"
            "### Memory — 7 / 3\n"
            "**CJM = 7 years · JM = 3 years.**"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 35",
                "Courts of Subordinate Judges / CJM and Munsiff / Judicial Magistrate.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-tiers-table",
                "type": "comparison",
                "title": "Three tiers — civil × criminal",
                "columns": [
                    {
                        "id": "top",
                        "heading": "District level",
                        "points": [
                            "Civil: District Judge",
                            "Criminal: Sessions Judge",
                            "Any sentence; death needs HC confirm",
                            "Original + appellate; supervisory",
                        ],
                    },
                    {
                        "id": "mid",
                        "heading": "Middle tier",
                        "points": [
                            "Civil: Subordinate Judge / Civil Judge (Sr)",
                            "Criminal: Chief Judicial Magistrate",
                            "Unlimited pecuniary (civil)",
                            "Criminal: up to 7 years",
                        ],
                    },
                    {
                        "id": "low",
                        "heading": "Lowest tier",
                        "points": [
                            "Civil: Munsiff / Civil Judge (Jr)",
                            "Criminal: Judicial Magistrate",
                            "Limited / small pecuniary stake",
                            "Criminal: up to 3 years",
                        ],
                    },
                ],
            },
            {
                "id": "sc-tiers-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Trap box",
                "body": (
                    "Unlimited pecuniary ≠ Sessions powers. "
                    "Subordinate Judge gets unlimited civil stake; criminal ‘any sentence’ "
                    "belongs to the **Sessions Judge** (with HC confirm for death)."
                ),
            },
        ],
    },
    {
        "title": "Special and Local Courts",
        "slug": "sc-special-courts",
        "sort_order": 8,
        "summary": (
            "City civil courts and metropolitan magistrates, small causes courts, "
            "and Panchayat Courts for petty matters."
        ),
        "body": (
            "## Metropolitan pattern\n\n"
            "In some metropolitan cities:\n"
            "- **City civil courts** (chief judges) on the civil side\n"
            "- **Courts of metropolitan magistrates** on the criminal side\n\n"
            "## Small Causes Courts\n\n"
            "Some states and former presidency towns (Delhi, Bombay, Calcutta, Madras) have "
            "Small Causes Courts:\n"
            "- Decide civil cases of **small value** in a **summary** manner\n"
            "- Decisions are **final**\n"
            "- High Court retains **revision** power\n\n"
            "## Panchayat Courts\n\n"
            "In some states, Panchayat Courts try **petty** civil and criminal cases. "
            "Names vary: Nyaya Panchayat, Gram Kutchery, Adalati Panchayat, Panchayat Adalat, etc.\n\n"
            "_Note: Gram Nyayalayas Act, 2008 is a later/related theme — not part of Ch.35 core._"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 35",
                "City civil courts, metropolitan magistrates, small causes, and Panchayat Courts.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-special-pillars",
                "type": "pillars",
                "title": "Three local variants",
                "items": [
                    {
                        "id": "metro",
                        "articles": "Metros",
                        "label": "City civil + Metro Mag",
                        "detail": "Urban civil (chief judges) and metropolitan criminal courts.",
                        "tone": "teal",
                    },
                    {
                        "id": "scc",
                        "articles": "Summary",
                        "label": "Small Causes Courts",
                        "detail": "Small-value civil · summary · final · HC revision.",
                        "tone": "olive",
                    },
                    {
                        "id": "panch",
                        "articles": "Petty",
                        "label": "Panchayat Courts",
                        "detail": "Petty civil/criminal; many local names.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "sc-special-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims cue — Small Causes",
                "body": (
                    "Final decision ≠ no High Court role. "
                    "Appeal is shut; **revision** by the High Court remains."
                ),
            },
        ],
    },
    {
        "title": "Articles at a Glance",
        "slug": "sc-articles-glance",
        "sort_order": 9,
        "summary": (
            "Table 35.1 redesigned — Arts 233 to 237 (including 233A) in one scan."
        ),
        "body": (
            "## Table 35.1 — compressed\n\n"
            "| Article | Subject |\n"
            "|---------|--------|\n"
            "| **233** | Appointment of district judges |\n"
            "| **233A** | Validation of appointments of, and judgements by, certain district judges |\n"
            "| **234** | Recruitment of persons other than district judges |\n"
            "| **235** | Control over subordinate courts |\n"
            "| **236** | Interpretation |\n"
            "| **237** | Application of Chapter provisions to certain magistrates |\n\n"
            "### Art. 237 one-liner\n"
            "Governor may direct that the Chapter VI provisions relating to persons in the "
            "state judicial service **apply to any class or classes of magistrates** in the state."
        ),
        "articles": [
            ("Art. 233", "Appointment of district judges."),
            ("Art. 233A", "Validation of certain district-judge appointments and judgements."),
            ("Art. 234", "Recruitment of persons other than district judges."),
            ("Art. 235", "Control over subordinate courts."),
            ("Art. 236", "Interpretation."),
            ("Art. 237", "Application to certain class or classes of Magistrates."),
        ],
        "visual_blocks": [
            {
                "id": "sc-glance-compare",
                "type": "comparison",
                "title": "Articles Related to Subordinate Courts",
                "columns": [
                    {
                        "id": "appoint",
                        "heading": "Appoint / recruit",
                        "points": [
                            "233 — District Judges (Governor + HC)",
                            "233A — Validation (20th Amdt, 1966)",
                            "234 — Other than DJ (Governor + SPSC + HC)",
                        ],
                    },
                    {
                        "id": "control-def",
                        "heading": "Control / define / extend",
                        "points": [
                            "235 — HC control below DJ",
                            "236 — ‘district judge’ & ‘judicial service’",
                            "237 — extend Chapter rules to magistrates",
                        ],
                    },
                ],
            },
            {
                "id": "sc-glance-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Last-minute scan",
                "body": "233 G+HC · 234 G+SPSC+HC · 235 HC reins · 236 definitions · 237 magistrates gate.",
            },
        ],
    },
    {
        "title": "Exam Kit — Prelims, PYQs & Mains",
        "slug": "sc-exam-kit",
        "sort_order": 10,
        "summary": (
            "High-yield traps, recurring themes, memory palace, and mains value-adds "
            "for Subordinate Courts."
        ),
        "body": (
            "## Prelims traps\n\n"
            "1. **233 vs 234 consultees** — HC only vs SPSC + HC.\n"
            "2. **Death sentence** — Sessions Judge may award; **HC confirmation mandatory**.\n"
            "3. **CJM 7 years vs JM 3 years** — do not swap.\n"
            "4. **Art. 235 control** is with the **High Court**, not the Governor.\n"
            "5. **20th Amendment / Art. 233A** — retrospective validation pairing.\n"
            "6. Small Causes: decisions **final**, but HC has **revision**.\n\n"
            "## Mains value-adds\n\n"
            "- Subordinate judiciary as **independence-from-executive** design (appointment + HC control).\n"
            "- **Administrative supremacy** of HC under Art. 235.\n"
            "- District dual hat (civil/criminal) as the hub of district justice delivery.\n"
            "- Constitutional core vs **state-made** structure/nomenclature — federal texture inside one judiciary.\n\n"
            "### One-liner for answers\n"
            "“Governor appoints; High Court recommends and controls — the Constitution’s formula "
            "for an independent subordinate judiciary.”"
        ),
        "articles": [
            (
                "Arts 233–237",
                "Full constitutional spine for subordinate courts revision.",
            ),
            (
                "Laxmikanth Ch. 35",
                "Structure, jurisdiction, and Table 35.1 — exam redesign layer.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sc-pyq-heat",
                "type": "pyq_heatmap",
                "title": "PYQ focus map",
                "items": [
                    {"concept_slug": "sc-district-judges", "label": "DJ appointment (233)"},
                    {"concept_slug": "sc-other-judges", "label": "Other judges (234)"},
                    {"concept_slug": "sc-hc-control", "label": "HC control (235)"},
                    {
                        "concept_slug": "sc-district-sessions",
                        "label": "Sessions / death confirm",
                    },
                    {
                        "concept_slug": "sc-tiers-jurisdiction",
                        "label": "7 yrs / 3 yrs limits",
                    },
                    {"concept_slug": "sc-articles-glance", "label": "Articles glance"},
                ],
            },
            {
                "id": "sc-memory-palace",
                "type": "memory_palace",
                "title": "District court corridor walk",
                "setting": "District court corridor from HC gallery to magistrate rooms",
                "loci": [
                    {
                        "id": "l1",
                        "place": "Governor’s seal on the door",
                        "association": "Art. 233 — G + HC",
                        "detail": "Appoint / post / promote DJ after HC consultation; N-7-R quals.",
                    },
                    {
                        "id": "l2",
                        "place": "SPSC notice board",
                        "association": "Art. 234",
                        "detail": "Other than DJ — Governor consults SPSC + HC; exam in practice.",
                    },
                    {
                        "id": "l3",
                        "place": "HC control desk",
                        "association": "Art. 235",
                        "detail": "Posting, promotion, leave below DJ — HC holds the reins.",
                    },
                    {
                        "id": "l4",
                        "place": "Sessions courtroom",
                        "association": "Dual hat + death confirm",
                        "detail": "District Judge = Sessions Judge; death needs HC confirmation.",
                    },
                    {
                        "id": "l5",
                        "place": "Magistrate wing — two clocks",
                        "association": "7 / 3",
                        "detail": "CJM up to 7 years; Judicial Magistrate up to 3 years.",
                    },
                ],
            },
            {
                "id": "sc-exam-tip",
                "type": "callout",
                "tone": "tip",
                "title": "60-second revision",
                "body": (
                    "233 G+HC · 234 G+SPSC+HC · 235 HC reins · DJ=SJ · death→HC confirm · "
                    "CJM 7 / JM 3 · 20th Amdt = 233A."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "sc-constitutional-map"),
    (HUB_SLUG, "parent", "sc-district-judges"),
    (HUB_SLUG, "parent", "sc-other-judges"),
    (HUB_SLUG, "parent", "sc-hc-control"),
    (HUB_SLUG, "parent", "sc-hierarchy"),
    (HUB_SLUG, "parent", "sc-district-sessions"),
    (HUB_SLUG, "parent", "sc-tiers-jurisdiction"),
    (HUB_SLUG, "parent", "sc-special-courts"),
    (HUB_SLUG, "parent", "sc-articles-glance"),
    (HUB_SLUG, "parent", "sc-exam-kit"),
    ("sc-constitutional-map", "related", "sc-articles-glance"),
    ("sc-district-judges", "related", "sc-other-judges"),
    ("sc-other-judges", "related", "sc-hc-control"),
    ("sc-hierarchy", "related", "sc-district-sessions"),
    ("sc-district-sessions", "related", "sc-tiers-jurisdiction"),
    ("sc-tiers-jurisdiction", "related", "sc-special-courts"),
    ("sc-articles-glance", "related", "sc-exam-kit"),
    ("sc-hc-control", "related", "sc-exam-kit"),
    ("high-court", "related", HUB_SLUG),
    ("supreme-court", "related", HUB_SLUG),
]

AMENDMENTS = [
    {
        "number": 20,
        "year": 1966,
        "title": "Twentieth Amendment",
        "summary": (
            "Inserted Article 233A to retrospectively validate appointments of certain "
            "district judges and judgements delivered by them."
        ),
        "effect": (
            "Cured defects in certain district-judge appointments; classic pairing with Art. 233A."
        ),
        "concept_slugs": ["sc-district-judges", "sc-articles-glance", HUB_SLUG],
    },
]

SAMPLE_PYQS = [
    (
        2016,
        (
            "The appointment, posting and promotion of district judges in a State are made by "
            "the Governor in consultation with which of the following?"
        ),
        "The High Court of the State (Art. 233) — SPSC is not a consultee for district judges.",
        ["sc-district-judges", "sc-exam-kit", HUB_SLUG],
    ),
    (
        2019,
        (
            "With reference to the control over subordinate courts, which statement is correct?"
        ),
        (
            "Art. 235 vests control — including posting, promotion and leave of officers "
            "inferior to district judge — in the High Court."
        ),
        ["sc-hc-control", "sc-exam-kit", HUB_SLUG],
    ),
    (
        2021,
        (
            "Consider the dual role of the highest judicial authority in a district. "
            "Which of the following is correct?"
        ),
        (
            "The same person acts as District Judge (civil) and Sessions Judge (criminal); "
            "a death sentence passed by the Sessions Judge requires High Court confirmation "
            "even without an appeal."
        ),
        ["sc-district-sessions", "sc-exam-kit", HUB_SLUG],
    ),
    (
        2014,
        (
            "Recruitment of persons other than district judges to the judicial service of a State "
            "is made by the Governor after consultation with:"
        ),
        "The State Public Service Commission and the High Court (Art. 234).",
        ["sc-other-judges", "sc-exam-kit", HUB_SLUG],
    ),
]


class Command(BaseCommand):
    help = "Seed Subordinate Courts chapter (Laxmikanth Ch.35)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug to seed into (default: fortuneias).",
        )

    def handle(self, *args, **options):
        from academies.seed_utils import get_academy_or_fail
        from subjects.models import Section

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
                "title": "Subordinate Courts",
                "sort_order": 6,
                "book_ref": "Laxmikanth 8th Ed, Ch. 35 · pp. 521–524",
                "summary": (
                    "Visual revision of Ch.35 — Arts 233–237, district-judge appointment, "
                    "HC control, hierarchy, jurisdiction, and exam kit."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="state-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Subordinate Courts",
                "summary": (
                    "HC’s lower arm — Part VI Arts 233–237 organise the district judiciary "
                    "and keep it independent of the executive."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **HC’s lower arm** mental model, then "
                    "**Constitutional map** → **233 / 234 / 235** → **Hierarchy** → "
                    "**District & Sessions** → **Tier limits**. Finish with "
                    "**Articles glance** and the **Exam kit**. "
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
            ref="Arts 233–237",
            excerpt=(
                "Part VI Chapter VI — organisation and independence of subordinate courts."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Laxmikanth Ch. 35",
            excerpt=(
                "Subordinate Courts — constitutional provisions, structure, "
                "jurisdiction, and Table 35.1."
            ),
            sort_order=1,
        )

        sc_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=sc_slugs) | Q(target__slug__in=sc_slugs),
            source__subject=subject,
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

        for amd_data in AMENDMENTS:
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

        self.stdout.write(
            self.style.SUCCESS(
                f"Subordinate Courts chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(AMENDMENTS)} amendments, {len(SAMPLE_PYQS)} PYQs linked."
            )
        )
