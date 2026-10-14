"""Seed Laxmikanth Ch.34 High Court (visual revision — Part IV State Government)."""

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

HUB_SLUG = "high-court"
CHAPTER_SLUG = "high-court"

ENTRY_PILLARS = [
    {
        "id": "origin",
        "articles": "Arts 214, 230–231",
        "label": "Origin & structure",
        "slug": "hc-origin-structure",
        "detail": "25 HCs; common HC; Delhi alone among UTs has its own.",
        "tone": "teal",
    },
    {
        "id": "appoint",
        "articles": "Arts 216–217",
        "label": "Appointment",
        "slug": "hc-appointment",
        "detail": "Collegium; NJAC struck down; strength fixed by President.",
        "tone": "olive",
    },
    {
        "id": "quals",
        "articles": "Arts 217, 219, 221",
        "label": "Qualifications & oath",
        "slug": "hc-qualifications",
        "detail": "No min age; no jurist route; oath before Governor.",
        "tone": "gold",
    },
    {
        "id": "tenure",
        "articles": "Arts 217–218",
        "label": "Tenure & removal",
        "slug": "hc-tenure-removal",
        "detail": "Retire at 62; impeachment same as SC; none impeached.",
        "tone": "orange",
    },
    {
        "id": "transfer",
        "articles": "Art. 222",
        "label": "Transfer",
        "slug": "hc-transfer",
        "detail": "Public interest only; transfer collegium of 4 + both CJs.",
        "tone": "terracotta",
    },
    {
        "id": "acting",
        "articles": "Arts 223–224A",
        "label": "Acting & additional",
        "slug": "hc-acting-additional",
        "detail": "Acting CJ; additional ≤2 yrs; retired judges at sittings.",
        "tone": "maroon",
    },
    {
        "id": "indep",
        "articles": "9 safeguards",
        "label": "Independence",
        "slug": "hc-independence",
        "detail": "Tenure, purse, practice ban; pension on CFI.",
        "tone": "teal",
    },
    {
        "id": "jmap",
        "articles": "7 heads",
        "label": "Jurisdiction map",
        "slug": "hc-jurisdiction-map",
        "detail": "Original → writ → appellate → supervisory → JR.",
        "tone": "olive",
    },
    {
        "id": "writ",
        "articles": "Art. 226",
        "label": "Writ powers",
        "slug": "hc-writ-226",
        "detail": "Wider than Art. 32; Chandra Kumar = basic structure.",
        "tone": "gold",
    },
    {
        "id": "appeal",
        "articles": "Art. 227",
        "label": "Appellate & supervisory",
        "slug": "hc-appellate-supervisory",
        "detail": "Death needs HC confirmation; suo motu superintendence.",
        "tone": "orange",
    },
    {
        "id": "control",
        "articles": "Arts 13, 215, 228",
        "label": "Control, record & JR",
        "slug": "hc-control-record-review",
        "detail": "Subordinate control; contempt; 42nd→43rd JR restore.",
        "tone": "terracotta",
    },
    {
        "id": "tables",
        "articles": "Tables 34.1–34.2",
        "label": "Articles & HC map",
        "slug": "hc-tables",
        "detail": "Article spine + condensed jurisdiction / rename traps.",
        "tone": "maroon",
    },
    {
        "id": "exam",
        "articles": "PYQ kit",
        "label": "Exam kit",
        "slug": "hc-exam-kit",
        "detail": "Prelims traps, PYQ themes, mains one-liners.",
        "tone": "teal",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "hc-roof-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "State apex roof",
        "topic_label": "High Court",
        "subject_label": "Arts 214–231 · Part VI",
        "relation_label": "Protects you from",
        "protects_from": [
            "Confusing Art. 226 with Art. 32 (226 is wider)",
            "Mixing HC retirement age (62) with SC (65)",
            "Forgetting common HC / collegium after NJAC",
            "Treating HC judicial review as optional or weaker on FRs",
        ],
        "insight": (
            "In India’s single integrated judiciary, the High Court is the apex of the state "
            "judicial system — below the Supreme Court, above subordinate courts."
        ),
    },
    {
        "id": "hc-entry-pillars",
        "type": "pillars",
        "title": "Thirteen revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "hc-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Path: Appointment → Independence → 226 vs 32 → Jurisdiction map → Exam kit. "
            "Trap trio: age 62 (not 65); Art. 226 wider than 32; pension on Consolidated Fund of India."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Origin & Constitutional Place",
        "slug": "hc-origin-structure",
        "sort_order": 1,
        "summary": (
            "1862 origins; Art. 214 HC for each state; 7th Amendment common HC; "
            "25 High Courts and UT jurisdiction rules."
        ),
        "body": (
            "## Place in the system\n\n"
            "Single integrated judiciary: **Supreme Court → High Court → subordinate courts**. "
            "The HC is the top court of a state (or group of states/UTs).\n\n"
            "### Origin\n"
            "- **1862:** Calcutta, Bombay, Madras (Indian High Courts Act, 1861).\n"
            "- **1866:** Allahabad; later each province got an HC.\n"
            "- After **1950**, provincial HCs became state HCs.\n\n"
            "### Constitution\n"
            "- **Art. 214:** High Court for each state.\n"
            "- **7th Amendment (1956):** Parliament may establish a **common HC** for two or more "
            "states, or states + UT (**Art. 231**).\n"
            "- **Art. 230:** Parliament may extend or exclude HC jurisdiction over any UT.\n"
            "- Territorial jurisdiction ≈ territory of the state(s)/UT concerned.\n\n"
            "### Numbers that stick\n"
            "- **25** High Courts.\n"
            "- Only **three** have jurisdiction over more than one state.\n"
            "- Among eight UTs, **Delhi alone** has a separate HC (since **1966**).\n"
            "- J&K and Ladakh share a common HC (renamed 2021)."
        ),
        "articles": [
            ("Art. 214", "High Courts for states."),
            ("Art. 230", "Extension of jurisdiction of High Courts to union territories."),
            ("Art. 231", "Establishment of a common High Court for two or more states."),
        ],
        "visual_blocks": [
            {
                "id": "hc-origin-tree",
                "type": "tree",
                "title": "Integrated judiciary",
                "root": {
                    "id": "sc",
                    "label": "Supreme Court",
                    "detail": "Apex — Union",
                    "children": [
                        {
                            "id": "hc",
                            "label": "High Court",
                            "slug": "high-court",
                            "detail": "State apex · Arts 214–231",
                            "children": [
                                {
                                    "id": "sub",
                                    "label": "Subordinate courts",
                                    "detail": "District & below",
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "id": "hc-origin-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "25 HCs · Delhi = only UT with its own HC · common HC = 7th Amd / Art. 231 · "
                    "Parliament can extend or exclude UT jurisdiction (Art. 230)."
                ),
            },
        ],
    },
    {
        "title": "Composition & Appointment",
        "slug": "hc-appointment",
        "sort_order": 2,
        "summary": (
            "Strength fixed by President; CJ and judges via collegium; "
            "NJAC (99th) struck down in Fourth Judges Case (2015)."
        ),
        "body": (
            "## Composition (Art. 216)\n\n"
            "Every HC has a **Chief Justice** and such other judges as the **President** may appoint. "
            "The Constitution does **not** fix strength — President decides by workload.\n\n"
            "### Appointment (Art. 217)\n"
            "- **CJ:** President after consultation with **CJI** and the **Governor** of the state "
            "(all Governors if common HC).\n"
            "- **Other judges:** also consult the **CJ of that High Court**.\n\n"
            "### Collegium evolution\n"
            "1. **Second Judges Case (1993):** appointment must conform to the opinion of the CJI.\n"
            "2. **Third Judges Case (1998):** for HC judges, CJI consults a collegium of **two** "
            "seniormost SC judges — sole CJI opinion ≠ ‘consultation’.\n"
            "3. **99th Amendment + NJAC Act (2014):** tried to replace collegium.\n"
            "4. **Fourth Judges Case (2015):** both struck down as unconstitutional — "
            "collegium restored; NJAC held to impair judicial independence."
        ),
        "articles": [
            ("Art. 216", "Constitution of High Courts — strength left to the President."),
            ("Art. 217", "Appointment and conditions of office of a Judge of a High Court."),
        ],
        "visual_blocks": [
            {
                "id": "hc-appoint-flow",
                "type": "flowchart",
                "title": "Who is consulted for appointment?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Appointing whom?",
                        "detail": "President always appoints; consultation set differs.",
                        "options": [
                            {"label": "Chief Justice of HC", "next": "cj"},
                            {"label": "Other HC judge", "next": "oj"},
                        ],
                    },
                    {
                        "id": "cj",
                        "label": "CJI + Governor(s)",
                        "detail": "Common HC → Governors of all concerned states.",
                    },
                    {
                        "id": "oj",
                        "label": "CJI + Governor(s) + HC CJ",
                        "detail": "Plus collegium practice: CJI + 2 seniormost SC judges (1998).",
                    },
                ],
            },
            {
                "id": "hc-appoint-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "NJAC is unconstitutional and void (2015) — collegium is operative again. "
                    "Do not treat the 99th Amendment as the living appointment system."
                ),
            },
        ],
    },
    {
        "title": "Qualifications, Oath & Salaries",
        "slug": "hc-qualifications",
        "sort_order": 3,
        "summary": (
            "Citizen + 10 years judicial office or HC advocacy; no minimum age; "
            "no distinguished-jurist route; oath before Governor."
        ),
        "body": (
            "## Qualifications\n\n"
            "1. Citizen of India.\n"
            "2. (a) Held a **judicial office** in India for **10 years**; or "
            "(b) been an **advocate** of a High Court (or HCs in succession) for **10 years**.\n\n"
            "**No minimum age** for appointment. "
            "**Unlike the Supreme Court**, there is **no** ‘distinguished jurist’ route for HC judges.\n\n"
            "### Oath (Art. 219)\n"
            "Before the **Governor** (or person appointed by the Governor). Swears to:\n"
            "1. bear true faith and allegiance to the Constitution;\n"
            "2. uphold sovereignty and integrity of India;\n"
            "3. perform duties without fear or favour, affection or ill-will;\n"
            "4. uphold the Constitution and the laws.\n\n"
            "### Salaries (Art. 221)\n"
            "Determined by Parliament; cannot be varied to disadvantage after appointment "
            "except during a **financial emergency**. "
            "From **2018:** CJ ₹2.50 lakh / month; judge ₹2.25 lakh. "
            "Retired CJ/judges get **50%** of last drawn salary as pension."
        ),
        "articles": [
            ("Art. 217", "Qualifications and conditions for HC judges."),
            ("Art. 219", "Oath or affirmation by judges of High Courts."),
            ("Art. 221", "Salaries etc. of judges."),
        ],
        "visual_blocks": [
            {
                "id": "hc-qual-vs-sc",
                "type": "comparison",
                "title": "HC vs SC — eligibility snapshot",
                "columns": [
                    {
                        "id": "hc",
                        "heading": "High Court",
                        "points": [
                            "Citizen + 10 yrs judicial office or HC advocacy",
                            "No minimum age prescribed",
                            "No distinguished-jurist clause",
                            "Oath before Governor",
                            "Retire at 62",
                        ],
                    },
                    {
                        "id": "sc",
                        "heading": "Supreme Court",
                        "points": [
                            "Citizen + 5 yrs HC judge / 10 yrs HC advocate / jurist",
                            "No minimum age prescribed",
                            "Distinguished jurist route exists",
                            "Oath before President",
                            "Retire at 65",
                        ],
                    },
                ],
            },
            {
                "id": "hc-qual-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "HC: no jurist appointment · oath = Governor · retire 62 · "
                    "salary cut only in financial emergency."
                ),
            },
        ],
    },
    {
        "title": "Tenure & Removal",
        "slug": "hc-tenure-removal",
        "sort_order": 4,
        "summary": (
            "Office till age 62; resign to President; removed like SC judges "
            "via special-majority Parliamentary address — none impeached so far."
        ),
        "body": (
            "## Tenure\n\n"
            "Constitution does not fix a fixed term; it provides:\n"
            "1. Holds office until age **62** (**15th Amendment** raised 60 → 62). "
            "Age dispute decided by President after consulting CJI — **decision final**.\n"
            "2. May resign by writing to the **President**.\n"
            "3. May be removed by the President on Parliament’s recommendation.\n"
            "4. Vacates office on appointment as SC judge or transfer to another HC.\n\n"
            "### Removal\n"
            "Same manner and grounds as an SC judge: Presidential order after each House "
            "presents an address in the **same session**, passed by **special majority** "
            "(majority of total membership + ≥2/3 of members present and voting). "
            "Grounds: **proved misbehaviour** or **incapacity**.\n\n"
            "### Judges Enquiry Act, 1968\n"
            "1. Removal motion: **100** LS members or **50** RS members → Speaker/Chairman.\n"
            "2. May admit or refuse.\n"
            "3. If admitted → three-member committee (SC CJ/judge + HC CJ + distinguished jurist).\n"
            "4. If guilty → House considers motion → special majority both Houses → address → "
            "President removes.\n\n"
            "**No High Court judge has been impeached so far.**"
        ),
        "articles": [
            ("Art. 217", "Tenure, resignation, removal, and vacation of office."),
            ("Art. 218", "Application of certain SC provisions relating to removal to High Courts."),
        ],
        "visual_blocks": [
            {
                "id": "hc-impeach-flow",
                "type": "flowchart",
                "title": "Impeachment path (same as SC)",
                "root": "motion",
                "steps": [
                    {
                        "id": "motion",
                        "label": "Removal motion",
                        "detail": "100 LS or 50 RS members → Speaker/Chairman.",
                        "options": [
                            {"label": "Admitted", "next": "committee"},
                            {"label": "Refused", "next": "end"},
                        ],
                    },
                    {
                        "id": "committee",
                        "label": "3-member enquiry",
                        "detail": "SC CJ/judge + HC CJ + distinguished jurist.",
                        "options": [
                            {"label": "Guilty", "next": "houses"},
                            {"label": "Not guilty", "next": "end"},
                        ],
                    },
                    {
                        "id": "houses",
                        "label": "Special majority both Houses",
                        "detail": "Same session address → President’s removal order.",
                    },
                    {
                        "id": "end",
                        "label": "Process ends",
                        "detail": "Judge continues in office.",
                    },
                ],
            },
            {
                "id": "hc-tenure-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "HC judges do not hold office during the pleasure of the President. "
                    "Age 62 (HC) ≠ 65 (SC). Procedure for removal = SC procedure."
                ),
            },
        ],
    },
    {
        "title": "Transfer of Judges",
        "slug": "hc-transfer",
        "sort_order": 5,
        "summary": (
            "Art. 222 transfer by President after consulting CJI; only in public interest; "
            "Third Judges Case requires collegium of four plus both HC CJs."
        ),
        "body": (
            "## Art. 222\n\n"
            "President may transfer a judge from one High Court to another after consulting "
            "the **Chief Justice of India**. On transfer, compensatory allowance as Parliament determines.\n\n"
            "### Case law\n"
            "- **1977:** transfer only as an **exceptional** measure, in **public interest**, "
            "not as punishment.\n"
            "- **1994:** judicial review available to check arbitrariness; "
            "**only the transferred judge** can challenge.\n"
            "- **Third Judges Case (1998):** for transfer, CJI must consult a collegium of "
            "**four** seniormost SC judges **plus** the CJs of the **two** High Courts "
            "(from and to). Sole CJI opinion ≠ consultation."
        ),
        "articles": [
            ("Art. 222", "Transfer of a judge from one High Court to another."),
        ],
        "visual_blocks": [
            {
                "id": "hc-transfer-vs-appoint",
                "type": "comparison",
                "title": "Collegium size — appointment vs transfer",
                "columns": [
                    {
                        "id": "appt",
                        "heading": "HC appointment (1998)",
                        "points": [
                            "CJI + 2 seniormost SC judges",
                            "Plus constitutional consultees (Governor, HC CJ)",
                            "Must conform to CJI/collegium opinion",
                        ],
                    },
                    {
                        "id": "xfer",
                        "heading": "HC transfer (1998)",
                        "points": [
                            "CJI + 4 seniormost SC judges",
                            "Plus CJs of both High Courts",
                            "Public interest only — not punishment",
                        ],
                    },
                ],
            },
            {
                "id": "hc-transfer-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "Appointment collegium for HC = **2** SC judges beside CJI; "
                    "transfer = **4** + both HC CJs. Only the transferred judge can challenge."
                ),
            },
        ],
    },
    {
        "title": "Acting, Additional & Retired Judges",
        "slug": "hc-acting-additional",
        "sort_order": 6,
        "summary": (
            "Acting CJ (Art. 223); additional/acting judges (Art. 224, ≤2 years); "
            "retired judges at sittings (Art. 224A)."
        ),
        "body": (
            "## Acting Chief Justice (Art. 223)\n\n"
            "President may appoint an HC judge as acting CJ when the office is vacant, "
            "or the CJ is temporarily absent, or unable to perform duties.\n\n"
            "### Additional & acting judges (Art. 224)\n"
            "- **Additional:** temporary period **not exceeding two years** for temporary "
            "increase in business or arrears.\n"
            "- **Acting:** when a judge (other than CJ) is unable to perform duties or is "
            "acting as CJ; holds office until the permanent judge resumes.\n"
            "- Neither can hold office after age **62**.\n\n"
            "### Retired judges (Art. 224A)\n"
            "HC CJ may request a retired judge of that or any other HC to sit temporarily, "
            "with prior consent of the **President** and the person. "
            "Entitled to allowances; enjoys jurisdiction and powers of a judge, "
            "but is **not otherwise deemed** a judge of that court."
        ),
        "articles": [
            ("Art. 223", "Appointment of acting Chief Justice."),
            ("Art. 224", "Appointment of additional and acting judges."),
            ("Art. 224A", "Appointment of retired judges at sittings of High Courts."),
        ],
        "visual_blocks": [
            {
                "id": "hc-acting-pillars",
                "type": "pillars",
                "title": "Three temporary routes",
                "items": [
                    {
                        "id": "acj",
                        "articles": "Art. 223",
                        "label": "Acting CJ",
                        "slug": "hc-acting-additional",
                        "detail": "Vacancy / absence / inability of CJ.",
                        "tone": "teal",
                    },
                    {
                        "id": "add",
                        "articles": "Art. 224",
                        "label": "Additional / acting",
                        "slug": "hc-acting-additional",
                        "detail": "Additional ≤2 years; both stop at age 62.",
                        "tone": "olive",
                    },
                    {
                        "id": "ret",
                        "articles": "Art. 224A",
                        "label": "Retired at sittings",
                        "slug": "hc-acting-additional",
                        "detail": "Powers of a judge; not ‘deemed’ a judge.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "hc-acting-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Additional judge max tenure = **two years**. "
                    "Art. 224A judge has powers of a judge but is not otherwise deemed one."
                ),
            },
        ],
    },
    {
        "title": "Independence of High Court",
        "slug": "hc-independence",
        "sort_order": 7,
        "summary": (
            "Nine constitutional safeguards — appointment, tenure, service conditions, "
            "charged expenses, practice ban, contempt, staff, and uncurtailable jurisdiction."
        ),
        "body": (
            "## Why independence?\n\n"
            "HC must work free of executive and legislative pressure — justice without fear or favour.\n\n"
            "### Nine safeguards\n"
            "1. **Mode of appointment** — President with judiciary (CJI / HC CJ), not pure executive pick.\n"
            "2. **Security of tenure** — not during pleasure; removal only as Constitution provides.\n"
            "3. **Fixed service conditions** — no disadvantageous change except financial emergency.\n"
            "4. **Expenses charged** — salaries, staff, admin on **state Consolidated Fund** "
            "(non-votable, discussable). **Pension of HC judge is charged on Consolidated Fund of India.**\n"
            "5. **Conduct not discussable** in Parliament/state legislature except during impeachment.\n"
            "6. **Ban on practice after retirement** (Art. 220) — permanent judges barred from "
            "pleading in any court/authority in India **except SC and other High Courts**.\n"
            "7. **Contempt power** — to protect authority and dignity.\n"
            "8. **Freedom to appoint staff** (Art. 229) — CJ appoints officers/servants and conditions.\n"
            "9. **Jurisdiction cannot be curtailed** — where specified in the Constitution, "
            "neither Parliament nor state legislature may cut it."
        ),
        "articles": [
            ("Art. 220", "Restriction on practice after being a permanent judge."),
            ("Art. 221", "Salaries etc. — charged; protected from disadvantageous variation."),
            ("Art. 229", "Officers and servants and the expenses of High Courts."),
        ],
        "visual_blocks": [
            {
                "id": "hc-indep-pillars",
                "type": "pillars",
                "title": "Nine independence pillars",
                "items": [
                    {
                        "id": "i1",
                        "articles": "Art. 217",
                        "label": "Appointment mode",
                        "slug": "hc-independence",
                        "detail": "Judiciary consulted — curtails executive discretion.",
                        "tone": "teal",
                    },
                    {
                        "id": "i2",
                        "articles": "Art. 217–218",
                        "label": "Security of tenure",
                        "slug": "hc-independence",
                        "detail": "Not during pleasure; hard removal path.",
                        "tone": "olive",
                    },
                    {
                        "id": "i3",
                        "articles": "Art. 221",
                        "label": "Fixed conditions",
                        "slug": "hc-independence",
                        "detail": "No adverse change except financial emergency.",
                        "tone": "gold",
                    },
                    {
                        "id": "i4",
                        "articles": "Purse",
                        "label": "Charged expenses",
                        "slug": "hc-independence",
                        "detail": "State CF for salaries; pension on CFI.",
                        "tone": "orange",
                    },
                    {
                        "id": "i5",
                        "articles": "Debate ban",
                        "label": "Conduct protected",
                        "slug": "hc-independence",
                        "detail": "No discussion except impeachment motion.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "i6",
                        "articles": "Art. 220",
                        "label": "Practice ban",
                        "slug": "hc-independence",
                        "detail": "Except SC and other High Courts.",
                        "tone": "maroon",
                    },
                    {
                        "id": "i7",
                        "articles": "Art. 215",
                        "label": "Contempt power",
                        "slug": "hc-independence",
                        "detail": "Protects authority and dignity.",
                        "tone": "teal",
                    },
                    {
                        "id": "i8",
                        "articles": "Art. 229",
                        "label": "Own staff",
                        "slug": "hc-independence",
                        "detail": "CJ appoints without executive interference.",
                        "tone": "olive",
                    },
                    {
                        "id": "i9",
                        "articles": "Constitution",
                        "label": "Jurisdiction intact",
                        "slug": "hc-independence",
                        "detail": "Cannot be curtailed by legislature.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "hc-indep-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Salaries/admin → Consolidated Fund of the **state**. "
                    "Pension of an HC judge → Consolidated Fund of **India**. Easy mix-up."
                ),
            },
        ],
    },
    {
        "title": "Jurisdiction at a Glance",
        "slug": "hc-jurisdiction-map",
        "sort_order": 8,
        "summary": (
            "Seven heads: original, writ, appellate, supervisory, control over subordinate courts, "
            "court of record, and judicial review."
        ),
        "body": (
            "## Role\n\n"
            "Highest court of appeal in the state; protector of FRs; interprets the Constitution; "
            "supervisory and consultative roles.\n\n"
            "Constitution largely continues pre-Constitution jurisdiction, **plus** revenue matters "
            "and added writ / superintendence / consultative powers.\n\n"
            "### Seven heads\n"
            "1. Original jurisdiction\n"
            "2. Writ jurisdiction\n"
            "3. Appellate jurisdiction\n"
            "4. Supervisory jurisdiction\n"
            "5. Control over subordinate courts\n"
            "6. Court of record\n"
            "7. Power of judicial review\n\n"
            "Governed by: Constitution, Letters Patent, Union/state Acts, IPC, CrPC 1973, CPC 1908.\n\n"
            "### Original jurisdiction (snapshot)\n"
            "- Election disputes of MPs / state legislators\n"
            "- Revenue matters / acts in revenue collection\n"
            "- Enforcement of Fundamental Rights\n"
            "- Cases transferred under Art. 228 (constitutional interpretation)\n"
            "- **Civil** original (higher value): Calcutta, Bombay, Madras, **Delhi**\n"
            "- **Criminal** original of Calcutta/Bombay/Madras abolished by CrPC **1973**"
        ),
        "articles": [
            ("Art. 225", "Jurisdiction of existing High Courts."),
            ("Art. 226", "Power of High Courts to issue certain writs."),
            ("Art. 227", "Power of superintendence over all courts by the High Court."),
            ("Art. 228", "Transfer of certain cases to High Court."),
        ],
        "visual_blocks": [
            {
                "id": "hc-jmap-pillars",
                "type": "pillars",
                "title": "Seven jurisdiction heads",
                "items": [
                    {
                        "id": "orig",
                        "articles": "Original",
                        "label": "Original",
                        "slug": "hc-jurisdiction-map",
                        "detail": "Elections, revenue, FRs, Art. 228, 4 civil HCs.",
                        "tone": "teal",
                    },
                    {
                        "id": "writ",
                        "articles": "Art. 226",
                        "label": "Writ",
                        "slug": "hc-writ-226",
                        "detail": "Wider than Art. 32 — ‘any other purpose’.",
                        "tone": "olive",
                    },
                    {
                        "id": "app",
                        "articles": "Civil/criminal",
                        "label": "Appellate",
                        "slug": "hc-appellate-supervisory",
                        "detail": "Primary role — wider than original.",
                        "tone": "gold",
                    },
                    {
                        "id": "sup",
                        "articles": "Art. 227",
                        "label": "Supervisory",
                        "slug": "hc-appellate-supervisory",
                        "detail": "All courts/tribunals except military.",
                        "tone": "orange",
                    },
                    {
                        "id": "ctrl",
                        "articles": "Admin",
                        "label": "Control",
                        "slug": "hc-control-record-review",
                        "detail": "District judges, leave, Art. 228, binding law.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "rec",
                        "articles": "Art. 215",
                        "label": "Court of record",
                        "slug": "hc-control-record-review",
                        "detail": "Precedents + contempt + self-review.",
                        "tone": "maroon",
                    },
                    {
                        "id": "jr",
                        "articles": "Arts 13, 226",
                        "label": "Judicial review",
                        "slug": "hc-control-record-review",
                        "detail": "Central + state laws; three challenge grounds.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "hc-jmap-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "Appellate > original in breadth. Four HCs with original civil: "
                    "Calcutta, Bombay, Madras, Delhi. Criminal original gone (1973)."
                ),
            },
        ],
    },
    {
        "title": "Writ Jurisdiction (Art. 226)",
        "slug": "hc-writ-226",
        "sort_order": 9,
        "summary": (
            "Five writs for FRs and ‘any other purpose’; wider than Art. 32; "
            "L. Chandra Kumar — 226/227 are basic structure."
        ),
        "body": (
            "## Art. 226\n\n"
            "HC may issue directions, orders, or writs — including **habeas corpus, mandamus, "
            "certiorari, prohibition, quo warranto** — for enforcement of FRs **and for any other "
            "purpose** (ordinary legal rights).\n\n"
            "### Reach\n"
            "To any person, authority, or government **within** territorial jurisdiction, "
            "or **outside** if the **cause of action** arises within (added by **15th Amendment**).\n\n"
            "### Concurrent but wider than Art. 32\n"
            "For FR violation, party may move HC or SC. "
            "SC under Art. 32 issues writs **only for FRs**; HC under 226 also for ordinary legal rights "
            "→ **HC writ jurisdiction is wider**.\n\n"
            "### L. Chandra Kumar (1997)\n"
            "Writ jurisdiction of HC (226) and SC (32), and HC superintendence (227), "
            "are part of the **basic structure** — cannot be ousted even by amendment. "
            "Tribunals are subject to HC writ jurisdiction; no leapfrog to SC without first going to HC."
        ),
        "articles": [
            ("Art. 226", "Power of High Courts to issue certain writs."),
            ("Art. 227", "Power of superintendence — linked in Chandra Kumar."),
            ("Art. 32", "SC writs — only for Fundamental Rights (compare)."),
        ],
        "visual_blocks": [
            {
                "id": "hc-writ-compare",
                "type": "comparison",
                "title": "Art. 32 vs Art. 226",
                "columns": [
                    {
                        "id": "a32",
                        "heading": "Supreme Court — Art. 32",
                        "points": [
                            "Writs only for Fundamental Rights",
                            "Itself a Fundamental Right",
                            "All-India territorial reach",
                            "Part of basic structure (Chandra Kumar)",
                        ],
                    },
                    {
                        "id": "a226",
                        "heading": "High Court — Art. 226",
                        "points": [
                            "FRs + ‘any other purpose’ (legal rights)",
                            "Constitutional remedy, not itself an FR",
                            "Territory + cause-of-action reach",
                            "Wider than 32; also basic structure",
                        ],
                    },
                ],
            },
            {
                "id": "hc-writ-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic — five writs",
                "body": (
                    "**H**abeas **M**andamus **C**ertiorari **P**rohibition **Q**uo warranto — "
                    "‘**HMC PQ**’. 226 = FR + ordinary rights → wider than 32."
                ),
            },
            {
                "id": "hc-writ-case",
                "type": "callout",
                "tone": "note",
                "title": "Landmark — Chandra Kumar (1997)",
                "body": (
                    "Arts 226 & 227 (and Art. 32) = basic structure. "
                    "Tribunal decisions → HC first; cannot oust HC writ power by amendment."
                ),
            },
        ],
    },
    {
        "title": "Appellate & Supervisory Jurisdiction",
        "slug": "hc-appellate-supervisory",
        "sort_order": 10,
        "summary": (
            "Primarily a court of appeal (civil and criminal); Art. 227 superintendence "
            "over all courts and tribunals except military."
        ),
        "body": (
            "## Appellate (primary role)\n\n"
            "Appeals from subordinate courts in the territory; wider than original jurisdiction.\n\n"
            "### Civil\n"
            "1. **First appeals** from district/additional/subordinate courts — law **and** fact "
            "(if amount exceeds limit).\n"
            "2. **Second appeals** — questions of **law only**.\n"
            "3. **Intra-court appeals** — single judge → division bench (where provided).\n"
            "4. Appeals from administrative/other tribunals → division bench; "
            "after Chandra Kumar, tribunals under HC writ — no direct SC route.\n\n"
            "### Criminal\n"
            "1. From sessions/additional sessions if imprisonment **> 7 years**.\n"
            "2. **Death sentence** by sessions/additional sessions needs **HC confirmation** "
            "before execution — even without an appeal.\n"
            "3. Certain CrPC appeals from assistant sessions / magistrates → HC.\n\n"
            "### Supervisory (Art. 227)\n"
            "Superintendence over all courts and tribunals in the territory "
            "(**except military**): call for returns; rules/forms; accounts; settle fees. "
            "Broad: covers courts whether or not under appellate jurisdiction; "
            "administrative **and** judicial; revisional; can be **suo motu**. "
            "Use sparingly — excess jurisdiction, natural justice, error of law, "
            "disregard of superior courts, perverse findings, manifest injustice."
        ),
        "articles": [
            ("Art. 227", "Power of superintendence over all courts by the High Court."),
        ],
        "visual_blocks": [
            {
                "id": "hc-appeal-flow",
                "type": "flowchart",
                "title": "Appeal path — quick filter",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What kind of matter?",
                        "options": [
                            {"label": "Civil first appeal", "next": "civil1"},
                            {"label": "Civil second appeal", "next": "civil2"},
                            {"label": "Criminal / death", "next": "crim"},
                            {"label": "Tribunal / writ", "next": "trib"},
                        ],
                    },
                    {
                        "id": "civil1",
                        "label": "Law + fact → HC",
                        "detail": "From district/additional/subordinate if amount limit crossed.",
                    },
                    {
                        "id": "civil2",
                        "label": "Law only → HC",
                        "detail": "Second appeal — not questions of fact.",
                    },
                    {
                        "id": "crim",
                        "label": ">7 years / death",
                        "detail": "Death needs HC confirmation even without appeal.",
                    },
                    {
                        "id": "trib",
                        "label": "HC first",
                        "detail": "Division bench / Art. 226 — no SC leapfrog (Chandra Kumar).",
                    },
                ],
            },
            {
                "id": "hc-appeal-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Death confirmation",
                "body": (
                    "Capital punishment by sessions court is **not** executable until the High Court "
                    "confirms it — appeal or no appeal."
                ),
            },
        ],
    },
    {
        "title": "Control, Court of Record & Judicial Review",
        "slug": "hc-control-record-review",
        "sort_order": 11,
        "summary": (
            "Administrative control over subordinate judiciary; Art. 215 court of record; "
            "JR under Arts 13 and 226 — 42nd curtailed, 43rd restored."
        ),
        "body": (
            "## Control over subordinate courts\n\n"
            "Beyond appeal and Art. 227:\n"
            "1. Consulted by Governor on appointment, posting, promotion of **district judges** "
            "and appointments to state judicial service (other than district judges).\n"
            "2. Posting, promotion, leave, transfers, discipline of judicial service "
            "(posts below district judge).\n"
            "3. **Art. 228:** withdraw case involving substantial question of law needing "
            "constitutional interpretation — decide or return with judgment.\n"
            "4. HC law binding on subordinate courts in its territory "
            "(like SC law binds all courts in India).\n\n"
            "### Court of record (Art. 215)\n"
            "1. Judgments/proceedings recorded — evidentiary value; precedents.\n"
            "2. Power to punish for **contempt** of itself; under Contempt of Courts Act 1971, "
            "also of subordinate courts (except where the contempt is an IPC offence).\n"
            "3. Can **review and correct** its own judgment even without an express "
            "Constitutional review power (SC has explicit Art. 137).\n\n"
            "### Judicial review\n"
            "Examine constitutionality of Union **and** state laws/executive orders; "
            "if ultra vires → void. Phrase ‘judicial review’ unused in text; "
            "Arts **13** and **226** confer it. Challenge grounds:\n"
            "1. Infringes Fundamental Rights (Part III)\n"
            "2. Outside competence of the framing authority\n"
            "3. Repugnant to constitutional provisions\n\n"
            "**42nd Amendment (1976)** barred HC from reviewing validity of **central** laws; "
            "**43rd Amendment (1977)** restored the original position."
        ),
        "articles": [
            ("Art. 13", "Laws inconsistent with Fundamental Rights — JR anchor."),
            ("Art. 215", "High Courts to be courts of record."),
            ("Art. 226", "Writs — vehicle for judicial review."),
            ("Art. 228", "Transfer of certain cases to High Court."),
        ],
        "visual_blocks": [
            {
                "id": "hc-jr-grounds",
                "type": "comparison",
                "title": "Three grounds to challenge a law/order",
                "columns": [
                    {
                        "id": "fr",
                        "heading": "FR breach",
                        "points": [
                            "Violates Part III",
                            "Classic Art. 13 + 226 path",
                        ],
                    },
                    {
                        "id": "comp",
                        "heading": "Competence",
                        "points": [
                            "Outside legislative/executive competence",
                            "Federal list / authority mismatch",
                        ],
                    },
                    {
                        "id": "rep",
                        "heading": "Repugnancy",
                        "points": [
                            "Conflicts with constitutional provisions",
                            "Ultra vires the Constitution",
                        ],
                    },
                ],
            },
            {
                "id": "hc-jr-timeline",
                "type": "callout",
                "tone": "note",
                "title": "42nd → 43rd",
                "body": (
                    "1976 (42nd): HC barred from testing central laws. "
                    "1977 (43rd): position restored — HC again reviews Union and state measures."
                ),
            },
        ],
    },
    {
        "title": "Articles & High Court Map",
        "slug": "hc-tables",
        "sort_order": 12,
        "summary": (
            "Arts 214–231 spine plus condensed jurisdiction card — common HCs, "
            "Delhi, newest courts, and rename traps."
        ),
        "body": (
            "## Article spine (Table 34.2)\n\n"
            "| Art. | Subject |\n"
            "|------|--------|\n"
            "| 214 | High Courts for states |\n"
            "| 215 | Courts of record |\n"
            "| 216 | Constitution of HCs |\n"
            "| 217 | Appointment & conditions |\n"
            "| 218 | SC removal provisions applied |\n"
            "| 219 | Oath |\n"
            "| 220 | Restriction on practice after permanent judgeship |\n"
            "| 221 | Salaries |\n"
            "| 222 | Transfer |\n"
            "| 223 | Acting CJ |\n"
            "| 224 | Additional & acting judges |\n"
            "| 224A | Retired judges at sittings |\n"
            "| 225 | Jurisdiction of existing HCs |\n"
            "| 226 | Writs |\n"
            "| 226A | Central-law validity under 226 — **repealed** |\n"
            "| 227 | Superintendence |\n"
            "| 228 | Transfer of cases to HC |\n"
            "| 228A | State-law validity special provisions — **repealed** |\n"
            "| 229 | Officers, servants, expenses |\n"
            "| 230 | Jurisdiction over UTs |\n"
            "| 231 | Common High Court |\n"
            "| 232 | Interpretation — **repealed** |\n\n"
            "### Condensed map (PYQ hotspots)\n"
            "- **1862 trio:** Bombay, Calcutta, Madras (city names changed; **HC names unchanged**).\n"
            "- **Delhi HC:** 1966 — only UT with its own HC.\n"
            "- **Common / multi-territory:** Bombay (MH+Goa+DN+DD); Gauhati (AS+NL+MZ+AR); "
            "Punjab & Haryana (+ Chandigarh); Kerala (+ Lakshadweep); Calcutta (+ A&N).\n"
            "- **2013:** Manipur, Meghalaya, Tripura (24 → then 25 with AP).\n"
            "- **2019:** separate Andhra Pradesh HC (Amaravati); Telangana keeps Hyderabad HC.\n"
            "- **Rename traps:** Orissa HC (state = Odisha); Mysore → Karnataka HC (1973); "
            "Assam → Gauhati (1971); J&K → J&K & Ladakh (2021)."
        ),
        "articles": [
            ("Arts 214–231", "Organisation, independence, jurisdiction, and related provisions."),
        ],
        "visual_blocks": [
            {
                "id": "hc-article-explorer",
                "type": "article_explorer",
                "title": "High Court — article spine",
                "article_ref": "Arts 214–231",
                "stages": [
                    {
                        "id": "org",
                        "label": "Organisation",
                        "detail": "214–224A — existence, judges, oath, transfer, temporary judges.",
                    },
                    {
                        "id": "powers",
                        "label": "Powers",
                        "detail": "225–228 — jurisdiction, writs, superintendence, case transfer.",
                    },
                    {
                        "id": "admin",
                        "label": "Admin & common HC",
                        "detail": "229–231 — staff/expenses, UTs, common High Court.",
                    },
                ],
            },
            {
                "id": "hc-map-compare",
                "type": "comparison",
                "title": "PYQ jurisdiction card",
                "columns": [
                    {
                        "id": "common",
                        "heading": "Multi-state / UT HCs",
                        "points": [
                            "Bombay — MH, Goa, DN & DD",
                            "Gauhati — AS, NL, MZ, AR",
                            "Punjab & Haryana — + Chandigarh",
                            "Kerala — + Lakshadweep",
                            "Calcutta — + Andaman & Nicobar",
                        ],
                    },
                    {
                        "id": "special",
                        "heading": "Special / recent",
                        "points": [
                            "Delhi 1966 — only UT HC",
                            "J&K & Ladakh common (2021 name)",
                            "NE trio 2013; AP separate 2019",
                            "Bombay/Calcutta/Madras/Orissa names kept",
                        ],
                    },
                ],
            },
            {
                "id": "hc-tables-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Last-minute scan",
                "body": (
                    "214–231 spine · 25 HCs · Delhi unique UT · 226 wider than 32 · "
                    "62 retire · pension on CFI · 226A/228A/232 repealed."
                ),
            },
        ],
    },
    {
        "title": "Prelims Traps, PYQ Themes & Mains VA",
        "slug": "hc-exam-kit",
        "sort_order": 13,
        "summary": (
            "High-yield prelims traps, recurring PYQ themes, and mains value-addition "
            "one-liners for the High Court chapter."
        ),
        "body": (
            "## Prelims traps\n\n"
            "- Retirement: HC **62** ≠ SC **65**.\n"
            "- No **distinguished jurist** appointment to HC.\n"
            "- Art. **226 wider** than Art. 32 (any other purpose).\n"
            "- Pension charged on **CFI**; salaries/admin on **state CF**.\n"
            "- Additional judge ≤ **2 years**; stops at 62.\n"
            "- Transfer collegium = **4** SC judges + both HC CJs (≠ appointment’s 2).\n"
            "- **25** High Courts; Delhi alone among UTs has its own.\n"
            "- Art. **220** practice ban — exception = SC + other HCs.\n"
            "- Death sentence needs **HC confirmation** even without appeal.\n\n"
            "## PYQ themes\n\n"
            "226 vs 32 · collegium / NJAC · independence & charged funds · common HC (Art. 231) · "
            "death confirmation · Chandra Kumar / basic structure of 226–227 · "
            "qualifications (no jurist) · transfer public interest.\n\n"
            "## Mains VA\n\n"
            "- Integrated judiciary with HC as the citizen’s nearest constitutional court.\n"
            "- Art. 226 as wider remedial jurisdiction than Art. 32 — access + ordinary rights.\n"
            "- Independence design: appointment + tenure + purse + practice ban + uncurtailable jurisdiction.\n"
            "- Transfer only in public interest — balances national judiciary with individual fairness."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "hc-pyq-heat",
                "type": "pyq_heatmap",
                "title": "PYQ focus map",
                "items": [
                    {"concept_slug": "hc-writ-226", "label": "Writ 226"},
                    {"concept_slug": "hc-appointment", "label": "Appointment"},
                    {"concept_slug": "hc-independence", "label": "Independence"},
                    {"concept_slug": "hc-origin-structure", "label": "Common HC"},
                    {"concept_slug": "hc-transfer", "label": "Transfer"},
                    {"concept_slug": "hc-control-record-review", "label": "JR / record"},
                ],
            },
            {
                "id": "hc-exam-traps",
                "type": "callout",
                "tone": "trap",
                "title": "Trap pack",
                "body": (
                    "62 ≠ 65 · 226 wider than 32 · pension = CFI · no HC jurist · "
                    "transfer collegium 4 · NJAC void · death needs confirmation."
                ),
            },
            {
                "id": "hc-exam-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "Art. 226 makes the High Court the most accessible constitutional court — "
                    "FR enforcement plus ordinary legal rights, under an independence design "
                    "that Chandra Kumar placed in the basic structure."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "hc-origin-structure"),
    (HUB_SLUG, "parent", "hc-appointment"),
    (HUB_SLUG, "parent", "hc-qualifications"),
    (HUB_SLUG, "parent", "hc-tenure-removal"),
    (HUB_SLUG, "parent", "hc-transfer"),
    (HUB_SLUG, "parent", "hc-acting-additional"),
    (HUB_SLUG, "parent", "hc-independence"),
    (HUB_SLUG, "parent", "hc-jurisdiction-map"),
    (HUB_SLUG, "parent", "hc-writ-226"),
    (HUB_SLUG, "parent", "hc-appellate-supervisory"),
    (HUB_SLUG, "parent", "hc-control-record-review"),
    (HUB_SLUG, "parent", "hc-tables"),
    (HUB_SLUG, "parent", "hc-exam-kit"),
    ("hc-appointment", "related", "hc-transfer"),
    ("hc-appointment", "related", "hc-qualifications"),
    ("hc-tenure-removal", "related", "hc-independence"),
    ("hc-writ-226", "related", "hc-appellate-supervisory"),
    ("hc-writ-226", "related", "hc-control-record-review"),
    ("hc-jurisdiction-map", "related", "hc-writ-226"),
    ("hc-independence", "related", "hc-control-record-review"),
    ("hc-exam-kit", "related", "hc-writ-226"),
    ("hc-exam-kit", "related", "hc-appointment"),
    (HUB_SLUG, "related", "supreme-court"),
    (HUB_SLUG, "related", "judicial-review"),
    ("hc-writ-226", "related", "basic-structure"),
    ("hc-control-record-review", "related", "judicial-review"),
]

SAMPLE_PYQS = [
    (
        2017,
        "Which of the following are the discretionary powers given to the High Court under Article 226?",
        "Art. 226 empowers HCs to issue writs for enforcement of Fundamental Rights and for any "
        "other purpose — wider than Art. 32, which is limited to FRs.",
        ["hc-writ-226", HUB_SLUG],
    ),
    (
        2015,
        "Consider the following statements about High Court judges: retirement age and qualifications.",
        "HC judges retire at 62; there is no distinguished-jurist route for HC appointment "
        "(unlike the Supreme Court).",
        ["hc-qualifications", "hc-tenure-removal", HUB_SLUG],
    ),
    (
        2014,
        "The power of the High Court to issue writs under Article 226 can be exercised:",
        "Within territorial jurisdiction and also outside if the cause of action arises within "
        "(15th Amendment). Concurrent with Art. 32 for FRs but wider overall.",
        ["hc-writ-226", HUB_SLUG],
    ),
    (
        2019,
        "With reference to the Constitution of India, consider common High Courts and UT jurisdiction.",
        "Parliament may establish a common HC for two or more states (Art. 231) and may extend "
        "or exclude HC jurisdiction over any UT (Art. 230). Delhi alone has a separate UT High Court.",
        ["hc-origin-structure", "hc-tables", HUB_SLUG],
    ),
    (
        2016,
        "Which of the following is/are true of the independence of High Courts?",
        "Salaries and administrative expenses are charged on the Consolidated Fund of the state; "
        "pension of an HC judge is charged on the Consolidated Fund of India.",
        ["hc-independence", HUB_SLUG],
    ),
    (
        2018,
        "In the context of judicial appointments and the NJAC, which statement is correct?",
        "The 99th Constitutional Amendment and NJAC Act were struck down in 2015 "
        "(Fourth Judges Case); the collegium system was restored.",
        ["hc-appointment", HUB_SLUG],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Supreme Court Advocates-on-Record Association v. Union of India",
        "slug": "second-judges-case",
        "parties": "Supreme Court Advocates-on-Record Association v. Union of India",
        "year": 1993,
        "court": CaseLaw.Court.SC,
        "summary": "Second Judges Case — primacy of the CJI in judicial appointments.",
        "holding": (
            "No appointment of a High Court judge can be made unless it is in conformity "
            "with the opinion of the Chief Justice of India."
        ),
        "concept_slugs": ["hc-appointment", HUB_SLUG],
    },
    {
        "title": "In re Presidential Reference (Third Judges Case)",
        "slug": "third-judges-case",
        "parties": "In re Presidential Reference",
        "year": 1998,
        "court": CaseLaw.Court.SC,
        "summary": "Clarified collegium consultation for SC/HC appointments and transfers.",
        "holding": (
            "For HC appointments, CJI consults two seniormost SC judges. For HC transfers, "
            "CJI consults a collegium of four seniormost SC judges plus the CJs of both High Courts. "
            "Sole opinion of the CJI does not constitute consultation."
        ),
        "concept_slugs": ["hc-appointment", "hc-transfer", HUB_SLUG],
    },
    {
        "title": "Supreme Court Advocates-on-Record Association v. Union of India (NJAC)",
        "slug": "fourth-judges-case",
        "parties": "Supreme Court Advocates-on-Record Association v. Union of India",
        "year": 2015,
        "court": CaseLaw.Court.SC,
        "summary": "Fourth Judges Case — NJAC and 99th Amendment struck down.",
        "holding": (
            "The 99th Constitutional Amendment and the NJAC Act are unconstitutional and void; "
            "the collegium system stands restored. NJAC was held to impair judicial independence."
        ),
        "concept_slugs": ["hc-appointment", HUB_SLUG],
    },
    {
        "title": "L. Chandra Kumar v. Union of India",
        "slug": "l-chandra-kumar",
        "parties": "L. Chandra Kumar v. Union of India",
        "year": 1997,
        "court": CaseLaw.Court.SC,
        "summary": "Writ jurisdiction of HC/SC and HC superintendence are basic structure.",
        "holding": (
            "Powers of High Courts under Articles 226 and 227 (and SC under Art. 32) form part "
            "of the basic structure and cannot be ousted. Tribunals remain subject to HC writ "
            "jurisdiction; aggrieved persons must approach the High Court before the Supreme Court."
        ),
        "concept_slugs": [
            "hc-writ-226",
            "hc-appellate-supervisory",
            "hc-control-record-review",
            HUB_SLUG,
        ],
    },
]

AMENDMENTS = [
    {
        "number": 7,
        "year": 1956,
        "title": "Seventh Amendment",
        "summary": (
            "Authorised Parliament to establish a common High Court for two or more states "
            "or for states and a union territory."
        ),
        "effect": "Enabled Arts 230–231 framework for common HCs and UT jurisdiction.",
        "concept_slugs": ["hc-origin-structure", "hc-tables", HUB_SLUG],
    },
    {
        "number": 15,
        "year": 1963,
        "title": "Fifteenth Amendment",
        "summary": (
            "Raised High Court judges’ retirement age from 60 to 62 and expanded Art. 226 "
            "reach where cause of action arises within the territory."
        ),
        "effect": "Age 62; extra-territorial cause-of-action writ jurisdiction.",
        "concept_slugs": ["hc-tenure-removal", "hc-writ-226", HUB_SLUG],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Among other changes, debarred High Courts from considering the constitutional "
            "validity of central laws."
        ),
        "effect": "Temporarily curtailed HC judicial review of Union legislation.",
        "concept_slugs": ["hc-control-record-review", HUB_SLUG],
    },
    {
        "number": 43,
        "year": 1977,
        "title": "Forty-third Amendment",
        "summary": "Restored the High Court’s power to review the constitutional validity of central laws.",
        "effect": "Reversed the 42nd Amendment curtailment of HC judicial review.",
        "concept_slugs": ["hc-control-record-review", HUB_SLUG],
    },
    {
        "number": 99,
        "year": 2014,
        "title": "Ninety-ninth Amendment",
        "summary": (
            "Sought to replace the collegium with the National Judicial Appointments Commission "
            "for SC and HC appointments."
        ),
        "effect": "Struck down with the NJAC Act in 2015; collegium restored.",
        "concept_slugs": ["hc-appointment", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed High Court chapter (Laxmikanth Ch.34) under Part IV State Government."

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
                "title": "High Court",
                "sort_order": 5,
                "book_ref": "Laxmikanth 8th Ed, Ch. 34",
                "summary": (
                    "Visual revision of Ch.34 — organisation, appointment, independence, "
                    "jurisdiction, writs, and Arts 214–231."
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
                "title": "High Court",
                "summary": (
                    "Apex court of a state or group of states — Arts 214–231; "
                    "writs under Art. 226 are wider than Art. 32 in scope."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **state apex roof** mental model, then "
                    "**Appointment** → **Independence** → **226 vs 32** → "
                    "**Jurisdiction map** → **Exam kit**. "
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
            ref="Laxmikanth Ch. 34",
            excerpt=(
                "High Court — organisation, appointment, independence, "
                "jurisdiction, writs, and related articles."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 214–231",
            excerpt="Part VI framework for High Courts — organisation to common HC.",
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Article 226",
            excerpt="Power of High Courts to issue certain writs.",
            sort_order=2,
        )

        hc_slugs = set(by_slug.keys())
        related_outside = {
            "supreme-court",
            "judicial-review",
            "basic-structure",
            "judiciary",
        }
        ConceptEdge.objects.filter(
            source__slug__in=hc_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=hc_slugs | related_outside).delete()

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

        # Preserve judiciary → high-court parent edge from seed_polity stub graph.
        judiciary = Concept.objects.filter(subject=subject, slug="judiciary").first()
        if judiciary:
            _, was_created = ConceptEdge.objects.get_or_create(
                source=judiciary,
                target=hub,
                relation_type="parent",
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
                f"High Court chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
