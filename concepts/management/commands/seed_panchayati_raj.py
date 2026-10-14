"""Seed Laxmikanth Ch.39 Panchayati Raj (visual revision — Part V Local Government)."""

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

HUB_SLUG = "panchayati-raj"
CHAPTER_SLUG = "panchayati-raj"

ENTRY_PILLARS = [
    {
        "id": "place",
        "articles": "Art. 40 · State List",
        "label": "Meaning & place",
        "slug": "pr-meaning-place",
        "detail": "Rural local self-government; state subject; Art. 40 → Part IX.",
        "tone": "teal",
    },
    {
        "id": "evol",
        "articles": "1952–1993",
        "label": "Evolution timeline",
        "slug": "pr-evolution-timeline",
        "detail": "CDP → Balwant Rai → Nagaur 1959 → 73rd (24 Apr 1993).",
        "tone": "olive",
    },
    {
        "id": "brm",
        "articles": "1957",
        "label": "Balwant Rai Mehta",
        "slug": "pr-balwant-rai",
        "detail": "Democratic decentralisation; 3-tier; PS executive; ZP advisory.",
        "tone": "gold",
    },
    {
        "id": "am",
        "articles": "1977–78",
        "label": "Ashok Mehta",
        "slug": "pr-ashok-mehta",
        "detail": "2-tier (ZP + mandal); district pivot; party polls; constitutional status.",
        "tone": "orange",
    },
    {
        "id": "later",
        "articles": "1985–88",
        "label": "Later committees",
        "slug": "pr-later-committees",
        "detail": "GVK Rao · Singhvi · Thungon · Gadgil (73rd blueprint).",
        "tone": "terracotta",
    },
    {
        "id": "path",
        "articles": "64th → 73rd",
        "label": "Constitutionalisation",
        "slug": "pr-constitutionalisation",
        "detail": "Rajiv bill failed RS; VP Singh lapsed; Rao → 73rd CAA.",
        "tone": "maroon",
    },
    {
        "id": "arch",
        "articles": "Part IX",
        "label": "73rd architecture",
        "slug": "pr-73rd-architecture",
        "detail": "Arts 243–243O; 11th Schedule (29); justiciable PRIs.",
        "tone": "teal",
    },
    {
        "id": "struct",
        "articles": "243A–C",
        "label": "Structure & elections",
        "slug": "pr-structure-elections",
        "detail": "Gram Sabha; 3-tier; direct members; skip intermediate ≤20 lakh.",
        "tone": "olive",
    },
    {
        "id": "res",
        "articles": "243D–F",
        "label": "Reservation & duration",
        "slug": "pr-reservation-duration",
        "detail": "SC/ST · ≥1/3 women · 5 yrs / 6 months · age 21.",
        "tone": "gold",
    },
    {
        "id": "inst",
        "articles": "243G–K",
        "label": "SEC · SFC · finances",
        "slug": "pr-sec-sfc-finances",
        "detail": "SEC removal ≈ HC judge; SFC every 5 yrs; 243H may-powers.",
        "tone": "orange",
    },
    {
        "id": "cv",
        "articles": "Mandatory vs optional",
        "label": "Compulsory vs voluntary",
        "slug": "pr-compulsory-voluntary",
        "detail": "Structure compulsory; depth of 3Fs voluntary → uneven devolution.",
        "tone": "terracotta",
    },
    {
        "id": "sch11",
        "articles": "11th Schedule",
        "label": "Eleventh Schedule",
        "slug": "pr-eleventh-schedule",
        "detail": "29 functional items via Art. 243G — A-LIFE mnemonic.",
        "tone": "maroon",
    },
    {
        "id": "pesa",
        "articles": "PESA 1996",
        "label": "PESA Act",
        "slug": "pr-pesa",
        "detail": "Fifth Schedule extension; GS nucleus; 10 states; ST chairs.",
        "tone": "teal",
    },
    {
        "id": "3fs",
        "articles": "2nd ARC",
        "label": "Finances & problems",
        "slug": "pr-finances-problems",
        "detail": "3Fs gap; tied funds; parallel bodies; weak own tax.",
        "tone": "olive",
    },
    {
        "id": "cmp",
        "articles": "73rd vs 74th",
        "label": "PR vs Municipalities",
        "slug": "pr-vs-municipalities-revision",
        "detail": "Part IX / IX-A; 11th / 12th; one-page quick revision.",
        "tone": "gold",
    },
    {
        "id": "exam",
        "articles": "PYQ kit",
        "label": "Exam kit",
        "slug": "pr-exam-kit",
        "detail": "Prelims traps, PYQ themes, cases, e-Gram Swaraj VA.",
        "tone": "orange",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pr-roof-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Grassroots republic",
        "topic_label": "Panchayati Raj",
        "subject_label": "Part IX · Arts 243–243O",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating PRIs as optional state charity",
            "Mixing 73rd (rural) with 74th (urban)",
            "Confusing SEC with the Election Commission of India",
            "Assuming 3Fs depth is as compulsory as the 3-tier structure",
        ],
        "insight": (
            "The 73rd Amendment made rural local self-government justiciable — "
            "elections, tenure, and reservation no longer depend on state whim."
        ),
    },
    {
        "id": "pr-entry-pillars",
        "type": "pillars",
        "title": "Sixteen revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "pr-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor · BAGS-TG",
        "body": (
            "Path: Committees → 73rd architecture → 3-tier + Gram Sabha → SEC/SFC → "
            "Compulsory vs Voluntary → PESA → Exam kit. "
            "Mnemonic BAGS-TG: Balwant Rai · Ashok Mehta · GVK Rao · Singhvi · "
            "Thungon · Gadgil (path to constitutionalisation)."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Meaning & Constitutional Place",
        "slug": "pr-meaning-place",
        "sort_order": 1,
        "summary": (
            "Rural local self-government for grass-root democracy and rural development; "
            "State List entry 5; Art. 40 DPSP made real by the 73rd Amendment."
        ),
        "body": (
            "## What it is\n\n"
            "**Panchayati Raj** = system of **rural local self-government**, set up by "
            "state Acts to build democracy at the grass-root level and drive rural development. "
            "Constitutionalised by the **73rd Constitutional Amendment Act, 1992**.\n\n"
            "### Federal place\n"
            "- **Local government** is a **state subject** — State List, Seventh Schedule, "
            "**entry 5**.\n"
            "- States create PRIs by legislation; the Centre cannot run a parallel rural "
            "local-government system in the ordinary federal division.\n\n"
            "### Constitutional bridge\n"
            "- **Art. 40** (DPSP): organise village panchayats and endow them with powers "
            "to function as units of self-government.\n"
            "- The **73rd Amendment** gave Art. 40 a **practical, justiciable shape** via "
            "Part IX — states are under constitutional obligation to adopt the new system."
        ),
        "articles": [
            ("Art. 40", "Organisation of village panchayats (DPSP)."),
            (
                "State List entry 5",
                "Local government — including rural local bodies — is a state subject.",
            ),
            ("73rd Amendment", "Constitutionalised Panchayati Raj (Part IX)."),
        ],
        "visual_blocks": [
            {
                "id": "pr-place-tree",
                "type": "tree",
                "title": "Three-tier polity",
                "root": {
                    "id": "union",
                    "label": "Union",
                    "detail": "Centre",
                    "children": [
                        {
                            "id": "state",
                            "label": "State",
                            "detail": "Local govt = State List entry 5",
                            "children": [
                                {
                                    "id": "local",
                                    "label": "Local (PRIs)",
                                    "slug": "panchayati-raj",
                                    "detail": "Part IX · rural third tier",
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "id": "pr-place-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Art. 40 → Part IX",
                "body": (
                    "Art. 40 was only a Directive Principle until the 73rd Amendment "
                    "put PRIs into the justiciable Part IX of the Constitution."
                ),
            },
        ],
    },
    {
        "title": "Evolution Timeline",
        "slug": "pr-evolution-timeline",
        "sort_order": 2,
        "summary": (
            "From Community Development (1952) and Balwant Rai (1957) through Nagaur "
            "inauguration (1959) to the 73rd Amendment (24 April 1993) and PESA (1996)."
        ),
        "body": (
            "## Arc in one glance\n\n"
            "1. **1952–53:** Community Development Programme + National Extension Service.\n"
            "2. **1957:** Balwant Rai Mehta → **democratic decentralisation** (Panchayati Raj).\n"
            "3. **1958:** NDC accepts recommendations (states free on pattern).\n"
            "4. **2 Oct 1959:** **Rajasthan** first — inaugurated at **Nagaur**; Andhra Pradesh follows.\n"
            "5. **Mid-1960s:** Most states create PRIs, but **tiers/tenure/powers differ** "
            "(RJ 3-tier; TN 2-tier; WB 4-tier; RJ–AP block-strong vs MH–GJ district-strong).\n"
            "6. **1970s–80s:** Decline + reform committees (Ashok Mehta → Gadgil).\n"
            "7. **1992–93:** **73rd CAA**; in force **24 April 1993**.\n"
            "8. **1996:** **PESA** extends Part IX logic to Fifth Schedule areas.\n\n"
            "### Pattern note\n"
            "Some states also set up **nyaya panchayats** for petty civil/criminal cases."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pr-evol-timeline",
                "type": "timeline",
                "title": "From CDP to PESA",
                "events": [
                    {
                        "id": "e1",
                        "year": 1952,
                        "label": "CDP launched",
                        "detail": "Community Development Programme; NES follows 1953.",
                    },
                    {
                        "id": "e2",
                        "year": 1957,
                        "label": "Balwant Rai Mehta",
                        "detail": "Democratic decentralisation → Panchayati Raj idea.",
                    },
                    {
                        "id": "e3",
                        "year": 1959,
                        "label": "Nagaur inauguration",
                        "detail": "Rajasthan first (2 Oct); Andhra Pradesh same year.",
                    },
                    {
                        "id": "e4",
                        "year": 1978,
                        "label": "Ashok Mehta Report",
                        "detail": "2-tier revival blueprint; constitutional recognition urged.",
                    },
                    {
                        "id": "e5",
                        "year": 1988,
                        "label": "Gadgil blueprint",
                        "detail": "Draft base for constitutional status + SEC/SFC.",
                    },
                    {
                        "id": "e6",
                        "year": 1993,
                        "label": "73rd in force",
                        "detail": "24 April 1993 — National Panchayat Day.",
                    },
                    {
                        "id": "e7",
                        "year": 1996,
                        "label": "PESA Act",
                        "detail": "Extension of Part IX to Fifth Schedule areas.",
                    },
                ],
            },
            {
                "id": "pr-evol-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchors",
                "body": (
                    "Rajasthan = first state · Nagaur · 2 Oct 1959 · "
                    "National Panchayat Day = **24 April** (73rd commencement)."
                ),
            },
        ],
    },
    {
        "title": "Balwant Rai Mehta Committee",
        "slug": "pr-balwant-rai",
        "sort_order": 3,
        "summary": (
            "1957 committee on CDP/NES; recommended three-tier democratic decentralisation "
            "with panchayat samiti as the executive body."
        ),
        "body": (
            "## Why appointed\n\n"
            "Jan 1957 — examine **Community Development Programme (1952)** and "
            "**National Extension Service (1953)**. Chair: **Balwantrai G. Mehta**. "
            "Report: **Nov 1957**.\n\n"
            "### Core recommendations\n"
            "1. **Three-tier** PR — gram panchayat (village), panchayat samiti (block), "
            "zila parishad (district), **organically linked** via **indirect** elections.\n"
            "2. Village panchayat = **directly** elected; samiti & parishad = **indirect**.\n"
            "3. All planning & development entrusted to these bodies.\n"
            "4. **Panchayat samiti = executive**; **zila parishad = advisory / coordinating / "
            "supervisory**.\n"
            "5. **District Collector = chairman** of zila parishad.\n"
            "6. Genuine transfer of power + adequate resources; further devolution over time.\n\n"
            "### Aftermath\n"
            "NDC accepted (Jan 1958) but left **pattern to states** — only broad fundamentals "
            "to be common."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pr-brm-tree",
                "type": "tree",
                "title": "Balwant Rai 3-tier",
                "root": {
                    "id": "zp",
                    "label": "Zila Parishad",
                    "detail": "Advisory · Collector as chair",
                    "children": [
                        {
                            "id": "ps",
                            "label": "Panchayat Samiti",
                            "detail": "Executive body (block)",
                            "children": [
                                {
                                    "id": "gp",
                                    "label": "Gram Panchayat",
                                    "detail": "Directly elected village tier",
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "id": "pr-brm-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory hook",
                "body": (
                    "Balwant Rai = **3-tier + samiti executive + Collector chairs ZP**. "
                    "This is the classic ‘democratic decentralisation’ origin story."
                ),
            },
        ],
    },
    {
        "title": "Ashok Mehta Committee",
        "slug": "pr-ashok-mehta",
        "sort_order": 4,
        "summary": (
            "1977–78 Janata-era committee; 132 recommendations to revive PRIs — "
            "two-tier system with zila parishad as the executive pivot."
        ),
        "body": (
            "## Why appointed\n\n"
            "Dec 1977 (Janata Government) — revive declining PRIs. Chair: **Ashok Mehta**. "
            "Report: **Aug 1978** (**132** recommendations).\n\n"
            "### High-yield recommendations\n"
            "1. Replace 3-tier with **2-tier**: **zila parishad** + **mandal panchayat** "
            "(group of villages, pop. ~15,000–20,000).\n"
            "2. **District** = first point of decentralisation below the state.\n"
            "3. **ZP = executive** body for district planning.\n"
            "4. **Official participation of political parties** in panchayat elections.\n"
            "5. **Compulsory taxation** powers for own resources.\n"
            "6. Regular **social audit** (district agency + legislators’ committee).\n"
            "7. No supersession; if imperative → elections within **6 months**.\n"
            "8. **Nyaya panchayats** separate from development panchayats; qualified judge as chair.\n"
            "9. Elections via chief electoral officer + CEC consultation.\n"
            "10. Development functions + staff under ZP; voluntary agencies; state PRI minister.\n"
            "11. SC/ST reservation by population; **constitutional recognition** of PRIs.\n\n"
            "### Aftermath\n"
            "Janata Government collapsed → **no central action**. Karnataka, West Bengal, "
            "Andhra Pradesh experimented with some ideas."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pr-am-compare",
                "type": "comparison",
                "title": "Balwant Rai vs Ashok Mehta",
                "columns": [
                    {
                        "id": "brm",
                        "heading": "Balwant Rai (1957)",
                        "points": [
                            "3-tier (GP–PS–ZP)",
                            "PS = executive; ZP = advisory",
                            "Collector chairs ZP",
                            "Indirect link across tiers",
                            "No formal party role stressed",
                        ],
                    },
                    {
                        "id": "am",
                        "heading": "Ashok Mehta (1978)",
                        "points": [
                            "2-tier (ZP + mandal)",
                            "ZP = executive pivot",
                            "District = first decentralisation point",
                            "Open party participation",
                            "Compulsory tax + constitutional status",
                        ],
                    },
                ],
            },
            {
                "id": "pr-am-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Ashok Mehta recommended **two tiers**, not three. "
                    "Do not mix with Balwant Rai’s classic three-tier model."
                ),
            },
        ],
    },
    {
        "title": "GVK Rao · Singhvi · Thungon · Gadgil",
        "slug": "pr-later-committees",
        "sort_order": 5,
        "summary": (
            "Four late-1980s committees that shifted the debate from revival to "
            "constitutional status — Gadgil became the drafting base for the 73rd Amendment."
        ),
        "body": (
            "## Four revision cards\n\n"
            "### G.V.K. Rao (1985)\n"
            "Planning Commission committee on rural development admin. Diagnosis: "
            "**‘grass without roots’** — development bureaucratised, PRIs weakened.\n"
            "- **ZP pivotal** for planning & development.\n"
            "- PRIs role in planning, implementation, monitoring.\n"
            "- Transfer some state planning functions to district units.\n"
            "- **District Development Commissioner** as CEO of ZP (all development depts).\n"
            "- Regular elections (overdue in 11 states).\n"
            "- Differed from Dantwala / Hanumantha Rao models that kept Collector-centric planning.\n\n"
            "### L.M. Singhvi (1986)\n"
            "Concept paper on revitalisation for democracy & development.\n"
            "- **Constitutional recognition** + new constitutional chapter; free & fair elections.\n"
            "- Nyaya panchayats for village clusters.\n"
            "- Reorganise villages for viable GPs; **Gram Sabha = embodiment of direct democracy**.\n"
            "- More village financial resources; **judicial tribunals** for election/dissolution disputes.\n\n"
            "### P.K. Thungon (1988)\n"
            "Parliamentary consultative sub-committee on district political-admin structure.\n"
            "- Constitutional recognition; **3-tier**; ZP as planning & development pivot.\n"
            "- Fixed **5-year** tenure; max supersession **6 months**.\n"
            "- State planning-coordination committee (planning minister + ZP presidents).\n"
            "- **Subject list in Constitution**; reservation by population + **women**.\n"
            "- **State Finance Commission**; Collector as **CEO** of ZP.\n\n"
            "### V.N. Gadgil (1988)\n"
            "Congress Policy & Programmes committee — **how to make PRIs effective**.\n"
            "- Constitutional status; 3-tier; 5-year term; **direct election** of all members.\n"
            "- Reservation for SCs, STs, women; socio-economic planning + subject list.\n"
            "- Tax/duty powers; **SFC** + **SEC**.\n"
            "- **Became the basis for drafting the amendment bill** that led to the 73rd CAA."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pr-later-pillars",
                "type": "pillars",
                "title": "Four committees → one destination",
                "items": [
                    {
                        "id": "gvk",
                        "articles": "1985",
                        "label": "G.V.K. Rao",
                        "slug": "pr-later-committees",
                        "detail": "Grass without roots · ZP pivotal · DDC as CEO.",
                        "tone": "teal",
                    },
                    {
                        "id": "lms",
                        "articles": "1986",
                        "label": "L.M. Singhvi",
                        "slug": "pr-later-committees",
                        "detail": "Constitutional chapter · Gram Sabha = direct democracy.",
                        "tone": "olive",
                    },
                    {
                        "id": "pkt",
                        "articles": "1988",
                        "label": "P.K. Thungon",
                        "slug": "pr-later-committees",
                        "detail": "5 yrs · SFC · subject list · women reservation.",
                        "tone": "gold",
                    },
                    {
                        "id": "vng",
                        "articles": "1988",
                        "label": "V.N. Gadgil",
                        "slug": "pr-later-committees",
                        "detail": "SEC + SFC + direct elections = 73rd blueprint.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pr-later-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Blueprint memory",
                "body": (
                    "**Gadgil = drafting base for the 73rd Amendment.** "
                    "Singhvi first pushed a full constitutional chapter + Gram Sabha as direct democracy."
                ),
            },
        ],
    },
    {
        "title": "Path to Constitutionalisation",
        "slug": "pr-constitutionalisation",
        "sort_order": 6,
        "summary": (
            "Three governments tried: Rajiv’s 64th Bill failed in Rajya Sabha; "
            "V.P. Singh’s bill lapsed; Narasimha Rao’s modified bill became the 73rd CAA."
        ),
        "body": (
            "## Three attempts\n\n"
            "### Rajiv Gandhi Government\n"
            "- **64th Constitutional Amendment Bill** (July 1989) to constitutionalise PRIs.\n"
            "- Lok Sabha passed (Aug 1989); **Rajya Sabha did not approve**.\n"
            "- Opposition charge: bill would **strengthen centralisation** in the federal system.\n\n"
            "### V.P. Singh Government\n"
            "- Nov 1989 National Front — promise to strengthen PRIs.\n"
            "- June 1990 CMs’ conference approved a fresh amendment.\n"
            "- Bill introduced Sept 1990 → **government fell → bill lapsed**.\n\n"
            "### P.V. Narasimha Rao Government\n"
            "- Modified proposals (controversial bits dropped).\n"
            "- Bill introduced Sept 1991 → **73rd Constitutional Amendment Act, 1992**.\n"
            "- Came into force **24 April 1993**.\n\n"
            "### Passage snapshot\n"
            "LS **22 Dec 1992** · RS **23 Dec 1992** · 17 state assemblies · "
            "President assent **20 April 1993**."
        ),
        "articles": [
            ("73rd Amendment", "Constitutional status for Panchayats — in force 24 April 1993."),
        ],
        "visual_blocks": [
            {
                "id": "pr-path-flow",
                "type": "flowchart",
                "title": "Three governments → 73rd",
                "root": "rajiv",
                "steps": [
                    {
                        "id": "rajiv",
                        "label": "Rajiv · 64th Bill (1989)",
                        "detail": "LS passed; RS rejected (centralisation charge).",
                        "options": [
                            {"label": "Next government", "next": "vp"},
                        ],
                    },
                    {
                        "id": "vp",
                        "label": "V.P. Singh · 1990 bill",
                        "detail": "Introduced after CMs’ conference; government fell → lapsed.",
                        "options": [
                            {"label": "Next government", "next": "rao"},
                        ],
                    },
                    {
                        "id": "rao",
                        "label": "Narasimha Rao · modified bill",
                        "detail": "Controversial parts dropped → 73rd CAA 1992.",
                        "options": [
                            {"label": "Commencement", "next": "force"},
                        ],
                    },
                    {
                        "id": "force",
                        "label": "In force 24 April 1993",
                        "detail": "National Panchayat Day.",
                    },
                ],
            },
            {
                "id": "pr-path-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Date pack",
                "body": (
                    "LS 22 Dec 1992 · RS 23 Dec 1992 · assent 20 Apr 1993 · "
                    "force **24 Apr 1993**."
                ),
            },
        ],
    },
    {
        "title": "73rd Architecture",
        "slug": "pr-73rd-architecture",
        "sort_order": 7,
        "summary": (
            "Part IX ‘The Panchayats’ (Arts 243–243O) plus the Eleventh Schedule "
            "(29 items under Art. 243G); shifts representative democracy toward participatory democracy."
        ),
        "body": (
            "## What the Act added\n\n"
            "- New **Part IX** — **‘The Panchayats’** — Arts **243 to 243-O**.\n"
            "- New **Eleventh Schedule** — **29** functional items (via **Art. 243-G**).\n"
            "- Gives practical shape to **Art. 40** (DPSP).\n\n"
            "### Significance\n"
            "- Constitutional **status** for PRIs → under the **justiciable** part of the Constitution.\n"
            "- Neither formation of panchayats nor regular elections now depend on state whim.\n"
            "- Provisions = **compulsory** (must be in state law) + **voluntary** (state discretion "
            "for local geography/politics).\n"
            "- Landmark shift: **representative → participatory** grass-root democracy.\n\n"
            "### Pair memory\n"
            "- **11th Schedule** = panchayats (rural) · **12th Schedule** = municipalities (urban)."
        ),
        "articles": [
            ("Part IX", "The Panchayats — Arts 243–243O."),
            ("Art. 243G", "Powers, authority and responsibilities of panchayats."),
            ("Eleventh Schedule", "29 functional items of panchayats."),
            ("Art. 40", "DPSP on village panchayats — given practical shape."),
        ],
        "visual_blocks": [
            {
                "id": "pr-arch-tree",
                "type": "tree",
                "title": "Part IX spine",
                "root": {
                    "id": "part9",
                    "label": "Part IX · The Panchayats",
                    "detail": "Arts 243–243O",
                    "children": [
                        {
                            "id": "struct",
                            "label": "243A–C Structure",
                            "detail": "Gram Sabha · constitution · composition",
                            "children": [
                                {
                                    "id": "res",
                                    "label": "243D–F",
                                    "detail": "Reservation · duration · disqualification",
                                }
                            ],
                        },
                        {
                            "id": "power",
                            "label": "243G–J Powers & money",
                            "detail": "Functions · taxes · SFC · audit",
                            "children": [
                                {
                                    "id": "elec",
                                    "label": "243K–O",
                                    "detail": "SEC · UTs · exemptions · bar on courts",
                                }
                            ],
                        },
                        {
                            "id": "sch",
                            "label": "11th Schedule",
                            "slug": "pr-eleventh-schedule",
                            "detail": "29 items via 243G",
                        },
                    ],
                },
            },
            {
                "id": "pr-arch-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Schedule pair",
                "body": (
                    "Eleventh Schedule = **rural** (29) · Twelfth Schedule = **urban** (18). "
                    "Do not swap them in prelims."
                ),
            },
        ],
    },
    {
        "title": "Gram Sabha & Three-Tier",
        "slug": "pr-structure-elections",
        "sort_order": 8,
        "summary": (
            "Gram Sabha as foundation; uniform three-tier PRIs; direct election of all members; "
            "indirect chairs at intermediate and district levels."
        ),
        "body": (
            "## Gram Sabha (243A)\n\n"
            "Foundation of the system — village assembly of **all registered voters** in the "
            "panchayat area. Powers/functions as the **state legislature** determines.\n\n"
            "## Three-tier system (243B)\n\n"
            "Panchayats at **village, intermediate, and district** levels — brings structural "
            "uniformity. Exception: a state with population **not exceeding 20 lakh** may "
            "**skip the intermediate** level.\n\n"
            "### Definitions (Act)\n"
            "- **Panchayat** — institution of self-government for rural areas (any name).\n"
            "- **Village** — as specified by the Governor (may include a group of villages).\n"
            "- **Intermediate level** — between village and district, specified by Governor.\n\n"
            "## Elections (243C)\n\n"
            "- **All members** at all three levels = **directly** elected.\n"
            "- Chairperson at **intermediate & district** = **indirectly** elected from among "
            "elected members.\n"
            "- Village chairperson = manner as **state legislature** decides.\n"
            "- Chairperson + directly/indirectly elected members have **voting rights** in meetings."
        ),
        "articles": [
            ("Art. 243A", "Gram Sabha."),
            ("Art. 243B", "Constitution of panchayats (three tiers)."),
            ("Art. 243C", "Composition of panchayats."),
        ],
        "visual_blocks": [
            {
                "id": "pr-struct-tree",
                "type": "tree",
                "title": "Gram Sabha → three tiers",
                "root": {
                    "id": "gs",
                    "label": "Gram Sabha",
                    "detail": "All registered voters · foundation",
                    "children": [
                        {
                            "id": "gp",
                            "label": "Village Panchayat",
                            "detail": "Direct members · chair as state decides",
                            "children": [
                                {
                                    "id": "ps",
                                    "label": "Intermediate (Samiti)",
                                    "detail": "May skip if pop ≤ 20 lakh",
                                    "children": [
                                        {
                                            "id": "zp",
                                            "label": "District (Zila Parishad)",
                                            "detail": "Indirect chair from members",
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "id": "pr-struct-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Election traps",
                "body": (
                    "Members = **direct** at all levels. Village sarpanch is **not** always "
                    "directly elected — state decides. Age to contest = **21**, not 25 (MLA floor)."
                ),
            },
        ],
    },
    {
        "title": "Reservation · Duration · Disqualification",
        "slug": "pr-reservation-duration",
        "sort_order": 9,
        "summary": (
            "SC/ST and women reservation at all tiers; optional OBC reservation; "
            "five-year tenure with six-month election rule; minimum contesting age 21."
        ),
        "body": (
            "## Reservation (243D)\n\n"
            "- **SC/ST seats** in every panchayat ∝ population share; also reservation of "
            "**chairperson offices** at village or any level for SCs/STs (by state law).\n"
            "- **Women ≥ one-third** of total seats (including women within SC/ST seats) and "
            "**≥ one-third of chairperson offices** at each level.\n"
            "- **OBC** reservation (seats or chairs) = **state option**.\n"
            "- SC/ST seat & chair reservations cease after Art. **334** period "
            "(book: presently **eighty years / till 2030**).\n"
            "- **83rd Amendment (2000):** SC seat reservation **not applicable to Arunachal Pradesh** "
            "(wholly tribal; no SCs).\n\n"
            "## Duration (243E)\n\n"
            "- Term = **5 years** from first meeting; can be dissolved earlier.\n"
            "- Fresh elections: before 5-year expiry **or** within **6 months** of dissolution.\n"
            "- If remainder period **< 6 months** → election for that remainder **not necessary**.\n"
            "- PRI reconstituted after premature dissolution continues only for the **remainder** "
            "of the original term (not a fresh full 5 years).\n\n"
            "## Disqualification (243F)\n\n"
            "- Same grounds as for state legislature elections, or as state law provides.\n"
            "- **Cannot** be disqualified only for being under 25 if age is **≥ 21**.\n"
            "- Disqualification questions → authority decided by state legislature."
        ),
        "articles": [
            ("Art. 243D", "Reservation of seats."),
            ("Art. 243E", "Duration of panchayats."),
            ("Art. 243F", "Disqualifications for membership."),
            ("83rd Amendment", "SC reservation in panchayats not applicable to Arunachal Pradesh."),
        ],
        "visual_blocks": [
            {
                "id": "pr-res-pillars",
                "type": "pillars",
                "title": "Four revision blocks",
                "items": [
                    {
                        "id": "scst",
                        "articles": "243D",
                        "label": "SC / ST",
                        "slug": "pr-reservation-duration",
                        "detail": "Seats + chairs ∝ population; Art. 334 sunset.",
                        "tone": "teal",
                    },
                    {
                        "id": "women",
                        "articles": "≥ 1/3",
                        "label": "Women",
                        "slug": "pr-reservation-duration",
                        "detail": "Seats and chair offices at every level.",
                        "tone": "olive",
                    },
                    {
                        "id": "obc",
                        "articles": "Optional",
                        "label": "OBC",
                        "slug": "pr-reservation-duration",
                        "detail": "State may provide — not a compulsory feature.",
                        "tone": "gold",
                    },
                    {
                        "id": "dur",
                        "articles": "243E–F",
                        "label": "Duration & DQ",
                        "slug": "pr-reservation-duration",
                        "detail": "5 yrs · 6 months · remainder rule · age 21.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pr-res-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Trap pack",
                "body": (
                    "Reconstituted after dissolution ≠ full 5 years (remainder only). "
                    "Arunachal SC-seat exception = **83rd Amendment**. Women floor = "
                    "**not less than one-third**, including chairs."
                ),
            },
        ],
    },
    {
        "title": "SEC · SFC · Powers · Finances",
        "slug": "pr-sec-sfc-finances",
        "sort_order": 10,
        "summary": (
            "State Election Commission and State Finance Commission as institutional spine; "
            "243G–H devolution and tax powers; audit, UT application, and bar on courts."
        ),
        "body": (
            "## State Election Commission (243K)\n\n"
            "- Superintendence, direction, control of **electoral rolls** and **all panchayat elections**.\n"
            "- State Election Commissioner appointed by the **Governor**.\n"
            "- Conditions of service / tenure fixed by Governor; **cannot be varied to disadvantage** "
            "after appointment.\n"
            "- **Removal** only in the manner and on grounds for a **High Court judge** "
            "(Parliament address → President) — **Governor cannot remove** though he/she appoints.\n"
            "- State legislature may legislate on election matters.\n\n"
            "## Powers & functions (243G)\n\n"
            "State may endow PRIs as institutions of self-government — devolution for:\n"
            "- Plans for **economic development and social justice**.\n"
            "- Implementation of schemes, including **11th Schedule** matters.\n\n"
            "## Finances (243H)\n\n"
            "State legislature **may**: authorise levy/collect/appropriate taxes/duties/tolls/fees; "
            "assign state-levied taxes; grants-in-aid from state Consolidated Fund; constitute "
            "panchayat funds.\n\n"
            "## State Finance Commission (243I)\n\n"
            "- Governor constitutes **every five years**.\n"
            "- Recommends: distribution of net proceeds (state ↔ panchayats + among tiers); "
            "taxes that may be assigned; grants-in-aid; measures to improve finances; other "
            "Governor-referred matters.\n"
            "- Composition/qualifications/selection = state law.\n"
            "- Recommendations + **action-taken report** → state legislature.\n"
            "- **Central Finance Commission** also suggests measures to augment state CF to "
            "supplement PRI resources (Art. **280** link).\n\n"
            "## Other\n"
            "- **243J** audit of accounts · **243L** apply to UTs (President may modify) · "
            "**243O** bar on courts in electoral matters (election petition only as state law provides)."
        ),
        "articles": [
            ("Art. 243G", "Powers, authority and responsibilities of panchayats."),
            ("Art. 243H", "Powers to impose taxes by, and funds of, the panchayats."),
            ("Art. 243-I", "State Finance Commission."),
            ("Art. 243J", "Audit of accounts of panchayats."),
            ("Art. 243K", "Elections to the panchayats (State Election Commission)."),
            ("Art. 243O", "Bar to interference by courts in electoral matters."),
        ],
        "visual_blocks": [
            {
                "id": "pr-sec-compare",
                "type": "comparison",
                "title": "SEC vs Election Commission of India",
                "columns": [
                    {
                        "id": "sec",
                        "heading": "State Election Commission",
                        "points": [
                            "Panchayat (and municipal) elections",
                            "Appointed by Governor",
                            "Removal like HC judge (not by Governor)",
                            "Art. 243K (also 243ZA for municipalities)",
                        ],
                    },
                    {
                        "id": "eci",
                        "heading": "Election Commission of India",
                        "points": [
                            "Parliament / state legislature / President / VP",
                            "Appointed by President",
                            "Removal like SC judge (CEC)",
                            "Art. 324",
                        ],
                    },
                ],
            },
            {
                "id": "pr-sec-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Removal trap",
                "body": (
                    "SEC is appointed by the Governor but **cannot be removed by the Governor** — "
                    "removal follows the High Court judge path."
                ),
            },
        ],
    },
    {
        "title": "Compulsory vs Voluntary Provisions",
        "slug": "pr-compulsory-voluntary",
        "sort_order": 11,
        "summary": (
            "Eleven compulsory features create the skeleton of Part IX; twelve voluntary "
            "features decide how much real power and money states actually devolve."
        ),
        "body": (
            "## Why this split matters\n\n"
            "**Compulsory** provisions must appear in state PRI laws. **Voluntary** provisions "
            "let states adapt to geography and politics — and explain why **3Fs depth varies** "
            "across India even though the **structure** looks uniform.\n\n"
            "### Compulsory (11) — structure & democracy\n"
            "1. Organise Gram Sabha.\n"
            "2. Establish village / intermediate / district panchayats.\n"
            "3. Direct elections to all seats at all levels.\n"
            "4. Indirect election of chairs at intermediate & district levels.\n"
            "5. Voting rights of chair + members.\n"
            "6. Minimum age **21** to contest.\n"
            "7. SC/ST reservation (members + chairs) at all levels.\n"
            "8. Women ≥ 1/3 (members + chairs) at all levels.\n"
            "9. 5-year tenure + elections within 6 months of supersession.\n"
            "10. State Election Commission.\n"
            "11. State Finance Commission every 5 years.\n\n"
            "### Voluntary (12) — depth of self-government\n"
            "1. Endow Gram Sabha with powers/functions.\n"
            "2. Manner of electing village chairperson.\n"
            "3–5. Representation of lower chairs / MPs / MLAs in higher tiers.\n"
            "6. OBC reservation.\n"
            "7. Powers to function as autonomous self-government institutions.\n"
            "8. Devolution for plans + some/all of **29** Schedule XI functions.\n"
            "9–12. Tax powers, assigned taxes, grants-in-aid, panchayat funds."
        ),
        "articles": [
            ("Part IX", "Compulsory vs voluntary features of the 73rd Amendment."),
        ],
        "visual_blocks": [
            {
                "id": "pr-cv-compare",
                "type": "comparison",
                "title": "Compulsory vs voluntary",
                "columns": [
                    {
                        "id": "comp",
                        "heading": "Compulsory (must)",
                        "points": [
                            "Gram Sabha + 3-tier structure",
                            "Direct member elections",
                            "SC/ST + women reservation",
                            "5-year term / 6-month rule",
                            "SEC + SFC",
                            "Age 21 to contest",
                        ],
                    },
                    {
                        "id": "vol",
                        "heading": "Voluntary (may)",
                        "points": [
                            "Real Gram Sabha powers",
                            "Village chair election mode",
                            "MP/MLA / chair representation",
                            "OBC reservation",
                            "Devolution of 29 subjects",
                            "Tax / grant / fund empowerment",
                        ],
                    },
                ],
            },
            {
                "id": "pr-cv-trap",
                "type": "callout",
                "tone": "trap",
                "title": "3Fs trap",
                "body": (
                    "Three-tier structure is **compulsory**, but the depth of **functions, funds, "
                    "functionaries** is largely **voluntary** — that is why devolution is uneven."
                ),
            },
        ],
    },
    {
        "title": "Eleventh Schedule",
        "slug": "pr-eleventh-schedule",
        "sort_order": 12,
        "summary": (
            "Twenty-nine functional items within the purview of panchayats under Art. 243G — "
            "grouped for quick revision with the A-LIFE mnemonic."
        ),
        "body": (
            "## Gateway\n\n"
            "Art. **243G** + **Eleventh Schedule** = 29 matters that states **may** entrust "
            "to panchayats (voluntary depth).\n\n"
            "### A-LIFE groups (memory)\n\n"
            "**A — Agri / land / water (1–3):** agriculture & extension; land improvement/reforms/"
            "consolidation/soil conservation; minor irrigation, water management, watershed.\n\n"
            "**L — Livelihoods (4–9):** animal husbandry/dairying/poultry; fisheries; social & farm "
            "forestry; minor forest produce; SSI including food processing; khadi/village/cottage "
            "industries.\n\n"
            "**I — Infra & energy (10–16):** rural housing; drinking water; fuel & fodder; roads/"
            "bridges/ferries/waterways; rural electrification; non-conventional energy; poverty "
            "alleviation.\n\n"
            "**F — Formation of human capital (17–22):** education (primary & secondary); technical/"
            "vocational training; adult & non-formal education; libraries; cultural activities; "
            "markets & fairs.\n\n"
            "**E — Equity & essentials (23–29):** health & sanitation; family welfare; women & child "
            "development; social welfare (incl. disabled); weaker sections (esp. SC/ST); PDS; "
            "maintenance of community assets."
        ),
        "articles": [
            ("Art. 243G", "Powers and responsibilities — including 11th Schedule matters."),
            ("Eleventh Schedule", "29 functional items of panchayats."),
        ],
        "visual_blocks": [
            {
                "id": "pr-sch11-pillars",
                "type": "pillars",
                "title": "A-LIFE · 29 items in 5 groups",
                "items": [
                    {
                        "id": "a",
                        "articles": "1–3",
                        "label": "A · Agri / land / water",
                        "slug": "pr-eleventh-schedule",
                        "detail": "Agriculture, land reforms, minor irrigation & watershed.",
                        "tone": "teal",
                    },
                    {
                        "id": "l",
                        "articles": "4–9",
                        "label": "L · Livelihoods",
                        "slug": "pr-eleventh-schedule",
                        "detail": "Animal husbandry, fisheries, forestry, MFP, SSI, khadi.",
                        "tone": "olive",
                    },
                    {
                        "id": "i",
                        "articles": "10–16",
                        "label": "I · Infra & energy",
                        "slug": "pr-eleventh-schedule",
                        "detail": "Housing, water, roads, power, poverty programmes.",
                        "tone": "gold",
                    },
                    {
                        "id": "f",
                        "articles": "17–22",
                        "label": "F · Formation (human)",
                        "slug": "pr-eleventh-schedule",
                        "detail": "Schools, skills, adult ed, libraries, culture, markets.",
                        "tone": "orange",
                    },
                    {
                        "id": "e",
                        "articles": "23–29",
                        "label": "E · Equity & essentials",
                        "slug": "pr-eleventh-schedule",
                        "detail": "Health, welfare, PDS, community assets.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "pr-sch11-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic — A-LIFE",
                "body": (
                    "Agriculture–Land–Irrigation · Livelihoods · Infra · Formation (education) · "
                    "Equity (health/welfare/PDS/assets). Gateway = **Art. 243G**."
                ),
            },
        ],
    },
    {
        "title": "PESA Act 1996",
        "slug": "pr-pesa",
        "sort_order": 13,
        "summary": (
            "Provisions of the Panchayats (Extension to the Scheduled Areas) Act — "
            "extends Part IX to Fifth Schedule areas with Gram Sabha-centric tribal self-rule."
        ),
        "body": (
            "## Why PESA?\n\n"
            "Part IX does **not** automatically apply to **Fifth Schedule** areas "
            "(also exempt: Nagaland, Meghalaya, Mizoram; Manipur hill district councils; "
            "Darjeeling Gorkha Hill Council). Parliament may extend Part IX with modifications — "
            "done via **PESA / Extension Act, 1996** (assent **24 Dec 1996**).\n\n"
            "**10 Fifth Schedule states:** Andhra Pradesh, Telangana, Chhattisgarh, Gujarat, "
            "Himachal Pradesh, Jharkhand, Madhya Pradesh, Maharashtra, Odisha, Rajasthan — "
            "all enacted compliance amendments.\n\n"
            "### Objectives (scan)\n"
            "Extend Part IX with modifications · tribal self-rule · Gram Sabha as nucleus · "
            "admin consistent with traditions · safeguard customs · empower appropriate tiers · "
            "prevent higher tiers swallowing lower tiers/GS.\n\n"
            "### Features that stick\n"
            "- State PRI law in Scheduled Areas must fit customary law & community resource practices.\n"
            "- Village ≈ habitation(s)/hamlet(s) managing affairs by tradition.\n"
            "- Gram Sabha safeguards traditions, cultural identity, community resources, customary "
            "dispute resolution; approves plans before village panchayat implements; identifies "
            "poverty-programme beneficiaries; certifies fund utilisation.\n"
            "- **ST reservation ≥ one-half of seats**; **all chairperson seats at all levels for STs**.\n"
            "- Nomination of unrepresented STs at intermediate/district ≤ **1/10** of elected strength.\n"
            "- Consult GS/PRI before land acquisition & rehabilitation; minor water bodies to "
            "appropriate PRI; **mandatory recommendation** for minor-mineral licences/leases/auctions.\n"
            "- Specific endowments: intoxicants; **MFP ownership**; prevent/restore land alienation; "
            "village markets; control money-lending; social-sector institutions; local plans/TSP.\n"
            "- Higher PRI must not assume lower PRI / Gram Sabha powers; endeavour to follow "
            "**Sixth Schedule** pattern at district level in Scheduled Areas."
        ),
        "articles": [
            ("Art. 243M", "Part IX not to apply to certain areas; Parliament may extend."),
            ("PESA Act 1996", "Extension of panchayat provisions to Fifth Schedule areas."),
        ],
        "visual_blocks": [
            {
                "id": "pr-pesa-flow",
                "type": "flowchart",
                "title": "Fifth Schedule → PESA",
                "root": "exempt",
                "steps": [
                    {
                        "id": "exempt",
                        "label": "Part IX does not auto-apply",
                        "detail": "Fifth Schedule areas + listed special areas.",
                        "options": [
                            {"label": "Parliament extends", "next": "pesa"},
                        ],
                    },
                    {
                        "id": "pesa",
                        "label": "PESA Act 1996",
                        "detail": "Part IX with tribal-centric modifications.",
                        "options": [
                            {"label": "State compliance", "next": "states"},
                        ],
                    },
                    {
                        "id": "states",
                        "label": "10 Fifth Schedule states",
                        "detail": "Amend state PRI Acts · Gram Sabha as nucleus.",
                    },
                ],
            },
            {
                "id": "pr-pesa-tip",
                "type": "callout",
                "tone": "tip",
                "title": "PESA anchors",
                "body": (
                    "GS = nucleus · ST ≥ **half** seats · **all** chairs ST · minor minerals need "
                    "GS/PRI recommendation · MFP ownership + land-alienation protection."
                ),
            },
        ],
    },
    {
        "title": "Finances · 3Fs · Why Ineffective",
        "slug": "pr-finances-problems",
        "sort_order": 14,
        "summary": (
            "Second ARC funding channels and fiscal weaknesses; MoPR roadmap reasons "
            "PRIs underperform despite constitutional status — the 3Fs gap."
        ),
        "body": (
            "## Where money comes from (2nd ARC)\n\n"
            "1. Union grants via **Central Finance Commission** (Art. 280).\n"
            "2. State devolution via **State Finance Commission** (Art. 243-I).\n"
            "3. State loans / grants.\n"
            "4. Scheme-specific CSS / Additional Central Assistance.\n"
            "5. **Own** tax & non-tax revenue.\n\n"
            "### Fiscal reality\n"
            "- Own resources meagre; even progressive states (KL/KA/TN) remain grant-dependent.\n"
            "- Thin tax domain + reluctance to collect → weak internal generation.\n"
            "- Most grants are **scheme-specific** → limited discretion.\n"
            "- States’ own fiscal stress → reluctance to devolve.\n"
            "- Critical 11th Schedule sectors (education, health, water, sanitation, minor irrigation) "
            "often still run directly by the state.\n"
            "- Result: **responsibility without matching resources**.\n"
            "- **Gram Panchayats** have a real tax domain; intermediate & district tiers lean on "
            "tolls/fees/secondary non-tax sources.\n"
            "- Typical GP taxes: property/house, profession, land cess, vehicle tolls, entertainment, "
            "sanitation/water/lighting, education cess, fairs, etc.\n\n"
            "## Why performance lags (MoPR roadmap)\n\n"
            "1. **Inadequate devolution** of **3Fs** (functions, funds, functionaries); SFC "
            "recommendations often weakly implemented.\n"
            "2. **Excessive bureaucracy** — sarpanches chasing block offices for funds/approvals.\n"
            "3. **Tied funds** → unsuitable activities or under-spend.\n"
            "4. **Grant dependence** → weaker citizen demand for social audit.\n"
            "5. **Reluctance to use fiscal powers** (hard to tax neighbours).\n"
            "6. **Weak Gram Sabha** — powers/procedures/penalties unspecified in many state Acts.\n"
            "7. **Parallel bodies / missions** usurp PRI space with superior resources.\n"
            "8. **Poor infrastructure & capacity** — no full-time secretary, no office, weak data, "
            "semi-literate representatives without periodic training."
        ),
        "articles": [
            ("Art. 243H", "Tax and fund powers of panchayats."),
            ("Art. 243-I", "State Finance Commission."),
            ("Art. 280", "Central Finance Commission — augmenting state CF for PRIs."),
        ],
        "visual_blocks": [
            {
                "id": "pr-fin-flow",
                "type": "flowchart",
                "title": "Money in → weak autonomy",
                "root": "in",
                "steps": [
                    {
                        "id": "in",
                        "label": "Funds arrive",
                        "detail": "CFC · SFC · state grants · CSS · own tax.",
                        "options": [
                            {"label": "Own tax weak", "next": "weak"},
                            {"label": "Scheme-tied", "next": "tied"},
                        ],
                    },
                    {
                        "id": "weak",
                        "label": "Thin own domain",
                        "detail": "GP better than upper tiers; reluctance to levy.",
                    },
                    {
                        "id": "tied",
                        "label": "Limited discretion",
                        "detail": "3Fs incomplete · parallel bodies · responsibility ≠ resources.",
                    },
                ],
            },
            {
                "id": "pr-fin-tip",
                "type": "callout",
                "tone": "tip",
                "title": "3Fs memory",
                "body": (
                    "**Functions · Funds · Functionaries** — constitutional skeleton without "
                    "matching 3Fs = ‘responsibility without resources’."
                ),
            },
        ],
    },
    {
        "title": "PR vs Municipalities + Quick Revision",
        "slug": "pr-vs-municipalities-revision",
        "sort_order": 15,
        "summary": (
            "Side-by-side 73rd vs 74th anchors plus a one-page article glance and "
            "60-second revision sheet for Panchayati Raj."
        ),
        "body": (
            "## Panchayats vs Municipalities (bridge)\n\n"
            "| Aspect | Panchayats (73rd) | Municipalities (74th) |\n"
            "| --- | --- | --- |\n"
            "| Part | IX | IX-A |\n"
            "| Articles | 243–243O | 243P–243ZG |\n"
            "| Schedule | 11th (29) | 12th (18) |\n"
            "| People body | Gram Sabha | Ward Committees (where provided) |\n"
            "| Structure | Village / intermediate / district | Nagar panchayat / municipal council / municipal corporation |\n"
            "| Elections body | SEC (243K) | SEC (243ZA) |\n"
            "| Finance body | SFC (243I) | SFC also covers municipalities |\n"
            "| Planning link | Feeds District Planning Committee | Same DPC / Metropolitan Planning Committee |\n\n"
            "## Articles at a glance (Table 39.2)\n\n"
            "- **243** Definitions · **243A** Gram Sabha · **243B** Constitution · "
            "**243C** Composition · **243D** Reservation · **243E** Duration · "
            "**243F** Disqualifications · **243G** Powers · **243H** Taxes/funds · "
            "**243-I** SFC · **243J** Audit · **243K** Elections/SEC · **243L** UTs · "
            "**243M** Exempted areas · **243N** Continuance · **243-O** Bar on courts.\n\n"
            "## Exempted / special (revision)\n\n"
            "Nagaland, Meghalaya, Mizoram; Fifth Schedule & tribal areas; Manipur hill district "
            "councils; Darjeeling Gorkha Hill Council — unless Parliament extends (as with PESA).\n\n"
            "## Continuance note\n\n"
            "States had **one year** from 24 Apr 1993 to adopt the new system; existing panchayats "
            "continued till term end unless dissolved sooner. Most state PRI Acts came in 1993–94."
        ),
        "articles": [
            ("Part IX", "The Panchayats — Arts 243–243O."),
            ("Part IX-A", "The Municipalities — Arts 243P–243ZG (comparison bridge)."),
            ("Eleventh Schedule", "29 panchayat subjects."),
            ("Twelfth Schedule", "18 municipality subjects."),
        ],
        "visual_blocks": [
            {
                "id": "pr-vs-muni",
                "type": "comparison",
                "title": "73rd vs 74th (quick)",
                "columns": [
                    {
                        "id": "pr",
                        "heading": "Panchayats",
                        "points": [
                            "Part IX · Arts 243–243O",
                            "11th Schedule · 29 subjects",
                            "Gram Sabha foundation",
                            "3 rural tiers (skip middle if ≤20 lakh)",
                            "Rural local self-government",
                        ],
                    },
                    {
                        "id": "muni",
                        "heading": "Municipalities",
                        "points": [
                            "Part IX-A · Arts 243P–243ZG",
                            "12th Schedule · 18 subjects",
                            "Ward Committees (urban)",
                            "3 urban types by size/transition",
                            "Urban local self-government",
                        ],
                    },
                ],
            },
            {
                "id": "pr-qr-tip",
                "type": "callout",
                "tone": "tip",
                "title": "60-second scan",
                "body": (
                    "243–243O · 29 subjects · 21 yrs · ≥1/3 women · SEC/SFC · "
                    "compulsory vs voluntary · PESA · 24 April 1993 · Nagaur 1959."
                ),
            },
        ],
    },
    {
        "title": "Prelims Traps, PYQ Themes & Mains VA",
        "slug": "pr-exam-kit",
        "sort_order": 16,
        "summary": (
            "High-yield prelims traps, recurring PYQ themes, landmark cases, "
            "mains value-addition, and a light recent-developments strip."
        ),
        "body": (
            "## Prelims traps\n\n"
            "- First state = **Rajasthan** (Nagaur, **2 Oct 1959**), not the 73rd itself.\n"
            "- 73rd in force = **24 April 1993** (National Panchayat Day).\n"
            "- Skip intermediate if population **≤ 20 lakh**.\n"
            "- Contest age **21** (not 25).\n"
            "- Women **≥ 1/3** seats **and** chair offices.\n"
            "- Members direct; village chair = **state decides**.\n"
            "- SEC appointed by Governor; removal **like HC judge**.\n"
            "- Structure compulsory; **3Fs depth voluntary**.\n"
            "- **11th** = panchayats (29); **12th** = municipalities (18).\n"
            "- Arunachal SC-seat exception = **83rd** Amendment.\n"
            "- PESA = **10** Fifth Schedule states; ST chairs **all** levels.\n"
            "- Ashok Mehta = **2-tier**; Balwant Rai = **3-tier**.\n\n"
            "## PYQ themes\n\n"
            "Features of 73rd · Gram Sabha · reservation (esp. women) · SEC/SFC · "
            "Balwant Rai vs Ashok Mehta · compulsory provisions · 11th Schedule items · "
            "PESA · Art. 40 link · duration/dissolution rules.\n\n"
            "## Mains VA\n\n"
            "- 73rd turned Art. 40 from aspiration into a justiciable third tier.\n"
            "- Participatory democracy still incomplete where Gram Sabha is paper-only.\n"
            "- Fiscal autonomy is the **soul** of PRI strength (2nd ARC) — grants alone hollow it out.\n"
            "- Parallel missions without PRI ownership recreate ‘grass without roots’.\n"
            "- PESA is not a copy-paste of Part IX — it is **tribal self-rule** with GS at the core.\n\n"
            "## Recent / VA (beyond Laxmikanth pp. 548–568)\n\n"
            "- **e-Gram Swaraj:** digital stack for planning, accounting, and progress monitoring "
            "of Gram Panchayats — exam angle = transparency + financial tracking.\n"
            "- **SVAMITVA:** drone-based property mapping in rural inhabited areas — links to "
            "own-source revenue / property tax potential of GPs.\n"
            "- **National Panchayat Day:** 24 April — commemorates 73rd commencement."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pr-pyq-heat",
                "type": "pyq_heatmap",
                "title": "PYQ focus map",
                "items": [
                    {"concept_slug": "pr-73rd-architecture", "label": "73rd features"},
                    {"concept_slug": "pr-structure-elections", "label": "Gram Sabha / tiers"},
                    {"concept_slug": "pr-reservation-duration", "label": "Reservation"},
                    {"concept_slug": "pr-sec-sfc-finances", "label": "SEC / SFC"},
                    {"concept_slug": "pr-compulsory-voluntary", "label": "Compulsory"},
                    {"concept_slug": "pr-pesa", "label": "PESA"},
                    {"concept_slug": "pr-balwant-rai", "label": "Committees"},
                    {"concept_slug": "pr-eleventh-schedule", "label": "11th Schedule"},
                ],
            },
            {
                "id": "pr-exam-traps",
                "type": "callout",
                "tone": "trap",
                "title": "Trap pack",
                "body": (
                    "Nagaur 1959 · 24 Apr 1993 · ≤20 lakh skip middle · age 21 · "
                    "SEC ≠ removable by Governor · 11th≠12th · Ashok Mehta = 2-tier · "
                    "3Fs not fully compulsory."
                ),
            },
            {
                "id": "pr-exam-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "Constitutionalising PRIs solved the ‘existence’ problem; the live challenge "
                    "is devolution of 3Fs and a working Gram Sabha — without which the third tier "
                    "risks remaining structure without substance."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pr-meaning-place"),
    (HUB_SLUG, "parent", "pr-evolution-timeline"),
    (HUB_SLUG, "parent", "pr-balwant-rai"),
    (HUB_SLUG, "parent", "pr-ashok-mehta"),
    (HUB_SLUG, "parent", "pr-later-committees"),
    (HUB_SLUG, "parent", "pr-constitutionalisation"),
    (HUB_SLUG, "parent", "pr-73rd-architecture"),
    (HUB_SLUG, "parent", "pr-structure-elections"),
    (HUB_SLUG, "parent", "pr-reservation-duration"),
    (HUB_SLUG, "parent", "pr-sec-sfc-finances"),
    (HUB_SLUG, "parent", "pr-compulsory-voluntary"),
    (HUB_SLUG, "parent", "pr-eleventh-schedule"),
    (HUB_SLUG, "parent", "pr-pesa"),
    (HUB_SLUG, "parent", "pr-finances-problems"),
    (HUB_SLUG, "parent", "pr-vs-municipalities-revision"),
    (HUB_SLUG, "parent", "pr-exam-kit"),
    ("pr-balwant-rai", "related", "pr-ashok-mehta"),
    ("pr-later-committees", "related", "pr-constitutionalisation"),
    ("pr-constitutionalisation", "related", "pr-73rd-architecture"),
    ("pr-73rd-architecture", "related", "pr-eleventh-schedule"),
    ("pr-73rd-architecture", "related", "pr-compulsory-voluntary"),
    ("pr-73rd-architecture", "related", "pr-pesa"),
    ("pr-structure-elections", "related", "pr-reservation-duration"),
    ("pr-sec-sfc-finances", "related", "pr-compulsory-voluntary"),
    ("pr-sec-sfc-finances", "related", "pr-finances-problems"),
    ("pr-eleventh-schedule", "related", "pr-finances-problems"),
    ("pr-pesa", "related", "pr-structure-elections"),
    ("pr-vs-municipalities-revision", "related", "pr-73rd-architecture"),
    ("pr-exam-kit", "related", "pr-73rd-architecture"),
    ("pr-exam-kit", "related", "pr-pesa"),
    ("pr-exam-kit", "related", "pr-compulsory-voluntary"),
    (HUB_SLUG, "related", "directive-principles"),
    (HUB_SLUG, "related", "federal-system"),
    (HUB_SLUG, "related", "salient-features-constitution"),
]

SAMPLE_PYQS = [
    (
        2011,
        "The Constitution (Seventy-third Amendment) Act, 1992, which aims at promoting the "
        "Panchayati Raj Institutions in the country, provides for which of the following?",
        "Among other things: Gram Sabha; three-tier PRIs (with limited exception); direct "
        "elections; reservation for SCs/STs and women; SEC and SFC — classic compulsory-feature set.",
        ["pr-73rd-architecture", "pr-compulsory-voluntary", HUB_SLUG],
    ),
    (
        2015,
        "The fundamental object of Panchayati Raj system is to ensure which among the following?",
        "Democratic decentralisation / people's participation in development — grass-root "
        "self-government, not merely bureaucratic delivery of schemes.",
        ["pr-meaning-place", "pr-balwant-rai", HUB_SLUG],
    ),
    (
        2016,
        "Consider statements on the State Election Commission and panchayat elections.",
        "SEC conducts panchayat elections; commissioner appointed by Governor; removal only "
        "in the manner of a High Court judge — not at the pleasure of the Governor.",
        ["pr-sec-sfc-finances", HUB_SLUG],
    ),
    (
        2017,
        "Which of the following are regarded as compulsory provisions under the 73rd Amendment?",
        "Organisation of Gram Sabha; three-tier structure; direct elections; reservation for "
        "SCs/STs and women; SEC; SFC — contrast with voluntary devolution of powers/taxes.",
        ["pr-compulsory-voluntary", HUB_SLUG],
    ),
    (
        2018,
        "With reference to the Provisions of the Panchayats (Extension to the Scheduled Areas) "
        "Act, 1996, consider Gram Sabha powers in Scheduled Areas.",
        "PESA makes Gram Sabha the nucleus — plan approval, beneficiary identification, "
        "custom/tradition protection, and decisive say on minor minerals / land issues.",
        ["pr-pesa", HUB_SLUG],
    ),
    (
        2012,
        "Which committee recommended the three-tier Panchayati Raj system?",
        "Balwant Rai Mehta Committee (1957) — democratic decentralisation with GP–PS–ZP.",
        ["pr-balwant-rai", "pr-evolution-timeline", HUB_SLUG],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Kishansing Tomar v. Municipal Corporation of Ahmedabad",
        "slug": "kishansing-tomar-sec-elections",
        "parties": "Kishansing Tomar v. Municipal Corporation of Ahmedabad",
        "year": 2006,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Supreme Court on timely local-body elections and the independence of the "
            "State Election Commission."
        ),
        "holding": (
            "Local-body elections must be held before the expiry of the term; the State "
            "Election Commission is to function independently, and state governments cannot "
            "frustrate the constitutional mandate of regular elections."
        ),
        "concept_slugs": ["pr-sec-sfc-finances", "pr-reservation-duration", HUB_SLUG],
    },
    {
        "title": "K. Krishna Murthy v. Union of India",
        "slug": "k-krishna-murthy-local-reservation",
        "parties": "K. Krishna Murthy v. Union of India",
        "year": 2010,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Constitution Bench on reservation of seats and chairperson offices in "
            "panchayats and municipalities."
        ),
        "holding": (
            "Upheld constitutional provisions enabling reservation in local bodies, while "
            "clarifying limits and the distinct nature of local-self-government reservation "
            "from parliamentary/assembly reservation debates."
        ),
        "concept_slugs": ["pr-reservation-duration", HUB_SLUG],
    },
    {
        "title": "Rajbala v. State of Haryana",
        "slug": "rajbala-haryana-panchayat-qualification",
        "parties": "Rajbala v. State of Haryana",
        "year": 2015,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Challenge to Haryana law prescribing educational and other qualifications "
            "for contesting panchayat elections."
        ),
        "holding": (
            "Supreme Court upheld the state's prescription of minimum educational and "
            "related qualifications for panchayat candidates as a matter of legislative policy "
            "within constitutional bounds — a recurring exam theme on eligibility conditions."
        ),
        "concept_slugs": ["pr-reservation-duration", "pr-structure-elections", HUB_SLUG],
    },
    {
        "title": "Vikas Kishanrao Gawali v. State of Maharashtra",
        "slug": "vikas-gawali-obc-local-reservation",
        "parties": "Vikas Kishanrao Gawali v. State of Maharashtra",
        "year": 2021,
        "court": CaseLaw.Court.SC,
        "summary": (
            "OBC reservation in local bodies — requirement of the triple-test before "
            "providing such reservation."
        ),
        "holding": (
            "States must satisfy the triple test (dedicated commission, contemporaneous "
            "rigorous data, and overall reservation ceiling) before notifying OBC reservation "
            "in local bodies — links to the voluntary OBC reservation space under Part IX."
        ),
        "concept_slugs": ["pr-reservation-duration", "pr-compulsory-voluntary", HUB_SLUG],
    },
]

AMENDMENTS = [
    {
        "number": 73,
        "year": 1992,
        "title": "Seventy-third Amendment",
        "summary": (
            "Added Part IX (The Panchayats) and the Eleventh Schedule; constitutionalised "
            "rural local self-government with compulsory structure, reservation, SEC and SFC."
        ),
        "effect": (
            "Arts 243–243O + 11th Schedule (29 subjects); in force 24 April 1993."
        ),
        "concept_slugs": [
            "pr-73rd-architecture",
            "pr-constitutionalisation",
            "pr-eleventh-schedule",
            HUB_SLUG,
        ],
    },
    {
        "number": 83,
        "year": 2000,
        "title": "Eighty-third Amendment",
        "summary": (
            "Exempted Arunachal Pradesh from the requirement of reservation of seats for "
            "Scheduled Castes in panchayats."
        ),
        "effect": (
            "SC seat reservation in panchayats not applicable to Arunachal Pradesh "
            "(wholly tribal population; no SCs)."
        ),
        "concept_slugs": ["pr-reservation-duration", HUB_SLUG],
    },
    {
        "number": 74,
        "year": 1992,
        "title": "Seventy-fourth Amendment",
        "summary": (
            "Added Part IX-A (The Municipalities) and the Twelfth Schedule — urban counterpart "
            "to the 73rd Amendment."
        ),
        "effect": "Urban local bodies constitutionalised; useful PR vs Municipalities contrast.",
        "concept_slugs": ["pr-vs-municipalities-revision", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = (
        "Seed Panchayati Raj chapter (Laxmikanth Ch.39) under Part V Local Government."
    )

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
                "title": "Panchayati Raj",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 39 · pp. 548–568",
                "summary": (
                    "Visual revision of Ch.39 — evolution, committees, 73rd Amendment, "
                    "Part IX, Eleventh Schedule, PESA, finances, and exam kit."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="local-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Panchayati Raj",
                "summary": (
                    "Rural local self-government — Part IX Arts 243–243O; "
                    "73rd Amendment constitutionalised the third tier."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **grassroots republic** mental model, then "
                    "**Committees** → **73rd architecture** → **3-tier + Gram Sabha** → "
                    "**SEC/SFC** → **Compulsory vs Voluntary** → **PESA** → **Exam kit**. "
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
            ref="Laxmikanth Ch. 39",
            excerpt=(
                "Panchayati Raj — evolution, committees, 73rd Amendment, "
                "Part IX, Eleventh Schedule, PESA, and finances."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 243–243O",
            excerpt="Part IX framework for Panchayats.",
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Eleventh Schedule",
            excerpt="29 functional items of the panchayats (Art. 243G).",
            sort_order=2,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 40",
            excerpt="DPSP on village panchayats — given practical shape by the 73rd Amendment.",
            sort_order=3,
        )

        pr_slugs = set(by_slug.keys())
        related_outside = {
            "directive-principles",
            "federal-system",
            "salient-features-constitution",
        }
        ConceptEdge.objects.filter(
            source__slug__in=pr_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=pr_slugs | related_outside).delete()

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
                f"Panchayati Raj chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
