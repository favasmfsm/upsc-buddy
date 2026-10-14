"""Seed Laxmikanth Ch.30 Governor (visual revision — Part IV State Government)."""

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

HUB_SLUG = "governor"
CHAPTER_SLUG = "governor"

ENTRY_PILLARS = [
    {
        "id": "appointment",
        "articles": "Arts 153, 155",
        "label": "Appointment",
        "slug": "gov-appointment",
        "detail": "Presidential warrant — Canadian model; independent office (Hargovind Pant).",
        "tone": "teal",
    },
    {
        "id": "quals",
        "articles": "Arts 157–159",
        "label": "Quals, oath & conditions",
        "slug": "gov-qualifications-oath",
        "detail": "Citizen + 35; CJ HC oath; Art. 158 conditions; Sarkaria selection.",
        "tone": "olive",
    },
    {
        "id": "term",
        "articles": "Arts 156, 160",
        "label": "Term & removal",
        "slug": "gov-term-removal",
        "detail": "5 years at pleasure — not justiciable (Surya Narain); no impeachment.",
        "tone": "gold",
    },
    {
        "id": "powers-map",
        "articles": "4 heads",
        "label": "Powers map",
        "slug": "gov-powers-map",
        "detail": "Executive–legislative–financial–judicial; no diplomatic/military/emergency.",
        "tone": "orange",
    },
    {
        "id": "executive",
        "articles": "Part VI",
        "label": "Executive powers",
        "slug": "gov-executive",
        "detail": "CM, AG, SEC, SPSC; Art. 167; 356 recommend; Chancellor.",
        "tone": "terracotta",
    },
    {
        "id": "leg-fin",
        "articles": "Arts 174–176",
        "label": "Legislative & financial",
        "slug": "gov-legislative-financial",
        "detail": "Legislature role, nominations, 104th; budget and money bills.",
        "tone": "maroon",
    },
    {
        "id": "veto",
        "articles": "Arts 200–201",
        "label": "Veto & reservation",
        "slug": "gov-veto",
        "detail": "Four options on ordinary bills — including reserve for President.",
        "tone": "teal",
    },
    {
        "id": "ordinance",
        "articles": "Art. 213",
        "label": "Ordinances",
        "slug": "gov-ordinance",
        "detail": "CoM advice; 3 Presidential-instruction cases; Wadhwa on repromulgation.",
        "tone": "olive",
    },
    {
        "id": "pardon",
        "articles": "Art. 161",
        "label": "Pardoning power",
        "slug": "gov-pardon",
        "detail": "State-law clemency; no death pardon; no court-martial.",
        "tone": "gold",
    },
    {
        "id": "position",
        "articles": "Arts 154, 163, 164",
        "label": "Constitutional position",
        "slug": "gov-constitutional-position",
        "detail": "Nominal head; discretion envisaged; no 42nd-style binding advice.",
        "tone": "orange",
    },
    {
        "id": "discretion",
        "articles": "Art. 163",
        "label": "Discretion map",
        "slug": "gov-discretion",
        "detail": "Constitutional vs situational vs special responsibilities.",
        "tone": "terracotta",
    },
    {
        "id": "issues",
        "articles": "Sarkaria",
        "label": "Issues & commissions",
        "slug": "gov-issues-sarkaria",
        "detail": "Eight Sarkaria friction points + Punchhi mains VA.",
        "tone": "maroon",
    },
    {
        "id": "tables",
        "articles": "Table 30.4",
        "label": "Articles glance",
        "slug": "gov-articles-tables",
        "detail": "Arts 153–167 plus legislature, assent, ordinance, judiciary.",
        "tone": "teal",
    },
    {
        "id": "exam",
        "articles": "PYQ kit",
        "label": "Exam kit",
        "slug": "gov-exam-kit",
        "detail": "Prelims traps, PYQ themes, and mains one-liners.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "gov-two-hats",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Two hats",
        "topic_label": "Governor of a State",
        "subject_label": "Arts 153–167 · Part VI",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating the Governor as the real executive",
            "Equating Governor with President (no VP; more discretion; pleasure tenure)",
            "Forgetting bill reservation and Art. 356 recommendation",
            "Assuming ministerial advice is always binding like Art. 74",
        ],
        "insight": (
            "Dual role: constitutional (nominal) head of the state and agent of the Centre — "
            "the federal hinge where aid-and-advice meets express and situational discretion."
        ),
    },
    {
        "id": "gov-entry-pillars",
        "type": "pillars",
        "title": "Fourteen revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "gov-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Path: Dual role → Appointment → Term (pleasure) → Veto / Ordinance / Pardon vs President → "
            "Art. 163 discretion → Sarkaria issues. "
            "Trap trio: nominee ≠ Central employee; no death pardon; ordinance needs CoM advice "
            "(plus 3 Presidential-instruction cases)."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Appointment of Governor",
        "slug": "gov-appointment",
        "sort_order": 1,
        "summary": (
            "Appointed by the President under Art. 155 — Canadian model, not elected; "
            "independent constitutional office (Hargovind Pant)."
        ),
        "body": (
            "## How the Governor is chosen\n\n"
            "Neither direct election nor an electoral college. The President appoints by "
            "**warrant under hand and seal** (Art. 155). In practice a Central nominee — "
            "but the office is **not** employment under the Centre.\n\n"
            "### Hargovind Pant (1979)\n"
            "Office of Governor is an **independent constitutional office** — not under the "
            "control of or subordinate to the Central government.\n\n"
            "### Why not elected? (CA logic — revise in 5)\n"
            "1. **Parliamentary incompatibility** — elected Governor clashes with a nominal head.\n"
            "2. **Conflict with CM** — dual elected centres of power.\n"
            "3. **Cost & spectacle** — elaborate election for a constitutional head is pointless.\n"
            "4. **Neutrality & unity** — party Governor fuels separatism and partisan bias.\n"
            "5. **Centre’s federal lever** — nomination keeps Union–State link.\n\n"
            "### Model choice\n"
            "US-style direct election **dropped**; **Canadian** provincial appointment by the Centre "
            "**accepted**. 7th CAA (1956): same person may be Governor of two or more states."
        ),
        "articles": [
            ("Art. 153", "Governors of States — usually one per state; 7th CAA allows multi-state."),
            ("Art. 155", "Appointment of Governor by the President by warrant under hand and seal."),
        ],
        "visual_blocks": [
            {
                "id": "gov-appt-flow",
                "type": "flowchart",
                "title": "Why appointed, not elected?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Should the state head be elected?",
                        "detail": "Constituent Assembly weighed US vs Canadian models.",
                        "options": [
                            {"label": "Direct election (US model)", "next": "reject"},
                            {"label": "Centre appoints (Canadian model)", "next": "accept"},
                        ],
                    },
                    {
                        "id": "reject",
                        "label": "Rejected",
                        "detail": "Conflicts with CM, cost, partisanship, separatist risks, leadership problem at polls.",
                    },
                    {
                        "id": "accept",
                        "label": "Accepted — Art. 155",
                        "detail": "President appoints; dual role as state head and Centre’s agent preserved.",
                    },
                ],
            },
            {
                "id": "gov-appt-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Nominee of the Centre ≠ Central government employee. "
                    "Hargovind Pant: independent constitutional office."
                ),
            },
        ],
    },
    {
        "title": "Qualifications, Oath & Conditions",
        "slug": "gov-qualifications-oath",
        "sort_order": 2,
        "summary": (
            "Only two constitutional qualifications; oath by CJ of the High Court; "
            "Art. 158 conditions, immunities, and Sarkaria selection norms."
        ),
        "body": (
            "## Qualifications (Art. 157)\n\n"
            "Only two: (1) **citizen of India**; (2) completed **35 years**.\n\n"
            "### Oath (Art. 159)\n"
            "Swears to execute the office; preserve, protect and defend the Constitution and the law; "
            "devote to the service and well-being of the people of the state. "
            "Administered by the **Chief Justice of the concerned High Court** (or seniormost judge available).\n\n"
            "### Conditions of office (Art. 158)\n"
            "1. Not a member of Parliament or state legislature (seat vacated on entering office).\n"
            "2. Not hold any other office of profit.\n"
            "3. Rent-free official residence (Raj Bhavan).\n"
            "4. Emoluments/allowances/privileges as determined by Parliament.\n"
            "5. Multi-state Governor — pay shared as President determines.\n"
            "6. Emoluments **cannot be diminished** during term.\n\n"
            "Salary raised (Finance Act 2018) from ₹1.10 lakh to **₹3.50 lakh** per month.\n\n"
            "### Immunities (Art. 361)\n"
            "Personal immunity for official acts; **no criminal proceedings** during term "
            "(even for personal acts); no arrest/imprisonment. Civil proceedings for personal acts "
            "only after **two months’ notice**.\n\n"
            "### Sarkaria on selection (revise)\n"
            "Eminent; **outsider** to the state; detached from local politics; not too active in "
            "recent politics; avoid ruling-party politician for an opposition-ruled state; "
            "**CM consultation** should be constitutionalised (amend Art. 155); informal "
            "VP/Speaker consult with PM — not a constitutional obligation."
        ),
        "articles": [
            ("Art. 157", "Qualifications — citizen of India; 35 years of age."),
            ("Art. 158", "Conditions of Governor’s office — seat, office of profit, emoluments."),
            ("Art. 159", "Oath or affirmation — by CJ of the High Court."),
            ("Art. 361", "Protection of President and Governors — immunities."),
        ],
        "visual_blocks": [
            {
                "id": "gov-quals-pillars",
                "type": "pillars",
                "title": "Office entry checklist",
                "items": [
                    {
                        "id": "q",
                        "articles": "Art. 157",
                        "label": "Qualifications",
                        "detail": "Citizen + 35 only — no other constitutional bar.",
                        "tone": "teal",
                    },
                    {
                        "id": "o",
                        "articles": "Art. 159",
                        "label": "Oath",
                        "detail": "CJ HC (or seniormost judge) administers.",
                        "tone": "olive",
                    },
                    {
                        "id": "c",
                        "articles": "Art. 158",
                        "label": "Conditions",
                        "detail": "No seat/profit; Raj Bhavan; pay protected.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "gov-sarkaria-select",
                "type": "callout",
                "tone": "tip",
                "title": "Sarkaria selection mnemonic — EOND",
                "body": (
                    "**E**minent · **O**utsider · **N**ot local-politics intimate · "
                    "**D**etached from recent politics. Plus: avoid Centre ruling-party "
                    "politician vs opposition state; consult CM (preferably via Art. 155)."
                ),
            },
        ],
    },
    {
        "title": "Term & Removal",
        "slug": "gov-term-removal",
        "sort_order": 3,
        "summary": (
            "Five-year term at the pleasure of the President — not justiciable; "
            "transfer/reappointment allowed; Art. 160 contingencies."
        ),
        "body": (
            "## Term (Art. 156)\n\n"
            "Holds office for **five years** from the date of entering office — but subject to the "
            "**pleasure of the President**. May resign anytime by writing to the President.\n\n"
            "### Surya Narain (1981)\n"
            "Pleasure of the President is **not justiciable**. No security of tenure; no fixed term "
            "in practice. Constitution lays down **no grounds** for removal.\n\n"
            "### Continuity rules\n"
            "- May be **transferred** to another state for the rest of the term.\n"
            "- May be **reappointed** to the same or another state after term ends.\n"
            "- Continues until successor assumes charge — **no interregnum**.\n\n"
            "### Contingencies (Art. 160)\n"
            "President may make provision for discharge of functions in contingencies not provided "
            "for (e.g. death). Chief Justice of the High Court may be appointed temporarily.\n\n"
            "There is **no impeachment** procedure for the Governor."
        ),
        "articles": [
            ("Art. 156", "Term of office — five years subject to President’s pleasure; resignation."),
            ("Art. 160", "Discharge of functions of the Governor in certain contingencies."),
        ],
        "visual_blocks": [
            {
                "id": "gov-term-timeline",
                "type": "timeline",
                "title": "Pleasure in practice (exam colour)",
                "events": [
                    {
                        "id": "e1",
                        "year": 1981,
                        "label": "Surya Narain",
                        "detail": "SC: President’s pleasure not justiciable.",
                    },
                    {
                        "id": "e2",
                        "year": 1989,
                        "label": "V.P. Singh govt",
                        "detail": "Asked Congress-appointed Governors to resign; mixed outcomes.",
                    },
                    {
                        "id": "e3",
                        "year": 1991,
                        "label": "Narasimha Rao",
                        "detail": "Changed fourteen Governors appointed by prior non-Congress govts.",
                    },
                ],
            },
            {
                "id": "gov-term-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Governor ≠ President on removal. No Art. 61-style impeachment. "
                    "Pleasure is political and non-justiciable (Surya Narain)."
                ),
            },
        ],
    },
    {
        "title": "Powers Map",
        "slug": "gov-powers-map",
        "sort_order": 4,
        "summary": (
            "Four heads like the President — executive, legislative, financial, judicial — "
            "but no diplomatic, military, or emergency powers."
        ),
        "body": (
            "## Four heads of power\n\n"
            "Governor’s powers are **more or less analogous** to the President’s under four heads:\n\n"
            "1. **Executive**\n"
            "2. **Legislative**\n"
            "3. **Financial**\n"
            "4. **Judicial**\n\n"
            "### What the Governor lacks\n"
            "Unlike the President, the Governor has **no diplomatic, military, or emergency powers**.\n\n"
            "Drill next into the three comparison hotspots: **veto (Arts 200–201)**, "
            "**ordinance (Art. 213)**, and **pardon (Art. 161)**."
        ),
        "articles": [
            ("Art. 154", "Executive power of the State vested in the Governor."),
            ("Art. 161", "Power of the Governor to grant pardons, etc."),
            ("Art. 200", "Assent to Bills."),
            ("Art. 213", "Power of Governor to promulgate Ordinances."),
        ],
        "visual_blocks": [
            {
                "id": "gov-powers-pillars",
                "type": "pillars",
                "title": "Four heads — then three drills",
                "items": [
                    {
                        "id": "ex",
                        "articles": "Exec",
                        "label": "Executive",
                        "slug": "gov-executive",
                        "detail": "Appointments, info, 356 recommend, Chancellor.",
                        "tone": "teal",
                    },
                    {
                        "id": "leg",
                        "articles": "Leg + Fin",
                        "label": "Legislative & financial",
                        "slug": "gov-legislative-financial",
                        "detail": "Legislature role, budget, money bills.",
                        "tone": "olive",
                    },
                    {
                        "id": "veto",
                        "articles": "200–201",
                        "label": "Veto drill",
                        "slug": "gov-veto",
                        "detail": "Assent / withhold / return / reserve.",
                        "tone": "gold",
                    },
                    {
                        "id": "ord",
                        "articles": "213",
                        "label": "Ordinance drill",
                        "slug": "gov-ordinance",
                        "detail": "Recess law-making + Wadhwa.",
                        "tone": "orange",
                    },
                    {
                        "id": "par",
                        "articles": "161",
                        "label": "Pardon drill",
                        "slug": "gov-pardon",
                        "detail": "State-law clemency vs President.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "gov-powers-missing",
                "type": "callout",
                "tone": "trap",
                "title": "Missing powers",
                "body": (
                    "No diplomatic, military, or emergency powers — classic prelims discriminator "
                    "vs the President."
                ),
            },
        ],
    },
    {
        "title": "Executive Powers",
        "slug": "gov-executive",
        "sort_order": 5,
        "summary": (
            "Formal executive head — CM and ministers, AG, SEC, SPSC, Art. 167 duties, "
            "356 recommendation, and Chancellor role."
        ),
        "body": (
            "## Executive snapshot\n\n"
            "1. All executive actions of the state are formally taken **in the Governor’s name**.\n"
            "2. Rules for authentication of orders in that name.\n"
            "3. Rules for convenient transaction of government business and allocation among ministers.\n"
            "4. Appoints **CM and other ministers** — they hold office during Governor’s pleasure. "
            "Tribal Welfare Minister in **Chhattisgarh, Jharkhand, Madhya Pradesh, Odisha**. "
            "**Bihar excluded** by the **94th CAA (2006)**.\n"
            "5. Appoints **Advocate General**; holds office during pleasure; fixes remuneration.\n"
            "6. Appoints **State Election Commissioner**; conditions/tenure fixed by Governor — but "
            "SEC removable **only like a High Court judge**.\n"
            "7. Appoints Chair and members of **SPSC** — but they can be removed **only by the President**.\n"
            "8. May seek any information on administration/legislation from the CM (Art. 167).\n"
            "9. May require CM to submit a minister’s decision to the Council of Ministers.\n"
            "10. May **recommend President’s Rule** (Art. 356); during it, acts as President’s agent "
            "with extensive executive powers.\n"
            "11. **Chancellor** of state universities; appoints Vice-Chancellors."
        ),
        "articles": [
            ("Art. 154", "Executive power of the State vested in the Governor."),
            ("Art. 164", "Other provisions as to Ministers — appointment, pleasure, Tribal Welfare."),
            ("Art. 165", "Advocate-General for the State."),
            ("Art. 166", "Conduct of business of the Government of a State."),
            ("Art. 167", "Duties of Chief Minister as respects the furnishing of information to Governor."),
        ],
        "visual_blocks": [
            {
                "id": "gov-sec-spsc",
                "type": "comparison",
                "title": "SEC vs SPSC — who removes?",
                "columns": [
                    {
                        "id": "sec",
                        "heading": "State Election Commissioner",
                        "points": [
                            "Appointed by Governor",
                            "Conditions/tenure fixed by Governor",
                            "Removed only like a High Court judge",
                        ],
                    },
                    {
                        "id": "spsc",
                        "heading": "SPSC Chair & members",
                        "points": [
                            "Appointed by Governor",
                            "Removed only by the President",
                            "Governor cannot remove them",
                        ],
                    },
                ],
            },
            {
                "id": "gov-exec-trap",
                "type": "callout",
                "tone": "trap",
                "title": "94th Amendment trap",
                "body": (
                    "Tribal Welfare Minister: CG, JH, MP, OD — **not Bihar** after the 94th CAA (2006)."
                ),
            },
        ],
    },
    {
        "title": "Legislative & Financial Powers",
        "slug": "gov-legislative-financial",
        "sort_order": 6,
        "summary": (
            "Integral part of the state legislature — sessions, nominations, disqualification; "
            "budget, money bills, Contingency Fund, and State Finance Commission."
        ),
        "body": (
            "## Legislative powers\n\n"
            "Governor is an **integral part** of the state legislature.\n\n"
            "1. Summon / prorogue Houses; **dissolve** the Legislative Assembly.\n"
            "2. Address at the first session after each general election and the first session each year.\n"
            "3. Send messages on pending bills or otherwise.\n"
            "4. Appoint a member to preside if Speaker & Deputy Speaker (or Chairman & Deputy) both vacant.\n"
            "5. Nominate **one-sixth** of the Legislative Council — literature, science, art, "
            "cooperative movement, social service.\n"
            "6. Anglo-Indian MLA nomination **discontinued** by the **104th CAA (2019)** "
            "(earlier: one member).\n"
            "7. Decides disqualification of legislators **in consultation with the Election Commission**.\n"
            "8. Assent / withhold / return / reserve bills (see veto cluster).\n"
            "9. Promulgate ordinances (see ordinance cluster).\n"
            "10. Lays reports of State Finance Commission, SPSC, and CAG (state accounts) before the legislature.\n\n"
            "## Financial powers\n\n"
            "1. Ensures Annual Financial Statement (state budget) is laid before the legislature.\n"
            "2. **Money bills** need prior recommendation.\n"
            "3. No demand for a grant except on recommendation.\n"
            "4. Advances from the **Contingency Fund** of the state.\n"
            "5. Constitutes a **Finance Commission** every five years to review finances of "
            "panchayats and municipalities."
        ),
        "articles": [
            ("Art. 174", "Sessions of the State Legislature, prorogation and dissolution."),
            ("Art. 175", "Right of Governor to address and send messages to the House or Houses."),
            ("Art. 176", "Special address by the Governor."),
            ("Art. 192", "Decision on questions as to disqualification — consult Election Commission."),
        ],
        "visual_blocks": [
            {
                "id": "gov-leg-checklist",
                "type": "memory_palace",
                "title": "Legislature desk memory palace",
                "setting": "Raj Bhavan desk facing the Assembly",
                "loci": [
                    {
                        "id": "l1",
                        "place": "Calendar on the wall",
                        "association": "Summon / prorogue / dissolve",
                        "detail": "Art. 174 — sessions control.",
                    },
                    {
                        "id": "l2",
                        "place": "Microphone",
                        "association": "Address & messages",
                        "detail": "Arts 175–176 — first session after polls and each year.",
                    },
                    {
                        "id": "l3",
                        "place": "Nomination tray marked 1/6",
                        "association": "Council nominations",
                        "detail": "Lit / science / art / coop / social service.",
                    },
                    {
                        "id": "l4",
                        "place": "Blank Anglo-Indian nameplate",
                        "association": "104th CAA",
                        "detail": "Anglo-Indian MLA nomination ended (from 2020).",
                    },
                ],
            },
            {
                "id": "gov-104-note",
                "type": "callout",
                "tone": "note",
                "title": "104th Amendment",
                "body": (
                    "Anglo-Indian nomination to State Assemblies discontinued — same wave that "
                    "ended Lok Sabha Anglo-Indian nominations."
                ),
            },
        ],
    },
    {
        "title": "Veto Power & Reservation",
        "slug": "gov-veto",
        "sort_order": 7,
        "summary": (
            "Arts 200–201 — ordinary bill has four options including reservation; "
            "money bill cannot be returned; President’s role after reservation."
        ),
        "body": (
            "## Ordinary bills (Art. 200)\n\n"
            "After passage, Governor may:\n"
            "1. **Give assent** → bill becomes Act.\n"
            "2. **Withhold assent** → bill ends.\n"
            "3. **Return** (if not a money bill) for reconsideration — if passed again, "
            "must assent (**suspensive veto** only).\n"
            "4. **Reserve** for the President’s consideration.\n\n"
            "### When reservation is obligatory / usual\n"
            "**Obligatory** if the bill endangers the position of the State High Court. "
            "Illustrative grounds (Soli Sorabjee): ultra vires; opposed to DPSP; against larger "
            "national interest; of grave national importance; compulsory acquisition under Art. 31A.\n\n"
            "### After reservation\n"
            "Governor has **no further role**. If President returns and Houses pass again, "
            "bill goes again only for **Presidential** assent — Governor’s assent not needed. "
            "President may still withhold assent even after reconsideration (unlike Union "
            "suspensive veto on Parliament bills).\n\n"
            "## Money bills\n\n"
            "Governor: assent / withhold / **reserve** — **cannot return** for reconsideration. "
            "Normally assents (introduced with prior recommendation)."
        ),
        "articles": [
            ("Art. 200", "Assent to Bills — assent, withhold, return, or reserve for President."),
            ("Art. 201", "Bills reserved for consideration of the President."),
        ],
        "visual_blocks": [
            {
                "id": "gov-veto-compare",
                "type": "comparison",
                "title": "Ordinary bills — President vs Governor",
                "columns": [
                    {
                        "id": "pres",
                        "heading": "President (Parliament bill)",
                        "points": [
                            "Assent / withhold / return (suspensive)",
                            "No ‘reserve for higher authority’",
                            "After return + re-pass → must assent",
                        ],
                    },
                    {
                        "id": "gov",
                        "heading": "Governor (state bill)",
                        "points": [
                            "Assent / withhold / return / reserve",
                            "Fourth option is the federal lever",
                            "After reserve → exits the process",
                        ],
                    },
                ],
            },
            {
                "id": "gov-veto-flow",
                "type": "flowchart",
                "title": "Bill reaches the Governor",
                "root": "bill",
                "steps": [
                    {
                        "id": "bill",
                        "label": "What kind of bill?",
                        "options": [
                            {"label": "Ordinary bill", "next": "ord"},
                            {"label": "Money bill", "next": "money"},
                        ],
                    },
                    {
                        "id": "ord",
                        "label": "4 options",
                        "detail": "Assent · Withhold · Return (suspensive) · Reserve for President.",
                    },
                    {
                        "id": "money",
                        "label": "3 options",
                        "detail": "Assent · Withhold · Reserve — cannot return.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Ordinance-Making Power",
        "slug": "gov-ordinance",
        "sort_order": 8,
        "summary": (
            "Art. 213 — recess legislation on CoM advice; three cases needing Presidential "
            "instructions; Wadhwa bars ordinance republics."
        ),
        "body": (
            "## Article 213 essentials\n\n"
            "- Promulgate when the Assembly (unicameral) or both Houses / either House "
            "(bicameral) is **not in session**.\n"
            "- Satisfaction that immediate action is necessary.\n"
            "- Co-extensive with the state legislature’s legislative power.\n"
            "- Same force and limitations as an Act; may be withdrawn anytime.\n"
            "- **Not discretionary** — only on advice of CoM headed by CM.\n"
            "- Laid before the House(s) on reassembly; ceases after **six weeks** from "
            "reassembly (or earlier if disapproved).\n\n"
            "### Three cases — need President’s instructions\n"
            "1. Same provisions would need **previous Presidential sanction** for introduction.\n"
            "2. Governor would have **reserved** a bill with the same provisions.\n"
            "3. A state Act with the same provisions would be **invalid without President’s assent**.\n\n"
            "### D.C. Wadhwa (1986)\n"
            "Bihar: 256 ordinances (1967–81) kept alive 1–14 years by repromulgation. "
            "SC: successive repromulgation with the same text without attempting Assembly "
            "passage **violates the Constitution** — ordinance power is exceptional, not a "
            "substitute for the legislature."
        ),
        "articles": [
            ("Art. 213", "Power of Governor to promulgate Ordinances during recess of Legislature."),
        ],
        "visual_blocks": [
            {
                "id": "gov-ord-compare",
                "type": "comparison",
                "title": "Ordinance — key deltas vs President",
                "columns": [
                    {
                        "id": "pres",
                        "heading": "President (Art. 123)",
                        "points": [
                            "No instruction from a higher authority",
                            "Advice of Union CoM",
                            "Both Houses / either House not in session",
                        ],
                    },
                    {
                        "id": "gov",
                        "heading": "Governor (Art. 213)",
                        "points": [
                            "3 cases need President’s instructions",
                            "Advice of state CoM",
                            "Same session logic for uni/bicameral Houses",
                        ],
                    },
                ],
            },
            {
                "id": "gov-ord-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Trap + Wadhwa",
                "body": (
                    "Ordinance ≠ discretionary. Memorise the **3 Presidential-instruction** cases. "
                    "Wadhwa: no ‘ordinance republic’ via endless repromulgation."
                ),
            },
        ],
    },
    {
        "title": "Pardoning Power",
        "slug": "gov-pardon",
        "sort_order": 9,
        "summary": (
            "Art. 161 — clemency for state-law offences; cannot pardon death or court-martial "
            "sentences."
        ),
        "body": (
            "## Article 161\n\n"
            "Governor may grant **pardons, reprieves, respites and remissions**, or "
            "**suspend, remit and commute** the sentence of any person convicted of an offence "
            "against a law relating to a matter to which the **executive power of the State** extends.\n\n"
            "### Vs President (must-know)\n"
            "1. President: Central-law offences · Governor: **state-law** offences.\n"
            "2. President alone may **pardon a death sentence**. Governor **cannot pardon death** — "
            "but may **suspend, remit or commute** a death sentence.\n"
            "3. President may act on **court-martial** sentences; Governor has **no** such power."
        ),
        "articles": [
            ("Art. 161", "Power of the Governor to grant pardons, etc., and to suspend, remit or commute sentences."),
            ("Art. 72", "Corresponding Presidential power — death pardon and court-martial."),
        ],
        "visual_blocks": [
            {
                "id": "gov-pardon-compare",
                "type": "comparison",
                "title": "Pardon — President vs Governor",
                "columns": [
                    {
                        "id": "pres",
                        "heading": "President (Art. 72)",
                        "points": [
                            "Central-law offences",
                            "Can pardon death sentence",
                            "Can act on court-martial sentences",
                        ],
                    },
                    {
                        "id": "gov",
                        "heading": "Governor (Art. 161)",
                        "points": [
                            "State-law offences",
                            "Cannot pardon death (may suspend/remit/commute)",
                            "No court-martial power",
                        ],
                    },
                ],
            },
            {
                "id": "gov-pardon-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic",
                "body": "Death pardon = President only. Governor: suspend / remit / commute — not pardon.",
            },
        ],
    },
    {
        "title": "Constitutional Position",
        "slug": "gov-constitutional-position",
        "sort_order": 10,
        "summary": (
            "Nominal executive with CoM aid and advice — except discretion; "
            "two structural differences from the President."
        ),
        "body": (
            "## Parliamentary system in the states\n\n"
            "Governor is the **nominal** executive; real executive is the **Council of Ministers "
            "headed by the CM** — except where required to act in **discretion**.\n\n"
            "### Triad to memorise\n"
            "- **Art. 154** — executive power of the State vested in the Governor.\n"
            "- **Art. 163** — CoM to aid and advise, except discretionary functions.\n"
            "- **Art. 164** — CoM collectively responsible to the Legislative Assembly "
            "(foundation of parliamentary government in the state).\n\n"
            "### Two differences vs President\n"
            "1. Constitution **envisages discretion** for the Governor — no parallel for the President.\n"
            "2. **42nd CAA** made ministerial advice binding on the President — **no such provision** "
            "for the Governor.\n\n"
            "Dual role in the federal system: **constitutional head of the state** and "
            "**representative of the Centre**."
        ),
        "articles": [
            ("Art. 154", "Executive power of the State."),
            ("Art. 163", "Council of Ministers to aid and advise the Governor — except discretion."),
            ("Art. 164", "Other provisions as to Ministers — collective responsibility to the Assembly."),
        ],
        "visual_blocks": [
            {
                "id": "gov-pos-compare",
                "type": "comparison",
                "title": "Governor vs President — position",
                "columns": [
                    {
                        "id": "pres",
                        "heading": "President",
                        "points": [
                            "No express constitutional discretion clause like Art. 163",
                            "42nd: advice binding; 44th: return once then bind",
                            "Union executive apex (Part V)",
                        ],
                    },
                    {
                        "id": "gov",
                        "heading": "Governor",
                        "points": [
                            "Art. 163 expressly contemplates discretion",
                            "No 42nd-style binding-advice clause",
                            "Dual role: state head + Centre’s agent",
                        ],
                    },
                ],
            },
            {
                "id": "gov-pos-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision anchor",
                "body": (
                    "154 (vesting) + 163 (advice/discretion) + 164 (collective responsibility) = "
                    "constitutional position in one line."
                ),
            },
        ],
    },
    {
        "title": "Discretionary Powers",
        "slug": "gov-discretion",
        "sort_order": 11,
        "summary": (
            "Constitutional discretion, situational discretion, and special responsibilities — "
            "Governor’s call on whether a matter is discretionary is final."
        ),
        "body": (
            "## Who decides if it is discretion?\n\n"
            "If any question arises whether a matter falls within the Governor’s discretion, "
            "the **Governor’s decision is final** — validity cannot be questioned on the ground "
            "that he/she ought or ought not to have acted in discretion.\n\n"
            "### Constitutional discretion (express)\n"
            "1. **Reservation** of a bill for the President.\n"
            "2. Recommendation for **President’s Rule**.\n"
            "3. Functions as administrator of an adjoining **UT** (additional charge).\n"
            "4. Determining royalty share payable to an autonomous Tribal District Council "
            "(Sixth Schedule — Assam, Meghalaya, Tripura, Mizoram).\n\n"
            "### Situational discretion (political exigency)\n"
            "1. Appoint CM when no clear majority / no obvious successor after CM’s death.\n"
            "2. Dismiss CoM that cannot prove confidence of the Assembly.\n"
            "3. Dissolve the Assembly if CoM has lost majority.\n\n"
            "### Special responsibilities (consult CoM; act finally in discretion)\n"
            "1. **Maharashtra** — Vidarbha & Marathwada boards.\n"
            "2. **Gujarat** — Saurashtra & Kutch boards.\n"
            "3. **Nagaland** — law and order (Naga Hills–Tuensang Area).\n"
            "4. **Assam** — tribal areas administration.\n"
            "5. **Manipur** — hill areas.\n"
            "6. **Sikkim** — peace; social/economic advancement of sections.\n"
            "7. **Arunachal Pradesh** — law and order.\n"
            "8. **Karnataka** — Hyderabad-Karnataka development board (**98th CAA, 2012**)."
        ),
        "articles": [
            ("Art. 163", "Aid and advice — except functions required to be exercised in discretion."),
            (
                "Sixth Schedule ¶9(2)",
                "Governor determines disputed royalty share for district councils — decision final.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "gov-disc-flow",
                "type": "flowchart",
                "title": "Which kind of discretion?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Is the power written in the Constitution / Schedule?",
                        "options": [
                            {"label": "Yes — express text", "next": "const"},
                            {"label": "No — political vacuum", "next": "sit"},
                            {"label": "Special responsibility state", "next": "spec"},
                        ],
                    },
                    {
                        "id": "const",
                        "label": "Constitutional discretion",
                        "detail": "Reserve bill · 356 recommend · UT admin · Sixth Schedule royalty.",
                    },
                    {
                        "id": "sit",
                        "label": "Situational discretion",
                        "detail": "Hung House CM · dismiss failed CoM · dissolve after majority loss.",
                    },
                    {
                        "id": "spec",
                        "label": "Special responsibilities",
                        "detail": "Consult CoM but decide finally — MH GJ NL AS MN SK AR KA.",
                    },
                ],
            },
            {
                "id": "gov-disc-states",
                "type": "callout",
                "tone": "tip",
                "title": "Special-responsibility mnemonic",
                "body": (
                    "**M**H **G**J **N**L **A**S **M**N **S**K **A**R **K**A — "
                    "“My Grand Nan Asks Many Silly ARKA questions.” "
                    "KA board via 98th CAA."
                ),
            },
        ],
    },
    {
        "title": "Issues & Commission Recommendations",
        "slug": "gov-issues-sarkaria",
        "sort_order": 12,
        "summary": (
            "Eight Sarkaria friction points in Governor functioning, plus a short Punchhi "
            "mains value-add beyond Ch.30 pages."
        ),
        "body": (
            "## Sarkaria Commission — eight issues (still live)\n\n"
            "1. **Choosing CM** — hung House: invite the leader who appears to have largest "
            "support; leave confidence to the Assembly.\n"
            "2. **Testing majority** — lists of supporters vs physical headcount; prefer floor test.\n"
            "3. **Dismissal of CM** — no uniform criteria historically; CM who lost majority "
            "should resign or face the House.\n"
            "4. **Dissolving the Assembly** — advice of majority CM normally binds; after "
            "majority loss, practice has been inconsistent.\n"
            "5. **Recommending President’s Rule** — often without exhausting alternatives; "
            "partisan criticism common.\n"
            "6. **Reserving bills** — controversial use of Art. 200 reservation.\n"
            "7. **LC nominations** — criticism that Governor has **no discretion** here "
            "(should follow CoM advice).\n"
            "8. **Chancellor role** — powers under university statutes; debate whether CoM "
            "advice still binds.\n\n"
            "### Appointment norms (recap)\n"
            "See qualifications cluster: EOND outsider norms; avoid ruling-party politician vs "
            "opposition state; constitutionalise CM consultation.\n\n"
            "### Punchhi Commission — mains VA (beyond Ch.30 pages)\n"
            "Useful exam add-ons commonly paired with Sarkaria:\n"
            "- Clearer norms on **appointment and fixed tenure / removal process**.\n"
            "- Meaningful **consultation with CM** before appointment.\n"
            "- Prefer **floor test** over Raj Bhavan arithmetic.\n"
            "- **Restrain Art. 356**; exhaust constitutional alternatives first.\n"
            "- Time-bound decisions on reserved bills (exam-friendly VA)."
        ),
        "articles": [
            ("Art. 163", "Discretion hinge — source of many Centre–State flashpoints."),
            ("Art. 200", "Reservation of bills — a recurring Sarkaria issue."),
            ("Art. 356", "President’s Rule recommendations by Governors."),
        ],
        "visual_blocks": [
            {
                "id": "gov-sarkaria-pillars",
                "type": "pillars",
                "title": "Eight Sarkaria friction points",
                "items": [
                    {
                        "id": "cm",
                        "articles": "CM",
                        "label": "Choosing CM",
                        "detail": "Largest likely support → floor decides.",
                        "tone": "teal",
                    },
                    {
                        "id": "maj",
                        "articles": "Test",
                        "label": "Testing majority",
                        "detail": "Floor test > headcount lists.",
                        "tone": "olive",
                    },
                    {
                        "id": "dis",
                        "articles": "Dismiss",
                        "label": "Dismissing CM",
                        "detail": "Lost majority → resign or face House.",
                        "tone": "gold",
                    },
                    {
                        "id": "diss",
                        "articles": "Dissolve",
                        "label": "Dissolution",
                        "detail": "Majority CM advice usually binds.",
                        "tone": "orange",
                    },
                    {
                        "id": "pr",
                        "articles": "356",
                        "label": "President’s Rule",
                        "detail": "Exhaust alternatives first.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "bill",
                        "articles": "200",
                        "label": "Reserving bills",
                        "detail": "Federal lever — often contested.",
                        "tone": "maroon",
                    },
                    {
                        "id": "lc",
                        "articles": "LC",
                        "label": "LC nominations",
                        "detail": "No real discretion — follow CoM.",
                        "tone": "teal",
                    },
                    {
                        "id": "ch",
                        "articles": "Chancellor",
                        "label": "Chancellor role",
                        "detail": "Statute powers vs CoM advice debate.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "gov-floor-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision box",
                "body": (
                    "Floor test > counting heads. Punchhi VA: tenure clarity, CM consultation, "
                    "356 restraint, time-bound reserved bills."
                ),
            },
        ],
    },
    {
        "title": "Articles at a Glance",
        "slug": "gov-articles-tables",
        "sort_order": 13,
        "summary": (
            "Table 30.4 style map — Arts 153–167 plus legislature, assent, ordinance, "
            "and judicial appointment articles."
        ),
        "body": (
            "## Office & executive\n\n"
            "- **153** Governors of States\n"
            "- **154** Executive power of State\n"
            "- **155** Appointment\n"
            "- **156** Term of office\n"
            "- **157** Qualifications\n"
            "- **158** Conditions of office\n"
            "- **159** Oath or affirmation\n"
            "- **160** Contingency discharge of functions\n"
            "- **161** Pardons etc.\n"
            "- **162** Extent of executive power of State\n"
            "- **163** CoM aid and advice / discretion\n"
            "- **164** Ministers\n"
            "- **165** Advocate-General\n"
            "- **166** Conduct of business\n"
            "- **167** CM’s duties to furnish information\n\n"
            "## Legislature, assent, ordinance, judiciary\n\n"
            "- **174–176** Sessions, messages, special address\n"
            "- **200** Assent to Bills\n"
            "- **201** Bills reserved for President\n"
            "- **213** Ordinances\n"
            "- **217** Consultation in HC judge appointments\n"
            "- **233** District judges\n"
            "- **234** Other judicial service appointments"
        ),
        "articles": [
            ("Arts 153–167", "State executive cluster — Governor at the core."),
            ("Arts 200–201, 213", "Assent, reservation, ordinances."),
            ("Arts 217, 233–234", "High Court consultation and subordinate judiciary."),
        ],
        "visual_blocks": [
            {
                "id": "gov-art-tree",
                "type": "tree",
                "title": "Governor articles by theme",
                "root": {
                    "id": "gov",
                    "label": "Governor",
                    "children": [
                        {
                            "id": "office",
                            "label": "Office",
                            "detail": "153–160",
                            "children": [
                                {"id": "a155", "label": "155 Appointment"},
                                {"id": "a156", "label": "156 Term"},
                                {"id": "a157", "label": "157 Quals"},
                            ],
                        },
                        {
                            "id": "exec",
                            "label": "Executive frame",
                            "detail": "154, 161–167",
                            "children": [
                                {"id": "a163", "label": "163 Discretion"},
                                {"id": "a161", "label": "161 Pardon"},
                            ],
                        },
                        {
                            "id": "leg",
                            "label": "Legislature link",
                            "detail": "174–176, 200–201, 213",
                            "children": [
                                {"id": "a200", "label": "200 Assent"},
                                {"id": "a213", "label": "213 Ordinance"},
                            ],
                        },
                        {
                            "id": "jud",
                            "label": "Judiciary link",
                            "detail": "217, 233–234",
                        },
                    ],
                },
            },
            {
                "id": "gov-art-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Quick scan",
                "body": (
                    "Hot triad for prelims: **163** (discretion) · **200/201** (veto/reserve) · "
                    "**213** (ordinance + 3 instruction cases)."
                ),
            },
        ],
    },
    {
        "title": "Exam Kit",
        "slug": "gov-exam-kit",
        "sort_order": 14,
        "summary": (
            "Prelims traps, PYQ themes, and mains one-liners for last-minute Governor revision."
        ),
        "body": (
            "## Prelims traps\n\n"
            "- Pleasure of President **not justiciable** (Surya Narain) — no impeachment.\n"
            "- **No Vice-Governor** analogue to Vice-President.\n"
            "- Nominee of Centre ≠ Central employee (Hargovind Pant).\n"
            "- **Cannot pardon death**; no court-martial clemency.\n"
            "- Ordinance on **CoM advice**; 3 cases need President’s instructions.\n"
            "- SPSC removed by **President**; SEC like **HC judge**.\n"
            "- Tribal Welfare Minister: CG/JH/MP/OD — **not Bihar (94th)**.\n"
            "- Anglo-Indian MLA nomination ended (**104th**).\n"
            "- Multi-state Governor via **7th CAA**.\n"
            "- Ordinary bill: **four** options; money bill: **three** (no return).\n\n"
            "## PYQ themes\n\n"
            "Appointment vs election · discretion vs aid-and-advice · veto/reservation · "
            "ordinance limits / Wadhwa · pardon vs President · dual role / federal friction · "
            "Sarkaria on CM choice and 356.\n\n"
            "## Mains one-liners\n\n"
            "- Dual role: constitutional head **and** Centre’s agent — federal hinge.\n"
            "- Art. 163 is where parliamentary form meets Union leverage.\n"
            "- Sarkaria: largest-support invitation + floor test; restrain partisan 356.\n"
            "- Wadhwa: ordinance is exceptional — not a parallel legislature."
        ),
        "articles": [
            ("Arts 155–163", "Appointment, term, and discretion — highest prelims density."),
            ("Arts 200–213", "Veto and ordinance — comparison with President."),
            ("Art. 161", "Pardon discriminators vs Art. 72."),
        ],
        "visual_blocks": [
            {
                "id": "gov-pyq-heat",
                "type": "pyq_heatmap",
                "title": "PYQ focus map",
                "items": [
                    {"concept_slug": "gov-appointment", "label": "Appointment"},
                    {"concept_slug": "gov-term-removal", "label": "Pleasure / tenure"},
                    {"concept_slug": "gov-veto", "label": "Veto / reserve"},
                    {"concept_slug": "gov-ordinance", "label": "Ordinance"},
                    {"concept_slug": "gov-pardon", "label": "Pardon"},
                    {"concept_slug": "gov-discretion", "label": "Discretion"},
                    {"concept_slug": "gov-issues-sarkaria", "label": "Sarkaria / 356"},
                ],
            },
            {
                "id": "gov-exam-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Last-minute trap trio",
                "body": (
                    "1) Pleasure ≠ impeachment. 2) Death pardon = President only. "
                    "3) Ordinance advice + 3 Presidential-instruction cases."
                ),
            },
            {
                "id": "gov-exam-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "Governor wears two hats — state constitutional head and Centre’s agent; "
                    "Art. 163 is the hinge where federal friction concentrates."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "gov-appointment"),
    (HUB_SLUG, "parent", "gov-qualifications-oath"),
    (HUB_SLUG, "parent", "gov-term-removal"),
    (HUB_SLUG, "parent", "gov-powers-map"),
    (HUB_SLUG, "parent", "gov-executive"),
    (HUB_SLUG, "parent", "gov-legislative-financial"),
    (HUB_SLUG, "parent", "gov-veto"),
    (HUB_SLUG, "parent", "gov-ordinance"),
    (HUB_SLUG, "parent", "gov-pardon"),
    (HUB_SLUG, "parent", "gov-constitutional-position"),
    (HUB_SLUG, "parent", "gov-discretion"),
    (HUB_SLUG, "parent", "gov-issues-sarkaria"),
    (HUB_SLUG, "parent", "gov-articles-tables"),
    (HUB_SLUG, "parent", "gov-exam-kit"),
    ("gov-appointment", "related", "gov-qualifications-oath"),
    ("gov-qualifications-oath", "related", "gov-term-removal"),
    ("gov-powers-map", "related", "gov-executive"),
    ("gov-powers-map", "related", "gov-legislative-financial"),
    ("gov-powers-map", "related", "gov-veto"),
    ("gov-powers-map", "related", "gov-ordinance"),
    ("gov-powers-map", "related", "gov-pardon"),
    ("gov-veto", "related", "gov-ordinance"),
    ("gov-constitutional-position", "related", "gov-discretion"),
    ("gov-discretion", "related", "gov-issues-sarkaria"),
    ("gov-constitutional-position", "related", "parliamentary-system"),
    ("gov-constitutional-position", "related", "president"),
    ("gov-pardon", "related", "president"),
    ("gov-veto", "related", "president"),
    ("gov-ordinance", "related", "president"),
    ("gov-issues-sarkaria", "related", "emergency-provisions"),
    ("gov-discretion", "related", "federal-system"),
    ("gov-exam-kit", "related", "gov-appointment"),
    ("gov-exam-kit", "related", "gov-veto"),
    ("gov-exam-kit", "related", "gov-discretion"),
]

SAMPLE_PYQS = [
    (
        2019,
        "The Governor of a State is appointed by the President. Which statement is correct?",
        "Appointed by warrant under Art. 155; office is an independent constitutional office "
        "(Hargovind Pant), not employment under the Central government.",
        ["gov-appointment", HUB_SLUG],
    ),
    (
        2014,
        "Which of the following is/are discretionary powers of the Governor?",
        "Constitutional discretion includes reserving a bill for the President and recommending "
        "President’s Rule; situational discretion includes appointing a CM in a hung Assembly.",
        ["gov-discretion", HUB_SLUG],
    ),
    (
        2013,
        "Consider the ordinance-making power of the Governor under Article 213.",
        "Not a discretionary power — exercised on CoM advice; in three specified cases, "
        "President’s instructions are required; Wadhwa bars successive repromulgation.",
        ["gov-ordinance", HUB_SLUG],
    ),
    (
        2012,
        "Difference between the pardoning powers of the President and the Governor includes:",
        "Governor cannot pardon a death sentence or court-martial sentence; may suspend, remit "
        "or commute a death sentence; covers state-law offences.",
        ["gov-pardon", HUB_SLUG],
    ),
    (
        2018,
        "When a bill is reserved by the Governor for the consideration of the President:",
        "Governor has no further role; if returned and passed again, it is presented again only "
        "for Presidential assent — Governor’s assent is no longer required.",
        ["gov-veto", HUB_SLUG],
    ),
    (
        2016,
        "With reference to the term of the Governor, which statement is correct?",
        "Five-year term is subject to the pleasure of the President; pleasure is not justiciable "
        "(Surya Narain); Constitution specifies no removal grounds.",
        ["gov-term-removal", HUB_SLUG],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Hargovind Pant v. Raghukul Tilak",
        "slug": "hargovind-pant-governor",
        "parties": "Hargovind Pant v. Raghukul Tilak",
        "year": 1979,
        "court": CaseLaw.Court.SC,
        "summary": "Nature of the office of Governor vis-à-vis the Central government.",
        "holding": (
            "Office of Governor is an independent constitutional office — not an employment "
            "under the Central government and not subordinate to it."
        ),
        "concept_slugs": ["gov-appointment", HUB_SLUG],
    },
    {
        "title": "Surya Narain v. Union of India",
        "slug": "surya-narain-governor",
        "parties": "Surya Narain v. Union of India",
        "year": 1981,
        "court": CaseLaw.Court.SC,
        "summary": "Justiciability of the President’s pleasure regarding the Governor’s tenure.",
        "holding": (
            "Pleasure of the President under Art. 156 is not justiciable; Governor has no "
            "security of tenure or fixed term enforceable in court."
        ),
        "concept_slugs": ["gov-term-removal", HUB_SLUG],
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
        "concept_slugs": ["gov-ordinance", HUB_SLUG],
    },
]

AMENDMENTS = [
    {
        "number": 7,
        "year": 1956,
        "title": "Seventh Amendment",
        "summary": (
            "Among other reorganisation changes, facilitated appointment of the same person "
            "as Governor for two or more states."
        ),
        "effect": "Art. 153 read with 7th CAA — multi-state Governor possible.",
        "concept_slugs": ["gov-appointment", HUB_SLUG],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Made ministerial advice binding on the President — no parallel provision for Governor."
        ),
        "effect": "Key contrast: Governor retains broader Art. 163 discretion space.",
        "concept_slugs": ["gov-constitutional-position", HUB_SLUG],
    },
    {
        "number": 94,
        "year": 2006,
        "title": "Ninety-fourth Amendment",
        "summary": (
            "Excluded Bihar from the requirement of a Tribal Welfare Minister among specified states."
        ),
        "effect": "Tribal Welfare Minister: Chhattisgarh, Jharkhand, Madhya Pradesh, Odisha only.",
        "concept_slugs": ["gov-executive", HUB_SLUG],
    },
    {
        "number": 98,
        "year": 2012,
        "title": "Ninety-eighth Amendment",
        "summary": (
            "Added special responsibility for a separate development board for the "
            "Hyderabad-Karnataka region."
        ),
        "effect": "Karnataka joins the special-responsibility list for the Governor.",
        "concept_slugs": ["gov-discretion", HUB_SLUG],
    },
    {
        "number": 104,
        "year": 2019,
        "title": "One Hundred and Fourth Amendment",
        "summary": (
            "Discontinued nomination of Anglo-Indian members to the Lok Sabha and state assemblies."
        ),
        "effect": "Governor no longer nominates an Anglo-Indian MLA (from 25 Jan 2020).",
        "concept_slugs": ["gov-legislative-financial", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed Governor chapter (Laxmikanth Ch.30) under Part IV State Government."

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
                "title": "Governor",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 30",
                "summary": (
                    "Visual revision of Ch.30 — dual role, appointment, powers, vetoes, "
                    "ordinances, pardon, discretion, and Sarkaria issues."
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
                "title": "Governor",
                "summary": (
                    "Constitutional head of the state and agent of the Centre — dual role "
                    "under Arts 153–167 in Part VI."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **two hats** mental model, then "
                    "**Appointment** → **Term (pleasure)** → **Veto / Ordinance / Pardon** → "
                    "**Art. 163 discretion** → **Sarkaria issues**. Finish with the **Exam kit**. "
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
            ref="Laxmikanth Ch. 30",
            excerpt=(
                "Governor — dual role, appointment, powers, vetoes, ordinances, "
                "pardon, discretion, and Sarkaria issues."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 153–167",
            excerpt="State executive framework in Part VI — Governor as nominal head with dual role.",
            sort_order=1,
        )

        gov_slugs = set(by_slug.keys())
        related_outside = {
            "parliamentary-system",
            "president",
            "emergency-provisions",
            "federal-system",
        }
        ConceptEdge.objects.filter(
            source__slug__in=gov_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=gov_slugs | related_outside).delete()

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
                f"Governor chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
