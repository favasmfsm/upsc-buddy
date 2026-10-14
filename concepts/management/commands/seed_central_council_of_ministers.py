"""Seed Laxmikanth Ch.21 Central Council of Ministers (visual revision)."""

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

HUB_SLUG = "central-council-of-ministers"
CHAPTER_SLUG = "central-council-of-ministers"

ENTRY_PILLARS = [
    {
        "id": "provisions",
        "articles": "74–75 · 77–78 · 88",
        "label": "Constitutional Provisions",
        "slug": "com-constitutional-provisions",
        "detail": "Status, appointment, business rules, PM duties, House rights.",
        "tone": "teal",
    },
    {
        "id": "advice",
        "articles": "42nd / 44th",
        "label": "Advice & Cases",
        "slug": "com-advice-and-cases",
        "detail": "Binding aid & advice; Rao & Shamsher; courts barred from advice.",
        "tone": "olive",
    },
    {
        "id": "appoint",
        "articles": "Art. 75 · 6 months",
        "label": "Appointment, Oath & Salary",
        "slug": "com-appointment-oath",
        "detail": "PM advises; non-MP window; oaths; Deputy PM descriptive only.",
        "tone": "gold",
    },
    {
        "id": "collective",
        "articles": "Art. 75",
        "label": "Collective Responsibility",
        "slug": "com-collective-responsibility",
        "detail": "One boat to Lok Sabha — no-confidence sinks the whole CoM.",
        "tone": "orange",
    },
    {
        "id": "individual",
        "articles": "Pleasure · UK contrast",
        "label": "Individual & No Legal Resp.",
        "slug": "com-individual-no-legal",
        "detail": "PM can drop a minister; India has no UK-style legal responsibility.",
        "tone": "terracotta",
    },
    {
        "id": "composition",
        "articles": "C–M–D (+ PS)",
        "label": "Composition",
        "slug": "com-composition",
        "detail": "Cabinet / MoS / Deputy; Parliamentary Secretaries outside CoM.",
        "tone": "maroon",
    },
    {
        "id": "vs-cabinet",
        "articles": "Table 21.1",
        "label": "CoM vs Cabinet",
        "slug": "com-vs-cabinet",
        "detail": "Wider theory body vs smaller decision nucleus (Art. 352 define).",
        "tone": "teal",
    },
    {
        "id": "role",
        "articles": "9 roles",
        "label": "Role of Cabinet",
        "slug": "com-cabinet-role",
        "detail": "Policy, crisis, foreign affairs — plus classic quote bank.",
        "tone": "olive",
    },
    {
        "id": "kitchen",
        "articles": "Inner circle",
        "label": "Kitchen Cabinet",
        "slug": "com-kitchen-cabinet",
        "detail": "Circle within a circle — cooked then tabled for formal approval.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "com-team-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Team that steers while the President seals",
        "topic_label": "Central Council of Ministers",
        "subject_label": "Arts 74–75 · 77–78 · 88",
        "relation_label": "Protects you from",
        "protects_from": [
            "Confusing Council of Ministers with the Cabinet",
            "Treating presidential advice as optional after 42nd/44th",
            "Forgetting collective responsibility is to the Lok Sabha",
            "Missing the 15% size cap and 6-month non-MP rule",
        ],
        "insight": (
            "Real executive = Council of Ministers headed by the PM; "
            "the President acts on its aid and advice."
        ),
    },
    {
        "id": "com-entry-pillars",
        "type": "pillars",
        "title": "Nine revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "com-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Arts **74–75–77–78–88**. "
            "Collective responsibility → **Lok Sabha**. "
            "**91st** Amendment: CoM ≤ **15%** of Lok Sabha strength; defection bars ministership. "
            "Scan CoM vs Cabinet → collective vs individual → kitchen cabinet."
        ),
    },
    {
        "id": "com-hub-heatmap",
        "type": "pyq_heatmap",
        "title": "PYQ focus (this chapter)",
        "items": [
            {"concept_slug": "com-collective-responsibility", "label": "Collective responsibility"},
            {"concept_slug": "com-vs-cabinet", "label": "CoM vs Cabinet"},
            {"concept_slug": "com-advice-and-cases", "label": "Binding advice"},
            {"concept_slug": "com-constitutional-provisions", "label": "15% / Arts"},
            {"concept_slug": "com-appointment-oath", "label": "Non-MP / 6 months"},
            {"concept_slug": "com-kitchen-cabinet", "label": "Kitchen cabinet"},
        ],
    },
]

CLUSTERS = [
    {
        "title": "Constitutional Provisions",
        "slug": "com-constitutional-provisions",
        "sort_order": 1,
        "summary": (
            "Arts 74, 75, 77, 78 and 88 — status of CoM, ministers’ tenure rules, "
            "business of government, PM’s duties, and House rights."
        ),
        "body": (
            "## Article map (revision)\n\n"
            "- **Art. 74** — CoM with PM at the head aids and advises the President; "
            "advice binding after reconsideration; nature of advice not inquired into by courts.\n"
            "- **Art. 75** — appointment; **15%** cap (91st); defection bar (91st); "
            "pleasure of President; **collective responsibility to Lok Sabha**; oath; "
            "**6-month** non-member rule; salaries by Parliament.\n"
            "- **Art. 77** — executive action in President’s name; authentication; "
            "rules for business allocation among ministers.\n"
            "- **Art. 78** — PM must communicate CoM decisions, furnish information on call, "
            "and submit a minister’s solo decision to the CoM if the President requires.\n"
            "- **Art. 88** — every minister may speak in either House / joint sitting / committees "
            "named to — but **votes only in own House**.\n\n"
            "Principles of parliamentary government are only sketched in Arts 74–75; "
            "detail comes from convention and statute."
        ),
        "articles": [
            (
                "Article 74",
                "Council of Ministers to aid and advise the President; advice not justiciable.",
            ),
            (
                "Article 75",
                "Appointment, size, defection bar, pleasure, collective responsibility, oath, 6 months, salaries.",
            ),
            (
                "Article 77",
                "Conduct of business of the Government of India.",
            ),
            (
                "Article 78",
                "Duties of the Prime Minister as respects the President.",
            ),
            (
                "Article 88",
                "Rights of ministers as respects the Houses — speak yes, vote only in own House.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-arts-explorer",
                "type": "article_explorer",
                "title": "Central CoM — article drill",
                "article_ref": "Arts 74–75 · 77–78 · 88",
                "stages": [
                    {
                        "id": "a74",
                        "label": "Art. 74 — Status",
                        "detail": (
                            "CoM headed by PM aids/advises President. "
                            "42nd/44th: advice binding; may reconsider once, then must follow."
                        ),
                    },
                    {
                        "id": "a75",
                        "label": "Art. 75 — Ministers",
                        "detail": (
                            "Appointment on PM advice; 15% LS cap; defection bar; "
                            "pleasure; collective to Lok Sabha; oath; 6-month rule; salaries."
                        ),
                    },
                    {
                        "id": "a77",
                        "label": "Art. 77 — Business",
                        "detail": (
                            "Actions in President’s name; authenticated instruments; "
                            "rules for allocation of business among ministers."
                        ),
                    },
                    {
                        "id": "a78",
                        "label": "Art. 78 — PM duties",
                        "detail": (
                            "Communicate decisions; furnish info when asked; "
                            "submit solo ministerial decisions to CoM if President requires."
                        ),
                    },
                    {
                        "id": "a88",
                        "label": "Art. 88 — House rights",
                        "detail": "Speak in either House — vote only where the minister is a member.",
                    },
                ],
            },
            {
                "id": "com-arts-prelims",
                "type": "callout",
                "tone": "trap",
                "title": "Prelims facts — 91st Amendment (2003)",
                "body": (
                    "Total ministers including PM ≤ **15% of Lok Sabha** strength. "
                    "A member disqualified for **defection** cannot be appointed minister. "
                    "Both inserted into Art. 75."
                ),
            },
        ],
    },
    {
        "title": "Nature of Advice & Landmark Cases",
        "slug": "com-advice-and-cases",
        "sort_order": 2,
        "summary": (
            "Aid and advice is binding after the 42nd/44th path; courts cannot inquire into "
            "the advice — Rao and Shamsher fix the real-executive reading."
        ),
        "body": (
            "## Binding advice (exam spine)\n\n"
            "Art. 74: CoM aids and advises the President.\n\n"
            "- **42nd Amendment** — President shall act in accordance with the advice.\n"
            "- **44th Amendment** — President may require **reconsideration once**; "
            "must then act on the advice tendered after reconsideration.\n"
            "- Art. 74(2) — nature of advice **not inquired into** by any court "
            "(confidential President–minister relationship).\n\n"
            "### Cases (one-liners)\n"
            "- **U.N.R. Rao (1971)** — even after Lok Sabha dissolution, CoM continues; "
            "President cannot exercise executive power without CoM (Art. 74 mandatory).\n"
            "- **Shamsher Singh (1974)** — ‘satisfaction of the President’ = satisfaction "
            "of the CoM with whose aid and advice powers are exercised.\n"
        ),
        "articles": [
            (
                "Article 74",
                "Aid and advice; reconsideration proviso; advice not justiciable.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-advice-flow",
                "type": "flowchart",
                "title": "Advice path (Art. 74)",
                "root": "tender",
                "steps": [
                    {
                        "id": "tender",
                        "label": "CoM tenders advice",
                        "detail": "PM-headed Council aids and advises the President.",
                        "options": [
                            {"label": "President acts on it", "next": "bind"},
                            {"label": "President asks to reconsider", "next": "reconsider"},
                        ],
                    },
                    {
                        "id": "reconsider",
                        "label": "Reconsideration (44th)",
                        "detail": "One reconsideration window — then advice returns.",
                        "options": [
                            {"label": "Advice after reconsideration", "next": "bind"},
                        ],
                    },
                    {
                        "id": "bind",
                        "label": "President must act on advice",
                        "detail": "42nd/44th — binding real-executive model. Courts cannot probe the advice (74(2)).",
                    },
                ],
            },
            {
                "id": "com-advice-cases",
                "type": "case_network",
                "title": "Advice & real executive — cases",
                "hub_label": "Art. 74 CoM",
                "cases": [
                    {
                        "id": "rao",
                        "label": "U.N.R. Rao",
                        "year": 1971,
                        "detail": "CoM continues after LS dissolution; no executive power without CoM.",
                        "case_slug": "unr-rao",
                    },
                    {
                        "id": "shamsher",
                        "label": "Shamsher Singh",
                        "year": 1974,
                        "detail": "Presidential ‘satisfaction’ = CoM satisfaction.",
                        "case_slug": "shamsher-singh",
                    },
                ],
            },
            {
                "id": "com-advice-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Mains / Prelims hook",
                "body": (
                    "Do not say advice is ‘optional’. Say: binding, with a one-time reconsider. "
                    "Pair with Parliamentary System features (nominal vs real executive)."
                ),
            },
        ],
    },
    {
        "title": "Appointment, Oath & Salary",
        "slug": "com-appointment-oath",
        "sort_order": 3,
        "summary": (
            "President appoints PM and, on PM’s advice, other ministers; oaths of office "
            "and secrecy; six-month rule for non-members; salaries by Parliament."
        ),
        "body": (
            "## Appointment path\n\n"
            "- **PM** appointed by the President; **other ministers** only on the **PM’s advice**.\n"
            "- Usually MPs (either House). A **non-member** may be minister but must become "
            "a member of either House within **six consecutive months** or cease to be minister.\n"
            "- Member of one House may speak in the other (Art. 88) but **votes only in own House**.\n\n"
            "### Oaths (President administers)\n"
            "**Office:** allegiance to Constitution; uphold sovereignty & integrity; "
            "discharge duties faithfully; do right without fear/favour/affection/ill-will.\n\n"
            "**Secrecy:** not reveal CoM matters except for due discharge of duties.\n\n"
            "### Deputy PM trap\n"
            "Constitution mentions PM and ministers — not ‘Deputy PM’. "
            "SC upheld Devi Lal’s 1990 oath: ‘Deputy PM’ is **descriptive only** — "
            "no extra powers of PM; oath valid if substantive part is correct.\n\n"
            "### Salary\n"
            "Determined by Parliament (Salaries and Allowances of Ministers Act, 1952). "
            "Base like an MP + rank-based sumptuary / facilities — skip memorising old ₹ figures."
        ),
        "articles": [
            (
                "Article 75(1)",
                "PM appointed by President; other ministers on advice of the PM.",
            ),
            (
                "Article 75(6)–(8)",
                "Oaths by President; six-month membership rule; salaries by Parliament.",
            ),
            (
                "Article 88",
                "Ministers may speak in either House but vote only in their own House.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-appoint-journey",
                "type": "journey",
                "title": "From recommendation to office",
                "stages": [
                    {
                        "id": "s1",
                        "label": "PM recommends",
                        "detail": "President can appoint only persons recommended by the PM.",
                    },
                    {
                        "id": "s2",
                        "label": "President appoints",
                        "detail": "Formal appointment under Art. 75.",
                    },
                    {
                        "id": "s3",
                        "label": "Oaths of office & secrecy",
                        "detail": "Administered by the President before entering office.",
                    },
                    {
                        "id": "s4",
                        "label": "6-month clock (if non-MP)",
                        "detail": "Must join either House within six consecutive months or cease to be minister.",
                    },
                ],
            },
            {
                "id": "com-appoint-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Deputy PM / MoS labels",
                "body": (
                    "‘Deputy Prime Minister’, ‘Minister of State’, ‘Deputy Minister’ — "
                    "labels do not create a separate constitutional office with PM powers. "
                    "Oath stands if the substantive text is correct."
                ),
            },
        ],
    },
    {
        "title": "Collective Responsibility",
        "slug": "com-collective-responsibility",
        "sort_order": 4,
        "summary": (
            "Fundamental parliamentary principle — the whole Council is jointly responsible "
            "to the Lok Sabha and sinks or swims together."
        ),
        "body": (
            "## One boat — Lok Sabha tide\n\n"
            "Art. 75: CoM is **collectively responsible to the Lok Sabha** "
            "(not the Rajya Sabha).\n\n"
            "- All ministers own **joint** responsibility for acts of omission and commission.\n"
            "- **No-confidence** against the CoM → **entire** ministry resigns — "
            "including ministers from the Rajya Sabha.\n"
            "- Resignation of the **PM** = resignation of the whole CoM "
            "(ministers need not resign separately).\n"
            "- Alternate path after defeat: advise President to **dissolve** Lok Sabha; "
            "President **need not oblige** a ministry that has lost confidence.\n\n"
            "### Cabinet solidarity\n"
            "Cabinet decisions bind all ministers (even dissenters in the meeting). "
            "Defend inside and outside Parliament — or **resign**.\n\n"
            "Examples: Ambedkar (Hindu Code Bill, 1953); C.D. Deshmukh (states reorganisation); "
            "Arif Mohammed (Muslim Women Act, 1986)."
        ),
        "articles": [
            (
                "Article 75(3)",
                "The Council of Ministers shall be collectively responsible to the Lok Sabha.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-collective-model",
                "type": "mental_model",
                "title": "Mental model",
                "metaphor": "One boat on the Lok Sabha tide",
                "topic_label": "Collective Responsibility",
                "subject_label": "Art. 75",
                "relation_label": "Means",
                "protects_from": [
                    "Thinking only Cabinet ministers resign on no-confidence",
                    "Saying responsibility is to both Houses equally",
                    "Allowing open dissent after a Cabinet decision",
                ],
                "insight": (
                    "Team responsibility to the lower House — confidence lost, whole CoM goes."
                ),
            },
            {
                "id": "com-collective-flow",
                "type": "flowchart",
                "title": "After a no-confidence motion",
                "root": "ncm",
                "steps": [
                    {
                        "id": "ncm",
                        "label": "Lok Sabha passes no-confidence",
                        "detail": "Against the Council of Ministers as a whole.",
                        "options": [
                            {"label": "Resign path", "next": "resign"},
                            {"label": "Dissolution advice", "next": "dissolve"},
                        ],
                    },
                    {
                        "id": "resign",
                        "label": "Entire CoM resigns",
                        "detail": "Includes Rajya Sabha ministers. PM’s resignation covers all.",
                    },
                    {
                        "id": "dissolve",
                        "label": "Advise dissolution of Lok Sabha",
                        "detail": "Claim House no longer represents the electorate — President may refuse.",
                        "options": [
                            {"label": "President refuses", "next": "must-go"},
                            {"label": "President dissolves", "next": "polls"},
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
                "id": "com-collective-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic",
                "body": (
                    "**One boat — Lok Sabha tide.** "
                    "Cabinet decision = public defence or resignation. "
                    "High-yield: responsibility is to **Lok Sabha only**."
                ),
            },
        ],
    },
    {
        "title": "Individual & No Legal Responsibility",
        "slug": "com-individual-no-legal",
        "sort_order": 5,
        "summary": (
            "Ministers hold office during the pleasure of the President (via PM); "
            "India has no British-style legal responsibility / countersignature system."
        ),
        "body": (
            "## Individual responsibility\n\n"
            "Art. 75 — ministers hold office during the **pleasure of the President**. "
            "In practice the President removes a minister **only on the PM’s advice**.\n\n"
            "- PM can ask a minister to resign or advise dismissal even while the CoM "
            "enjoys Lok Sabha confidence.\n"
            "- This power is the **instrument** of collective responsibility "
            "(Ambedkar: without PM’s power to nominate and dismiss, no collective responsibility).\n\n"
            "## No legal responsibility (India ≠ Britain)\n\n"
            "- **Britain:** King’s order for a public act is countersigned by a minister; "
            "illegal order → minister liable (‘King can do no wrong’).\n"
            "- **India:** no constitutional countersignature / legal-responsibility system; "
            "courts barred from inquiring into advice to the President.\n\n"
            "**Mains VA:** Quote Ambedkar on PM as the hinge of collective responsibility; "
            "contrast UK legal responsibility with India’s political responsibility model."
        ),
        "articles": [
            (
                "Article 75(2)",
                "Ministers hold office during the pleasure of the President.",
            ),
            (
                "Article 74(2)",
                "Advice tendered to the President shall not be inquired into in any court.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-resp-compare",
                "type": "comparison",
                "title": "Collective vs individual responsibility",
                "columns": [
                    {
                        "id": "collective",
                        "heading": "Collective",
                        "points": [
                            "Whole CoM answerable to Lok Sabha",
                            "No-confidence sinks the team",
                            "Cabinet solidarity — defend or resign",
                            "Political responsibility to the House",
                        ],
                    },
                    {
                        "id": "individual",
                        "heading": "Individual",
                        "points": [
                            "Pleasure of President (via PM)",
                            "PM can drop a weak/dissenting minister",
                            "Tool to enforce collective responsibility",
                            "House confidence of CoM may still hold",
                        ],
                    },
                ],
            },
            {
                "id": "com-legal-compare",
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
                        "heading": "India",
                        "points": [
                            "No countersignature system in Constitution",
                            "No parallel ‘legal responsibility’ clause",
                            "Courts barred from probing advice (Art. 74(2))",
                        ],
                    },
                ],
            },
            {
                "id": "com-ambedkar-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Ambedkar (Mains VA)",
                "body": (
                    "Collective responsibility is achieved only through the PM’s power "
                    "to nominate and dismiss ministers — without that instrument, "
                    "there is no collective responsibility."
                ),
            },
        ],
    },
    {
        "title": "Composition of the Council",
        "slug": "com-composition",
        "sort_order": 6,
        "summary": (
            "Three-tier CoM — Cabinet ministers, Ministers of State, Deputy ministers — "
            "plus Parliamentary Secretaries outside the Council."
        ),
        "body": (
            "## Ranks (C–M–D)\n\n"
            "Difference = rank, emoluments, political weight. PM sits at the top.\n\n"
            "1. **Cabinet ministers** — head key ministries (Home, Defence, Finance, MEA…); "
            "members of Cabinet; attend meetings; policy over the whole Central government.\n"
            "2. **Ministers of State** — independent charge **or** attached to a Cabinet minister "
            "(department / specific items). Under Cabinet minister’s overall charge when attached. "
            "Independent MoS act like Cabinet ministers for their portfolio but are **not** "
            "Cabinet members (attend only if specially invited).\n"
            "3. **Deputy ministers** — no independent charge; assist Cabinet / MoS in "
            "administrative, political, and parliamentary work; not in Cabinet.\n\n"
            "**Deputy PM** — appointed mostly for political reasons; descriptive rank.\n\n"
            "### Outside the CoM\n"
            "**Parliamentary Secretaries** — not CoM members; appointed by the **PM** "
            "(not President); no department; assist seniors in parliamentary duties.\n\n"
            "Three-tier classification is by **British convention**; Salaries Act 1952 "
            "defines ‘minister’ to include a deputy minister."
        ),
        "articles": [
            (
                "Articles 74 & 75",
                "CoM is constitutional; size/classification of ranks not spelled out in detail.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-composition-tree",
                "type": "tree",
                "title": "Council hierarchy",
                "root": {
                    "id": "pm",
                    "label": "Prime Minister",
                    "detail": "Supreme governing authority of the Council",
                    "children": [
                        {
                            "id": "cabinet",
                            "label": "Cabinet Ministers",
                            "slug": "com-composition",
                            "detail": "Cabinet members — key portfolios & policy",
                            "children": [
                                {
                                    "id": "mos",
                                    "label": "Ministers of State",
                                    "slug": "com-composition",
                                    "detail": "Independent charge or attached",
                                    "children": [
                                        {
                                            "id": "deputy",
                                            "label": "Deputy Ministers",
                                            "slug": "com-composition",
                                            "detail": "Assist only — no independent charge",
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "id": "ps",
                            "label": "Parliamentary Secretaries",
                            "slug": "com-composition",
                            "detail": "Outside CoM — PM-appointed; no department",
                        },
                    ],
                },
            },
            {
                "id": "com-composition-pillars",
                "type": "pillars",
                "title": "Three tiers + outsider",
                "items": [
                    {
                        "id": "cab",
                        "articles": "Cabinet",
                        "label": "Cabinet Ministers",
                        "slug": "com-composition",
                        "detail": "In Cabinet; weekly decision nucleus.",
                        "tone": "teal",
                    },
                    {
                        "id": "mos",
                        "articles": "MoS",
                        "label": "Ministers of State",
                        "slug": "com-composition",
                        "detail": "Independent or attached; invite-only to Cabinet.",
                        "tone": "olive",
                    },
                    {
                        "id": "dep",
                        "articles": "Deputy",
                        "label": "Deputy Ministers",
                        "slug": "com-composition",
                        "detail": "Assist seniors; never independent charge.",
                        "tone": "gold",
                    },
                    {
                        "id": "ps",
                        "articles": "Outside",
                        "label": "Parl. Secretaries",
                        "slug": "com-composition",
                        "detail": "Not CoM; help with House work only.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "com-composition-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic",
                "body": (
                    "**C–M–D** inside the Council; **PS outside**. "
                    "Cabinet ≠ all ministers — only cabinet-rank ministers sit in Cabinet."
                ),
            },
        ],
    },
    {
        "title": "Council of Ministers vs Cabinet",
        "slug": "com-vs-cabinet",
        "sort_order": 7,
        "summary": (
            "CoM is the wider constitutional body; Cabinet is the smaller decision-making "
            "nucleus that directs and speaks for the Council in practice."
        ),
        "body": (
            "## Do not use the words interchangeably\n\n"
            "They differ in composition, meeting habit, and real power "
            "(Laxmikanth Table 21.1 — compressed below).\n\n"
            "- **CoM** — Arts **74–75**; all three ranks; rarely meets as a body; "
            "powers in **theory**; implements Cabinet decisions; size ≤ **15%** of LS (91st); "
            "collectively responsible to Lok Sabha.\n"
            "- **Cabinet** — cabinet-rank only; meets often (~weekly); exercises CoM powers "
            "**in practice**; directs policy binding on all ministers; defined in **Art. 352** "
            "(44th) as PM + other cabinet-rank ministers under Art. 75 — role still largely "
            "**conventional**; **enforces** collective responsibility of the CoM.\n"
        ),
        "articles": [
            (
                "Articles 74 & 75",
                "Council of Ministers — constitutional body dealt with in detail.",
            ),
            (
                "Article 352",
                "Defines ‘Cabinet’ (inserted by 44th Amendment) — PM and other cabinet-rank ministers.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-vs-cabinet-compare",
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
                            "Arts 74–75; size ≤ 15% of Lok Sabha (91st)",
                            "Collectively responsible to Lok Sabha",
                        ],
                    },
                    {
                        "id": "cabinet",
                        "heading": "Cabinet",
                        "points": [
                            "Smaller — cabinet-rank only",
                            "Meets frequently; collective decisions",
                            "Powers in practice; directs & binds all ministers",
                            "Named in Art. 352 (44th); functions by convention",
                            "Enforces CoM’s collective responsibility",
                        ],
                    },
                ],
            },
            {
                "id": "com-vs-cabinet-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Art. 352 definition trap",
                "body": (
                    "Cabinet entered the constitutional text via the **44th Amendment** "
                    "in Art. **352** (Emergency) — a definition, not a full description of powers. "
                    "Original Constitution text did not use ‘Cabinet’ this way."
                ),
            },
        ],
    },
    {
        "title": "Role of Cabinet",
        "slug": "com-cabinet-role",
        "sort_order": 8,
        "summary": (
            "Highest decision-making and policy body of the Central government — "
            "plus classic political-science descriptions useful for Mains."
        ),
        "body": (
            "## Nine roles (scan)\n\n"
            "1. Highest decision-making authority in the politico-administrative system.\n"
            "2. Chief policy-formulating body of the Central government.\n"
            "3. Supreme executive authority of the Central government.\n"
            "4. Chief coordinator of Central administration.\n"
            "5. Advisory body to the President — advice **binding**.\n"
            "6. Chief crisis manager (emergencies).\n"
            "7. Major legislative and financial matters.\n"
            "8. Control over higher appointments (constitutional authorities, senior secretariat).\n"
            "9. Foreign policy and foreign affairs.\n\n"
            "### Quote bank (memory, not essay dump)\n"
            "- Ramsay Muir — steering wheel / ‘dictatorship of the Cabinet’.\n"
            "- Lowell — keystone of the political arch.\n"
            "- Marriott — pivot of political machinery.\n"
            "- Gladstone — solar orb.\n"
            "- Barker — magnet of policy.\n"
            "- **Bagehot** — hyphen that joins / buckle that binds executive and legislature.\n"
            "- Jennings — core of the constitutional system.\n"
            "- L.S. Amery — central directing instrument.\n"
        ),
        "articles": [
            (
                "Article 74",
                "Cabinet (as core of CoM) advises the President — advice binding.",
            ),
            (
                "Article 352",
                "Constitutional definition of Cabinet (44th Amendment).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "com-role-pillars",
                "type": "pillars",
                "title": "Nine cabinet roles",
                "items": [
                    {
                        "id": "decide",
                        "articles": "1",
                        "label": "Highest decision body",
                        "slug": "com-cabinet-role",
                        "detail": "Top formal decision-making authority.",
                        "tone": "teal",
                    },
                    {
                        "id": "policy",
                        "articles": "2",
                        "label": "Chief policy body",
                        "slug": "com-cabinet-role",
                        "detail": "Formulates Central government policy.",
                        "tone": "olive",
                    },
                    {
                        "id": "exec",
                        "articles": "3–4",
                        "label": "Executive & coordinator",
                        "slug": "com-cabinet-role",
                        "detail": "Supreme executive + chief admin coordinator.",
                        "tone": "gold",
                    },
                    {
                        "id": "advise",
                        "articles": "5",
                        "label": "Advise President",
                        "slug": "com-cabinet-role",
                        "detail": "Binding advice under Art. 74 path.",
                        "tone": "orange",
                    },
                    {
                        "id": "crisis",
                        "articles": "6",
                        "label": "Crisis manager",
                        "slug": "com-cabinet-role",
                        "detail": "Handles emergency situations.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "legfin",
                        "articles": "7",
                        "label": "Legislative & financial",
                        "slug": "com-cabinet-role",
                        "detail": "Major Bills, budget, and money matters.",
                        "tone": "maroon",
                    },
                    {
                        "id": "appoint",
                        "articles": "8",
                        "label": "Higher appointments",
                        "slug": "com-cabinet-role",
                        "detail": "Constitutional posts & senior secretariat.",
                        "tone": "teal",
                    },
                    {
                        "id": "foreign",
                        "articles": "9",
                        "label": "Foreign affairs",
                        "slug": "com-cabinet-role",
                        "detail": "Foreign policy and external relations.",
                        "tone": "olive",
                    },
                    {
                        "id": "quotes",
                        "articles": "VA",
                        "label": "Quote bank",
                        "slug": "com-cabinet-role",
                        "detail": "Bagehot hyphen · Muir dictatorship · Jennings core.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "com-role-palace",
                "type": "memory_palace",
                "title": "Cabinet room memory palace",
                "setting": "Cabinet meeting room",
                "loci": [
                    {
                        "id": "l1",
                        "place": "Steering wheel on the table",
                        "association": "Ramsay Muir",
                        "detail": "Cabinet = steering wheel of the ship of state.",
                    },
                    {
                        "id": "l2",
                        "place": "Hyphen carved on the door",
                        "association": "Bagehot",
                        "detail": "Hyphen / buckle joining executive and legislature.",
                    },
                    {
                        "id": "l3",
                        "place": "Keystone above the arch",
                        "association": "Lowell",
                        "detail": "Keystone of the political arch.",
                    },
                    {
                        "id": "l4",
                        "place": "Dictator’s chair (labelled ‘majority’)",
                        "association": "Cabinet dictatorship",
                        "detail": "Muir — absolute majority turns Cabinet into a publicity-qualified dictatorship.",
                    },
                ],
            },
            {
                "id": "com-role-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Mains VA pick-2",
                "body": (
                    "Prefer **Bagehot (hyphen)** for fusion of powers and "
                    "**Muir (cabinet dictatorship)** for majority-government critique — "
                    "both travel well to the Indian context."
                ),
            },
        ],
    },
    {
        "title": "Kitchen / Inner Cabinet",
        "slug": "com-kitchen-cabinet",
        "sort_order": 9,
        "summary": (
            "Informal inner circle around the PM — often the real power centre; "
            "may include outsiders; merits of speed vs demerits of bypassing Cabinet."
        ),
        "body": (
            "## Circle within a circle\n\n"
            "Formal Cabinet is the highest decision body **on paper**. "
            "In practice a still smaller **Inner / Kitchen Cabinet** — PM + a few trusted "
            "colleagues (sometimes friends/family) — often cooks decisions first.\n\n"
            "Every Indian PM has had an inner circle; Indira Gandhi’s was especially powerful "
            "and popularised the ‘kitchen cabinet’ label.\n\n"
            "### Merits\n"
            "- Smaller → more efficient decisions.\n"
            "- Meets more often; faster business.\n"
            "- Helps PM keep secrecy on sensitive political issues.\n\n"
            "### Demerits\n"
            "- Reduces Cabinet’s authority as the formal apex.\n"
            "- Lets **outsiders** influence government without legal office.\n"
            "- Formal Cabinet may only rubber-stamp (‘cooked then tabled’).\n\n"
            "Not unique to India — also known in USA and Britain."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "com-kitchen-compare",
                "type": "comparison",
                "title": "Kitchen cabinet — merits vs demerits",
                "columns": [
                    {
                        "id": "merits",
                        "heading": "Merits",
                        "points": [
                            "Small unit → efficient decisions",
                            "Meets often; expedites business",
                            "Secrecy on sensitive political issues",
                        ],
                    },
                    {
                        "id": "demerits",
                        "heading": "Demerits",
                        "points": [
                            "Undermines Cabinet as apex body",
                            "Outsiders influence without office",
                            "Formal approval becomes theatre",
                        ],
                    },
                ],
            },
            {
                "id": "com-kitchen-callout",
                "type": "callout",
                "tone": "tip",
                "title": "One-liner",
                "body": (
                    "**Circle within a circle — cooked then tabled.** "
                    "Extra-constitutional inner cabinet; powerful, informal, exam-favourite."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "com-constitutional-provisions"),
    (HUB_SLUG, "parent", "com-advice-and-cases"),
    (HUB_SLUG, "parent", "com-appointment-oath"),
    (HUB_SLUG, "parent", "com-collective-responsibility"),
    (HUB_SLUG, "parent", "com-individual-no-legal"),
    (HUB_SLUG, "parent", "com-composition"),
    (HUB_SLUG, "parent", "com-vs-cabinet"),
    (HUB_SLUG, "parent", "com-cabinet-role"),
    (HUB_SLUG, "parent", "com-kitchen-cabinet"),
    ("com-constitutional-provisions", "related", "com-advice-and-cases"),
    ("com-advice-and-cases", "related", "com-appointment-oath"),
    ("com-collective-responsibility", "related", "com-individual-no-legal"),
    ("com-composition", "related", "com-vs-cabinet"),
    ("com-vs-cabinet", "related", "com-cabinet-role"),
    ("com-cabinet-role", "related", "com-kitchen-cabinet"),
    ("com-collective-responsibility", "related", "com-vs-cabinet"),
    (HUB_SLUG, "related", "parliamentary-system"),
    ("com-advice-and-cases", "related", "ps-features"),
    ("com-collective-responsibility", "related", "ps-features"),
]

AMENDMENTS = [
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Among other changes, provided that the President shall act in accordance "
            "with the advice of the Council of Ministers."
        ),
        "effect": "With the 44th Amendment, ministerial advice to the President is binding.",
        "concept_slugs": [HUB_SLUG, "com-advice-and-cases", "com-constitutional-provisions"],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": (
            "Added the reconsideration proviso to Art. 74 and inserted a definition of "
            "Cabinet in Art. 352."
        ),
        "effect": (
            "President may require reconsideration once, then must follow advice; "
            "Cabinet defined for Emergency provisions."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "com-advice-and-cases",
            "com-vs-cabinet",
            "com-cabinet-role",
        ],
    },
    {
        "number": 91,
        "year": 2003,
        "title": "Ninety-first Amendment",
        "summary": (
            "Capped the size of the Council of Ministers and barred defection-disqualified "
            "members from ministership."
        ),
        "effect": (
            "Art. 75: ministers including PM ≤ 15% of Lok Sabha; "
            "defection → cannot be appointed minister."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "com-constitutional-provisions",
            "com-composition",
            "com-vs-cabinet",
        ],
    },
]

LANDMARK_CASES = [
    {
        "title": "U.N.R. Rao v. Indira Gandhi",
        "slug": "unr-rao",
        "parties": "U.N.R. Rao v. Indira Gandhi",
        "year": 1971,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Even after dissolution of the Lok Sabha, the Council of Ministers continues; "
            "Art. 74 is mandatory."
        ),
        "holding": (
            "The President cannot exercise executive power without the aid and advice of "
            "the Council of Ministers; any such exercise would violate Article 74."
        ),
        "concept_slugs": [HUB_SLUG, "com-advice-and-cases"],
    },
    {
        "title": "Shamsher Singh v. State of Punjab",
        "slug": "shamsher-singh",
        "parties": "Shamsher Singh v. State of Punjab",
        "year": 1974,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Wherever the Constitution requires the satisfaction of the President, "
            "it means the satisfaction of the Council of Ministers."
        ),
        "holding": (
            "Presidential satisfaction is not personal satisfaction but that of the CoM "
            "with whose aid and advice the President exercises powers and functions."
        ),
        "concept_slugs": [HUB_SLUG, "com-advice-and-cases"],
    },
]

SAMPLE_PYQS = [
    (
        2013,
        (
            "Consider the following statements: "
            "The Council of Ministers is collectively responsible to the Lok Sabha. "
            "Which of the following is correct regarding this principle?"
        ),
        (
            "Collective responsibility under Art. 75 means the whole CoM (including Rajya Sabha "
            "ministers) must resign if Lok Sabha passes no-confidence; Cabinet solidarity applies."
        ),
        ["com-collective-responsibility", HUB_SLUG],
    ),
    (
        2015,
        (
            "Which of the following is/are true? "
            "Cabinet is a smaller body than the Council of Ministers; "
            "Cabinet was originally not mentioned in the Constitution in the same way as CoM."
        ),
        (
            "Both themes are correct — Cabinet is cabinet-rank only; defined in Art. 352 via 44th; "
            "CoM is the wider Arts 74–75 body."
        ),
        ["com-vs-cabinet", HUB_SLUG],
    ),
    (
        2017,
        (
            "With reference to the Council of Ministers, the total number of ministers "
            "including the Prime Minister shall not exceed:"
        ),
        "15% of the total strength of the Lok Sabha (91st Constitutional Amendment Act, 2003).",
        ["com-constitutional-provisions", HUB_SLUG],
    ),
    (
        2019,
        (
            "A person who is not a member of Parliament can be appointed a minister, "
            "but must become a member within:"
        ),
        "Six consecutive months — else ceases to be a minister (Art. 75).",
        ["com-appointment-oath", HUB_SLUG],
    ),
    (
        2021,
        (
            "The advice tendered by Ministers to the President shall not be inquired into "
            "by any court. This provision emphasises:"
        ),
        (
            "Confidential President–minister relationship under Art. 74(2); "
            "paired with binding advice after 42nd/44th."
        ),
        ["com-advice-and-cases", HUB_SLUG],
    ),
]


class Command(BaseCommand):
    help = "Seed Central Council of Ministers chapter (Laxmikanth Ch.21)."

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
                "title": "Central Council of Ministers",
                "sort_order": 4,
                "book_ref": "Laxmikanth 8th Ed, Ch. 21",
                "summary": (
                    "Visual revision of Ch.21 — Arts 74–75/77–78/88, advice & cases, "
                    "collective/individual responsibility, CoM vs Cabinet, kitchen cabinet."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Central Council of Ministers",
                "summary": (
                    "Real executive headed by the PM — aid and advice, responsibility to "
                    "Lok Sabha, ranks, and Cabinet as the decision nucleus."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **team that steers while the President seals** mental model, "
                    "then **Provisions** → **Advice & cases** → **Collective responsibility**. "
                    "Finish with **CoM vs Cabinet**, **Cabinet role**, and **Kitchen cabinet**. "
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
            ref="Laxmikanth Ch. 21",
            excerpt=(
                "Central Council of Ministers — Arts 74–75, 77–78, 88; "
                "responsibility, composition, CoM vs Cabinet, kitchen cabinet."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 74 & 75",
            excerpt="Aid and advice; appointment, size, collective responsibility to Lok Sabha.",
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 77, 78 & 88",
            excerpt="Business of GoI; PM’s duties to President; ministers’ rights in the Houses.",
            sort_order=2,
        )

        com_slugs = set(by_slug.keys())
        related_outside = {"parliamentary-system", "ps-features"}
        ConceptEdge.objects.filter(
            source__slug__in=com_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=com_slugs | related_outside).delete()

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
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Central Council of Ministers chapter seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(LANDMARK_CASES)} cases, "
                f"{len(AMENDMENTS)} amendments linked, {len(SAMPLE_PYQS)} PYQs."
            )
        )
