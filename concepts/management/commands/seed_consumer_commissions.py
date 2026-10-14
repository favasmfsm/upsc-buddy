"""Seed Laxmikanth Ch.37 Consumer Commissions (visual revision — Part IV State Government)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "consumer-commissions"
CHAPTER_SLUG = "consumer-commissions"

ENTRY_PILLARS = [
    {
        "id": "cpa",
        "articles": "CPA 2019",
        "label": "CPA 2019 & hierarchy",
        "slug": "cc-cpa-2019",
        "detail": "1986 repealed; three-tier District–State–National forums.",
        "tone": "teal",
    },
    {
        "id": "rights",
        "articles": "6 rights",
        "label": "Consumer rights & CCPA",
        "slug": "cc-consumer-rights",
        "detail": "Six statutory rights + CCPA; appeal to National Commission.",
        "tone": "olive",
    },
    {
        "id": "national",
        "articles": "NCDRC",
        "label": "National Commission",
        "slug": "cc-national",
        "detail": "Composition, tenure, pecuniary/appellate/revisional, admin control.",
        "tone": "gold",
    },
    {
        "id": "state",
        "articles": "SCDRC",
        "label": "State Commission",
        "slug": "cc-state",
        "detail": "45-day appeals from District; Centre–state rule split.",
        "tone": "orange",
    },
    {
        "id": "district",
        "articles": "DCDRC",
        "label": "District Commission",
        "slug": "cc-district",
        "detail": "Entry forum; pecuniary only; vacancy bridging by state.",
        "tone": "terracotta",
    },
    {
        "id": "table",
        "articles": "Table 37.1",
        "label": "Pecuniary jurisdiction",
        "slug": "cc-jurisdiction-table",
        "detail": "2021 Rules default: 50L → 2Cr → above.",
        "tone": "maroon",
    },
    {
        "id": "appeals",
        "articles": "Ladder",
        "label": "Appeals & control",
        "slug": "cc-appeals-control",
        "detail": "45 then thirties; NCDRC admin control; transfers.",
        "tone": "teal",
    },
    {
        "id": "exam",
        "articles": "PYQ kit",
        "label": "Exam kit",
        "slug": "cc-exam-kit",
        "detail": "Prelims traps, PYQ themes, mains one-liners, memory box.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "cc-ladder-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Three-tier consumer court ladder",
        "topic_label": "Consumer Commissions",
        "subject_label": "CPA 2019 · Ch. 37",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating them as regular civil courts",
            "Memorising 2019 Act limits instead of 2021 Rules",
            "Mixing appeal windows (45 vs 30 days)",
            "Forgetting CCPA appeals go to the National Commission",
        ],
        "insight": (
            "Quasi-judicial ADR for consumers only — District → State → National → Supreme Court; "
            "pecuniary ladder under 2021 Rules is the exam default."
        ),
    },
    {
        "id": "cc-entry-pillars",
        "type": "pillars",
        "title": "Eight revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "cc-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Path: CPA 2019 → Rights/CCPA → District → State → National → Table 37.1 → Appeals. "
            "Trap trio: **50L / 2Cr** (2021); **45 then thirties**; tenure **4 yrs** "
            "(Pres 70 / members 67) via Tribunals Reforms Act 2021."
        ),
    },
]

CLUSTERS = [
    {
        "title": "CPA 2019 & Three-Tier Hierarchy",
        "slug": "cc-cpa-2019",
        "sort_order": 1,
        "summary": (
            "Consumer Protection Act, 2019 replaces 1986; District, State, and National "
            "Commissions as quasi-judicial consumer forums."
        ),
        "body": (
            "## CPA 2019\n\n"
            "The **Consumer Protection Act, 2019** repealed and replaced the **1986 Act**. "
            "It retains a **three-tier** consumer dispute redressal machinery.\n\n"
            "### Names (full → short)\n"
            "- District Consumer Disputes Redressal Commission → **District Commission**\n"
            "- State Consumer Disputes Redressal Commission → **State Commission**\n"
            "- National Consumer Disputes Redressal Commission → **National Commission (NCDRC)**\n\n"
            "Popular labels: consumer forums / consumer courts. Nature: **quasi-judicial** "
            "ADR **exclusively for consumers**.\n\n"
            "### Who establishes?\n"
            "- **District:** state government (may set up more than one in a district).\n"
            "- **State:** state government (ordinarily at capital; regional branches allowed; "
            "other places notified in consultation with the State Commission).\n"
            "- **National:** central government (ordinarily NCR; regional branches; other places "
            "notified in consultation with the National Commission).\n\n"
            "### Scale (book snapshot)\n"
            "~**678** District Commissions, **35** State Commissions, National Commission at apex "
            "(constituted **1988**)."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 37",
                "CPA 2019 three-tier District, State, and National Consumer Disputes Redressal Commissions.",
            ),
            (
                "CPA 2019",
                "Repealed and replaced the Consumer Protection Act, 1986.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-cpa-tree",
                "type": "tree",
                "title": "Three-tier hierarchy",
                "root": {
                    "id": "cpa",
                    "label": "CPA 2019 forums",
                    "detail": "Quasi-judicial · consumers only",
                    "children": [
                        {
                            "id": "nat",
                            "label": "National Commission",
                            "slug": "cc-national",
                            "detail": "Centre establishes · apex",
                            "children": [
                                {
                                    "id": "state",
                                    "label": "State Commission",
                                    "slug": "cc-state",
                                    "detail": "State establishes",
                                    "children": [
                                        {
                                            "id": "dist",
                                            "label": "District Commission",
                                            "slug": "cc-district",
                                            "detail": "State establishes · entry forum",
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "id": "cc-cpa-timeline",
                "type": "timeline",
                "title": "Reform spine",
                "events": [
                    {
                        "id": "e1986",
                        "year": 1986,
                        "label": "CPA 1986",
                        "detail": "Original three-tier consumer forums.",
                    },
                    {
                        "id": "e1988",
                        "year": 1988,
                        "label": "NCDRC set up",
                        "detail": "National Commission constituted.",
                    },
                    {
                        "id": "e2019",
                        "year": 2019,
                        "label": "CPA 2019",
                        "detail": "Repeals 1986; modern consumer regime.",
                    },
                    {
                        "id": "e2020",
                        "year": 2020,
                        "label": "Commission Rules",
                        "detail": "Composition (e.g. NCDRC ≤11 members).",
                    },
                    {
                        "id": "e2021",
                        "year": 2021,
                        "label": "Jurisdiction + tenure",
                        "detail": "2021 pecuniary Rules; Tribunals Reforms Act tenure.",
                    },
                ],
            },
            {
                "id": "cc-cpa-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Not ordinary civil courts — **quasi-judicial** consumer ADR. "
                    "District & State = **state** government; National = **Centre**."
                ),
            },
        ],
    },
    {
        "title": "Consumer Rights & CCPA",
        "slug": "cc-consumer-rights",
        "sort_order": 2,
        "summary": (
            "Six consumer rights under CPA 2019 and the Central Consumer Protection Authority; "
            "CCPA orders are appealable to the National Commission."
        ),
        "body": (
            "## Six consumer rights (UPSC pack)\n\n"
            "CPA 2019 recognises six core rights (memory chain **SIIRRC**):\n\n"
            "1. **Safety** — protection against hazardous goods/services.\n"
            "2. **Information** — be informed about quality, quantity, potency, purity, price, standards.\n"
            "3. **Choice** — access to a variety of goods/services at competitive prices.\n"
            "4. **Representation** — be heard and assured that consumer interests will receive due consideration.\n"
            "5. **Redressal** — seek redress against unfair trade practices / restrictive practices / exploitation.\n"
            "6. **Consumer education** — acquire knowledge and skills to be an informed consumer.\n\n"
            "## CCPA\n\n"
            "The **Central Consumer Protection Authority (CCPA)** is the Centre’s regulator under "
            "CPA 2019 (unfair trade practices, misleading ads, consumer rights protection).\n\n"
            "Orders of the CCPA can be appealed to the **National Commission within 30 days** "
            "of receipt (condonation possible for sufficient cause).\n\n"
            "*Rights list is a standard CPA 2019 revision pack; Laxmikanth Ch.37 focuses on "
            "commission machinery and links CCPA via National Commission appeals.*"
        ),
        "articles": [
            (
                "CPA 2019 · CCPA",
                "CCPA orders appealable to the National Commission within 30 days.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-rights-pillars",
                "type": "pillars",
                "title": "Six consumer rights (SIIRRC)",
                "items": [
                    {
                        "id": "safety",
                        "articles": "1",
                        "label": "Safety",
                        "detail": "Against hazardous goods and services.",
                        "tone": "teal",
                    },
                    {
                        "id": "info",
                        "articles": "2",
                        "label": "Information",
                        "detail": "Quality, quantity, price, standards.",
                        "tone": "olive",
                    },
                    {
                        "id": "choice",
                        "articles": "3",
                        "label": "Choice",
                        "detail": "Variety at competitive prices.",
                        "tone": "gold",
                    },
                    {
                        "id": "rep",
                        "articles": "4",
                        "label": "Representation",
                        "detail": "Right to be heard.",
                        "tone": "orange",
                    },
                    {
                        "id": "redress",
                        "articles": "5",
                        "label": "Redressal",
                        "detail": "Against unfair / restrictive practices.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "edu",
                        "articles": "6",
                        "label": "Consumer education",
                        "detail": "Skills to be an informed consumer.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "cc-rights-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory box",
                "body": (
                    "**SIIRRC** — Safety, Information, Choice, Representation, Redressal, "
                    "Consumer education. CCPA → National Commission in **30 days**."
                ),
            },
        ],
    },
    {
        "title": "National Commission (NCDRC)",
        "slug": "cc-national",
        "sort_order": 3,
        "summary": (
            "Composition, appointment, tenure, pecuniary/appellate/revisional jurisdiction, "
            "other powers, and administrative control over State Commissions."
        ),
        "body": (
            "## Composition (2020 Rules)\n\n"
            "- **President** + not less than **four** and not more than **eleven** members.\n"
            "- Of the eleven members, **at least one woman**.\n"
            "- Minimum age for President/member: **50 years**.\n"
            "- Appointed by the **central government** on recommendation of a "
            "**search-cum-selection committee** chaired by the **CJI** or a Supreme Court Judge "
            "nominated by the CJI.\n"
            "- Centre makes rules on qualifications, appointment, salaries, resignation, removal, etc.\n"
            "- Salary/allowances and other service conditions **shall not be varied to disadvantage** "
            "after appointment.\n\n"
            "## Tenure (Tribunals Reforms Act, 2021)\n\n"
            "**4 years** or until age **70** (President) / **67** (members), whichever is earlier.\n\n"
            "## Jurisdiction\n\n"
            "1. **Pecuniary** — consideration **above ₹2 crore** (2021 Rules; Act text had above ₹10 crore).\n"
            "2. **Appellate** — appeals from any **State Commission** (within **30 days** of order; "
            "condonation allowed). Also appeals from **CCPA** (within **30 days** of receipt).\n"
            "3. **Revisional** — call for records / pass orders where a State Commission "
            "(a) exercised jurisdiction not vested, (b) failed to exercise vested jurisdiction, or "
            "(c) acted illegally / with material irregularity.\n\n"
            "## Other powers\n\n"
            "- Declare **unfair contract terms** null and void.\n"
            "- **Review** own orders for error apparent (suo motu or on application within **30 days**).\n"
            "- Set aside **ex-parte** orders on application.\n"
            "- **Transfer** complaints: District of one state ↔ another, or State ↔ State "
            "(on application or suo motu).\n\n"
            "## Appeal upward\n\n"
            "Appeal from National Commission → **Supreme Court** within **30 days** "
            "(condonation possible)."
        ),
        "articles": [
            (
                "Commission Rules, 2020",
                "National Commission: President + 4–11 members; at least one woman.",
            ),
            (
                "Tribunals Reforms Act, 2021",
                "Term 4 years or age 70 (President) / 67 (members), whichever earlier.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-nat-pillars",
                "type": "pillars",
                "title": "NCDRC at a glance",
                "items": [
                    {
                        "id": "comp",
                        "articles": "2020",
                        "label": "Composition",
                        "detail": "President + 4–11; ≥1 woman; age ≥50.",
                        "tone": "teal",
                    },
                    {
                        "id": "appoint",
                        "articles": "CJI chair",
                        "label": "Appointment",
                        "detail": "Centre on search-cum-selection (CJI/SC judge).",
                        "tone": "olive",
                    },
                    {
                        "id": "term",
                        "articles": "2021",
                        "label": "Tenure",
                        "detail": "4 yrs or 70 / 67 — Tribunals Reforms.",
                        "tone": "gold",
                    },
                    {
                        "id": "juris",
                        "articles": "3 heads",
                        "label": "Jurisdiction",
                        "detail": "Pecuniary + appellate + revisional.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "cc-nat-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims trio",
                "body": (
                    "Above **₹2 crore** (2021) · appeal to SC in **30 days** · "
                    "admin control over **all State Commissions** (without killing quasi-judicial freedom)."
                ),
            },
            {
                "id": "cc-nat-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Trap",
                "body": (
                    "Do not quote the bare 2019 Act’s ₹10 crore National threshold as current "
                    "exam default — **2021 Rules** lowered it to **above ₹2 crore**."
                ),
            },
        ],
    },
    {
        "title": "State Commission",
        "slug": "cc-state",
        "sort_order": 4,
        "summary": (
            "Composition, Centre–state rule split, pecuniary/appellate/revisional jurisdiction, "
            "other powers, and administrative control over District Commissions."
        ),
        "body": (
            "## Composition\n\n"
            "President + not less than **four** and not more than such number as prescribed "
            "(in consultation with the central government).\n\n"
            "### Rule split (exam favourite)\n"
            "- **Centre** — qualifications, recruitment method, appointment procedure, term, "
            "resignation, removal.\n"
            "- **State** — salaries, allowances, and other service conditions.\n\n"
            "## Jurisdiction\n\n"
            "1. **Pecuniary** — above **₹50 lakh** up to **₹2 crore** (2021 Rules; Act had "
            "above ₹1 crore up to ₹10 crore).\n"
            "2. **Appellate** — appeals from any **District Commission within the state** "
            "within **45 days** (condonation possible).\n"
            "3. **Revisional** — same three grounds as National, but over District Commissions "
            "in the state.\n\n"
            "## Other powers\n\n"
            "- Unfair contract terms → null and void.\n"
            "- Review own orders (error apparent; 30 days).\n"
            "- Transfer complaint from one District Commission to another **within the state**.\n"
            "- **Administrative control** over all District Commissions in its jurisdiction."
        ),
        "articles": [
            (
                "CPA 2019 · State Commission",
                "Appeal from District Commission within 45 days; State controls Districts administratively.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-state-compare",
                "type": "comparison",
                "title": "State vs National — quick contrast",
                "columns": [
                    {
                        "id": "state",
                        "heading": "State Commission",
                        "points": [
                            "State establishes",
                            "Pecuniary: >₹50L to ₹2Cr (2021)",
                            "Appeals from District — 45 days",
                            "Admin control over Districts in state",
                            "Transfer only within the state",
                            "Centre: quals/term; State: pay",
                        ],
                    },
                    {
                        "id": "nat",
                        "heading": "National Commission",
                        "points": [
                            "Centre establishes",
                            "Pecuniary: >₹2Cr (2021)",
                            "Appeals from State / CCPA — 30 days",
                            "Admin control over all State Commissions",
                            "Inter-state / State↔State transfer",
                            "Centre rules on pay & service too",
                        ],
                    },
                ],
            },
            {
                "id": "cc-state-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory hook",
                "body": (
                    "**45** days only on the District→State step. Everything above that rung "
                    "is a **30**-day window."
                ),
            },
        ],
    },
    {
        "title": "District Commission",
        "slug": "cc-district",
        "sort_order": 5,
        "summary": (
            "Entry-level forum: composition, vacancy bridging, pecuniary jurisdiction up to "
            "₹50 lakh (2021), review power — no appellate jurisdiction."
        ),
        "body": (
            "## Composition\n\n"
            "President + not less than **two** and not more than such number as prescribed "
            "(in consultation with the Centre).\n\n"
            "- **Centre** — qualifications, recruitment, appointment procedure, term, resignation, removal.\n"
            "- **State** — salaries, allowances, other service conditions.\n\n"
            "### Vacancy bridging\n"
            "If President/member post is vacant, the state government may direct:\n"
            "1. another specified District Commission to exercise that district’s jurisdiction also; or\n"
            "2. President/member of another District Commission to discharge those functions also.\n\n"
            "## Jurisdiction & working\n\n"
            "- **Pecuniary only** — up to **₹50 lakh** (2021 Rules; Act had up to ₹1 crore).\n"
            "- No appellate jurisdiction over any lower forum.\n"
            "- Ordinarily at district HQ; may sit at other notified places (state govt in consultation "
            "with State Commission).\n"
            "- **Review** own orders for error apparent (suo motu or application within **30 days**)."
        ),
        "articles": [
            (
                "CPA 2019 · District Commission",
                "Entry forum; pecuniary up to ₹50 lakh under 2021 Rules; review within 30 days.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-dist-pillars",
                "type": "pillars",
                "title": "District Commission spine",
                "items": [
                    {
                        "id": "comp",
                        "articles": "≥2",
                        "label": "Composition",
                        "detail": "President + ≥2 members (as prescribed).",
                        "tone": "teal",
                    },
                    {
                        "id": "money",
                        "articles": "2021",
                        "label": "Pecuniary",
                        "detail": "Up to ₹50 lakh — exam default.",
                        "tone": "olive",
                    },
                    {
                        "id": "vacancy",
                        "articles": "State",
                        "label": "Vacancy bridge",
                        "detail": "Another District forum/member can cover.",
                        "tone": "gold",
                    },
                    {
                        "id": "review",
                        "articles": "30 days",
                        "label": "Review",
                        "detail": "Error apparent — same 30-day window.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "cc-dist-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "District Commission has **no appellate jurisdiction**. "
                    "It is the **entry** forum — appeals go **up** to the State Commission (45 days)."
                ),
            },
        ],
    },
    {
        "title": "Pecuniary Jurisdiction Table",
        "slug": "cc-jurisdiction-table",
        "sort_order": 6,
        "summary": (
            "Table 37.1 redesigned — 1986 Act vs 2019 Act vs 2021 Rules; revise the 2021 ladder first."
        ),
        "body": (
            "## Exam default — 2021 Rules\n\n"
            "| Forum | Pecuniary (consideration paid) |\n"
            "|---|---|\n"
            "| District | Up to **₹50 lakh** |\n"
            "| State | Above ₹50 lakh up to **₹2 crore** |\n"
            "| National | Above **₹2 crore** |\n\n"
            "## Why three columns?\n\n"
            "The Act itself set higher thresholds; the Centre reduced them in **2021** "
            "(Jurisdiction Rules). Prelims often tests the **current** ladder — memorise 2021, "
            "know 2019/1986 for contrast questions.\n\n"
            "### Act text (2019) vs Rules (2021)\n"
            "- District: ₹1 crore → **₹50 lakh**\n"
            "- State: ₹1–10 crore → **₹50 lakh–₹2 crore**\n"
            "- National: above ₹10 crore → **above ₹2 crore**\n\n"
            "### 1986 (historical)\n"
            "District ≤₹20 lakh · State ₹20 lakh–₹1 crore · National >₹1 crore."
        ),
        "articles": [
            (
                "Table 37.1",
                "Pecuniary jurisdiction under 2021 Rules, 2019 Act, and 1986 Act.",
            ),
            (
                "Jurisdiction Rules, 2021",
                "Reduced pecuniary thresholds for District, State, and National Commissions.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-juris-compare",
                "type": "comparison",
                "title": "Table 37.1 — pecuniary jurisdiction",
                "columns": [
                    {
                        "id": "rules2021",
                        "heading": "2021 Rules (revise)",
                        "points": [
                            "District: up to ₹50 lakh",
                            "State: >₹50 lakh to ₹2 crore",
                            "National: above ₹2 crore",
                            "Exam default ladder",
                        ],
                    },
                    {
                        "id": "act2019",
                        "heading": "2019 Act text",
                        "points": [
                            "District: up to ₹1 crore",
                            "State: >₹1 crore to ₹10 crore",
                            "National: above ₹10 crore",
                            "Centre may prescribe other values",
                        ],
                    },
                    {
                        "id": "act1986",
                        "heading": "1986 Act",
                        "points": [
                            "District: up to ₹20 lakh",
                            "State: >₹20 lakh to ₹1 crore",
                            "National: above ₹1 crore",
                            "Historical contrast only",
                        ],
                    },
                ],
            },
            {
                "id": "cc-juris-memory",
                "type": "callout",
                "tone": "tip",
                "title": "Memory box — 50L → 2Cr → above",
                "body": (
                    "Say it once: **fifty lakh, two crore, above**. "
                    "That is District / State / National under the **2021 Rules**."
                ),
            },
        ],
    },
    {
        "title": "Appeals & Administrative Control",
        "slug": "cc-appeals-control",
        "sort_order": 7,
        "summary": (
            "Appeal chain and deadlines, CCPA path, National Commission administrative control, "
            "and transfer powers."
        ),
        "body": (
            "## Appeal ladder\n\n"
            "1. District → State — **45 days** from District order.\n"
            "2. State → National — **30 days** from State order.\n"
            "3. CCPA → National — **30 days** from receipt of CCPA order.\n"
            "4. National → Supreme Court — **30 days** from National order.\n\n"
            "All windows allow **condonation** if sufficient cause is shown.\n\n"
            "## National administrative control over State Commissions\n\n"
            "1. Monitor performance — periodical returns on institution, disposal, pendency.\n"
            "2. Investigate allegations against State Commission President/members; "
            "inquiry reports to the concerned state government.\n"
            "3. Issue instructions on: uniform hearing procedures; prior service of document copies; "
            "English translation of non-English judgments; speedy grant of document copies.\n"
            "4. Oversee State/District functioning (inspection etc.) to serve Act objectives "
            "**without interfering with quasi-judicial freedom**.\n\n"
            "## Transfers\n\n"
            "- **National:** inter-state District transfers; State↔State.\n"
            "- **State:** District↔District within the state."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 37",
                "Appeal windows 45/30/30; National admin control; transfer powers.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-appeal-journey",
                "type": "journey",
                "title": "Appeal ladder",
                "stages": [
                    {
                        "id": "d",
                        "label": "District",
                        "slug": "cc-district",
                        "detail": "Entry forum · up to ₹50L",
                    },
                    {
                        "id": "s",
                        "label": "State (45 days)",
                        "slug": "cc-state",
                        "detail": "From District order",
                    },
                    {
                        "id": "n",
                        "label": "National (30 days)",
                        "slug": "cc-national",
                        "detail": "From State or CCPA",
                    },
                    {
                        "id": "sc",
                        "label": "Supreme Court (30 days)",
                        "detail": "From National order",
                    },
                ],
            },
            {
                "id": "cc-appeal-flow",
                "type": "flowchart",
                "title": "Which appeal window?",
                "root": "from",
                "steps": [
                    {
                        "id": "from",
                        "label": "Appealing from where?",
                        "detail": "Window depends on the forum below.",
                        "options": [
                            {"label": "District Commission", "next": "d45"},
                            {"label": "State Commission", "next": "n30"},
                            {"label": "CCPA", "next": "ccpa30"},
                            {"label": "National Commission", "next": "sc30"},
                        ],
                    },
                    {
                        "id": "d45",
                        "label": "→ State · 45 days",
                        "detail": "Only step with a 45-day limit.",
                    },
                    {
                        "id": "n30",
                        "label": "→ National · 30 days",
                        "detail": "From any State Commission order.",
                    },
                    {
                        "id": "ccpa30",
                        "label": "→ National · 30 days",
                        "detail": "From date of receipt of CCPA order.",
                    },
                    {
                        "id": "sc30",
                        "label": "→ Supreme Court · 30 days",
                        "detail": "Apex judicial review of NCDRC.",
                    },
                ],
            },
            {
                "id": "cc-appeal-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "**D-S-N-SC** + “45 then thirties”. "
                    "Admin control ≠ judicial interference — book stresses quasi-judicial freedom."
                ),
            },
        ],
    },
    {
        "title": "Exam Kit",
        "slug": "cc-exam-kit",
        "sort_order": 8,
        "summary": (
            "Prelims fact pack, traps, PYQ themes, mains value-adds, and last-minute memory aids."
        ),
        "body": (
            "## Prelims fact pack\n\n"
            "- CPA **2019** replaced **1986**; forums are **quasi-judicial**.\n"
            "- ~678 District · 35 State · NCDRC apex since **1988**.\n"
            "- Pecuniary **2021**: 50L / 2Cr / above.\n"
            "- Appeals: **45** (D→S) · **30** (S→N, CCPA→N, N→SC).\n"
            "- NCDRC: President + **4–11**; ≥1 woman; age ≥**50**; term **4 yrs** / 70 / 67.\n"
            "- Search-cum-selection chaired by **CJI** or nominated SC Judge.\n"
            "- District has **no** appellate jurisdiction.\n\n"
            "## PYQ themes\n\n"
            "- Who establishes which commission (state vs Centre).\n"
            "- Pecuniary limits — especially **2021 vs 2019 Act**.\n"
            "- Appeal periods and CCPA→National path.\n"
            "- Composition / woman member / age & tenure.\n"
            "- Nature of forums (quasi-judicial ADR, not ordinary courts).\n\n"
            "## Mains value-adds\n\n"
            "- Three-tier **specialised ADR** for consumers — speed and access vs civil suits.\n"
            "- **Centre–state rule split** at State/District (quals vs salaries) as cooperative federalism in regulation.\n"
            "- National **admin control** with explicit protection of quasi-judicial freedom.\n"
            "- CPA 2019 modernisation: regulator (CCPA) + lowered pecuniary thresholds for easier access.\n\n"
            "## Memory box\n\n"
            "- Ladder: **D-S-N-SC**\n"
            "- Money: **50L → 2Cr → above**\n"
            "- Time: **45 then thirties**\n"
            "- Reforms trio: **CPA 2019 · 2020 Commission Rules · 2021 Jurisdiction + Tribunals Reforms**\n"
            "- Rights: **SIIRRC**"
        ),
        "articles": [
            (
                "UPSC revision",
                "Pecuniary ladder, appeal windows, composition/tenure, and CPA 2019 framing.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-exam-heat",
                "type": "pyq_heatmap",
                "title": "PYQ focus map",
                "items": [
                    {"concept_slug": "cc-cpa-2019", "label": "CPA & hierarchy"},
                    {"concept_slug": "cc-jurisdiction-table", "label": "Pecuniary"},
                    {"concept_slug": "cc-appeals-control", "label": "Appeals"},
                    {"concept_slug": "cc-national", "label": "National"},
                    {"concept_slug": "cc-state", "label": "State"},
                    {"concept_slug": "cc-district", "label": "District"},
                    {"concept_slug": "cc-consumer-rights", "label": "Rights/CCPA"},
                ],
            },
            {
                "id": "cc-exam-traps",
                "type": "callout",
                "tone": "trap",
                "title": "Trap pack",
                "body": (
                    "2019 Act limits ≠ 2021 Rules · District ≠ appellate · "
                    "45 only on D→S · NCDRC ≠ constitutional body · "
                    "CCPA appeals go to National, not SC directly."
                ),
            },
            {
                "id": "cc-exam-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "“Consumer commissions are specialised quasi-judicial ADR — "
                    "a three-tier ladder that pairs accessible pecuniary thresholds with "
                    "appellate discipline up to the Supreme Court.”"
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "cc-cpa-2019"),
    (HUB_SLUG, "parent", "cc-consumer-rights"),
    (HUB_SLUG, "parent", "cc-national"),
    (HUB_SLUG, "parent", "cc-state"),
    (HUB_SLUG, "parent", "cc-district"),
    (HUB_SLUG, "parent", "cc-jurisdiction-table"),
    (HUB_SLUG, "parent", "cc-appeals-control"),
    (HUB_SLUG, "parent", "cc-exam-kit"),
    ("cc-cpa-2019", "related", "cc-national"),
    ("cc-cpa-2019", "related", "cc-state"),
    ("cc-cpa-2019", "related", "cc-district"),
    ("cc-consumer-rights", "related", "cc-national"),
    ("cc-national", "related", "cc-state"),
    ("cc-state", "related", "cc-district"),
    ("cc-jurisdiction-table", "related", "cc-district"),
    ("cc-jurisdiction-table", "related", "cc-state"),
    ("cc-jurisdiction-table", "related", "cc-national"),
    ("cc-appeals-control", "related", "cc-national"),
    ("cc-appeals-control", "related", "cc-state"),
    ("cc-exam-kit", "related", "cc-jurisdiction-table"),
    ("cc-exam-kit", "related", "cc-appeals-control"),
    ("cc-exam-kit", "related", "cc-national"),
]

SAMPLE_PYQS = [
    (
        2021,
        (
            "With reference to the Consumer Protection Act, 2019, consider the following statements:\n"
            "1. The District Commission has jurisdiction to entertain complaints where the value of "
            "goods or services paid as consideration does not exceed ₹1 crore under the 2021 Rules.\n"
            "2. An appeal against the order of a District Commission lies to the State Commission "
            "within 45 days.\n"
            "Which of the statements given above is/are correct?"
        ),
        "2 only — under the 2021 Jurisdiction Rules the District ceiling is ₹50 lakh (not ₹1 crore); "
        "the 45-day District→State appeal window is correct.",
        ["cc-jurisdiction-table", "cc-district", "cc-appeals-control", "cc-exam-kit"],
    ),
    (
        2020,
        (
            "Which of the following are correctly matched?\n"
            "1. District Consumer Commission — established by the state government\n"
            "2. National Consumer Commission — established by the central government\n"
            "3. Appeal from the National Commission — lies to the High Court\n"
            "Select the correct answer using the code given below."
        ),
        "1 and 2 only — appeal from the National Commission lies to the Supreme Court (within 30 days), "
        "not the High Court.",
        ["cc-cpa-2019", "cc-national", "cc-appeals-control", "cc-exam-kit"],
    ),
    (
        2022,
        (
            "Consider the following statements about the National Consumer Disputes Redressal Commission:\n"
            "1. It shall consist of a President and not less than four members.\n"
            "2. At least one member shall be a woman.\n"
            "3. A person below 50 years of age is eligible to be appointed as President.\n"
            "Which of the statements given above are correct?"
        ),
        "1 and 2 only — minimum age for President or member is 50 years (not eligible below 50).",
        ["cc-national", "cc-exam-kit"],
    ),
    (
        2019,
        (
            "The Central Consumer Protection Authority (CCPA) is associated with which of the following?\n"
            "1. Protection of consumer rights\n"
            "2. Appeal against its orders lies to the National Commission within 30 days\n"
            "3. It replaces the three-tier consumer commissions under CPA 2019\n"
            "Select the correct answer."
        ),
        "1 and 2 only — CCPA is a regulator; it does not replace the District/State/National commissions. "
        "Appeals from CCPA go to the National Commission within 30 days.",
        ["cc-consumer-rights", "cc-national", "cc-exam-kit"],
    ),
]


class Command(BaseCommand):
    help = "Seed Consumer Commissions chapter (Laxmikanth Ch.37)."

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
                "title": "Consumer Commissions",
                "sort_order": 8,
                "book_ref": "Laxmikanth 8th Ed, Ch. 37",
                "summary": (
                    "Visual revision of Ch.37 — CPA 2019, District/State/National commissions, "
                    "pecuniary jurisdiction, appeals, and consumer rights."
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
                "title": "Consumer Commissions",
                "summary": (
                    "Three-tier quasi-judicial consumer forums under CPA 2019 — "
                    "District, State, and National Commissions."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **three-tier ladder** mental model, then "
                    "**CPA 2019** → **Rights/CCPA** → **District** → **State** → **National** → "
                    "**Table 37.1** → **Appeals**. Finish with the **Exam kit**. "
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
            ref="Laxmikanth Ch. 37",
            excerpt=(
                "Consumer Commissions — CPA 2019, District/State/National forums, "
                "jurisdiction, appeals, and administrative control."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="CPA 2019",
            excerpt="Three-tier consumer dispute redressal machinery replacing the 1986 Act.",
            sort_order=1,
        )

        cc_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=cc_slugs, source__subject=subject
        ).filter(target__slug__in=cc_slugs).delete()

        created_edges = 0
        for src, rel, tgt in EDGES:
            source = by_slug.get(src)
            target = by_slug.get(tgt)
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
            concepts = [by_slug[s] for s in slugs if s in by_slug]
            if concepts:
                existing = list(pyq.concepts.all())
                pyq.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Consumer Commissions chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
