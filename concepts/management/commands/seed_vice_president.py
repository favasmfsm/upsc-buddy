"""Seed Laxmikanth Ch.19 Vice-President (visual revision)."""

from django.core.management.base import BaseCommand

from concepts.models import (
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "vice-president"
CHAPTER_SLUG = "vice-president"

ENTRY_PILLARS = [
    {
        "id": "election",
        "articles": "Art. 66",
        "label": "Election",
        "slug": "vp-election",
        "detail": "Parliament only (elected + nominated); no MLAs; PR + STV.",
        "tone": "teal",
    },
    {
        "id": "quals",
        "articles": "Art. 66 · 69",
        "label": "Quals, oath & conditions",
        "slug": "vp-qualifications-oath",
        "detail": "C-35-RS-NoProfit; oath by President; seat vacated on entry.",
        "tone": "olive",
    },
    {
        "id": "term",
        "articles": "Art. 67–68",
        "label": "Term, removal & vacancy",
        "slug": "vp-term-removal",
        "detail": "5 years; RS starts removal; R-14-ES majorities; fresh term on casual fill.",
        "tone": "gold",
    },
    {
        "id": "powers",
        "articles": "Art. 64–65",
        "label": "Powers & functions",
        "slug": "vp-powers-functions",
        "detail": "RS Chairman + acting/discharging President (≤6 months on vacancy).",
        "tone": "orange",
    },
    {
        "id": "rs",
        "articles": "Art. 64",
        "label": "Rajya Sabha Chairman",
        "slug": "vp-rajya-sabha",
        "detail": "Day job = Speaker-like Chair; salary as Chairman, not as VP.",
        "tone": "terracotta",
    },
    {
        "id": "usa",
        "articles": "Compare",
        "label": "India vs USA",
        "slug": "vp-india-vs-usa",
        "detail": "Acting ≠ succession; ‘His Superfluous Highness’.",
        "tone": "maroon",
    },
    {
        "id": "articles",
        "articles": "Arts 63–71",
        "label": "Articles at a glance",
        "slug": "vp-articles",
        "detail": "63 exists → 71 SC disputes — one-liner map.",
        "tone": "teal",
    },
    {
        "id": "exam",
        "articles": "Prelims / Mains",
        "label": "Exam anchors",
        "slug": "vp-exam-anchors",
        "detail": "Timeline, traps, PYQ themes, mains value-adds.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "vp-spare-tyre-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Spare tyre + House speaker",
        "topic_label": "Vice-President",
        "subject_label": "Arts 63–71",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating VP as President for the unexpired term",
            "Using the President’s electoral college for VP",
            "Starting removal from Lok Sabha",
            "Saying the VP draws a fixed VP salary",
        ],
        "insight": (
            "Daily job: chair Rajya Sabha. Continuity job: act or discharge as President "
            "until a new President is elected or the sitting one resumes — not US-style succession."
        ),
    },
    {
        "id": "vp-entry-pillars",
        "type": "pillars",
        "title": "Eight revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "vp-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "College ≠ President’s (nominated MPs vote; no MLAs) → "
            "Removal only from Rajya Sabha (R-14-ES) → "
            "Acting President ≤ 6 months → "
            "Salary as RS Chairman → "
            "‘His Superfluous Highness’ = continuity, not power."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Election",
        "slug": "vp-election",
        "sort_order": 1,
        "summary": (
            "Indirect election by both Houses of Parliament (elected + nominated); "
            "no state MLAs; PR by STV; SC decides disputes."
        ),
        "body": (
            "## Election (Art. 66) — revision spine\n\n"
            "- **Indirect** election — not by the people.\n"
            "- Electoral college = members of **both Houses of Parliament** "
            "(**elected and nominated**).\n"
            "- **Does not** include members of state legislative assemblies.\n"
            "- **Manner** same as President: proportional representation by "
            "**single transferable vote**; **secret ballot**.\n\n"
            "### Why different from President? (Ambedkar)\n"
            "- President = head of State for Centre **and** states → MLAs must have a voice.\n"
            "- VP’s normal job = preside over the Council of States; acting as President is rare "
            "and temporary → state legislatures need not elect the VP.\n\n"
            "### Disputes (Art. 71)\n"
            "- Supreme Court inquires and decides; decision is **final**.\n"
            "- Incomplete electoral college ≠ ground to challenge.\n"
            "- If election later voided, acts done before the SC declaration remain valid.\n\n"
            "### Procedure note\n"
            "- Original Constitution: election by both Houses assembled at a **joint meeting**.\n"
            "- **11th Amendment (1961)** removed that cumbersome joint-sitting procedure."
        ),
        "articles": [
            (
                "Art. 66",
                "Election of Vice-President — electoral college of both Houses; PR by STV.",
            ),
            (
                "Art. 71",
                "Matters relating to election of VP — SC decides; acts before voiding stay valid.",
            ),
            (
                "11th Amendment (1961)",
                "Ended joint-sitting election of the Vice-President.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "vp-college-compare",
                "type": "comparison",
                "title": "Electoral college — VP vs President",
                "columns": [
                    {
                        "id": "vp",
                        "heading": "Vice-President (Art. 66)",
                        "points": [
                            "Both Houses of Parliament",
                            "Elected + nominated MPs",
                            "No state MLAs / MLCs",
                            "PR by STV; secret ballot",
                        ],
                    },
                    {
                        "id": "pres",
                        "heading": "President (Art. 54)",
                        "points": [
                            "Elected MPs of both Houses",
                            "No nominated MPs",
                            "Elected MLAs of states (+ Delhi/Puducherry etc.)",
                            "PR by STV; secret ballot",
                        ],
                    },
                ],
            },
            {
                "id": "vp-dispute-flow",
                "type": "flowchart",
                "title": "Election dispute path",
                "root": "doubt",
                "steps": [
                    {
                        "id": "doubt",
                        "label": "Doubt / dispute on VP election",
                        "detail": "Art. 71",
                        "options": [
                            {"label": "Who decides?", "next": "sc"},
                        ],
                    },
                    {
                        "id": "sc",
                        "label": "Supreme Court",
                        "detail": "Inquiry + decision is final.",
                        "options": [
                            {"label": "College incomplete?", "next": "incomplete"},
                            {"label": "Election declared void?", "next": "void"},
                        ],
                    },
                    {
                        "id": "incomplete",
                        "label": "Not a challenge ground",
                        "detail": "Vacancy in the electoral college does not invalidate the election.",
                    },
                    {
                        "id": "void",
                        "label": "Past acts still valid",
                        "detail": "Acts done before the SC declaration continue in force.",
                    },
                ],
            },
            {
                "id": "vp-election-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Prelims traps",
                "body": (
                    "Nominated MPs vote for VP, not for President. "
                    "No MLAs in VP college. "
                    "Manner (PR+STV) is the same — composition is not."
                ),
            },
        ],
    },
    {
        "title": "Qualifications, Oath & Conditions",
        "slug": "vp-qualifications-oath",
        "sort_order": 2,
        "summary": (
            "Citizen, 35 years, Rajya Sabha-eligible, no office of profit; "
            "oath by President; legislature seat vacated on entering office."
        ),
        "body": (
            "## Qualifications (four)\n\n"
            "1. Citizen of India.\n"
            "2. Completed **35 years** of age.\n"
            "3. Qualified for election as a member of the **Rajya Sabha** "
            "(not Lok Sabha).\n"
            "4. Does not hold any **office of profit** under Union / state / local / other public authority.\n\n"
            "### Office of profit — not deemed\n"
            "Sitting President or VP, Governor of any state, and Union/state minister "
            "are **not** treated as holding an office of profit for this candidature.\n\n"
            "### Nomination (statute)\n"
            "- ≥ **20 proposers** + **20 seconders** (electors).\n"
            "- Security deposit **₹15,000** in RBI "
            "(Presidential and Vice-Presidential Elections Act, 1952 as amended 1997).\n\n"
            "### Oath (Art. 69)\n"
            "- Bear true faith and allegiance to the Constitution; faithfully discharge duties.\n"
            "- Administered by the **President** (or a person appointed by the President).\n\n"
            "### Conditions of office\n"
            "1. Not a member of either House of Parliament or any state legislature — "
            "if elected, the seat is **deemed vacated** on entering VP office.\n"
            "2. Shall not hold any other office of profit.\n\n"
            "**Mnemonic:** `C-35-RS-NoProfit`."
        ),
        "articles": [
            (
                "Art. 66",
                "Qualifications for election as Vice-President (incl. Rajya Sabha eligibility).",
            ),
            (
                "Art. 69",
                "Oath or affirmation by the Vice-President — administered by the President.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "vp-quals-pillars",
                "type": "pillars",
                "title": "Four qualifications (C-35-RS-NoProfit)",
                "items": [
                    {
                        "id": "citizen",
                        "articles": "1",
                        "label": "Citizen of India",
                        "slug": "vp-qualifications-oath",
                        "detail": "Must be an Indian citizen.",
                        "tone": "teal",
                    },
                    {
                        "id": "age",
                        "articles": "35",
                        "label": "35 years of age",
                        "slug": "vp-qualifications-oath",
                        "detail": "Same age floor as President.",
                        "tone": "olive",
                    },
                    {
                        "id": "rs",
                        "articles": "RS",
                        "label": "Rajya Sabha-eligible",
                        "slug": "vp-qualifications-oath",
                        "detail": "Qualified for RS membership — not Lok Sabha.",
                        "tone": "gold",
                    },
                    {
                        "id": "profit",
                        "articles": "4",
                        "label": "No office of profit",
                        "slug": "vp-qualifications-oath",
                        "detail": "Exceptions: sitting President/VP, Governor, Union/state minister.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "vp-quals-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Exam traps",
                "body": (
                    "Qualified for **Rajya Sabha**, not Lok Sabha. "
                    "Oath by **President** (President’s oath is by CJI). "
                    "20+20 proposers/seconders and ₹15k deposit are statutory, not in the Constitution text."
                ),
            },
            {
                "id": "vp-quals-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": "C-35-RS-NoProfit → Citizen · 35 · Rajya Sabha-eligible · No office of profit.",
            },
        ],
    },
    {
        "title": "Term, Removal & Vacancy",
        "slug": "vp-term-removal",
        "sort_order": 3,
        "summary": (
            "Five-year term; removal by RS effective majority + LS simple majority "
            "after 14 days’ notice; casual vacancy gets a full fresh term."
        ),
        "body": (
            "## Term (Art. 67)\n\n"
            "- Holds office for **five years** from the date of entering office.\n"
            "- May resign anytime by writing to the **President**.\n"
            "- Continues until successor assumes charge.\n"
            "- Eligible for **re-election** for any number of terms "
            "(e.g. Dr. S. Radhakrishnan — second term).\n\n"
            "## Removal — not impeachment\n\n"
            "- **No** formal impeachment; Constitution mentions **no grounds**.\n"
            "- Resolution can be introduced **only in Rajya Sabha** (not Lok Sabha).\n"
            "- RS: passed by a majority of **all the then members** (effective majority).\n"
            "- LS: **agrees** by **simple majority**.\n"
            "- At least **14 days’** advance notice before moving the resolution.\n\n"
            "**Mnemonic:** `R-14-ES` — Rajya Sabha starts · 14 days · Effective then Simple.\n\n"
            "## Vacancy (Art. 68)\n\n"
            "Can arise by: expiry of tenure · resignation · removal · death · otherwise "
            "(disqualification / election declared void).\n\n"
            "- Term about to expire → election **before** expiry.\n"
            "- Casual vacancy → election **as soon as possible**; newly elected VP gets a "
            "**full fresh five years** from assuming charge.\n"
            "- Krishna Kant was the first Vice-President to die in office."
        ),
        "articles": [
            (
                "Art. 67",
                "Term of office — resignation to President; removal by RS resolution agreed by LS.",
            ),
            (
                "Art. 68",
                "Time of holding election to fill vacancy; casual vacancy → full fresh term.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "vp-removal-flow",
                "type": "flowchart",
                "title": "Removal path (Art. 67)",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "Move to remove VP",
                        "detail": "No grounds listed; not impeachment.",
                        "options": [
                            {"label": "Which House initiates?", "next": "rs"},
                        ],
                    },
                    {
                        "id": "rs",
                        "label": "Rajya Sabha only",
                        "detail": "Cannot introduce in Lok Sabha. 14 days’ advance notice.",
                        "options": [
                            {"label": "RS majority needed?", "next": "effective"},
                        ],
                    },
                    {
                        "id": "effective",
                        "label": "Effective majority in RS",
                        "detail": "Majority of all the then members of Rajya Sabha.",
                        "options": [
                            {"label": "Then Lok Sabha?", "next": "ls"},
                        ],
                    },
                    {
                        "id": "ls",
                        "label": "Lok Sabha agrees — simple majority",
                        "detail": "Agreement by simple majority completes removal.",
                    },
                ],
            },
            {
                "id": "vp-vacancy-compare",
                "type": "comparison",
                "title": "Exit paths & vacancy fill",
                "columns": [
                    {
                        "id": "resign",
                        "heading": "Resignation",
                        "points": [
                            "Letter addressed to the President",
                            "Casual vacancy → elect ASAP",
                            "New VP: full fresh 5 years",
                        ],
                    },
                    {
                        "id": "remove",
                        "heading": "Removal",
                        "points": [
                            "RS initiates (R-14-ES)",
                            "No constitutional grounds",
                            "Not impeachment like President",
                        ],
                    },
                    {
                        "id": "expiry",
                        "heading": "Term expiry",
                        "points": [
                            "Election before term ends",
                            "May continue until successor takes charge",
                            "Re-election allowed (unlimited)",
                        ],
                    },
                ],
            },
            {
                "id": "vp-term-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "R-14-ES: Rajya Sabha starts · 14 days’ notice · Effective majority (RS) "
                    "then Simple majority (LS)."
                ),
            },
        ],
    },
    {
        "title": "Powers & Functions",
        "slug": "vp-powers-functions",
        "sort_order": 4,
        "summary": (
            "Two-fold role: ex-officio Rajya Sabha Chairman, and act/discharge as President "
            "in vacancy or absence — acting ≤ six months on vacancy."
        ),
        "body": (
            "## Two-fold functions only\n\n"
            "1. **Ex-officio Chairman of Rajya Sabha** (Art. 64) — powers similar to "
            "Lok Sabha Speaker in that capacity.\n"
            "2. **Act as / discharge functions of President** (Art. 65) when needed.\n\n"
            "### When does the VP step into the President’s chair?\n\n"
            "**Vacancy** (resignation, impeachment, death, or otherwise):\n"
            "- VP **acts as President** for a **maximum of six months** — "
            "a new President must be elected within that period.\n\n"
            "**Absence / illness / other cause** (sitting President unable to discharge functions):\n"
            "- VP **discharges** the President’s functions until the President resumes.\n\n"
            "### While acting / discharging\n"
            "- Does **not** perform duties of RS Chairman — **Deputy Chairman** does.\n"
            "- Entitled to **President’s** salary and allowances (not Chairman’s) for that period.\n\n"
            "### Continuity examples (Laxmikanth)\n"
            "- Zakir Husain / Fakhruddin Ali Ahmed died in office → V.V. Giri / B.D. Jatti acted.\n"
            "- Radhakrishnan discharged functions when Rajendra Prasad was abroad (1960) / ill (1961).\n\n"
            "**Art. 70:** discharge of President’s functions in other contingencies "
            "(Parliament may make provision)."
        ),
        "articles": [
            (
                "Art. 64",
                "Vice-President is ex-officio Chairman of the Council of States.",
            ),
            (
                "Art. 65",
                "VP acts as President or discharges functions during casual vacancy / absence.",
            ),
            (
                "Art. 70",
                "Discharge of President’s functions in other contingencies.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "vp-acting-flow",
                "type": "flowchart",
                "title": "When does the VP take the President’s chair?",
                "root": "trigger",
                "steps": [
                    {
                        "id": "trigger",
                        "label": "President’s office issue",
                        "detail": "Art. 65",
                        "options": [
                            {"label": "Vacancy (death / resign / impeach / otherwise)", "next": "act"},
                            {"label": "Absence / illness / other cause", "next": "discharge"},
                        ],
                    },
                    {
                        "id": "act",
                        "label": "VP acts as President",
                        "detail": "Maximum six months — new President must be elected.",
                        "options": [
                            {"label": "RS Chair meanwhile?", "next": "deputy"},
                        ],
                    },
                    {
                        "id": "discharge",
                        "label": "VP discharges functions",
                        "detail": "Until the sitting President resumes office.",
                        "options": [
                            {"label": "RS Chair meanwhile?", "next": "deputy"},
                        ],
                    },
                    {
                        "id": "deputy",
                        "label": "Deputy Chairman chairs Rajya Sabha",
                        "detail": "VP does not preside as Chairman while acting/discharging.",
                    },
                ],
            },
            {
                "id": "vp-dual-pillars",
                "type": "pillars",
                "title": "Dual role",
                "items": [
                    {
                        "id": "chair",
                        "articles": "Art. 64",
                        "label": "RS Chairman",
                        "slug": "vp-rajya-sabha",
                        "detail": "Normal, continuous legislative role — Speaker-like in Upper House.",
                        "tone": "teal",
                    },
                    {
                        "id": "acting",
                        "articles": "Art. 65",
                        "label": "Acting / discharging President",
                        "slug": "vp-powers-functions",
                        "detail": "Rare continuity role — ≤6 months on vacancy; not unexpired-term succession.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "vp-powers-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Acting ≠ succession",
                "body": (
                    "Indian VP does **not** become President for the unexpired term. "
                    "That is the US model. India: acting President until a new election."
                ),
            },
        ],
    },
    {
        "title": "Rajya Sabha Chairman Role",
        "slug": "vp-rajya-sabha",
        "sort_order": 5,
        "summary": (
            "Ex-officio Chairman of Rajya Sabha; Speaker-like powers; "
            "no separate VP salary — paid as Chairman."
        ),
        "body": (
            "## Day job = Chairman (Art. 64)\n\n"
            "- VP is **ex-officio Chairman** of the Council of States (Rajya Sabha).\n"
            "- As presiding officer, powers and functions resemble those of the "
            "**Speaker of Lok Sabha** (in the Upper House context).\n"
            "- Resembles the American VP who chairs the Senate.\n\n"
            "### Key operating rules\n"
            "- Cannot preside over Rajya Sabha when a resolution for **own removal** "
            "is under consideration.\n"
            "- While acting as / discharging President’s functions, does **not** chair RS — "
            "Deputy Chairman does.\n\n"
            "### Emoluments\n"
            "- Constitution fixes **no salary for the Vice-President as such**.\n"
            "- Draws regular salary as **ex-officio Chairman of Rajya Sabha**.\n"
            "- As per Laxmikanth 8e: Finance Act 2018 raised Chairman’s salary from "
            "₹1.25 lakh to **₹4 lakh/month** (w.e.f. 1 Jan 2016).\n"
            "- Pension (2008 amendment): **50% of salary** per month "
            "(earlier ₹20,000/month).\n"
            "- Also: daily allowance, free furnished residence, medical, travel, etc.\n\n"
            "**Revision box:** Day job = Chairman; night job = continuity insurance."
        ),
        "articles": [
            (
                "Art. 64",
                "Vice-President to be ex-officio Chairman of the Council of States.",
            ),
            (
                "Art. 67",
                "Removal resolution — VP cannot preside as Chairman while it is under consideration.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "vp-rs-pillars",
                "type": "pillars",
                "title": "Chairman role — revision set",
                "items": [
                    {
                        "id": "exofficio",
                        "articles": "Art. 64",
                        "label": "Ex-officio Chair",
                        "slug": "vp-rajya-sabha",
                        "detail": "Office of VP automatically makes one Chairman of Rajya Sabha.",
                        "tone": "teal",
                    },
                    {
                        "id": "speakerlike",
                        "articles": "Practice",
                        "label": "Speaker-like powers",
                        "slug": "vp-rajya-sabha",
                        "detail": "Presiding-officer powers akin to Lok Sabha Speaker in the Upper House.",
                        "tone": "olive",
                    },
                    {
                        "id": "noremoval",
                        "articles": "Art. 67",
                        "label": "No chair during own removal",
                        "slug": "vp-rajya-sabha",
                        "detail": "Cannot preside when a removal resolution against self is under consideration.",
                        "tone": "gold",
                    },
                    {
                        "id": "pay",
                        "articles": "Statute",
                        "label": "Paid as Chairman",
                        "slug": "vp-rajya-sabha",
                        "detail": "No constitutional VP salary — pay is as RS Chairman (Laxmikanth 8e figures).",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "vp-rs-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Salary trap",
                "body": (
                    "There is no fixed constitutional salary ‘as Vice-President’. "
                    "Pay = Chairman of Rajya Sabha. While acting as President → President’s pay."
                ),
            },
        ],
    },
    {
        "title": "India vs American VP",
        "slug": "vp-india-vs-usa",
        "sort_order": 6,
        "summary": (
            "Modelled on the US Vice-President, but India uses acting presidency — "
            "not succession for the unexpired term."
        ),
        "body": (
            "## Same model, different succession\n\n"
            "- Office is **modelled on** the American Vice-President "
            "(also chairs the Upper House).\n"
            "- **Critical difference:** US VP **succeeds** to the presidency for the "
            "**unexpired term** of the predecessor.\n"
            "- Indian VP **merely acts** as President until a new President assumes charge.\n\n"
            "### Why create the office?\n"
            "- Constitution assigns few significant standalone VP functions.\n"
            "- Scholars’ jab: **‘His Superfluous Highness’**.\n"
            "- Design purpose: maintain **political continuity** of the Indian State.\n\n"
            "**Mains line:** Continuity device in a parliamentary republic — not a powerful "
            "second executive."
        ),
        "articles": [
            (
                "Art. 64–65",
                "Legislative chairmanship + temporary presidential continuity — not US succession.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "vp-india-usa-compare",
                "type": "comparison",
                "title": "Indian VP vs American VP",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Modelled on US VP",
                            "Ex-officio Chairman of Rajya Sabha",
                            "Acts as President until new election",
                            "Max 6 months on presidential vacancy",
                            "Few standalone VP functions",
                            "‘His Superfluous Highness’ critique",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Source model",
                            "President of the Senate",
                            "Succeeds as President",
                            "Serves unexpired term of predecessor",
                            "Succession-centric design",
                            "Clear line in presidential vacancy",
                        ],
                    },
                ],
            },
            {
                "id": "vp-usa-mains",
                "type": "callout",
                "tone": "note",
                "title": "Mains value-add",
                "body": (
                    "Use the contrast to argue: Indian VP is a **continuity and legislative** "
                    "office, not a shadow executive. Pair with Ambedkar’s reason for excluding "
                    "state legislatures from the electoral college."
                ),
            },
        ],
    },
    {
        "title": "Articles at a Glance",
        "slug": "vp-articles",
        "sort_order": 7,
        "summary": (
            "Arts 63–71 one-liner map — from creation of the office to election disputes."
        ),
        "body": (
            "## Articles related to Vice-President\n\n"
            "| Art | One-liner |\n"
            "|-----|-----------|\n"
            "| **63** | There shall be a Vice-President of India |\n"
            "| **64** | Ex-officio Chairman of the Council of States |\n"
            "| **65** | Act as / discharge President’s functions (vacancy or absence) |\n"
            "| **66** | Election of Vice-President |\n"
            "| **67** | Term, resignation, removal |\n"
            "| **68** | Time of election to fill vacancy; term of person elected |\n"
            "| **69** | Oath or affirmation |\n"
            "| **70** | Discharge of President’s functions in other contingencies |\n"
            "| **71** | Matters relating to election (SC) |\n\n"
            "**Memory chain:** "
            "`63 exists → 64 chairs → 65 acts → 66 elects → 67 term → 68 fills → 69 oath → 70 contingency → 71 SC`.\n\n"
            "**Revision triangle:** 66 (who elects) · 68 (when to fill) · 69 (oath before entry)."
        ),
        "articles": [
            ("Art. 63", "The Vice-President of India."),
            ("Art. 64", "Ex-officio Chairman of the Council of States."),
            ("Art. 65", "Act as President or discharge functions during vacancy / absence."),
            ("Art. 66", "Election of Vice-President."),
            ("Art. 67", "Term of office of Vice-President."),
            ("Art. 68", "Time of holding election to fill vacancy."),
            ("Art. 69", "Oath or affirmation by the Vice-President."),
            ("Art. 70", "Discharge of President’s functions in other contingencies."),
            ("Art. 71", "Matters relating to election of Vice-President."),
        ],
        "visual_blocks": [
            {
                "id": "vp-articles-tree",
                "type": "tree",
                "title": "Arts 63–71 map",
                "root": {
                    "id": "vp-root",
                    "label": "Vice-President",
                    "detail": "Arts 63–71",
                    "children": [
                        {
                            "id": "office",
                            "label": "Office & role",
                            "detail": "63–65",
                            "children": [
                                {"id": "a63", "label": "63 — Exists", "detail": "There shall be a VP"},
                                {"id": "a64", "label": "64 — Chairs RS", "detail": "Ex-officio Chairman"},
                                {"id": "a65", "label": "65 — Acts / discharges", "detail": "Presidential continuity"},
                            ],
                        },
                        {
                            "id": "process",
                            "label": "Process",
                            "detail": "66–69",
                            "children": [
                                {"id": "a66", "label": "66 — Election", "detail": "College + PR/STV"},
                                {"id": "a67", "label": "67 — Term / removal", "detail": "5 years; R-14-ES"},
                                {"id": "a68", "label": "68 — Fill vacancy", "detail": "Timing + fresh term"},
                                {"id": "a69", "label": "69 — Oath", "detail": "By President"},
                            ],
                        },
                        {
                            "id": "safety",
                            "label": "Safety net",
                            "detail": "70–71",
                            "children": [
                                {"id": "a70", "label": "70 — Other contingencies", "detail": "Parliament may provide"},
                                {"id": "a71", "label": "71 — Election disputes", "detail": "SC final"},
                            ],
                        },
                    ],
                },
            },
            {
                "id": "vp-articles-tip",
                "type": "callout",
                "tone": "tip",
                "title": "66–68–69 triangle",
                "body": (
                    "Before entry: elect under **66**, swear under **69**. "
                    "If the chair empties mid-stream: fill under **68**."
                ),
            },
        ],
    },
    {
        "title": "Exam Anchors",
        "slug": "vp-exam-anchors",
        "sort_order": 8,
        "summary": (
            "Compact history timeline, prelims fact pack, PYQ themes, and mains value-adds "
            "for last-minute Vice-President revision."
        ),
        "body": (
            "## Prelims fact pack\n\n"
            "- Rank: next to the President in the official warrant of precedence.\n"
            "- Modelled on American VP — but **acting ≠ succession**.\n"
            "- College: all MPs (elected + nominated); **no MLAs**.\n"
            "- Qualification: eligible for **Rajya Sabha**, not Lok Sabha.\n"
            "- Removal: **only RS initiates**; effective majority (RS) + simple (LS); "
            "14 days’ notice; **no grounds**.\n"
            "- Acting as President on vacancy: **≤ 6 months**.\n"
            "- Salary: as **RS Chairman**, not as VP.\n"
            "- Election disputes: **Supreme Court** (Art. 71).\n\n"
            "## PYQ themes\n\n"
            "- Electoral college composition vs President (nominated MPs / MLAs).\n"
            "- Removal procedure, majority type, which House initiates.\n"
            "- Acting President time limit and Deputy Chairman takeover.\n"
            "- Qualification (RS eligibility / office of profit exceptions).\n"
            "- India–US succession contrast.\n"
            "- 11th Amendment / Art. 71 finality.\n\n"
            "## Mains value-adds\n\n"
            "- Ambedkar: why states stay out of VP election.\n"
            "- Continuity rationale vs ‘His Superfluous Highness’.\n"
            "- Dual-role tension: Chair of RS vs acting President.\n"
            "- Bridge: VP removal (Art. 67) vs President impeachment (Art. 61) — "
            "different houses, majorities, and grounds logic."
        ),
        "articles": [
            (
                "Arts 63–71",
                "Full Vice-President cluster — election, term, role, disputes.",
            ),
            (
                "11th Amendment (1961)",
                "Simplified VP election procedure (ended joint sitting).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "vp-history-timeline",
                "type": "timeline",
                "title": "Notable moments (compact)",
                "events": [
                    {
                        "id": "e1960",
                        "year": 1960,
                        "label": "Radhakrishnan discharges",
                        "detail": "President Prasad on USSR tour — VP discharges functions.",
                    },
                    {
                        "id": "e1961",
                        "year": 1961,
                        "label": "11th Amendment + illness stint",
                        "detail": "Joint-sitting election ended; again discharges when Prasad ill.",
                    },
                    {
                        "id": "e1969",
                        "year": 1969,
                        "label": "Giri acts as President",
                        "detail": "After Zakir Husain’s death in office.",
                    },
                    {
                        "id": "e1977",
                        "year": 1977,
                        "label": "Jatti acts as President",
                        "detail": "After Fakhruddin Ali Ahmed’s death (Laxmikanth).",
                    },
                    {
                        "id": "e1997",
                        "year": 1997,
                        "label": "Election rules tightened",
                        "detail": "Proposers/seconders 5→20; security deposit hiked (to ₹15,000).",
                    },
                    {
                        "id": "e2008",
                        "year": 2008,
                        "label": "Pension update",
                        "detail": "VP pension → 50% of salary (Laxmikanth 8e).",
                    },
                    {
                        "id": "e2018",
                        "year": 2018,
                        "label": "Chairman salary",
                        "detail": "RS Chairman pay to ₹4 lakh/month (Finance Act 2018; Laxmikanth 8e).",
                    },
                    {
                        "id": "e2022",
                        "year": 2022,
                        "label": "Dhankhar elected",
                        "detail": "Latest winner in Laxmikanth’s elections table.",
                    },
                ],
            },
            {
                "id": "vp-pyq-themes",
                "type": "callout",
                "tone": "tip",
                "title": "PYQ themes to drill",
                "body": (
                    "College composition · Removal (House + majority + 14 days) · "
                    "Acting ≤6 months · RS (not LS) qualification · India≠USA succession · "
                    "11th Amendment / Art. 71."
                ),
            },
            {
                "id": "vp-mains-box",
                "type": "callout",
                "tone": "note",
                "title": "Mains revision box",
                "body": (
                    "Frame answers around continuity of the State + RS chairmanship. "
                    "Cite Ambedkar on the electoral college, then contrast US succession. "
                    "Close with the ‘superfluous’ critique and why the office still matters."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "vp-election"),
    (HUB_SLUG, "parent", "vp-qualifications-oath"),
    (HUB_SLUG, "parent", "vp-term-removal"),
    (HUB_SLUG, "parent", "vp-powers-functions"),
    (HUB_SLUG, "parent", "vp-rajya-sabha"),
    (HUB_SLUG, "parent", "vp-india-vs-usa"),
    (HUB_SLUG, "parent", "vp-articles"),
    (HUB_SLUG, "parent", "vp-exam-anchors"),
    ("vp-election", "related", "vp-articles"),
    ("vp-election", "related", "vp-qualifications-oath"),
    ("vp-term-removal", "related", "vp-exam-anchors"),
    ("vp-term-removal", "related", "vp-rajya-sabha"),
    ("vp-powers-functions", "related", "vp-rajya-sabha"),
    ("vp-powers-functions", "related", "vp-india-vs-usa"),
    ("vp-india-vs-usa", "related", "vp-exam-anchors"),
    ("vp-articles", "related", "vp-exam-anchors"),
    # Soft cross-chapter links (skipped if missing)
    (HUB_SLUG, "related", "president"),
    ("vp-election", "related", "president"),
    ("vp-powers-functions", "related", "president"),
]

AMENDMENTS = [
    {
        "number": 11,
        "year": 1961,
        "title": "Eleventh Amendment",
        "summary": (
            "Changed the manner of electing the Vice-President — ended the original "
            "requirement of both Houses assembling at a joint meeting."
        ),
        "effect": (
            "VP election procedure aligned with a simpler parliamentary college vote "
            "(still PR by STV)."
        ),
        "concept_slugs": [HUB_SLUG, "vp-election", "vp-exam-anchors"],
    },
]

SAMPLE_PYQS = [
    (
        2013,
        "With reference to the election of the Vice-President of India, consider the composition "
        "of the electoral college.",
        "Electoral college = members of both Houses of Parliament (elected and nominated). "
        "It does not include elected members of state legislative assemblies — unlike the President.",
        [HUB_SLUG, "vp-election", "vp-exam-anchors"],
    ),
    (
        2018,
        "Which of the following is/are correct regarding removal of the Vice-President of India?",
        "Resolution can be introduced only in Rajya Sabha; requires majority of all the then "
        "members of RS and agreement of Lok Sabha by simple majority; 14 days’ notice; "
        "no grounds specified in the Constitution.",
        ["vp-term-removal", "vp-exam-anchors"],
    ),
    (
        2004,
        "Who among the following can participate in the election of both the President and "
        "the Vice-President of India?",
        "Elected members of both Houses of Parliament participate in both. Nominated MPs "
        "vote for VP but not for President; MLAs vote for President but not for VP.",
        ["vp-election", HUB_SLUG],
    ),
    (
        2012,
        "Consider the following statements about the Vice-President of India acting as President.",
        "On a presidential vacancy the VP acts as President for a maximum of six months. "
        "While so acting, the Deputy Chairman performs the duties of Chairman of Rajya Sabha. "
        "The Indian VP does not succeed for the unexpired term (unlike the US VP).",
        ["vp-powers-functions", "vp-india-vs-usa", "vp-exam-anchors"],
    ),
    (
        2009,
        "A candidate for the office of Vice-President of India must be qualified for election as a "
        "member of which House?",
        "Rajya Sabha (Council of States) — not Lok Sabha.",
        ["vp-qualifications-oath", "vp-exam-anchors"],
    ),
    (
        2016,
        "The Constitution of India does not mention any ground for the removal of which of the "
        "following officers / authorities?",
        "Vice-President — Art. 67 provides the removal process but specifies no grounds "
        "(contrast with impeachment grounds for the President).",
        ["vp-term-removal", "vp-exam-anchors"],
    ),
]


class Command(BaseCommand):
    help = "Seed Vice-President chapter (Laxmikanth Ch.19)."

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
                "title": "Vice-President",
                "sort_order": 2,
                "book_ref": "Laxmikanth 8th Ed, Ch. 19",
                "summary": (
                    "Visual revision of Ch.19 — election, qualifications, term/removal, "
                    "powers, Rajya Sabha Chairman role, India vs USA, and exam anchors."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Vice-President",
                "summary": (
                    "Second-highest office — ex-officio Rajya Sabha Chairman and "
                    "continuity stand-in for the President (acting, not succession)."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **spare tyre + House speaker** mental model, then "
                    "**Election** → **Quals** → **Term/removal**. "
                    "Drill **Powers** and **RS Chairman**, contrast **India vs USA**, "
                    "lock **Arts 63–71**, finish with **Exam anchors**. "
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
            ref="Laxmikanth Ch. 19",
            excerpt=(
                "Vice-President — Arts 63–71; election, term/removal, dual role, "
                "India vs USA."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 64 & 65",
            excerpt="Ex-officio RS Chairman; act as / discharge President’s functions.",
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 66 & 67",
            excerpt="Election by Parliament; five-year term; RS-led removal (R-14-ES).",
            sort_order=2,
        )

        vp_slugs = set(by_slug.keys())
        related_outside = {"president"}
        ConceptEdge.objects.filter(
            source__slug__in=vp_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=vp_slugs | related_outside).delete()

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
                f"Vice-President chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(AMENDMENTS)} amendments linked, {len(SAMPLE_PYQS)} PYQs."
            )
        )
