"""Seed Laxmikanth Ch.36 Tribunals (visual revision — Part IV State Government)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "tribunals"
CHAPTER_SLUG = "tribunals"

ENTRY_PILLARS = [
    {
        "id": "origin",
        "articles": "42nd · XIV-A",
        "label": "Origin & Part XIV-A",
        "slug": "tr-origin",
        "detail": "No original tribunal Part — 42nd adds Arts 323A & 323B only.",
        "tone": "teal",
    },
    {
        "id": "a323a",
        "articles": "Art. 323A",
        "label": "323A & AT Act 1985",
        "slug": "tr-323a-act",
        "detail": "Parliament only — service disputes out of civil courts/HCs.",
        "tone": "olive",
    },
    {
        "id": "cat",
        "articles": "CAT",
        "label": "Central Administrative Tribunal",
        "slug": "tr-cat",
        "detail": "19 benches; coverage & exclusions; natural justice; ₹50.",
        "tone": "gold",
    },
    {
        "id": "sat",
        "articles": "SAT · JAT",
        "label": "State & Joint Tribunals",
        "slug": "tr-sat-jat",
        "detail": "On state request; HC CJ chairs search committee; JAT for 2+ states.",
        "tone": "orange",
    },
    {
        "id": "a323b",
        "articles": "Art. 323B",
        "label": "323B — other matters",
        "slug": "tr-323b",
        "detail": "Eight subjects; Parliament + States; hierarchy allowed.",
        "tone": "terracotta",
    },
    {
        "id": "compare",
        "articles": "3 diffs",
        "label": "323A vs 323B",
        "slug": "tr-323a-vs-323b",
        "detail": "Subject · who establishes · hierarchy — the Prelims trio.",
        "tone": "maroon",
    },
    {
        "id": "chandra",
        "articles": "1997",
        "label": "Chandra Kumar & appeals",
        "slug": "tr-chandra-kumar",
        "detail": "Judicial review = basic structure; CAT → HC DB → SC.",
        "tone": "teal",
    },
    {
        "id": "exam",
        "articles": "PYQ kit",
        "label": "Exam kit",
        "slug": "tr-exam-kit",
        "detail": "Prelims facts, PYQ themes, mains one-liners.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "tr-lane-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Specialised lane",
        "topic_label": "Tribunals",
        "subject_label": "Part XIV-A · Arts 323A–323B",
        "relation_label": "Protects you from",
        "protects_from": [
            "Thinking tribunals erase High Court judicial review",
            "Mixing 323A (services) with 323B (other matters)",
            "Assuming States can create 323A tribunals",
            "Skipping HC and jumping straight to the Supreme Court from CAT",
        ],
        "insight": (
            "Part XIV-A routes selected disputes to specialised tribunals for speed "
            "and cost — but Chandra Kumar keeps HC/SC judicial review intact."
        ),
    },
    {
        "id": "tr-entry-pillars",
        "type": "pillars",
        "title": "Eight revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "tr-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "323A = services · Parliament only · no hierarchy. "
            "323B = eight matters · Parliament + States · hierarchy OK. "
            "Appeals: CAT → HC Division Bench → SC (Chandra Kumar, 1997)."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Origin & Part XIV-A",
        "slug": "tr-origin",
        "sort_order": 1,
        "summary": (
            "Original Constitution silent on tribunals — 42nd Amendment (1976) "
            "adds Part XIV-A with only Articles 323A and 323B."
        ),
        "body": (
            "## Where tribunals sit\n\n"
            "The original Constitution had **no** tribunal provisions. "
            "The **42nd Amendment Act, 1976** inserted **Part XIV-A — Tribunals**, "
            "containing only two Articles:\n\n"
            "- **Article 323A** — administrative tribunals (service matters)\n"
            "- **Article 323B** — tribunals for other specified matters\n\n"
            "### Timeline hook\n"
            "1976 (Part XIV-A) → 1985 (AT Act / CAT) → 1993 (75th: rent & tenancy in 323B) "
            "→ 1997 (Chandra Kumar) → 2006 (Vice-Chairman removed) → 2021 "
            "(Tribunals Reforms Act — tenure/age footnote in Laxmikanth)."
        ),
        "articles": [
            ("Art. 323A", "Administrative tribunals — Part XIV-A."),
            ("Art. 323B", "Tribunals for other matters — Part XIV-A."),
            ("42nd Amendment", "1976 — inserted Part XIV-A."),
        ],
        "visual_blocks": [
            {
                "id": "tr-origin-tree",
                "type": "tree",
                "title": "Constitutional map",
                "root": {
                    "id": "const",
                    "label": "Constitution of India",
                    "children": [
                        {
                            "id": "xiva",
                            "label": "Part XIV-A — Tribunals",
                            "detail": "42nd Amendment, 1976",
                            "children": [
                                {
                                    "id": "a323a",
                                    "label": "Art. 323A",
                                    "slug": "tr-323a-act",
                                    "detail": "Administrative / service matters",
                                },
                                {
                                    "id": "a323b",
                                    "label": "Art. 323B",
                                    "slug": "tr-323b",
                                    "detail": "Other specified matters",
                                },
                            ],
                        }
                    ],
                },
            },
            {
                "id": "tr-origin-timeline",
                "type": "timeline",
                "title": "Tribunals timeline",
                "events": [
                    {
                        "id": "e1976",
                        "year": 1976,
                        "label": "42nd Amendment",
                        "detail": "Part XIV-A added — Arts 323A & 323B.",
                    },
                    {
                        "id": "e1985",
                        "year": 1985,
                        "label": "AT Act & CAT",
                        "detail": "Administrative Tribunals Act; CAT set up.",
                    },
                    {
                        "id": "e1993",
                        "year": 1993,
                        "label": "75th Amendment",
                        "detail": "Rent & tenancy rights added to 323B list.",
                    },
                    {
                        "id": "e1997",
                        "year": 1997,
                        "label": "Chandra Kumar",
                        "detail": "HC/SC exclusion clauses struck; JR = basic structure.",
                    },
                    {
                        "id": "e2006",
                        "year": 2006,
                        "label": "AT Amendment",
                        "detail": "Vice-Chairman post removed from CAT.",
                    },
                    {
                        "id": "e2021",
                        "year": 2021,
                        "label": "Tribunals Reforms Act",
                        "detail": "Book footnote: CAT tenure/age rules as cited.",
                    },
                ],
            },
            {
                "id": "tr-origin-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "Part XIV-A is a **two-Article Part** — same economy as Part IVA "
                    "(Fundamental Duties): one compact insertion, high exam yield."
                ),
            },
        ],
    },
    {
        "title": "Article 323A & AT Act 1985",
        "slug": "tr-323a-act",
        "sort_order": 2,
        "summary": (
            "Parliament alone may create administrative tribunals for recruitment and "
            "service disputes of public servants — AT Act 1985 enables CAT and SATs."
        ),
        "body": (
            "## Article 323A\n\n"
            "Empowers **Parliament** to provide for administrative tribunals adjudicating "
            "disputes on **recruitment and conditions of service** of persons appointed to "
            "public services of the Centre, the states, local bodies, public corporations, "
            "and other public authorities.\n\n"
            "In effect, 323A lets Parliament take service-matter adjudication out of "
            "**civil courts and High Courts** and place it before administrative tribunals.\n\n"
            "## Administrative Tribunals Act, 1985\n\n"
            "Passed under Article 323A. Authorises the Central government to establish:\n\n"
            "- one **Central Administrative Tribunal (CAT)**\n"
            "- **State Administrative Tribunals (SATs)**\n\n"
            "Purpose in the book: **speedy and inexpensive** justice for aggrieved public servants."
        ),
        "articles": [
            (
                "Art. 323A",
                "Parliament — administrative tribunals for public service matters.",
            ),
            (
                "AT Act 1985",
                "Statutory vehicle for CAT and SATs under Article 323A.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "tr-323a-flow",
                "type": "flowchart",
                "title": "Does 323A / AT Act apply?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What kind of dispute?",
                        "detail": "Match subject → forum.",
                        "options": [
                            {
                                "label": "Recruitment / service of public servants",
                                "next": "admin",
                            },
                            {
                                "label": "Tax, labour, elections, rent…",
                                "next": "other",
                            },
                            {
                                "label": "Ordinary civil / criminal",
                                "next": "courts",
                            },
                        ],
                    },
                    {
                        "id": "admin",
                        "label": "Art. 323A lane",
                        "detail": "Parliament → AT Act → CAT / SAT / JAT.",
                    },
                    {
                        "id": "other",
                        "label": "Art. 323B lane",
                        "detail": "See eight specified matters — Parliament or States.",
                        "slug": "tr-323b",
                    },
                    {
                        "id": "courts",
                        "label": "Ordinary courts",
                        "detail": "Not the Part XIV-A specialised track.",
                    },
                ],
            },
            {
                "id": "tr-323a-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Why CAT exists",
                "body": (
                    "Book line: AT Act opened a new chapter in **speedy and inexpensive** "
                    "justice for aggrieved public servants."
                ),
            },
            {
                "id": "tr-323a-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Only **Parliament** can establish tribunals under 323A — "
                    "states cannot invent their own 323A service tribunals outside the Act’s scheme."
                ),
            },
        ],
    },
    {
        "title": "Central Administrative Tribunal (CAT)",
        "slug": "tr-cat",
        "sort_order": 3,
        "summary": (
            "CAT (1985): 19 benches; original jurisdiction over AIS and Central service "
            "matters; exclusions; Chairman + Members; natural justice; ₹50 fee."
        ),
        "body": (
            "## Setup & benches\n\n"
            "CAT set up in **1985** — principal bench at **New Delhi**. "
            "**19 regular benches**: 17 at principal seats of High Courts plus "
            "**Jaipur** and **Lucknow**. Benches also hold **circuit sittings** "
            "(e.g. Port Blair, Shimla, Ranchi).\n\n"
            "## Jurisdiction (covered)\n\n"
            "Original jurisdiction over recruitment and all service matters of:\n\n"
            "- All-India Services\n"
            "- Central civil services\n"
            "- Civil posts under the Centre\n"
            "- **Civilian** employees of defence services\n\n"
            "## Excluded\n\n"
            "- Members of the **defence forces**\n"
            "- Officers and servants of the **Supreme Court**\n"
            "- Secretarial staff of **Parliament**\n\n"
            "## Composition & tenure\n\n"
            "Multi-member body: **Chairman + Members** (judicial and administrative streams). "
            "Vice-Chairman removed by the Administrative Tribunals (Amendment) Act, **2006**. "
            "Sanctioned strength (book): Chairman **1**, Members **69**.\n\n"
            "- Minimum age for appointment: **50**\n"
            "- Term: **4 years**, or until age **70** (Chairman) / **67** (Members), "
            "whichever is earlier — as per the **Tribunals Reforms Act, 2021** footnote\n"
            "- Appointed by the Central government on recommendations of a "
            "**search-cum-selection committee** chaired by the **CJI** or a "
            "CJI-nominated Supreme Court Judge\n\n"
            "## Procedure\n\n"
            "Not bound by CPC 1908 — guided by **principles of natural justice**. "
            "Nominal fee **₹50**. Applicant may appear in person or through a lawyer."
        ),
        "articles": [
            ("CAT", "Central Administrative Tribunal under AT Act 1985."),
            (
                "TRA 2021 footnote",
                "Tenure/age of Chairman and Members as cited in Laxmikanth.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "tr-cat-compare",
                "type": "comparison",
                "title": "CAT coverage vs exclusions",
                "columns": [
                    {
                        "id": "in",
                        "heading": "Covered",
                        "points": [
                            "All-India Services",
                            "Central civil services",
                            "Civil posts under the Centre",
                            "Civilian defence employees",
                        ],
                    },
                    {
                        "id": "out",
                        "heading": "Excluded",
                        "points": [
                            "Members of the defence forces",
                            "SC officers and servants",
                            "Parliament secretariat staff",
                        ],
                    },
                ],
            },
            {
                "id": "tr-cat-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "**Civilian** defence employees are covered; members of the "
                    "**defence forces** are not — do not collapse the two."
                ),
            },
            {
                "id": "tr-cat-note",
                "type": "callout",
                "tone": "note",
                "title": "Bench memory",
                "body": (
                    "19 regular benches — 17 at HC principal seats + Jaipur & Lucknow; "
                    "circuits include Port Blair, Shimla, Ranchi, and NE capitals."
                ),
            },
        ],
    },
    {
        "title": "State & Joint Administrative Tribunals",
        "slug": "tr-sat-jat",
        "sort_order": 4,
        "summary": (
            "Centre sets up SAT on state request; state-employee jurisdiction; "
            "HC CJ chairs search committee; JAT for two or more states."
        ),
        "body": (
            "## State Administrative Tribunals (SATs)\n\n"
            "The AT Act 1985 empowers the **Central government** to establish SATs "
            "on **specific request** of the concerned state governments.\n\n"
            "Like CAT, SATs exercise **original jurisdiction** over recruitment and "
            "all service matters of **state government employees**.\n\n"
            "Chairman and Members are appointed by the **Central government** on "
            "recommendations of a search-cum-selection committee **chaired by the "
            "Chief Justice of the High Court** of the concerned state.\n\n"
            "## Joint Administrative Tribunal (JAT)\n\n"
            "The Act allows a **JAT for two or more states**. A JAT exercises all "
            "jurisdiction and powers exercisable by the administrative tribunals for those states."
        ),
        "articles": [
            ("SAT", "State Administrative Tribunal — on state request."),
            ("JAT", "Joint Administrative Tribunal for two or more states."),
        ],
        "visual_blocks": [
            {
                "id": "tr-sat-flow",
                "type": "flowchart",
                "title": "How a SAT / JAT is born",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "State(s) want a service tribunal?",
                        "detail": "AT Act pathway under Article 323A.",
                        "options": [
                            {"label": "One state requests", "next": "sat"},
                            {"label": "Two or more states", "next": "jat"},
                        ],
                    },
                    {
                        "id": "sat",
                        "label": "Centre establishes SAT",
                        "detail": "Original jurisdiction — state government employees.",
                    },
                    {
                        "id": "jat",
                        "label": "Centre may set up JAT",
                        "detail": "Combined jurisdiction of those states’ tribunals.",
                    },
                ],
            },
            {
                "id": "tr-sat-compare",
                "type": "comparison",
                "title": "Who chairs the search-cum-selection committee?",
                "columns": [
                    {
                        "id": "cat",
                        "heading": "CAT",
                        "points": [
                            "CJI, or",
                            "SC Judge nominated by the CJI",
                        ],
                    },
                    {
                        "id": "sat",
                        "heading": "SAT",
                        "points": [
                            "Chief Justice of the State High Court",
                            "Concerned state’s HC",
                        ],
                    },
                ],
            },
            {
                "id": "tr-sat-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook",
                "body": (
                    "SAT is not automatic — **state request** + **Centre establishes**. "
                    "Appointment still by the Centre."
                ),
            },
        ],
    },
    {
        "title": "Article 323B — Other Matters",
        "slug": "tr-323b",
        "sort_order": 5,
        "summary": (
            "Eight specified matters; Parliament and state legislatures (competence); "
            "hierarchy of tribunals allowed; rent & tenancy via 75th Amendment."
        ),
        "body": (
            "## Who may establish\n\n"
            "Under **Article 323B**, **Parliament and state legislatures** may provide "
            "for tribunals on the listed matters **within their legislative competence**.\n\n"
            "## Eight matters\n\n"
            "1. Taxation\n"
            "2. Foreign exchange, import and export\n"
            "3. Industrial and labour\n"
            "4. Land reforms\n"
            "5. Ceiling on urban property\n"
            "6. Elections to Parliament and state legislatures\n"
            "7. Foodstuffs\n"
            "8. **Rent and tenancy rights** — added by the **75th Amendment Act, 1993**\n\n"
            "Unlike 323A, a **hierarchy** of tribunals may be created under 323B."
        ),
        "articles": [
            ("Art. 323B", "Tribunals for other specified matters."),
            ("75th Amendment", "1993 — rent and tenancy rights added to the list."),
        ],
        "visual_blocks": [
            {
                "id": "tr-323b-pillars",
                "type": "pillars",
                "title": "Eight 323B subjects",
                "items": [
                    {
                        "id": "tax",
                        "articles": "1",
                        "label": "Taxation",
                        "slug": "tr-323b",
                        "detail": "Tax disputes.",
                        "tone": "teal",
                    },
                    {
                        "id": "forex",
                        "articles": "2",
                        "label": "Forex / trade",
                        "slug": "tr-323b",
                        "detail": "Foreign exchange, import and export.",
                        "tone": "olive",
                    },
                    {
                        "id": "labour",
                        "articles": "3",
                        "label": "Industrial & labour",
                        "slug": "tr-323b",
                        "detail": "Industry and labour disputes.",
                        "tone": "gold",
                    },
                    {
                        "id": "land",
                        "articles": "4",
                        "label": "Land reforms",
                        "slug": "tr-323b",
                        "detail": "Agrarian reform matters.",
                        "tone": "orange",
                    },
                    {
                        "id": "urban",
                        "articles": "5",
                        "label": "Urban ceiling",
                        "slug": "tr-323b",
                        "detail": "Ceiling on urban property.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "elections",
                        "articles": "6",
                        "label": "Elections",
                        "slug": "tr-323b",
                        "detail": "Parliament & state legislature elections.",
                        "tone": "maroon",
                    },
                    {
                        "id": "food",
                        "articles": "7",
                        "label": "Foodstuffs",
                        "slug": "tr-323b",
                        "detail": "Foodstuffs-related disputes.",
                        "tone": "teal",
                    },
                    {
                        "id": "rent",
                        "articles": "8 · 75th",
                        "label": "Rent & tenancy",
                        "slug": "tr-323b",
                        "detail": "Added by 75th Amendment, 1993.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "tr-323b-memory",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid — T FILE CUR",
                "body": (
                    "**T**ax · **F**orex/trade · **I**ndustrial-labour · **L**and reforms · "
                    "**E**lections · **C**eiling (urban) · **U**… foodst**U**ffs · **R**ent/tenancy. "
                    "Or simply: Tax, Trade, Labour, Land, Ceiling, Elections, Food, Rent."
                ),
            },
            {
                "id": "tr-323b-note",
                "type": "callout",
                "tone": "note",
                "title": "Hierarchy allowed",
                "body": (
                    "323B can stack tribunals in a hierarchy; 323A contemplates one Centre "
                    "tribunal and one per state (or joint) — **no hierarchy**."
                ),
            },
        ],
    },
    {
        "title": "323A vs 323B — Three Differences",
        "slug": "tr-323a-vs-323b",
        "sort_order": 6,
        "summary": (
            "Book’s three-point contrast: subject-matter, who establishes, and hierarchy."
        ),
        "body": (
            "## The Prelims trio\n\n"
            "Laxmikanth lists **three** differences between Articles 323A and 323B:\n\n"
            "1. **Subject** — 323A: public service matters only; 323B: the specified other matters.\n"
            "2. **Who establishes** — 323A: **Parliament only**; 323B: Parliament **and** "
            "state legislatures (within competence).\n"
            "3. **Structure** — 323A: one Centre + one per state/group of states — "
            "**no hierarchy**; 323B: a **hierarchy** of tribunals may be created.\n\n"
            "Master this table — it is the highest-yield comparison in the chapter."
        ),
        "articles": [
            ("Art. 323A", "Services · Parliament only · no hierarchy."),
            ("Art. 323B", "Other matters · Parliament + States · hierarchy OK."),
        ],
        "visual_blocks": [
            {
                "id": "tr-vs-compare",
                "type": "comparison",
                "title": "Article 323A vs Article 323B",
                "columns": [
                    {
                        "id": "a",
                        "heading": "Article 323A",
                        "points": [
                            "Public service matters only",
                            "Established only by Parliament",
                            "One Centre + one per state/group",
                            "No hierarchy of tribunals",
                        ],
                    },
                    {
                        "id": "b",
                        "heading": "Article 323B",
                        "points": [
                            "Specified other matters (eight)",
                            "Parliament + state legislatures",
                            "Within legislative competence",
                            "Hierarchy of tribunals permitted",
                        ],
                    },
                ],
            },
            {
                "id": "tr-vs-tip",
                "type": "callout",
                "tone": "tip",
                "title": "30-second script",
                "body": (
                    "Services / Parliament / flat vs Other-eight / both Houses / stacked — "
                    "that is the whole 323A–323B game."
                ),
            },
            {
                "id": "tr-vs-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Do not say states can create 323A tribunals, or that 323A allows a "
                    "multi-tier tribunal hierarchy."
                ),
            },
        ],
    },
    {
        "title": "Chandra Kumar & Appeal Hierarchy",
        "slug": "tr-chandra-kumar",
        "sort_order": 7,
        "summary": (
            "L. Chandra Kumar (1997): exclusion of HC/SC jurisdiction unconstitutional; "
            "judicial review is basic structure; CAT appeals go to HC Division Bench first."
        ),
        "body": (
            "## Old position\n\n"
            "Originally, appeals against CAT orders could go **only to the Supreme Court**, "
            "not to the High Courts.\n\n"
            "## L. Chandra Kumar v. Union of India (1997)\n\n"
            "The Supreme Court held that provisions excluding the jurisdiction of the "
            "High Courts and the Supreme Court under these Articles were "
            "**unconstitutional**.\n\n"
            "- Clause **2(d) of Article 323A** and Clause **3(d) of Article 323B** "
            "struck insofar as they ousted HC/SC jurisdiction\n"
            "- **Judicial review** is part of the **basic structure** of the Constitution\n"
            "- Appeals against CAT orders lie before the **division bench of the "
            "concerned High Court**\n"
            "- An aggrieved public servant **cannot** approach the Supreme Court "
            "directly against a CAT order without first going to the High Court\n\n"
            "Consequently, judicial remedies are available against orders of these tribunals."
        ),
        "articles": [
            (
                "L. Chandra Kumar (1997)",
                "HC/SC exclusion void; JR = basic structure; CAT → HC DB.",
            ),
            ("Art. 323A(2)(d)", "Exclusion clause held unconstitutional."),
            ("Art. 323B(3)(d)", "Exclusion clause held unconstitutional."),
        ],
        "visual_blocks": [
            {
                "id": "tr-ck-flow",
                "type": "flowchart",
                "title": "Appeal path after Chandra Kumar",
                "root": "cat",
                "steps": [
                    {
                        "id": "cat",
                        "label": "CAT / tribunal order",
                        "detail": "Aggrieved party wants to challenge.",
                        "options": [
                            {"label": "Correct path", "next": "hc"},
                            {"label": "Direct to SC?", "next": "wrong"},
                        ],
                    },
                    {
                        "id": "hc",
                        "label": "HC Division Bench",
                        "detail": "Concerned High Court — mandatory first stop.",
                        "options": [
                            {"label": "Further appeal", "next": "sc"},
                        ],
                    },
                    {
                        "id": "sc",
                        "label": "Supreme Court",
                        "detail": "After the High Court stage.",
                    },
                    {
                        "id": "wrong",
                        "label": "Not available",
                        "detail": "Direct SC jump barred after Chandra Kumar.",
                    },
                ],
            },
            {
                "id": "tr-ck-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Tribunals are **not** beyond judicial review. Chandra Kumar restored "
                    "HC/SC supervision — judicial review is basic structure."
                ),
            },
            {
                "id": "tr-ck-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "Specialised adjudication for speed, but constitutional courts keep "
                    "the last word — CAT → HC Division Bench → SC."
                ),
            },
        ],
    },
    {
        "title": "Prelims, PYQ Themes & Mains VA",
        "slug": "tr-exam-kit",
        "sort_order": 8,
        "summary": (
            "Book-grounded prelims facts, PYQ themes, mains value-adds, and a "
            "30-second revision script."
        ),
        "body": (
            "## Prelims facts\n\n"
            "- Part **XIV-A** added by **42nd** Amendment (1976) — only 323A & 323B.\n"
            "- **323A**: services · Parliament only · no hierarchy.\n"
            "- **323B**: eight matters · Parliament + States · hierarchy OK.\n"
            "- **75th** (1993): rent & tenancy rights into 323B list.\n"
            "- CAT: **19** benches; Jaipur & Lucknow extras; fee **₹50**; natural justice, not CPC.\n"
            "- CAT excludes defence **forces**, SC staff, Parliament secretariat.\n"
            "- No Vice-Chairman after **2006** amendment.\n"
            "- Age ≥50; term 4 years or 70/67 — **TRA 2021** footnote.\n"
            "- SAT only on **state request**; search committee chaired by **State HC CJ**.\n"
            "- Chandra Kumar (1997): CAT → **HC Division Bench** → SC.\n\n"
            "## PYQ themes\n\n"
            "- 323A vs 323B three differences\n"
            "- Who can establish which tribunal\n"
            "- CAT coverage / exclusions\n"
            "- Effect of Chandra Kumar on HC jurisdiction\n"
            "- 42nd / 75th amendment hooks\n\n"
            "## Mains value-adds\n\n"
            "- Specialised tribunals for speedy/inexpensive justice vs independence of judiciary.\n"
            "- Judicial review as basic structure — limiting ouster clauses.\n"
            "- CAT→HC→SC as the constitutional balance after Chandra Kumar.\n\n"
            "### 30-second script\n"
            "XIV-A / 42nd → 323A services (Parliament, flat) vs 323B eight (both, stacked) → "
            "CAT 19 benches + exclusions → SAT on request → Chandra Kumar: HC DB first."
        ),
        "articles": [
            (
                "Prelims pack",
                "XIV-A; 323A/323B trio; CAT exclusions; Chandra Kumar path; 75th rent.",
            ),
            ("Table 36.3", "Arts 323A and 323B at a glance."),
        ],
        "visual_blocks": [
            {
                "id": "tr-exam-pillars",
                "type": "pillars",
                "title": "Three exam lanes",
                "items": [
                    {
                        "id": "prelims",
                        "articles": "Facts",
                        "label": "Prelims facts",
                        "slug": "tr-exam-kit",
                        "detail": "XIV-A, trio, exclusions, ₹50, TRA ages, 75th.",
                        "tone": "teal",
                    },
                    {
                        "id": "mains",
                        "articles": "VA",
                        "label": "Mains value-adds",
                        "slug": "tr-exam-kit",
                        "detail": "Speed vs JR; basic structure; CAT→HC→SC balance.",
                        "tone": "gold",
                    },
                    {
                        "id": "traps",
                        "articles": "Avoid",
                        "label": "Traps",
                        "slug": "tr-exam-kit",
                        "detail": "States≠323A; forces≠civilians; no direct SC from CAT.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "tr-exam-heatmap",
                "type": "pyq_heatmap",
                "title": "PYQ focus map",
                "items": [
                    {"concept_slug": "tr-323a-vs-323b", "label": "323A vs 323B"},
                    {"concept_slug": "tr-cat", "label": "CAT"},
                    {"concept_slug": "tr-chandra-kumar", "label": "Chandra Kumar"},
                    {"concept_slug": "tr-323b", "label": "323B matters"},
                    {"concept_slug": "tr-sat-jat", "label": "SAT / JAT"},
                ],
            },
            {
                "id": "tr-exam-script",
                "type": "callout",
                "tone": "tip",
                "title": "30-second revision",
                "body": (
                    "XIV-A · 323A services/Parliament/flat · 323B eight/both/stacked · "
                    "CAT 19 + exclusions · SAT on request · Chandra Kumar: HC DB → SC."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "tr-origin"),
    (HUB_SLUG, "parent", "tr-323a-act"),
    (HUB_SLUG, "parent", "tr-cat"),
    (HUB_SLUG, "parent", "tr-sat-jat"),
    (HUB_SLUG, "parent", "tr-323b"),
    (HUB_SLUG, "parent", "tr-323a-vs-323b"),
    (HUB_SLUG, "parent", "tr-chandra-kumar"),
    (HUB_SLUG, "parent", "tr-exam-kit"),
    ("tr-origin", "related", "tr-323a-act"),
    ("tr-origin", "related", "tr-323b"),
    ("tr-323a-act", "related", "tr-323b"),
    ("tr-323a-act", "related", "tr-cat"),
    ("tr-323a-act", "related", "tr-sat-jat"),
    ("tr-cat", "related", "tr-sat-jat"),
    ("tr-cat", "related", "tr-chandra-kumar"),
    ("tr-323a-vs-323b", "related", "tr-323a-act"),
    ("tr-323a-vs-323b", "related", "tr-323b"),
    ("tr-chandra-kumar", "related", "tr-exam-kit"),
    ("tr-323a-vs-323b", "related", "tr-exam-kit"),
    ("tr-exam-kit", "related", "tr-cat"),
]

SAMPLE_PYQS = [
    (
        2015,
        "With reference to Articles 323A and 323B, which statement is correct?",
        "323A covers public service matters and only Parliament may establish such tribunals; "
        "323B covers specified other matters and both Parliament and state legislatures may act "
        "within competence; hierarchy is allowed only under 323B.",
        ["tr-323a-vs-323b", "tr-exam-kit"],
    ),
    (
        2017,
        "Which of the following are excluded from the jurisdiction of the Central Administrative Tribunal?",
        "Members of the defence forces; officers and servants of the Supreme Court; "
        "and secretarial staff of Parliament are not covered by CAT.",
        ["tr-cat", "tr-exam-kit"],
    ),
    (
        2019,
        "After L. Chandra Kumar (1997), an appeal against an order of the CAT lies first to:",
        "The division bench of the concerned High Court — direct approach to the Supreme Court "
        "without first going to the High Court is not available.",
        ["tr-chandra-kumar", "tr-cat"],
    ),
    (
        2021,
        "State Administrative Tribunals under the Administrative Tribunals Act, 1985 are established:",
        "By the Central government on the specific request of the concerned state government(s).",
        ["tr-sat-jat", "tr-323a-act"],
    ),
    (
        2013,
        "Rent and tenancy rights were included among matters for tribunals under Article 323B by:",
        "The 75th Constitutional Amendment Act, 1993.",
        ["tr-323b", "tr-origin"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "L. Chandra Kumar v. Union of India",
        "slug": "l-chandra-kumar",
        "parties": "L. Chandra Kumar v. Union of India",
        "year": 1997,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Challenge to provisions under Articles 323A and 323B that excluded the "
            "jurisdiction of the High Courts and the Supreme Court over tribunal orders."
        ),
        "holding": (
            "Clause 2(d) of Article 323A and Clause 3(d) of Article 323B, insofar as they "
            "excluded HC/SC jurisdiction, are unconstitutional. Judicial review is part of "
            "the basic structure. Appeals against CAT orders lie before the division bench "
            "of the concerned High Court before the Supreme Court."
        ),
        "concept_slugs": ["tr-chandra-kumar", "tr-cat", HUB_SLUG, "tr-exam-kit"],
    },
]

AMENDMENTS = [
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Inserted Part XIV-A (Tribunals) consisting of Articles 323A and 323B."
        ),
        "effect": (
            "Created the constitutional footing for administrative tribunals and "
            "tribunals for other specified matters."
        ),
        "concept_slugs": [HUB_SLUG, "tr-origin", "tr-323a-act", "tr-323b"],
    },
    {
        "number": 75,
        "year": 1993,
        "title": "Seventy-fifth Amendment",
        "summary": (
            "Added rent and tenancy rights to the list of matters under Article 323B."
        ),
        "effect": "Expanded 323B’s eight-matter catalogue to include rent and tenancy.",
        "concept_slugs": ["tr-323b", "tr-origin", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed Tribunals chapter (Laxmikanth Ch.36)."

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
                "title": "Tribunals",
                "sort_order": 7,
                "book_ref": "Laxmikanth 8th Ed, Ch. 36",
                "summary": (
                    "Visual revision of Ch.36 — Part XIV-A, Arts 323A/323B, CAT/SAT/JAT, "
                    "and Chandra Kumar appeal hierarchy."
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
                "title": "Tribunals",
                "summary": (
                    "Part XIV-A specialised lanes for service and other disputes — "
                    "Arts 323A & 323B, with judicial review preserved by Chandra Kumar."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **specialised lane** mental model, then "
                    "**Origin** → **323A / AT Act** → **CAT** → **SAT/JAT** → **323B** → "
                    "**323A vs 323B** → **Chandra Kumar**. Finish with the **Exam kit**. "
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
            ref="Laxmikanth Ch. 36",
            excerpt=(
                "Tribunals — Part XIV-A, Arts 323A/323B, CAT/SAT/JAT, Chandra Kumar."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 323A–323B",
            excerpt="Administrative tribunals and tribunals for other matters.",
            sort_order=1,
        )

        tr_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=tr_slugs) | Q(target__slug__in=tr_slugs),
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
                existing = list(pyq.concepts.all())
                pyq.concepts.set({*existing, *concepts})

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

        self.stdout.write(
            self.style.SUCCESS(
                f"Tribunals chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
