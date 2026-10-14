"""Seed Laxmikanth Ch.24 Parliamentary Committees (visual revision)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "parliamentary-committees"
CHAPTER_SLUG = "parliamentary-committees"

ENTRY_PILLARS = [
    {
        "id": "meaning",
        "articles": "4 tests",
        "label": "Meaning & four tests",
        "slug": "pc-meaning",
        "detail": "Why committees exist; Rules of Houses; four conditions that define a PC.",
        "tone": "teal",
    },
    {
        "id": "classify",
        "articles": "Map",
        "label": "Classification",
        "slug": "pc-classification",
        "detail": "Standing vs Ad hoc; six standing buckets; inquiry vs Select/Joint.",
        "tone": "olive",
    },
    {
        "id": "trio",
        "articles": "Table",
        "label": "Financial trio",
        "slug": "pc-financial-trio",
        "detail": "PAC · Estimates · PUC — membership, chair, CAG, focus at a glance.",
        "tone": "gold",
    },
    {
        "id": "pac",
        "articles": "CAG",
        "label": "Public Accounts",
        "slug": "pc-pac",
        "detail": "Post-mortem of accounts; Opposition chair; CAG as guide.",
        "tone": "orange",
    },
    {
        "id": "est",
        "articles": "Economy",
        "label": "Estimates",
        "slug": "pc-estimates",
        "detail": "Continuous economy committee — 30 LS only; no CAG.",
        "tone": "terracotta",
    },
    {
        "id": "puc",
        "articles": "PSUs",
        "label": "Public Undertakings",
        "slug": "pc-puc",
        "detail": "Krishna Menon 1964; PSU reports + commercial prudence.",
        "tone": "maroon",
    },
    {
        "id": "drsc",
        "articles": "24 · 31",
        "label": "DRSCs",
        "slug": "pc-drsc",
        "detail": "1993→2004; DFGs before vote; bills & reports; advisory.",
        "tone": "teal",
    },
    {
        "id": "other",
        "articles": "4 buckets",
        "label": "Other standing",
        "slug": "pc-other-standing",
        "detail": "Inquire · Scrutinise · Business · House-keeping — numbers & traps.",
        "tone": "olive",
    },
    {
        "id": "adhoc",
        "articles": "Bills",
        "label": "Ad hoc",
        "slug": "pc-ad-hoc",
        "detail": "Inquiry committees + Select/Joint Committees on Bills.",
        "tone": "gold",
    },
    {
        "id": "consult",
        "articles": "Trap",
        "label": "Consultative ≠ PC",
        "slug": "pc-consultative",
        "detail": "MoPA; Minister chairs; fail the four tests.",
        "tone": "orange",
    },
    {
        "id": "revise",
        "articles": "Exam",
        "label": "PYQ & quick tables",
        "slug": "pc-revision-tables",
        "detail": "Prelims facts, mains VA, memory palace, PYQ themes.",
        "tone": "terracotta",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pc-workbench-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Parliament’s specialised workbench",
        "topic_label": "Parliamentary Committees",
        "subject_label": "Rules of the Houses · Ch. 24",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating Consultative Committees as parliamentary committees",
            "Confusing PAC (CAG/accounts) with Estimates (economy)",
            "Assuming all financial committees have Rajya Sabha members",
            "Thinking committee recommendations bind the ministries",
        ],
        "insight": (
            "The House is too large for deep scrutiny — committees supply time, "
            "expertise, and continuous oversight under the Rules of the two Houses."
        ),
    },
    {
        "id": "pc-entry-pillars",
        "type": "pillars",
        "title": "Eleven revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "pc-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "4 tests → Standing vs Ad hoc → Financial trio numbers → DRSC 24 / 31 "
            "(8 RS + 16 LS) → Consultative ≠ parliamentary → recommendations advisory. "
            "Scan Meaning → Classification → Trio → PAC/Estimates/PUC → DRSCs → Exam box."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Meaning & Four Tests",
        "slug": "pc-meaning",
        "sort_order": 1,
        "summary": (
            "Parliament is too unwieldy for detailed scrutiny — committees assist. "
            "Four Rules-of-House conditions define a parliamentary committee."
        ),
        "body": (
            "## Why committees?\n\n"
            "- Functions of Parliament are **varied, complex, and voluminous**.\n"
            "- The House lacks adequate **time** and **expertise** for every bill and account.\n"
            "- Committees enable detailed scrutiny and continuous oversight.\n\n"
            "## Constitutional footing\n\n"
            "- Constitution **mentions** committees at places but does **not** fix composition, "
            "tenure, or functions.\n"
            "- Those details live in the **Rules of Procedure** of Lok Sabha and Rajya Sabha "
            "(and Speakers’/Chairman’s directions).\n\n"
            "## Four tests (all must hold)\n\n"
            "A parliamentary committee is one that:\n"
            "1. Is **appointed or elected** by the House **or nominated** by the Speaker/Chairman\n"
            "2. Works under the **direction** of the Speaker/Chairman\n"
            "3. Presents its **report** to the House or to the Speaker/Chairman\n"
            "4. Has a **secretariat** provided by the Lok Sabha / Rajya Sabha\n\n"
            "### Memory\n"
            "**A-D-R-S** — Appointed · Direction · Report · Secretariat."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 24",
                "Meaning — four conditions from Rules of the Houses.",
            ),
            (
                "Rules of Houses",
                "Composition, tenure, and functions of parliamentary committees.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-four-tests-flow",
                "type": "flowchart",
                "title": "Is it a parliamentary committee?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Body of MPs?",
                        "detail": "Start here — not every MP group is a PC.",
                        "options": [
                            {"label": "Appointed/elected/nominated by House or Speaker/Chairman?", "next": "dir"},
                            {"label": "No / informal only", "next": "fail"},
                        ],
                    },
                    {
                        "id": "dir",
                        "label": "Works under Speaker/Chairman direction?",
                        "detail": "Second test.",
                        "options": [
                            {"label": "Yes", "next": "report"},
                            {"label": "No", "next": "fail"},
                        ],
                    },
                    {
                        "id": "report",
                        "label": "Reports to House or Speaker/Chairman?",
                        "detail": "Third test.",
                        "options": [
                            {"label": "Yes", "next": "sec"},
                            {"label": "No", "next": "fail"},
                        ],
                    },
                    {
                        "id": "sec",
                        "label": "House secretariat provided?",
                        "detail": "Fourth test — LS/RS secretariat.",
                        "options": [
                            {"label": "Yes — all four pass", "next": "pass"},
                            {"label": "No", "next": "fail"},
                        ],
                    },
                    {
                        "id": "pass",
                        "label": "Parliamentary committee",
                        "detail": "Standing or Ad hoc under Rules of the Houses.",
                    },
                    {
                        "id": "fail",
                        "label": "Not a parliamentary committee",
                        "detail": "Classic trap: Consultative Committees fail these tests.",
                    },
                ],
            },
            {
                "id": "pc-meaning-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Consultative committees have MPs but are **not** parliamentary committees — "
                    "they fail the four tests. Open the Consultative cluster."
                ),
            },
        ],
    },
    {
        "title": "Classification Map",
        "slug": "pc-classification",
        "sort_order": 2,
        "summary": (
            "Standing = permanent/continuous; Ad hoc = task then dissolve. "
            "Six standing function buckets; Ad hoc = Inquiry + Advisory (Select/Joint)."
        ),
        "body": (
            "## Two broad kinds\n\n"
            "| Kind | Nature |\n"
            "|------|--------|\n"
            "| **Standing** | Permanent — constituted every year or periodically; continuous work |\n"
            "| **Ad hoc** | Temporary — cease when the assigned task is done |\n\n"
            "## Standing — six buckets (by function)\n\n"
            "1. **Financial** — PAC, Estimates, PUC\n"
            "2. **Department-Related Standing Committees (DRSCs)** — 24\n"
            "3. **Committees to Inquire** — Petitions, Privileges, Ethics\n"
            "4. **Committees to Scrutinise & Control** — Assurances, Subordinate Legislation, Papers Laid, SC/ST, Women, Offices of Profit\n"
            "5. **Day-to-day Business** — BAC, Private Members’ Bills, Rules, Absence\n"
            "6. **House-keeping / Service** — General Purposes, House, Library, Salaries & Allowances\n\n"
            "## Ad hoc — two types\n\n"
            "- **Inquiry** — specific subjects (e.g. Railway Convention, MPLADS)\n"
            "- **Advisory** — Select / Joint Committees on **Bills**\n\n"
            "### Memory\n"
            "**Fin · Dept · Inquire · Scrutinise · Business · House** (FID-SBH)."
        ),
        "articles": [
            (
                "Classification",
                "Standing (6 function groups) vs Ad hoc (Inquiry + Select/Joint on Bills).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-class-tree",
                "type": "tree",
                "title": "Committee map",
                "root": {
                    "id": "pcs",
                    "label": "Parliamentary Committees",
                    "children": [
                        {
                            "id": "standing",
                            "label": "Standing",
                            "detail": "Permanent / continuous",
                            "slug": "pc-classification",
                            "children": [
                                {
                                    "id": "fin",
                                    "label": "Financial trio",
                                    "slug": "pc-financial-trio",
                                    "detail": "PAC · Estimates · PUC",
                                },
                                {
                                    "id": "drsc",
                                    "label": "DRSCs (24)",
                                    "slug": "pc-drsc",
                                    "detail": "Ministry coverage",
                                },
                                {
                                    "id": "other",
                                    "label": "Inquire · Scrutinise · Business · House",
                                    "slug": "pc-other-standing",
                                },
                            ],
                        },
                        {
                            "id": "adhoc",
                            "label": "Ad hoc",
                            "detail": "Task then dissolve",
                            "slug": "pc-ad-hoc",
                            "children": [
                                {"id": "inq", "label": "Inquiry committees"},
                                {"id": "sel", "label": "Select / Joint on Bills"},
                            ],
                        },
                    ],
                },
            },
            {
                "id": "pc-class-memory",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "Standing spine: **Fin · Dept · Inquire · Scrutinise · Business · House**. "
                    "Ad hoc: Inquiry subjects OR Bill committees (Select/Joint)."
                ),
            },
        ],
    },
    {
        "title": "Financial Trio Compared",
        "slug": "pc-financial-trio",
        "sort_order": 3,
        "summary": (
            "PAC, Estimates, and PUC at a glance — membership, chair, CAG link, and focus."
        ),
        "body": (
            "## Master comparison\n\n"
            "| | **PAC** | **Estimates** | **PUC** |\n"
            "|--|---------|---------------|--------|\n"
            "| Origin | 1921 (GoI Act 1919) | 1950 (John Mathai); roots 1921 | 1964 (Krishna Menon) |\n"
            "| Strength | **22** (15 LS + 7 RS) | **30 LS only** (no RS) | **22** (15 LS + 7 RS) |\n"
            "| Tenure | 1 year | 1 year | 1 year |\n"
            "| Election | PR + STV | PR + STV | PR + STV |\n"
            "| Minister | Cannot be member | Cannot | Cannot |\n"
            "| Chair | Speaker; **Opp since 1967** | Speaker; usually ruling | Speaker |\n"
            "| Focus | CAG audit / accounts | Budget estimates → economies | PSU reports + CAG on PSUs |\n"
            "| CAG assist | Yes — guide, friend, philosopher | **No** | Uses CAG reports on PSUs |\n\n"
            "## Shared limits\n\n"
            "- Recommendations are **advisory**, not binding.\n"
            "- Work is largely **post-mortem**.\n"
            "- No day-to-day administration intervention.\n"
            "- Open individual clusters for functions & traps."
        ),
        "articles": [
            (
                "Financial Committees",
                "PAC · Estimates · PUC — the three standing financial committees.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-trio-compare",
                "type": "comparison",
                "title": "Three financial committees",
                "columns": [
                    {
                        "id": "pac",
                        "heading": "PAC",
                        "points": [
                            "22 (15 LS + 7 RS)",
                            "Opposition chair (since 1967)",
                            "CAG audit & accounts",
                            "CAG assists the committee",
                        ],
                    },
                    {
                        "id": "est",
                        "heading": "Estimates",
                        "points": [
                            "30 — Lok Sabha only",
                            "Usually ruling-party chair",
                            "Continuous economy committee",
                            "No CAG assistance",
                        ],
                    },
                    {
                        "id": "puc",
                        "heading": "PUC",
                        "points": [
                            "22 (15 LS + 7 RS)",
                            "Speaker appoints chair",
                            "PSU reports & accounts",
                            "CAG reports on PSUs",
                        ],
                    },
                ],
            },
            {
                "id": "pc-trio-limit",
                "type": "callout",
                "tone": "note",
                "title": "Shared limit",
                "body": (
                    "All three: advisory reports · post-mortem character · no day-to-day admin. "
                    "Do not treat them as executive bodies."
                ),
            },
        ],
    },
    {
        "title": "Public Accounts Committee",
        "slug": "pc-pac",
        "sort_order": 4,
        "summary": (
            "Examines CAG audit reports and Union accounts — post-mortem financial control; "
            "Opposition chair by convention since 1967."
        ),
        "body": (
            "## Snapshot\n\n"
            "- Oldest lineage: **1921** under GoI Act 1919.\n"
            "- **22** members (15 LS + 7 RS); elected yearly by PR + STV; **1-year** term.\n"
            "- Minister **cannot** be a member.\n"
            "- Chair appointed by Speaker; since **1967**, convention of **Opposition** chair.\n\n"
            "## Core functions\n\n"
            "1. Examine **appropriation** and **finance** accounts (and other accounts laid in LS).\n"
            "2. On CAG appropriation audit — check legal availability, authority, and re-appropriation rules.\n"
            "3. Accounts of state corporations / trading / manufacturing (except those with PUC).\n"
            "4. Autonomous / semi-autonomous bodies audited by CAG.\n"
            "5. CAG reports on receipts / stores & stocks.\n"
            "6. Excess expenditure over grants.\n\n"
            "CAG = **guide, friend and philosopher** of the PAC.\n\n"
            "## Limits\n\n"
            "- Not concerned with broader **policy** questions.\n"
            "- **Post-mortem** of spent money.\n"
            "- Cannot intervene in day-to-day administration.\n"
            "- Recommendations advisory; cannot disallow expenditure; not an executive body.\n\n"
            "### Memory\n"
            "**PAC = Past Accounts + CAG + Opposition Chair**."
        ),
        "articles": [
            (
                "PAC",
                "22 members; CAG audit reports; Opposition chair convention since 1967.",
            ),
            (
                "CAG link",
                "CAG acts as guide, friend and philosopher of the PAC.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-pac-pillars",
                "type": "pillars",
                "title": "PAC revision spine",
                "items": [
                    {
                        "id": "compose",
                        "articles": "22",
                        "label": "Composition",
                        "slug": "pc-pac",
                        "detail": "15 LS + 7 RS · PR+STV · 1 year · no minister.",
                        "tone": "teal",
                    },
                    {
                        "id": "chair",
                        "articles": "1967",
                        "label": "Opposition chair",
                        "slug": "pc-pac",
                        "detail": "Speaker appoints; Opp convention since 1967.",
                        "tone": "gold",
                    },
                    {
                        "id": "cag",
                        "articles": "Audit",
                        "label": "CAG partnership",
                        "slug": "pc-pac",
                        "detail": "Appropriation, finance, PU reports — CAG guides PAC.",
                        "tone": "orange",
                    },
                    {
                        "id": "limit",
                        "articles": "Limits",
                        "label": "What it cannot do",
                        "slug": "pc-pac",
                        "detail": "No broad policy · post-mortem · advisory · no disallowance.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pc-pac-tip",
                "type": "callout",
                "tone": "tip",
                "title": "One-liner",
                "body": (
                    "Ashok Chanda: PAC traditions conform to the highest traditions of "
                    "parliamentary democracy — but still advisory and post-mortem."
                ),
            },
        ],
    },
    {
        "title": "Estimates Committee",
        "slug": "pc-estimates",
        "sort_order": 5,
        "summary": (
            "Continuous economy committee — 30 Lok Sabha members only; suggests economies "
            "and even alternative policies within estimate limits."
        ),
        "body": (
            "## Snapshot\n\n"
            "- Post-independence form **1950** (John Mathai); roots in 1921 standing financial committee.\n"
            "- Originally 25; since **1956** → **30**, **all from Lok Sabha** (RS has **no** representation).\n"
            "- Elected yearly by PR + STV; 1-year term; minister cannot be member.\n"
            "- Chair: Speaker; generally from the **ruling** party.\n\n"
            "## Functions\n\n"
            "1. Report economies, organisation, efficiency, administrative reform consistent with policy in the estimates.\n"
            "2. Suggest **alternative policies** for efficiency and economy.\n"
            "3. Examine whether money is well laid out within the policy implied in the estimates.\n"
            "4. Suggest the **form** in which estimates are presented.\n\n"
            "Does **not** cover PSUs allotted to PUC. Need not finish all estimates in a year; "
            "Demands may be voted even without its report.\n\n"
            "## Limits\n\n"
            "- Examines estimates **after** they are voted — not before.\n"
            "- Cannot question Parliament’s policy.\n"
            "- Advisory; covers selected ministries by rotation.\n"
            "- **Lacks CAG assistance** (unlike PAC).\n"
            "- Post-mortem character.\n\n"
            "### Memory\n"
            "**Estimates = Economy + LS-only 30 + No CAG**."
        ),
        "articles": [
            (
                "Estimates Committee",
                "30 LS only; continuous economy committee; no CAG assistance.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-est-compare",
                "type": "comparison",
                "title": "Estimates vs PAC (quick)",
                "columns": [
                    {
                        "id": "est",
                        "heading": "Estimates",
                        "points": [
                            "30 — Lok Sabha only",
                            "Economies in budget estimates",
                            "May suggest alternative policies",
                            "No CAG as guide",
                            "After estimates are voted",
                        ],
                    },
                    {
                        "id": "pac",
                        "heading": "PAC",
                        "points": [
                            "22 — both Houses",
                            "Accounts already spent",
                            "Legal + propriety check via CAG",
                            "CAG guides the committee",
                            "Appropriation / finance focus",
                        ],
                    },
                ],
            },
            {
                "id": "pc-est-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Rajya Sabha has **no** representation on the Estimates Committee. "
                    "Do not mix this with PAC/PUC (both have RS members)."
                ),
            },
        ],
    },
    {
        "title": "Committee on Public Undertakings",
        "slug": "pc-puc",
        "sort_order": 6,
        "summary": (
            "Created 1964 on Krishna Menon recommendation — scrutinises PSUs’ reports, "
            "accounts, and commercial management; 22 members."
        ),
        "body": (
            "## Snapshot\n\n"
            "- Created **1964** (Krishna Menon Committee). Originally 15; since **1974** → **22** "
            "(15 LS + 7 RS).\n"
            "- Elected yearly by PR + STV; 1-year term; minister cannot be member.\n"
            "- Chair appointed by the Speaker.\n\n"
            "## Functions\n\n"
            "1. Examine reports and accounts of public undertakings.\n"
            "2. Examine **CAG reports** on public undertakings.\n"
            "3. Check management against sound business principles and prudent commercial practices "
            "(autonomy + efficiency).\n"
            "4. Other PAC/Estimates-type functions on PSUs as allotted by the Speaker.\n\n"
            "## Must **not** examine\n\n"
            "- Major **government policy** (as distinct from commercial functions)\n"
            "- **Day-to-day** administration\n"
            "- Matters for which special-statute machinery already exists for that PSU\n\n"
            "## Limits\n\n"
            "- Only ~**10–12** undertakings a year.\n"
            "- Post-mortem; members are not technical experts.\n"
            "- Recommendations advisory.\n\n"
            "### Memory\n"
            "**PUC = PSUs + Krishna Menon 1964**."
        ),
        "articles": [
            (
                "PUC",
                "1964 Krishna Menon; 22 members; PSU reports and commercial prudence.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-puc-compare",
                "type": "comparison",
                "title": "What PUC does vs excludes",
                "columns": [
                    {
                        "id": "does",
                        "heading": "Examines",
                        "points": [
                            "PSU reports and accounts",
                            "CAG reports on PSUs",
                            "Business principles & commercial practices",
                            "Speaker-allotted PAC/Estimates-type PSU work",
                        ],
                    },
                    {
                        "id": "not",
                        "heading": "Does not examine",
                        "points": [
                            "Major government policy (non-commercial)",
                            "Day-to-day administration",
                            "Special-statute PSU machinery issues",
                            "More than ~10–12 PSUs in a year (capacity)",
                        ],
                    },
                ],
            },
            {
                "id": "pc-puc-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook",
                "body": (
                    "Need for a separate PSU committee was visualised via the "
                    "**Krishna Menon Committee** — a frequent match-the-origin item."
                ),
            },
        ],
    },
    {
        "title": "Department-Related Standing Committees",
        "slug": "pc-drsc",
        "sort_order": 7,
        "summary": (
            "24 DRSCs (31 members each) deepen executive accountability — DFGs before vote, "
            "bills, annual reports, and long-term policy documents."
        ),
        "body": (
            "## Evolution\n\n"
            "- **1989**: three pilot DRSCs (Agriculture; S&T; Environment & Forests).\n"
            "- **1993**: **17** DRSCs (Rules Committee recommendation).\n"
            "- **2004**: +7 → **24** (cover all Central ministries/departments).\n\n"
            "## Composition\n\n"
            "- Each: **31** members — **21 LS + 10 RS** (earlier up to 45 until July 2004 restructuring).\n"
            "- Nominated by Speaker (LS) and Chairman (RS) — not elected like financial trio.\n"
            "- Minister **ineligible**; becomes minister → ceases membership.\n"
            "- Term: **one year** from constitution.\n"
            "- Split: **8 under Rajya Sabha**, **16 under Lok Sabha**.\n\n"
            "## Functions\n\n"
            "1. Consider **Demands for Grants** of concerned ministries **before** discussion/vote in LS "
            "(report must **not** suggest cut motions).\n"
            "2. Examine bills of those ministries.\n"
            "3. Consider annual reports.\n"
            "4. Consider national basic **long-term policy** documents.\n\n"
            "## Limits\n\n"
            "- No day-to-day administration.\n"
            "- Generally avoid matters of other parliamentary committees.\n"
            "- Recommendations **advisory** (not binding on Parliament).\n\n"
            "## Mains merits (value-adds)\n\n"
            "- Proceedings relatively free of party bias; flexible procedure.\n"
            "- Closer, continuous, in-depth executive control.\n"
            "- Economy/efficiency pressure on ministries; informed House debates.\n"
            "- Wider MP participation; expert/public evidence; stronger RS role in financial control.\n\n"
            "### Do not dump Table 24.1\n"
            "Remember **8 RS + 16 LS** and that all ministries are covered — open jurisdiction only if a PYQ names a ministry."
        ),
        "articles": [
            (
                "DRSCs",
                "1993: 17 → 2004: 24; each 31 (21 LS + 10 RS); 8 under RS, 16 under LS.",
            ),
            (
                "K.R. Narayanan (1993)",
                "Purpose: more detailed consideration → meaningful accountability, not to weaken administration.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-drsc-timeline",
                "type": "timeline",
                "title": "DRSC evolution",
                "events": [
                    {
                        "id": "e1989",
                        "year": 1989,
                        "label": "3 pilots",
                        "detail": "Agriculture; Science & Technology; Environment & Forests.",
                    },
                    {
                        "id": "e1993",
                        "year": 1993,
                        "label": "17 DRSCs",
                        "detail": "Rules Committee recommendation; inaugurated 31 March 1993.",
                    },
                    {
                        "id": "e2004",
                        "year": 2004,
                        "label": "24 DRSCs · 31 members",
                        "detail": "+7 committees; strength fixed at 21 LS + 10 RS.",
                    },
                ],
            },
            {
                "id": "pc-drsc-dfg-flow",
                "type": "flowchart",
                "title": "DFG scrutiny cycle",
                "root": "budget",
                "steps": [
                    {
                        "id": "budget",
                        "label": "General discussion on Budget",
                        "detail": "In both Houses.",
                        "options": [
                            {"label": "Next", "next": "adjourn"},
                        ],
                    },
                    {
                        "id": "adjourn",
                        "label": "Houses adjourn for fixed period",
                        "detail": "Window for committee work.",
                        "options": [
                            {"label": "Next", "next": "scrutinise"},
                        ],
                    },
                    {
                        "id": "scrutinise",
                        "label": "DRSCs consider DFGs",
                        "detail": "No request for more time; separate report per ministry.",
                        "options": [
                            {"label": "Next", "next": "house"},
                        ],
                    },
                    {
                        "id": "house",
                        "label": "House considers DFGs in light of reports",
                        "detail": "Reports inform debate; no cut-motion suggestions in reports.",
                    },
                ],
            },
            {
                "id": "pc-drsc-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Numbers to lock",
                "body": (
                    "**24** committees · **31** members (21+10) · **8** under RS / **16** under LS · "
                    "minister ineligible · recommendations advisory."
                ),
            },
        ],
    },
    {
        "title": "Other Standing Committees",
        "slug": "pc-other-standing",
        "sort_order": 8,
        "summary": (
            "Inquire, Scrutinise & Control, Day-to-day Business, and House-keeping — "
            "high-yield membership numbers and LS-only traps."
        ),
        "body": (
            "## Four buckets (non-financial standing)\n\n"
            "### 1. Committees to Inquire\n"
            "- **Petitions** — bills & public importance; representations on Union subjects.\n"
            "- **Privileges** — semi-judicial; breach of privilege.\n"
            "- **Ethics** — code of conduct (RS 1997; LS 2000).\n\n"
            "### 2. Scrutinise & Control\n"
            "- **Government Assurances** (1953) — promises on the floor.\n"
            "- **Subordinate Legislation** (1953) — delegated rules within scope (**classic PYQ**).\n"
            "- **Papers Laid on the Table** (1975) — compliance of papers (not Sub. Leg. notifications).\n"
            "- **SC/ST Welfare** (30 = 20+10) — NCSC/NCST reports & safeguards.\n"
            "- **Empowerment of Women** (1997; 30 = 20+10) — NCW reports & equality measures.\n"
            "- **Offices of Profit** (15 = 10+5) — disqualification angle.\n\n"
            "### 3. Day-to-day Business\n"
            "- **Business Advisory** — timetable (LS: Speaker chairs; RS: Chairman ex-officio).\n"
            "- **Private Members’ Bills & Resolutions** — **LS only** (Dy Speaker chairs); RS → BAC.\n"
            "- **Rules Committee** — procedure amendments.\n"
            "- **Absence of Members** — **LS only**; 60-day absence cases.\n\n"
            "### 4. House-keeping\n"
            "- General Purposes · House · Library (9 = 6+3) · Salaries & Allowances (1954 Act; 15 = 10+5).\n\n"
            "## Membership cheat-sheet\n\n"
            "| Committee | LS | RS | Hook |\n"
            "|-----------|----|----|------|\n"
            "| Petitions / Privileges / Ethics | 15 | 10 | Ethics: RS ’97, LS ’00 |\n"
            "| Govt Assurances / Papers Laid | 15 | 10 | Assurances 1953 |\n"
            "| Subordinate Legislation | **15** | **15** | Both Houses 15 |\n"
            "| SC/ST; Women Empowerment | 20 | 10 | Joint 30 |\n"
            "| Offices of Profit | 10 | 5 | Disqualification |\n"
            "| Business Advisory | 15 (+Speaker) | 11 (+Chairman) | Timetable |\n"
            "| Private Members’ Bills | 15 (Dy Speaker) | **None** | LS-only |\n"
            "| Absence of Members | 15 | **None** | 60 days |\n"
            "| Library | 6 | 3 | Total 9 |\n"
            "| Salaries & Allowances | 10 | 5 | 1954 Act |"
        ),
        "articles": [
            (
                "Other standing",
                "Inquire · Scrutinise · Business · House-keeping — membership table.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-other-pillars",
                "type": "pillars",
                "title": "Four non-financial standing buckets",
                "items": [
                    {
                        "id": "inquire",
                        "articles": "3",
                        "label": "Inquire",
                        "slug": "pc-other-standing",
                        "detail": "Petitions · Privileges · Ethics.",
                        "tone": "teal",
                    },
                    {
                        "id": "scrutinise",
                        "articles": "6",
                        "label": "Scrutinise & Control",
                        "slug": "pc-other-standing",
                        "detail": "Assurances · Sub. Leg. · Papers · SC/ST · Women · Offices of Profit.",
                        "tone": "gold",
                    },
                    {
                        "id": "business",
                        "articles": "4",
                        "label": "Day-to-day Business",
                        "slug": "pc-other-standing",
                        "detail": "BAC · Private Members · Rules · Absence.",
                        "tone": "orange",
                    },
                    {
                        "id": "house",
                        "articles": "4",
                        "label": "House-keeping",
                        "slug": "pc-other-standing",
                        "detail": "General Purposes · House · Library · Salaries.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pc-other-trap",
                "type": "callout",
                "tone": "trap",
                "title": "LS-only specials",
                "body": (
                    "Committee on Private Members’ Bills and Resolutions and Committee on Absence "
                    "of Members exist only in **Lok Sabha**. In Rajya Sabha, BAC / House itself covers them."
                ),
            },
        ],
    },
    {
        "title": "Ad Hoc Committees",
        "slug": "pc-ad-hoc",
        "sort_order": 9,
        "summary": (
            "Temporary inquiry committees on specific subjects, plus Select/Joint Committees "
            "that scrutinise particular Bills clause by clause."
        ),
        "body": (
            "## Two ad hoc types\n\n"
            "### 1. Inquiry Committees\n"
            "Constituted by Houses on a motion, or by Speaker/Chairman, for a specific subject. "
            "High-yield examples:\n"
            "- **Railway Convention Committee** (first post-independence 1949; dividend + later Railway subjects)\n"
            "- Committee on **MPLADS**\n"
            "- Joint Committee on **Security in Parliament Complex**\n"
            "- Committee on Welfare of **OBCs**\n"
            "- Committee to Inquire into Improper Conduct of a Member\n\n"
            "(Skip low-yield amenities/portrait-type lists for revision.)\n\n"
            "### 2. Advisory — Select / Joint on Bills\n"
            "- House may refer a Bill to a **Select Committee** of that House or a **Joint Committee** of both.\n"
            "- Motion required; for Joint Committee, other House nominates members.\n"
            "- Committee considers Bill **clause by clause**; can take evidence; amendments possible.\n"
            "- Report to the House; dissenters may append **minutes of dissent**.\n"
            "- Procedure fixed in Rules + Speaker/Chairman directions — distinct from other ad hoc bodies."
        ),
        "articles": [
            (
                "Ad hoc",
                "Inquiry committees + Select/Joint Committees on Bills.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-adhoc-bill-flow",
                "type": "flowchart",
                "title": "Bill → Select or Joint Committee",
                "root": "bill",
                "steps": [
                    {
                        "id": "bill",
                        "label": "Bill up for general discussion",
                        "detail": "House may keep it or refer it.",
                        "options": [
                            {"label": "Refer to Select Committee", "next": "select"},
                            {"label": "Refer to Joint Committee", "next": "joint"},
                            {"label": "No reference", "next": "floor"},
                        ],
                    },
                    {
                        "id": "select",
                        "label": "Select Committee of that House",
                        "detail": "Clause-by-clause + evidence + amendments.",
                        "options": [
                            {"label": "Report", "next": "report"},
                        ],
                    },
                    {
                        "id": "joint",
                        "label": "Joint Committee of both Houses",
                        "detail": "Other House nominates members after motion.",
                        "options": [
                            {"label": "Report", "next": "report"},
                        ],
                    },
                    {
                        "id": "report",
                        "label": "Report to the House",
                        "detail": "Majority report; minutes of dissent allowed.",
                    },
                    {
                        "id": "floor",
                        "label": "Proceed on the floor",
                        "detail": "No committee stage for that Bill.",
                    },
                ],
            },
            {
                "id": "pc-adhoc-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "Ad hoc = temporary. If the exam names a **Bill** committee → Select/Joint. "
                    "If it names a **subject inquiry** → Inquiry Committee."
                ),
            },
        ],
    },
    {
        "title": "Consultative Committees",
        "slug": "pc-consultative",
        "sort_order": 10,
        "summary": (
            "MoPA-constituted informal forums chaired by the Minister — MPs discuss policy, "
            "but these are NOT parliamentary committees."
        ),
        "body": (
            "## What they are\n\n"
            "- Attached to various Central ministries/departments.\n"
            "- Members from **both Houses**; membership **voluntary** (party choice).\n"
            "- **Minister / MoS** of that ministry chairs.\n"
            "- Forum for **informal** discussion of policies, programmes, and implementation.\n"
            "- Constituted by **Ministry of Parliamentary Affairs** (guidelines + meeting logistics).\n"
            "- Strength: **minimum 10, maximum 30**.\n"
            "- Constituted after a new Lok Sabha; **dissolve** on LS dissolution; reconstituted with next LS.\n\n"
            "## Extra\n\n"
            "- Separate **Informal Consultative Committees** for Railway Zones "
            "(MPs from the zone’s area).\n\n"
            "## Hard rule\n\n"
            "They **fail the four tests** → **not** parliamentary committees "
            "(despite being composed of MPs)."
        ),
        "articles": [
            (
                "Consultative Committees",
                "MoPA; Minister chairs; informal; 10–30; dissolve with Lok Sabha.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-consult-compare",
                "type": "comparison",
                "title": "Parliamentary vs Consultative",
                "columns": [
                    {
                        "id": "pc",
                        "heading": "Parliamentary committee",
                        "points": [
                            "Appointed/elected/nominated under House Rules",
                            "Works under Speaker/Chairman direction",
                            "Reports to House / Speaker / Chairman",
                            "House secretariat",
                            "Formal scrutiny & recommendations",
                        ],
                    },
                    {
                        "id": "cc",
                        "heading": "Consultative committee",
                        "points": [
                            "Constituted by MoPA",
                            "Minister chairs",
                            "Informal discussion forum",
                            "No House-secretariat PC footing",
                            "Fails the four tests → not a PC",
                        ],
                    },
                ],
            },
            {
                "id": "pc-consult-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Must-win prelims trap",
                "body": (
                    "If a statement says ‘Consultative Committees are parliamentary committees’ "
                    "→ **False**. Same if it implies Speaker direction / House report / LS secretariat."
                ),
            },
        ],
    },
    {
        "title": "PYQ & Quick Tables",
        "slug": "pc-revision-tables",
        "sort_order": 11,
        "summary": (
            "Last-minute pack — membership cheat-sheet, prelims facts, mains value-adds, "
            "memory palace, and PYQ themes."
        ),
        "body": (
            "## Membership & chair cheat-sheet\n\n"
            "| Body | Key number | Chair convention |\n"
            "|------|------------|------------------|\n"
            "| PAC | 22 (15+7) | **Opposition** (since 1967) |\n"
            "| Estimates | **30 LS only** | Usually ruling |\n"
            "| PUC | 22 (15+7) | Speaker appoints |\n"
            "| Each DRSC | **31** (21+10) | Nominated; no minister |\n"
            "| DRSCs total | **24** (8 RS + 16 LS) | — |\n"
            "| Sub. Legislation | 15 / 15 | — |\n"
            "| Consultative | 10–30 | **Minister** |\n\n"
            "## Minister cannot be member\n\n"
            "PAC · Estimates · PUC · DRSCs (and typically other scrutiny committees).\n\n"
            "## Prelims facts\n\n"
            "- Opp chair PAC; Estimates LS-only; no CAG for Estimates.\n"
            "- DRSC 24 & 31; Subordinate Legislation = delegated legislation check.\n"
            "- Consultative ≠ parliamentary; PUC ← Krishna Menon 1964.\n"
            "- CAG = guide, friend, philosopher of PAC.\n"
            "- Committee recommendations are **advisory**.\n\n"
            "## Mains value-adds\n\n"
            "- Financial committees **institutionalise** parliamentary financial control but remain "
            "**post-mortem** and **advisory**.\n"
            "- DRSCs deepen accountability, nourish information for debates, and give RS a larger role.\n"
            "- Party-less working culture vs limits (no binding force; capacity constraints).\n"
            "- Structure answer: Standing (6 buckets) + Ad hoc (Inquiry / Select-Joint) + "
            "Financial trio + DRSCs + limits.\n\n"
            "### 30-second script\n"
            "4 tests → Standing/Ad hoc → PAC(CAG/Opp) · Estimates(LS30/no CAG) · PUC(Menon) → "
            "DRSC 24/31 → Consultative ≠ PC → advisory."
        ),
        "articles": [
            (
                "Exam pack",
                "Numbers, chair conventions, prelims traps, mains structure.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pc-memory-palace",
                "type": "memory_palace",
                "title": "Parliament corridor memory walk",
                "setting": "Parliament House corridor of committee rooms",
                "loci": [
                    {
                        "id": "l1",
                        "place": "Entrance gate",
                        "association": "Four tests (A-D-R-S)",
                        "detail": "Appointed · Direction · Report · Secretariat — Consultative fail here.",
                    },
                    {
                        "id": "l2",
                        "place": "Accounts chamber",
                        "association": "PAC",
                        "detail": "22 · Opp chair · CAG friend · past expenditure.",
                    },
                    {
                        "id": "l3",
                        "place": "Economy alcove",
                        "association": "Estimates",
                        "detail": "30 LS only · continuous economy · no CAG.",
                    },
                    {
                        "id": "l4",
                        "place": "PSU gallery",
                        "association": "PUC",
                        "detail": "Krishna Menon 1964 · 22 · commercial prudence.",
                    },
                    {
                        "id": "l5",
                        "place": "Ministry map wall",
                        "association": "DRSCs",
                        "detail": "24 · 31 (21+10) · DFGs before vote · advisory.",
                    },
                    {
                        "id": "l6",
                        "place": "Informal lounge",
                        "association": "Consultative",
                        "detail": "MoPA · Minister chairs · not a PC.",
                    },
                ],
            },
            {
                "id": "pc-exam-lanes",
                "type": "pillars",
                "title": "Three exam lanes",
                "items": [
                    {
                        "id": "prelims",
                        "articles": "Facts",
                        "label": "Prelims facts",
                        "slug": "pc-revision-tables",
                        "detail": "Opp PAC · LS-only Estimates · DRSC 24/31 · Sub. Leg. · Consultative trap.",
                        "tone": "teal",
                    },
                    {
                        "id": "mains",
                        "articles": "VA",
                        "label": "Mains value-adds",
                        "slug": "pc-revision-tables",
                        "detail": "Institutionalisation + post-mortem limits; DRSC accountability depth.",
                        "tone": "gold",
                    },
                    {
                        "id": "pyq",
                        "articles": "Themes",
                        "label": "PYQ themes",
                        "slug": "pc-revision-tables",
                        "detail": "Sub. Leg. ID · PAC–CAG · Estimates functions · PUC origin · system structure.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pc-exam-script",
                "type": "callout",
                "tone": "tip",
                "title": "30-second revision",
                "body": (
                    "4 tests · Standing/Ad hoc · PAC=CAG+Opp · Estimates=LS30+no CAG · "
                    "PUC=Menon · DRSC 24/31 · Consultative≠PC · all advisory."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pc-meaning"),
    (HUB_SLUG, "parent", "pc-classification"),
    (HUB_SLUG, "parent", "pc-financial-trio"),
    (HUB_SLUG, "parent", "pc-pac"),
    (HUB_SLUG, "parent", "pc-estimates"),
    (HUB_SLUG, "parent", "pc-puc"),
    (HUB_SLUG, "parent", "pc-drsc"),
    (HUB_SLUG, "parent", "pc-other-standing"),
    (HUB_SLUG, "parent", "pc-ad-hoc"),
    (HUB_SLUG, "parent", "pc-consultative"),
    (HUB_SLUG, "parent", "pc-revision-tables"),
    ("pc-financial-trio", "parent", "pc-pac"),
    ("pc-financial-trio", "parent", "pc-estimates"),
    ("pc-financial-trio", "parent", "pc-puc"),
    ("pc-meaning", "related", "pc-classification"),
    ("pc-meaning", "related", "pc-consultative"),
    ("pc-classification", "related", "pc-financial-trio"),
    ("pc-classification", "related", "pc-drsc"),
    ("pc-classification", "related", "pc-ad-hoc"),
    ("pc-pac", "related", "pc-estimates"),
    ("pc-estimates", "related", "pc-puc"),
    ("pc-drsc", "related", "pc-financial-trio"),
    ("pc-other-standing", "related", "pc-revision-tables"),
    ("pc-ad-hoc", "related", "pc-drsc"),
    ("pc-consultative", "related", "pc-revision-tables"),
    ("pc-pac", "related", "cag"),
    ("pc-pac", "related", "public-accounts-committee"),
    ("parliamentary-system", "related", HUB_SLUG),
    ("parliament", "related", HUB_SLUG),
]

SAMPLE_PYQS = [
    (
        2013,
        (
            "With reference to the Parliament of India, which of the following Parliamentary Committees "
            "scrutinizes and reports to the House whether the powers to make regulations, rules, "
            "sub-rules, by-laws, etc. conferred by the Constitution or delegated by the Parliament "
            "are being properly exercised by the Executive within the scope of such delegation?"
        ),
        "Committee on Subordinate Legislation.",
        ["pc-other-standing", "pc-revision-tables"],
    ),
    (
        2015,
        (
            "The need for a separate parliamentary committee on public undertakings was first visualised by:"
        ),
        "Krishna Menon Committee.",
        ["pc-puc", "pc-financial-trio"],
    ),
    (
        2017,
        (
            "Which of the following are the functions of the Public Accounts Committee of Parliament?"
        ),
        (
            "Examines appropriation and finance accounts and CAG audit reports; checks legal "
            "availability and authority of expenditure; post-mortem financial control — assisted by CAG."
        ),
        ["pc-pac", "pc-financial-trio"],
    ),
    (
        2019,
        "The functions of the Estimates Committee include:",
        (
            "Suggesting economies, efficiency, and administrative reform consistent with the policy "
            "in the estimates; may suggest alternative policies; continuous economy committee."
        ),
        ["pc-estimates", "pc-financial-trio"],
    ),
    (
        2023,
        (
            "Explain the structure of the Parliamentary Committee system. How far have the financial "
            "committees helped in the institutionalisation of the Indian Parliament?"
        ),
        (
            "Structure: Standing (financial, DRSC, inquire, scrutinise, business, housekeeping) + "
            "Ad hoc (inquiry / Select-Joint). Financial committees institutionalise oversight via "
            "PAC–CAG, Estimates, and PUC, but remain advisory and largely post-mortem."
        ),
        ["pc-classification", "pc-financial-trio", "pc-revision-tables", HUB_SLUG],
    ),
]


class Command(BaseCommand):
    help = "Seed Parliamentary Committees chapter (Laxmikanth Ch.24)."

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
                "title": "Parliamentary Committees",
                "sort_order": 9,
                "book_ref": "Laxmikanth 8th Ed, Ch. 24",
                "summary": (
                    "Visual revision of Ch.24 — meaning & four tests, standing/ad hoc map, "
                    "financial trio, DRSCs, other standing, ad hoc, consultative trap, exam box."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Parliamentary Committees",
                "summary": (
                    "Parliament’s specialised workbench — standing and ad hoc committees under "
                    "the Rules of the Houses for detailed legislative and financial scrutiny."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **specialised workbench** mental model, then "
                    "**Meaning (4 tests)** → **Classification** → **Financial trio**. "
                    "Drill **PAC / Estimates / PUC** and **DRSCs**, scan **Other standing** "
                    "and **Ad hoc**, lock the **Consultative ≠ PC** trap, finish with the "
                    "**Exam box**. This is a visual revision layer — not a substitute for Laxmikanth."
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
            ref="Laxmikanth Ch. 24",
            excerpt=(
                "Parliamentary Committees — meaning, standing/ad hoc, financial committees, "
                "DRSCs, and consultative committees."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Rules of the Houses",
            excerpt="Composition, tenure, and functions of parliamentary committees.",
            sort_order=1,
        )

        pc_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=pc_slugs) | Q(target__slug__in=pc_slugs),
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
                pyq.concepts.add(*concepts)

        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Parliamentary Committees chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
