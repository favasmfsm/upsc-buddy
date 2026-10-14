"""Seed Laxmikanth Ch.41 Union Territories (visual revision chapter)."""

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
from subjects.models import Chapter, Section, Subject

HUB_SLUG = "union-territories"
CHAPTER_SLUG = "union-territories"

THEME_PILLARS = [
    {
        "id": "why",
        "articles": "1874 → 1956",
        "label": "Why UTs exist",
        "slug": "ut-why-creation",
        "detail": "Scheduled districts → Part C/D → 7th CAA; four creation reasons.",
        "tone": "teal",
    },
    {
        "id": "eight",
        "articles": "28 + 8",
        "label": "Eight UTs at a glance",
        "slug": "ut-eight-map",
        "detail": "Years, LG vs Administrator, legislature Y/N — ACDD-JLLP.",
        "tone": "olive",
    },
    {
        "id": "arts",
        "articles": "239–242",
        "label": "Article map (Part VIII)",
        "slug": "ut-article-map",
        "detail": "239 admin · 239A–B · 239AA/AB Delhi · 240 regs · 241 HC · 242 repealed.",
        "tone": "gold",
    },
    {
        "id": "admin",
        "articles": "Art. 239",
        "label": "Administrator / LG",
        "slug": "ut-administrator-lg",
        "detail": "Agent of the President — not a Governor-style head of state.",
        "tone": "orange",
    },
    {
        "id": "parl",
        "articles": "All 3 lists",
        "label": "Parliament supremacy",
        "slug": "ut-parliament-power",
        "detail": "Local assembly never erases Central legislative control.",
        "tone": "terracotta",
    },
    {
        "id": "legis",
        "articles": "3 of 8",
        "label": "UTs with legislature",
        "slug": "ut-with-legislature",
        "detail": "Delhi · Puducherry · J&K — competence exceptions differ.",
        "tone": "maroon",
    },
    {
        "id": "reg",
        "articles": "Art. 240",
        "label": "Presidential regulations",
        "slug": "ut-art240-regulations",
        "detail": "A&N, Lakshadweep, DNH+DD, Ladakh; Puducherry if dissolved.",
        "tone": "teal",
    },
    {
        "id": "hc",
        "articles": "Art. 241",
        "label": "High Courts for UTs",
        "slug": "ut-high-courts",
        "detail": "Only Delhi has its own HC; others under adjacent courts.",
        "tone": "olive",
    },
    {
        "id": "delhi",
        "articles": "69th · 239AA",
        "label": "Special provisions — NCT Delhi",
        "slug": "ut-nct-delhi",
        "detail": "Assembly 70 · CoM of 7 · no public order/police/land.",
        "tone": "gold",
    },
    {
        "id": "compare",
        "articles": "Table 41.2",
        "label": "States vs Union Territories",
        "slug": "ut-states-vs-uts",
        "detail": "Federal vs unitary · autonomy · Governor vs agent.",
        "tone": "orange",
    },
    {
        "id": "hmac",
        "articles": "MHA",
        "label": "MHA + HMAC / AAC",
        "slug": "ut-advisory-hmac",
        "detail": "Nodal ministry; advisory forums for UTs without legislature.",
        "tone": "terracotta",
    },
    {
        "id": "exam",
        "articles": "Revision",
        "label": "One-page quick revision",
        "slug": "ut-exam-anchors",
        "detail": "Prelims traps, PYQ themes, mains lines, 60-second sheet.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "ut-mental-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Enclave",
        "topic_label": "Union Territories",
        "subject_label": "Centre",
        "relation_label": "Directly administers",
        "protects_from": [
            "Federal power-sharing assumptions",
            "Treating assembly as statehood",
            "Confusing LG with Governor",
        ],
        "insight": (
            "UTs are central enclaves — unitary islands on a federal map. "
            "Popular local institutions never erase President + Parliament supremacy."
        ),
    },
    {
        "id": "ut-twelve-pillars",
        "type": "pillars",
        "title": "Twelve revision stops",
        "items": THEME_PILLARS,
    },
    {
        "id": "ut-revision-path",
        "type": "callout",
        "tone": "tip",
        "title": "Revision path",
        "body": (
            "Eight map → Article map (239–241) → Legislature trio → NCT Delhi → "
            "States vs UTs sheet → exam anchors. Cross-link Ch.6 for J&K/Ladakh creation."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Why UTs Exist & Creation Path",
        "slug": "ut-why-creation",
        "sort_order": 1,
        "summary": (
            "From scheduled districts to Part C/D to Union Territories (7th CAA, 1956) — "
            "plus four reasons UTs were created."
        ),
        "body": (
            "## Path to the UT label\n\n"
            "- British era: **scheduled districts (1874)** → later **Chief Commissioners’ Provinces**.\n"
            "- After independence: placed as **Part C States** and **Part D Territories**.\n"
            "- **1956:** 7th Constitutional Amendment + States Reorganisation Act → "
            "constituted as **Union Territories**.\n"
            "- Later elevations to statehood: Himachal Pradesh, Manipur, Tripura, Mizoram, "
            "Arunachal Pradesh, Goa.\n"
            "- Portuguese (Goa, Daman & Diu, Dadra & Nagar Haveli) and French (Puducherry) "
            "acquisitions were constituted as UTs.\n\n"
            "## Four creation reasons\n\n"
            "1. **Political & administrative** — Delhi, Chandigarh.\n"
            "2. **Cultural distinctiveness** — Puducherry, Dadra & Nagar Haveli and Daman & Diu.\n"
            "3. **Strategic importance** — Andaman & Nicobar, Lakshadweep.\n"
            "4. **Special care of tribal/backward people** — former NE UTs that later became states.\n\n"
            "## Recent map shifts (compressed)\n\n"
            "- **2019:** Erstwhile State of J&K → UT of J&K (with legislature) + UT of Ladakh "
            "(without legislature). Creation history → Ch.6 *Union and its Territory*.\n"
            "- **2020:** Dadra & Nagar Haveli + Daman & Diu merged (minimum government, "
            "maximum governance; end duplication).\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 41",
                "Creation of Union Territories — history, reasons, 2019/2020 shifts.",
            ),
            (
                "7th CAA, 1956",
                "With States Reorganisation Act — Part C/D → Union Territories.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-creation-timeline",
                "type": "timeline",
                "title": "Creation timeline",
                "events": [
                    {
                        "id": "e1874",
                        "year": 1874,
                        "label": "Scheduled districts",
                        "detail": "British-era special administration areas.",
                    },
                    {
                        "id": "e1950",
                        "year": 1950,
                        "label": "Parts A–D",
                        "detail": "Part C states + Part D territories under Central control.",
                    },
                    {
                        "id": "e1956",
                        "year": 1956,
                        "label": "UT label born",
                        "detail": "7th CAA + States Reorganisation Act.",
                    },
                    {
                        "id": "e2019",
                        "year": 2019,
                        "label": "J&K + Ladakh",
                        "detail": "Bifurcation into two UTs (legislature / no legislature).",
                    },
                    {
                        "id": "e2020",
                        "year": 2020,
                        "label": "DNH + DD merge",
                        "detail": "Single UT — Dadra and Nagar Haveli and Daman and Diu.",
                    },
                ],
            },
            {
                "id": "ut-why-pillars",
                "type": "pillars",
                "title": "Four reasons for UTs",
                "items": [
                    {
                        "id": "pol",
                        "articles": "Reason 1",
                        "label": "Political / admin",
                        "detail": "Delhi and Chandigarh.",
                        "tone": "teal",
                    },
                    {
                        "id": "cult",
                        "articles": "Reason 2",
                        "label": "Cultural distinctiveness",
                        "detail": "Puducherry; DNH and Daman & Diu.",
                        "tone": "olive",
                    },
                    {
                        "id": "strat",
                        "articles": "Reason 3",
                        "label": "Strategic importance",
                        "detail": "Andaman & Nicobar; Lakshadweep.",
                        "tone": "gold",
                    },
                    {
                        "id": "tribal",
                        "articles": "Reason 4",
                        "label": "Tribal / backward care",
                        "detail": "Former NE UTs — later elevated to states.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "ut-why-callout",
                "type": "callout",
                "tone": "note",
                "title": "2019 reasons (exam one-liners)",
                "body": (
                    "Ladakh: large, sparse, difficult terrain → UT **without** legislature. "
                    "J&K: internal security / cross-border terrorism context → UT **with** legislature."
                ),
            },
        ],
    },
    {
        "title": "Eight UTs at a Glance",
        "slug": "ut-eight-map",
        "sort_order": 2,
        "summary": (
            "Present map: 28 states + 8 UTs, no acquired territories — years, head, "
            "and whether each has a legislature."
        ),
        "body": (
            "## Present position\n\n"
            "Art. 1 territory: **states · union territories · acquired territories**. "
            "Today: **28 states, 8 UTs, no acquired territories**.\n\n"
            "| UT | Year | Head | Legislature |\n"
            "|---|---|---|---|\n"
            "| Andaman & Nicobar Islands | 1956 | Lt. Governor | No |\n"
            "| Delhi (NCT) | 1956 | Lt. Governor + CoM | Yes |\n"
            "| Lakshadweep | 1956 | Administrator | No |\n"
            "| Puducherry | 1962 | Lt. Governor + CoM | Yes |\n"
            "| Chandigarh | 1966 | Administrator | No |\n"
            "| Jammu & Kashmir | 2019 | Lt. Governor + CoM | Yes |\n"
            "| Ladakh | 2019 | Lt. Governor | No |\n"
            "| Dadra & Nagar Haveli and Daman & Diu | 2020 | Administrator | No |\n\n"
            "## Name / status notes\n\n"
            "- Lakshadweep renamed **1973** (from Laccadive, Minicoy and Amindivi Islands).\n"
            "- Delhi redesignated **NCT of Delhi** (1992 / 69th CAA).\n"
            "- Pondicherry → **Puducherry** (2006).\n"
            "- DNH (1961) + Daman & Diu (1962) → merged UT **2020**.\n\n"
            "**Mnemonic (ACDD-JLLP):** Andaman, Chandigarh, Delhi, Dadra–Daman, "
            "J&K, Ladakh, Lakshadweep, Puducherry.\n"
        ),
        "articles": [
            ("Art. 1", "Territory of India — states, UTs, acquired territories."),
            (
                "Laxmikanth Ch. 41",
                "Eight UTs with years of creation; LG vs Administrator map.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-eight-compare",
                "type": "comparison",
                "title": "With vs without legislature",
                "columns": [
                    {
                        "id": "with",
                        "heading": "With legislature (3)",
                        "points": [
                            "Delhi (NCT) — LG + CM + CoM",
                            "Puducherry — LG + CM + CoM",
                            "Jammu & Kashmir — LG + CM + CoM",
                        ],
                    },
                    {
                        "id": "without",
                        "heading": "Without legislature (5)",
                        "points": [
                            "Andaman & Nicobar — LG",
                            "Ladakh — LG",
                            "Chandigarh — Administrator",
                            "Lakshadweep — Administrator",
                            "DNH and Daman & Diu — Administrator",
                        ],
                    },
                ],
            },
            {
                "id": "ut-eight-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Trap",
                "body": (
                    "Eight UTs ≠ uniform administration. Same category, different heads, "
                    "different legislatures, different High Court arrangements."
                ),
            },
            {
                "id": "ut-eight-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "**ACDD-JLLP** — Andaman, Chandigarh, Delhi, Dadra–Daman, "
                    "J&K, Ladakh, Lakshadweep, Puducherry. "
                    "Legislature trio = **D-P-J** (Delhi, Puducherry, J&K)."
                ),
            },
        ],
    },
    {
        "title": "Constitutional Article Map (Part VIII)",
        "slug": "ut-article-map",
        "sort_order": 3,
        "summary": (
            "Articles 239 to 242 — administration, local legislatures, NCT Delhi, "
            "regulations, High Courts; Art. 242 repealed."
        ),
        "body": (
            "## Part VIII at a glance\n\n"
            "Arts **239–241** deal with Union Territories. There is **no uniformity** "
            "in administrative systems even though all UTs are one category.\n\n"
            "| Article | Subject |\n"
            "|---|---|\n"
            "| **239** | Administration of Union territories |\n"
            "| **239A** | Local legislatures / Council of Ministers for certain UTs |\n"
            "| **239AA** | Special provisions — Delhi |\n"
            "| **239AB** | Failure of constitutional machinery (Delhi) |\n"
            "| **239B** | Administrator’s ordinances during recess |\n"
            "| **240** | President’s regulations for certain UTs |\n"
            "| **241** | High Courts for Union territories |\n"
            "| **242** | Coorg — **repealed** |\n\n"
            "No separate Part for **acquired territories** — UT administration provisions apply to them too.\n"
        ),
        "articles": [
            ("Art. 239", "Administration of Union territories."),
            ("Art. 239A", "Local legislatures or Council of Ministers for certain UTs."),
            ("Art. 239AA", "Special provisions with respect to Delhi."),
            ("Art. 239AB", "Provision in case of failure of constitutional machinery."),
            ("Art. 239B", "Power of administrator to promulgate Ordinances during recess."),
            ("Art. 240", "Power of President to make regulations for certain UTs."),
            ("Art. 241", "High Courts for Union territories."),
            ("Art. 242", "Coorg — repealed."),
        ],
        "visual_blocks": [
            {
                "id": "ut-part-viii-tree",
                "type": "tree",
                "title": "Part VIII — constitutional map",
                "root": {
                    "id": "part8",
                    "label": "Part VIII — UTs",
                    "children": [
                        {
                            "id": "a239",
                            "label": "Art. 239",
                            "detail": "President → Administrator",
                            "slug": "ut-administrator-lg",
                        },
                        {
                            "id": "a239a",
                            "label": "Arts 239A / 239B",
                            "detail": "Local legislature · ordinances",
                            "slug": "ut-with-legislature",
                        },
                        {
                            "id": "a239aa",
                            "label": "Arts 239AA / 239AB",
                            "detail": "NCT Delhi special + failure clause",
                            "slug": "ut-nct-delhi",
                        },
                        {
                            "id": "a240",
                            "label": "Art. 240",
                            "detail": "Presidential regulations",
                            "slug": "ut-art240-regulations",
                        },
                        {
                            "id": "a241",
                            "label": "Art. 241",
                            "detail": "High Courts for UTs",
                            "slug": "ut-high-courts",
                        },
                        {
                            "id": "a242",
                            "label": "Art. 242",
                            "detail": "Coorg — repealed",
                        },
                    ],
                },
            },
            {
                "id": "ut-article-note",
                "type": "callout",
                "tone": "note",
                "title": "Acquired territories",
                "body": (
                    "Constitution has no separate admin scheme for acquired territories — "
                    "Part VIII UT rules apply to them as well."
                ),
            },
        ],
    },
    {
        "title": "Administrator & Lieutenant Governor",
        "slug": "ut-administrator-lg",
        "sort_order": 4,
        "summary": (
            "Every UT is administered by the President through an administrator — "
            "an agent of the President, not a head of state like a Governor."
        ),
        "body": (
            "## Core rule (Art. 239)\n\n"
            "- Every UT is administered by the **President** acting through an "
            "**administrator** appointed by him/her.\n"
            "- Administrator = **agent of the President**, **not** head of state "
            "(contrast: Governor of a state).\n"
            "- President may specify the designation: **Lieutenant Governor**, "
            "**Chief Commissioner**, or **Administrator**.\n\n"
            "## Present designations\n\n"
            "- **Lt. Governor:** Delhi, Puducherry, Andaman & Nicobar, J&K, Ladakh.\n"
            "- **Administrator:** Chandigarh, Dadra & Nagar Haveli and Daman & Diu, "
            "Lakshadweep.\n\n"
            "## Governor as UT administrator\n\n"
            "President may appoint the **Governor of a state** as administrator of an "
            "adjoining UT. In that capacity the Governor acts **independently of** "
            "his/her Council of Ministers.\n"
        ),
        "articles": [
            (
                "Art. 239",
                "UT administered by President through an administrator (agent).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-gov-vs-admin",
                "type": "comparison",
                "title": "Governor vs Administrator / LG",
                "columns": [
                    {
                        "id": "gov",
                        "heading": "Governor (State)",
                        "points": [
                            "Constitutional head of the state",
                            "Federal relationship with Centre",
                            "Uniform designation across states",
                            "Acts on CoM advice (with limited discretion)",
                        ],
                    },
                    {
                        "id": "admin",
                        "heading": "Administrator / LG (UT)",
                        "points": [
                            "Agent of the President",
                            "Unitary / direct Central control",
                            "Varied designations (LG / Admin / CC)",
                            "May be state Governor for adjoining UT — independent of state CoM",
                        ],
                    },
                ],
            },
            {
                "id": "ut-admin-flow",
                "type": "flowchart",
                "title": "Who heads the UT?",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "President appoints administrator",
                        "detail": "Art. 239 — agent of the President.",
                        "options": [
                            {"label": "Designate as LG", "next": "lg"},
                            {"label": "Designate as Administrator", "next": "adm"},
                            {"label": "Use adjoining state Governor", "next": "gov"},
                        ],
                    },
                    {
                        "id": "lg",
                        "label": "Lt. Governor",
                        "detail": "Delhi, Puducherry, A&N, J&K, Ladakh.",
                    },
                    {
                        "id": "adm",
                        "label": "Administrator",
                        "detail": "Chandigarh, DNH+DD, Lakshadweep.",
                    },
                    {
                        "id": "gov",
                        "label": "State Governor as UT admin",
                        "detail": "Acts independently of the state Council of Ministers.",
                    },
                ],
            },
            {
                "id": "ut-admin-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Prelims trap",
                "body": (
                    "LG / Administrator ≠ Governor. Same sounding office; different "
                    "constitutional character — **agent of President**, not head of state."
                ),
            },
        ],
    },
    {
        "title": "Powers of Parliament over UTs",
        "slug": "ut-parliament-power",
        "sort_order": 5,
        "summary": (
            "Parliament can make laws on any subject of the three lists for UTs — "
            "even those with local legislatures."
        ),
        "body": (
            "## Supreme Central control\n\n"
            "- Parliament can legislate on **any subject of the three lists** "
            "(including the **State List**) for Union Territories.\n"
            "- This power **extends to** Puducherry, Delhi and J&K even though they "
            "have local legislatures.\n"
            "- Establishing a local legislature does **not diminish** the supreme "
            "control of the **President and Parliament**.\n\n"
            "## Revision line\n\n"
            "**Assembly ≠ statehood.** Local democratic institutions coexist with "
            "full Central legislative supremacy over the UT.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 41",
                "Parliament’s power on all three lists for UTs remains unaffected.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-parl-model",
                "type": "mental_model",
                "title": "Mental model",
                "metaphor": "Override",
                "topic_label": "Parliament & UTs",
                "subject_label": "Parliament",
                "relation_label": "Can legislate on",
                "protects_from": [
                    "Assuming State List is reserved for UT assemblies",
                    "Treating Delhi/Puducherry/J&K as full states",
                ],
                "insight": (
                    "For UTs, Parliament’s State List power survives even after a "
                    "local legislature is created."
                ),
            },
            {
                "id": "ut-parl-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Trap",
                "body": (
                    "Do not say: ‘Once an assembly exists, Parliament loses State List "
                    "power over that UT.’ False — control remains supreme."
                ),
            },
        ],
    },
    {
        "title": "UTs with Legislature",
        "slug": "ut-with-legislature",
        "sort_order": 6,
        "summary": (
            "Puducherry (1963), Delhi (1992) and J&K (2019) have Assembly + CoM — "
            "with different State List exceptions."
        ),
        "body": (
            "## Three UTs with popular institutions\n\n"
            "Puducherry (1963), Delhi (1992) and Jammu & Kashmir (2019) have a "
            "**legislative assembly** and a **council of ministers** headed by a CM. "
            "The other **six** UTs do not.\n\n"
            "## Legislative competence\n\n"
            "| UT | Assembly size | Can make laws on | Exceptions |\n"
            "|---|---|---|---|\n"
            "| **Puducherry** | 30 | State List + Concurrent List | — |\n"
            "| **Delhi (NCT)** | 70 | State List + Concurrent List | **Public order, police, land** |\n"
            "| **J&K** | 83 | State List + Concurrent List | **Public order, police** |\n\n"
            "Parliament’s laws **prevail**; Parliament’s State List power over UTs "
            "remains intact.\n\n"
            "Ladakh is a separate UT **without** legislature. For 2019 creation path → "
            "Ch.6 cluster on J&K & Ladakh.\n"
        ),
        "articles": [
            (
                "Art. 239A",
                "Creation of local legislatures / CoM for certain Union territories.",
            ),
            (
                "Art. 239AA",
                "Special provisions — NCT Delhi legislative competence.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-legis-compare",
                "type": "comparison",
                "title": "Legislature trio — competence",
                "columns": [
                    {
                        "id": "pud",
                        "heading": "Puducherry (30)",
                        "points": [
                            "Full State List + Concurrent",
                            "No State List carve-outs in the book table",
                            "Art. 240 only if assembly suspended/dissolved",
                        ],
                    },
                    {
                        "id": "del",
                        "heading": "Delhi (70)",
                        "points": [
                            "State + Concurrent",
                            "Except: public order, police, land",
                            "Parliament prevails",
                        ],
                    },
                    {
                        "id": "jk",
                        "heading": "J&K (83)",
                        "points": [
                            "State + Concurrent",
                            "Except: public order, police",
                            "Land not carved out like Delhi",
                        ],
                    },
                ],
            },
            {
                "id": "ut-legis-pillars",
                "type": "pillars",
                "title": "With vs without",
                "items": [
                    {
                        "id": "yes",
                        "articles": "3 UTs",
                        "label": "With Assembly + CoM",
                        "detail": "Delhi · Puducherry · J&K — still under President/Parliament.",
                        "tone": "teal",
                    },
                    {
                        "id": "no",
                        "articles": "5 UTs",
                        "label": "No popular legislature",
                        "detail": "A&N · Chandigarh · DNH+DD · Lakshadweep · Ladakh.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "ut-legis-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exception mnemonic",
                "body": (
                    "Delhi bans **3**: Public order, Police, Land (**PPL**). "
                    "J&K bans **2**: Public order, Police (**PP**). "
                    "Puducherry: full State List (in this chapter’s frame)."
                ),
            },
        ],
    },
    {
        "title": "Presidential Regulations (Art. 240)",
        "slug": "ut-art240-regulations",
        "sort_order": 7,
        "summary": (
            "President may make regulations for peace, progress and good government "
            "of specified UTs — with a special rule for Puducherry."
        ),
        "body": (
            "## Where Art. 240 applies\n\n"
            "President can make regulations for:\n"
            "- Andaman & Nicobar Islands\n"
            "- Lakshadweep\n"
            "- Dadra & Nagar Haveli and Daman & Diu\n"
            "- **Ladakh**\n\n"
            "## Puducherry special rule\n\n"
            "For Puducherry, the President can legislate by regulation **only when** "
            "the assembly is **suspended or dissolved**.\n\n"
            "## Force of a regulation\n\n"
            "- Same force and effect as an **Act of Parliament**.\n"
            "- May **repeal or amend** any Act of Parliament **in relation to** "
            "these union territories.\n"
        ),
        "articles": [
            (
                "Art. 240",
                "Power of President to make regulations for certain Union territories.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-240-flow",
                "type": "flowchart",
                "title": "Can the President regulate?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Which UT?",
                        "options": [
                            {
                                "label": "A&N / Lakshadweep / DNH+DD / Ladakh",
                                "next": "always",
                            },
                            {"label": "Puducherry", "next": "pud"},
                            {"label": "Delhi / J&K / Chandigarh", "next": "no"},
                        ],
                    },
                    {
                        "id": "always",
                        "label": "Art. 240 available",
                        "detail": "Regulations for peace, progress and good government.",
                    },
                    {
                        "id": "pud",
                        "label": "Only if assembly suspended/dissolved",
                        "detail": "Otherwise local legislature occupies the space.",
                    },
                    {
                        "id": "no",
                        "label": "Not in the Art. 240 list (this chapter)",
                        "detail": "Use ordinary Parliament / NCT / other routes.",
                    },
                ],
            },
            {
                "id": "ut-240-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Trap",
                "body": (
                    "Art. 240 for Puducherry is **conditional**. Do not mark it as always "
                    "available like A&N or Lakshadweep."
                ),
            },
        ],
    },
    {
        "title": "High Courts for Union Territories",
        "slug": "ut-high-courts",
        "sort_order": 8,
        "summary": (
            "Parliament may establish a High Court for a UT or place it under an "
            "adjacent High Court — only Delhi has its own."
        ),
        "body": (
            "## Art. 241 rule\n\n"
            "Parliament can **establish a High Court** for a UT or put it under the "
            "jurisdiction of the High Court of an **adjacent state**.\n\n"
            "## Jurisdiction map\n\n"
            "| UT | Judiciary |\n"
            "|---|---|\n"
            "| Delhi | **Own High Court** (since 1966) |\n"
            "| Andaman & Nicobar | Calcutta High Court |\n"
            "| Chandigarh | Punjab & Haryana High Court |\n"
            "| DNH and Daman & Diu | Bombay High Court |\n"
            "| Lakshadweep | Kerala High Court |\n"
            "| Puducherry | Madras High Court |\n"
            "| J&K and Ladakh | Common **J&K & Ladakh High Court** |\n"
        ),
        "articles": [
            (
                "Art. 241",
                "High Courts for Union territories — establish or extend jurisdiction.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-hc-compare",
                "type": "comparison",
                "title": "HC map for UTs",
                "columns": [
                    {
                        "id": "own",
                        "heading": "Own / common HC",
                        "points": [
                            "Delhi — separate High Court (1966)",
                            "J&K + Ladakh — common J&K & Ladakh HC",
                        ],
                    },
                    {
                        "id": "adjacent",
                        "heading": "Under adjacent HC",
                        "points": [
                            "A&N → Calcutta",
                            "Chandigarh → Punjab & Haryana",
                            "DNH+DD → Bombay",
                            "Lakshadweep → Kerala",
                            "Puducherry → Madras",
                        ],
                    },
                ],
            },
            {
                "id": "ut-hc-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims fact",
                "body": (
                    "Only **Delhi** among UTs has a High Court of its own. "
                    "J&K and Ladakh share one common High Court."
                ),
            },
        ],
    },
    {
        "title": "Special Provisions — NCT of Delhi",
        "slug": "ut-nct-delhi",
        "sort_order": 9,
        "summary": (
            "69th CAA: NCT status, LG, Assembly of 70, CoM of 7, competence carve-outs, "
            "LG–Council differences, President’s rule analogue, ordinances."
        ),
        "body": (
            "## 69th Constitutional Amendment (w.e.f. 1 Feb 1992)\n\n"
            "- Redesignated Delhi as **National Capital Territory of Delhi**.\n"
            "- Administrator designated **Lieutenant Governor**.\n"
            "- Created **Legislative Assembly** + **Council of Ministers**.\n\n"
            "## Assembly & legislation\n\n"
            "- Strength fixed at **70**; elections by **ECI**.\n"
            "- Laws on State List + Concurrent List **except** public order, police, land.\n"
            "- **Laws of Parliament prevail** over Assembly laws.\n\n"
            "## Council of Ministers\n\n"
            "- Strength = **10% of 70 = 7** (CM + 6 ministers).\n"
            "- **CM appointed by the President** (not by the LG).\n"
            "- Other ministers appointed by the President on CM’s advice.\n"
            "- Hold office during the **pleasure of the President**.\n"
            "- Collectively responsible to the Assembly.\n\n"
            "## LG and the Council\n\n"
            "- CoM aids and advises the LG except where LG must act in **discretion**.\n"
            "- Difference of opinion → LG **refers to the President** and acts accordingly.\n\n"
            "## Failure of constitutional machinery (≈ Art. 356)\n\n"
            "If administration cannot be carried on under these provisions, President may "
            "suspend them (on LG’s report or otherwise) and make incidental provisions — "
            "Delhi’s analogue of President’s Rule (**Art. 239AB** theme).\n\n"
            "## LG ordinances\n\n"
            "- During recess of the Assembly; same force as an Act.\n"
            "- Need **prior permission of the President**.\n"
            "- Must be approved within **six weeks** of reassembly; can be withdrawn anytime.\n"
            "- **Cannot** promulgate when Assembly is dissolved or suspended.\n"
        ),
        "articles": [
            ("Art. 239AA", "Special provisions with respect to Delhi."),
            ("Art. 239AB", "Failure of constitutional machinery in NCT Delhi."),
            ("Art. 239B", "Administrator’s ordinance power during recess."),
            (
                "69th CAA, 1991",
                "NCT status, LG designation, Assembly and Council of Ministers.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-delhi-pillars",
                "type": "pillars",
                "title": "NCT Delhi — must-memorise",
                "items": [
                    {
                        "id": "asm",
                        "articles": "70",
                        "label": "Assembly",
                        "detail": "Directly elected; ECI; no PPL subjects.",
                        "tone": "teal",
                    },
                    {
                        "id": "com",
                        "articles": "7",
                        "label": "Council of Ministers",
                        "detail": "10% of 70; CM by President; pleasure of President.",
                        "tone": "olive",
                    },
                    {
                        "id": "lg",
                        "articles": "239AA",
                        "label": "LG–Council clash",
                        "detail": "Difference → refer to President.",
                        "tone": "gold",
                    },
                    {
                        "id": "pr",
                        "articles": "239AB",
                        "label": "President’s rule analogue",
                        "detail": "Suspend special provisions ≈ Art. 356 logic.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "ut-delhi-flow",
                "type": "flowchart",
                "title": "LG and ministers disagree",
                "root": "diff",
                "steps": [
                    {
                        "id": "diff",
                        "label": "Difference of opinion (LG vs CoM)",
                        "detail": "Aid-and-advise fails on a matter.",
                        "options": [
                            {"label": "What must LG do?", "next": "ref"},
                        ],
                    },
                    {
                        "id": "ref",
                        "label": "Refer to the President",
                        "detail": "LG acts according to the President’s decision.",
                    },
                ],
            },
            {
                "id": "ut-delhi-exam",
                "type": "callout",
                "tone": "note",
                "title": "Exam layer (not a book rewrite)",
                "body": (
                    "PYQ themes: LG vs elected government; public order/police/land; "
                    "services conflicts; democracy in the national capital vs Central control. "
                    "Case anchors: NDMC v. State of Punjab (239AA validity theme); "
                    "Govt. of NCT of Delhi v. UoI (2018 — LG–Council relationship). "
                    "Watch current affairs for later services-related holdings."
                ),
            },
        ],
    },
    {
        "title": "States vs Union Territories",
        "slug": "ut-states-vs-uts",
        "sort_order": 10,
        "summary": (
            "Seven-point contrast — federal vs unitary relation, autonomy, "
            "administrative uniformity, and Parliament’s State List power."
        ),
        "body": (
            "## Table 41.2 redesign\n\n"
            "Use this as a last-minute comparison sheet. States sit in a **federal** "
            "relationship; UTs are under **direct Central administration** — a "
            "conspicuous unitary departure within India’s federal map.\n\n"
            "**Mnemonic F.A.U.G.H.P.** (state side): Federal · Autonomy · Uniform admin · "
            "Governor · Head of state · Parliament limited on State List — "
            "flip each for UTs.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 41",
                "Comparing States and Union Territories — Table 41.2.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-states-compare",
                "type": "comparison",
                "title": "States vs Union Territories",
                "columns": [
                    {
                        "id": "states",
                        "heading": "States",
                        "points": [
                            "Relationship with Centre is federal",
                            "Share distribution of power with Centre",
                            "Have autonomy",
                            "Uniform administrative set-up",
                            "Executive head = Governor",
                            "Governor is constitutional head of the state",
                            "Parliament ordinarily cannot legislate on State List",
                        ],
                    },
                    {
                        "id": "uts",
                        "heading": "Union Territories",
                        "points": [
                            "Relationship with Centre is unitary",
                            "Under direct control and administration of Centre",
                            "Do not have autonomy",
                            "No uniformity in administrative set-up",
                            "Head = Administrator / LG / Chief Commissioner",
                            "Administrator is an agent of the President",
                            "Parliament can legislate on any of the three lists",
                        ],
                    },
                ],
            },
            {
                "id": "ut-states-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid — F.A.U.G.H.P.",
                "body": (
                    "**F**ederal · **A**utonomy · **U**niform · **G**overnor · "
                    "**H**ead of state · **P**arliament limited — states. "
                    "UTs = opposite on each letter."
                ),
            },
        ],
    },
    {
        "title": "MHA & Advisory Committees",
        "slug": "ut-advisory-hmac",
        "sort_order": 11,
        "summary": (
            "Ministry of Home Affairs is the nodal ministry; HMAC/AAC advise on "
            "development for UTs without legislature."
        ),
        "body": (
            "## Nodal ministry\n\n"
            "Under the Government of India (Allocation of Business) Rules, 1961, "
            "**Ministry of Home Affairs** is the nodal ministry for all UT matters "
            "relating to legislation, finance and budget, services, and appointment of "
            "Lt. Governors and Administrators.\n\n"
            "## HMAC / AAC\n\n"
            "The **five UTs without legislature** (A&N, Chandigarh, DNH+DD, Lakshadweep, "
            "Ladakh) have:\n"
            "- **Home Minister’s Advisory Committee (HMAC)** — chaired by Union Home Minister, or\n"
            "- **Administrator’s Advisory Committee (AAC)** — chaired by the Administrator.\n\n"
            "Members include MPs and elected members from local bodies "
            "(District Panchayats and Municipal Councils), among others. "
            "These forums discuss social and economic development issues of the UTs.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 41",
                "MHA nodal role; HMAC/AAC for UTs without legislature.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-mha-flow",
                "type": "flowchart",
                "title": "Central channel for UTs",
                "root": "mha",
                "steps": [
                    {
                        "id": "mha",
                        "label": "Ministry of Home Affairs",
                        "detail": "Nodal — legislation, finance/budget, services, LG/Admin appointments.",
                        "options": [
                            {"label": "UT with legislature", "next": "with"},
                            {"label": "UT without legislature", "next": "without"},
                        ],
                    },
                    {
                        "id": "with",
                        "label": "LG + Assembly + CoM path",
                        "detail": "Delhi · Puducherry · J&K — still under Presidential/Parliamentary supremacy.",
                    },
                    {
                        "id": "without",
                        "label": "HMAC / AAC advisory forum",
                        "detail": "Home Minister or Administrator chairs; MPs + local body members.",
                    },
                ],
            },
            {
                "id": "ut-hmac-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims fact",
                "body": (
                    "HMAC/AAC exist for the **five UTs without legislature** — not for "
                    "Delhi, Puducherry, or J&K."
                ),
            },
        ],
    },
    {
        "title": "Exam Anchors — Quick Revision",
        "slug": "ut-exam-anchors",
        "sort_order": 12,
        "summary": (
            "Prelims facts, PYQ themes, mains value-adds, memory aids, and a "
            "60-second revision sheet for Ch.41."
        ),
        "body": (
            "## Prelims facts\n\n"
            "- **8 UTs**, **28 states**, no acquired territories.\n"
            "- **3 with legislature:** Delhi, Puducherry, J&K.\n"
            "- Delhi exceptions: **public order, police, land**; J&K: **public order, police**.\n"
            "- Administrator / LG = **agent of President**, not Governor.\n"
            "- Parliament: **all three lists** for every UT.\n"
            "- Art. 240: A&N, Lakshadweep, DNH+DD, Ladakh; Puducherry only if "
            "assembly suspended/dissolved.\n"
            "- Only **Delhi** has its own High Court; J&K & Ladakh share one.\n"
            "- NCT CoM = **7**; CM appointed by **President**.\n"
            "- Art. **242** (Coorg) repealed.\n"
            "- DNH+DD merger year: **2020**; J&K/Ladakh: **2019**.\n\n"
            "## PYQ themes\n\n"
            "- States vs UTs (federal vs unitary).\n"
            "- NCT legislative competence and LG–Council relationship.\n"
            "- Parliament’s power over UTs with assemblies.\n"
            "- Administrator as agent of President.\n"
            "- Part VIII article identification (239–241).\n\n"
            "## Mains value-adds\n\n"
            "- UTs as **unitary enclaves** in a federal polity.\n"
            "- Rationale tension: strategic/cultural needs vs democratic deficit "
            "in UTs without legislature.\n"
            "- NCT Delhi as a unique experiment — representative government under "
            "Central overhang.\n"
            "- Art. 240 regulations as a residual unitary tool.\n\n"
            "## Memory spine\n\n"
            "1. **ACDD-JLLP** eight UTs; **D-P-J** legislature trio.\n"
            "2. **PPL** (Delhi) / **PP** (J&K) carve-outs.\n"
            "3. **F.A.U.G.H.P.** states vs opposite for UTs.\n"
            "4. Agent ≠ Governor; Assembly ≠ statehood.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 41",
                "Full chapter revision sheet — prelims, mains, memory.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ut-exam-pillars",
                "type": "pillars",
                "title": "Exam three-pack",
                "items": [
                    {
                        "id": "pre",
                        "articles": "Facts",
                        "label": "Prelims",
                        "detail": "8 UTs · D-P-J · PPL/PP · agent · Art. 240 · Delhi HC.",
                        "tone": "teal",
                    },
                    {
                        "id": "mains",
                        "articles": "Structure",
                        "label": "Mains",
                        "detail": "Unitary enclaves · NCT experiment · Art. 240 tool.",
                        "tone": "olive",
                    },
                    {
                        "id": "traps",
                        "articles": "Avoid",
                        "label": "Traps",
                        "detail": "LG≠Governor; assembly≠statehood; Puducherry Art. 240 conditional.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "ut-numbers-compare",
                "type": "comparison",
                "title": "Must-memorise numbers",
                "columns": [
                    {
                        "id": "map",
                        "heading": "Map & sizes",
                        "points": [
                            "28 states + 8 UTs",
                            "Delhi Assembly 70",
                            "Puducherry Assembly 30",
                            "J&K Assembly 83",
                            "Delhi CoM = 7 (10%)",
                        ],
                    },
                    {
                        "id": "years",
                        "heading": "Years & articles",
                        "points": [
                            "1956 UT label (7th CAA)",
                            "69th CAA → NCT (1992)",
                            "2019 J&K + Ladakh",
                            "2020 DNH+DD merge",
                            "Arts 239–241 (242 repealed)",
                        ],
                    },
                ],
            },
            {
                "id": "ut-revision-sheet",
                "type": "callout",
                "tone": "tip",
                "title": "60-second revision",
                "body": (
                    "Central enclaves → 8 UTs (ACDD-JLLP) → 3 with legislature (D-P-J) → "
                    "agent ≠ Governor → Parliament all lists → Art. 240 list + Puducherry "
                    "condition → Delhi PPL / CoM 7 / CM by President → only Delhi own HC → "
                    "F.A.U.G.H.P. states vs opposite."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "ut-why-creation"),
    (HUB_SLUG, "parent", "ut-eight-map"),
    (HUB_SLUG, "parent", "ut-article-map"),
    (HUB_SLUG, "parent", "ut-administrator-lg"),
    (HUB_SLUG, "parent", "ut-parliament-power"),
    (HUB_SLUG, "parent", "ut-with-legislature"),
    (HUB_SLUG, "parent", "ut-art240-regulations"),
    (HUB_SLUG, "parent", "ut-high-courts"),
    (HUB_SLUG, "parent", "ut-nct-delhi"),
    (HUB_SLUG, "parent", "ut-states-vs-uts"),
    (HUB_SLUG, "parent", "ut-advisory-hmac"),
    (HUB_SLUG, "parent", "ut-exam-anchors"),
    ("ut-why-creation", "related", "union-and-its-territory"),
    ("ut-why-creation", "related", "uit-jk-ladakh-2019"),
    ("ut-eight-map", "related", "uit-jk-ladakh-2019"),
    ("ut-with-legislature", "related", "uit-jk-ladakh-2019"),
    ("ut-parliament-power", "related", "federal-system"),
    ("ut-parliament-power", "related", "union-and-its-territory"),
    ("ut-administrator-lg", "related", "governor"),
    ("ut-states-vs-uts", "related", "federal-system"),
    ("ut-states-vs-uts", "related", "governor"),
    ("ut-nct-delhi", "related", "emergency-provisions"),
    ("ut-nct-delhi", "related", "ut-with-legislature"),
    ("ut-art240-regulations", "related", "ut-with-legislature"),
    ("ut-high-courts", "related", "high-court"),
    ("ut-exam-anchors", "related", "ut-states-vs-uts"),
    ("ut-exam-anchors", "related", "ut-nct-delhi"),
    ("ut-article-map", "related", "ut-nct-delhi"),
]

SAMPLE_PYQS = [
    (
        2017,
        "With reference to the administration of Union Territories in India, consider the "
        "following statements: An administrator of a UT is an agent of the President and "
        "not a head of state like a Governor. Which of the statements given is/are correct?",
        "Correct — under Art. 239 the administrator is an agent of the President; "
        "designation may be LG / Chief Commissioner / Administrator.",
        [HUB_SLUG, "ut-administrator-lg", "ut-exam-anchors"],
    ),
    (
        2015,
        "Which of the following is/are true of the legislative competence of the NCT of Delhi? "
        "The Assembly can legislate on State List subjects except public order, police and land; "
        "Parliament’s laws prevail.",
        "Both themes are correct under the 69th CAA / Art. 239AA framework as summarised "
        "in Ch.41 — Assembly 70; carve-outs PPL; Parliament prevails.",
        ["ut-nct-delhi", "ut-with-legislature"],
    ),
    (
        2013,
        "Parliament can make laws for Union Territories on subjects in the State List. "
        "Does creating a local legislature for a UT take away this power?",
        "No. Parliament’s power on all three lists for UTs remains unaffected even after "
        "a local legislature is established (Puducherry, Delhi, J&K included).",
        ["ut-parliament-power", HUB_SLUG],
    ),
    (
        2019,
        "Distinguish the constitutional position of States and Union Territories with "
        "respect to their relationship with the Centre.",
        "States: federal relationship, autonomy, power-sharing, Governor as constitutional "
        "head, Parliament ordinarily barred from State List. UTs: unitary/direct Central "
        "control, no autonomy, non-uniform admin, administrator as Presidential agent, "
        "Parliament can legislate on all three lists.",
        ["ut-states-vs-uts", "ut-exam-anchors"],
    ),
    (
        2021,
        "Under Article 240, the President may make regulations for certain Union Territories. "
        "For which territories, and what is special about Puducherry?",
        "Art. 240 covers A&N, Lakshadweep, DNH+DD and Ladakh. For Puducherry, regulations "
        "only when the assembly is suspended or dissolved. A regulation has the force of "
        "an Act of Parliament and may amend/repeal Parliament’s Act for that UT.",
        ["ut-art240-regulations", "ut-exam-anchors"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "NDMC v. State of Punjab",
        "slug": "ndmc-v-state-of-punjab",
        "parties": "New Delhi Municipal Council v. State of Punjab",
        "year": 1997,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Exam anchor for NCT / Art. 239AA special status themes — national capital "
            "under Central legislative overhang."
        ),
        "holding": (
            "Often cited in debates on Delhi’s special constitutional position and "
            "the validity/operation of Art. 239AA arrangements for the national capital."
        ),
        "concept_slugs": [HUB_SLUG, "ut-nct-delhi", "ut-exam-anchors"],
    },
    {
        "title": "Government of NCT of Delhi v. Union of India",
        "slug": "gnctd-v-uoi-2018",
        "parties": "Government of NCT of Delhi v. Union of India",
        "year": 2018,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Landmark on LG–Council relationship under Art. 239AA — representative "
            "democracy in NCT vs Central control."
        ),
        "holding": (
            "Clarified that the LG is bound by the aid and advice of the Council of Ministers "
            "except where the Constitution expressly requires discretionary action; "
            "differences are referred to the President as provided."
        ),
        "concept_slugs": [HUB_SLUG, "ut-nct-delhi", "ut-exam-anchors"],
    },
]

AMENDMENTS = [
    {
        "number": 7,
        "year": 1956,
        "title": "Seventh Amendment",
        "summary": (
            "With the States Reorganisation Act, reconstituted Part C/D territories as "
            "Union Territories and reorganised the state map."
        ),
        "effect": "Birth of the constitutional category ‘Union Territories’.",
        "concept_slugs": [HUB_SLUG, "ut-why-creation", "ut-eight-map"],
    },
    {
        "number": 69,
        "year": 1991,
        "title": "Sixty-ninth Amendment",
        "summary": (
            "Special status for Delhi — redesignated National Capital Territory; "
            "LG designation; Legislative Assembly and Council of Ministers (w.e.f. 1 Feb 1992)."
        ),
        "effect": "Inserted/operationalised Art. 239AA framework for NCT Delhi.",
        "concept_slugs": [HUB_SLUG, "ut-nct-delhi", "ut-with-legislature"],
    },
]


class Command(BaseCommand):
    help = "Seed Union Territories chapter (Laxmikanth Ch.41 visual revision)."

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
                "title": "Union Territories",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 41, pp. 587–593",
                "summary": (
                    "Visual revision of Ch.41 — Part VIII Arts 239–241, eight UTs, "
                    "Administrator/LG, Parliament supremacy, NCT Delhi, States vs UTs."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="union-territories-and-special-areas"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Union Territories",
                "summary": (
                    "Part VIII administration of UTs — eight territories, non-uniform "
                    "setup, Arts 239–241, NCT Delhi special status."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **central enclaves** mental model, then scan the "
                    "**twelve stops**. Lock the **eight-UT map**, **article map**, and "
                    "**legislature trio**, then drill **NCT Delhi** and **States vs UTs**. "
                    "Finish with exam anchors. "
                    "J&K/Ladakh **creation** history lives in Ch.6 — this chapter owns "
                    "**administration**. "
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
            ref="Laxmikanth Ch. 41",
            excerpt=(
                "Union Territories — Part VIII Arts 239–241, administration, "
                "NCT Delhi, States vs UTs."
            ),
            sort_order=0,
        )

        ut_slugs = set(by_slug.keys())
        related_outside = {
            "union-and-its-territory",
            "uit-jk-ladakh-2019",
            "federal-system",
            "governor",
            "emergency-provisions",
            "high-court",
        }
        ConceptEdge.objects.filter(
            Q(source__slug__in=ut_slugs) | Q(target__slug__in=ut_slugs),
            source__subject=subject,
        ).filter(
            Q(source__slug__in=ut_slugs | related_outside)
            | Q(target__slug__in=ut_slugs | related_outside)
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
                by_slug[s]
                for s in case_data["concept_slugs"]
                if s in by_slug
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
                by_slug[s]
                for s in amd_data["concept_slugs"]
                if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Union Territories chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments."
            )
        )
