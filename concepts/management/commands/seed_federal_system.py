"""Seed Laxmikanth Ch.14 Federal System (visual revision chapter)."""

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

HUB_SLUG = "federal-system"
CHAPTER_SLUG = "federal-system"

REVISION_PILLARS = [
    {
        "id": "fed-vs-uni",
        "articles": "Table 14.1",
        "label": "Federal vs Unitary",
        "slug": "fs-federal-vs-unitary",
        "detail": "Dual polity vs single government — seven classic contrasts.",
        "tone": "teal",
    },
    {
        "id": "why",
        "articles": "Framers",
        "label": "Why Federalism in India",
        "slug": "fs-why-federal",
        "detail": "Size + diversity → national unity with regional autonomy.",
        "tone": "olive",
    },
    {
        "id": "union",
        "articles": "Art. 1 · 3",
        "label": "Union of States",
        "slug": "fs-union-of-states",
        "detail": "Not ‘Federation’ — no agreement, no secession; Art. 3 tilt.",
        "tone": "gold",
    },
    {
        "id": "canada",
        "articles": "Model",
        "label": "Canadian Model",
        "slug": "fs-canadian-model",
        "detail": "Disintegration + ‘Union’ + strong Centre — not the US model.",
        "tone": "orange",
    },
    {
        "id": "seven",
        "articles": "7 features",
        "label": "Seven Federal Features",
        "slug": "fs-federal-features",
        "detail": "Dual · Written · Division · Supremacy · Rigid · Independent · Bicameral.",
        "tone": "terracotta",
    },
    {
        "id": "fourteen",
        "articles": "14 features",
        "label": "Fourteen Unitary Features",
        "slug": "fs-unitary-features",
        "detail": "Power / Structural / State / Amendment buckets — P-S-S-A.",
        "tone": "maroon",
    },
    {
        "id": "labels",
        "articles": "Scholars",
        "label": "Expert Labels + Ambedkar",
        "slug": "fs-expert-labels",
        "detail": "Quasi-federal to cooperative — match thinker to phrase.",
        "tone": "teal",
    },
    {
        "id": "bommai",
        "articles": "1994",
        "label": "Bommai + Federal Spirit",
        "slug": "fs-bommai-spirit",
        "detail": "Federalism is a basic feature; exceptions ≠ the rule.",
        "tone": "olive",
    },
    {
        "id": "toolkit",
        "articles": "60-sec",
        "label": "Quick Revision Toolkit",
        "slug": "fs-revision-toolkit",
        "detail": "7 vs 14 · India–US–Canada · article pins · PYQ themes.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "fs-switchboard-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Switchboard",
        "topic_label": "Federal System",
        "subject_label": "Union of States",
        "relation_label": "Helps you avoid",
        "protects_from": [
            "Calling India a ‘federation of states’",
            "Mixing independent vs integrated judiciary",
            "Treating emergency overrides as the federal rule",
            "Confusing US equality of states with India’s RS seats",
        ],
        "insight": (
            "Normal mode = dual polity; exceptional dials (emergency, Art. 249, Art. 3) "
            "pull power to the Centre without rewriting the Constitution."
        ),
    },
    {
        "id": "fs-nine-pillars",
        "type": "pillars",
        "title": "Nine revision clusters",
        "items": REVISION_PILLARS,
    },
    {
        "id": "fs-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Identity card (30 seconds)",
        "body": (
            "India is a **Union of States** (Art. 1) — not an agreement-based federation; "
            "states cannot secede. Federal form + unitary tilt. Bommai (1994): federalism is a "
            "**basic feature**. Open clusters below for 7 federal vs 14 unitary features."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Federal vs Unitary",
        "slug": "fs-federal-vs-unitary",
        "sort_order": 1,
        "summary": "Definitions, foedus etymology, integration vs disintegration, Table 14.1 contrasts.",
        "body": (
            "## Federal vs unitary\n\n"
            "- **Unitary:** all powers in the national government; regional units (if any) derive "
            "authority from it (Britain, France, Japan, China).\n"
            "- **Federal:** Constitution itself divides powers between national and regional "
            "governments; both operate independently in their spheres (US, Switzerland, Australia, "
            "Canada, Russia, Brazil).\n\n"
            "**Etymology:** *foedus* (Latin) = treaty / agreement. A federation is a new state formed "
            "by treaty or agreement among units (states / cantons / provinces / republics).\n\n"
            "**Two formation paths**\n"
            "- **Integration:** weak/independent units unite → strong Union (US, 1787; oldest federation).\n"
            "- **Disintegration:** a big unitary state grants provincial autonomy (Canada, 1867; "
            "also India’s path).\n\n"
            "US = model federation (50 states, originally 13). Canada = 10 provinces (originally 4)."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "fs-table-14-1",
                "type": "comparison",
                "title": "Table 14.1 — Federal vs Unitary",
                "columns": [
                    {
                        "id": "federal",
                        "heading": "Federal government",
                        "points": [
                            "Dual government (national + regional)",
                            "Written Constitution",
                            "Division of powers by the Constitution",
                            "Supremacy of the Constitution",
                            "Rigid Constitution",
                            "Independent judiciary",
                            "Bicameral legislature",
                        ],
                    },
                    {
                        "id": "unitary",
                        "heading": "Unitary government",
                        "points": [
                            "Single national government (may create regions)",
                            "Written (France) or unwritten (Britain)",
                            "No division — all powers with Centre",
                            "May or may not be supreme (Japan vs Britain)",
                            "May be rigid (France) or flexible (Britain)",
                            "Judiciary may or may not be independent",
                            "May be bicameral (Britain) or unicameral (China)",
                        ],
                    },
                ],
            },
            {
                "id": "fs-fed-uni-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "UPSC often asks ‘which is a federal feature?’ using this exact seven-point list. "
                    "Memorise the federal column first."
                ),
            },
        ],
    },
    {
        "title": "Why Federalism in India",
        "slug": "fs-why-federal",
        "sort_order": 2,
        "summary": "Large size + socio-cultural diversity — unity reconciled with regional autonomy.",
        "body": (
            "## Why the framers chose federalism\n\n"
            "Two main reasons:\n"
            "1. **Large size** of the country\n"
            "2. **Socio-cultural diversity**\n\n"
            "Federal design was meant to ensure **efficient governance** and to reconcile "
            "**national unity** with **regional autonomy**.\n\n"
            "Mnemonic: **Unity + Autonomy** — one Union, many regions with constitutionally "
            "assigned spheres."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "fs-why-pillars",
                "type": "pillars",
                "title": "Two framers’ reasons",
                "items": [
                    {
                        "id": "size",
                        "articles": "Reason 1",
                        "label": "Large size",
                        "slug": "fs-why-federal",
                        "detail": "One Centre cannot efficiently administer every local need alone.",
                        "tone": "teal",
                    },
                    {
                        "id": "diversity",
                        "articles": "Reason 2",
                        "label": "Socio-cultural diversity",
                        "slug": "fs-why-federal",
                        "detail": "Regional autonomy protects plurality within national unity.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "fs-why-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liner",
                "body": (
                    "Federalism in India is a design choice for **unity with diversity**, not a compact "
                    "of sovereign states joining by treaty."
                ),
            },
        ],
    },
    {
        "title": "Union of States (Article 1)",
        "slug": "fs-union-of-states",
        "sort_order": 3,
        "summary": "‘Federation’ unused; Art. 1 Union of States — no agreement, no secession; Art. 3 tilt.",
        "body": (
            "## Union of States — not ‘Federation’\n\n"
            "The word **federation** appears nowhere in the Constitution. **Article 1** describes "
            "India as a **Union of States**.\n\n"
            "**Ambedkar’s two reasons** for preferring ‘Union’:\n"
            "1. Indian federation is **not** the result of an agreement among the states (unlike the US).\n"
            "2. States have **no right to secede** — the federation is a union because it is "
            "**indestructible**.\n\n"
            "**Classic line:** India = **indestructible Union of destructible states**. "
            "USA = **indestructible Union of indestructible states**.\n\n"
            "**Article 3 tilt:** Parliament may unilaterally change the area, boundaries, or name "
            "of any state — only a **simple majority**, not a special majority."
        ),
        "articles": [
            (
                "Article 1",
                "India, that is Bharat, shall be a Union of States — not an agreement-based federation; no secession.",
            ),
            (
                "Article 3",
                "Parliament may form new states / alter areas, boundaries, or names — simple majority; states are destructible.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fs-union-compare",
                "type": "comparison",
                "title": "Territorial integrity — India vs US",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Called ‘Union of States’ (Art. 1)",
                            "Not formed by agreement of states",
                            "No right to secede",
                            "Parliament can alter state territory (Art. 3)",
                            "Indestructible Union of destructible states",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "United States",
                        "points": [
                            "Classic agreement-based federation",
                            "States joined by compact",
                            "States have territorial integrity as a federal safeguard",
                            "Indestructible Union of indestructible states",
                            "Equality of states in the Senate (2 each)",
                        ],
                    },
                ],
            },
            {
                "id": "fs-union-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Wording trap",
                "body": (
                    "Do **not** write ‘India is a federation of states’. Correct framing: "
                    "**Union of States** — federal system with unitary bias / quasi-federal tilt."
                ),
            },
        ],
    },
    {
        "title": "Canadian Model (not American)",
        "slug": "fs-canadian-model",
        "sort_order": 4,
        "summary": "India mirrors Canada: disintegration, ‘Union’ wording, and a strong Centre.",
        "body": (
            "## Canadian model — three resemblance points\n\n"
            "Indian federalism is based on the **Canadian model**, not the American model. "
            "Canada establishes a **very strong Centre**.\n\n"
            "India resembles Canada in:\n"
            "1. **Formation** — by way of disintegration (not US-style integration).\n"
            "2. **Preference for ‘Union’** — Canadian federation is also called a Union.\n"
            "3. **Centralising tendency** — more powers with the Centre vis-à-vis the units.\n\n"
            "US remains the oldest federation (1787) and the textbook ‘model’, but India’s "
            "architecture tracks Canada’s strong-Centre design."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "fs-india-canada-us",
                "type": "comparison",
                "title": "India · Canada · USA (Ch.14 pins)",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Disintegration path",
                            "‘Union of States’",
                            "Strong Centre",
                            "Residuary → Centre",
                            "Single citizenship",
                            "Single Constitution (J&K was the old exception)",
                            "Unequal RS seats by population",
                            "Appointed Governors",
                        ],
                    },
                    {
                        "id": "canada",
                        "heading": "Canada",
                        "points": [
                            "Disintegration path (1867)",
                            "Also called a ‘Union’",
                            "Strong Centre",
                            "Single citizenship (like India)",
                            "Appointed provincial heads (pattern India followed)",
                            "10 provinces (originally 4)",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Integration path (1787)",
                            "Agreement of states",
                            "Residuary → states",
                            "Dual citizenship",
                            "Separate state constitutions",
                            "Equal Senate representation",
                            "Elected state heads",
                            "Dual court systems",
                        ],
                    },
                ],
            },
            {
                "id": "fs-canada-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims one-liner",
                "body": (
                    "If asked ‘Indian federation is closer to which model?’ → **Canadian** "
                    "(disintegration + Union + strong Centre)."
                ),
            },
        ],
    },
    {
        "title": "Seven Federal Features",
        "slug": "fs-federal-features",
        "sort_order": 5,
        "summary": "Dual polity, written Constitution, 7th Schedule division, supremacy, rigidity, independent judiciary, bicameralism.",
        "body": (
            "## Seven federal features\n\n"
            "Mnemonic: **D-W-D-S-R-I-B** — Dual, Written, Division, Supremacy, Rigid, "
            "Independent judiciary, Bicameral.\n"
            "Phrase: **“Dual Written Division Supremacy Rigid Independent Bicameral”**.\n\n"
            "1. **Dual polity** — Union (national matters) + states (regional/local).\n"
            "2. **Written Constitution** — lengthiest; structures and limits both governments.\n"
            "3. **Division of powers** — 7th Schedule: Union (~98; orig. 97), State (~59; orig. 66), "
            "Concurrent (~52; orig. 47). Concurrent conflict → **Central law prevails**. "
            "**Residuary → Centre** (Art. 248).\n"
            "4. **Supremacy of the Constitution** — laws must conform; judicial review.\n"
            "5. **Rigid Constitution** (federal parts) — Centre–state relations / judicial organisation "
            "need special majority of Parliament **+** ratification by half the states (Art. 368 path).\n"
            "6. **Independent judiciary** — SC protects supremacy and settles Centre–state / inter-state disputes.\n"
            "7. **Bicameralism** — Rajya Sabha represents states; Lok Sabha represents the people."
        ),
        "articles": [
            (
                "Seventh Schedule",
                "Union / State / Concurrent Lists — constitutional division of legislative subjects.",
            ),
            (
                "Article 248",
                "Residuary powers of legislation vest in Parliament (Centre) — unlike the US.",
            ),
            (
                "Article 246",
                "Subject-matter of laws made by Parliament and by the Legislatures of States.",
            ),
            (
                "Article 368",
                "Federal provisions need special majority + ratification by not less than half the state legislatures.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fs-seven-pillars",
                "type": "pillars",
                "title": "Seven federal features",
                "items": [
                    {
                        "id": "dual",
                        "articles": "1 · Dual",
                        "label": "Dual Polity",
                        "slug": "fs-federal-features",
                        "detail": "Union + states — each sovereign in its assigned field.",
                        "tone": "teal",
                    },
                    {
                        "id": "written",
                        "articles": "2 · Written",
                        "label": "Written Constitution",
                        "slug": "fs-federal-features",
                        "detail": "Lengthiest written text — avoids Centre–state ambiguity.",
                        "tone": "olive",
                    },
                    {
                        "id": "division",
                        "articles": "3 · 7th Sch.",
                        "label": "Division of Powers",
                        "slug": "fs-federal-features",
                        "detail": "Three lists; concurrent conflict → Centre; residuary → Centre.",
                        "tone": "gold",
                    },
                    {
                        "id": "supremacy",
                        "articles": "4 · JR",
                        "label": "Supremacy of Constitution",
                        "slug": "fs-federal-features",
                        "detail": "Centre and state laws must conform — else invalid.",
                        "tone": "orange",
                    },
                    {
                        "id": "rigid",
                        "articles": "5 · Art. 368",
                        "label": "Rigid (federal parts)",
                        "slug": "fs-federal-features",
                        "detail": "Special majority + half the states for federal structure changes.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "indep",
                        "articles": "6 · SC",
                        "label": "Independent Judiciary",
                        "slug": "fs-federal-features",
                        "detail": "Protects supremacy; settles Centre–state and inter-state disputes.",
                        "tone": "maroon",
                    },
                    {
                        "id": "bicam",
                        "articles": "7 · RS",
                        "label": "Bicameralism",
                        "slug": "fs-federal-features",
                        "detail": "Rajya Sabha = states’ House; federal equilibrium check.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "fs-seven-tip",
                "type": "callout",
                "tone": "tip",
                "title": "List counts + conflict rule",
                "body": (
                    "Union ~98 / State ~59 / Concurrent ~52 (originally 97 / 66 / 47). "
                    "Concurrent clash → Central law wins. Residuary subjects → **Centre** (Art. 248)."
                ),
            },
        ],
    },
    {
        "title": "Fourteen Unitary Features",
        "slug": "fs-unitary-features",
        "sort_order": 6,
        "summary": "Fourteen non-federal features grouped as Power / Structural / State / Amendment (P-S-S-A).",
        "body": (
            "## Fourteen unitary / non-federal features\n\n"
            "Bucket mnemonic: **P-S-S-A** — Power tilt · Structural unity · State weakness · "
            "Amendment asymmetry.\n\n"
            "**Power tilt (1, 6, 11)**\n"
            "1. Strong Centre (more + important subjects; Concurrent override; residuary to Centre).\n"
            "6. Emergency provisions — federal → unitary **without formal amendment**.\n"
            "11. Parliament’s authority over State List (e.g. Art. 249 RS resolution in national interest) "
            "even without emergency.\n\n"
            "**Structural unity (3, 7, 8, 9, 10, 13)**\n"
            "3. Single Constitution · 7. Single citizenship · 8. Integrated judiciary · "
            "9. All-India Services · 10. Integrated audit (CAG) · 13. Integrated election machinery.\n\n"
            "**State weakness (2, 5, 12, 14)**\n"
            "2. States not indestructible (Art. 3) · 5. No equality of RS representation · "
            "12. Appointment of Governor · 14. Veto over state bills (absolute Presidential veto).\n\n"
            "**Amendment asymmetry (4)**\n"
            "4. Flexibility — bulk amendable by Parliament alone; only Centre can initiate amendment.\n\n"
            "Erstwhile J&K had its own state Constitution (exception to single Constitution) till 2019."
        ),
        "articles": [
            (
                "Article 3",
                "States have no right to territorial integrity — Parliament may alter area, boundaries, or name.",
            ),
            (
                "Article 249",
                "Rajya Sabha resolution can empower Parliament to legislate on a State List subject in the national interest.",
            ),
            (
                "Article 356",
                "State emergency (President’s Rule) — Centre can override state machinery (with Bommai limits).",
            ),
            (
                "Articles 352 / 360",
                "National and financial emergencies — further centralise power; federal structure can become unitary.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fs-unitary-tree",
                "type": "tree",
                "title": "14 unitary features — P-S-S-A buckets",
                "root": {
                    "id": "unitary",
                    "label": "14 Unitary features",
                    "detail": "Non-federal tilt toward the Centre",
                    "children": [
                        {
                            "id": "power",
                            "label": "Power tilt",
                            "detail": "P",
                            "children": [
                                {
                                    "id": "u1",
                                    "label": "1. Strong Centre",
                                    "detail": "Lists + Concurrent + residuary",
                                },
                                {
                                    "id": "u6",
                                    "label": "6. Emergency provisions",
                                    "detail": "Federal → unitary, no amendment",
                                },
                                {
                                    "id": "u11",
                                    "label": "11. Parliament on State List",
                                    "detail": "Art. 249 etc. without emergency",
                                },
                            ],
                        },
                        {
                            "id": "structural",
                            "label": "Structural unity",
                            "detail": "S",
                            "children": [
                                {
                                    "id": "u3",
                                    "label": "3. Single Constitution",
                                    "detail": "Except erstwhile J&K till 2019",
                                },
                                {
                                    "id": "u7",
                                    "label": "7. Single citizenship",
                                    "detail": "Like Canada; unlike US/Australia",
                                },
                                {
                                    "id": "u8",
                                    "label": "8. Integrated judiciary",
                                    "detail": "SC → HC → subordinates",
                                },
                                {
                                    "id": "u9",
                                    "label": "9. All-India Services",
                                    "detail": "IAS / IPS / IFoS — Centre control",
                                },
                                {
                                    "id": "u10",
                                    "label": "10. Integrated audit (CAG)",
                                    "detail": "Audits Centre and states",
                                },
                                {
                                    "id": "u13",
                                    "label": "13. Integrated elections",
                                    "detail": "ECI for Centre and states",
                                },
                            ],
                        },
                        {
                            "id": "state",
                            "label": "State weakness",
                            "detail": "S",
                            "children": [
                                {
                                    "id": "u2",
                                    "label": "2. States not indestructible",
                                    "detail": "Art. 3 · simple majority",
                                },
                                {
                                    "id": "u5",
                                    "label": "5. Unequal RS seats",
                                    "detail": "By population (1–31), not equality",
                                },
                                {
                                    "id": "u12",
                                    "label": "12. Appointed Governor",
                                    "detail": "Centre’s agent; pleasure of President",
                                },
                                {
                                    "id": "u14",
                                    "label": "14. Veto over state bills",
                                    "detail": "Absolute Presidential veto",
                                },
                            ],
                        },
                        {
                            "id": "amend",
                            "label": "Amendment asymmetry",
                            "detail": "A",
                            "children": [
                                {
                                    "id": "u4",
                                    "label": "4. Flexible bulk amendment",
                                    "detail": "Parliament alone; states cannot initiate",
                                },
                            ],
                        },
                    ],
                },
            },
            {
                "id": "fs-unitary-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Independent ≠ Integrated",
                "body": (
                    "**Independent judiciary** = federal feature (protects supremacy / federal disputes). "
                    "**Integrated judiciary** = unitary feature (one hierarchy enforces Centre + state laws). "
                    "Do not swap them in Prelims."
                ),
            },
        ],
    },
    {
        "title": "Expert Labels + Ambedkar",
        "slug": "fs-expert-labels",
        "sort_order": 7,
        "summary": "Scholar labels from quasi-federal to cooperative; Ambedkar on dual polity and flexibility.",
        "body": (
            "## Critical evaluation — match scholar to phrase\n\n"
            "| Thinker | Label |\n"
            "|---|---|\n"
            "| K.C. Wheare | Quasi-federal; ‘unitary state with subsidiary federal features’ |\n"
            "| K. Santhanam | Unitary bias via Central finance dominance + Planning Commission "
            "(NITI Aayog since 2015) |\n"
            "| Paul Appleby | Extremely federal |\n"
            "| Morris Jones | Bargaining federalism |\n"
            "| Ivor Jennings | Federation with a strong centralising tendency |\n"
            "| C.H. Alexandrowicz | *Sui generis* (unique) |\n"
            "| Granville Austin | Cooperative federalism |\n\n"
            "**Ambedkar (CAD):** Constitution is federal because it establishes a **dual polity**; "
            "Union is not a loose league; states are not Union agencies — both derive authority from "
            "the Constitution. It can be **unitary as well as federal** as circumstances require. "
            "Basic principle: legislative/executive authority is partitioned by the Constitution "
            "itself, not by a law of the Centre."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "fs-labels-compare",
                "type": "comparison",
                "title": "Scholar ↔ phrase (must-match)",
                "columns": [
                    {
                        "id": "centralising",
                        "heading": "Centralising / sceptical",
                        "points": [
                            "K.C. Wheare — quasi-federal",
                            "K. Santhanam — finance + planning → unitary bias",
                            "Ivor Jennings — strong centralising tendency",
                        ],
                    },
                    {
                        "id": "federal-spirit",
                        "heading": "Federal / cooperative",
                        "points": [
                            "Paul Appleby — extremely federal",
                            "Morris Jones — bargaining federalism",
                            "Granville Austin — cooperative federalism",
                            "Alexandrowicz — sui generis",
                        ],
                    },
                ],
            },
            {
                "id": "fs-labels-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims drill",
                "body": (
                    "Match pairs: Wheare ↔ quasi-federal · Morris Jones ↔ bargaining · "
                    "Austin ↔ cooperative · Jennings ↔ centralising tendency · Alexandrowicz ↔ sui generis."
                ),
            },
        ],
    },
    {
        "title": "Bommai + Federal Spirit",
        "slug": "fs-bommai-spirit",
        "sort_order": 8,
        "summary": "Bommai (1994): federalism is a basic feature; seven working trends show living federal spirit.",
        "body": (
            "## Bommai (1994) and the living federal spirit\n\n"
            "**S.R. Bommai v. Union of India (1994):** Constitution is federal; federalism is a "
            "**basic feature**. States are not appendages/satellites of the Centre. Within their "
            "sphere they are supreme. Emergency and other overrides are **exceptions, not the rule**. "
            "Federalism is a matter of **principle**, not administrative convenience.\n\n"
            "**Compromise design:** (i) normal division with state autonomy; (ii) exceptional need "
            "for national integrity and a strong Union.\n\n"
            "**Seven trends reflecting federal spirit**\n"
            "1. Inter-state territorial disputes (e.g. Belgaum)\n"
            "2. River-water disputes (e.g. Cauvery)\n"
            "3. Rise of regional parties in power\n"
            "4. Creation of new states (regional aspirations)\n"
            "5. States’ demand for more Central grants\n"
            "6. Assertion of autonomy / resistance to Central interference\n"
            "7. SC procedural limits on Art. 356 (President’s Rule)"
        ),
        "articles": [
            (
                "Article 356",
                "President’s Rule — Bommai imposed judicially enforceable procedural limitations on misuse.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fs-spirit-pillars",
                "type": "pillars",
                "title": "Seven federal-spirit trends",
                "items": [
                    {
                        "id": "t1",
                        "articles": "Trend 1",
                        "label": "Territory disputes",
                        "slug": "fs-bommai-spirit",
                        "detail": "e.g. Maharashtra–Karnataka (Belgaum).",
                        "tone": "teal",
                    },
                    {
                        "id": "t2",
                        "articles": "Trend 2",
                        "label": "River-water disputes",
                        "slug": "fs-bommai-spirit",
                        "detail": "e.g. Cauvery (Karnataka–Tamil Nadu).",
                        "tone": "olive",
                    },
                    {
                        "id": "t3",
                        "articles": "Trend 3",
                        "label": "Regional parties",
                        "slug": "fs-bommai-spirit",
                        "detail": "State-level power centres assert federal bargaining.",
                        "tone": "gold",
                    },
                    {
                        "id": "t4",
                        "articles": "Trend 4",
                        "label": "New states",
                        "slug": "fs-bommai-spirit",
                        "detail": "Mizoram, Jharkhand, Telangana — regional aspirations.",
                        "tone": "orange",
                    },
                    {
                        "id": "t5",
                        "articles": "Trend 5",
                        "label": "Fiscal demands",
                        "slug": "fs-bommai-spirit",
                        "detail": "States push for larger Central grants.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "t6",
                        "articles": "Trend 6",
                        "label": "Autonomy assertion",
                        "slug": "fs-bommai-spirit",
                        "detail": "Resistance to Central interference in state spheres.",
                        "tone": "maroon",
                    },
                    {
                        "id": "t7",
                        "articles": "Art. 356",
                        "label": "Art. 356 limits",
                        "slug": "fs-bommai-spirit",
                        "detail": "Bommai — procedural checks on President’s Rule.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "fs-bommai-note",
                "type": "callout",
                "tone": "note",
                "title": "Mains value addition",
                "body": (
                    "Bommai line: federalism is **not a matter of administrative convenience, but one of "
                    "principle**. Greater Central power ≠ states as mere appendages. Link to Basic Structure."
                ),
            },
        ],
    },
    {
        "title": "Quick Revision Toolkit",
        "slug": "fs-revision-toolkit",
        "sort_order": 9,
        "summary": "60-second drill: 7 vs 14, India–US–Canada pins, article strip, PYQ themes.",
        "body": (
            "## 60-second drill\n\n"
            "**Article pin strip:** Art. 1 (Union) · Art. 3 (destructible states) · Art. 246 / 7th Schedule "
            "(lists) · Art. 248 (residuary → Centre) · Art. 249 (Parliament on State List) · "
            "Arts 352 / 356 / 360 (emergencies) · Art. 368 (federal amendment path).\n\n"
            "**PYQ themes**\n"
            "- Nature of Indian federation / ‘quasi-federal’\n"
            "- ‘Union of States’ vs ‘federation’ wording\n"
            "- Residuary powers with the Centre\n"
            "- Unequal RS representation vs US Senate equality\n"
            "- Emergency converts federal → unitary without amendment\n"
            "- Bommai: federalism as basic feature\n"
            "- Independent judiciary (federal) vs integrated judiciary (unitary)\n\n"
            "Scan the comparison below, then jump to any weak cluster."
        ),
        "articles": [
            (
                "Article 1",
                "Union of States — revision anchor for wording questions.",
            ),
            (
                "Article 248",
                "Residuary powers — Centre (classic Prelims contrast with US).",
            ),
            (
                "Seventh Schedule",
                "Three lists — division of powers is the core federal feature.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fs-toolkit-compare",
                "type": "comparison",
                "title": "7 federal vs 14 unitary — scan card",
                "columns": [
                    {
                        "id": "seven",
                        "heading": "7 Federal (D-W-D-S-R-I-B)",
                        "points": [
                            "Dual polity",
                            "Written Constitution",
                            "Division of powers",
                            "Supremacy of Constitution",
                            "Rigid federal amendment path",
                            "Independent judiciary",
                            "Bicameralism",
                        ],
                    },
                    {
                        "id": "fourteen",
                        "heading": "14 Unitary (P-S-S-A)",
                        "points": [
                            "Strong Centre · Emergency · Art. 249 path",
                            "Single Const. · citizenship · integrated courts",
                            "AIS · CAG · ECI (integrated)",
                            "Art. 3 · unequal RS · Governor · bill veto",
                            "Flexible bulk amendment (Centre initiates)",
                        ],
                    },
                ],
            },
            {
                "id": "fs-toolkit-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Last-minute order",
                "body": (
                    "1) Art. 1 wording → 2) Canadian model → 3) 7 vs 14 → 4) scholar labels → "
                    "5) Bommai basic feature. That covers almost every Ch.14 Prelims/Mains ask."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "fs-federal-vs-unitary"),
    (HUB_SLUG, "parent", "fs-why-federal"),
    (HUB_SLUG, "parent", "fs-union-of-states"),
    (HUB_SLUG, "parent", "fs-canadian-model"),
    (HUB_SLUG, "parent", "fs-federal-features"),
    (HUB_SLUG, "parent", "fs-unitary-features"),
    (HUB_SLUG, "parent", "fs-expert-labels"),
    (HUB_SLUG, "parent", "fs-bommai-spirit"),
    (HUB_SLUG, "parent", "fs-revision-toolkit"),
    ("fs-federal-features", "related", "fs-unitary-features"),
    ("fs-unitary-features", "related", "sf-federal-unitary"),
    ("fs-bommai-spirit", "related", "basic-structure"),
    ("fs-union-of-states", "related", "fs-canadian-model"),
    ("fs-expert-labels", "related", "fs-bommai-spirit"),
    (HUB_SLUG, "related", "parliamentary-system"),
    (HUB_SLUG, "related", "sf-federal-unitary"),
]

SAMPLE_PYQS = [
    (
        2017,
        "Which one of the following is not a feature of Indian federalism?",
        "Often tested via unitary tilts — e.g. unequal Rajya Sabha representation, residuary with Centre, or single citizenship (contrast with classical US federalism).",
        ["fs-unitary-features", "fs-federal-features", HUB_SLUG],
    ),
    (
        2015,
        "The provisions in the Constitution of India relating to the ‘Union of States’ primarily indicate that:",
        "India is not a federation formed by agreement of states and states have no right to secede (Art. 1 — Ambedkar).",
        ["fs-union-of-states", HUB_SLUG],
    ),
    (
        2016,
        "Which of the following are regarded as federal features of the Indian Constitution?",
        "Dual polity, written Constitution, division of powers, supremacy of Constitution, independent judiciary, bicameralism (and rigid amendment for federal parts).",
        ["fs-federal-features", "fs-federal-vs-unitary"],
    ),
    (
        2014,
        "Residuary powers under the Indian Constitution are vested in:",
        "The Union / Parliament (Art. 248) — unlike the United States where residuary powers vest in the states.",
        ["fs-federal-features", "fs-canadian-model", HUB_SLUG],
    ),
    (
        2013,
        "The Indian Constitution has been described as ‘quasi-federal’ by:",
        "K.C. Wheare — ‘unitary state with subsidiary federal features rather than a federal state with subsidiary unitary features’.",
        ["fs-expert-labels", HUB_SLUG],
    ),
]

LANDMARK_CASES = [
    {
        "title": "S.R. Bommai v. Union of India",
        "slug": "sr-bommai",
        "parties": "S.R. Bommai v. Union of India",
        "year": 1994,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Landmark ruling on Article 356 and the federal character of the Constitution — "
            "federalism held to be a basic feature."
        ),
        "holding": (
            "The Constitution is federal; federalism is a basic feature. States have an independent "
            "constitutional existence and are not appendages of the Centre. Emergency and similar "
            "overrides are exceptions, not the rule. Federalism is a matter of principle, not "
            "administrative convenience."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "fs-bommai-spirit",
            "fs-expert-labels",
            "fs-unitary-features",
        ],
    },
]

# Ch.14’s J&K / Art. 370 footnote is covered in cluster body (single Constitution exception
# till 2019). No numbered ConstitutionalAmendment record — avoid inventing a fake “370th”.
AMENDMENTS = []


class Command(BaseCommand):
    help = "Seed Federal System chapter (Laxmikanth Ch.14, pp. 213–220)."

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
                "title": "Federal System",
                "sort_order": 2,
                "book_ref": "Laxmikanth 8th Ed, Ch. 14, pp. 213–220",
                "summary": (
                    "Visual revision of Ch.14 — Union of States, Canadian model, "
                    "7 federal vs 14 unitary features, scholar labels, and Bommai."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Federal System",
                "summary": (
                    "Federal form with unitary tilt — Union of States, 7+14 features, "
                    "expert labels, and Bommai’s basic-feature holding."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **switchboard mental model**, then scan the **nine clusters**. "
                    "Drill **7 federal vs 14 unitary**, scholar labels, and **Bommai**. "
                    "Finish with the Quick Revision Toolkit. "
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
            ref="Laxmikanth Ch. 14",
            excerpt="Federal System — Union of States, federal/unitary features, labels, Bommai.",
            sort_order=0,
        )

        fs_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=fs_slugs, source__subject=subject
        ).filter(
            target__slug__in=fs_slugs
            | {
                "sf-federal-unitary",
                "basic-structure",
                "parliamentary-system",
            }
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
                f"Federal System chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments."
            )
        )
