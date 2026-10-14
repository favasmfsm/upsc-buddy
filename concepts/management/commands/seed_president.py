"""Seed Laxmikanth Ch.18 President (visual revision — Part III Central Government)."""

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

HUB_SLUG = "president"
CHAPTER_SLUG = "president"

ENTRY_PILLARS = [
    {
        "id": "election",
        "articles": "Arts 54–55",
        "label": "Election & college",
        "slug": "pr-election",
        "detail": "Indirect election — MPs + state MLAs + Delhi/Puducherry; vote-value parity.",
        "tone": "teal",
    },
    {
        "id": "why",
        "articles": "CA logic",
        "label": "Why indirect",
        "slug": "pr-why-indirect",
        "detail": "Parliamentary harmony, cost, and Union–state representation.",
        "tone": "olive",
    },
    {
        "id": "quals",
        "articles": "Arts 58–60",
        "label": "Qualifications & oath",
        "slug": "pr-qualifications-oath",
        "detail": "Citizen, 35+, LS-eligible; oath by CJI; office conditions.",
        "tone": "gold",
    },
    {
        "id": "impeach",
        "articles": "Art. 61",
        "label": "Term & impeachment",
        "slug": "pr-term-impeachment",
        "detail": "5 years; Elect ≠ Impeach; ⅔ total membership both Houses.",
        "tone": "orange",
    },
    {
        "id": "vacancy",
        "articles": "Arts 62, 65",
        "label": "Vacancy & succession",
        "slug": "pr-vacancy-succession",
        "detail": "VP → CJI → seniormost SC judge; 6-month election window.",
        "tone": "terracotta",
    },
    {
        "id": "powers-map",
        "articles": "7 heads",
        "label": "Powers map",
        "slug": "pr-powers-map",
        "detail": "Executive through emergency — one map for revision.",
        "tone": "maroon",
    },
    {
        "id": "exec-leg",
        "articles": "Part V",
        "label": "Executive & legislative",
        "slug": "pr-executive-legislative",
        "detail": "Appointments, Parliament role, nominations, prior recommendation.",
        "tone": "teal",
    },
    {
        "id": "other",
        "articles": "5 heads",
        "label": "Other powers",
        "slug": "pr-other-powers",
        "detail": "Financial, judicial, diplomatic, military, emergency.",
        "tone": "olive",
    },
    {
        "id": "veto",
        "articles": "Arts 111, 201",
        "label": "Veto power",
        "slug": "pr-veto",
        "detail": "Absolute, suspensive, pocket — Centre vs state legislation.",
        "tone": "gold",
    },
    {
        "id": "ordinance",
        "articles": "Art. 123",
        "label": "Ordinances",
        "slug": "pr-ordinance",
        "detail": "Recess legislation — 6 months + 6 weeks; Cooper & Wadhwa.",
        "tone": "orange",
    },
    {
        "id": "pardon",
        "articles": "Art. 72",
        "label": "Pardoning power",
        "slug": "pr-pardon",
        "detail": "PCRRR; President vs Governor on court martial and death.",
        "tone": "terracotta",
    },
    {
        "id": "position",
        "articles": "Arts 53, 74, 75",
        "label": "Constitutional position",
        "slug": "pr-constitutional-position",
        "detail": "Nominal executive; 42nd/44th advice; situational discretion.",
        "tone": "maroon",
    },
    {
        "id": "tables",
        "articles": "Table 18.3",
        "label": "Articles & tables",
        "slug": "pr-articles-tables",
        "detail": "Article glance + veto table + vote-value idea.",
        "tone": "teal",
    },
    {
        "id": "exam",
        "articles": "PYQ kit",
        "label": "Exam kit",
        "slug": "pr-exam-kit",
        "detail": "Prelims traps, PYQ themes, and mains one-liners.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pr-seal-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Ceremonial seal",
        "topic_label": "President of India",
        "subject_label": "Arts 52–78 · Part V",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating the President as the real executive",
            "Confusing who elects with who impeaches",
            "Forgetting pocket veto and Art. 123 life-span",
            "Equating Indian President with the US President",
        ],
        "insight": (
            "Ambedkar: head of the State, not of the Executive — represents the nation "
            "but does not rule it; a seal by which the nation’s decisions are made known."
        ),
    },
    {
        "id": "pr-entry-pillars",
        "type": "pillars",
        "title": "Fourteen revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "pr-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Path: Election → Vetoes → Ordinance → Pardon → Position (42nd/44th + situational discretion). "
            "Trap trio: Elect ≠ Impeach; pocket veto (no time limit); Art. 123 max life = 6 months + 6 weeks."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Election & Electoral College",
        "slug": "pr-election",
        "sort_order": 1,
        "summary": (
            "Indirect election by elected MPs, state MLAs, and Delhi/Puducherry MLAs — "
            "vote-value parity, STV, and SC as final election court."
        ),
        "body": (
            "## Electoral college (Arts 54–55)\n\n"
            "**Votes:** elected members of both Houses of Parliament; elected MLAs of states; "
            "elected MLAs of Delhi and Puducherry.\n\n"
            "**Do not vote:** nominated MPs; nominated MLAs; MLCs (elected or nominated); "
            "nominated MLAs of Puducherry. Dissolved assembly members are not qualified to vote.\n\n"
            "### Vote value (parity)\n"
            "- **MLA:** (state population ÷ elected MLAs) ÷ 1000 (multiples of 1,000 in the quotient).\n"
            "- **MP:** total MLA votes of all states ÷ total elected MPs of both Houses.\n"
            "- Goal: uniformity among states + parity between states as a whole and the Union.\n\n"
            "### Method\n"
            "Proportional representation by single transferable vote; **secret ballot**. "
            "Quota ≈ (valid votes ÷ 2) + 1. Preferences 1, 2, 3…; transfer from lowest until quota.\n\n"
            "### Disputes (Art. 71)\n"
            "Supreme Court decides; incomplete college ≠ ground to challenge; acts before a void "
            "declaration remain valid.\n\n"
            "### Election highlights\n"
            "Only Rajendra Prasad elected twice; Sanjeeva Reddy unopposed (1977); "
            "first woman Pratibha Patil (2007); first tribal woman Droupadi Murmu (2022)."
        ),
        "articles": [
            ("Art. 54", "Election of President — electoral college composition."),
            ("Art. 55", "Manner of election — uniformity, parity, PR by STV."),
            ("Art. 71", "Matters relating to election of President — SC decides disputes."),
        ],
        "visual_blocks": [
            {
                "id": "pr-elect-flow",
                "type": "flowchart",
                "title": "Who votes for the President?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Is the person an elected legislator?",
                        "detail": "Start with membership type before counting votes.",
                        "options": [
                            {"label": "Elected MP (LS/RS)", "next": "yes"},
                            {"label": "Elected state MLA", "next": "yes"},
                            {"label": "Elected MLA of Delhi/Puducherry", "next": "yes"},
                            {"label": "Nominated / MLC / dissolved MLA", "next": "no"},
                        ],
                    },
                    {
                        "id": "yes",
                        "label": "In the electoral college",
                        "detail": "Casts vote(s) by value under Art. 55; STV + secret ballot.",
                    },
                    {
                        "id": "no",
                        "label": "Out of the college",
                        "detail": "Nominated MPs/MLAs, all MLCs, and members of a dissolved assembly do not vote.",
                    },
                ],
            },
            {
                "id": "pr-elect-formula",
                "type": "callout",
                "tone": "tip",
                "title": "Formula card",
                "body": (
                    "MLA value ≈ (Population ÷ elected MLAs) ÷ 1000. "
                    "MP value = Σ MLA votes ÷ elected MPs. "
                    "Quota = (valid votes ÷ 2) + 1."
                ),
            },
            {
                "id": "pr-elect-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "104th Amendment ended Anglo-Indian nominations (from 25 Jan 2020) — "
                    "they were never electoral-college voters anyway (nominated). "
                    "Incomplete college does not void the election."
                ),
            },
        ],
    },
    {
        "title": "Why Indirect Election",
        "slug": "pr-why-indirect",
        "sort_order": 2,
        "summary": (
            "Constituent Assembly chose indirect election for parliamentary harmony, "
            "cost, and equal Union–state representation — ‘PR’ is a misnomer for one seat."
        ),
        "body": (
            "## Why not direct?\n\n"
            "1. **Harmony with parliamentary system** — President is nominal; real power with CoM/PM. "
            "Direct election with no real power would be anomalous.\n"
            "2. **Cost and scale** — vast electorate for a symbolic head is unwarranted.\n"
            "3. **Not Parliament alone** — Parliament-only election would make the President a "
            "party nominee of the dominant party, not a representative of the states.\n\n"
            "### Naming caveat\n"
            "‘Proportional representation’ is a misnomer when only **one** seat is filled — "
            "preferential / alternative vote is more accurate. ‘Single transferable vote’ was also "
            "objected to because each elector has **plural** preference votes."
        ),
        "articles": [
            ("Art. 54–55", "Indirect election designed for a parliamentary, federal Union."),
        ],
        "visual_blocks": [
            {
                "id": "pr-why-pillars",
                "type": "pillars",
                "title": "Three CA reasons",
                "items": [
                    {
                        "id": "harmony",
                        "articles": "Reason 1",
                        "label": "Parliamentary harmony",
                        "slug": "pr-why-indirect",
                        "detail": "Nominal head — direct mandate without power would be odd.",
                        "tone": "teal",
                    },
                    {
                        "id": "cost",
                        "articles": "Reason 2",
                        "label": "Cost & size",
                        "slug": "pr-why-indirect",
                        "detail": "Nationwide direct poll for a symbolic office is wasteful.",
                        "tone": "olive",
                    },
                    {
                        "id": "states",
                        "articles": "Reason 3",
                        "label": "Union + states",
                        "slug": "pr-why-indirect",
                        "detail": "College includes state MLAs — not a Parliament-only pick.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "pr-why-note",
                "type": "callout",
                "tone": "note",
                "title": "Mains VA",
                "body": (
                    "Present system makes the President a representative of the Union and the "
                    "states equally — useful federalism angle in GS-II answers."
                ),
            },
        ],
    },
    {
        "title": "Qualifications, Oath & Conditions",
        "slug": "pr-qualifications-oath",
        "sort_order": 3,
        "summary": (
            "Citizen, 35+, Lok Sabha-eligible, no office of profit; oath by CJI; "
            "office conditions, immunities, and nomination thresholds."
        ),
        "body": (
            "## Qualifications (Art. 58)\n\n"
            "1. Citizen of India\n"
            "2. Completed **35** years\n"
            "3. Qualified for election as a **Lok Sabha** member\n"
            "4. Not hold any office of profit (Union/state/local/public authority)\n\n"
            "**Not office of profit:** sitting President, Vice-President, Governor, Union/state minister.\n\n"
            "### Nomination (statute)\n"
            "≥ **50 proposers + 50 seconders**; security deposit **₹15,000** (forfeited if < 1/6 votes). "
            "Raised in **1997** (earlier 10+10 and ₹2,500) to deter non-serious candidates.\n\n"
            "### Oath (Art. 60)\n"
            "Execute office; preserve, protect and defend the Constitution and the law; "
            "devote to service and well-being of the people. Administered by **CJI** "
            "(or seniormost SC judge available).\n\n"
            "### Conditions (Art. 59)\n"
            "Not a member of Parliament/state legislature (seat vacated on entering office); "
            "no other office of profit; rent-free official residence; emoluments fixed by Parliament "
            "and **not diminished** during term.\n\n"
            "### Prelims figures\n"
            "Salary raised to **₹5 lakh/month** (2018). Criminal immunity for personal acts during term; "
            "civil proceedings only after **two months’ notice**."
        ),
        "articles": [
            ("Art. 58", "Qualifications for election as President."),
            ("Art. 59", "Conditions of President’s office."),
            ("Art. 60", "Oath or affirmation by the President."),
        ],
        "visual_blocks": [
            {
                "id": "pr-qual-compare",
                "type": "comparison",
                "title": "Qualifications vs conditions of office",
                "columns": [
                    {
                        "id": "quals",
                        "heading": "To be elected (Art. 58)",
                        "points": [
                            "Citizen of India",
                            "35+ years of age",
                            "Eligible for Lok Sabha",
                            "No office of profit (with listed exceptions)",
                            "50+50 proposers/seconders; ₹15k deposit",
                        ],
                    },
                    {
                        "id": "conds",
                        "heading": "While in office (Art. 59)",
                        "points": [
                            "Not MP / MLA / MLC",
                            "No other office of profit",
                            "Rent-free official residence",
                            "Emoluments not diminished during term",
                            "Criminal immunity; civil suit after 2 months’ notice",
                        ],
                    },
                ],
            },
            {
                "id": "pr-qual-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Oath one-liner",
                "body": "Oath by CJI — preserve, protect, defend the Constitution (Art. 60).",
            },
        ],
    },
    {
        "title": "Term & Impeachment",
        "slug": "pr-term-impeachment",
        "sort_order": 4,
        "summary": (
            "Five-year term with unlimited re-election; Art. 61 impeachment for ‘violation of the "
            "Constitution’ — Elect ≠ Impeach participants."
        ),
        "body": (
            "## Term (Art. 56–57)\n\n"
            "Holds office for **five years**; may resign to the **Vice-President**; eligible for "
            "**re-election any number of times** (USA: max two terms). May continue until successor "
            "assumes charge.\n\n"
            "## Impeachment (Art. 61)\n\n"
            "Ground: **‘violation of the Constitution’** (undefined). Quasi-judicial in Parliament.\n\n"
            "1. Charges by **either House**, signed by **¼** of that House’s members; **14 days’** notice.\n"
            "2. Resolution by **⅔ of total membership** of initiating House.\n"
            "3. Other House investigates; President may appear/be represented.\n"
            "4. If other House also passes by **⅔ of total membership** → removed from that date.\n\n"
            "**Elect ≠ Impeach:** nominated MPs may **impeach** but not **elect**; elected state/UT "
            "MLAs **elect** but do **not** impeach. No President has been impeached so far."
        ),
        "articles": [
            ("Art. 56", "Term of office of President."),
            ("Art. 57", "Eligibility for re-election."),
            ("Art. 61", "Procedure for impeachment of the President."),
        ],
        "visual_blocks": [
            {
                "id": "pr-impeach-flow",
                "type": "flowchart",
                "title": "Impeachment path (Art. 61)",
                "root": "init",
                "steps": [
                    {
                        "id": "init",
                        "label": "Either House frames charges",
                        "detail": "Signed by ¼ members; 14 days’ notice to the President.",
                        "options": [{"label": "Next", "next": "pass1"}],
                    },
                    {
                        "id": "pass1",
                        "label": "⅔ of total membership passes",
                        "detail": "Initiating House must clear special majority of total membership.",
                        "options": [{"label": "Next", "next": "other"}],
                    },
                    {
                        "id": "other",
                        "label": "Other House investigates",
                        "detail": "President has right to appear and be represented.",
                        "options": [{"label": "Charges sustained?", "next": "remove"}],
                    },
                    {
                        "id": "remove",
                        "label": "⅔ of total membership → removed",
                        "detail": "Removal from the date the second House passes the resolution.",
                    },
                ],
            },
            {
                "id": "pr-impeach-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Elect ≠ Impeach",
                "body": (
                    "MLAs elect, don’t impeach. Nominated MPs impeach, don’t elect. "
                    "Majority is ⅔ of **total membership**, not present and voting."
                ),
            },
        ],
    },
    {
        "title": "Vacancy & Succession",
        "slug": "pr-vacancy-succession",
        "sort_order": 5,
        "summary": (
            "How vacancies arise; election timing; Vice-President / CJI / seniormost judge succession ladder."
        ),
        "body": (
            "## When vacancy arises\n\n"
            "Expiry of term · resignation · impeachment · death · otherwise (disqualification / election void).\n\n"
            "## Election timing (Art. 62)\n\n"
            "- **Expiry:** election **before** term ends — outgoing President continues if delayed "
            "(no interregnum; VP does **not** act in this case).\n"
            "- **Resignation / removal / death / otherwise:** election within **six months**; "
            "new President gets a **full five-year** term.\n\n"
            "## Who acts / discharges (Art. 65)\n\n"
            "- Vacancy (resign/remove/death/else): **Vice-President acts** as President until election.\n"
            "- Absence/illness: **VP discharges** functions until President resumes.\n"
            "- If VP office also vacant: **CJI**, then **seniormost SC judge** available.\n\n"
            "Acting President enjoys all powers and immunities; emoluments as determined by Parliament.\n\n"
            "**Example:** After Zakir Husain’s death (1969), V.V. Giri acted, then resigned to contest; "
            "CJI M. Hidayatullah officiated (20 Jul–24 Aug 1969)."
        ),
        "articles": [
            ("Art. 62", "Time of holding election to fill vacancy in the office of President."),
            ("Art. 65", "Vice-President to act as President or to discharge his functions."),
        ],
        "visual_blocks": [
            {
                "id": "pr-vacancy-journey",
                "type": "journey",
                "title": "Succession ladder",
                "stages": [
                    {
                        "id": "v1",
                        "label": "Vice-President",
                        "detail": "Acts on vacancy; discharges on absence/illness.",
                    },
                    {
                        "id": "v2",
                        "label": "Chief Justice of India",
                        "detail": "If VP office is also vacant.",
                    },
                    {
                        "id": "v3",
                        "label": "Seniormost SC judge",
                        "detail": "If CJI office is also vacant.",
                    },
                ],
            },
            {
                "id": "pr-vacancy-flow",
                "type": "flowchart",
                "title": "Vacancy type → election clock",
                "root": "type",
                "steps": [
                    {
                        "id": "type",
                        "label": "How did the office fall vacant?",
                        "detail": "Timing rules differ for expiry vs sudden vacancy.",
                        "options": [
                            {"label": "Term about to expire", "next": "expiry"},
                            {"label": "Resign / remove / death / else", "next": "sudden"},
                        ],
                    },
                    {
                        "id": "expiry",
                        "label": "Elect before expiry",
                        "detail": "Outgoing President continues if delayed — VP does not act.",
                    },
                    {
                        "id": "sudden",
                        "label": "Elect within 6 months",
                        "detail": "VP acts meanwhile; new President gets full 5-year term.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Powers at a Glance",
        "slug": "pr-powers-map",
        "sort_order": 6,
        "summary": (
            "Seven heads of presidential power — map first, then drill executive/legislative, "
            "other powers, veto, ordinance, and pardon."
        ),
        "body": (
            "## Seven heads\n\n"
            "1. **Executive** — all Union executive action in President’s name; appointments; Art. 78.\n"
            "2. **Legislative** — integral part of Parliament; summon/prorogue/dissolve; assent; ordinances.\n"
            "3. **Financial** — Contingency Fund; Budget; Money Bill recommendation; no demand without recommendation.\n"
            "4. **Judicial** — appoint SC/HC judges; Art. 143 advisory opinion; pardons (Art. 72).\n"
            "5. **Diplomatic** — international treaties/agreements in President’s name; receives diplomats.\n"
            "6. **Military** — supreme commander; war/peace on CoM advice.\n"
            "7. **Emergency** — Arts **352**, **356/365**, **360**.\n\n"
            "Deep dive next: Executive & Legislative → Other powers → Veto → Ordinance → Pardon."
        ),
        "articles": [
            ("Art. 53", "Executive power of the Union vested in the President."),
        ],
        "visual_blocks": [
            {
                "id": "pr-powers-pillars",
                "type": "pillars",
                "title": "Seven power heads",
                "items": [
                    {
                        "id": "exec",
                        "articles": "1",
                        "label": "Executive",
                        "slug": "pr-executive-legislative",
                        "detail": "Name, appointments, business rules, Art. 78.",
                        "tone": "teal",
                    },
                    {
                        "id": "leg",
                        "articles": "2",
                        "label": "Legislative",
                        "slug": "pr-executive-legislative",
                        "detail": "Parliament role, nominations, prior recommendation, assent.",
                        "tone": "olive",
                    },
                    {
                        "id": "fin",
                        "articles": "3",
                        "label": "Financial",
                        "slug": "pr-other-powers",
                        "detail": "Budget, Money Bills, Contingency Fund.",
                        "tone": "gold",
                    },
                    {
                        "id": "jud",
                        "articles": "4",
                        "label": "Judicial",
                        "slug": "pr-other-powers",
                        "detail": "Judges, Art. 143, link to pardons.",
                        "tone": "orange",
                    },
                    {
                        "id": "dip",
                        "articles": "5",
                        "label": "Diplomatic",
                        "slug": "pr-other-powers",
                        "detail": "Treaties and diplomats in President’s name.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "mil",
                        "articles": "6",
                        "label": "Military",
                        "slug": "pr-other-powers",
                        "detail": "Supreme commander — war/peace on advice.",
                        "tone": "maroon",
                    },
                    {
                        "id": "emg",
                        "articles": "7",
                        "label": "Emergency",
                        "slug": "pr-other-powers",
                        "detail": "352 · 356/365 · 360 — depth in Emergency chapter.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "pr-powers-note",
                "type": "callout",
                "tone": "note",
                "title": "Revision tip",
                "body": (
                    "Veto, ordinance, and pardon are high-frequency — treat them as separate "
                    "revision stops even though they sit under legislative/judicial umbrellas."
                ),
            },
        ],
    },
    {
        "title": "Executive & Legislative Powers",
        "slug": "pr-executive-legislative",
        "sort_order": 7,
        "summary": (
            "Union executive in the President’s name; key appointments; integral role in Parliament "
            "including nominations and prior recommendation bills."
        ),
        "body": (
            "## Executive (high-yield)\n\n"
            "- All executive action of GoI formally in President’s name; authentication & business rules.\n"
            "- Appoints **PM and ministers** (pleasure); **AG**; **CAG**; **CEC/ECs**; **UPSC**; "
            "**Governors**; **Finance Commission**; etc.\n"
            "- Art. **78**: PM communicates decisions, furnishes information, and (if required) "
            "submits a minister’s decision to the full council.\n"
            "- Administers UTs via administrators; powers on scheduled/tribal areas; can appoint "
            "backward-classes commission and Inter-State Council.\n\n"
            "## Legislative (high-yield)\n\n"
            "- Integral part of Parliament: summon, prorogue, dissolve LS; joint sitting "
            "(presided by LS Speaker); addresses; messages.\n"
            "- Nominates **12** Rajya Sabha members (literature, science, art, social service).\n"
            "- **104th Amendment (2019):** discontinued Anglo-Indian nomination to LS "
            "(and state assemblies) from 25 Jan 2020.\n"
            "- Decides MP disqualification in consultation with Election Commission.\n"
            "- Prior recommendation/permission for Money Bills, expenditure from Consolidated Fund, "
            "new states/boundaries, and listed Union–state fiscal bills; prior sanction for certain "
            "state trade-restriction bills."
        ),
        "articles": [
            ("Art. 53", "Executive power of the Union."),
            ("Art. 74–75", "Council of Ministers — aid and advice; collective responsibility."),
            ("Art. 78", "Duties of PM regarding information to the President."),
            ("Art. 79–86", "Parliament composition and presidential role (summon, address, etc.)."),
        ],
        "visual_blocks": [
            {
                "id": "pr-appoint-tree",
                "type": "tree",
                "title": "Key appointments in President’s name",
                "root": {
                    "id": "pres",
                    "label": "President",
                    "children": [
                        {
                            "id": "exec-wing",
                            "label": "Executive wing",
                            "children": [
                                {"id": "pm", "label": "PM & ministers"},
                                {"id": "ag", "label": "Attorney General"},
                                {"id": "gov", "label": "Governors"},
                            ],
                        },
                        {
                            "id": "const-bodies",
                            "label": "Constitutional offices",
                            "children": [
                                {"id": "cag", "label": "CAG"},
                                {"id": "ec", "label": "Election Commission"},
                                {"id": "upsc", "label": "UPSC"},
                                {"id": "fc", "label": "Finance Commission"},
                            ],
                        },
                    ],
                },
            },
            {
                "id": "pr-leg-trap",
                "type": "callout",
                "tone": "trap",
                "title": "104th Amendment",
                "body": (
                    "Anglo-Indian LS nomination ended — do not still list ‘2 Anglo-Indian members’ "
                    "as a current legislative power."
                ),
            },
        ],
    },
    {
        "title": "Financial, Judicial, Diplomatic, Military & Emergency",
        "slug": "pr-other-powers",
        "sort_order": 8,
        "summary": (
            "Compact map of the remaining five power heads — Budget/Money Bills, judges & Art. 143, "
            "diplomacy, supreme command, and three emergencies."
        ),
        "body": (
            "## Financial\n\n"
            "Advances from Contingency Fund; Money Bill prior recommendation; Annual Financial Statement "
            "(Budget) laid before Parliament; no demand for grant except on recommendation.\n\n"
            "## Judicial\n\n"
            "Appoints Chief Justice and other SC/HC judges; can seek **Art. 143** advisory opinion of SC; "
            "pardoning power under Art. 72 (separate cluster).\n\n"
            "## Diplomatic\n\n"
            "International treaties and agreements negotiated/concluded in President’s name; "
            "receives credentials of diplomats; represents India in international forums.\n\n"
            "## Military\n\n"
            "**Supreme commander** of defence forces; appoints chiefs; war and peace on advice of CoM.\n\n"
            "## Emergency\n\n"
            "- National Emergency — **Art. 352**\n"
            "- President’s Rule — **Arts 356 & 365**\n"
            "- Financial Emergency — **Art. 360**\n\n"
            "Depth lives in the Emergency Provisions chapter when seeded — memorize the trio here."
        ),
        "articles": [
            ("Art. 112–117", "Financial procedures involving the President."),
            ("Art. 124, 217, 143", "Judges’ appointment and advisory jurisdiction."),
            ("Art. 352, 356, 365, 360", "Three emergency proclamations."),
        ],
        "visual_blocks": [
            {
                "id": "pr-other-pillars",
                "type": "pillars",
                "title": "Five heads — one card each",
                "items": [
                    {
                        "id": "fin",
                        "articles": "Finance",
                        "label": "Financial",
                        "slug": "pr-other-powers",
                        "detail": "Contingency Fund · Money Bill · Budget · demands.",
                        "tone": "teal",
                    },
                    {
                        "id": "jud",
                        "articles": "Judicial",
                        "label": "Judicial",
                        "slug": "pr-pardon",
                        "detail": "SC/HC judges · Art. 143 · link to Art. 72.",
                        "tone": "olive",
                    },
                    {
                        "id": "dip",
                        "articles": "Diplomatic",
                        "label": "Diplomatic",
                        "slug": "pr-other-powers",
                        "detail": "Treaties and diplomats in President’s name.",
                        "tone": "gold",
                    },
                    {
                        "id": "mil",
                        "articles": "Military",
                        "label": "Military",
                        "slug": "pr-other-powers",
                        "detail": "Supreme commander — war/peace on CoM advice.",
                        "tone": "orange",
                    },
                    {
                        "id": "emg",
                        "articles": "Emergency",
                        "label": "Emergency trio",
                        "slug": "pr-other-powers",
                        "detail": "352 · 356/365 · 360.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "pr-emg-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic",
                "body": "Emergencies: National (352) · State machinery (356/365) · Financial (360).",
            },
        ],
    },
    {
        "title": "Veto Power",
        "slug": "pr-veto",
        "sort_order": 9,
        "summary": (
            "Art. 111 alternatives; absolute, suspensive, and pocket vetoes; Centre vs state "
            "legislation under Arts 200–201; no veto on constitutional amendments."
        ),
        "body": (
            "## Art. 111 (Union bills)\n\n"
            "Assent · withhold assent · return (if **not** a Money Bill). If returned and passed again "
            "(with or without amendments), assent is **obligatory**.\n\n"
            "## Four veto types worldwide\n\n"
            "Absolute · Qualified · Suspensive · Pocket. **India has three** (no qualified veto — USA has it).\n\n"
            "- **Absolute:** withhold assent → bill dies (private members’ bills; or govt bill after "
            "cabinet change advising against assent). Examples: PEPSU Appropriation Bill (1954); "
            "MPs’ Salary Bill (1991).\n"
            "- **Suspensive:** return for reconsideration; overridden by **ordinary** majority re-passage "
            "(not a higher majority as in USA). **No suspensive veto on Money Bills.**\n"
            "- **Pocket:** neither assent nor reject nor return — indefinite silence (no time limit). "
            "‘Bigger pocket’ than USA (10 days). Example: Indian Post Office (Amendment) Bill, 1986 (Zail Singh).\n\n"
            "## Constitutional amendment bills\n\n"
            "**24th Amendment (1971):** President **must** give assent — no veto.\n\n"
            "## State legislation (Arts 200–201)\n\n"
            "Governor may reserve a bill. President: assent / withhold / return (non-Money) via Governor. "
            "Even after re-passage, President is **not bound** to assent — state legislature cannot override. "
            "No time limit → pocket veto also available on reserved state bills."
        ),
        "articles": [
            ("Art. 111", "Assent to bills passed by Parliament."),
            ("Art. 200", "Assent to bills — Governor’s options including reservation."),
            ("Art. 201", "Bills reserved for consideration of the President."),
        ],
        "visual_blocks": [
            {
                "id": "pr-veto-compare",
                "type": "comparison",
                "title": "Veto types — India vs available globally",
                "columns": [
                    {
                        "id": "india",
                        "heading": "Indian President",
                        "points": [
                            "Absolute veto — yes",
                            "Suspensive veto — yes (ordinary majority override)",
                            "Pocket veto — yes (no time limit)",
                            "Qualified veto — no",
                            "CA bills — must assent (24th)",
                        ],
                    },
                    {
                        "id": "world",
                        "heading": "Contrast notes",
                        "points": [
                            "USA has qualified veto (higher majority override)",
                            "USA pocket window ≈ 10 days",
                            "India Money Bill: assent or withhold — no return",
                            "State reserved bill: legislature cannot override President",
                            "Object: check hasty / unconstitutional legislation",
                        ],
                    },
                ],
            },
            {
                "id": "pr-veto-table",
                "type": "callout",
                "tone": "tip",
                "title": "Table 18.2 — glance",
                "body": (
                    "Ordinary bills: ratify / reject / return (Centre & state reserved). "
                    "Money bills: ratify / reject — cannot return. "
                    "CA bills: Centre — only ratify; cannot be introduced in state legislatures."
                ),
            },
            {
                "id": "pr-veto-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Pocket ≠ suspensive",
                "body": (
                    "Suspensive = return and can be overridden by re-passage. "
                    "Pocket = silence forever unless the President later acts."
                ),
            },
        ],
    },
    {
        "title": "Ordinance-Making Power",
        "slug": "pr-ordinance",
        "sort_order": 10,
        "summary": (
            "Art. 123 recess legislation — same force as an Act, four limits, justiciable satisfaction, "
            "max life 6 months + 6 weeks, and Wadhwa on re-promulgation."
        ),
        "body": (
            "## Art. 123\n\n"
            "President may promulgate ordinances when **both Houses are not in session** or "
            "**either House** is not in session (law needs both Houses). Ordinance when both are "
            "in session is **void**. Same force as an Act of Parliament — temporary law.\n\n"
            "### Four limits\n"
            "1. Houses not both in session.\n"
            "2. Satisfaction that immediate action is necessary — **justiciable** on mala fide "
            "(Cooper, 1970). 38th made satisfaction final; **44th** deleted that — review restored.\n"
            "3. Coextensive with Parliament’s law-making power except **duration** — cannot violate FRs; "
            "cannot amend the Constitution.\n"
            "4. Must be laid before both Houses on reassembly; ceases after **six weeks** from reassembly "
            "if not approved (or earlier if both Houses disapprove). Max life ≈ **6 months + 6 weeks** "
            "(max gap between sessions + six weeks).\n\n"
            "Withdraw anytime; only on **CoM advice** (not discretionary). Can be retrospective; "
            "may amend/repeal Acts or tax law. **Not linked to Art. 352** — can issue without emergency.\n\n"
            "**D.C. Wadhwa (1986):** successive re-promulgation without attempting assembly passage "
            "violates the Constitution."
        ),
        "articles": [
            ("Art. 123", "Power of President to promulgate ordinances during recess of Parliament."),
            ("Art. 13", "‘Law’ includes ordinances — FR limitations apply."),
        ],
        "visual_blocks": [
            {
                "id": "pr-ord-flow",
                "type": "flowchart",
                "title": "Is the ordinance valid?",
                "root": "session",
                "steps": [
                    {
                        "id": "session",
                        "label": "Are both Houses in session?",
                        "detail": "Ordinance power is not parallel legislation.",
                        "options": [
                            {"label": "Yes — both sitting", "next": "void"},
                            {"label": "No — either/both in recess", "next": "need"},
                        ],
                    },
                    {
                        "id": "void",
                        "label": "Ordinance void",
                        "detail": "Cannot legislate by ordinance while Parliament can pass a law.",
                    },
                    {
                        "id": "need",
                        "label": "Immediate action needed?",
                        "detail": "Satisfaction is justiciable (mala fide / colourable prorogation).",
                        "options": [
                            {"label": "Yes + within Parliament’s competence", "next": "ok"},
                            {"label": "Amends Constitution / violates FR", "next": "bad"},
                        ],
                    },
                    {
                        "id": "ok",
                        "label": "Valid — lay on reassembly",
                        "detail": "Max life 6 months + 6 weeks if Parliament takes no action.",
                    },
                    {
                        "id": "bad",
                        "label": "Unconstitutional",
                        "detail": "Same limits as an Act — no CA by ordinance; FRs bind.",
                    },
                ],
            },
            {
                "id": "pr-ord-timeline",
                "type": "timeline",
                "title": "Satisfaction & judicial review",
                "events": [
                    {
                        "id": "t1",
                        "year": 1970,
                        "label": "Cooper",
                        "detail": "President’s satisfaction can be questioned for mala fide.",
                    },
                    {
                        "id": "t2",
                        "year": 1975,
                        "label": "38th Amendment",
                        "detail": "Made satisfaction final and beyond judicial review.",
                    },
                    {
                        "id": "t3",
                        "year": 1978,
                        "label": "44th Amendment",
                        "detail": "Deleted finality — satisfaction again justiciable.",
                    },
                    {
                        "id": "t4",
                        "year": 1986,
                        "label": "D.C. Wadhwa",
                        "detail": "Re-promulgation as substitute for legislation struck down.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Pardoning Power",
        "slug": "pr-pardon",
        "sort_order": 11,
        "summary": (
            "Art. 72 forms of clemency (PCRRR); President vs Governor; Kehar Singh and Maru Ram on "
            "cabinet advice and limited judicial review."
        ),
        "body": (
            "## Art. 72 — when President can pardon\n\n"
            "1. Offence against a **Union law**\n"
            "2. Sentence by **court martial**\n"
            "3. Sentence of **death**\n\n"
            "Independent of judiciary — not a court of appeal. Objects: correct judicial error; "
            "relieve unduly harsh sentences.\n\n"
            "### PCRRR\n"
            "- **Pardon** — removes sentence + conviction; full absolution.\n"
            "- **Commutation** — heavier form → lighter form.\n"
            "- **Remission** — reduce period; character unchanged.\n"
            "- **Respite** — lesser sentence for special fact (e.g. pregnancy).\n"
            "- **Reprieve** — temporary stay (especially of death) to seek pardon/commutation.\n\n"
            "### vs Governor (Art. 161)\n"
            "- Governor: **no** court-martial pardon; **no** death **pardon** "
            "(even if state law prescribes death).\n"
            "- Both have concurrent power to **suspend, remit, commute** a death sentence.\n\n"
            "### Case law\n"
            "Kehar Singh (1988) / Maru Ram (1980): no right to oral hearing; President may re-appreciate "
            "evidence; exercise on **cabinet advice**; limited JR — irrelevant, irrational, mala fide, "
            "or discriminatory."
        ),
        "articles": [
            ("Art. 72", "Power of President to grant pardons etc. and to suspend, remit or commute sentences."),
            ("Art. 161", "Power of Governor to grant pardons etc."),
        ],
        "visual_blocks": [
            {
                "id": "pr-pardon-compare",
                "type": "comparison",
                "title": "Art. 72 President vs Art. 161 Governor",
                "columns": [
                    {
                        "id": "pres",
                        "heading": "President (Art. 72)",
                        "points": [
                            "Union-law offences",
                            "Court-martial sentences — yes",
                            "Death sentence — full pardon yes",
                            "Also suspend / remit / commute death",
                            "On Union cabinet advice",
                        ],
                    },
                    {
                        "id": "gov",
                        "heading": "Governor (Art. 161)",
                        "points": [
                            "State-law offences",
                            "Court-martial — no",
                            "Death — cannot pardon",
                            "Can suspend / remit / commute death",
                            "On state council advice",
                        ],
                    },
                ],
            },
            {
                "id": "pr-pardon-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic — PCRRR",
                "body": "Pardon · Commutation · Remission · Respite · Reprieve.",
            },
        ],
    },
    {
        "title": "Constitutional Position",
        "slug": "pr-constitutional-position",
        "sort_order": 12,
        "summary": (
            "Nominal executive under Arts 53, 74, 75; 42nd/44th advice loop; three situational "
            "discretions; Narayanan examples."
        ),
        "body": (
            "## Nominal, not real\n\n"
            "Parliamentary system → President is **nominal** executive; real executive is CoM headed by PM. "
            "Ambedkar: like the English King — head of State, not of the Executive; ceremonial seal.\n\n"
            "### Three articles\n"
            "1. **Art. 53** — executive power vested in President.\n"
            "2. **Art. 74** — CoM with PM to aid and advise; President **shall** act on advice.\n"
            "3. **Art. 75** — collective responsibility to **Lok Sabha** (foundation of parliamentary govt).\n\n"
            "### Advice loop\n"
            "- **42nd (1976):** advice made expressly binding.\n"
            "- **44th (1978):** President may return advice **once** for reconsideration; "
            "reconsidered advice is **binding**.\n\n"
            "**Examples:** K.R. Narayanan returned Art. 356 advice on UP (1997) — cabinet dropped it; "
            "returned Bihar advice (1998), then accepted re-advice (President’s Rule Feb 1999).\n\n"
            "### Situational discretion (no constitutional discretion otherwise)\n"
            "1. Appoint PM when no clear LS majority / no obvious successor on PM’s death.\n"
            "2. Dismiss CoM that cannot prove LS confidence.\n"
            "3. Dissolve LS if CoM has lost majority."
        ),
        "articles": [
            ("Art. 53", "Executive power of the Union."),
            ("Art. 74", "Council of Ministers to aid and advise the President."),
            ("Art. 75", "Other provisions as to ministers — collective responsibility to Lok Sabha."),
        ],
        "visual_blocks": [
            {
                "id": "pr-pos-model",
                "type": "mental_model",
                "title": "Ambedkar’s seal",
                "metaphor": "Nation’s seal",
                "topic_label": "Constitutional position",
                "subject_label": "Arts 53 · 74 · 75",
                "relation_label": "Keeps clear",
                "protects_from": [
                    "US-style presidential reading of Indian office",
                    "Ignoring binding ministerial advice",
                    "Missing the three situational discretion cases",
                ],
                "insight": (
                    "He represents the nation but does not rule the nation — "
                    "generally bound by ministers; nothing contrary to or without their advice."
                ),
            },
            {
                "id": "pr-pos-timeline",
                "type": "timeline",
                "title": "Binding advice — 42nd → 44th",
                "events": [
                    {
                        "id": "a42",
                        "year": 1976,
                        "label": "42nd Amendment",
                        "detail": "President shall act on CoM advice.",
                    },
                    {
                        "id": "a44",
                        "year": 1978,
                        "label": "44th Amendment",
                        "detail": "May return once; reconsidered advice binds.",
                    },
                    {
                        "id": "n97",
                        "year": 1997,
                        "label": "Narayanan — UP",
                        "detail": "Returned 356 advice; cabinet did not press.",
                    },
                    {
                        "id": "n98",
                        "year": 1999,
                        "label": "Narayanan — Bihar",
                        "detail": "Returned once in 1998; re-advice led to President’s Rule (Feb 1999).",
                    },
                ],
            },
        ],
    },
    {
        "title": "Articles & Reference Tables",
        "slug": "pr-articles-tables",
        "sort_order": 13,
        "summary": (
            "Table 18.3 article glance, veto summary, and vote-value idea for last-minute lookup."
        ),
        "body": (
            "## Core articles (Table 18.3 spine)\n\n"
            "| Article | Subject |\n"
            "|---|---|\n"
            "| 52 | The President of India |\n"
            "| 53 | Executive power of the Union |\n"
            "| 54–55 | Election & manner |\n"
            "| 56–57 | Term & re-election |\n"
            "| 58–60 | Qualifications, conditions, oath |\n"
            "| 61–62 | Impeachment & vacancy election |\n"
            "| 65 | VP acts / discharges |\n"
            "| 71 | Election disputes |\n"
            "| 72 | Pardons |\n"
            "| 74–75 | Aid & advice; ministers |\n"
            "| 76 | Attorney-General |\n"
            "| 77–78 | Conduct of business; PM’s duties |\n"
            "| 111 / 123 | Assent / ordinances |\n\n"
            "Vote values (Table 18.4 idea): MLA value from state population; MP value equalises "
            "total state votes with Parliament — parity, not a number to rote-memorise every year."
        ),
        "articles": [
            ("Arts 52–62, 65, 71–72, 74–78", "Principal constitutional provisions on the President."),
            ("Arts 111 & 123", "Assent to bills and ordinance-making power."),
        ],
        "visual_blocks": [
            {
                "id": "pr-article-explorer",
                "type": "article_explorer",
                "title": "President — article spine",
                "article_ref": "Arts 52–78 (selected)",
                "stages": [
                    {
                        "id": "office",
                        "label": "Office & election",
                        "detail": "52–62, 65, 71 — who is President, how chosen, term, vacancy.",
                    },
                    {
                        "id": "powers",
                        "label": "Key powers",
                        "detail": "72 (pardon), 111 (assent), 123 (ordinance), emergencies 352/356/360.",
                    },
                    {
                        "id": "position",
                        "label": "Aid & advice",
                        "detail": "53, 74, 75, 78 — nominal head + binding CoM advice.",
                    },
                ],
            },
            {
                "id": "pr-tables-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Last-minute scan",
                "body": (
                    "If short on time: Elect ≠ Impeach · three vetoes · 123 life-span · PCRRR · "
                    "42/44 advice · three situational discretions."
                ),
            },
        ],
    },
    {
        "title": "Prelims Traps, PYQ Themes & Mains VA",
        "slug": "pr-exam-kit",
        "sort_order": 14,
        "summary": (
            "High-yield prelims traps, recurring PYQ themes, and mains value-addition one-liners "
            "for the President chapter."
        ),
        "body": (
            "## Prelims traps\n\n"
            "- Electoral college ≠ impeachment participants.\n"
            "- Pocket vs suspensive vs absolute; no qualified veto; no veto on CA bills (24th).\n"
            "- Ordinance: either House in recess OK; both in session → void; max 6M+6W.\n"
            "- Governor cannot pardon court martial or death (but can suspend/remit/commute death).\n"
            "- Re-election unlimited in India.\n"
            "- 44th: return advice once, then bind.\n\n"
            "## PYQ themes\n\n"
            "College composition · impeachment majority · veto classification · Art. 123 · "
            "Art. 72 vs 161 · situational discretion · 42nd/44th.\n\n"
            "## Mains VA\n\n"
            "- Ambedkar seal quote (nominal head).\n"
            "- Federal representative via state MLAs in the college.\n"
            "- Situational discretion as safety valve in hung politics.\n"
            "- Ordinance as exceptional, not parallel, legislation (Wadhwa)."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pr-pyq-heat",
                "type": "pyq_heatmap",
                "title": "PYQ focus map",
                "items": [
                    {"concept_slug": "pr-election", "label": "Election"},
                    {"concept_slug": "pr-term-impeachment", "label": "Impeachment"},
                    {"concept_slug": "pr-veto", "label": "Veto"},
                    {"concept_slug": "pr-ordinance", "label": "Ordinance"},
                    {"concept_slug": "pr-pardon", "label": "Pardon"},
                    {"concept_slug": "pr-constitutional-position", "label": "Position"},
                ],
            },
            {
                "id": "pr-exam-traps",
                "type": "callout",
                "tone": "trap",
                "title": "Trap pack",
                "body": (
                    "Elect ≠ Impeach · pocket ≠ suspensive · ordinance ≠ emergency · "
                    "Governor ≠ full Art. 72 twin · CA bill assent mandatory."
                ),
            },
            {
                "id": "pr-exam-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "“He represents the nation but does not rule the nation” (Ambedkar) — "
                    "use with Arts 53/74/75 and the 44th reconsideration valve."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pr-election"),
    (HUB_SLUG, "parent", "pr-why-indirect"),
    (HUB_SLUG, "parent", "pr-qualifications-oath"),
    (HUB_SLUG, "parent", "pr-term-impeachment"),
    (HUB_SLUG, "parent", "pr-vacancy-succession"),
    (HUB_SLUG, "parent", "pr-powers-map"),
    (HUB_SLUG, "parent", "pr-executive-legislative"),
    (HUB_SLUG, "parent", "pr-other-powers"),
    (HUB_SLUG, "parent", "pr-veto"),
    (HUB_SLUG, "parent", "pr-ordinance"),
    (HUB_SLUG, "parent", "pr-pardon"),
    (HUB_SLUG, "parent", "pr-constitutional-position"),
    (HUB_SLUG, "parent", "pr-articles-tables"),
    (HUB_SLUG, "parent", "pr-exam-kit"),
    ("pr-election", "related", "pr-why-indirect"),
    ("pr-term-impeachment", "related", "pr-vacancy-succession"),
    ("pr-powers-map", "related", "pr-executive-legislative"),
    ("pr-powers-map", "related", "pr-other-powers"),
    ("pr-veto", "related", "pr-ordinance"),
    ("pr-pardon", "related", "pr-other-powers"),
    ("pr-constitutional-position", "related", "parliamentary-system"),
    ("pr-exam-kit", "related", "pr-election"),
    ("pr-exam-kit", "related", "pr-veto"),
    ("pr-exam-kit", "related", "pr-ordinance"),
    ("pr-ordinance", "related", "ordinance"),
    ("pr-other-powers", "related", "article-356"),
]

SAMPLE_PYQS = [
    (
        2018,
        "With reference to the election of the President of India, consider the electoral college. "
        "Which of the following do not take part in the election?",
        "Nominated members of Parliament and state legislative councils (MLCs) do not vote; "
        "dissolved assembly members also do not. Elected MLAs of Delhi and Puducherry do vote.",
        ["pr-election", HUB_SLUG],
    ),
    (
        2013,
        "Regarding the impeachment of the President, which statement is correct about who participates?",
        "Nominated members of Parliament can participate in impeachment though they do not elect; "
        "elected MLAs of states do not participate in impeachment though they elect.",
        ["pr-term-impeachment", HUB_SLUG],
    ),
    (
        2014,
        "Which of the following vetoes is/are available to the President of India?",
        "Absolute, suspensive, and pocket vetoes — not the qualified veto.",
        ["pr-veto", HUB_SLUG],
    ),
    (
        2015,
        "The President can promulgate an ordinance under Article 123 when:",
        "When both Houses or either House of Parliament is not in session, if immediate action is needed; "
        "maximum life roughly six months plus six weeks if not approved.",
        ["pr-ordinance", HUB_SLUG],
    ),
    (
        2012,
        "Difference between pardoning powers of the President and the Governor includes:",
        "President can pardon court-martial and death sentences; Governor cannot pardon court-martial "
        "or grant death pardon (but may suspend/remit/commute death).",
        ["pr-pardon", HUB_SLUG],
    ),
    (
        2016,
        "After the 44th Constitutional Amendment, advice of the Council of Ministers to the President:",
        "President may require reconsideration once; thereafter, reconsidered advice is binding.",
        ["pr-constitutional-position", HUB_SLUG],
    ),
]

LANDMARK_CASES = [
    {
        "title": "R.C. Cooper v. Union of India",
        "slug": "rc-cooper-ordinance",
        "parties": "R.C. Cooper v. Union of India",
        "year": 1970,
        "court": CaseLaw.Court.SC,
        "summary": "Bank nationalisation era case touching presidential ordinance satisfaction.",
        "holding": (
            "President’s satisfaction for issuing an ordinance can be questioned in court "
            "on the ground of mala fide."
        ),
        "concept_slugs": ["pr-ordinance", HUB_SLUG],
    },
    {
        "title": "D.C. Wadhwa v. State of Bihar",
        "slug": "dc-wadhwa",
        "parties": "D.C. Wadhwa v. State of Bihar",
        "year": 1986,
        "court": CaseLaw.Court.SC,
        "summary": "Governor’s re-promulgation of ordinances in Bihar without assembly passage.",
        "holding": (
            "Successive re-promulgation of ordinances with the same text without attempt to "
            "pass bills violates the Constitution; ordinance power is exceptional, not a substitute "
            "for the legislature."
        ),
        "concept_slugs": ["pr-ordinance", HUB_SLUG],
    },
    {
        "title": "Kehar Singh v. Union of India",
        "slug": "kehar-singh",
        "parties": "Kehar Singh v. Union of India",
        "year": 1988,
        "court": CaseLaw.Court.SC,
        "summary": "Principles governing presidential pardoning power under Article 72.",
        "holding": (
            "No right to oral hearing; President may re-examine evidence; power on cabinet advice; "
            "limited judicial review for irrelevant, irrational, mala fide or discriminatory decisions."
        ),
        "concept_slugs": ["pr-pardon", HUB_SLUG],
    },
    {
        "title": "Maru Ram v. Union of India",
        "slug": "maru-ram",
        "parties": "Maru Ram v. Union of India",
        "year": 1980,
        "court": CaseLaw.Court.SC,
        "summary": "Earlier articulation of cabinet advice and reviewability of clemency.",
        "holding": (
            "Pardoning power is to be exercised on the advice of the Council of Ministers; "
            "judicial review lies for mala fide or similarly vitiated decisions."
        ),
        "concept_slugs": ["pr-pardon", HUB_SLUG],
    },
]

AMENDMENTS = [
    {
        "number": 24,
        "year": 1971,
        "title": "Twenty-fourth Amendment",
        "summary": (
            "Made it obligatory for the President to give assent to a constitutional amendment bill."
        ),
        "effect": "No veto — absolute, suspensive, or pocket — on constitutional amendment bills.",
        "concept_slugs": ["pr-veto", HUB_SLUG],
    },
    {
        "number": 38,
        "year": 1975,
        "title": "Thirty-eighth Amendment",
        "summary": (
            "Made the President’s satisfaction for issuing ordinances final and beyond judicial review."
        ),
        "effect": "Later undone by the 44th Amendment — satisfaction again justiciable.",
        "concept_slugs": ["pr-ordinance", HUB_SLUG],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Among other changes, expressly bound the President to act on the aid and advice "
            "of the Council of Ministers."
        ),
        "effect": "Cemented the nominal character of the presidency under Art. 74.",
        "concept_slugs": ["pr-constitutional-position", HUB_SLUG],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": (
            "Allowed the President to return ministerial advice once for reconsideration; "
            "reconsidered advice binds. Also deleted 38th-era finality of ordinance satisfaction."
        ),
        "effect": "Advice loop: bind → return once → bind; ordinance satisfaction justiciable again.",
        "concept_slugs": ["pr-constitutional-position", "pr-ordinance", HUB_SLUG],
    },
    {
        "number": 104,
        "year": 2019,
        "title": "One Hundred and Fourth Amendment",
        "summary": (
            "Discontinued nomination of Anglo-Indian members to the Lok Sabha and state assemblies."
        ),
        "effect": "From 25 January 2020, President no longer nominates Anglo-Indians to the Lok Sabha.",
        "concept_slugs": ["pr-executive-legislative", "pr-election", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed President chapter (Laxmikanth Ch.18) under Part III Central Government."

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
                "title": "President",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 18",
                "summary": (
                    "Visual revision of Ch.18 — election, qualifications, impeachment, powers, "
                    "vetoes, ordinances, pardon, and constitutional position."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "President",
                "summary": (
                    "Constitutional head of the Indian State — nominal executive, first citizen, "
                    "and symbol of unity; Arts 52–78 in Part V."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **ceremonial seal** mental model, then "
                    "**Election** → **Impeachment** → **Vetoes** → **Ordinance** → **Pardon** → "
                    "**Constitutional position**. Finish with the **Exam kit**. "
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
            ref="Laxmikanth Ch. 18",
            excerpt=(
                "President — election, term, impeachment, powers, vetoes, "
                "ordinances, pardon, and constitutional position."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 52–78",
            excerpt="Union executive framework in Part V — President at the apex as nominal head.",
            sort_order=1,
        )

        pr_slugs = set(by_slug.keys())
        related_outside = {
            "parliamentary-system",
            "ordinance",
            "article-356",
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
                f"President chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
