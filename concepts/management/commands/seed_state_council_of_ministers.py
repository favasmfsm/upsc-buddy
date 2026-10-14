"""Seed Laxmikanth Ch.32 State Council of Ministers (visual revision)."""

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

HUB_SLUG = "state-council-of-ministers"
CHAPTER_SLUG = "state-council-of-ministers"

ENTRY_PILLARS = [
    {
        "id": "provisions",
        "articles": "163–164 · 166–167 · 177",
        "label": "Constitutional Provisions",
        "slug": "scom-constitutional-provisions",
        "detail": "Status, ministers, business rules, CM duties, House rights.",
        "tone": "teal",
    },
    {
        "id": "advice",
        "articles": "Art. 163 · Shamsher",
        "label": "Advice & Discretion",
        "slug": "scom-advice-and-discretion",
        "detail": "Aid & advice except discretion; Governor’s call is final; courts barred.",
        "tone": "olive",
    },
    {
        "id": "appoint",
        "articles": "Art. 164 · 94th",
        "label": "Appointment, Tribal Welfare, Oath",
        "slug": "scom-appointment-oath",
        "detail": "CM advises; tribal-welfare states; 6-month non-member rule.",
        "tone": "gold",
    },
    {
        "id": "collective",
        "articles": "Art. 164",
        "label": "Collective Responsibility",
        "slug": "scom-collective-responsibility",
        "detail": "One boat to the Assembly — no-confidence sinks the whole CoM.",
        "tone": "orange",
    },
    {
        "id": "individual",
        "articles": "Pleasure · UK contrast",
        "label": "Individual & No Legal Resp.",
        "slug": "scom-individual-no-legal",
        "detail": "CM can drop a minister; India has no UK-style legal responsibility.",
        "tone": "terracotta",
    },
    {
        "id": "composition",
        "articles": "C–M–D (+ Dy CM)",
        "label": "Composition",
        "slug": "scom-composition",
        "detail": "Cabinet / MoS / Deputy; departments not ministries.",
        "tone": "maroon",
    },
    {
        "id": "vs-cabinet",
        "articles": "Wider vs nucleus",
        "label": "CoM vs Cabinet",
        "slug": "scom-vs-cabinet",
        "detail": "Wider theory body vs smaller decision nucleus.",
        "tone": "teal",
    },
    {
        "id": "role",
        "articles": "8 roles · committees",
        "label": "Cabinet Role & Committees",
        "slug": "scom-cabinet-role",
        "detail": "Policy, crisis, appointments — standing & ad hoc committees.",
        "tone": "olive",
    },
    {
        "id": "vs-centre",
        "articles": "Centre ↔ State",
        "label": "Centre vs State CoM",
        "slug": "scom-centre-vs-state",
        "detail": "Article map, discretion, min 12, tribal welfare, Assembly.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "scom-team-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Team that steers while the Governor seals — except discretion",
        "topic_label": "State Council of Ministers",
        "subject_label": "Arts 163–164 · 166–167 · 177",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating Governor as always bound like the President under Art. 74",
            "Confusing Council of Ministers with the Cabinet",
            "Forgetting collective responsibility is to the Legislative Assembly",
            "Missing the 15% cap, min-12 floor, and tribal-welfare states",
        ],
        "insight": (
            "Real executive = Council of Ministers headed by the CM; "
            "the Governor acts on aid and advice except where the Constitution "
            "requires him/her to act in discretion."
        ),
    },
    {
        "id": "scom-entry-pillars",
        "type": "pillars",
        "title": "Nine revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "scom-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Arts **163–164–166–167–177**. "
            "Collective responsibility → **Legislative Assembly**. "
            "**91st**: CoM ≤ **15%** of Assembly + **min 12**; defection bars ministership. "
            "**94th**: tribal welfare in CG, JH, MP, Odisha. "
            "Scan Centre vs State → discretion → CoM vs Cabinet."
        ),
    },
    {
        "id": "scom-hub-heatmap",
        "type": "pyq_heatmap",
        "title": "PYQ focus (this chapter)",
        "items": [
            {"concept_slug": "scom-constitutional-provisions", "label": "15% / min 12"},
            {"concept_slug": "scom-advice-and-discretion", "label": "Governor discretion"},
            {"concept_slug": "scom-collective-responsibility", "label": "Collective to Assembly"},
            {"concept_slug": "scom-centre-vs-state", "label": "Centre vs State"},
            {"concept_slug": "scom-appointment-oath", "label": "Tribal welfare / 6 months"},
            {"concept_slug": "scom-vs-cabinet", "label": "CoM vs Cabinet"},
        ],
    },
]

CLUSTERS = [
    {
        "title": "Constitutional Provisions",
        "slug": "scom-constitutional-provisions",
        "sort_order": 1,
        "summary": (
            "Arts 163, 164, 166, 167 and 177 — status of CoM, ministers’ tenure rules, "
            "business of government, CM’s duties, and House rights."
        ),
        "body": (
            "## Article map (revision)\n\n"
            "- **Art. 163** — CoM with CM at the head aids and advises the Governor, "
            "**except** where the Governor must act in **discretion**; "
            "Governor’s decision on whether a matter is discretionary is **final**; "
            "nature of advice not inquired into by courts.\n"
            "- **Art. 164** — CM & ministers’ appointment; tribal welfare minister "
            "(CG, JH, MP, Odisha); **15%** cap + **min 12** (91st); defection bar (91st); "
            "pleasure of Governor; **collective responsibility to Legislative Assembly**; "
            "oath; **6-month** non-member rule; salaries by state legislature.\n"
            "- **Art. 166** — executive action in Governor’s name; authentication; "
            "rules for business allocation (except discretionary business).\n"
            "- **Art. 167** — CM must communicate CoM decisions, furnish information on call, "
            "and submit a minister’s solo decision to the CoM if the Governor requires.\n"
            "- **Art. 177** — every minister may speak in the Assembly (and Council where it "
            "exists) / committees named to — but **votes only in own House**.\n\n"
            "Principles of parliamentary government are only sketched in Arts 163–164; "
            "detail comes from convention and statute.\n\n"
            "**Mnemonic:** 163 status · 164 ministers · 166 business · 167 CM → Governor · 177 Houses."
        ),
        "articles": [
            (
                "Article 163",
                "Council of Ministers to aid and advise Governor; discretion exception; advice not justiciable.",
            ),
            (
                "Article 164",
                "Appointment, size, tribal welfare, defection bar, pleasure, collective responsibility, oath, 6 months, salaries.",
            ),
            (
                "Article 166",
                "Conduct of business of the Government of a State.",
            ),
            (
                "Article 167",
                "Duties of the Chief Minister as respects the Governor.",
            ),
            (
                "Article 177",
                "Rights of ministers as respects the Houses — speak yes, vote only in own House.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-arts-explorer",
                "type": "article_explorer",
                "title": "State CoM — article drill",
                "article_ref": "Arts 163–164 · 166–167 · 177",
                "stages": [
                    {
                        "id": "a163",
                        "label": "Art. 163 — Status",
                        "detail": (
                            "CoM headed by CM aids/advises Governor — except discretion. "
                            "Governor’s call on discretion is final; advice not justiciable."
                        ),
                    },
                    {
                        "id": "a164",
                        "label": "Art. 164 — Ministers",
                        "detail": (
                            "Appointment on CM advice; 15% Assembly cap + min 12; "
                            "defection bar; pleasure; collective to Assembly; oath; 6-month; salaries."
                        ),
                    },
                    {
                        "id": "a166",
                        "label": "Art. 166 — Business",
                        "detail": (
                            "Actions in Governor’s name; authenticated instruments; "
                            "rules for allocation — except discretionary business."
                        ),
                    },
                    {
                        "id": "a167",
                        "label": "Art. 167 — CM duties",
                        "detail": (
                            "Communicate decisions; furnish info when asked; "
                            "submit solo ministerial decisions to CoM if Governor requires."
                        ),
                    },
                    {
                        "id": "a177",
                        "label": "Art. 177 — House rights",
                        "detail": (
                            "Speak in Assembly (and Council if any) — vote only where "
                            "the minister is a member."
                        ),
                    },
                ],
            },
            {
                "id": "scom-arts-prelims",
                "type": "callout",
                "tone": "trap",
                "title": "Prelims facts — 91st Amendment (2003)",
                "body": (
                    "Total ministers including CM ≤ **15% of Legislative Assembly** strength. "
                    "But number shall **not be less than 12**. "
                    "A member disqualified for **defection** cannot be appointed minister. "
                    "All inserted into Art. 164. "
                    "Mnemonic: **15% ceiling · 12 floor · defection = no berth**."
                ),
            },
        ],
    },
    {
        "title": "Advice, Discretion & Cases",
        "slug": "scom-advice-and-discretion",
        "sort_order": 2,
        "summary": (
            "Aid and advice except where the Governor must act in discretion; "
            "advice is confidential; Shamsher Singh fixes the real-executive reading."
        ),
        "body": (
            "## Aid & advice with a State twist\n\n"
            "Art. 163: CoM headed by the CM aids and advises the Governor in the exercise "
            "of functions — **except** where the Governor is required to act in **discretion**.\n\n"
            "- If any question arises whether a matter is discretionary, the **Governor’s "
            "decision is final** — validity cannot be challenged on the ground that he/she "
            "ought or ought not to have acted in discretion.\n"
            "- Nature of advice tendered to the Governor **cannot be inquired into** by any court "
            "(confidential Governor–minister relationship).\n\n"
            "### Case (one-liner)\n"
            "- **Shamsher Singh (1974)** — except in spheres of discretion, the Governor "
            "must act on aid and advice of the CoM; ‘satisfaction of the Governor’ is not "
            "personal satisfaction but that of the CoM.\n\n"
            "**Exam hook:** Do not copy-paste the Centre’s 42nd/44th binding-advice story "
            "onto Art. 163 — the State differentiator is the **discretion carve-out**."
        ),
        "articles": [
            (
                "Article 163",
                "Aid and advice except discretion; Governor’s decision final; advice not justiciable.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-advice-flow",
                "type": "flowchart",
                "title": "Advice vs discretion (Art. 163)",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Is the function discretionary?",
                        "detail": "Constitution may require the Governor to act in discretion.",
                        "options": [
                            {"label": "Ordinary function", "next": "advice"},
                            {"label": "Discretionary function", "next": "discretion"},
                            {"label": "Doubt — is it discretionary?", "next": "governor-call"},
                        ],
                    },
                    {
                        "id": "advice",
                        "label": "Act on CoM aid & advice",
                        "detail": "Governor is not to act personally against or without CoM advice (Shamsher).",
                    },
                    {
                        "id": "discretion",
                        "label": "Governor acts in discretion",
                        "detail": "Constitutional carve-out — CoM advice does not bind here.",
                    },
                    {
                        "id": "governor-call",
                        "label": "Governor’s decision is final",
                        "detail": "Validity cannot be challenged on ‘ought / ought not’ grounds.",
                        "options": [
                            {"label": "Treats as ordinary", "next": "advice"},
                            {"label": "Treats as discretionary", "next": "discretion"},
                        ],
                    },
                ],
            },
            {
                "id": "scom-advice-cases",
                "type": "case_network",
                "title": "Real executive — State reading",
                "hub_label": "Art. 163 CoM",
                "cases": [
                    {
                        "id": "shamsher",
                        "label": "Shamsher Singh",
                        "year": 1974,
                        "detail": (
                            "Except discretion, Governor acts on CoM aid & advice; "
                            "satisfaction = CoM satisfaction."
                        ),
                        "case_slug": "shamsher-singh",
                    },
                ],
            },
            {
                "id": "scom-advice-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Mains / Prelims hook",
                "body": (
                    "Centre Art. 74 has no parallel ‘discretion’ clause in the same way. "
                    "State Art. 163 = aid & advice **plus** discretion exception + finality of "
                    "Governor’s classification. Pair with Governor chapter for examples."
                ),
            },
        ],
    },
    {
        "title": "Appointment, Tribal Welfare, Oath & Salary",
        "slug": "scom-appointment-oath",
        "sort_order": 3,
        "summary": (
            "Governor appoints CM and, on CM’s advice, other ministers; tribal-welfare "
            "minister in four states; oaths; six-month rule; salaries by state legislature."
        ),
        "body": (
            "## Appointment path\n\n"
            "- **CM** appointed by the Governor; **other ministers** only on the **CM’s advice**.\n"
            "- Usually members of either House of the state legislature. A **non-member** may "
            "be minister but must become a member (election or nomination) of either House "
            "within **six consecutive months** or cease to be minister.\n"
            "- Member of one House may speak in the other but **votes only in own House** "
            "(Art. 177).\n\n"
            "### Tribal welfare minister (Art. 164)\n"
            "Mandatory in **Chhattisgarh, Jharkhand, Madhya Pradesh, Odisha** "
            "(may also hold SC/BC welfare or other work).\n\n"
            "- Originally: Bihar, MP, Odisha.\n"
            "- **94th Amendment (2006)** — freed **Bihar** (no Scheduled Areas; tiny ST share); "
            "extended obligation to **Chhattisgarh** and **Jharkhand**.\n"
            "- Mnemonic: **Bihar out · CG & JH in · keep MP & Odisha**.\n\n"
            "### Oaths (Governor administers)\n"
            "**Office:** allegiance to Constitution; uphold sovereignty & integrity; "
            "discharge duties faithfully; do right without fear/favour/affection/ill-will.\n\n"
            "**Secrecy:** not reveal CoM matters except for due discharge of duties.\n\n"
            "### Salary\n"
            "Determined by the **state legislature**. Base like an MLA/MLC + rank-based "
            "sumptuary allowance, accommodation, TA, medical facilities, etc."
        ),
        "articles": [
            (
                "Article 164(1)",
                "CM appointed by Governor; other ministers on advice of the CM; tribal welfare minister in four states.",
            ),
            (
                "Article 164(6)–(8)",
                "Oaths by Governor; six-month membership rule; salaries by state legislature.",
            ),
            (
                "Article 177",
                "Ministers may speak in both Houses (where Council exists) but vote only in their own House.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-appoint-journey",
                "type": "journey",
                "title": "From recommendation to office",
                "stages": [
                    {
                        "id": "s1",
                        "label": "CM recommends",
                        "detail": "Governor can appoint only persons recommended by the CM.",
                    },
                    {
                        "id": "s2",
                        "label": "Governor appoints",
                        "detail": "Formal appointment under Art. 164.",
                    },
                    {
                        "id": "s3",
                        "label": "Oaths of office & secrecy",
                        "detail": "Administered by the Governor before entering office.",
                    },
                    {
                        "id": "s4",
                        "label": "6-month clock (if non-member)",
                        "detail": (
                            "Must join either House of the state legislature within six "
                            "consecutive months or cease to be minister."
                        ),
                    },
                ],
            },
            {
                "id": "scom-appoint-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Tribal welfare — 94th trap",
                "body": (
                    "Current list: **CG, JH, MP, Odisha** — not Bihar. "
                    "94th (2006) dropped Bihar and added the two new states. "
                    "Do not recite the original Bihar–MP–Odisha trio in exams."
                ),
            },
        ],
    },
    {
        "title": "Collective Responsibility",
        "slug": "scom-collective-responsibility",
        "sort_order": 4,
        "summary": (
            "Fundamental parliamentary principle — the whole Council is jointly responsible "
            "to the Legislative Assembly and sinks or swims together."
        ),
        "body": (
            "## One boat — Assembly tide\n\n"
            "Art. 164: CoM is **collectively responsible to the Legislative Assembly** "
            "(not the Legislative Council).\n\n"
            "- All ministers own **joint** responsibility for acts of omission and commission.\n"
            "- **No-confidence** against the CoM → **entire** ministry resigns — "
            "including ministers from the Legislative Council.\n"
            "- Resignation of the **CM** = resignation of the whole CoM "
            "(ministers need not resign separately).\n"
            "- Alternate path after defeat: advise Governor to **dissolve** the Assembly; "
            "Governor **need not oblige** a ministry that has lost confidence.\n\n"
            "### Cabinet solidarity\n"
            "Cabinet decisions bind all ministers (even dissenters in the meeting). "
            "Defend inside and outside the legislature — or **resign**.\n\n"
            "**Mnemonic:** Assembly sinks the boat; Council ministers drown too."
        ),
        "articles": [
            (
                "Article 164(2)",
                "The Council of Ministers shall be collectively responsible to the Legislative Assembly of the State.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-collective-model",
                "type": "mental_model",
                "title": "Mental model",
                "metaphor": "One boat on the Assembly tide",
                "topic_label": "Collective Responsibility",
                "subject_label": "Art. 164",
                "relation_label": "Means",
                "protects_from": [
                    "Thinking only Cabinet ministers resign on no-confidence",
                    "Saying responsibility is to both Houses equally",
                    "Assuming Governor must dissolve after defeat",
                ],
                "insight": (
                    "Team responsibility to the lower House — confidence lost, whole CoM goes."
                ),
            },
            {
                "id": "scom-collective-flow",
                "type": "flowchart",
                "title": "After a no-confidence motion",
                "root": "ncm",
                "steps": [
                    {
                        "id": "ncm",
                        "label": "Assembly passes no-confidence",
                        "detail": "Against the Council of Ministers as a whole.",
                        "options": [
                            {"label": "Resign path", "next": "resign"},
                            {"label": "Dissolution advice", "next": "dissolve"},
                        ],
                    },
                    {
                        "id": "resign",
                        "label": "Entire CoM resigns",
                        "detail": (
                            "Includes Legislative Council ministers. "
                            "CM’s resignation covers all."
                        ),
                    },
                    {
                        "id": "dissolve",
                        "label": "Advise dissolution of Assembly",
                        "detail": (
                            "Claim House no longer represents the electorate — "
                            "Governor may refuse."
                        ),
                        "options": [
                            {"label": "Governor refuses", "next": "must-go"},
                            {"label": "Governor dissolves", "next": "polls"},
                        ],
                    },
                    {
                        "id": "must-go",
                        "label": "Ministry must quit",
                        "detail": "Lost confidence — cannot cling on without House support.",
                    },
                    {
                        "id": "polls",
                        "label": "Fresh elections",
                        "detail": "Political reset — CoM still needed for aid & advice until new House settles.",
                    },
                ],
            },
            {
                "id": "scom-collective-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic",
                "body": (
                    "**One boat — Assembly tide.** "
                    "Cabinet decision = public defence or resignation. "
                    "High-yield: responsibility is to **Legislative Assembly only**."
                ),
            },
        ],
    },
    {
        "title": "Individual & No Legal Responsibility",
        "slug": "scom-individual-no-legal",
        "sort_order": 5,
        "summary": (
            "Ministers hold office during the pleasure of the Governor (via CM); "
            "India has no British-style legal responsibility / countersignature system."
        ),
        "body": (
            "## Individual responsibility\n\n"
            "Art. 164 — ministers hold office during the **pleasure of the Governor**. "
            "In practice the Governor removes a minister **only on the CM’s advice**.\n\n"
            "- CM can ask a minister to resign or advise dismissal even while the CoM "
            "enjoys Assembly confidence.\n"
            "- This power is the **instrument** of collective responsibility.\n\n"
            "## No legal responsibility (India ≠ Britain)\n\n"
            "- **Britain:** King’s order for a public act is countersigned by a minister; "
            "illegal order → minister liable (‘King can do no wrong’).\n"
            "- **India (states):** no constitutional countersignature / legal-responsibility "
            "system; courts barred from inquiring into advice to the Governor.\n\n"
            "**Mains VA:** Contrast UK legal responsibility with India’s political "
            "responsibility model — same at Centre and states."
        ),
        "articles": [
            (
                "Article 164",
                "Ministers hold office during the pleasure of the Governor.",
            ),
            (
                "Article 163(3)",
                "Advice tendered to the Governor shall not be inquired into in any court.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-resp-compare",
                "type": "comparison",
                "title": "Collective vs individual responsibility",
                "columns": [
                    {
                        "id": "collective",
                        "heading": "Collective",
                        "points": [
                            "Whole CoM answerable to Legislative Assembly",
                            "No-confidence sinks the team",
                            "Cabinet solidarity — defend or resign",
                            "Political responsibility to the House",
                        ],
                    },
                    {
                        "id": "individual",
                        "heading": "Individual",
                        "points": [
                            "Pleasure of Governor (via CM)",
                            "CM can drop a weak/dissenting minister",
                            "Tool to enforce collective responsibility",
                            "House confidence of CoM may still hold",
                        ],
                    },
                ],
            },
            {
                "id": "scom-legal-compare",
                "type": "comparison",
                "title": "Legal responsibility — Britain vs India",
                "columns": [
                    {
                        "id": "uk",
                        "heading": "Britain",
                        "points": [
                            "Countersignature of royal orders",
                            "Minister liable if order illegal",
                            "‘King can do no wrong’",
                        ],
                    },
                    {
                        "id": "in",
                        "heading": "India (states)",
                        "points": [
                            "No countersignature system in Constitution",
                            "No parallel ‘legal responsibility’ clause",
                            "Courts barred from probing advice (Art. 163)",
                        ],
                    },
                ],
            },
            {
                "id": "scom-indiv-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "Pleasure of Governor ≠ personal whim. Removal runs through the **CM**. "
                    "Same logic as Centre: individual responsibility is how collective "
                    "responsibility is enforced."
                ),
            },
        ],
    },
    {
        "title": "Composition of the Council",
        "slug": "scom-composition",
        "sort_order": 6,
        "summary": (
            "Three-tier CoM — Cabinet ministers, Ministers of State, Deputy ministers — "
            "plus optional Deputy CM; states use departments, not ministries."
        ),
        "body": (
            "## Ranks (C–M–D)\n\n"
            "Constitution does **not** specify size or ranking — CM decides by exigency "
            "(subject to the **91st** size cap). Difference = rank, emoluments, political weight. "
            "CM sits at the top as supreme governing authority in the state.\n\n"
            "1. **Cabinet ministers** — head important departments (home, education, finance, "
            "agriculture…); members of Cabinet; attend meetings; policy over the whole "
            "state government.\n"
            "2. **Ministers of state** — independent charge **or** attached to a Cabinet minister. "
            "Not Cabinet members; attend only if specially invited when their department "
            "is considered.\n"
            "3. **Deputy ministers** — no independent charge; attached to Cabinet ministers; "
            "assist in administrative, political and parliamentary duties; not in Cabinet.\n\n"
            "**Deputy CM** — appointed mostly for local political reasons; descriptive rank.\n\n"
            "### Naming trap\n"
            "The term ‘ministry / ministries’ is used at the **Centre**, not in the states. "
            "State government is divided into **departments**, not ministries."
        ),
        "articles": [
            (
                "Articles 163 & 164",
                "CoM is constitutional; size/classification of ranks not spelled out in detail (91st caps size).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-composition-tree",
                "type": "tree",
                "title": "Council hierarchy",
                "root": {
                    "id": "cm",
                    "label": "Chief Minister",
                    "detail": "Supreme governing authority of the Council",
                    "children": [
                        {
                            "id": "cabinet",
                            "label": "Cabinet Ministers",
                            "slug": "scom-composition",
                            "detail": "Cabinet members — key departments & policy",
                            "children": [
                                {
                                    "id": "mos",
                                    "label": "Ministers of State",
                                    "slug": "scom-composition",
                                    "detail": "Independent charge or attached",
                                    "children": [
                                        {
                                            "id": "deputy",
                                            "label": "Deputy Ministers",
                                            "slug": "scom-composition",
                                            "detail": "Assist only — no independent charge",
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "id": "dycm",
                            "label": "Deputy CM (optional)",
                            "slug": "scom-composition",
                            "detail": "Mostly for local political reasons",
                        },
                    ],
                },
            },
            {
                "id": "scom-composition-pillars",
                "type": "pillars",
                "title": "Three tiers + Deputy CM",
                "items": [
                    {
                        "id": "cab",
                        "articles": "Cabinet",
                        "label": "Cabinet Ministers",
                        "slug": "scom-composition",
                        "detail": "In Cabinet; key departments & policy.",
                        "tone": "teal",
                    },
                    {
                        "id": "mos",
                        "articles": "MoS",
                        "label": "Ministers of State",
                        "slug": "scom-composition",
                        "detail": "Independent or attached; invite-only to Cabinet.",
                        "tone": "olive",
                    },
                    {
                        "id": "dep",
                        "articles": "Deputy",
                        "label": "Deputy Ministers",
                        "slug": "scom-composition",
                        "detail": "Assist seniors; never independent charge.",
                        "tone": "gold",
                    },
                    {
                        "id": "dycm",
                        "articles": "Optional",
                        "label": "Deputy CM",
                        "slug": "scom-composition",
                        "detail": "Political convenience — descriptive rank.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "scom-composition-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic",
                "body": (
                    "**C–M–D** inside the Council; **Deputy CM** is optional politics. "
                    "States = **departments**, not ministries. "
                    "Cabinet ≠ all ministers — only cabinet-rank sit in Cabinet."
                ),
            },
        ],
    },
    {
        "title": "Council of Ministers vs Cabinet",
        "slug": "scom-vs-cabinet",
        "sort_order": 7,
        "summary": (
            "CoM is the wider constitutional body; Cabinet is the smaller decision-making "
            "nucleus that directs and speaks for the Council in practice."
        ),
        "body": (
            "## Do not use the words interchangeably\n\n"
            "- **CoM** — Arts **163–164**; all three ranks; rarely meets as a body; "
            "powers in **theory**; implements Cabinet decisions; size ≤ **15%** of Assembly "
            "and ≥ **12** (91st); collectively responsible to Legislative Assembly.\n"
            "- **Cabinet** — cabinet-rank only; nucleus of the CoM; real centre of authority "
            "in the state government; directs policy binding on all ministers.\n"
        ),
        "articles": [
            (
                "Articles 163 & 164",
                "Council of Ministers — constitutional body dealt with in detail.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-vs-cabinet-compare",
                "type": "comparison",
                "title": "CoM vs Cabinet (exam table)",
                "columns": [
                    {
                        "id": "com",
                        "heading": "Council of Ministers",
                        "points": [
                            "Wider body — all three ranks",
                            "Does not meet as a body / no collective functions",
                            "Powers in theory; implements Cabinet decisions",
                            "Arts 163–164; ≤ 15% of Assembly, min 12 (91st)",
                            "Collectively responsible to Legislative Assembly",
                        ],
                    },
                    {
                        "id": "cabinet",
                        "heading": "Cabinet",
                        "points": [
                            "Smaller — cabinet-rank only",
                            "Nucleus of the CoM; meets for decisions",
                            "Powers in practice; real centre of authority",
                            "Functions largely by convention",
                            "Enforces CoM’s collective responsibility",
                        ],
                    },
                ],
            },
            {
                "id": "scom-vs-cabinet-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Revision box",
                "body": (
                    "Cabinet is a **smaller body within** the CoM — not a rival. "
                    "In answers, say ‘Cabinet decides; CoM implements and is answerable "
                    "to the Assembly’."
                ),
            },
        ],
    },
    {
        "title": "Role of Cabinet & Committees",
        "slug": "scom-cabinet-role",
        "sort_order": 8,
        "summary": (
            "Eight roles of the state Cabinet plus standing and ad hoc cabinet committees "
            "set up by the CM."
        ),
        "body": (
            "## Eight roles (scan)\n\n"
            "1. Highest decision-making authority in the politico-administrative system of a state.\n"
            "2. Chief policy-formulating body of the state government.\n"
            "3. Supreme executive authority of the state government.\n"
            "4. Chief coordinator of the state administration.\n"
            "5. Advisory body to the Governor.\n"
            "6. Chief crisis manager — deals with all emergency situations.\n"
            "7. Deals with all major legislative and financial matters.\n"
            "8. Controls higher appointments (constitutional authorities and senior "
            "secretariat administrators).\n\n"
            "## Cabinet committees\n\n"
            "- Two types: **standing** (permanent) and **ad hoc** (temporary).\n"
            "- Set up by the **CM** as exigencies require — number, names, composition vary.\n"
            "- Sort issues, formulate proposals, and may take decisions; "
            "**Cabinet can review** committee decisions."
        ),
        "articles": [
            (
                "Articles 163 & 164",
                "Cabinet as nucleus of the CoM — roles largely conventional.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-cabinet-roles",
                "type": "pillars",
                "title": "Eight cabinet roles",
                "items": [
                    {
                        "id": "r1",
                        "articles": "1",
                        "label": "Highest decision body",
                        "slug": "scom-cabinet-role",
                        "detail": "Top politico-administrative decisions.",
                        "tone": "teal",
                    },
                    {
                        "id": "r2",
                        "articles": "2",
                        "label": "Policy engine",
                        "slug": "scom-cabinet-role",
                        "detail": "Chief policy-formulating body.",
                        "tone": "olive",
                    },
                    {
                        "id": "r3",
                        "articles": "3–4",
                        "label": "Executive & coordinator",
                        "slug": "scom-cabinet-role",
                        "detail": "Supreme executive; coordinates administration.",
                        "tone": "gold",
                    },
                    {
                        "id": "r4",
                        "articles": "5–6",
                        "label": "Advise & crisis",
                        "slug": "scom-cabinet-role",
                        "detail": "Advises Governor; manages emergencies.",
                        "tone": "orange",
                    },
                    {
                        "id": "r5",
                        "articles": "7–8",
                        "label": "Laws, money, posts",
                        "slug": "scom-cabinet-role",
                        "detail": "Legislative/financial matters; higher appointments.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "scom-committees-compare",
                "type": "comparison",
                "title": "Cabinet committees",
                "columns": [
                    {
                        "id": "standing",
                        "heading": "Standing",
                        "points": [
                            "Permanent nature",
                            "Set up by CM as needed",
                            "Names/composition vary over time",
                        ],
                    },
                    {
                        "id": "adhoc",
                        "heading": "Ad hoc",
                        "points": [
                            "Temporary nature",
                            "Created for specific exigencies",
                            "Cabinet can review their decisions",
                        ],
                    },
                ],
            },
            {
                "id": "scom-cabinet-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Mains VA pick-2",
                "body": (
                    "Pick two: Cabinet as **crisis manager** + **advisory body to Governor**; "
                    "or policy engine + higher appointments. Mention committees sort work "
                    "but Cabinet remains the reviewing authority."
                ),
            },
        ],
    },
    {
        "title": "Centre vs State Council of Ministers",
        "slug": "scom-centre-vs-state",
        "sort_order": 9,
        "summary": (
            "Parallel article map and State-only traps — discretion, min-12 floor, "
            "tribal welfare, Assembly responsibility, salary by state legislature."
        ),
        "body": (
            "## Article map (Centre ↔ State)\n\n"
            "| Theme | Centre | State |\n"
            "|-------|--------|-------|\n"
            "| Status / advice | Art. 74 | Art. 163 |\n"
            "| Ministers | Art. 75 | Art. 164 |\n"
            "| Business | Art. 77 | Art. 166 |\n"
            "| PM / CM duties | Art. 78 | Art. 167 |\n"
            "| House rights | Art. 88 | Art. 177 |\n\n"
            "## State-only traps\n\n"
            "- **Discretion carve-out** in Art. 163 (no Art. 74 twin).\n"
            "- Size: ≤ **15%** of Assembly **and** ≥ **12** (Centre has 15% of Lok Sabha; "
            "no constitutional min-12 floor).\n"
            "- **Tribal welfare minister** in CG, JH, MP, Odisha (94th).\n"
            "- Collective responsibility to **Legislative Assembly** (not Lok Sabha).\n"
            "- Salaries by **state legislature** (not Parliament).\n"
            "- States use **departments**, not ministries.\n\n"
            "Ch.32 has no kitchen-cabinet section — revise that from Central CoM if needed."
        ),
        "articles": [
            (
                "Articles 163–164 / 166–167 / 177",
                "State CoM cluster — parallel to Centre’s 74–75 / 77–78 / 88.",
            ),
            (
                "Articles 74–75 / 77–78 / 88",
                "Central CoM cluster — compare side by side for prelims.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "scom-centre-state-compare",
                "type": "comparison",
                "title": "Centre vs State CoM (exam table)",
                "columns": [
                    {
                        "id": "centre",
                        "heading": "Centre",
                        "points": [
                            "Arts 74–75 · 77–78 · 88",
                            "Aid & advice to President (42nd/44th binding path)",
                            "≤ 15% of Lok Sabha (no min-12 in Art. 75)",
                            "Collective responsibility to Lok Sabha",
                            "Salaries by Parliament",
                            "Ministries / Cabinet / kitchen cabinet themes",
                        ],
                    },
                    {
                        "id": "state",
                        "heading": "State",
                        "points": [
                            "Arts 163–164 · 166–167 · 177",
                            "Aid & advice to Governor — except discretion",
                            "≤ 15% of Assembly + min 12 (91st)",
                            "Collective responsibility to Legislative Assembly",
                            "Salaries by state legislature",
                            "Departments; tribal welfare in four states (94th)",
                        ],
                    },
                ],
            },
            {
                "id": "scom-centre-state-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Last-minute checklist",
                "body": (
                    "If a question mixes Centre and State: check **House of responsibility**, "
                    "**size floor (12)**, **discretion**, and **tribal-welfare states** first. "
                    "Article twins: 74↔163, 75↔164, 77↔166, 78↔167, 88↔177."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "scom-constitutional-provisions"),
    (HUB_SLUG, "parent", "scom-advice-and-discretion"),
    (HUB_SLUG, "parent", "scom-appointment-oath"),
    (HUB_SLUG, "parent", "scom-collective-responsibility"),
    (HUB_SLUG, "parent", "scom-individual-no-legal"),
    (HUB_SLUG, "parent", "scom-composition"),
    (HUB_SLUG, "parent", "scom-vs-cabinet"),
    (HUB_SLUG, "parent", "scom-cabinet-role"),
    (HUB_SLUG, "parent", "scom-centre-vs-state"),
    ("scom-constitutional-provisions", "related", "scom-advice-and-discretion"),
    ("scom-advice-and-discretion", "related", "scom-appointment-oath"),
    ("scom-collective-responsibility", "related", "scom-individual-no-legal"),
    ("scom-composition", "related", "scom-vs-cabinet"),
    ("scom-vs-cabinet", "related", "scom-cabinet-role"),
    ("scom-cabinet-role", "related", "scom-centre-vs-state"),
    ("scom-collective-responsibility", "related", "scom-vs-cabinet"),
    (HUB_SLUG, "related", "central-council-of-ministers"),
    (HUB_SLUG, "related", "parliamentary-system"),
    ("scom-centre-vs-state", "related", "central-council-of-ministers"),
    ("scom-advice-and-discretion", "related", "governor"),
]

AMENDMENTS = [
    {
        "number": 91,
        "year": 2003,
        "title": "Ninety-first Amendment",
        "summary": (
            "Capped the size of the Council of Ministers and barred defection-disqualified "
            "members from ministership — at Centre and in the states."
        ),
        "effect": (
            "Art. 164: ministers including CM ≤ 15% of Legislative Assembly strength, "
            "and not less than 12; defection → cannot be appointed minister."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "scom-constitutional-provisions",
            "scom-composition",
            "scom-centre-vs-state",
        ],
    },
    {
        "number": 94,
        "year": 2006,
        "title": "Ninety-fourth Amendment",
        "summary": (
            "Changed the roster of states that must have a minister in charge of tribal welfare."
        ),
        "effect": (
            "Freed Bihar from the tribal-welfare minister obligation; extended it to "
            "Chhattisgarh and Jharkhand (with Madhya Pradesh and Odisha retained)."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "scom-appointment-oath",
            "scom-constitutional-provisions",
            "scom-centre-vs-state",
        ],
    },
]

LANDMARK_CASES = [
    {
        "title": "Shamsher Singh v. State of Punjab",
        "slug": "shamsher-singh",
        "parties": "Shamsher Singh v. State of Punjab",
        "year": 1974,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Except where the Governor is to act in discretion, the Governor must act on "
            "the aid and advice of the Council of Ministers; ‘satisfaction’ means CoM satisfaction."
        ),
        "holding": (
            "The Governor is not required to act personally without or against the aid and "
            "advice of the CoM outside discretionary spheres; wherever the Constitution "
            "requires the satisfaction of the Governor, it is the satisfaction of the CoM."
        ),
        "concept_slugs": [HUB_SLUG, "scom-advice-and-discretion"],
    },
]

SAMPLE_PYQS = [
    (
        2013,
        (
            "Consider the following statements regarding the State Council of Ministers: "
            "It is collectively responsible to the Legislative Assembly of the state. "
            "Which of the following is correct regarding this principle?"
        ),
        (
            "Collective responsibility under Art. 164 means the whole CoM (including "
            "Legislative Council ministers) must resign if the Assembly passes no-confidence; "
            "Cabinet solidarity applies."
        ),
        ["scom-collective-responsibility", HUB_SLUG],
    ),
    (
        2015,
        (
            "With reference to the Council of Ministers in a state, which of the following "
            "is/are correct? The total number of ministers including the Chief Minister "
            "shall not exceed 15% of the total strength of the Legislative Assembly, "
            "and shall not be less than 12."
        ),
        (
            "Both the 15% ceiling and the minimum of 12 ministers (including CM) were "
            "inserted by the 91st Constitutional Amendment Act, 2003 (Art. 164)."
        ),
        ["scom-constitutional-provisions", HUB_SLUG],
    ),
    (
        2017,
        (
            "In which of the following states is there a constitutional requirement "
            "for a minister in charge of tribal welfare?"
        ),
        (
            "Chhattisgarh, Jharkhand, Madhya Pradesh and Odisha (Art. 164; 94th Amendment "
            "removed Bihar and added CG & JH)."
        ),
        ["scom-appointment-oath", HUB_SLUG],
    ),
    (
        2019,
        (
            "A person who is not a member of the state legislature can be appointed "
            "a minister, but must become a member within:"
        ),
        "Six consecutive months — else ceases to be a minister (Art. 164).",
        ["scom-appointment-oath", HUB_SLUG],
    ),
    (
        2021,
        (
            "Which of the following correctly distinguishes the State Council of Ministers "
            "from the Cabinet?"
        ),
        (
            "CoM is the wider body of all ranks; Cabinet is the smaller cabinet-rank nucleus "
            "and the real centre of authority in the state government."
        ),
        ["scom-vs-cabinet", HUB_SLUG],
    ),
    (
        2022,
        (
            "Under Article 163, if a question arises whether a matter falls within the "
            "Governor’s discretion, whose decision is final?"
        ),
        (
            "The decision of the Governor is final; validity cannot be questioned on the "
            "ground that he/she ought or ought not to have acted in discretion."
        ),
        ["scom-advice-and-discretion", HUB_SLUG],
    ),
]


class Command(BaseCommand):
    help = "Seed State Council of Ministers chapter (Laxmikanth Ch.32)."

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
                "title": "State Council of Ministers",
                "sort_order": 3,
                "book_ref": "Laxmikanth 8th Ed, Ch. 32, pp. 474–479",
                "summary": (
                    "Visual revision of Ch.32 — Arts 163–164/166–167/177, advice & discretion, "
                    "collective/individual responsibility, CoM vs Cabinet, Centre vs State."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "State Council of Ministers",
                "summary": (
                    "Real executive headed by the CM — aid and advice (except discretion), "
                    "responsibility to the Assembly, ranks, and Cabinet as the decision nucleus."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **team that steers while the Governor seals — except "
                    "discretion** mental model, then **Provisions** → **Advice & discretion** → "
                    "**Collective responsibility**. "
                    "Finish with **CoM vs Cabinet**, **Cabinet role**, and **Centre vs State**. "
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
            ref="Laxmikanth Ch. 32",
            excerpt=(
                "State Council of Ministers — Arts 163–164, 166–167, 177; "
                "responsibility, composition, CoM vs Cabinet, Centre vs State."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 163 & 164",
            excerpt=(
                "Aid and advice (except discretion); appointment, size, collective "
                "responsibility to Legislative Assembly."
            ),
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 166, 167 & 177",
            excerpt=(
                "Business of state government; CM’s duties to Governor; "
                "ministers’ rights in the Houses."
            ),
            sort_order=2,
        )

        scom_slugs = set(by_slug.keys())
        related_outside = {
            "parliamentary-system",
            "central-council-of-ministers",
            "governor",
        }
        ConceptEdge.objects.filter(
            source__slug__in=scom_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=scom_slugs | related_outside).delete()

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

        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="state-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"State Council of Ministers chapter seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(LANDMARK_CASES)} cases, "
                f"{len(AMENDMENTS)} amendments linked, {len(SAMPLE_PYQS)} PYQs."
            )
        )
