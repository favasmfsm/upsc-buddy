"""Seed Laxmikanth Ch.95 World Constitutions (Part XIII — visual revision)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "world-constitutions"
CHAPTER_SLUG = "world-constitutions"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

INDIA_COMPARE_BASE = {
    "form": "Parliamentary republic (Westminster + republican head of state)",
    "executive": "Nominal President + real PM/Council of Ministers (Arts 74–75)",
    "legislature": "Bicameral Parliament; Lok Sabha dominant; Rajya Sabha federal",
    "judiciary": "Integrated & independent; SC apex; judicial review + basic structure",
    "federalism": "Quasi-federal / federal with unitary bias; residuary with Centre",
    "amendment": "Art. 368 — simple / special / special + state ratification",
    "jr": "Strong judicial review; due process evolved via Art. 21; basic structure",
    "rights": "Justiciable FRs (Part III) + non-justiciable DPSPs (Part IV) + FDs",
    "emergency": "Arts 352/356/360 — National, State, Financial; post-44th safeguards",
    "philosophy": "Liberty, equality, fraternity; justice (SEP); secular democratic republic",
}


def india_vs(country_id: str, country_heading: str, them: dict) -> dict:
    """Build a 2-column India vs Country comparison visual."""
    labels = [
        ("form", "Form of Government"),
        ("executive", "Executive"),
        ("legislature", "Legislature"),
        ("judiciary", "Judiciary"),
        ("federalism", "Federalism"),
        ("amendment", "Constitutional Amendment"),
        ("jr", "Judicial Review"),
        ("rights", "Rights"),
        ("emergency", "Emergency Powers"),
        ("philosophy", "Constitutional Philosophy"),
    ]
    india_points = [f"**{label}:** {INDIA_COMPARE_BASE[key]}" for key, label in labels]
    them_points = [f"**{label}:** {them[key]}" for key, label in labels]
    return {
        "id": f"wc-{country_id}-vs-india",
        "type": "comparison",
        "title": f"Constitution of India vs Constitution of {country_heading}",
        "columns": [
            {"id": "india", "heading": "India", "points": india_points},
            {"id": country_id, "heading": country_heading, "points": them_points},
        ],
    }


COUNTRY_PILLARS = [
    {
        "id": "usa",
        "articles": "pp. 949–952",
        "label": "United States",
        "slug": "wc-usa",
        "detail": "Oldest written · Presidential · Federal · Bill of Rights",
        "tone": "teal",
    },
    {
        "id": "britain",
        "articles": "pp. 953–957",
        "label": "United Kingdom",
        "slug": "wc-britain",
        "detail": "Unwritten · Parliamentary · Unitary · Sovereignty of Parliament",
        "tone": "olive",
    },
    {
        "id": "france",
        "articles": "pp. 957–961",
        "label": "France",
        "slug": "wc-france",
        "detail": "Fifth Republic · Quasi-presidential · Constitutional Council",
        "tone": "gold",
    },
    {
        "id": "japan",
        "articles": "pp. 961–965",
        "label": "Japan",
        "slug": "wc-japan",
        "detail": "Art. 9 renunciation of war · Never amended · JR in Constitution",
        "tone": "orange",
    },
    {
        "id": "ussr",
        "articles": "pp. 965–968",
        "label": "USSR (1977)",
        "slug": "wc-ussr",
        "detail": "Socialist federal · Presidium · CPSU · FRs + FDs",
        "tone": "terracotta",
    },
    {
        "id": "russia",
        "articles": "pp. 968–969",
        "label": "Russia (1993)",
        "slug": "wc-russia",
        "detail": "Multi-party · Strong President · Constitutional Court",
        "tone": "maroon",
    },
    {
        "id": "china",
        "articles": "pp. 969–972",
        "label": "China",
        "slug": "wc-china",
        "detail": "1982 · CPC leadership · Unicameral NPC · Democratic centralism",
        "tone": "teal",
    },
    {
        "id": "switzerland",
        "articles": "pp. 972–979",
        "label": "Switzerland",
        "slug": "wc-switzerland",
        "detail": "Council of 7 · Direct democracy · Triple citizenship",
        "tone": "olive",
    },
]

HUB_EXTRA_PILLARS = [
    {
        "id": "sources",
        "articles": "Table 4.4",
        "label": "Sources Borrowed",
        "slug": "wc-sources-borrowed",
        "detail": "GoI 1935 + 10 constitutions → India’s provisions",
        "tone": "gold",
    },
    {
        "id": "master",
        "articles": "Revision",
        "label": "Master Comparison",
        "slug": "wc-master-table",
        "detail": "All 8 + India feature matrix",
        "tone": "orange",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "wc-passport-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Passport of world constitutions",
        "topic_label": "World Constitutions",
        "subject_label": "India as synthesis",
        "relation_label": "Protects you from",
        "protects_from": [
            "Memorising countries in isolation without India comparison",
            "Confusing presidential / parliamentary / hybrid / council models",
            "Mixing USSR 1977 with Russia 1993",
            "Treating Swiss Council as a cabinet or US President",
        ],
        "insight": (
            "Each constitution is a stamp: compare form, executive, federalism, "
            "rights, and amendment — then map what India borrowed."
        ),
    },
    {
        "id": "wc-entry-pillars",
        "type": "pillars",
        "title": "Eight systems + Sources + Master table",
        "items": COUNTRY_PILLARS + HUB_EXTRA_PILLARS,
    },
    {
        "id": "wc-hub-exam5",
        "type": "callout",
        "tone": "tip",
        "title": "Exam in 5 minutes — system sniff test",
        "body": (
            "**USA** = Presidential + federal + rigid written. "
            "**UK** = Unwritten + parliamentary sovereignty. "
            "**France** = Hybrid (strong President + PM responsible to Parliament). "
            "**Japan** = Parliamentary monarchy + Art. 9. "
            "**USSR** = Socialist federal + Presidium + CPSU. "
            "**Russia** = Strong President + Constitutional Court. "
            "**China** = CPC leadership + unicameral NPC. "
            "**Switzerland** = Council of 7 + direct democracy."
        ),
    },
]

# ---------------------------------------------------------------------------
# Country clusters
# ---------------------------------------------------------------------------

CLUSTERS = [
    {
        "title": "United States Constitution",
        "slug": "wc-usa",
        "sort_order": 1,
        "summary": (
            "Oldest written constitution (1787/1789) — presidential, federal, rigid, "
            "separation of powers, Bill of Rights, powerful Senate."
        ),
        "body": (
            "## Historical background\n"
            "- Framed **1787** (Philadelphia); in force **1789**; post-Revolution (1775–83).\n"
            "- Originally 13 states → **50 states + DC** today.\n\n"
            "## Identity card\n"
            "| Lens | USA |\n|---|---|\n"
            "| Form | Presidential republic |\n"
            "| Constitution | Written (Preamble + 7 Articles + 27 Amendments) |\n"
            "| Nature | Rigid (only 27 amendments since 1789) |\n"
            "| Structure | Federal — residuary with **states** |\n"
            "| Philosophy | Limited government, separation of powers, due process |\n\n"
            "## Political system & organs\n"
            "- **Executive:** President = head of state + government; fixed 4-year term; "
            "Cabinet/Kitchen Cabinet advisory; no membership in Congress.\n"
            "- **Legislature:** Congress — Senate (100, 6 yrs) + HoR (435, 2 yrs); "
            "Senate = most powerful upper house in the world.\n"
            "- **Judiciary:** Supreme Court + inferior courts; judicial review (ultra vires).\n"
            "- **Federalism:** Limited enumerated Centre powers; each state has own constitution, "
            "legislature, governor, supreme court.\n"
            "- **Amendment:** (i) 2/3 both Houses + 3/4 states; or (ii) convention on petition of 2/3 states + 3/4 ratification.\n"
            "- **Rights:** Bill of Rights (first 10 Amendments, 1791); life, liberty, property — due process.\n"
            "- **Emergency / local / elections:** No Indian-style Art. 352 catalogue in book focus; "
            "states run local government; President via **Electoral College (538; need 270)**.\n\n"
            "### President — exam spine\n"
            "- Quals: natural-born; **35**; 14 yrs residence.\n"
            "- Term: 4 yrs; 22nd Amendment → max **10 yrs** / elected twice.\n"
            "- Removal: Impeachment (HoR majority → Senate 2/3; CJ presides).\n"
            "- Powers: enforce laws, CIC, appointments, treaties (Senate), pardon, "
            "qualified + **pocket veto**, messages, special sessions, budget, executive orders.\n\n"
            "## Unique features\n"
            "Oldest written; checks & balances; Kitchen Cabinet; pocket veto; dual citizenship possible "
            "(contrast India single citizenship).\n\n"
            "## Advantages / limitations\n"
            "- **+** Stability of tenure; clear separation; strong rights culture; federal laboratories.\n"
            "- **−** Gridlock; rigid amendment; Electoral College quirks; no collective responsibility.\n\n"
            "## Current relevance & UPSC\n"
            "Benchmark for presidential vs parliamentary, judicial review origin debates, "
            "impeachment/VP borrowings, due process vs procedure established by law."
        ),
        "articles": [
            ("US Constitution 1787", "Oldest existing written constitution; in force 1789."),
            ("Bill of Rights 1791", "First ten Amendments — model for Fundamental Rights."),
            ("22nd Amendment 1951", "Presidential term limit — max ten years."),
        ],
        "visual_blocks": [
            india_vs(
                "usa",
                "United States",
                {
                    "form": "Presidential republic — single real executive",
                    "executive": "President = head of state + government; fixed tenure; not responsible to Congress",
                    "legislature": "Bicameral Congress; Senate most powerful upper house; fixed terms",
                    "judiciary": "Separate federal judiciary; JR via practice (Marbury tradition)",
                    "federalism": "True federal; residuary with **states**; dual constitutions",
                    "amendment": "Very rigid — 2/3 Congress + 3/4 states (or convention route)",
                    "jr": "Strong JR; Constitution supreme; ultra vires doctrine",
                    "rights": "Bill of Rights; due process of law",
                    "emergency": "No Indian-style three emergencies; wartime & statute-based powers",
                    "philosophy": "Limited government, individualism, separation of powers",
                },
            ),
            {
                "id": "wc-usa-features",
                "type": "pillars",
                "title": "Nine salient features (revision)",
                "items": [
                    {
                        "id": "written",
                        "articles": "F1",
                        "label": "Written",
                        "slug": "wc-usa",
                        "detail": "Oldest written; Preamble + 7 Arts + 27 Amends",
                        "tone": "teal",
                    },
                    {
                        "id": "rigid",
                        "articles": "F2",
                        "label": "Rigid",
                        "slug": "wc-usa",
                        "detail": "Special amendment; only 27 times since 1789",
                        "tone": "olive",
                    },
                    {
                        "id": "federal",
                        "articles": "F3",
                        "label": "Federal",
                        "slug": "wc-usa",
                        "detail": "First modern federation; residuary → states",
                        "tone": "gold",
                    },
                    {
                        "id": "pres",
                        "articles": "F4",
                        "label": "Presidential",
                        "slug": "wc-usa",
                        "detail": "Fixed tenure; no dissolution of HoR",
                        "tone": "orange",
                    },
                    {
                        "id": "sep",
                        "articles": "F5–6",
                        "label": "Separation + Checks",
                        "slug": "wc-usa",
                        "detail": "Arts I–III; veto, confirmation, JR",
                        "tone": "terracotta",
                    },
                    {
                        "id": "bor",
                        "articles": "F7–9",
                        "label": "JR + Bill of Rights + Bicameral",
                        "slug": "wc-usa",
                        "detail": "Supremacy; first BoR; powerful Senate",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "wc-usa-electoral",
                "type": "flowchart",
                "title": "US Presidential election path",
                "root": "people",
                "steps": [
                    {
                        "id": "people",
                        "label": "People elect Presidential Electors",
                        "detail": "Per state = Congressional seats + 3 for DC → 538",
                        "options": [
                            {"label": "Electors vote", "next": "college"},
                        ],
                    },
                    {
                        "id": "college",
                        "label": "Electoral College votes",
                        "detail": "Need 270 to win; college dissolves after election",
                        "options": [
                            {"label": "≥270", "next": "president"},
                            {"label": "No majority", "next": "hor"},
                        ],
                    },
                    {
                        "id": "hor",
                        "label": "House of Representatives decides",
                        "detail": "From top 3 electoral-college candidates (1800, 1824, 1876)",
                    },
                    {
                        "id": "president",
                        "label": "President inaugurated",
                        "detail": "Term begins 20 January; max 2 elections / 10 years",
                    },
                ],
            },
        ],
    },
    {
        "title": "British Constitution",
        "slug": "wc-britain",
        "sort_order": 2,
        "summary": (
            "Mother of Constitutions — unwritten, flexible, unitary, parliamentary "
            "sovereignty, Rule of Law, constitutional monarchy, Cabinet/Shadow Cabinet."
        ),
        "body": (
            "## Historical background\n"
            "- UK of Great Britain and Northern Ireland; evolved over centuries.\n"
            "- Blend of monarchy, aristocracy, democracy — **mother of Constitutions**.\n\n"
            "## Identity card\n"
            "| Lens | Britain |\n|---|---|\n"
            "| Form | Parliamentary constitutional monarchy |\n"
            "| Constitution | **Unwritten / evolved** |\n"
            "| Nature | Flexible (ordinary legislation can change ‘constitution’) |\n"
            "| Structure | Unitary |\n"
            "| Philosophy | Parliamentary sovereignty + Rule of Law (Dicey) |\n\n"
            "## Sources of the unwritten Constitution\n"
            "1. **Conventions** (e.g. King acts on ministers’ advice; PM from Commons majority)\n"
            "2. **Great Charters** — Magna Carta 1215, Petition of Right 1628, Bill of Rights 1689\n"
            "3. **Statutes**\n"
            "4. **Common Law**\n"
            "5. **Commentaries** — Dicey, Bagehot, Blackstone\n\n"
            "## Political system & organs\n"
            "- **Executive:** King/Queen (Crown) ceremonial; Cabinet = real executive; PM dominant "
            "(‘prime ministerial government’ vs older *primus inter pares*).\n"
            "- **Legislature:** Lords (~677 appointed) + Commons (659 elected) — Commons dominant.\n"
            "- **Judiciary:** Independent; **no** judicial review striking down Acts of Parliament "
            "(sovereignty of Parliament).\n"
            "- **Federalism:** Unitary — local authorities subordinate.\n"
            "- **Amendment:** Flexible — Parliament can alter by ordinary majority.\n"
            "- **Rights:** Evolved; HRA era beyond classic Laxmikanth list — book stresses Rule of Law.\n"
            "- **Elections:** Universal adult franchise; Commons life normally fixed by statute/convention.\n\n"
            "### Cabinet cluster\n"
            "- PM + ~20 senior ministers; Attorney-General etc. **not** in Cabinet.\n"
            "- **Privy Council** (~330) — historic advisory body; Lord President.\n"
            "- **Shadow Cabinet** — official opposition parallel ministry; Jennings: Leader of Opposition = alternative PM.\n\n"
            "## Unique features\n"
            "Unwritten; absolute parliamentary sovereignty; Shadow Cabinet; Crown vs King distinction.\n\n"
            "## Advantages / limitations\n"
            "- **+** Flexibility; responsible government; continuity.\n"
            "- **−** No entrenched rights shield like US/India; executive dominance risk.\n\n"
            "## Current relevance & UPSC\n"
            "Core of India’s parliamentary borrowings; contrast sovereignty (UK) vs constitutional "
            "supremacy + JR (India/USA)."
        ),
        "articles": [
            ("Magna Carta 1215", "Great Charter — early limit on absolute monarchy."),
            ("Bill of Rights 1689", "Landmark statute in British constitutional evolution."),
            ("Dicey — Rule of Law", "Supremacy of law; equality before law; constitution as result of rights."),
        ],
        "visual_blocks": [
            india_vs(
                "britain",
                "United Kingdom",
                {
                    "form": "Parliamentary constitutional monarchy",
                    "executive": "Crown ceremonial; Cabinet/PM real; Shadow Cabinet unique",
                    "legislature": "Lords + Commons; Commons supreme; oldest popular legislature",
                    "judiciary": "Independent but cannot void Acts of Parliament",
                    "federalism": "Unitary",
                    "amendment": "Flexible — ordinary legislation",
                    "jr": "No JR of parliamentary statutes (sovereignty)",
                    "rights": "Evolved / statutory; Rule of Law culture",
                    "emergency": "Statutory & prerogative powers — not Indian three-fold scheme",
                    "philosophy": "Parliamentary sovereignty + Rule of Law",
                },
            ),
            {
                "id": "wc-britain-features",
                "type": "pillars",
                "title": "Eight salient features",
                "items": [
                    {
                        "id": "unwritten",
                        "articles": "F1",
                        "label": "Unwritten",
                        "slug": "wc-britain",
                        "detail": "Conventions, charters, statutes, common law, commentaries",
                        "tone": "teal",
                    },
                    {
                        "id": "flex",
                        "articles": "F2",
                        "label": "Flexible",
                        "slug": "wc-britain",
                        "detail": "No special amendment procedure",
                        "tone": "olive",
                    },
                    {
                        "id": "unitary",
                        "articles": "F3",
                        "label": "Unitary",
                        "slug": "wc-britain",
                        "detail": "Single supreme centre",
                        "tone": "gold",
                    },
                    {
                        "id": "parl",
                        "articles": "F4",
                        "label": "Parliamentary",
                        "slug": "wc-britain",
                        "detail": "Responsible Cabinet; Commons confidence",
                        "tone": "orange",
                    },
                    {
                        "id": "sov",
                        "articles": "F5–6",
                        "label": "Sovereignty + Rule of Law",
                        "slug": "wc-britain",
                        "detail": "Parliament supreme; Dicey’s three implications",
                        "tone": "terracotta",
                    },
                    {
                        "id": "monarchy",
                        "articles": "F7–8",
                        "label": "Monarchy + Bicameral",
                        "slug": "wc-britain",
                        "detail": "Constitutional monarchy; Lords & Commons",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "wc-britain-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Trap — India ≠ Britain",
                "body": (
                    "India borrowed Cabinet system but is a **republic** with a written Constitution, "
                    "**judicial review**, limited Parliament, and **no** official Shadow Cabinet. "
                    "UK: parliamentary sovereignty; India: constitutional supremacy + basic structure."
                ),
            },
        ],
    },
    {
        "title": "French Constitution (Fifth Republic)",
        "slug": "wc-france",
        "sort_order": 3,
        "summary": (
            "1958 Gaullist Constitution — written, rigid, unitary, quasi-presidential/"
            "quasi-parliamentary, rationalised Parliament, Constitutional Council."
        ),
        "body": (
            "## Historical background\n"
            "- Frequent constitution changes since 1789 Revolution (~every 12 years historically).\n"
            "- **Fifth Republic (1958)** under de Gaulle — strong stable executive.\n"
            "- Motto: **Liberty, Equality, Fraternity**; indivisible, secular, democratic, social republic.\n\n"
            "## Identity card\n"
            "| Lens | France |\n|---|---|\n"
            "| Form | Hybrid — quasi-presidential + quasi-parliamentary |\n"
            "| Constitution | Written (Preamble + chapters; see Table 95.1) |\n"
            "| Nature | Rigid (60% both Houses **or** referendum; republican form unamendable) |\n"
            "| Structure | Unitary (more unitary than Britain) |\n"
            "| Philosophy | Republicanism; LEF; strong presidency |\n\n"
            "## Political system & organs\n"
            "- **Executive:** Directly elected President (since 1962) + PM/Council of Ministers "
            "responsible to Parliament; ministers **cannot** be MPs.\n"
            "- **Legislature:** National Assembly (577, 5 yrs direct) + Senate (348, 6 yrs indirect); "
            "Assembly dominant; **rationalised Parliament** (limited law domain; decrees elsewhere).\n"
            "- **Judiciary / watchdog:** Constitutional Council (9 members, 9-year term) — advisory, "
            "not fully binding like a US SC.\n"
            "- **Parties:** Constitutionally recognised; must respect sovereignty & democracy.\n"
            "- **President powers (high-yield):** appoint/dismiss PM & ministers; CIC; treaties; "
            "referendum; emergency measures; dissolve National Assembly (limits: not twice in 12 months; "
            "not during emergency).\n"
            "- **Election:** Absolute majority; two-ballot runoff if needed.\n"
            "- **Tenure:** 5 years; max **two consecutive** terms (2008); impeachment for high treason via High Court.\n\n"
            "## Unique features\n"
            "Hybrid executive; rationalised Parliament; Constitutional Council; unamendable republic clause.\n\n"
            "## Advantages / limitations\n"
            "- **+** Stability vs Fourth Republic; clear national leadership.\n"
            "- **−** Cohabitation tensions; weak Parliament; advisory Council vs strong JR.\n\n"
            "## Current relevance & UPSC\n"
            "India borrowed **Republic** + LEF ideals in Preamble — not the French hybrid executive."
        ),
        "articles": [
            ("Fifth Republic 1958", "Present French Constitution — de Gaulle."),
            ("1962 amendment", "Direct election of President."),
            ("Constitutional Council", "9 members × 9 years — constitutional watchdog (advisory)."),
        ],
        "visual_blocks": [
            india_vs(
                "france",
                "France",
                {
                    "form": "Hybrid (strong President + responsible PM/Cabinet)",
                    "executive": "Directly elected President dominates; PM leads government; ministers not MPs",
                    "legislature": "Bicameral; rationalised (restricted) law-making",
                    "judiciary": "Constitutional Council (advisory) + judicial authority",
                    "federalism": "Unitary — local units by central convenience",
                    "amendment": "60% both Houses or referendum; republican form locked",
                    "jr": "Council reviews conformity — opinion not fully binding",
                    "rights": "Republican rights tradition; LEF motto",
                    "emergency": "Special presidential emergency powers after consulting key offices",
                    "philosophy": "Liberty, Equality, Fraternity; secular social republic",
                },
            ),
            {
                "id": "wc-france-features",
                "type": "pillars",
                "title": "Eight salient features",
                "items": [
                    {
                        "id": "written",
                        "articles": "F1",
                        "label": "Written + LEF",
                        "slug": "wc-france",
                        "detail": "Fifth Republic text; Liberty Equality Fraternity",
                        "tone": "teal",
                    },
                    {
                        "id": "rigid",
                        "articles": "F2",
                        "label": "Rigid",
                        "slug": "wc-france",
                        "detail": "60% or referendum; no monarchy path",
                        "tone": "olive",
                    },
                    {
                        "id": "unitary",
                        "articles": "F3",
                        "label": "Unitary",
                        "slug": "wc-france",
                        "detail": "More unitary than Britain",
                        "tone": "gold",
                    },
                    {
                        "id": "hybrid",
                        "articles": "F4",
                        "label": "Quasi-Pres + Parl",
                        "slug": "wc-france",
                        "detail": "Strong President + responsible ministers",
                        "tone": "orange",
                    },
                    {
                        "id": "rat",
                        "articles": "F5–6",
                        "label": "Bicameral + Rationalised",
                        "slug": "wc-france",
                        "detail": "Limited parliamentary domain",
                        "tone": "terracotta",
                    },
                    {
                        "id": "cc",
                        "articles": "F7–8",
                        "label": "Council + Parties",
                        "slug": "wc-france",
                        "detail": "Constitutional Council; parties recognised",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "wc-france-president-timeline",
                "type": "timeline",
                "title": "French President — amended rules (Table 95.2)",
                "events": [
                    {
                        "id": "1958",
                        "year": 1958,
                        "label": "Original",
                        "detail": "Indirect election; 7-year term; no term limit",
                    },
                    {
                        "id": "1962",
                        "year": 1962,
                        "label": "Direct election",
                        "detail": "Referendum amendment — universal suffrage",
                    },
                    {
                        "id": "2000",
                        "year": 2000,
                        "label": "Five-year term",
                        "detail": "Tenure cut from seven to five years",
                    },
                    {
                        "id": "2008",
                        "year": 2008,
                        "label": "Two consecutive terms",
                        "detail": "Max two consecutive presidential terms",
                    },
                ],
            },
        ],
    },
    {
        "title": "Japanese Constitution",
        "slug": "wc-japan",
        "sort_order": 4,
        "summary": (
            "1947 MacArthur/Showa Constitution — written, rigid (never amended), unitary, "
            "parliamentary monarchy, Art. 9 renunciation of war, constitutional JR."
        ),
        "body": (
            "## Historical background\n"
            "- Meiji Constitution 1889–1947 (autocratic monarchy).\n"
            "- Post-WWII Allied Occupation; **MacArthur** direction; operative **1947** "
            "(MacArthur / Showa Constitution). Emperor Hirohito; PM Shidehara.\n\n"
            "## Identity card\n"
            "| Lens | Japan |\n|---|---|\n"
            "| Form | Parliamentary constitutional monarchy |\n"
            "| Constitution | Written (Preamble + 103 Articles / 11 chapters) |\n"
            "| Nature | Rigid — Diet 2/3 + popular referendum; **never amended** |\n"
            "| Structure | Unitary (Tokyo centre; provinces subordinate) |\n"
            "| Philosophy | Popular sovereignty, peace, democracy |\n\n"
            "## Political system & organs\n"
            "- **Executive:** Emperor = symbol only; Cabinet (PM + up to 20) real executive; "
            "collective responsibility to Diet.\n"
            "- **Legislature:** Diet — House of Councillors (252, 6 yrs) + House of Representatives "
            "(512, 4 yrs); Diet = highest organ / sole law-maker.\n"
            "- **Judiciary:** Supreme Court with **JR written into Constitution** (unlike US practice origin).\n"
            "- **Rights:** Arts 10–40 — equality, freedom, religion, property, economic, education, "
            "cultural, constitutional remedies — ‘eternal and inviolate’.\n"
            "- **Art. 9:** Renunciation of war / war potential; self-defence forces justified as inherent defence.\n"
            "- **Local government:** Chapters on local self-government (Arts 92–95).\n\n"
            "### Japan ≠ Britain (4 differences)\n"
            "1. PM chosen by Diet, appointed by Emperor (UK: sovereign chooses/appoints).\n"
            "2. Ministers appointed by PM (UK: by Crown).\n"
            "3. PM can remove ministers at will (UK: traditionally constrained).\n"
            "4. Only a **majority** of ministers need be Diet members (UK: all must be Parliament members).\n\n"
            "## Unique features\n"
            "Art. 9; never amended; JR from text; blend of US rights + British cabinet pattern.\n\n"
            "## Advantages / limitations\n"
            "- **+** Peace clause; popular sovereignty; elaborate rights.\n"
            "- **−** Amendment near-impossible; Art. 9 political controversy; Emperor symbolism debates.\n\n"
            "## Current relevance & UPSC\n"
            "India borrowed **procedure established by law** from Japan — contrast US due process."
        ),
        "articles": [
            ("Japanese Constitution 1947", "MacArthur / Showa Constitution — still unamended."),
            ("Article 9", "Renunciation of war as sovereign right of the nation."),
            ("Arts 10–40", "Rights and duties of the people."),
        ],
        "visual_blocks": [
            india_vs(
                "japan",
                "Japan",
                {
                    "form": "Parliamentary constitutional monarchy",
                    "executive": "Emperor ceremonial; Cabinet/PM real; Diet designates PM",
                    "legislature": "Bicameral Diet — highest organ of state power",
                    "judiciary": "SC with JR **from Constitution**",
                    "federalism": "Unitary",
                    "amendment": "Diet 2/3 + popular referendum — never used",
                    "jr": "Explicit constitutional JR (vs US practice-based origin)",
                    "rights": "Elaborate Bill-of-Rights style catalogue (Arts 10–40)",
                    "emergency": "No Indian three-emergency model in book focus",
                    "philosophy": "Peace + popular sovereignty; renunciation of war",
                },
            ),
            {
                "id": "wc-japan-features",
                "type": "pillars",
                "title": "Nine salient features",
                "items": [
                    {
                        "id": "written",
                        "articles": "F1",
                        "label": "Written blend",
                        "slug": "wc-japan",
                        "detail": "US + British blend; people sovereignty",
                        "tone": "teal",
                    },
                    {
                        "id": "rigid",
                        "articles": "F2",
                        "label": "Rigid / unamended",
                        "slug": "wc-japan",
                        "detail": "Still reads as in 1947",
                        "tone": "olive",
                    },
                    {
                        "id": "unitary",
                        "articles": "F3",
                        "label": "Unitary",
                        "slug": "wc-japan",
                        "detail": "Provinces subordinate to Tokyo",
                        "tone": "gold",
                    },
                    {
                        "id": "parl",
                        "articles": "F4–5",
                        "label": "Parliamentary monarchy",
                        "slug": "wc-japan",
                        "detail": "Emperor symbol; Cabinet real",
                        "tone": "orange",
                    },
                    {
                        "id": "jr",
                        "articles": "F6–7",
                        "label": "JR + Rights",
                        "slug": "wc-japan",
                        "detail": "JR in text; Arts 10–40",
                        "tone": "terracotta",
                    },
                    {
                        "id": "art9",
                        "articles": "F8–9",
                        "label": "Art. 9 + Bicameral",
                        "slug": "wc-japan",
                        "detail": "Renounce war; Diet bicameral",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "wc-japan-art9",
                "type": "callout",
                "tone": "tip",
                "title": "Art. 9 mnemonic — Peace forever",
                "body": (
                    "**R**enounce war · **N**o war potential · **N**o belligerency — but "
                    "**self-defence forces** allowed as inherent right of every state. "
                    "Only modern state with constitutional renunciation of war."
                ),
            },
        ],
    },
    {
        "title": "Soviet Constitution (1977)",
        "slug": "wc-ussr",
        "sort_order": 5,
        "summary": (
            "Brezhnev Constitution — first socialist constitutional tradition; federal "
            "‘Federation of Federations’; Presidium; CPSU monopoly; FRs + FDs."
        ),
        "body": (
            "## Historical background\n"
            "- USSR after 1917 Bolshevik Revolution (Lenin); Marxism–Leninism.\n"
            "- Constitutions: 1918, 1924, 1936 (Stalin), **1977 (Brezhnev)**.\n"
            "- Collapsed/disintegrated **1989–91**.\n\n"
            "## Identity card\n"
            "| Lens | USSR 1977 |\n|---|---|\n"
            "| Form | Socialist parliamentary (formal) + CPSU monopoly |\n"
            "| Constitution | Written (20 chapters, 174 Articles, 9 parts) |\n"
            "| Nature | Rigid — 2/3 each House of Supreme Soviet |\n"
            "| Structure | Federal — 15 Union Republics; residuary to units; right to secede |\n"
            "| Philosophy | Marxism–Leninism; socialist ownership |\n\n"
            "## Political system & organs\n"
            "- **Legislature:** Supreme Soviet — Soviet of the Union + Soviet of Nationalities "
            "(750 each; equal powers).\n"
            "- **Executive:** Council of Ministers (Premier) highest executive/admin authority; "
            "responsible to Supreme Soviet.\n"
            "- **Presidium:** 39-member standing committee — **collegial/plural executive**; "
            "Chairman = formal head of state; ‘20th Century Innovation’.\n"
            "- **Party:** CPSU = leading & guiding force (one-party dictatorship in practice).\n"
            "- **Democratic centralism:** electiveness + accountability + lower bodies obey higher.\n"
            "- **Rights:** 18 listed — socialist form; not to harm society/state.\n"
            "- **Duties:** 11 listed — inseparable from rights.\n"
            "- **Federal detail:** Autonomous republics/regions/areas → ‘Federation of Federations’.\n\n"
            "## Unique features\n"
            "Presidium; CPSU constitutional monopoly; secession right; socialist FR/FD model.\n\n"
            "## Advantages / limitations\n"
            "- **+** Social/economic rights catalogue; formal federal equality of houses.\n"
            "- **−** Party dictatorship; rights subordinated to state/society; collapsed system.\n\n"
            "## Current relevance & UPSC\n"
            "India borrowed **Fundamental Duties** + Preamble ideal of justice (social, economic, political)."
        ),
        "articles": [
            ("Soviet Constitution 1977", "Brezhnev Constitution — last USSR constitution."),
            ("Presidium", "Collegial / plural executive — Standing Committee of Supreme Soviet."),
            ("CPSU clause", "Leading and guiding force of Soviet society."),
        ],
        "visual_blocks": [
            india_vs(
                "ussr",
                "USSR (1977)",
                {
                    "form": "Formal parliamentary socialist + CPSU monopoly",
                    "executive": "Council of Ministers + Collegial Presidium (plural head of state)",
                    "legislature": "Equal bicameral Supreme Soviet (750 + 750)",
                    "judiciary": "Socialist legality under party-state (not liberal JR model)",
                    "federalism": "15 republics; residuary to units; right to secede; sub-federations",
                    "amendment": "2/3 each House of Supreme Soviet",
                    "jr": "No liberal judicial supremacy like USA/India",
                    "rights": "Extensive socialist FRs + 11 FDs; limited by state/society interest",
                    "emergency": "Party-state control — not Indian emergency catalogue",
                    "philosophy": "Marxism–Leninism; socialist ownership; democratic centralism",
                },
            ),
            {
                "id": "wc-ussr-features",
                "type": "pillars",
                "title": "Eleven features — scan list",
                "items": [
                    {
                        "id": "written",
                        "articles": "1–2",
                        "label": "Written + Rigid",
                        "slug": "wc-ussr",
                        "detail": "174 Articles; 2/3 amendment",
                        "tone": "teal",
                    },
                    {
                        "id": "socialist",
                        "articles": "3",
                        "label": "Socialist",
                        "slug": "wc-ussr",
                        "detail": "State/collective ownership base",
                        "tone": "olive",
                    },
                    {
                        "id": "federal",
                        "articles": "4",
                        "label": "Federal",
                        "slug": "wc-ussr",
                        "detail": "Federation of Federations",
                        "tone": "gold",
                    },
                    {
                        "id": "parl",
                        "articles": "5–7",
                        "label": "Parl + Bicameral + Presidium",
                        "slug": "wc-ussr",
                        "detail": "Council of Ministers; equal houses; plural executive",
                        "tone": "orange",
                    },
                    {
                        "id": "party",
                        "articles": "8–9",
                        "label": "CPSU + Dem. Centralism",
                        "slug": "wc-ussr",
                        "detail": "One-party; hierarchical obedience",
                        "tone": "terracotta",
                    },
                    {
                        "id": "frfd",
                        "articles": "10–11",
                        "label": "FRs + FDs",
                        "slug": "wc-ussr",
                        "detail": "18 rights · 11 duties (socialist form)",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "wc-ussr-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Do not mix with Russia 1993",
                "body": (
                    "USSR = socialist federal + Presidium + CPSU. "
                    "Russia 1993 = multi-party liberal-democratic order + strong President + "
                    "Constitutional Court. Treat as **continuity/rupture**, not the same system."
                ),
            },
        ],
    },
    {
        "title": "Russian Constitution (1993)",
        "slug": "wc-russia",
        "sort_order": 6,
        "summary": (
            "Post-USSR constitution (20 Dec 1993) — multi-ethnic federal republic, "
            "strong President, bicameral Federal Assembly, Constitutional Court."
        ),
        "body": (
            "## Historical background\n"
            "- Largest ex-USSR unit (~75% area, ~50% population).\n"
            "- New Constitution **20 December 1993** after USSR dissolution (Dec 1991).\n\n"
            "## Identity card (10 book bullets → revision card)\n"
            "| Lens | Russia 1993 |\n|---|---|\n"
            "| Form | Federal presidential-leaning republic |\n"
            "| Constitution | Written (1993) |\n"
            "| Structure | Federal — republics, krais, oblasts, okrugs, federal cities, Jewish AR |\n"
            "| Political order | Liberal-democratic; multi-party; free elections |\n"
            "| Separation | Legislature, executive, judiciary independent |\n\n"
            "## Organs\n"
            "- **Legislature:** Federal Assembly — Federation Council (178; 2 per unit) + "
            "State Duma (450; 4 yrs direct).\n"
            "- **Executive:** President = head of state, executive head, CIC; 4-year direct election "
            "(as in book); appoints PM & ministers; can dismiss them.\n"
            "- **Judiciary:** 19-member Constitutional Court — reviews presidential decrees, "
            "government orders, Federal Assembly laws.\n"
            "- **Removal:** Impeachment for high treason/grave crime — 2/3 both Houses.\n"
            "- **Rights:** Guarantees FRs; discards earlier totalitarian system.\n\n"
            "## Unique features vs USSR\n"
            "Multi-party vs CPSU; individual President vs Presidium; Constitutional Court; "
            "liberal-democratic vocabulary.\n\n"
            "## Advantages / limitations\n"
            "- **+** Formal rights & multi-party framework; constitutional court.\n"
            "- **−** Strong presidency can overshadow assembly; federal asymmetry complexity.\n\n"
            "## Current relevance & UPSC\n"
            "Compare rupture from Soviet model; India still cites **Soviet** (not 1993 Russia) "
            "for Fundamental Duties / Preamble justice ideal."
        ),
        "articles": [
            ("Russian Constitution 1993", "Adopted 20 December 1993 after USSR dissolution."),
            ("Federal Assembly", "Federation Council (178) + State Duma (450)."),
            ("Constitutional Court", "19 members — constitutionality of decrees, orders, laws."),
        ],
        "visual_blocks": [
            india_vs(
                "russia",
                "Russia",
                {
                    "form": "Federal republic with strong presidency",
                    "executive": "President head of state + executive + CIC; appoints PM",
                    "legislature": "Bicameral Federal Assembly (Council + Duma)",
                    "judiciary": "19-member Constitutional Court for constitutionality review",
                    "federalism": "Complex federation of republics/territories/regions/areas/cities",
                    "amendment": "Special constitutional procedures (book lists features, not full Art. map)",
                    "jr": "Constitutional Court review of executive & legislative acts",
                    "rights": "Liberal-democratic FR guarantees (post-totalitarian)",
                    "emergency": "Presidential system with impeachment path — not Indian three emergencies",
                    "philosophy": "Sovereign multi-ethnic republic; separation of powers; multi-party",
                },
            ),
            {
                "id": "wc-russia-vs-ussr",
                "type": "comparison",
                "title": "USSR 1977 vs Russia 1993 (rupture)",
                "columns": [
                    {
                        "id": "ussr",
                        "heading": "USSR 1977",
                        "points": [
                            "Socialist constitution; CPSU monopoly",
                            "Presidium = collegial head of state",
                            "Equal bicameral Supreme Soviet (750+750)",
                            "Right to secede; Federation of Federations",
                            "Socialist FRs + FDs",
                        ],
                    },
                    {
                        "id": "rus",
                        "heading": "Russia 1993",
                        "points": [
                            "Liberal-democratic; multi-party elections",
                            "Single President as head of state/executive",
                            "Federation Council 178 + State Duma 450",
                            "Federal subjects without USSR secession model",
                            "FR guarantees; Constitutional Court",
                        ],
                    },
                ],
            },
            {
                "id": "wc-russia-note",
                "type": "callout",
                "tone": "note",
                "title": "Book depth note",
                "body": (
                    "Laxmikanth treats Russia briefly (10 bullets). For exams, master the "
                    "**continuity/rupture** table and the strong-President + Constitutional Court pair."
                ),
            },
        ],
    },
    {
        "title": "Chinese Constitution (1982)",
        "slug": "wc-china",
        "sort_order": 7,
        "summary": (
            "1982 Constitution — socialist, rigid, unitary multinational state, CPC leadership, "
            "unicameral NPC, democratic centralism, FRs limited by collective interest."
        ),
        "body": (
            "## Historical background\n"
            "- PRC 1949 (Mao / CPC). Constitutions: 1954, 1975, 1978, **1982** (present).\n"
            "- Drafted via National Constitution Revision Committee; nationwide discussion; "
            "promulgated 4 Dec 1982.\n\n"
            "## Identity card\n"
            "| Lens | China 1982 |\n|---|---|\n"
            "| Form | Socialist state — people’s democratic dictatorship |\n"
            "| Constitution | Written (Preamble + originally 138 Arts / 4 chapters) |\n"
            "| Nature | Rigid — NPC 2/3; proposal by Standing Committee or ≥1/5 deputies |\n"
            "| Structure | Unitary multinational state (Beijing centre) |\n"
            "| Defining feature | **CPC leadership** (Art. 1 / Preamble) |\n\n"
            "## Political system & organs\n"
            "- **Legislature:** Unicameral **NPC** (~3000; 5 yrs) — highest state organ; "
            "Standing Committee ~200 permanent.\n"
            "- **Executive:** State Council (Central People’s Government) headed by Premier — "
            "highest administrative organ; responsible to NPC. President ceremonial "
            "(elected by NPC, 5 yrs, age **45+**); not comparable to US President or Indian PM power.\n"
            "- **Party:** Multi-party cooperation **under CPC leadership**; ideological lineage through "
            "Xi Jinping Thought etc.\n"
            "- **Democratic centralism:** People’s congresses elected; admin/judicial organs created by "
            "and accountable to congresses.\n"
            "- **Rights:** 19 listed — must not undermine state/society/collective/others’ rights.\n"
            "- **Duties:** 7 listed (unity, law, motherland, defence, military/militia, taxes, work/education/family planning).\n\n"
            "## Unique features\n"
            "CPC as constitutional defining feature; unicameral giant NPC; ceremonial President + Premier system.\n\n"
            "## Advantages / limitations\n"
            "- **+** Formal social/economic rights; central coordination.\n"
            "- **−** Rights subordinated to collective/state; party primacy over competitive multiparty democracy.\n\n"
            "## Current relevance & UPSC\n"
            "Contrast India’s competitive multiparty democracy and justiciable FRs; "
            "compare FD catalogues (USSR/China vs India Art. 51A)."
        ),
        "articles": [
            ("Chinese Constitution 1982", "Fourth and present PRC constitution."),
            ("NPC", "Unicameral highest state organ of power (~3000 deputies)."),
            ("Art. 1 / Preamble", "CPC leadership as defining feature of socialism with Chinese characteristics."),
        ],
        "visual_blocks": [
            india_vs(
                "china",
                "China",
                {
                    "form": "Socialist republic under people’s democratic dictatorship + CPC leadership",
                    "executive": "Ceremonial President + Premier/State Council responsible to NPC",
                    "legislature": "Unicameral NPC + Standing Committee",
                    "judiciary": "People’s courts & procuratorates under people’s congresses framework",
                    "federalism": "Unitary multinational state",
                    "amendment": "NPC 2/3; proposal by Standing Committee or 1/5 deputies",
                    "jr": "No independent liberal JR like India/USA",
                    "rights": "Broad catalogue but limited by state/society/collective interest",
                    "emergency": "Centralised party-state — not Indian emergency articles model",
                    "philosophy": "Socialism with Chinese characteristics; democratic centralism",
                },
            ),
            {
                "id": "wc-china-features",
                "type": "pillars",
                "title": "Ten salient features",
                "items": [
                    {
                        "id": "written",
                        "articles": "F1–2",
                        "label": "Written + Rigid",
                        "slug": "wc-china",
                        "detail": "NPC 2/3 amendment path",
                        "tone": "teal",
                    },
                    {
                        "id": "socialist",
                        "articles": "F3",
                        "label": "Socialist",
                        "slug": "wc-china",
                        "detail": "People’s democratic dictatorship",
                        "tone": "olive",
                    },
                    {
                        "id": "unitary",
                        "articles": "F4",
                        "label": "Unitary",
                        "slug": "wc-china",
                        "detail": "Multinational; powers at Beijing",
                        "tone": "gold",
                    },
                    {
                        "id": "parl",
                        "articles": "F5–6",
                        "label": "Parl form + Unicameral",
                        "slug": "wc-china",
                        "detail": "State Council; NPC only",
                        "tone": "orange",
                    },
                    {
                        "id": "cpc",
                        "articles": "F7–8",
                        "label": "CPC + Dem. Centralism",
                        "slug": "wc-china",
                        "detail": "Leadership defining feature",
                        "tone": "terracotta",
                    },
                    {
                        "id": "frfd",
                        "articles": "F9–10",
                        "label": "FRs + FDs",
                        "slug": "wc-china",
                        "detail": "19 rights · 7 duties",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "wc-china-compare-heads",
                "type": "callout",
                "tone": "trap",
                "title": "Trap — Chinese President ≠ US President ≠ Indian PM",
                "body": (
                    "Chinese **President** is ceremonial (NPC-elected). Real admin leadership is "
                    "**Premier/State Council**, but authority is **not** comparable to Indian/British PM. "
                    "Overarching political leadership is the **CPC**."
                ),
            },
        ],
    },
    {
        "title": "Swiss Constitution",
        "slug": "wc-switzerland",
        "sort_order": 8,
        "summary": (
            "1999 Constitution (in force 2000) — federal cantons, unique Council of 7, "
            "equal bicameralism, direct democracy, triple citizenship, social goals."
        ),
        "body": (
            "## Historical background\n"
            "- Constitutions: **1848** (federal state), 1874, **1999** (in force 1 Jan 2000).\n"
            "- Adopted by Federal Assembly Dec 1998; approved by people & cantons Apr 1999.\n\n"
            "## Identity card\n"
            "| Lens | Switzerland |\n|---|---|\n"
            "| Form | Federal council (collegial) republic |\n"
            "| Constitution | Written (Preamble + 196 Articles / 6 titles) |\n"
            "| Nature | Rigid — total/partial revision; people + cantons approval |\n"
            "| Structure | Federal — 26 cantons (20 full + 6 half); residuary to cantons |\n"
            "| Philosophy | Direct democracy; consensus; federal diversity |\n\n"
            "## Political system & organs\n"
            "- **Executive:** Federal Council — **7 members**, equal authority; President = "
            "*primus inter pares* for 1 year (no consecutive re-election as President). "
            "Not removable by no-confidence or impeachment. Non-partisan collegial style. "
            "C.F. Strong: combines merits of parliamentary + presidential.\n"
            "- **Legislature:** Federal Assembly — Council of States (46) + National Council (200 PR). "
            "**Equal powers** — unique upper house equality (Strong).\n"
            "- **Direct democracy:** Mandatory & optional referendum; initiative (100,000 voters) "
            "for constitutional revision at federal level.\n"
            "- **Citizenship:** **Triple** — commune + canton + federation.\n"
            "- **Rights:** 25 listed (dignity, equality, life, privacy, religion, expression, etc.).\n"
            "- **Social goals:** 7 goals — **no direct enforceable right** to benefits (DPSP-like).\n"
            "- **Half cantons:** 1 seat in Council of States (vs 2); half vote on constitutional revision.\n\n"
            "## Unique features\n"
            "Council model; equal bicameralism; direct democracy; triple citizenship; social goals.\n\n"
            "## Advantages / limitations\n"
            "- **+** Stability, inclusion, citizen participation, cantonal autonomy.\n"
            "- **−** Slow decision-making; complexity of referendums; half-canton asymmetries.\n\n"
            "## Current relevance & UPSC\n"
            "Classic ‘neither parliamentary nor presidential’ executive; compare Swiss social goals "
            "to Indian DPSPs (non-justiciable)."
        ),
        "articles": [
            ("Swiss Constitution 1999", "Third constitution; in force 1 January 2000."),
            ("Federal Council", "Seven-member collegial executive — unique council model."),
            ("Initiative & Referendum", "Direct democracy devices at federal level."),
        ],
        "visual_blocks": [
            india_vs(
                "switzerland",
                "Switzerland",
                {
                    "form": "Federal council republic (collegial executive)",
                    "executive": "7 equal Federal Councillors; rotating ceremonial President",
                    "legislature": "Equal bicameral Federal Assembly (States 46 + National 200)",
                    "judiciary": "Federal Supreme Court & other judicial authorities",
                    "federalism": "26 cantons; residuary with cantons; half-canton quirks",
                    "amendment": "Total/partial revision — needs people + cantons",
                    "jr": "Constitutional review within federal judicial framework",
                    "rights": "Elaborate FRs + non-justiciable social goals",
                    "emergency": "Emergency federal acts subject to referendum rules",
                    "philosophy": "Direct democracy; consensus; triple citizenship",
                },
            ),
            {
                "id": "wc-swiss-features",
                "type": "pillars",
                "title": "Nine salient features",
                "items": [
                    {
                        "id": "written",
                        "articles": "F1–2",
                        "label": "Written + Rigid",
                        "slug": "wc-switzerland",
                        "detail": "People + cantons for revision",
                        "tone": "teal",
                    },
                    {
                        "id": "federal",
                        "articles": "F3",
                        "label": "Federal cantons",
                        "slug": "wc-switzerland",
                        "detail": "26 cantons; residuary to units",
                        "tone": "olive",
                    },
                    {
                        "id": "council",
                        "articles": "F4",
                        "label": "Council of 7",
                        "slug": "wc-switzerland",
                        "detail": "Plural executive; Strong’s hybrid merits",
                        "tone": "gold",
                    },
                    {
                        "id": "equal",
                        "articles": "F5",
                        "label": "Equal bicameral",
                        "slug": "wc-switzerland",
                        "detail": "Upper = lower powers",
                        "tone": "orange",
                    },
                    {
                        "id": "dd",
                        "articles": "F6",
                        "label": "Direct democracy",
                        "slug": "wc-switzerland",
                        "detail": "Referendum + initiative",
                        "tone": "terracotta",
                    },
                    {
                        "id": "triple",
                        "articles": "F7–9",
                        "label": "Triple + Rights + Goals",
                        "slug": "wc-switzerland",
                        "detail": "Commune–canton–federation; FRs; social goals",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "wc-swiss-direct",
                "type": "flowchart",
                "title": "Swiss direct democracy — which tool?",
                "root": "q",
                "steps": [
                    {
                        "id": "q",
                        "label": "What is being decided?",
                        "options": [
                            {"label": "Constitutional change", "next": "init_ref"},
                            {"label": "Federal act / treaty class", "next": "opt_ref"},
                        ],
                    },
                    {
                        "id": "init_ref",
                        "label": "Initiative and/or mandatory referendum",
                        "detail": "100,000 voters may initiate; people + cantons must approve amendments",
                    },
                    {
                        "id": "opt_ref",
                        "label": "Optional referendum path",
                        "detail": "50,000 voters or 8 cantons can demand a popular vote",
                    },
                ],
            },
        ],
    },
]

# Append sources, matrices, and revision clusters below.
EXTRA_CLUSTERS = [
    {
        "title": "Sources Borrowed by the Indian Constitution",
        "slug": "wc-sources-borrowed",
        "sort_order": 9,
        "summary": (
            "Table 4.4 deep revision — country, feature, Indian provision, present relevance, "
            "UPSC notes. Canada/Australia/Ireland/Germany/South Africa live here (no full clusters)."
        ),
        "body": (
            "## How to revise sources\n"
            "Ambedkar: framed after ‘ransacking’ world constitutions. "
            "**GoI Act 1935** is the deepest structural source (~250 provisions).\n\n"
            "### Three layers\n"
            "1. **Structural** — GoI Act 1935 (+ Canadian strong Centre)\n"
            "2. **Philosophical** — USA (FRs) + Ireland (DPSPs) + France (Republic/LEF)\n"
            "3. **Political** — Britain (Cabinet / parliamentary)\n\n"
            "## Master borrowed-features sheet\n\n"
            "| Source | Feature borrowed | Indian provision (anchor) | Present relevance | UPSC notes |\n"
            "|---|---|---|---|---|\n"
            "| **GoI Act 1935** | Federal scheme; Governor; Judiciary; PSCs; Emergency; SC advisory jurisdiction; admin details | Arts 1, 153+, 124+, 315+, 352–360, 143; Schedules | Still the skeleton of Union–State machinery | ~250 provisions transplanted |\n"
            "| **Britain** | Parliamentary govt; Rule of Law; legislative procedure; single citizenship; Cabinet; prerogative writs; privileges; bicameralism | Arts 74–75, 79+, 105, 32/226 writs; Citizenship Part II | Daily working of Indian polity | India ≠ parliamentary sovereignty |\n"
            "| **USA** | FRs; independent judiciary; judicial review; impeachment of President; judge removal; Vice-President | Parts III; Arts 124, 61, 67–71 | Rights culture + checks on high offices | Due process evolved via Art. 21 |\n"
            "| **Ireland** | DPSPs; Rajya Sabha nominations; method of electing President | Part IV; Art. 80(1)(a); Art. 54–55 | Socio-economic democracy agenda | DPSP non-justiciable |\n"
            "| **Canada** | Federation with strong Centre; residuary with Centre; Centre-appointed Governors | Art. 248; Seventh Schedule; Art. 155 | Explains unitary bias | Contrast USA residuary → states |\n"
            "| **Australia** | Concurrent List; freedom of trade/commerce/intercourse; joint sitting | Seventh Schedule; Arts 301–307; Art. 108 | Centre–state legislative overlap | Joint sitting = rare but tested |\n"
            "| **Weimar Germany** | Suspension of FRs during Emergency | Arts 358–359 | Emergency rights regime | 44th safeguards matter |\n"
            "| **USSR** | Fundamental Duties; justice (SEP) in Preamble | Art. 51A; Preamble | Duties + justice vocabulary | From Soviet, not Russia 1993 |\n"
            "| **France** | Republic; Liberty, Equality, Fraternity | Preamble | Republican identity | Not French hybrid executive |\n"
            "| **South Africa** | Amendment procedure; election of Rajya Sabha members | Art. 368; Art. 80 | Rigid–flexible blend | RS election method |\n"
            "| **Japan** | Procedure established by law | Art. 21 (classic contrast with US due process) | Maneka Gandhi expanded meaning | Pair with US due process questions |\n\n"
            "### High-yield feature → source mnemonics\n"
            "- **FR + JR + impeachment + VP** → USA\n"
            "- **Cabinet + Rule of Law + single citizenship + writs** → Britain\n"
            "- **DPSP + President election method + RS nomination** → Ireland\n"
            "- **Concurrent List + joint sitting + trade freedom** → Australia\n"
            "- **Strong Centre + residuary Centre + Governors** → Canada\n"
            "- **FD + Preamble justice** → USSR\n"
            "- **Republic + LEF** → France\n"
            "- **Art. 368 style + RS election** → South Africa\n"
            "- **Emergency FR suspension** → Weimar\n"
            "- **Procedure established by law** → Japan\n"
        ),
        "articles": [
            ("Table 4.4", "Sources of the Constitution at a Glance (Laxmikanth Ch.4, pp. 81–82)."),
            ("GoI Act 1935", "Main structural source — federal scheme and administrative detail."),
            ("Art. 368 / Part III–IV", "Amendment, FRs, DPSPs — map borrowed ideas to Indian text."),
        ],
        "visual_blocks": [
            {
                "id": "wc-sources-pillars",
                "type": "pillars",
                "title": "Eleven sources at a glance",
                "items": [
                    {
                        "id": "goi",
                        "articles": "1935",
                        "label": "GoI Act 1935",
                        "slug": "wc-sources-borrowed",
                        "detail": "Federal scheme, Governor, Judiciary, PSCs, Emergency, Art. 143",
                        "tone": "teal",
                    },
                    {
                        "id": "uk",
                        "articles": "UK",
                        "label": "Britain",
                        "slug": "wc-britain",
                        "detail": "Parliamentary, Cabinet, Rule of Law, writs, bicameralism",
                        "tone": "olive",
                    },
                    {
                        "id": "usa",
                        "articles": "USA",
                        "label": "United States",
                        "slug": "wc-usa",
                        "detail": "FRs, JR, impeachment, judge removal, VP",
                        "tone": "gold",
                    },
                    {
                        "id": "irl",
                        "articles": "Ireland",
                        "label": "Ireland",
                        "slug": "wc-sources-borrowed",
                        "detail": "DPSP, RS nomination, President election method",
                        "tone": "orange",
                    },
                    {
                        "id": "can",
                        "articles": "Canada",
                        "label": "Canada",
                        "slug": "wc-sources-borrowed",
                        "detail": "Strong Centre; residuary Centre; appointed Governors",
                        "tone": "terracotta",
                    },
                    {
                        "id": "aus",
                        "articles": "Australia",
                        "label": "Australia",
                        "slug": "wc-sources-borrowed",
                        "detail": "Concurrent List; trade freedom; joint sitting",
                        "tone": "maroon",
                    },
                    {
                        "id": "wei",
                        "articles": "Weimar",
                        "label": "Germany (Weimar)",
                        "slug": "wc-sources-borrowed",
                        "detail": "FR suspension in Emergency",
                        "tone": "teal",
                    },
                    {
                        "id": "ussr",
                        "articles": "USSR",
                        "label": "USSR",
                        "slug": "wc-ussr",
                        "detail": "Fundamental Duties; Preamble justice (SEP)",
                        "tone": "olive",
                    },
                    {
                        "id": "fr",
                        "articles": "France",
                        "label": "France",
                        "slug": "wc-france",
                        "detail": "Republic; Liberty, Equality, Fraternity",
                        "tone": "gold",
                    },
                    {
                        "id": "sa",
                        "articles": "RSA",
                        "label": "South Africa",
                        "slug": "wc-sources-borrowed",
                        "detail": "Amendment procedure; RS election",
                        "tone": "orange",
                    },
                    {
                        "id": "jp",
                        "articles": "Japan",
                        "label": "Japan",
                        "slug": "wc-japan",
                        "detail": "Procedure established by law",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "wc-sources-layers",
                "type": "callout",
                "tone": "tip",
                "title": "Three layers + India-vs note",
                "body": (
                    "Structural ← GoI 1935 / Canada · Philosophical ← USA + Ireland + France · "
                    "Political ← Britain. Canada, Australia, Ireland, Weimar Germany, South Africa "
                    "appear **only here** (no separate country chapters in Part XIII)."
                ),
            },
            {
                "id": "wc-sources-india-vs",
                "type": "comparison",
                "title": "India vs source countries — what was NOT copied wholesale",
                "columns": [
                    {
                        "id": "borrowed",
                        "heading": "Borrowed idea",
                        "points": [
                            "British Cabinet / parliamentary form",
                            "US Fundamental Rights + judicial review",
                            "Irish DPSPs",
                            "Canadian strong Centre",
                            "Japanese ‘procedure established by law’",
                        ],
                    },
                    {
                        "id": "indianised",
                        "heading": "Indian twist",
                        "points": [
                            "Republic + written Constitution + JR (≠ UK sovereignty)",
                            "Also DPSPs + basic structure limit on amendment",
                            "Justiciable FRs balanced with DPSPs (Minerva)",
                            "Emergency + single Constitution (≠ classic dual)",
                            "Expanded via Maneka toward fairness (due-process flavour)",
                        ],
                    },
                ],
            },
        ],
    },
    {
        "title": "Systems Matrix — Form & Constitution Types",
        "slug": "wc-systems-matrix",
        "sort_order": 10,
        "summary": (
            "Parliamentary vs Presidential; Federal vs Unitary; Written vs Unwritten; "
            "Rigid vs Flexible — cross-country scan."
        ),
        "body": (
            "## Parliamentary vs Presidential\n"
            "| | Parliamentary | Presidential |\n|---|---|---|\n"
            "| Executive | Dual (nominal + real) | Single real executive |\n"
            "| Tenure | Depends on House confidence | Fixed |\n"
            "| Ministers | Usually legislators | Usually not legislators |\n"
            "| Dissolution | Lower House can be dissolved | Typically fixed legislature |\n"
            "| Examples | UK, India, Japan | USA |\n"
            "| Hybrid | — | France (President + responsible PM) |\n"
            "| Council | — | Switzerland (neither classic model) |\n\n"
            "## Federal vs Unitary\n"
            "- **Federal:** USA, Switzerland, USSR (1977), Russia, India (quasi).\n"
            "- **Unitary:** UK, France, Japan, China.\n"
            "- **Residuary:** USA/Swiss/USSR → units; India/Canada model → Centre.\n\n"
            "## Written vs Unwritten\n"
            "- **Unwritten:** UK only in this set.\n"
            "- **Written:** all others + India.\n\n"
            "## Rigid vs Flexible\n"
            "- **Flexible:** UK.\n"
            "- **Rigid:** USA, France, Japan (never amended), Switzerland, China, USSR.\n"
            "- **Blend:** India (Art. 368 three paths)."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-sys-parl-pres",
                "type": "comparison",
                "title": "Parliamentary vs Presidential (core)",
                "columns": [
                    {
                        "id": "parl",
                        "heading": "Parliamentary",
                        "points": [
                            "UK, India, Japan (Cabinet)",
                            "Collective responsibility",
                            "Fusion of powers",
                            "PM leadership; dissolution possible",
                        ],
                    },
                    {
                        "id": "pres",
                        "heading": "Presidential / other",
                        "points": [
                            "USA — classic presidential",
                            "France — hybrid",
                            "Switzerland — council of 7",
                            "Russia — strong President + PM",
                        ],
                    },
                ],
            },
            {
                "id": "wc-sys-fed-uni",
                "type": "comparison",
                "title": "Federal vs Unitary",
                "columns": [
                    {
                        "id": "fed",
                        "heading": "Federal",
                        "points": [
                            "USA — residuary states",
                            "Switzerland — residuary cantons",
                            "USSR — residuary republics + secession",
                            "Russia — complex subjects",
                            "India — residuary Centre (Canadian)",
                        ],
                    },
                    {
                        "id": "uni",
                        "heading": "Unitary",
                        "points": [
                            "UK — mother unitary parliamentary",
                            "France — more unitary than Britain",
                            "Japan — provinces subordinate",
                            "China — unitary multinational",
                        ],
                    },
                ],
            },
            {
                "id": "wc-sys-written-rigid",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 minutes — type sniff",
                "body": (
                    "**Unwritten+Flexible+Unitary+Parliamentary** = UK. "
                    "**Written+Rigid+Federal+Presidential** = USA. "
                    "**Written+Rigid+Unitary+Hybrid** = France. "
                    "**Written+Rigid+Federal+Council** = Switzerland. "
                    "**India** = Written + blend rigidity + quasi-federal + parliamentary republic."
                ),
            },
        ],
    },
    {
        "title": "Organs Matrix — Heads, Houses, Elections",
        "slug": "wc-organs-matrix",
        "sort_order": 11,
        "summary": (
            "Bicameral vs unicameral; Head of State vs Head of Government; election systems."
        ),
        "body": (
            "## Bicameral vs Unicameral\n"
            "- **Unicameral:** China (NPC).\n"
            "- **Bicameral:** USA, UK, France, Japan, USSR, Russia, Switzerland, India.\n"
            "- **Equal houses:** Switzerland (unique); USSR (equal 750+750).\n"
            "- **Powerful upper house:** USA Senate (classic).\n\n"
            "## Head of State vs Head of Government\n"
            "| Country | Head of State | Head of Government |\n|---|---|---|\n"
            "| India | President (nominal) | PM |\n"
            "| UK | King/Queen | PM |\n"
            "| USA | President | President |\n"
            "| France | President (real pivot) | PM |\n"
            "| Japan | Emperor (symbol) | PM |\n"
            "| USSR | Presidium Chairman (collegial) | Premier |\n"
            "| Russia | President | PM (appointed) |\n"
            "| China | President (ceremonial) | Premier |\n"
            "| Switzerland | Federal President (1 yr, among 7) | Federal Council collectively |\n\n"
            "## Election systems (high-yield)\n"
            "- USA President: Electoral College 538 / 270.\n"
            "- France President: direct two-ballot absolute majority.\n"
            "- India President: indirect elected college (Art. 54–55) — Irish method borrowed.\n"
            "- Swiss National Council: proportional representation.\n"
            "- China NPC: multilevel election of deputies."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-organs-heads",
                "type": "comparison",
                "title": "Head of State comparison",
                "columns": [
                    {
                        "id": "ceremonial",
                        "heading": "Mostly ceremonial / nominal",
                        "points": [
                            "India — President",
                            "UK — Crown",
                            "Japan — Emperor",
                            "China — President",
                            "Switzerland — rotating Federal President",
                        ],
                    },
                    {
                        "id": "real",
                        "heading": "Real executive head of state",
                        "points": [
                            "USA — President",
                            "France — President (dominant)",
                            "Russia — President",
                            "USSR — Presidium (collegial real formal head)",
                        ],
                    },
                ],
            },
            {
                "id": "wc-organs-houses",
                "type": "pillars",
                "title": "Legislature shapes",
                "items": [
                    {
                        "id": "uni",
                        "articles": "China",
                        "label": "Unicameral",
                        "slug": "wc-china",
                        "detail": "NPC ~3000 + Standing Committee",
                        "tone": "teal",
                    },
                    {
                        "id": "equal",
                        "articles": "CH / USSR",
                        "label": "Equal bicameral",
                        "slug": "wc-switzerland",
                        "detail": "Swiss houses equal; USSR 750=750",
                        "tone": "olive",
                    },
                    {
                        "id": "senate",
                        "articles": "USA",
                        "label": "Powerful upper house",
                        "slug": "wc-usa",
                        "detail": "American Senate — strongest second chamber",
                        "tone": "gold",
                    },
                    {
                        "id": "lower",
                        "articles": "UK/IN",
                        "label": "Lower-house dominant",
                        "slug": "wc-britain",
                        "detail": "Commons / Lok Sabha pattern",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "wc-organs-elections",
                "type": "callout",
                "tone": "tip",
                "title": "Election systems — quick hits",
                "body": (
                    "USA EC 538/270 · France two-ballot · India indirect President (Ireland) · "
                    "Swiss PR National Council · Russia direct President · Japan Diet designates PM."
                ),
            },
        ],
    },
    {
        "title": "Rights, Emergency & Judicial Review",
        "slug": "wc-rights-emergency-jr",
        "sort_order": 12,
        "summary": (
            "Fundamental rights catalogues, emergency logics, and judicial review models across countries."
        ),
        "body": (
            "## Fundamental Rights across constitutions\n"
            "- **USA:** Bill of Rights (1791); due process.\n"
            "- **Japan:** Arts 10–40 — elaborate; eternal & inviolate.\n"
            "- **USSR/China:** Broad socio-economic lists; limited by state/society/collective.\n"
            "- **Switzerland:** 25 FRs + non-justiciable social goals.\n"
            "- **India:** Justiciable Part III + DPSPs + FDs — unique trilogy.\n\n"
            "## Emergency provisions comparison\n"
            "- **India:** Arts 352/356/360 — most examined catalogue.\n"
            "- **France:** Special presidential emergency powers after consulting PM, house presidents, Council.\n"
            "- **Weimar → India:** FR suspension idea during Emergency.\n"
            "- **Switzerland:** Emergency federal acts — referendum rules apply.\n"
            "- **USA/UK:** Statute/prerogative wartime powers — not Indian three-fold scheme.\n\n"
            "## Judicial Review across countries\n"
            "| Model | Where |\n|---|---|\n"
            "| Strong JR (constitution supreme) | USA, India, Japan |\n"
            "| JR written in Constitution | Japan (explicit) |\n"
            "| JR via practice | USA (classic narrative) |\n"
            "| No JR of statutes | UK (parliamentary sovereignty) |\n"
            "| Advisory/constitutional council | France |\n"
            "| Constitutional Court | Russia (19 members) |\n"
            "| Weak/party-state legality | USSR, China |"
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-jr-compare",
                "type": "comparison",
                "title": "Judicial Review spectrum",
                "columns": [
                    {
                        "id": "strong",
                        "heading": "Strong / explicit",
                        "points": [
                            "USA — ultra vires; BoR guardian",
                            "India — JR + basic structure",
                            "Japan — JR from Constitution text",
                            "Russia — Constitutional Court",
                        ],
                    },
                    {
                        "id": "limited",
                        "heading": "Limited / absent",
                        "points": [
                            "UK — no voiding Acts of Parliament",
                            "France — Constitutional Council advisory",
                            "China/USSR — not liberal JR model",
                        ],
                    },
                ],
            },
            {
                "id": "wc-rights-pillars",
                "type": "pillars",
                "title": "Rights models",
                "items": [
                    {
                        "id": "liberal",
                        "articles": "USA/JP",
                        "label": "Liberal BoR style",
                        "slug": "wc-usa",
                        "detail": "Justiciable civil-political core",
                        "tone": "teal",
                    },
                    {
                        "id": "trilogy",
                        "articles": "India",
                        "label": "FR + DPSP + FD",
                        "slug": "wc-sources-borrowed",
                        "detail": "India’s distinctive combination",
                        "tone": "olive",
                    },
                    {
                        "id": "socialist",
                        "articles": "USSR/CN",
                        "label": "Socialist catalogues",
                        "slug": "wc-ussr",
                        "detail": "Rights + duties; collective limits",
                        "tone": "gold",
                    },
                    {
                        "id": "swiss",
                        "articles": "CH",
                        "label": "FRs + social goals",
                        "slug": "wc-switzerland",
                        "detail": "Goals non-enforceable like DPSPs",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "wc-emergency-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Emergency trap",
                "body": (
                    "Don’t invent Art. 352 clones abroad. For comparative answers: state India’s three "
                    "emergencies clearly, then note France’s presidential emergency clause and Weimar’s "
                    "influence on FR suspension — not identical institutions."
                ),
            },
        ],
    },
    {
        "title": "Amendment & Distribution of Powers",
        "slug": "wc-amendment-powers",
        "sort_order": 13,
        "summary": (
            "Amendment procedures and federal/unitary power distribution including residuary rules."
        ),
        "body": (
            "## Constitutional amendment procedures\n"
            "| Country | Procedure (book spine) |\n|---|---|\n"
            "| USA | 2/3 Congress + 3/4 states (or convention route) |\n"
            "| UK | Ordinary legislation (flexible) |\n"
            "| France | 60% both Houses **or** referendum; republic locked |\n"
            "| Japan | Diet 2/3 + referendum — never used |\n"
            "| USSR | 2/3 each House of Supreme Soviet |\n"
            "| China | NPC 2/3; proposal Standing Committee or 1/5 deputies |\n"
            "| Switzerland | Total/partial revision; people + cantons |\n"
            "| India | Art. 368 — simple / special / special + state ratification (SA influence) |\n\n"
            "## Distribution of powers\n"
            "- **Enumerated Centre, residuary units:** USA, Switzerland, USSR.\n"
            "- **Residuary Centre:** India (Canadian), strong-Centre federation.\n"
            "- **Unitary delegation:** UK, France, Japan, China — local/provincial powers from Centre.\n"
            "- **Concurrent List:** Australia → India Seventh Schedule."
        ),
        "articles": [
            ("Art. 368", "Indian amendment — three pathways; South African influence on procedure."),
            ("Seventh Schedule", "Union / State / Concurrent — Australian concurrent idea."),
            ("Art. 248", "Residuary powers with Union — Canadian pattern."),
        ],
        "visual_blocks": [
            {
                "id": "wc-amend-compare",
                "type": "comparison",
                "title": "Amendment difficulty (intuitive)",
                "columns": [
                    {
                        "id": "hard",
                        "heading": "Hard / rigid",
                        "points": [
                            "USA — only 27 amendments",
                            "Japan — zero amendments",
                            "Switzerland — people + cantons",
                            "France — special majority / referendum",
                        ],
                    },
                    {
                        "id": "easy-blend",
                        "heading": "Flexible / blend",
                        "points": [
                            "UK — ordinary law",
                            "India — three Art. 368 paths",
                            "China/USSR — special legislative majority",
                        ],
                    },
                ],
            },
            {
                "id": "wc-residuary",
                "type": "flowchart",
                "title": "Where do residuary powers go?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Federal constitution?",
                        "options": [
                            {"label": "Yes — USA / Swiss / USSR pattern", "next": "units"},
                            {"label": "Yes — India / Canada pattern", "next": "centre"},
                            {"label": "No — unitary state", "next": "unitary"},
                        ],
                    },
                    {
                        "id": "units",
                        "label": "Residuary → units",
                        "detail": "States / cantons / Union Republics",
                    },
                    {
                        "id": "centre",
                        "label": "Residuary → Centre",
                        "detail": "Art. 248 India — strong Centre",
                    },
                    {
                        "id": "unitary",
                        "label": "No true residuary split",
                        "detail": "UK, France, Japan, China — centre holds supremacy",
                    },
                ],
            },
            {
                "id": "wc-amend-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mnemonic — RAJ of rigidity",
                "body": (
                    "**R**igid classics: USA, Japan, Switzerland, France. "
                    "**A**mend freely: UK. "
                    "**J**uggle three paths: India (Art. 368)."
                ),
            },
        ],
    },
    {
        "title": "Master Comparison Table",
        "slug": "wc-master-table",
        "sort_order": 14,
        "summary": (
            "One feature matrix of all eight book constitutions plus India — Prelims/Mains cheat sheet."
        ),
        "body": (
            "## Master matrix (all 8 + India)\n\n"
            "| Feature | India | USA | UK | France | Japan | USSR | Russia | China | Swiss |\n"
            "|---|---|---|---|---|---|---|---|---|---|\n"
            "| Written? | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes |\n"
            "| Rigid? | Blend | Yes | No | Yes | Yes* | Yes | Yes | Yes | Yes |\n"
            "| Federal? | Quasi | Yes | No | No | No | Yes | Yes | No | Yes |\n"
            "| Executive | Parl. | Pres. | Parl. | Hybrid | Parl. | Parl.+Presidium | Strong Pres. | Parl. form | Council |\n"
            "| Legislature | Bi | Bi | Bi | Bi | Bi | Bi equal | Bi | Uni | Bi equal |\n"
            "| JR | Strong | Strong | No (statutes) | Council | Strong (text) | Weak | Const. Court | Weak | Federal courts |\n"
            "| Rights | FR+DPSP+FD | BoR | Evolved | Republican | Arts 10–40 | Socialist FR+FD | Liberal FR | FR+FD limited | FR+goals |\n"
            "| Unique | Basic structure | Oldest written | Mother / unwritten | Rationalised Parl. | Art. 9 | Presidium | 1993 rupture | CPC lead | Direct democracy |\n\n"
            "\\*Japan: never amended.\n\n"
            "### Constitutional philosophies (one-liners)\n"
            "- India — justice (SEP), liberty, equality, fraternity; secular democratic republic.\n"
            "- USA — limited government & separation of powers.\n"
            "- UK — parliamentary sovereignty + Rule of Law.\n"
            "- France — LEF; strong republican presidency.\n"
            "- Japan — peace & popular sovereignty.\n"
            "- USSR — Marxism–Leninism; socialist ownership.\n"
            "- Russia — post-Soviet liberal-democratic federal republic.\n"
            "- China — socialism with Chinese characteristics; CPC leadership.\n"
            "- Switzerland — direct democracy & cantonal federalism."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-master-pillars",
                "type": "pillars",
                "title": "Eight + India — open a country",
                "items": COUNTRY_PILLARS,
            },
            {
                "id": "wc-master-families-preview",
                "type": "callout",
                "tone": "tip",
                "title": "Use with Constitutional Families",
                "body": (
                    "Scan this matrix first, then open **Constitutional Families** for the tree view "
                    "and **One-pagers** for country flashcards."
                ),
            },
            {
                "id": "wc-master-india-row",
                "type": "comparison",
                "title": "India’s synthesis row",
                "columns": [
                    {
                        "id": "took",
                        "heading": "Took from world",
                        "points": [
                            "Cabinet (UK)",
                            "FRs/JR (USA)",
                            "DPSPs (Ireland)",
                            "Strong Centre (Canada)",
                            "Concurrent List (Australia)",
                        ],
                    },
                    {
                        "id": "made",
                        "heading": "Made Indian",
                        "points": [
                            "Republic + written Constitution",
                            "Basic structure",
                            "Quasi-federal emergency tilt",
                            "FR–DPSP balance",
                            "Integrated judiciary",
                        ],
                    },
                ],
            },
        ],
    },
    {
        "title": "Constitutional Families",
        "slug": "wc-constitutional-families",
        "sort_order": 15,
        "summary": (
            "Conceptual family tree — Westminster, Presidential, Hybrid, Council, Socialist — "
            "with India as a synthesis node."
        ),
        "body": (
            "## Families (conceptual map)\n"
            "1. **Westminster parliamentary** — UK → India, Japan (with local twists).\n"
            "2. **Presidential** — USA.\n"
            "3. **Hybrid** — France (Fifth Republic).\n"
            "4. **Council / collegial** — Switzerland (and USSR Presidium as plural executive cousin).\n"
            "5. **Socialist party-state** — USSR 1977, China 1982 (Russia 1993 exits toward presidential republic).\n\n"
            "India sits at the **synthesis** node: Westminster politics + US rights/JR + Irish DPSPs + "
            "Canadian federal tilt + other borrowings."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-families-tree",
                "type": "tree",
                "title": "Constitutional families",
                "root": {
                    "id": "world",
                    "label": "World constitutional families",
                    "children": [
                        {
                            "id": "west",
                            "label": "Westminster",
                            "detail": "Parliamentary responsible government",
                            "children": [
                                {"id": "uk", "label": "UK", "slug": "wc-britain"},
                                {"id": "in", "label": "India (republic twist)", "slug": "world-constitutions"},
                                {"id": "jp", "label": "Japan", "slug": "wc-japan"},
                            ],
                        },
                        {
                            "id": "pres",
                            "label": "Presidential",
                            "children": [
                                {"id": "usa", "label": "USA", "slug": "wc-usa"},
                                {"id": "ru", "label": "Russia (strong Pres.)", "slug": "wc-russia"},
                            ],
                        },
                        {
                            "id": "hybrid",
                            "label": "Hybrid",
                            "children": [
                                {"id": "fr", "label": "France V Republic", "slug": "wc-france"},
                            ],
                        },
                        {
                            "id": "council",
                            "label": "Council / Collegial",
                            "children": [
                                {"id": "ch", "label": "Switzerland", "slug": "wc-switzerland"},
                                {"id": "ussr", "label": "USSR Presidium", "slug": "wc-ussr"},
                            ],
                        },
                        {
                            "id": "socialist",
                            "label": "Socialist party-state",
                            "children": [
                                {"id": "su", "label": "USSR 1977", "slug": "wc-ussr"},
                                {"id": "cn", "label": "China 1982", "slug": "wc-china"},
                            ],
                        },
                    ],
                },
            },
            {
                "id": "wc-families-map",
                "type": "map",
                "title": "Conceptual world map (nodes)",
                "nodes": [
                    {"id": "usa", "label": "USA", "detail": "Presidential federal"},
                    {"id": "uk", "label": "UK", "detail": "Unwritten parliamentary"},
                    {"id": "fr", "label": "France", "detail": "Hybrid"},
                    {"id": "jp", "label": "Japan", "detail": "Peace parliament"},
                    {"id": "in", "label": "India", "detail": "Synthesis"},
                    {"id": "ch", "label": "Swiss", "detail": "Council"},
                    {"id": "cn", "label": "China", "detail": "CPC"},
                    {"id": "ru", "label": "Russia", "detail": "1993"},
                ],
                "edges": [
                    {"from": "uk", "to": "in"},
                    {"from": "usa", "to": "in"},
                    {"from": "fr", "to": "in"},
                    {"from": "jp", "to": "in"},
                    {"from": "uk", "to": "jp"},
                ],
            },
            {
                "id": "wc-families-tip",
                "type": "callout",
                "tone": "note",
                "title": "Map is conceptual",
                "body": (
                    "This is a revision graph, not a geographic GIS map — use it to place each "
                    "constitution in a family before memorising details."
                ),
            },
        ],
    },
    {
        "title": "Mnemonics, Traps & Exam-in-5-Minutes",
        "slug": "wc-mnemonics-traps",
        "sort_order": 16,
        "summary": (
            "Memory tricks, frequently confused features, and rapid revision boxes for Prelims."
        ),
        "body": (
            "## Frequently confused\n"
            "| Confusion | Clear it |\n|---|---|\n"
            "| UK sovereignty vs India JR | UK Parliament supreme; India Constitution supreme |\n"
            "| USA residuary vs India residuary | USA → states; India → Centre |\n"
            "| France vs USA President | France also has PM responsible to Parliament |\n"
            "| Swiss Council vs Cabinet | Not removable by no-confidence; equal 7 |\n"
            "| USSR vs Russia | 1977 socialist vs 1993 multi-party presidential |\n"
            "| China President vs Premier | President ceremonial; Premier heads State Council |\n"
            "| Japan JR vs USA JR | Japan’s JR is textual; USA’s classic story is practice |\n"
            "| Dual vs triple vs single citizenship | USA dual possible; Swiss triple; India single |\n\n"
            "## Mnemonics\n"
            "- **BUJF-JRCS** countries in book order: Britain? Wait — use passport order: "
            "**U**SA **B**ritain **F**rance **J**apan **U**SSR **R**ussia **C**hina **S**wiss → "
            "**UBFJURCS** (“U Be For Justice Under Rule — Compare Systems”).\n"
            "- Sources: **B-U-I-C-A-G-S-F-S-J** + GoI — “Bring Usa Ireland Canada Australia; "
            "Germany Soviet France SA Japan”.\n"
            "- Swiss: **CDED** — Council, Direct democracy, Equal houses, Dual? → **Triple** citizenship."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-exam5",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 minutes",
                "body": (
                    "1) Name system family 2) Written/rigid/federal ticks 3) Who is real executive "
                    "4) One unique feature 5) One India borrowing. Repeat for all eight."
                ),
            },
            {
                "id": "wc-traps",
                "type": "callout",
                "tone": "trap",
                "title": "Top Prelims traps",
                "body": (
                    "Japan never amended ≠ flexible. French Constitutional Council ≠ US Supreme Court. "
                    "Shadow Cabinet is British, not Indian. Swiss President is not a US-style executive. "
                    "Fundamental Duties borrowed from USSR, not Russia 1993."
                ),
            },
            {
                "id": "wc-memory-palace",
                "type": "memory_palace",
                "title": "Passport stamps palace",
                "setting": "Immigration desk with eight passport stamps",
                "loci": [
                    {
                        "id": "gate",
                        "place": "Entry gate stamp",
                        "association": "USA",
                        "detail": "Oldest written; EC 270; pocket veto",
                    },
                    {
                        "id": "hall",
                        "place": "Great hall stamp",
                        "association": "UK",
                        "detail": "Unwritten; sovereignty; Shadow Cabinet",
                    },
                    {
                        "id": "tower",
                        "place": "Tower stamp",
                        "association": "France",
                        "detail": "Hybrid; 60%; Council of 9",
                    },
                    {
                        "id": "garden",
                        "place": "Peace garden stamp",
                        "association": "Japan",
                        "detail": "Art. 9; never amended",
                    },
                    {
                        "id": "archive",
                        "place": "Archive dual stamp",
                        "association": "USSR → Russia",
                        "detail": "Presidium → 1993 President",
                    },
                    {
                        "id": "wall",
                        "place": "Wall stamp",
                        "association": "China",
                        "detail": "CPC; unicameral NPC",
                    },
                    {
                        "id": "alpine",
                        "place": "Alpine stamp",
                        "association": "Switzerland",
                        "detail": "Seven equals; referendum",
                    },
                ],
            },
        ],
    },
    {
        "title": "One-Page Summaries & Final Revision",
        "slug": "wc-one-pagers",
        "sort_order": 17,
        "summary": (
            "Country flashcards, sources cheat sheet, philosophies, and a one-page final revision summary."
        ),
        "body": (
            "## Country-wise one-pagers\n\n"
            "### USA\n"
            "Written·Rigid·Federal·Presidential·BoR·EC 538/270·Senate powerhouse·Kitchen Cabinet·Pocket veto.\n\n"
            "### UK\n"
            "Unwritten·Flexible·Unitary·Parliamentary sovereignty·Rule of Law·Cabinet/Shadow/Privy Council.\n\n"
            "### France\n"
            "1958·Hybrid·Unitary·Rigid·Rationalised Parliament·Constitutional Council·Direct President.\n\n"
            "### Japan\n"
            "1947·Unitary·Parliamentary monarchy·Art. 9·JR in text·Never amended·Diet bicameral.\n\n"
            "### USSR 1977\n"
            "Socialist federal·Presidium·CPSU·Equal houses·FR+FD·Federation of Federations.\n\n"
            "### Russia 1993\n"
            "Multi-party federal·Strong President·Duma+Council·Constitutional Court·Impeachment 2/3.\n\n"
            "### China 1982\n"
            "Socialist unitary·CPC leadership·NPC unicameral·Premier real admin·FR limited by collective.\n\n"
            "### Switzerland 1999\n"
            "Council of 7·Equal bicameral·Direct democracy·Triple citizenship·Social goals non-justiciable.\n\n"
            "## Sources borrowed — cheat sheet\n"
            "GoI1935 structure · UK politics · USA rights/JR · Ireland DPSP/President · Canada Centre · "
            "Australia Concurrent/joint sitting · Weimar emergency FR · USSR duties/justice · "
            "France Republic/LEF · SA amendment/RS · Japan procedure.\n\n"
            "## One-page final revision\n"
            "Passport metaphor → 8 stamps → India-vs each → sources table → systems matrices → "
            "families tree → traps. Stop when you can teach each country in 60 seconds."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-onepager-timeline",
                "type": "timeline",
                "title": "Constitution years timeline",
                "events": [
                    {"id": "usa", "year": 1787, "label": "USA framed", "detail": "In force 1789"},
                    {"id": "jp", "year": 1947, "label": "Japan", "detail": "MacArthur/Showa"},
                    {"id": "in", "year": 1950, "label": "India", "detail": "Synthesis constitution"},
                    {"id": "fr", "year": 1958, "label": "France V", "detail": "Gaullist republic"},
                    {"id": "ussr", "year": 1977, "label": "USSR Brezhnev", "detail": "Last Soviet constitution"},
                    {"id": "cn", "year": 1982, "label": "China", "detail": "Present PRC text"},
                    {"id": "ru", "year": 1993, "label": "Russia", "detail": "Post-USSR"},
                    {"id": "ch", "year": 1999, "label": "Switzerland", "detail": "In force 2000"},
                ],
            },
            {
                "id": "wc-sources-cheat",
                "type": "callout",
                "tone": "tip",
                "title": "Sources cheat sheet (60 seconds)",
                "body": (
                    "1935 skeleton · UK Cabinet · US FRs/JR/VP · Ireland DPSP · Canada residuary Centre · "
                    "Australia Concurrent · Weimar FR suspend · USSR FD · France LEF · SA Art.368 flavour · "
                    "Japan procedure."
                ),
            },
            {
                "id": "wc-final-box",
                "type": "callout",
                "tone": "note",
                "title": "Final revision box",
                "body": (
                    "If stuck in Mains: define the foreign feature → place family → contrast India on "
                    "executive/federalism/rights/amendment → close with borrowing or deliberate rejection."
                ),
            },
        ],
    },
    {
        "title": "PYQ Themes — World Constitutions",
        "slug": "wc-pyq-themes",
        "sort_order": 18,
        "summary": (
            "Recurring UPSC themes: sources of Constitution, parliamentary vs presidential, "
            "Swiss council, Japanese Art. 9, French hybrid, Rule of Law, residuary powers."
        ),
        "body": (
            "## Theme map\n"
            "1. **Sources of the Constitution** — match feature → country (highest frequency).\n"
            "2. **Parliamentary vs Presidential** — India/UK vs USA; merits.\n"
            "3. **Federal features** — residuary powers USA vs India/Canada.\n"
            "4. **Rule of Law / parliamentary sovereignty** — UK contrasts.\n"
            "5. **Judicial review** — USA/Japan/India vs UK.\n"
            "6. **Unique executives** — Swiss Council; French hybrid; USSR Presidium.\n"
            "7. **Peace clause** — Japanese Art. 9.\n"
            "8. **Rights designs** — BoR, socialist rights, Swiss social goals vs DPSPs.\n\n"
            "Practice by writing 3 match-the-following lines daily from the Sources table."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "wc-pyq-heat",
                "type": "pyq_heatmap",
                "title": "PYQ focus areas",
                "items": [
                    {"concept_slug": "wc-sources-borrowed", "label": "Sources borrowed"},
                    {"concept_slug": "wc-systems-matrix", "label": "Parl vs Pres / federal"},
                    {"concept_slug": "wc-usa", "label": "USA features"},
                    {"concept_slug": "wc-britain", "label": "UK features"},
                    {"concept_slug": "wc-switzerland", "label": "Swiss council"},
                    {"concept_slug": "wc-japan", "label": "Japan Art. 9"},
                    {"concept_slug": "wc-france", "label": "French hybrid"},
                    {"concept_slug": "wc-master-table", "label": "Master matrix"},
                ],
            },
            {
                "id": "wc-pyq-tip",
                "type": "callout",
                "tone": "tip",
                "title": "How Prelims frames this",
                "body": (
                    "Expect assertion–reason and matching lists on borrowings. "
                    "Mains loves ‘compare parliamentary and presidential’ and ‘features borrowed’ essays."
                ),
            },
            {
                "id": "wc-pyq-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Statement traps",
                "body": (
                    "Watch absolute words: ‘India copied British parliamentary sovereignty’, "
                    "‘Swiss executive is presidential’, ‘Japan amended Art. 9’, "
                    "‘Chinese President is like the US President’."
                ),
            },
        ],
    },
]

CLUSTERS = CLUSTERS + EXTRA_CLUSTERS

EDGES = [
    (HUB_SLUG, "parent", "wc-usa"),
    (HUB_SLUG, "parent", "wc-britain"),
    (HUB_SLUG, "parent", "wc-france"),
    (HUB_SLUG, "parent", "wc-japan"),
    (HUB_SLUG, "parent", "wc-ussr"),
    (HUB_SLUG, "parent", "wc-russia"),
    (HUB_SLUG, "parent", "wc-china"),
    (HUB_SLUG, "parent", "wc-switzerland"),
    (HUB_SLUG, "parent", "wc-sources-borrowed"),
    (HUB_SLUG, "parent", "wc-systems-matrix"),
    (HUB_SLUG, "parent", "wc-organs-matrix"),
    (HUB_SLUG, "parent", "wc-rights-emergency-jr"),
    (HUB_SLUG, "parent", "wc-amendment-powers"),
    (HUB_SLUG, "parent", "wc-master-table"),
    (HUB_SLUG, "parent", "wc-constitutional-families"),
    (HUB_SLUG, "parent", "wc-mnemonics-traps"),
    (HUB_SLUG, "parent", "wc-one-pagers"),
    (HUB_SLUG, "parent", "wc-pyq-themes"),
    ("wc-sources-borrowed", "related", "sf-sources"),
    ("wc-sources-borrowed", "related", "wc-usa"),
    ("wc-sources-borrowed", "related", "wc-britain"),
    ("wc-sources-borrowed", "related", "wc-france"),
    ("wc-sources-borrowed", "related", "wc-japan"),
    ("wc-sources-borrowed", "related", "wc-ussr"),
    ("wc-ussr", "related", "wc-russia"),
    ("wc-systems-matrix", "related", "wc-master-table"),
    ("wc-master-table", "related", "wc-constitutional-families"),
    ("wc-one-pagers", "related", "wc-mnemonics-traps"),
    ("wc-pyq-themes", "related", "wc-sources-borrowed"),
    ("wc-usa", "related", "wc-britain"),
    ("wc-france", "related", "wc-usa"),
    ("wc-switzerland", "related", "wc-systems-matrix"),
]

SAMPLE_PYQS = [
    (
        2013,
        "Which of the following are the features of the British Constitution?",
        "Unwritten, flexible, unitary, parliamentary sovereignty, Rule of Law — classic Laxmikanth list.",
        ["wc-britain", "wc-systems-matrix"],
    ),
    (
        2014,
        "The power of judicial review was first acquired by the Supreme Court of which country through interpretation?",
        "USA — classic narrative of judicial review via practice (contrast Japan’s textual JR).",
        ["wc-usa", "wc-japan", "wc-rights-emergency-jr"],
    ),
    (
        2015,
        "Match features borrowed by the Indian Constitution with their sources.",
        "Use Table 4.4 — e.g. DPSP←Ireland; Concurrent List←Australia; FDs←USSR; procedure←Japan.",
        ["wc-sources-borrowed"],
    ),
    (
        2017,
        "Which one of the following is not a feature of Indian federalism compared to USA?",
        "Residuary powers with Centre (Canada) vs USA residuary with states; single Constitution; etc.",
        ["wc-usa", "wc-sources-borrowed", "wc-amendment-powers"],
    ),
    (
        2019,
        "Consider comparative statements on parliamentary and presidential systems.",
        "India/UK responsible executive vs USA fixed separation — see systems matrix.",
        ["wc-systems-matrix", "wc-britain", "wc-usa"],
    ),
    (
        2021,
        "With reference to the Constitution of India, consider borrowings from other constitutions.",
        "Republic/LEF←France; amendment procedure←South Africa; strong Centre←Canada.",
        ["wc-sources-borrowed", "wc-france"],
    ),
]


class Command(BaseCommand):
    help = (
        "Seed World Constitutions chapter (Laxmikanth Ch.95 / Part XIII) — "
        "eight systems, sources borrowed, comparison matrices."
    )

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
                "title": "World Constitutions",
                "sort_order": 1,
                "book_ref": (
                    "Laxmikanth 8th Ed, Ch. 95 (pp. 949–979); "
                    "Sources Table 4.4 (pp. 81–82)"
                ),
                "summary": (
                    "Visual revision of Part XIII — eight world constitutions compared with India, "
                    "sources borrowed, and exam comparison matrices."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "World Constitutions",
                "summary": (
                    "Passport of world constitutions — USA, Britain, France, Japan, USSR, "
                    "Russia, China, Switzerland — plus sources and master matrices."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **passport mental model**, stamp each of the **eight systems**, "
                    "always read the **India vs** comparison, then lock **Sources Borrowed** and "
                    "the **master matrices**. Finish with mnemonics and PYQ themes.\n\n"
                    "This is a visual revision layer — not a substitute for Laxmikanth Ch.95."
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
            for i, (ref, excerpt) in enumerate(cluster.get("articles") or []):
                ConceptArticle.objects.create(
                    concept=concept,
                    ref=ref,
                    excerpt=excerpt,
                    sort_order=i,
                )

        ConceptArticle.objects.filter(concept=hub).delete()
        ConceptArticle.objects.create(
            concept=hub,
            ref="Laxmikanth Ch. 95",
            excerpt="World Constitutions — Part XIII comparison revision.",
            sort_order=0,
        )

        wc_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=wc_slugs, source__subject=subject
        ).filter(
            target__slug__in=wc_slugs | {"sf-sources"}
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

        self.stdout.write(
            self.style.SUCCESS(
                f"World Constitutions chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} sample PYQs."
            )
        )
