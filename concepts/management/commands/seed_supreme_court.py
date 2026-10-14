"""Seed Laxmikanth Ch.26 Supreme Court (visual revision chapter)."""

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

HUB_SLUG = "supreme-court"
CHAPTER_SLUG = "supreme-court"

ENTRY_PILLARS = [
    {
        "id": "footing",
        "articles": "124–147 · Part V",
        "label": "Footing & integrated judiciary",
        "slug": "sc-footing",
        "detail": "One hierarchy SC→HC→subordinate; Centre + state laws.",
        "tone": "teal",
    },
    {
        "id": "composition",
        "articles": "34 judges",
        "label": "Composition & strength",
        "slug": "sc-composition",
        "detail": "CJI + 33; Parliament raises strength by law.",
        "tone": "olive",
    },
    {
        "id": "appointment",
        "articles": "Collegium",
        "label": "Appointment & Collegium",
        "slug": "sc-appointment",
        "detail": "Judges cases 1–4; NJAC struck; seniormost CJI.",
        "tone": "gold",
    },
    {
        "id": "qual",
        "articles": "Art. 124",
        "label": "Qualifications, oath, salaries",
        "slug": "sc-qual-oath",
        "detail": "Citizen + 5/10 yrs or jurist; no min age; CFI charge.",
        "tone": "orange",
    },
    {
        "id": "tenure",
        "articles": "65 · removal",
        "label": "Tenure & removal",
        "slug": "sc-tenure-removal",
        "detail": "Until 65; special majority address; Judges Enquiry Act.",
        "tone": "terracotta",
    },
    {
        "id": "acting",
        "articles": "126–130",
        "label": "Acting, seat & procedure",
        "slug": "sc-acting-seat",
        "detail": "Acting/ad hoc/retired; Delhi seat; constitutional bench ≥5.",
        "tone": "maroon",
    },
    {
        "id": "independence",
        "articles": "9 safeguards",
        "label": "Independence",
        "slug": "sc-independence",
        "detail": "Appointment to jurisdiction — structural freedom from exec/legislature.",
        "tone": "teal",
    },
    {
        "id": "jmap",
        "articles": "9 powers",
        "label": "Jurisdiction overview",
        "slug": "sc-jurisdiction-map",
        "detail": "Original, writ, appellate, advisory, record, JR, review…",
        "tone": "olive",
    },
    {
        "id": "orig",
        "articles": "131 · 32",
        "label": "Original + Writ",
        "slug": "sc-original-writ",
        "detail": "Federal disputes; FR writs; Art. 32 vs 226.",
        "tone": "gold",
    },
    {
        "id": "appellate",
        "articles": "132–136",
        "label": "Appellate + SLP",
        "slug": "sc-appellate",
        "detail": "Constitutional, civil, criminal appeals; Art. 136 discretion.",
        "tone": "orange",
    },
    {
        "id": "advisory",
        "articles": "143 · 129",
        "label": "Advisory + Court of Record",
        "slug": "sc-advisory-record",
        "detail": "Non-binding opinions; contempt; 15 references so far.",
        "tone": "terracotta",
    },
    {
        "id": "review",
        "articles": "137 · doctrines",
        "label": "Review, JR & other powers",
        "slug": "sc-review-other",
        "detail": "Review/curative; JR snapshot; doctrines; Art. 141–142.",
        "tone": "maroon",
    },
    {
        "id": "usa",
        "articles": "Table 26.1",
        "label": "India vs USA",
        "slug": "sc-india-usa",
        "detail": "SLP, advisory, JR width, due process vs procedure…",
        "tone": "teal",
    },
    {
        "id": "exam",
        "articles": "Prelims · Mains",
        "label": "Articles + exam pack",
        "slug": "sc-exam-revision",
        "detail": "Articles glance, PYQ themes, traps, mains value-adds.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "sc-load-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Three hats of the apex court",
        "topic_label": "Supreme Court",
        "subject_label": "Part V · Arts 124–147 · Ch. 26",
        "relation_label": "Protects you from",
        "protects_from": [
            "Confusing India’s integrated judiciary with the US dual system",
            "Treating ‘consultation’ as optional after 1993",
            "Calling NJAC the current appointment law",
            "Mixing Art. 32 with Art. 226 scope",
            "Treating Art. 143 opinion as binding on the President",
        ],
        "insight": (
            "Federal court + guarantor of Fundamental Rights + final court of appeal "
            "— also guardian and ultimate interpreter of the Constitution."
        ),
    },
    {
        "id": "sc-entry-pillars",
        "type": "pillars",
        "title": "Fourteen revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "sc-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Scan Footing → Composition → Collegium → Independence → Jurisdiction nine-pack "
            "→ India–USA → Articles glance. Anchors: 34 judges; age 65; collegium (Fourth Judges); "
            "constitutional bench ≥5; Art. 143 non-binding; Parliament may extend, not curtail, "
            "jurisdiction."
        ),
    },
    {
        "id": "sc-hub-heatmap",
        "type": "pyq_heatmap",
        "title": "PYQ focus map",
        "items": [
            {"concept_slug": "sc-appointment", "label": "Collegium"},
            {"concept_slug": "sc-independence", "label": "Independence"},
            {"concept_slug": "sc-original-writ", "label": "Writ / Original"},
            {"concept_slug": "sc-appellate", "label": "SLP"},
            {"concept_slug": "sc-advisory-record", "label": "Advisory"},
            {"concept_slug": "sc-tenure-removal", "label": "Removal"},
            {"concept_slug": "sc-india-usa", "label": "India–USA"},
            {"concept_slug": "sc-exam-revision", "label": "Exam pack"},
        ],
    },
]

CLUSTERS = [
    {
        "title": "Constitutional footing & integrated judiciary",
        "slug": "sc-footing",
        "sort_order": 1,
        "summary": (
            "Part V Arts 124–147; inaugurated 28 Jan 1950; one hierarchy enforcing "
            "Centre and state laws — unlike the US dual court system."
        ),
        "body": (
            "## Where the Supreme Court sits\n\n"
            "Articles **124–147** in **Part V** deal with organisation, independence, "
            "jurisdiction, powers, and procedure. Parliament may also regulate them.\n\n"
            "### Birth of the Court\n"
            "- Inaugurated **28 January 1950**.\n"
            "- Succeeded the **Federal Court** (GoI Act 1935).\n"
            "- Replaced the British **Privy Council** as India’s highest court of appeal "
            "— so its jurisdiction is wider than the Federal Court’s.\n\n"
            "### Integrated judiciary\n"
            "India has a **single hierarchy**: Supreme Court → High Courts → subordinate "
            "courts (district and below). This system, taken from the GoI Act 1935, "
            "enforces **both Central and state laws**.\n\n"
            "### Memory aid\n"
            "**One hierarchy, both laws** — federal country, unified judiciary."
        ),
        "articles": [
            ("Articles 124–147", "Organisation, independence, jurisdiction, powers, procedure of the SC."),
            ("Part V", "The Union — includes the Supreme Court chapter of the Constitution."),
            ("GoI Act 1935", "Source of India’s single integrated court system."),
        ],
        "visual_blocks": [
            {
                "id": "sc-footing-tree",
                "type": "tree",
                "title": "Integrated judicial hierarchy",
                "root": {
                    "id": "sc",
                    "label": "Supreme Court",
                    "slug": "supreme-court",
                    "detail": "Apex · Arts 124–147",
                    "children": [
                        {
                            "id": "hc",
                            "label": "High Courts",
                            "detail": "State / group of states",
                            "children": [
                                {
                                    "id": "dist",
                                    "label": "District & subordinate courts",
                                    "detail": "Enforce Centre + state laws",
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "id": "sc-footing-compare",
                "type": "comparison",
                "title": "India vs USA — court systems",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Integrated / unified judiciary",
                            "One hierarchy for Centre + states",
                            "One system of fundamental law",
                            "Adopted from GoI Act 1935",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Dual (double) system of courts",
                            "Federal judiciary for federal laws",
                            "State judiciary for state laws",
                            "Separate federal and state tracks",
                        ],
                    },
                ],
            },
            {
                "id": "sc-footing-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "Federal like the USA, but **unified judiciary** like a unitary spirit "
                    "in court structure. Parliament can regulate/enlarge SC powers — "
                    "it cannot casually rewrite the constitutional design of the Court."
                ),
            },
        ],
    },
    {
        "title": "Composition & strength",
        "slug": "sc-composition",
        "sort_order": 2,
        "summary": (
            "34 judges today (1 CJI + 33); originally 8; Parliament increases strength "
            "by law under Art. 124(1)."
        ),
        "body": (
            "## Strength of the Court\n\n"
            "At present: **thirty-four judges** — one Chief Justice of India and "
            "**thirty-three** other judges.\n\n"
            "Originally Art. 124 fixed strength at **eight** (1 CJI + 7). Parliament "
            "has raised the number of other judges by statute.\n\n"
            "### Acts at a glance (incl. CJI)\n"
            "| Year / footing | Total (incl. CJI) |\n"
            "|---|---|\n"
            "| Art. 124 (original) | 8 |\n"
            "| 1956 Act | 11 |\n"
            "| 1960 Amendment | 14 |\n"
            "| 1977 Amendment | 18 |\n"
            "| 1986 Amendment | 26 |\n"
            "| 2008 Amendment | 31 |\n"
            "| **2019 Amendment** | **34** |\n"
        ),
        "articles": [
            ("Article 124(1)", "SC consists of CJI and, until Parliament by law prescribes a larger number, not more than seven other judges."),
            ("Supreme Court (Number of Judges) Act / Amendments", "Parliament’s statutes fixing maximum strength."),
        ],
        "visual_blocks": [
            {
                "id": "sc-comp-timeline",
                "type": "timeline",
                "title": "Strength timeline (including CJI)",
                "events": [
                    {"id": "e1950", "year": 1950, "label": "8 judges", "detail": "Art. 124 original — CJI + 7"},
                    {"id": "e1956", "year": 1956, "label": "11", "detail": "Number of Judges Act"},
                    {"id": "e1960", "year": 1960, "label": "14", "detail": "Amendment Act"},
                    {"id": "e1977", "year": 1977, "label": "18", "detail": "Amendment Act"},
                    {"id": "e1986", "year": 1986, "label": "26", "detail": "Amendment Act"},
                    {"id": "e2008", "year": 2008, "label": "31", "detail": "Amendment Act"},
                    {"id": "e2019", "year": 2019, "label": "34", "detail": "CJI + 33 — current"},
                ],
            },
            {
                "id": "sc-comp-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Strength is **not** frozen forever in the Constitution. "
                    "Art. 124(1) expressly lets Parliament prescribe a larger number. "
                    "Quote **34** (2019) for ‘at present’ questions."
                ),
            },
        ],
    },
    {
        "title": "Appointment & Collegium",
        "slug": "sc-appointment",
        "sort_order": 3,
        "summary": (
            "President appoints; consultation → concurrence via Judges cases; "
            "collegium of CJI + 4; 99th/NJAC struck in Fourth Judges (2015)."
        ),
        "body": (
            "## Who appoints?\n\n"
            "Judges of the Supreme Court are appointed by the **President**.\n"
            "- **CJI:** after consultation with such SC and HC judges as the President deems necessary.\n"
            "- **Other judges:** after consultation with the CJI and such other SC/HC judges as deemed necessary — "
            "**consultation with the CJI is obligatory**.\n\n"
            "### Consultation → Collegium (mnemonic)\n"
            "**1 → exchange · 2 → binding + 2 · 3 → plurality + 4 · 4 → NJAC out.**\n\n"
            "| Case | Year | Holding (revision line) |\n"
            "|---|---|---|\n"
            "| First Judges (S.P. Gupta) | 1981 | Consultation ≠ concurrence — exchange of views |\n"
            "| Second Judges (SCARA) | 1993 | Consultation = **concurrence**; CJI + 2 seniormost; seniormost → CJI |\n"
            "| Third Judges (In Re Ref.) | 1998 | Collegium of **CJI + 4**; if 2 oppose, do not recommend |\n"
            "| Fourth Judges (SCARA) | 2015 | **99th CAA + NJAC Act void**; collegium restored |\n\n"
            "### CJI appointment\n"
            "1950–1973: seniormost convention. Violated in **1973** (A.N. Ray) and **1977** (M.U. Beg). "
            "Second Judges (1993) restored: **only the seniormost** SC judge should be appointed CJI."
        ),
        "articles": [
            ("Article 124(2)", "Appointment of CJI and other judges by the President after consultation."),
            ("99th Amendment / NJAC Act 2014", "Struck down in Fourth Judges case (2015) — collegium revived."),
        ],
        "visual_blocks": [
            {
                "id": "sc-appt-flow",
                "type": "flowchart",
                "title": "From consultation to collegium",
                "root": "first",
                "steps": [
                    {
                        "id": "first",
                        "label": "First Judges 1981",
                        "detail": "Consultation = exchange of views, not concurrence.",
                        "options": [{"label": "Next", "next": "second"}],
                    },
                    {
                        "id": "second",
                        "label": "Second Judges 1993",
                        "detail": "Consultation = concurrence; CJI advice binding; consult 2 seniormost; seniormost → CJI.",
                        "options": [{"label": "Next", "next": "third"}],
                    },
                    {
                        "id": "third",
                        "label": "Third Judges 1998",
                        "detail": "Plurality: collegium of CJI + 4; adverse opinion of 2 blocks recommendation.",
                        "options": [{"label": "Next", "next": "njac"}],
                    },
                    {
                        "id": "njac",
                        "label": "99th CAA + NJAC Act 2014",
                        "detail": "Tried to replace collegium with NJAC.",
                        "options": [{"label": "Next", "next": "fourth"}],
                    },
                    {
                        "id": "fourth",
                        "label": "Fourth Judges 2015",
                        "detail": "NJAC unconstitutional — affects independence; collegium operative again.",
                    },
                ],
            },
            {
                "id": "sc-appt-cases",
                "type": "case_network",
                "title": "Judges cases spine",
                "hub_label": "Appointments",
                "cases": [
                    {
                        "id": "j1",
                        "label": "First Judges",
                        "year": 1981,
                        "detail": "Consultation ≠ concurrence",
                        "case_slug": "first-judges-case",
                    },
                    {
                        "id": "j2",
                        "label": "Second Judges",
                        "year": 1993,
                        "detail": "Concurrence + CJI+2",
                        "case_slug": "second-judges-case",
                    },
                    {
                        "id": "j3",
                        "label": "Third Judges",
                        "year": 1998,
                        "detail": "Collegium of 5",
                        "case_slug": "third-judges-case",
                    },
                    {
                        "id": "j4",
                        "label": "Fourth Judges",
                        "year": 2015,
                        "detail": "NJAC void",
                        "case_slug": "fourth-judges-case",
                    },
                ],
            },
            {
                "id": "sc-appt-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "NJAC is **not** current law. Arts 124A–C still appear in some texts, "
                    "but Fourth Judges made them void. Answer appointment questions with **collegium**."
                ),
            },
        ],
    },
    {
        "title": "Qualifications, oath & salaries",
        "slug": "sc-qual-oath",
        "sort_order": 4,
        "summary": (
            "Citizen + HC judge 5 yrs or advocate 10 yrs or distinguished jurist; "
            "no minimum age; oath before President; salaries by Parliament."
        ),
        "body": (
            "## Qualifications\n\n"
            "1. **Citizen of India**; and\n"
            "2. (a) Judge of a High Court (or HCs in succession) for **five years**; **or**\n"
            "   (b) Advocate of a High Court (or HCs in succession) for **ten years**; **or**\n"
            "   (c) A **distinguished jurist** in the opinion of the President.\n\n"
            "No **minimum age** is prescribed for appointment as an SC judge.\n\n"
            "### Oath\n"
            "Before the President (or person appointed by the President). The judge swears to:\n"
            "- bear true faith and allegiance to the Constitution;\n"
            "- uphold the sovereignty and integrity of India;\n"
            "- duly and faithfully perform the office;\n"
            "- uphold the Constitution and the laws.\n\n"
            "### Salaries & conditions\n"
            "Determined by Parliament; cannot be varied to their **disadvantage** after appointment "
            "except during a **financial emergency**. Salaries/allowances/pensions and SC "
            "administrative expenses are **charged on the Consolidated Fund of India**."
        ),
        "articles": [
            ("Article 124(3)", "Qualifications for appointment as a judge of the Supreme Court."),
            ("Article 124(6) / oath", "Oath or affirmation before entering office."),
            ("Article 125", "Salaries, etc., of judges."),
        ],
        "visual_blocks": [
            {
                "id": "sc-qual-pillars",
                "type": "pillars",
                "title": "Three qualification paths (+ citizenship)",
                "items": [
                    {
                        "id": "cit",
                        "articles": "Must",
                        "label": "Citizen of India",
                        "slug": "sc-qual-oath",
                        "detail": "Non-negotiable base requirement.",
                        "tone": "teal",
                    },
                    {
                        "id": "hc5",
                        "articles": "5 years",
                        "label": "HC judge path",
                        "slug": "sc-qual-oath",
                        "detail": "Judge of a High Court (or HCs in succession) for five years.",
                        "tone": "olive",
                    },
                    {
                        "id": "adv10",
                        "articles": "10 years",
                        "label": "Advocate path",
                        "slug": "sc-qual-oath",
                        "detail": "Advocate of a High Court (or HCs in succession) for ten years.",
                        "tone": "gold",
                    },
                    {
                        "id": "jurist",
                        "articles": "Rare",
                        "label": "Distinguished jurist",
                        "slug": "sc-qual-oath",
                        "detail": "In the opinion of the President — often forgotten in MCQs.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "sc-qual-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Prelims trap",
                "body": (
                    "Remember the **distinguished jurist** route. Also: Constitution fixes "
                    "**no minimum age** for SC appointment (contrast with retirement at 65)."
                ),
            },
        ],
    },
    {
        "title": "Tenure & removal",
        "slug": "sc-tenure-removal",
        "sort_order": 5,
        "summary": (
            "Holds office until 65; resign to President; removal only for proved "
            "misbehaviour or incapacity via special-majority Parliamentary address."
        ),
        "body": (
            "## Tenure (three provisions)\n\n"
            "The Constitution does **not** fix a fixed-year tenure. Instead:\n"
            "1. Holds office until age **65** (age dispute → authority/manner as Parliament provides).\n"
            "2. May **resign** by writing to the President.\n"
            "3. May be **removed** by the President on Parliament’s recommendation.\n\n"
            "### Removal grounds\n"
            "Only **proved misbehaviour** or **incapacity**.\n\n"
            "### Special majority\n"
            "Address of each House in the **same session**: majority of **total membership** "
            "+ not less than **two-thirds** of members **present and voting**.\n\n"
            "### Judges Enquiry Act, 1968 (procedure)\n"
            "1. Removal motion: **100** LS members or **50** RS members → Speaker/Chairman.\n"
            "2. Admit or refuse.\n"
            "3. If admitted → **3-member** inquiry committee: (a) CJI or SC judge, "
            "(b) HC Chief Justice, (c) distinguished jurist.\n"
            "4. If guilty → Houses pass motion by special majority → address → President’s order.\n\n"
            "**No SC judge has been removed so far.** Justice V. Ramaswami (1991–93): "
            "committee found guilt, but the motion failed in the Lok Sabha."
        ),
        "articles": [
            ("Article 124(2) proviso / (4)–(5)", "Age 65; resignation; removal by Presidential order after Parliamentary address."),
            ("Judges Enquiry Act, 1968", "Statutory procedure for investigation and removal motion."),
        ],
        "visual_blocks": [
            {
                "id": "sc-remove-flow",
                "type": "flowchart",
                "title": "Removal path (Judges Enquiry Act)",
                "root": "motion",
                "steps": [
                    {
                        "id": "motion",
                        "label": "Removal motion",
                        "detail": "Signed by 100 LS or 50 RS members → Speaker/Chairman.",
                        "options": [
                            {"label": "Admitted", "next": "committee"},
                            {"label": "Refused", "next": "end"},
                        ],
                    },
                    {
                        "id": "committee",
                        "label": "3-member inquiry",
                        "detail": "SC judge/CJI + HC CJ + distinguished jurist.",
                        "options": [
                            {"label": "Guilty", "next": "houses"},
                            {"label": "Not guilty", "next": "end"},
                        ],
                    },
                    {
                        "id": "houses",
                        "label": "Both Houses — special majority",
                        "detail": "Total membership + ⅔ present & voting; same session.",
                        "options": [{"label": "Address presented", "next": "president"}],
                    },
                    {
                        "id": "president",
                        "label": "President’s removal order",
                        "detail": "Judge removed from office.",
                    },
                    {
                        "id": "end",
                        "label": "Process stops",
                        "detail": "No removal — e.g. Ramaswami motion failed in LS.",
                    },
                ],
            },
            {
                "id": "sc-remove-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Wording trap",
                "body": (
                    "The Constitution does **not** use the word ‘impeachment’ for judges "
                    "(that word is used for the President). Still, UPSC often says "
                    "‘impeachment-like process’ — know the **100/50** and special-majority numbers."
                ),
            },
        ],
    },
    {
        "title": "Acting, ad hoc, seat & procedure",
        "slug": "sc-acting-seat",
        "sort_order": 6,
        "summary": (
            "Acting CJI, ad hoc HC judge, retired judges; Delhi seat with optional "
            "other seats; constitutional / Art. 143 benches of at least five."
        ),
        "body": (
            "## Acting Chief Justice (Art. 126)\n\n"
            "President may appoint an SC judge as acting CJI when the office is vacant, "
            "or the CJI is temporarily absent, or unable to perform duties.\n\n"
            "## Ad hoc judge (Art. 127)\n\n"
            "If quorum of permanent judges is lacking, **CJI** may appoint a High Court "
            "judge as ad hoc SC judge — after consulting that HC’s Chief Justice and with "
            "**previous consent of the President**. Must be SC-qualified. Attends SC in "
            "priority to other duties; enjoys SC judge’s jurisdiction, powers, privileges.\n\n"
            "## Retired judge (Art. 128)\n\n"
            "CJI may request a retired SC or (qualified) retired HC judge to act temporarily — "
            "with previous consent of the **President** and of the person. Enjoys powers/"
            "privileges but is **not otherwise deemed** a judge of the Supreme Court.\n\n"
            "## Seat (Art. 130)\n\n"
            "Constitution declares **Delhi** as the seat. CJI may appoint other place(s) "
            "with **President’s approval** — optional, not compulsory; no court can mandamus "
            "the President or CJI to do so.\n\n"
            "## Procedure\n\n"
            "SC makes rules with President’s approval. **Constitutional cases** and "
            "**Art. 143 references** → bench of at least **five** judges. Other cases → "
            "single judges / division benches. Judgments in open court; majority decides; "
            "dissenting opinions allowed."
        ),
        "articles": [
            ("Article 126", "Appointment of acting Chief Justice."),
            ("Article 127", "Appointment of ad hoc judges."),
            ("Article 128", "Attendance of retired judges at sittings."),
            ("Article 130", "Seat of Supreme Court."),
            ("Article 145", "Rules of court, etc."),
        ],
        "visual_blocks": [
            {
                "id": "sc-acting-compare",
                "type": "comparison",
                "title": "Acting vs Ad hoc vs Retired",
                "columns": [
                    {
                        "id": "acting",
                        "heading": "Acting CJI (126)",
                        "points": [
                            "Appointed by President",
                            "SC judge fills CJI vacancy/absence/inability",
                            "Temporary head of Court",
                        ],
                    },
                    {
                        "id": "adhoc",
                        "heading": "Ad hoc (127)",
                        "points": [
                            "CJI appoints HC judge",
                            "Need: HC CJ consult + President consent",
                            "Quorum shortage; full SC powers while sitting",
                        ],
                    },
                    {
                        "id": "retired",
                        "heading": "Retired (128)",
                        "points": [
                            "CJI requests retired SC/HC judge",
                            "President + person must consent",
                            "Powers yes; not ‘deemed’ SC judge otherwise",
                        ],
                    },
                ],
            },
            {
                "id": "sc-bench-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook — constitutional bench",
                "body": (
                    "Constitutional cases and Presidential references under Art. 143 "
                    "are decided by a bench of **at least five** judges."
                ),
            },
        ],
    },
    {
        "title": "Independence of the Supreme Court",
        "slug": "sc-independence",
        "sort_order": 7,
        "summary": (
            "Nine constitutional safeguards — from appointment mode and tenure security "
            "to CFI charge, contempt power, and non-curtailment of jurisdiction."
        ),
        "body": (
            "## Why independence?\n\n"
            "The SC is a federal court, highest court of appeal, guarantor of Fundamental "
            "Rights, and guardian of the Constitution. It must be free from executive and "
            "legislative pressure.\n\n"
            "### Nine safeguards (revision spine)\n"
            "1. **Mode of appointment** — President with judiciary’s consultation (curbs absolute executive discretion).\n"
            "2. **Security of tenure** — removal only as Constitution provides (not during pleasure).\n"
            "3. **Fixed service conditions** — no disadvantageous change except financial emergency.\n"
            "4. **Expenses on Consolidated Fund** — non-votable (can be discussed).\n"
            "5. **Conduct not discussable** — in Parliament/state legislatures except during removal motion.\n"
            "6. **Ban on practice after retirement** — no pleading/acting in any court/authority in India.\n"
            "7. **Contempt power** — protects authority, dignity, honour.\n"
            "8. **Freedom to appoint staff** — CJI appoints officers/servants; sets service conditions.\n"
            "9. **Jurisdiction cannot be curtailed** — Parliament may **extend**, not cut down, guaranteed jurisdiction.\n\n"
            "### Memory aid\n"
            "**A-T-S-C-C-B-C-S-J** — Appoint · Tenure · Salary · Charged · Conduct · Ban · Contempt · Staff · Jurisdiction."
        ),
        "articles": [
            ("Article 124", "Appointment, tenure, removal — independence through process."),
            ("Article 125 / 146", "Salaries; officers, servants, expenses charged on CFI."),
            ("Article 121 / 211", "Restriction on discussion of judges’ conduct."),
            ("Article 129", "Court of Record — contempt power."),
            ("Article 138", "Enlargement (not curtailment) of jurisdiction."),
        ],
        "visual_blocks": [
            {
                "id": "sc-indep-pillars",
                "type": "pillars",
                "title": "Nine independence chips",
                "items": [
                    {
                        "id": "i1",
                        "articles": "1",
                        "label": "Mode of appointment",
                        "slug": "sc-appointment",
                        "detail": "President + judiciary consultation / collegium.",
                        "tone": "teal",
                    },
                    {
                        "id": "i2",
                        "articles": "2",
                        "label": "Security of tenure",
                        "slug": "sc-tenure-removal",
                        "detail": "Not during pleasure; only constitutional removal.",
                        "tone": "olive",
                    },
                    {
                        "id": "i3",
                        "articles": "3",
                        "label": "Fixed service conditions",
                        "slug": "sc-qual-oath",
                        "detail": "No disadvantageous change except financial emergency.",
                        "tone": "gold",
                    },
                    {
                        "id": "i4",
                        "articles": "4",
                        "label": "Charged on CFI",
                        "slug": "sc-independence",
                        "detail": "Salaries + admin expenses — non-votable.",
                        "tone": "orange",
                    },
                    {
                        "id": "i5",
                        "articles": "5",
                        "label": "Conduct not discussable",
                        "slug": "sc-independence",
                        "detail": "Except when removal motion is under consideration.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "i6",
                        "articles": "6",
                        "label": "Ban on practice",
                        "slug": "sc-independence",
                        "detail": "Retired SC judges barred from practice in India.",
                        "tone": "maroon",
                    },
                    {
                        "id": "i7",
                        "articles": "7",
                        "label": "Contempt power",
                        "slug": "sc-advisory-record",
                        "detail": "Punish contempt to protect authority.",
                        "tone": "teal",
                    },
                    {
                        "id": "i8",
                        "articles": "8",
                        "label": "Appoint own staff",
                        "slug": "sc-independence",
                        "detail": "CJI appoints officers/servants without executive interference.",
                        "tone": "olive",
                    },
                    {
                        "id": "i9",
                        "articles": "9",
                        "label": "Jurisdiction protected",
                        "slug": "sc-jurisdiction-map",
                        "detail": "Parliament may extend, not curtail, SC jurisdiction.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "sc-indep-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "Independence is **structural**, not ceremonial — lock the nine chips "
                    "and the extend-not-curtail rule for both Prelims and Mains."
                ),
            },
        ],
    },
    {
        "title": "Jurisdiction & powers overview",
        "slug": "sc-jurisdiction-map",
        "sort_order": 8,
        "summary": (
            "Nine-power map: original, writ, appellate, advisory, court of record, "
            "judicial review, review, constitutional interpretation, and other powers."
        ),
        "body": (
            "## Vast jurisdiction\n\n"
            "The Supreme Court is not only a federal court (like the US SC) but also a "
            "final court of appeal (British tradition), guardian/interpreter of the "
            "Constitution, guarantor of FRs, plus advisory and supervisory roles.\n\n"
            "### Nine-pack (drill each cluster)\n"
            "1. Original jurisdiction\n"
            "2. Writ jurisdiction\n"
            "3. Appellate jurisdiction\n"
            "4. Advisory jurisdiction\n"
            "5. Court of Record\n"
            "6. Judicial review\n"
            "7. Review jurisdiction\n"
            "8. Constitutional interpretation\n"
            "9. Other powers\n\n"
            "Deep dive on **judicial review** continues in Laxmikanth Ch.27 — this chapter "
            "keeps a revision snapshot only."
        ),
        "articles": [
            ("Articles 131–143", "Core jurisdiction articles — original through advisory."),
            ("Articles 129, 137, 141–142", "Record, review, binding law, enforcement."),
        ],
        "visual_blocks": [
            {
                "id": "sc-jmap-pillars",
                "type": "pillars",
                "title": "Nine jurisdiction chips",
                "items": [
                    {
                        "id": "j1",
                        "articles": "131",
                        "label": "Original",
                        "slug": "sc-original-writ",
                        "detail": "Federal Centre–state / inter-state disputes.",
                        "tone": "teal",
                    },
                    {
                        "id": "j2",
                        "articles": "32",
                        "label": "Writ",
                        "slug": "sc-original-writ",
                        "detail": "FR enforcement — heart of the Constitution.",
                        "tone": "olive",
                    },
                    {
                        "id": "j3",
                        "articles": "132–136",
                        "label": "Appellate + SLP",
                        "slug": "sc-appellate",
                        "detail": "Constitutional, civil, criminal + special leave.",
                        "tone": "gold",
                    },
                    {
                        "id": "j4",
                        "articles": "143",
                        "label": "Advisory",
                        "slug": "sc-advisory-record",
                        "detail": "President may consult; opinion not binding.",
                        "tone": "orange",
                    },
                    {
                        "id": "j5",
                        "articles": "129",
                        "label": "Court of Record",
                        "slug": "sc-advisory-record",
                        "detail": "Precedents + contempt power.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "j6",
                        "articles": "JR",
                        "label": "Judicial review",
                        "slug": "sc-review-other",
                        "detail": "Ultra vires laws/acts → void (Ch.27 depth).",
                        "tone": "maroon",
                    },
                    {
                        "id": "j7",
                        "articles": "137",
                        "label": "Review",
                        "slug": "sc-review-other",
                        "detail": "Review own judgments; curative after dismissal.",
                        "tone": "teal",
                    },
                    {
                        "id": "j8",
                        "articles": "Doctrines",
                        "label": "Interpretation",
                        "slug": "sc-review-other",
                        "detail": "Final interpreter — severability, pith & substance…",
                        "tone": "olive",
                    },
                    {
                        "id": "j9",
                        "articles": "Other",
                        "label": "Other powers",
                        "slug": "sc-review-other",
                        "detail": "Elections, UPSC refs, transfer, Art. 141–142…",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "sc-jmap-tip",
                "type": "callout",
                "tone": "tip",
                "title": "One-liner",
                "body": (
                    "More than a US-style federal court — also British-style final appeal, "
                    "advisory jurisdiction, and integrated superintendence over lower courts."
                ),
            },
        ],
    },
    {
        "title": "Original & writ jurisdiction",
        "slug": "sc-original-writ",
        "sort_order": 9,
        "summary": (
            "Art. 131 federal disputes (with water-dispute exclusion); Art. 32 FR writs; "
            "compare with wider Art. 226 High Court writs."
        ),
        "body": (
            "## Original jurisdiction (Art. 131)\n\n"
            "Exclusive original jurisdiction in federal disputes:\n"
            "- Centre vs one or more states;\n"
            "- Centre + any state(s) vs one or more other states;\n"
            "- State vs state.\n\n"
            "**Excluded:** disputes from pre-Constitution treaties/agreements (unless "
            "continued); **inter-state river water** disputes under the Inter-State River "
            "Water Disputes Act, 1956.\n\n"
            "## Writ jurisdiction (Art. 32)\n\n"
            "Right to move the SC for enforcement of Fundamental Rights — called the "
            "**heart and soul** / guarantee of Part III. When an FR is violated, the Court "
            "cannot refuse on mere technicalities.\n\n"
            "Writs: habeas corpus, mandamus, prohibition, certiorari, quo warranto.\n\n"
            "Parliament may by law empower the SC to issue writs for **other purposes** "
            "(Art. 139)."
        ),
        "articles": [
            ("Article 131", "Original jurisdiction of the Supreme Court."),
            ("Article 32", "Remedies for enforcement of Fundamental Rights."),
            ("Article 226", "High Court writs — FR + other legal rights."),
            ("Article 139", "Parliament may confer additional writ powers on the SC."),
        ],
        "visual_blocks": [
            {
                "id": "sc-writ-compare",
                "type": "comparison",
                "title": "Art. 32 vs Art. 226",
                "columns": [
                    {
                        "id": "a32",
                        "heading": "Article 32 (SC)",
                        "points": [
                            "Fundamental Right itself",
                            "Only for enforcement of FRs",
                            "Cannot be refused when FR violated",
                            "Against State for Part III rights",
                        ],
                    },
                    {
                        "id": "a226",
                        "heading": "Article 226 (HC)",
                        "points": [
                            "Constitutional power of High Courts",
                            "FRs + other legal rights",
                            "Wider scope than Art. 32",
                            "Territorial limits of the High Court",
                        ],
                    },
                ],
            },
            {
                "id": "sc-orig-flow",
                "type": "flowchart",
                "title": "Does Art. 131 apply?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Federal party dispute?",
                        "detail": "Centre–state, Centre+state(s) vs other state(s), or state–state.",
                        "options": [
                            {"label": "Yes — check exclusions", "next": "excl"},
                            {"label": "No", "next": "no"},
                        ],
                    },
                    {
                        "id": "excl",
                        "label": "Excluded subject?",
                        "detail": "Pre-Constitution treaty (unless continued) or inter-state river water (1956 Act).",
                        "options": [
                            {"label": "Excluded", "next": "out"},
                            {"label": "Not excluded", "next": "yes"},
                        ],
                    },
                    {
                        "id": "yes",
                        "label": "Art. 131 original jurisdiction",
                        "detail": "Exclusive federal dispute before the Supreme Court.",
                    },
                    {
                        "id": "out",
                        "label": "Outside Art. 131",
                        "detail": "e.g. water disputes go to tribunal route under the 1956 Act.",
                    },
                    {
                        "id": "no",
                        "label": "Not original federal jurisdiction",
                        "detail": "Use appellate, writ, or other appropriate jurisdiction.",
                    },
                ],
            },
            {
                "id": "sc-writ-tip",
                "type": "callout",
                "tone": "note",
                "title": "Prelims note",
                "body": (
                    "HC writs are **wider** in subject-matter; SC Art. 32 is a "
                    "**Fundamental Right** limited to FRs. Water disputes ≠ Art. 131."
                ),
            },
        ],
    },
    {
        "title": "Appellate jurisdiction & SLP",
        "slug": "sc-appellate",
        "sort_order": 10,
        "summary": (
            "Appeals from High Courts on constitutional, civil, and criminal matters; "
            "Art. 136 special leave — plenary discretion except military tribunals."
        ),
        "body": (
            "## Three appellate streams\n\n"
            "1. **Constitutional** (Art. 132) — substantial question of law as to "
            "interpretation of the Constitution.\n"
            "2. **Civil** (Art. 133) — civil matters from High Courts (with certificate/"
            "conditions).\n"
            "3. **Criminal** (Art. 134) — criminal matters from High Courts "
            "(as specified).\n\n"
            "**Art. 134A** — certificate for appeal to the Supreme Court.\n\n"
            "Parliament enlarged criminal appellate jurisdiction in 1970.\n\n"
            "## Special Leave to Appeal (Art. 136)\n\n"
            "SC may, in its discretion, grant special leave to appeal from any judgment, "
            "decree, determination, sentence or order of **any court or tribunal** in "
            "India — **except** military courts/tribunals.\n\n"
            "This plenary power is a major India–USA differentiator. SLP is **not a right** "
            "— pure judicial discretion."
        ),
        "articles": [
            ("Article 132", "Appellate jurisdiction — constitutional questions from HCs."),
            ("Article 133", "Appellate jurisdiction — civil matters."),
            ("Article 134", "Appellate jurisdiction — criminal matters."),
            ("Article 134A", "Certificate for appeal to the Supreme Court."),
            ("Article 136", "Special leave to appeal by the Supreme Court."),
        ],
        "visual_blocks": [
            {
                "id": "sc-app-flow",
                "type": "flowchart",
                "title": "Path to the Supreme Court",
                "root": "hc",
                "steps": [
                    {
                        "id": "hc",
                        "label": "High Court judgment / order",
                        "detail": "Starting point for most ordinary appeals.",
                        "options": [
                            {"label": "Constitutional question", "next": "a132"},
                            {"label": "Civil matter", "next": "a133"},
                            {"label": "Criminal matter", "next": "a134"},
                            {"label": "No certificate / residual", "next": "slp"},
                        ],
                    },
                    {
                        "id": "a132",
                        "label": "Art. 132 appeal",
                        "detail": "Substantial question of law as to Constitution.",
                    },
                    {
                        "id": "a133",
                        "label": "Art. 133 appeal",
                        "detail": "Civil appellate route (with conditions/certificate).",
                    },
                    {
                        "id": "a134",
                        "label": "Art. 134 appeal",
                        "detail": "Criminal appellate route as specified.",
                    },
                    {
                        "id": "slp",
                        "label": "Art. 136 SLP",
                        "detail": "Discretionary leave vs any court/tribunal except military.",
                    },
                ],
            },
            {
                "id": "sc-slp-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Art. 136 is **discretion**, not a right. It does **not** cover "
                    "military courts/tribunals. USA has no equivalent plenary SLP power."
                ),
            },
        ],
    },
    {
        "title": "Advisory jurisdiction & Court of Record",
        "slug": "sc-advisory-record",
        "sort_order": 11,
        "summary": (
            "Art. 143 consultative opinions (non-binding); 15 references so far; "
            "Art. 129 Court of Record and contempt under the 1971 Act."
        ),
        "body": (
            "## Advisory jurisdiction (Art. 143)\n\n"
            "1. President **may** refer a question of law or fact of public importance — "
            "Court **may** tender or refuse opinion.\n"
            "2. On certain pre-Constitution treaty/agreement matters — Court **must** "
            "tender opinion.\n\n"
            "In both cases the opinion is **advisory, not a judicial pronouncement** — "
            "**not binding** on the President.\n\n"
            "About **15 references** so far. High-yield ones: Berubari (1960), Cauvery "
            "(1992), Ram Janmabhoomi (1993), Consultation process (1998), "
            "2G / natural resources auction (2012).\n\n"
            "## Court of Record (Art. 129)\n\n"
            "Two powers:\n"
            "(a) Judgments/proceedings recorded as perpetual evidence and precedent.\n"
            "(b) Power to punish for **contempt** — including of HCs, subordinate courts "
            "and tribunals nationwide (1991 ruling).\n\n"
            "### Contempt of Courts Act, 1971\n"
            "- **Civil:** wilful disobedience of court order/undertaking.\n"
            "- **Criminal:** scandalises court / prejudices proceeding / obstructs justice.\n"
            "- Defences: innocent publication, fair accurate report, fair criticism.\n"
            "- Punishment: up to **6 months** simple imprisonment and/or fine up to **₹2,000**.\n"
            "- Limitation: no proceedings after **1 year** from alleged contempt.\n"
            "- Not applicable to Nyaya Panchayats / village courts."
        ),
        "articles": [
            ("Article 143", "Power of President to consult the Supreme Court."),
            ("Article 129", "Supreme Court to be a court of record."),
            ("Contempt of Courts Act, 1971", "Civil/criminal contempt, defences, punishment, limitation."),
        ],
        "visual_blocks": [
            {
                "id": "sc-adv-timeline",
                "type": "timeline",
                "title": "High-yield Art. 143 references",
                "events": [
                    {"id": "r1960", "year": 1960, "label": "Berubari Union", "detail": "Territory transfer — amendment needed"},
                    {"id": "r1992", "year": 1992, "label": "Cauvery Tribunal", "detail": "Water disputes & SC role"},
                    {"id": "r1993", "year": 1993, "label": "Ram Janmabhoomi", "detail": "Sensitive reference"},
                    {"id": "r1998", "year": 1998, "label": "Consultation process", "detail": "Led to Third Judges norms"},
                    {"id": "r2012", "year": 2012, "label": "2G / natural resources", "detail": "Mandatory auction theme"},
                ],
            },
            {
                "id": "sc-adv-compare",
                "type": "comparison",
                "title": "Art. 143 clauses at a glance",
                "columns": [
                    {
                        "id": "c1",
                        "heading": "Clause (1)",
                        "points": [
                            "President may refer",
                            "Court may refuse",
                            "Public importance Q of law/fact",
                            "Opinion not binding",
                        ],
                    },
                    {
                        "id": "c2",
                        "heading": "Clause (2)",
                        "points": [
                            "Pre-Constitution treaty matters",
                            "Court must tender opinion",
                            "Still advisory only",
                            "President need not follow",
                        ],
                    },
                ],
            },
            {
                "id": "sc-adv-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "Lock: **15 references**; opinion **never binding**; contrast with "
                    "UPSC/SPSC misbehaviour reference where SC advice **is binding** "
                    "on the President."
                ),
            },
        ],
    },
    {
        "title": "Review, JR snapshot, doctrines & other powers",
        "slug": "sc-review-other",
        "sort_order": 12,
        "summary": (
            "Art. 137 review and curative petitions; JR one-liner; 13 interpretation "
            "doctrines; elections, UPSC refs, Arts 141–142, superintendence."
        ),
        "body": (
            "## Review jurisdiction (Art. 137)\n\n"
            "SC may review its own judgment/order. File within **30 days**; usually "
            "before the **same bench**. Grounds: new important evidence; error apparent "
            "on the face of the record; any other sufficient reason.\n\n"
            "### Curative petition\n"
            "Even after review dismissal, limited reconsideration to cure gross "
            "miscarriage of justice: natural justice violation; abuse of process; "
            "bias of the judge.\n\n"
            "## Judicial review (snapshot)\n\n"
            "Power to examine constitutionality of Centre/state laws and executive "
            "orders. If ultra vires → illegal, unconstitutional, null and void. "
            "(Full chapter: Judicial Review.)\n\n"
            "## Constitutional interpretation — doctrines (names + cue)\n"
            "Severability · Waiver · Eclipse · Territorial nexus · Pith & substance · "
            "Colourable legislation · Implied powers · Incidental/ancillary · Precedent · "
            "Occupied field · Prospective overruling · Harmonious construction · "
            "Liberal interpretation.\n\n"
            "## Other powers\n"
            "- President/VP **election disputes** — original, exclusive, final.\n"
            "- **UPSC/SPSC/JSPSC** misbehaviour reference — advice **binding** on President.\n"
            "- Withdraw HC cases / transfer between HCs.\n"
            "- **Art. 141** — law declared by SC binding on all courts.\n"
            "- **Art. 142** — enforce decrees; do complete justice.\n"
            "- Judicial superintendence over courts/tribunals in India.\n"
            "- Jurisdiction enlarged by Parliament (Union list) or Centre–state agreement."
        ),
        "articles": [
            ("Article 137", "Review of judgments or orders by the Supreme Court."),
            ("Article 141", "Law declared by SC binding on all courts."),
            ("Article 142", "Enforcement of decrees and orders; complete justice."),
            ("Article 138", "Enlargement of the jurisdiction of the Supreme Court."),
            ("Article 139A", "Transfer of certain cases."),
        ],
        "visual_blocks": [
            {
                "id": "sc-review-flow",
                "type": "flowchart",
                "title": "After a final SC judgment",
                "root": "judgment",
                "steps": [
                    {
                        "id": "judgment",
                        "label": "SC judgment / order",
                        "detail": "Ordinary finality.",
                        "options": [{"label": "Seek review?", "next": "review"}],
                    },
                    {
                        "id": "review",
                        "label": "Review petition (Art. 137)",
                        "detail": "30 days; same bench; new evidence / apparent error / sufficient reason.",
                        "options": [
                            {"label": "Dismissed", "next": "curative"},
                            {"label": "Allowed / notice", "next": "reopen"},
                        ],
                    },
                    {
                        "id": "curative",
                        "label": "Curative petition",
                        "detail": "Natural justice / miscarriage / abuse / bias — very narrow.",
                    },
                    {
                        "id": "reopen",
                        "label": "Matter reconsidered",
                        "detail": "Court may modify or affirm after hearing.",
                    },
                ],
            },
            {
                "id": "sc-doctrine-pillars",
                "type": "pillars",
                "title": "High-yield doctrines (cue cards)",
                "items": [
                    {
                        "id": "d1",
                        "articles": "1",
                        "label": "Severability",
                        "slug": "sc-review-other",
                        "detail": "Strike bad part; save the rest if separable.",
                        "tone": "teal",
                    },
                    {
                        "id": "d2",
                        "articles": "2",
                        "label": "Eclipse",
                        "slug": "sc-review-other",
                        "detail": "Pre-Constitution law shadowed by FR; revives if shadow lifts.",
                        "tone": "olive",
                    },
                    {
                        "id": "d3",
                        "articles": "3",
                        "label": "Pith & substance",
                        "slug": "sc-review-other",
                        "detail": "True nature of law decides legislative competence.",
                        "tone": "gold",
                    },
                    {
                        "id": "d4",
                        "articles": "4",
                        "label": "Colourable legislation",
                        "slug": "sc-review-other",
                        "detail": "What you cannot do directly, you cannot do indirectly.",
                        "tone": "orange",
                    },
                    {
                        "id": "d5",
                        "articles": "5",
                        "label": "Harmonious construction",
                        "slug": "sc-review-other",
                        "detail": "Read provisions to avoid conflict where possible.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "d6",
                        "articles": "6",
                        "label": "Prospective overruling",
                        "slug": "sc-review-other",
                        "detail": "New ruling applies forward; protects past transactions.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "sc-other-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Binding vs advisory",
                "body": (
                    "Art. **143** opinion — **not** binding. UPSC/SPSC misbehaviour "
                    "reference — SC advice **is binding** on the President. Do not mix them."
                ),
            },
        ],
    },
    {
        "title": "India vs USA Supreme Courts",
        "slug": "sc-india-usa",
        "sort_order": 13,
        "summary": (
            "Eight-point comparison: original scope, appellate breadth, SLP, advisory, "
            "JR width, due process vs procedure, enlargement, superintendence."
        ),
        "body": (
            "## Redesigned Table 26.1\n\n"
            "Use this as a single-screen Prelims/Mains comparison. India’s SC combines "
            "federal + wide appellate + advisory roles inside an **integrated** judiciary; "
            "the US SC sits atop a **dual** court system with narrower appellate reach "
            "and no advisory opinions."
        ),
        "articles": [
            ("Laxmikanth Table 26.1", "Comparing Indian and American Supreme Courts."),
            ("Article 21 cue", "India — procedure established by law (vs US due process of law)."),
        ],
        "visual_blocks": [
            {
                "id": "sc-usa-compare",
                "type": "comparison",
                "title": "Indian SC vs American SC",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Original jurisdiction mainly federal cases",
                            "Appellate: constitutional + civil + criminal",
                            "Wide Art. 136 SLP (except military)",
                            "Has advisory jurisdiction (Art. 143)",
                            "JR scope relatively limited (procedure established by law)",
                            "Defends rights via ‘procedure established by law’",
                            "Parliament can enlarge jurisdiction",
                            "Superintendence over HCs — integrated system",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Original also covers admiralty, ambassadors, etc.",
                            "Appellate mainly constitutional cases",
                            "No equivalent plenary SLP power",
                            "No advisory jurisdiction",
                            "Very wide judicial review",
                            "Defends rights via ‘due process of law’",
                            "Jurisdiction largely fixed by Constitution",
                            "No such superintendence — dual judiciary",
                        ],
                    },
                ],
            },
            {
                "id": "sc-usa-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "**S-A-J-D-E-S** — SLP · Advisory · JR width · Due process contrast · "
                    "Enlargement by Parliament · Superintendence. Those six win most MCQs."
                ),
            },
        ],
    },
    {
        "title": "Articles glance & exam revision",
        "slug": "sc-exam-revision",
        "sort_order": 14,
        "summary": (
            "Compressed Arts 124–147 map, Prelims fact box, PYQ themes, mains "
            "value-adds, and classic traps."
        ),
        "body": (
            "## Articles at a glance (compressed)\n\n"
            "| Article | Subject |\n"
            "|---|---|\n"
            "| 124 | Establishment & constitution of SC |\n"
            "| 124A–C | NJAC text (void after Fourth Judges) |\n"
            "| 125 | Salaries etc. |\n"
            "| 126–128 | Acting CJI · ad hoc · retired judges |\n"
            "| 129–130 | Court of Record · Seat |\n"
            "| 131 | Original jurisdiction |\n"
            "| 131A / 144A | Repealed |\n"
            "| 132–134A | Appellate + certificate |\n"
            "| 136–137 | SLP · Review |\n"
            "| 138–140 | Enlargement · writs · ancillary |\n"
            "| 141–144 | Binding law · enforcement · aid to SC |\n"
            "| 143 | Advisory jurisdiction |\n"
            "| 145–147 | Rules · staff/expenses · interpretation |\n\n"
            "### Prelims facts box\n"
            "- **34** judges (2019); retire at **65**.\n"
            "- Constitutional / Art. 143 bench ≥ **5**.\n"
            "- Seat: **Delhi** (other seats optional with President).\n"
            "- Expenses **charged on CFI**; no practice after retirement.\n"
            "- Water disputes **excluded** from Art. 131.\n"
            "- Art. 143 opinion **non-binding**.\n"
            "- Removal motion: **100** LS / **50** RS.\n\n"
            "### PYQ themes\n"
            "Collegium evolution · independence devices · Art. 32 vs 226 · Art. 136 · "
            "advisory nature · Court of Record · composition Acts · impeachment numbers.\n\n"
            "### Mains value-adds\n"
            "Independence vs accountability (NJAC debate); integrated judiciary & "
            "federalism; SLP and docket pressure; constitutional bench discipline; "
            "extend-not-curtail jurisdiction."
        ),
        "articles": [
            ("Articles 124–147", "Full SC block in Part V — organisation through interpretation."),
            ("Laxmikanth Table 26.3", "Articles related to Supreme Court at a glance."),
        ],
        "visual_blocks": [
            {
                "id": "sc-exam-tree",
                "type": "tree",
                "title": "Article clusters for last-minute scan",
                "root": {
                    "id": "arts",
                    "label": "Arts 124–147",
                    "detail": "Part V — Supreme Court",
                    "children": [
                        {
                            "id": "org",
                            "label": "124–130 Organisation",
                            "detail": "Strength, appointment, acting, seat, record",
                        },
                        {
                            "id": "jur",
                            "label": "131–143 Jurisdiction",
                            "detail": "Original → advisory spine",
                        },
                        {
                            "id": "ops",
                            "label": "138–147 Operations",
                            "detail": "Enlargement, binding law, rules, staff",
                        },
                    ],
                },
            },
            {
                "id": "sc-exam-heat",
                "type": "pyq_heatmap",
                "title": "Cluster PYQ heat",
                "items": [
                    {"concept_slug": "sc-appointment", "label": "Collegium"},
                    {"concept_slug": "sc-independence", "label": "Independence"},
                    {"concept_slug": "sc-original-writ", "label": "32 / 131"},
                    {"concept_slug": "sc-appellate", "label": "136 SLP"},
                    {"concept_slug": "sc-advisory-record", "label": "143 / 129"},
                    {"concept_slug": "sc-tenure-removal", "label": "Removal"},
                    {"concept_slug": "sc-india-usa", "label": "India–USA"},
                    {"concept_slug": "sc-composition", "label": "Strength"},
                ],
            },
            {
                "id": "sc-exam-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Last-minute traps",
                "body": (
                    "NJAC ≠ current · Art. 143 ≠ binding · ‘impeachment’ word not in "
                    "Constitution for judges · HC writs wider than Art. 32 · SLP skips "
                    "military only · strength raised by **Parliament**, not amendment alone."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "sc-footing"),
    (HUB_SLUG, "parent", "sc-composition"),
    (HUB_SLUG, "parent", "sc-appointment"),
    (HUB_SLUG, "parent", "sc-qual-oath"),
    (HUB_SLUG, "parent", "sc-tenure-removal"),
    (HUB_SLUG, "parent", "sc-acting-seat"),
    (HUB_SLUG, "parent", "sc-independence"),
    (HUB_SLUG, "parent", "sc-jurisdiction-map"),
    (HUB_SLUG, "parent", "sc-original-writ"),
    (HUB_SLUG, "parent", "sc-appellate"),
    (HUB_SLUG, "parent", "sc-advisory-record"),
    (HUB_SLUG, "parent", "sc-review-other"),
    (HUB_SLUG, "parent", "sc-india-usa"),
    (HUB_SLUG, "parent", "sc-exam-revision"),
    ("sc-jurisdiction-map", "related", "sc-original-writ"),
    ("sc-jurisdiction-map", "related", "sc-appellate"),
    ("sc-jurisdiction-map", "related", "sc-advisory-record"),
    ("sc-jurisdiction-map", "related", "sc-review-other"),
    ("sc-appointment", "related", "sc-independence"),
    ("sc-tenure-removal", "related", "sc-independence"),
    ("sc-original-writ", "related", "sc-appellate"),
    ("sc-india-usa", "related", "sc-footing"),
    ("sc-exam-revision", "related", "sc-appointment"),
    ("fundamental-rights", "related", HUB_SLUG),
    ("fr-remedies-32", "related", "sc-original-writ"),
    ("judicial-review", "related", HUB_SLUG),
    ("president", "related", "sc-advisory-record"),
    ("basic-structure", "related", "sc-appointment"),
    ("sf-integrated-judiciary", "related", "sc-footing"),
]

SAMPLE_PYQS = [
    (
        2019,
        "With reference to the Constitution of India, prohibitions or limitations or provisions contained in ordinary laws cannot act as prohibitions or limitations on the constitutional powers under Article 142. This suggests that:",
        "Art. 142 enables the Supreme Court to do ‘complete justice’ — ordinary law limits do not cabin that constitutional power (classic SC jurisdiction theme).",
        ["sc-review-other", "sc-exam-revision"],
    ),
    (
        2021,
        "With reference to Indian judiciary, consider: (1) Any retired judge of the Supreme Court can be called to sit as a judge. (2) A High Court judge can be appointed as an ad hoc judge of the Supreme Court.",
        "Both themes appear in Arts 127–128 — ad hoc HC judge with consents; retired judge attendance with President + person’s consent (check exact statement wording in the paper).",
        ["sc-acting-seat", "sc-exam-revision"],
    ),
    (
        2018,
        "Consider the following statements about the Supreme Court’s advisory jurisdiction under Article 143:",
        "Opinion is advisory and not binding on the President; under clause (1) the Court may refuse to opine.",
        ["sc-advisory-record", "sc-exam-revision"],
    ),
    (
        2017,
        "Which of the following are the circumstances when an acting Chief Justice of India can be appointed?",
        "Vacancy in CJI office; temporary absence; inability to perform duties (Art. 126).",
        ["sc-acting-seat"],
    ),
    (
        2015,
        "The power of the Supreme Court of India to decide disputes between the Centre and the States falls under its:",
        "Original jurisdiction (Art. 131).",
        ["sc-original-writ", "sc-jurisdiction-map"],
    ),
    (
        2014,
        "The power to increase the number of judges in the Supreme Court of India is vested in:",
        "Parliament (by law under Art. 124(1)).",
        ["sc-composition", "sc-exam-revision"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "First Judges Case (S.P. Gupta)",
        "slug": "first-judges-case",
        "parties": "S.P. Gupta v. Union of India",
        "year": 1981,
        "court": CaseLaw.Court.SC,
        "summary": "Interpreted ‘consultation’ in judicial appointments as exchange of views, not concurrence.",
        "holding": (
            "Consultation does not mean concurrence — it only implies exchange of views "
            "between the executive and the judiciary."
        ),
        "concept_slugs": [HUB_SLUG, "sc-appointment", "sc-independence"],
    },
    {
        "title": "Second Judges Case (SCARA)",
        "slug": "second-judges-case",
        "parties": "Supreme Court Advocates-on-Record Association v. Union of India",
        "year": 1993,
        "court": CaseLaw.Court.SC,
        "summary": "Turned consultation into concurrence; seeded collegium; seniormost judge as CJI.",
        "holding": (
            "CJI’s advice is binding on the President in SC appointments; CJI consults two "
            "seniormost colleagues; only the seniormost SC judge should be appointed CJI."
        ),
        "concept_slugs": [HUB_SLUG, "sc-appointment", "sc-independence"],
    },
    {
        "title": "Third Judges Case (In Re Presidential Reference)",
        "slug": "third-judges-case",
        "parties": "In Re Presidential Reference (Art. 143)",
        "year": 1998,
        "court": CaseLaw.Court.SC,
        "summary": "Plurality consultation — collegium of CJI + four seniormost judges.",
        "holding": (
            "Sole opinion of the CJI is not ‘consultation’; collegium of four seniormost "
            "judges required; if two give adverse opinion, recommendation should not go forward."
        ),
        "concept_slugs": [HUB_SLUG, "sc-appointment", "sc-advisory-record"],
    },
    {
        "title": "Fourth Judges Case (NJAC)",
        "slug": "fourth-judges-case",
        "parties": "Supreme Court Advocates-on-Record Association v. Union of India",
        "year": 2015,
        "court": CaseLaw.Court.SC,
        "summary": "Struck down 99th Amendment and NJAC Act; restored collegium.",
        "holding": (
            "99th Constitutional Amendment and NJAC Act are unconstitutional and void — "
            "NJAC would affect independence of the judiciary; collegium system revived."
        ),
        "concept_slugs": [HUB_SLUG, "sc-appointment", "sc-independence", "sc-exam-revision"],
    },
]

AMENDMENTS = [
    {
        "number": 99,
        "year": 2014,
        "title": "Ninety-ninth Amendment",
        "summary": (
            "Inserted Arts 124A–C to create the National Judicial Appointments Commission "
            "replacing the collegium for SC/HC appointments — struck down in 2015."
        ),
        "effect": (
            "Intended to replace collegium with NJAC; declared unconstitutional in Fourth "
            "Judges case (2015) along with the NJAC Act — collegium restored."
        ),
        "concept_slugs": [HUB_SLUG, "sc-appointment", "sc-exam-revision"],
    },
]


class Command(BaseCommand):
    help = "Seed Supreme Court chapter (Laxmikanth Ch.26)."

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
                "title": "Supreme Court",
                "sort_order": 11,
                "book_ref": "Laxmikanth 8th Ed, Ch. 26 (pp. 414–430)",
                "summary": (
                    "Visual revision of Ch.26 — organisation, collegium, independence, "
                    "jurisdiction nine-pack, India vs USA, and exam pack."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Supreme Court",
                "summary": (
                    "Three hats of the apex court — federal court, FR guarantor, and "
                    "final court of appeal; guardian and interpreter of the Constitution."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **three hats** mental model, then "
                    "**Footing → Composition → Collegium → Independence → Jurisdiction "
                    "nine-pack → India–USA → Articles glance**. "
                    "Drill writ/appellate/advisory clusters for Prelims sharpness. "
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
            ref="Articles 124–147 · Part V",
            excerpt=(
                "Organisation, independence, jurisdiction, powers, and procedure of "
                "the Supreme Court of India."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Laxmikanth Ch. 26",
            excerpt=(
                "Supreme Court — composition, collegium, independence, jurisdiction, "
                "India–USA comparison, articles at a glance."
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

        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Supreme Court chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
