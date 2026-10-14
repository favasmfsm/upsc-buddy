"""Seed Laxmikanth Ch.9 Directive Principles of State Policy (visual revision)."""

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

HUB_SLUG = "directive-principles"
CHAPTER_SLUG = "directive-principles"

PILLAR_ITEMS = [
    {
        "id": "features",
        "articles": "Arts 36–37",
        "label": "Features & Nature",
        "slug": "dpsp-features",
        "detail": "Ireland source; Instrument of Instructions; non-justiciable yet fundamental.",
        "tone": "teal",
    },
    {
        "id": "socialistic",
        "articles": "Socialistic",
        "label": "Socialistic Principles",
        "slug": "dpsp-socialistic",
        "detail": "Welfare, livelihood, equal pay, work, legal aid — democratic socialism.",
        "tone": "olive",
    },
    {
        "id": "gandhian",
        "articles": "Gandhian",
        "label": "Gandhian Principles",
        "slug": "dpsp-gandhian",
        "detail": "Panchayats, cottage industries, co-ops, weaker sections, prohibition, cows.",
        "tone": "gold",
    },
    {
        "id": "liberal",
        "articles": "Liberal–intellectual",
        "label": "Liberal–Intellectual",
        "slug": "dpsp-liberal",
        "detail": "UCC, early childhood care, environment, judiciary separation, peace.",
        "tone": "orange",
    },
    {
        "id": "new",
        "articles": "42 · 44 · 86 · 97",
        "label": "New Directive Principles",
        "slug": "dpsp-new-amendments",
        "detail": "Amendments that added or reshaped Part IV directives.",
        "tone": "terracotta",
    },
    {
        "id": "sanction",
        "articles": "Art. 37",
        "label": "Sanction Behind DPSP",
        "slug": "dpsp-sanction",
        "detail": "Political / public-opinion sanction — not court compulsion.",
        "tone": "maroon",
    },
    {
        "id": "vs-fr",
        "articles": "Table 9.1",
        "label": "DPSP vs Fundamental Rights",
        "slug": "dpsp-vs-fr",
        "detail": "Justiciable shield vs non-justiciable programme for the State.",
        "tone": "teal",
    },
    {
        "id": "conflict",
        "articles": "Art. 31C",
        "label": "FR–DPSP Conflict",
        "slug": "dpsp-conflict",
        "detail": "Champakam → Minerva — present balance and basic structure.",
        "tone": "olive",
    },
    {
        "id": "crit-util",
        "articles": "Criticism · Utility",
        "label": "Criticism & Utility",
        "slug": "dpsp-criticism-utility",
        "detail": "Famous critiques plus why DPSP still matter for governance.",
        "tone": "gold",
    },
    {
        "id": "implement",
        "articles": "Since 1950",
        "label": "Implementation Themes",
        "slug": "dpsp-implementation",
        "detail": "Theme buckets — planning, land/labour, welfare, environment, weaker sections.",
        "tone": "orange",
    },
    {
        "id": "outside",
        "articles": "335 · 350-A · 351",
        "label": "Directives Outside Part IV",
        "slug": "dpsp-outside-part-iv",
        "detail": "Also non-justiciable — read the Constitution as a whole.",
        "tone": "terracotta",
    },
    {
        "id": "glance",
        "articles": "Arts 36–51",
        "label": "Articles at a Glance",
        "slug": "dpsp-articles-glance",
        "detail": "Table 9.2 memory index for Part IV.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "dpsp-compass-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Compass",
        "topic_label": "Directive Principles",
        "subject_label": "State",
        "relation_label": "Points the State toward",
        "protects_from": [
            "Police-state thinking",
            "Ignoring social justice",
            "Governance without goals",
            "Political democracy alone",
        ],
        "insight": (
            "DPSP are the State's compass toward welfare and economic democracy. "
            "Art. 37 makes them fundamental in governance — the needle is political sanction, not courts."
        ),
    },
    {
        "id": "dpsp-twelve-pillars",
        "type": "pillars",
        "title": "Twelve revision clusters",
        "items": PILLAR_ITEMS,
    },
    {
        "id": "dpsp-revision-anchor",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Start from the compass, then scan the twelve pillars. "
            "Master classification (socialistic / Gandhian / liberal) and the FR–DPSP conflict timeline before drills."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Features of the Directive Principles",
        "slug": "dpsp-features",
        "sort_order": 1,
        "summary": "Part IV ideals for the State — Ireland source; non-justiciable yet fundamental in governance (Art. 37).",
        "body": (
            "## Features of the Directive Principles\n\n"
            "Part IV — **Articles 36 to 51**. Borrowed from the **Irish Constitution (1937)** "
            "(itself from Spain). Ambedkar: **novel features**. With FR, they are the philosophy / "
            "‘Conscience of the Constitution’ (Granville Austin).\n\n"
            "- **Ideals for policy & law** — constitutional instructions to legislature, executive, administration.\n"
            "- **Art. 36** — ‘State’ has the **same meaning as in Part III** (Art. 12).\n"
            "- **Instrument of Instructions** — Ambedkar: like GoI Act 1935 instructions, but to legislature & executive.\n"
            "- **Welfare state** — economic & social democracy; not colonial ‘police state’.\n"
            "- **Non-justiciable (Art. 37)** — cannot compel implementation; yet **fundamental in the governance** "
            "of the country; duty of the State to apply them in making laws.\n"
            "- Courts may treat a law giving effect to a DPSP as **‘reasonable’** under Art. 14 / 19 and save it."
        ),
        "articles": [
            (
                "Article 36",
                "Definition of State in Part IV — same meaning as in Part III.",
            ),
            (
                "Article 37",
                "DPSP fundamental in governance; duty of the State to apply them in making laws; non-justiciable.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-feat-pillars",
                "type": "pillars",
                "title": "Five feature hooks",
                "items": [
                    {
                        "id": "ideals",
                        "articles": "Policy ideals",
                        "label": "Instructions to the State",
                        "slug": "dpsp-features",
                        "detail": "Keep in mind while formulating policies and enacting laws.",
                        "tone": "teal",
                    },
                    {
                        "id": "art36",
                        "articles": "Art. 36",
                        "label": "State = Part III meaning",
                        "slug": "dpsp-features",
                        "detail": "Centre, states, local and other public authorities.",
                        "tone": "olive",
                    },
                    {
                        "id": "goi1935",
                        "articles": "GoI Act 1935",
                        "label": "Instrument of Instructions",
                        "slug": "dpsp-features",
                        "detail": "Ambedkar’s analogy — instructions to legislature & executive.",
                        "tone": "gold",
                    },
                    {
                        "id": "welfare",
                        "articles": "Welfare state",
                        "label": "Social & economic democracy",
                        "slug": "dpsp-features",
                        "detail": "Justice, liberty, equality, fraternity — not a police state.",
                        "tone": "orange",
                    },
                    {
                        "id": "art37",
                        "articles": "Art. 37",
                        "label": "Non-justiciable but fundamental",
                        "slug": "dpsp-features",
                        "detail": "Duty to apply in making laws; political sanction.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "dpsp-feat-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook",
                "body": (
                    "Source = Ireland · ‘novel features’ = Ambedkar · Art. 36 mirrors Art. 12 · "
                    "Art. 37 = fundamental in governance + non-justiciable."
                ),
            },
        ],
    },
    {
        "title": "Socialistic Principles",
        "slug": "dpsp-socialistic",
        "sort_order": 2,
        "summary": "Democratic socialism path — welfare, livelihood, equal pay, work, legal aid, nutrition.",
        "body": (
            "## Socialistic Principles\n\n"
            "Constitution does **not** classify DPSP; scholars group by content. "
            "Socialistic principles aim at social & economic justice and a welfare state.\n\n"
            "- **Art. 38** — social order of justice; minimise inequalities (income, status, facilities, opportunities).\n"
            "- **Art. 39** — livelihood; equitable distribution; no wealth concentration; equal pay; worker/child health; "
            "healthy development of children.\n"
            "- **Art. 39A** — equal justice; free legal aid.\n"
            "- **Art. 41** — right to work, education, public assistance (unemployment, old age, sickness, disablement).\n"
            "- **Art. 42** — just & humane conditions of work; maternity relief.\n"
            "- **Art. 43** — living wage; decent standard of life; social & cultural opportunities for workers.\n"
            "- **Art. 43A** — participation of workers in management of industries.\n"
            "- **Art. 47** — nutrition, standard of living, public health (also Gandhian for prohibition)."
        ),
        "articles": [
            ("Article 38", "Social order for welfare; minimise inequalities."),
            ("Article 39", "Certain principles of policy — livelihood, distribution, equal pay, children."),
            ("Article 39A", "Equal justice and free legal aid."),
            ("Article 41", "Right to work, education, and public assistance."),
            ("Article 42", "Just and humane conditions of work; maternity relief."),
            ("Article 43", "Living wage, etc., for workers."),
            ("Article 43A", "Participation of workers in management of industries."),
            ("Article 47", "Nutrition, standard of living, and public health."),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-soc-pillars",
                "type": "pillars",
                "title": "Socialistic articles — scan map",
                "items": [
                    {
                        "id": "a38",
                        "articles": "Art. 38",
                        "label": "Welfare & equality",
                        "slug": "dpsp-socialistic",
                        "detail": "Social order of justice; minimise inequalities.",
                        "tone": "teal",
                    },
                    {
                        "id": "a39",
                        "articles": "Art. 39",
                        "label": "Livelihood & resources",
                        "slug": "dpsp-socialistic",
                        "detail": "Livelihood, distribution, no concentration, equal pay, children.",
                        "tone": "olive",
                    },
                    {
                        "id": "a39a",
                        "articles": "Art. 39A",
                        "label": "Equal justice & legal aid",
                        "slug": "dpsp-socialistic",
                        "detail": "Free legal aid to the poor.",
                        "tone": "gold",
                    },
                    {
                        "id": "a41",
                        "articles": "Art. 41",
                        "label": "Work & assistance",
                        "slug": "dpsp-socialistic",
                        "detail": "Work, education, public assistance in need.",
                        "tone": "orange",
                    },
                    {
                        "id": "a42-43",
                        "articles": "42 · 43 · 43A",
                        "label": "Workers’ dignity",
                        "slug": "dpsp-socialistic",
                        "detail": "Humane work, maternity, living wage, worker participation.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "a47",
                        "articles": "Art. 47",
                        "label": "Nutrition & health",
                        "slug": "dpsp-socialistic",
                        "detail": "Raise nutrition and living standard; improve public health.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "dpsp-soc-tip",
                "type": "callout",
                "tone": "tip",
                "title": "39(b) & (c) exam magnet",
                "body": (
                    "Art. 39(b) material resources for common good · Art. 39(c) no concentration of wealth — "
                    "these two still enjoy Art. 31C shield after Minerva Mills."
                ),
            },
        ],
    },
    {
        "title": "Gandhian Principles",
        "slug": "dpsp-gandhian",
        "sort_order": 3,
        "summary": "Village republic ideals — panchayats, cottage industries, co-ops, weaker sections, prohibition, cows.",
        "body": (
            "## Gandhian Principles\n\n"
            "Based on Gandhian reconstruction during the national movement.\n\n"
            "- **Art. 40** — organise village panchayats as units of self-government.\n"
            "- **Art. 43** — promote cottage industries (individual or co-operation) in rural areas.\n"
            "- **Art. 43B** — voluntary, autonomous, democratic, professional co-operative societies.\n"
            "- **Art. 46** — educational & economic interests of SCs, STs, and other weaker sections; protect from injustice.\n"
            "- **Art. 47** — prohibit intoxicating drinks and drugs injurious to health.\n"
            "- **Art. 48** — prohibit slaughter of cows, calves, and other milch and draught cattle; improve breeds."
        ),
        "articles": [
            ("Article 40", "Organisation of village panchayats."),
            ("Article 43", "Cottage industries in rural areas (also living wage — socialistic)."),
            ("Article 43B", "Promotion of co-operative societies."),
            ("Article 46", "Interests of SCs, STs, and other weaker sections."),
            ("Article 47", "Prohibition of intoxicating drinks and drugs."),
            ("Article 48", "Prohibit cow slaughter; improve cattle breeds."),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-gandhi-pillars",
                "type": "pillars",
                "title": "Gandhian six",
                "items": [
                    {
                        "id": "a40",
                        "articles": "Art. 40",
                        "label": "Village panchayats",
                        "slug": "dpsp-gandhian",
                        "detail": "Units of self-government — link to 73rd Amendment.",
                        "tone": "teal",
                    },
                    {
                        "id": "a43c",
                        "articles": "Art. 43",
                        "label": "Cottage industries",
                        "slug": "dpsp-gandhian",
                        "detail": "Rural individual or co-operation basis.",
                        "tone": "olive",
                    },
                    {
                        "id": "a43b",
                        "articles": "Art. 43B",
                        "label": "Co-operative societies",
                        "slug": "dpsp-gandhian",
                        "detail": "97th Amendment — voluntary, autonomous, democratic.",
                        "tone": "gold",
                    },
                    {
                        "id": "a46",
                        "articles": "Art. 46",
                        "label": "Weaker sections",
                        "slug": "dpsp-gandhian",
                        "detail": "SC/ST and other weaker sections — education & economy.",
                        "tone": "orange",
                    },
                    {
                        "id": "a47p",
                        "articles": "Art. 47",
                        "label": "Prohibition",
                        "slug": "dpsp-gandhian",
                        "detail": "Prohibit drinks and drugs injurious to health.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "a48c",
                        "articles": "Art. 48",
                        "label": "Cow protection",
                        "slug": "dpsp-gandhian",
                        "detail": "Prohibit slaughter of cows, calves, milch/draught cattle.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "dpsp-gandhi-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Overlap trap",
                "body": (
                    "Art. 43 and Art. 47 appear in more than one category — cottage/living wage and "
                    "nutrition/prohibition. Classify by the limb asked."
                ),
            },
        ],
    },
    {
        "title": "Liberal–Intellectual Principles",
        "slug": "dpsp-liberal",
        "sort_order": 4,
        "summary": "Liberal ideology — UCC, early childhood care, scientific agriculture, environment, monuments, judiciary, peace.",
        "body": (
            "## Liberal–Intellectual Principles\n\n"
            "- **Art. 44** — uniform civil code for all citizens.\n"
            "- **Art. 45** — early childhood care and education until age **six** (after 86th; elementary education moved to Art. 21A).\n"
            "- **Art. 48** — organise agriculture and animal husbandry on modern and scientific lines.\n"
            "- **Art. 48A** — protect and improve environment; safeguard forests and wildlife.\n"
            "- **Art. 49** — protect monuments and places/objects of national importance.\n"
            "- **Art. 50** — separate judiciary from executive in public services of the State.\n"
            "- **Art. 51** — international peace and security; honourable relations; respect for international law; "
            "settlement of disputes by arbitration."
        ),
        "articles": [
            ("Article 44", "Uniform civil code for the citizens."),
            ("Article 45", "Early childhood care and education below six years."),
            ("Article 48", "Agriculture and animal husbandry on scientific lines."),
            ("Article 48A", "Environment, forests, and wildlife."),
            ("Article 49", "Monuments and places of national importance."),
            ("Article 50", "Separation of judiciary from executive."),
            ("Article 51", "International peace and security."),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-lib-pillars",
                "type": "pillars",
                "title": "Liberal–intellectual seven",
                "items": [
                    {
                        "id": "a44",
                        "articles": "Art. 44",
                        "label": "Uniform Civil Code",
                        "slug": "dpsp-liberal",
                        "detail": "Endeavour to secure UCC throughout India.",
                        "tone": "teal",
                    },
                    {
                        "id": "a45",
                        "articles": "Art. 45",
                        "label": "Early childhood (0–6)",
                        "slug": "dpsp-liberal",
                        "detail": "86th shifted 6–14 education to Art. 21A FR.",
                        "tone": "olive",
                    },
                    {
                        "id": "a48s",
                        "articles": "Art. 48",
                        "label": "Scientific agriculture",
                        "slug": "dpsp-liberal",
                        "detail": "Modern and scientific lines (also cow limb is Gandhian).",
                        "tone": "gold",
                    },
                    {
                        "id": "a48a",
                        "articles": "Art. 48A",
                        "label": "Environment",
                        "slug": "dpsp-liberal",
                        "detail": "Forests and wildlife — 42nd Amendment.",
                        "tone": "orange",
                    },
                    {
                        "id": "a49",
                        "articles": "Art. 49",
                        "label": "Monuments",
                        "slug": "dpsp-liberal",
                        "detail": "Artistic or historic interest of national importance.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "a50",
                        "articles": "Art. 50",
                        "label": "Separate judiciary",
                        "slug": "dpsp-liberal",
                        "detail": "From executive in public services — CrPC 1973.",
                        "tone": "maroon",
                    },
                    {
                        "id": "a51",
                        "articles": "Art. 51",
                        "label": "International peace",
                        "slug": "dpsp-liberal",
                        "detail": "Peace, honourable relations, intl law, arbitration.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "dpsp-lib-tip",
                "type": "callout",
                "tone": "tip",
                "title": "86th memory pair",
                "body": "Art. 21A = free & compulsory education 6–14 (FR) · Art. 45 = early childhood care & education until 6 (DPSP).",
            },
        ],
    },
    {
        "title": "New Directive Principles",
        "slug": "dpsp-new-amendments",
        "sort_order": 5,
        "summary": "42nd, 44th, 86th, and 97th Amendments — what was added or rewritten in Part IV.",
        "body": (
            "## New Directive Principles\n\n"
            "**42nd Amendment (1976)** added four directives:\n"
            "1. Healthy development of children (**Art. 39**).\n"
            "2. Equal justice and free legal aid (**Art. 39A**).\n"
            "3. Workers’ participation in management (**Art. 43A**).\n"
            "4. Environment, forests, wildlife (**Art. 48A**).\n\n"
            "**44th Amendment (1978)** — minimise inequalities in income, status, facilities, opportunities (**Art. 38**).\n\n"
            "**86th Amendment (2002)** — changed **Art. 45** to early childhood care/education until age six; "
            "elementary education became FR under **Art. 21A**.\n\n"
            "**97th Amendment (2011)** — promote co-operative societies (**Art. 43B**)."
        ),
        "articles": [
            ("Article 39A", "Added by 42nd — equal justice and free legal aid."),
            ("Article 43A", "Added by 42nd — workers in management."),
            ("Article 48A", "Added by 42nd — environment."),
            ("Article 43B", "Added by 97th — co-operative societies."),
            ("Article 45", "Rewritten by 86th — early childhood care until six."),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-new-timeline",
                "type": "timeline",
                "title": "Amendments that reshaped Part IV",
                "events": [
                    {
                        "id": "e1976",
                        "year": 1976,
                        "label": "42nd — four new DPSPs",
                        "detail": "Art. 39 (children), 39A, 43A, 48A.",
                    },
                    {
                        "id": "e1978",
                        "year": 1978,
                        "label": "44th — Art. 38 inequalities",
                        "detail": "Minimise inequalities in income, status, facilities, opportunities.",
                    },
                    {
                        "id": "e2002",
                        "year": 2002,
                        "label": "86th — Art. 45 + 21A",
                        "detail": "Elementary education → FR; Art. 45 = early childhood until 6.",
                    },
                    {
                        "id": "e2011",
                        "year": 2011,
                        "label": "97th — Art. 43B",
                        "detail": "Promotion of co-operative societies.",
                    },
                ],
            },
            {
                "id": "dpsp-new-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Count mnemonic",
                "body": "42nd = four new · 44th = inequalities · 86th = rewrite 45 · 97th = co-ops.",
            },
        ],
    },
    {
        "title": "Sanction Behind Directive Principles",
        "slug": "dpsp-sanction",
        "sort_order": 6,
        "summary": "Real sanction is political / public opinion; courts may still use DPSP as beacon-lights.",
        "body": (
            "## Sanction behind Directive Principles\n\n"
            "Sir B.N. Rau recommended splitting rights into justiciable and non-justiciable — accepted by the "
            "Drafting Committee (Part III vs Part IV).\n\n"
            "- Framers gave **no legal teeth** — believed in **awakened public opinion** more than court procedures.\n"
            "- **Art. 37** duty is moral/constitutional on the State; enforcement path is **elections and politics**.\n"
            "- Still useful in courts: help uphold laws as reasonable under Art. 14 / 19 when they implement a DPSP."
        ),
        "articles": [
            (
                "Article 37",
                "Fundamental in governance; duty to apply in making laws — without judicial enforceability.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-sanction-compare",
                "type": "comparison",
                "title": "What ‘sanction’ means here",
                "columns": [
                    {
                        "id": "not",
                        "heading": "Not this",
                        "points": [
                            "Citizen cannot sue to compel a DPSP",
                            "Court cannot strike a law only for violating a DPSP",
                            "No automatic enforcement without legislation",
                        ],
                    },
                    {
                        "id": "yes",
                        "heading": "But this",
                        "points": [
                            "Political accountability / public opinion",
                            "Art. 37 duty in law-making",
                            "Beacon-light for judicial review of other laws",
                        ],
                    },
                ],
            },
            {
                "id": "dpsp-sanction-tip",
                "type": "callout",
                "tone": "tip",
                "title": "One-liner",
                "body": "Legal teeth = none · Real sanction = public opinion · Soft power in court = reasonableness shield.",
            },
        ],
    },
    {
        "title": "DPSP vs Fundamental Rights",
        "slug": "dpsp-vs-fr",
        "sort_order": 7,
        "summary": "Table 9.1 condensed — justiciable negative rights vs non-justiciable positive programme.",
        "body": (
            "## DPSP vs Fundamental Rights\n\n"
            "- **FR** — justiciable; mostly **negative** obligations (State shall not); automatically enforced; "
            "courts **must** strike violating laws.\n"
            "- **DPSP** — non-justiciable; **positive** programme (State shall strive); need legislation; "
            "courts **cannot** void a law only for violating a DPSP, but may **uphold** a law because it implements one.\n"
            "- Together: political democracy (FR) + economic/social democracy (DPSP)."
        ),
        "articles": [
            ("Part III", "Fundamental Rights — justiciable."),
            ("Part IV", "Directive Principles — non-justiciable."),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-vs-fr-compare",
                "type": "comparison",
                "title": "Fundamental Rights vs Directive Principles",
                "columns": [
                    {
                        "id": "fr",
                        "heading": "Fundamental Rights",
                        "points": [
                            "Part III — justiciable",
                            "Negative obligations on the State",
                            "Political democracy",
                            "Automatically enforced",
                            "Courts bound to void violating laws",
                        ],
                    },
                    {
                        "id": "dpsp",
                        "heading": "Directive Principles",
                        "points": [
                            "Part IV — non-justiciable (Art. 37)",
                            "Positive obligations / programmes",
                            "Social & economic democracy",
                            "Need legislation to implement",
                            "May uphold laws giving effect to a directive",
                        ],
                    },
                ],
            },
            {
                "id": "dpsp-vs-fr-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Open the FR chapter",
                "body": "For Part III depth, open the Fundamental Rights chapter — this cluster is the comparison card only.",
            },
        ],
    },
    {
        "title": "Conflict between FR and DPSP",
        "slug": "dpsp-conflict",
        "sort_order": 8,
        "summary": "Champakam → Golaknath → Art. 31C → Kesavananda → 42nd → Minerva — present balance position.",
        "body": (
            "## Conflict between Fundamental Rights and Directive Principles\n\n"
            "**Champakam Dorairajan (1951):** FR prevail; DPSP subsidiary; FR amendable → 1st, 4th, 17th Amendments.\n\n"
            "**Golaknath (1967):** Parliament cannot abridge FR to implement DPSP.\n\n"
            "**24th & 25th (1971):** 24th restores amendability of FR; 25th inserts **Art. 31C** — "
            "(1) laws for Art. **39(b)/(c)** not void for conflicting with Art. 14/19/31; "
            "(2) declaration that law gives effect to policy not open to court challenge.\n\n"
            "**Kesavananda (1973):** Art. 31C **second** provision void (judicial review = basic feature); "
            "first provision upheld.\n\n"
            "**42nd (1976):** Extended 31C protection to laws implementing **any** DPSP — later struck in Minerva.\n\n"
            "**Minerva Mills (1980):** Absolute primacy of all DPSP over Arts 14/19 invalid; "
            "**balance** of FR and DPSP is basic structure. **Present position:** FR supremacy overall; "
            "Art. 31C still shields laws for **39(b)/(c)** vs Arts 14/19; Parliament may amend FR to implement DPSP "
            "if basic structure is not damaged."
        ),
        "articles": [
            (
                "Article 31C",
                "Laws giving effect to Art. 39(b)/(c) — limited immunity from Arts 14 and 19.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-conflict-timeline",
                "type": "timeline",
                "title": "FR–DPSP conflict timeline",
                "events": [
                    {
                        "id": "e1951",
                        "year": 1951,
                        "label": "Champakam Dorairajan",
                        "detail": "FR prevail; DPSP subsidiary; FR amendable.",
                    },
                    {
                        "id": "e1967",
                        "year": 1967,
                        "label": "Golaknath",
                        "detail": "Cannot abridge FR to implement DPSP.",
                    },
                    {
                        "id": "e1971",
                        "year": 1971,
                        "label": "24th & 25th · Art. 31C",
                        "detail": "Amend FR restored; 31C for 39(b)/(c) + non-challenge clause.",
                    },
                    {
                        "id": "e1973",
                        "year": 1973,
                        "label": "Kesavananda",
                        "detail": "31C(2) void; 31C(1) upheld; basic structure.",
                    },
                    {
                        "id": "e1976",
                        "year": 1976,
                        "label": "42nd expands 31C",
                        "detail": "Any DPSP — later struck in Minerva.",
                    },
                    {
                        "id": "e1980",
                        "year": 1980,
                        "label": "Minerva Mills",
                        "detail": "Balance is basic structure; 39(b)/(c) shield remains.",
                    },
                ],
            },
            {
                "id": "dpsp-conflict-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Present position (memorise)",
                "body": (
                    "FR enjoy supremacy overall · Art. 31C still protects 39(b)/(c) laws vs Arts 14/19 · "
                    "FR may be amended to implement DPSP if basic structure survives · "
                    "Harmony of FR + DPSP = basic structure (Minerva)."
                ),
            },
        ],
    },
    {
        "title": "Criticism and Utility",
        "slug": "dpsp-criticism-utility",
        "sort_order": 9,
        "summary": "Famous critiques (cheque on a bank, dustbin of sentiments) plus why DPSP still matter.",
        "body": (
            "## Criticism and utility\n\n"
            "### Criticism (labels only)\n"
            "- **No legal force** — K.T. Shah: ‘pious superfluities’ / ‘cheque on a bank…’; "
            "T.T. Krishnamachari: ‘dustbin of sentiments’; Jennings: ‘pious aspirations’.\n"
            "- **Illogically arranged** — no consistent philosophy (Srinivasan / Jennings).\n"
            "- **Conservative** — Jennings: Fabian socialism without the socialism; 19th-century England ghosts.\n"
            "- **Constitutional conflict** (K. Santhanam) — Centre–states; President–PM; Governor–CM.\n\n"
            "### Utility (why keep them)\n"
            "- Art. 37: fundamental to governance; Ambedkar: goal of **economic democracy**.\n"
            "- Instrument of instructions; beacon-lights for courts; amplify Preamble; continuity of policy; "
            "fill Part III vacuum with socio-economic rights; opposition check; performance test; common manifesto."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "dpsp-crit-pillars",
                "type": "pillars",
                "title": "Four criticism hooks",
                "items": [
                    {
                        "id": "no-force",
                        "articles": "No legal force",
                        "label": "Cheque on a bank",
                        "slug": "dpsp-criticism-utility",
                        "detail": "K.T. Shah · Krishnamachari ‘dustbin of sentiments’.",
                        "tone": "teal",
                    },
                    {
                        "id": "illogic",
                        "articles": "Arrangement",
                        "label": "Illogically arranged",
                        "slug": "dpsp-criticism-utility",
                        "detail": "Mixes vital and trivial; no consistent philosophy.",
                        "tone": "olive",
                    },
                    {
                        "id": "fabian",
                        "articles": "Jennings",
                        "label": "Conservative / Fabian",
                        "slug": "dpsp-criticism-utility",
                        "detail": "Fabian socialism without the socialism.",
                        "tone": "gold",
                    },
                    {
                        "id": "conflict",
                        "articles": "Santhanam",
                        "label": "Constitutional conflict",
                        "slug": "dpsp-criticism-utility",
                        "detail": "Centre–states; President–PM; Governor–CM.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "dpsp-util-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Utility one-liners",
                "body": (
                    "Ambedkar = economic democracy · Austin = social revolution · "
                    "Setalvad = instrument of instructions + beacon-lights + Preamble amplifier."
                ),
            },
        ],
    },
    {
        "title": "Implementation Themes",
        "slug": "dpsp-implementation",
        "sort_order": 10,
        "summary": "Theme buckets since 1950 — not the full statute catalogue; incomplete for resource and socio-economic reasons.",
        "body": (
            "## Implementation (theme buckets)\n\n"
            "Successive governments have legislated and programmed for DPSP. Revise by **theme**, not the full list:\n\n"
            "- **Planning & redistribution** — Planning Commission → NITI Aayog; land reforms; bank/insurance nationalisation themes.\n"
            "- **Labour & women workers** — wages, factories, bonded/child labour, maternity, equal remuneration.\n"
            "- **Legal aid & justice** — Legal Services Authorities Act; Lok Adalats (Art. 39A).\n"
            "- **Rural / cottage / panchayats** — KVIC boards; rural employment schemes; **73rd** panchayati raj (Art. 40).\n"
            "- **Environment** — Wildlife / Forest Acts; pollution boards; National Forest Policy (Art. 48A).\n"
            "- **Weaker sections** — reservations; PCR / PoA Acts; NCSC/NCST; NCBC (102nd); EWS (103rd).\n"
            "- **Institutions & health** — CrPC separation of judiciary (Art. 50); PHCs; old-age pensions; non-alignment / Panchsheel (Art. 51).\n\n"
            "Incomplete implementation reasons (short): inadequate finances, unfavourable socio-economic conditions, "
            "population pressure, Centre–state strain."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "dpsp-impl-pillars",
                "type": "pillars",
                "title": "Seven implementation themes",
                "items": [
                    {
                        "id": "plan",
                        "articles": "Planning",
                        "label": "Planning & land",
                        "slug": "dpsp-implementation",
                        "detail": "Plans / NITI; land reforms; redistribution themes.",
                        "tone": "teal",
                    },
                    {
                        "id": "labour",
                        "articles": "Labour",
                        "label": "Labour & women",
                        "slug": "dpsp-implementation",
                        "detail": "Wages, child/bonded labour, maternity, equal pay.",
                        "tone": "olive",
                    },
                    {
                        "id": "legal",
                        "articles": "Art. 39A",
                        "label": "Legal aid",
                        "slug": "dpsp-implementation",
                        "detail": "Legal Services Authorities; Lok Adalats.",
                        "tone": "gold",
                    },
                    {
                        "id": "rural",
                        "articles": "Art. 40",
                        "label": "Rural & panchayats",
                        "slug": "dpsp-implementation",
                        "detail": "Cottage boards; rural jobs; 73rd Amendment.",
                        "tone": "orange",
                    },
                    {
                        "id": "env",
                        "articles": "Art. 48A",
                        "label": "Environment",
                        "slug": "dpsp-implementation",
                        "detail": "Wildlife, forests, pollution boards.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "weak",
                        "articles": "Art. 46",
                        "label": "Weaker sections",
                        "slug": "dpsp-implementation",
                        "detail": "Reservations, commissions, EWS (103rd).",
                        "tone": "maroon",
                    },
                    {
                        "id": "inst",
                        "articles": "50 · 51",
                        "label": "Institutions & peace",
                        "slug": "dpsp-implementation",
                        "detail": "Judiciary separation; health; non-alignment.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "dpsp-impl-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision stance",
                "body": (
                    "Do not memorise every Act name from Laxmikanth — map 1–2 examples per theme to the Article."
                ),
            },
        ],
    },
    {
        "title": "Directives Outside Part IV",
        "slug": "dpsp-outside-part-iv",
        "sort_order": 11,
        "summary": "Arts 335, 350-A, 351 — also non-justiciable; judiciary reads the Constitution as a whole.",
        "body": (
            "## Directives outside Part IV\n\n"
            "- **Art. 335** (Part XVI) — claims of SCs/STs to services, consistent with efficiency of administration.\n"
            "- **Art. 350-A** (Part XVII) — facilities for instruction in the **mother tongue** at primary stage for linguistic minorities.\n"
            "- **Art. 351** (Part XVII) — Union duty to promote and develop **Hindi** as a medium of expression for India’s composite culture.\n\n"
            "Also non-justiciable; courts give them equal attention because all parts of the Constitution must be read together."
        ),
        "articles": [
            ("Article 335", "Claims of SCs and STs to services."),
            ("Article 350-A", "Instruction in mother tongue at primary stage."),
            ("Article 351", "Development of the Hindi language."),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-outside-pillars",
                "type": "pillars",
                "title": "Three outside directives",
                "items": [
                    {
                        "id": "a335",
                        "articles": "Art. 335",
                        "label": "SC/ST service claims",
                        "slug": "dpsp-outside-part-iv",
                        "detail": "Consistent with maintenance of administrative efficiency.",
                        "tone": "teal",
                    },
                    {
                        "id": "a350a",
                        "articles": "Art. 350-A",
                        "label": "Mother tongue",
                        "slug": "dpsp-outside-part-iv",
                        "detail": "Primary education for linguistic minority children.",
                        "tone": "olive",
                    },
                    {
                        "id": "a351",
                        "articles": "Art. 351",
                        "label": "Hindi development",
                        "slug": "dpsp-outside-part-iv",
                        "detail": "Spread Hindi for composite culture expression.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "dpsp-outside-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam trap",
                "body": "Not every ‘directive’ lives in Part IV — 335 / 350-A / 351 are classic outside-Part-IV hooks.",
            },
        ],
    },
    {
        "title": "Articles at a Glance",
        "slug": "dpsp-articles-glance",
        "sort_order": 12,
        "summary": "Table 9.2 memory index — Arts 36–51 subject matter for quick recall.",
        "body": (
            "## Articles related to DPSP (at a glance)\n\n"
            "- **36** State · **37** Application / nature\n"
            "- **38** Social order / welfare · **39** Policy principles · **39A** Equal justice & legal aid\n"
            "- **40** Panchayats · **41** Work, education, assistance · **42** Work conditions & maternity\n"
            "- **43** Living wage · **43A** Workers in management · **43B** Co-operatives\n"
            "- **44** UCC · **45** Early childhood (0–6) · **46** Weaker sections\n"
            "- **47** Nutrition / health / prohibition · **48** Agriculture / cattle · **48A** Environment\n"
            "- **49** Monuments · **50** Separate judiciary · **51** International peace\n\n"
            "Note: substantive directives are **38–51**; 36–37 are definition and application."
        ),
        "articles": [
            ("Part IV (Arts 36–51)", "Directive Principles of State Policy — full article map."),
        ],
        "visual_blocks": [
            {
                "id": "dpsp-glance-tree",
                "type": "tree",
                "title": "Part IV map",
                "root": {
                    "id": "part-iv",
                    "label": "Part IV DPSP",
                    "detail": "Arts 36–51",
                    "children": [
                        {
                            "id": "gate",
                            "label": "36–37 Gate",
                            "detail": "State definition · application / Art. 37",
                            "slug": "dpsp-features",
                        },
                        {
                            "id": "soc",
                            "label": "Socialistic",
                            "detail": "38 · 39 · 39A · 41 · 42 · 43 · 43A · 47",
                            "slug": "dpsp-socialistic",
                        },
                        {
                            "id": "gan",
                            "label": "Gandhian",
                            "detail": "40 · 43 · 43B · 46 · 47 · 48",
                            "slug": "dpsp-gandhian",
                        },
                        {
                            "id": "lib",
                            "label": "Liberal–intellectual",
                            "detail": "44 · 45 · 48 · 48A · 49 · 50 · 51",
                            "slug": "dpsp-liberal",
                        },
                    ],
                },
            },
            {
                "id": "dpsp-glance-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision index",
                "body": "Use this cluster as a last-minute map — drill open socialistic / Gandhian / liberal for one-liners.",
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "dpsp-features"),
    (HUB_SLUG, "parent", "dpsp-socialistic"),
    (HUB_SLUG, "parent", "dpsp-gandhian"),
    (HUB_SLUG, "parent", "dpsp-liberal"),
    (HUB_SLUG, "parent", "dpsp-new-amendments"),
    (HUB_SLUG, "parent", "dpsp-sanction"),
    (HUB_SLUG, "parent", "dpsp-vs-fr"),
    (HUB_SLUG, "parent", "dpsp-conflict"),
    (HUB_SLUG, "parent", "dpsp-criticism-utility"),
    (HUB_SLUG, "parent", "dpsp-implementation"),
    (HUB_SLUG, "parent", "dpsp-outside-part-iv"),
    (HUB_SLUG, "parent", "dpsp-articles-glance"),
    ("dpsp-vs-fr", "related", "fundamental-rights"),
    ("dpsp-conflict", "related", "fundamental-rights"),
    ("dpsp-features", "related", "dpsp-sanction"),
    ("dpsp-socialistic", "related", "dpsp-gandhian"),
    ("dpsp-gandhian", "related", "dpsp-liberal"),
    ("dpsp-new-amendments", "related", "dpsp-conflict"),
    ("dpsp-articles-glance", "related", "dpsp-socialistic"),
    ("dpsp-articles-glance", "related", "dpsp-gandhian"),
    ("dpsp-articles-glance", "related", "dpsp-liberal"),
    ("dpsp-implementation", "related", "dpsp-socialistic"),
    ("dpsp-outside-part-iv", "related", "dpsp-features"),
]

SAMPLE_PYQS = [
    (
        2015,
        "The ideal of 'Welfare State' in the Indian Constitution is enshrined in its:",
        "Directive Principles of State Policy (Part IV).",
        [HUB_SLUG, "dpsp-features"],
    ),
    (
        2013,
        "According to the Constitution of India, which of the following are fundamental to the governance of the country?",
        "Directive Principles of State Policy (Article 37).",
        ["dpsp-features", "dpsp-sanction", HUB_SLUG],
    ),
    (
        2017,
        "Which principle among the following was added to the Directive Principles of State Policy by the 42nd Amendment?",
        "Equal justice and free legal aid (Art. 39A) — also children, workers’ participation, environment.",
        ["dpsp-new-amendments", "dpsp-socialistic"],
    ),
    (
        2020,
        "With reference to the provisions of the Constitution, consider the balance between Fundamental Rights and Directive Principles:",
        "Minerva Mills (1980) — Constitution founded on the bedrock of balance between FR and DPSP; harmony is basic structure.",
        ["dpsp-conflict", "dpsp-vs-fr", HUB_SLUG],
    ),
    (
        2002,
        "The 86th Constitutional Amendment Act changed Article 45. The amended directive requires the State to provide:",
        "Early childhood care and education for all children until they complete the age of six years.",
        ["dpsp-new-amendments", "dpsp-liberal"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "State of Madras v. Champakam Dorairajan",
        "slug": "champakam-dorairajan",
        "parties": "State of Madras v. Champakam Dorairajan",
        "year": 1951,
        "court": CaseLaw.Court.SC,
        "summary": "Early FR–DPSP conflict — FR prevail; DPSP run as subsidiary.",
        "holding": (
            "In case of conflict, Fundamental Rights prevail over Directive Principles; "
            "DPSP have to conform to and run as subsidiary to FR. FR remain amendable."
        ),
        "concept_slugs": ["dpsp-conflict", "dpsp-vs-fr", HUB_SLUG],
    },
    {
        "title": "Golaknath v. State of Punjab",
        "slug": "golaknath",
        "parties": "Golak Nath v. State of Punjab",
        "year": 1967,
        "court": CaseLaw.Court.SC,
        "summary": "Parliament cannot abridge Fundamental Rights to implement DPSP.",
        "holding": (
            "Fundamental Rights are sacrosanct — Parliament cannot take away or abridge them "
            "for implementing Directive Principles."
        ),
        "concept_slugs": ["dpsp-conflict", HUB_SLUG],
    },
    {
        "title": "Kesavananda Bharati v. State of Kerala",
        "slug": "kesavananda-bharati",
        "parties": "Kesavananda Bharati v. State of Kerala",
        "year": 1973,
        "court": CaseLaw.Court.SC,
        "summary": "Basic structure; Art. 31C second provision struck; first provision upheld.",
        "holding": (
            "Judicial review is a basic feature — Art. 31C’s bar on questioning a policy declaration "
            "is unconstitutional; the first limb protecting laws for Art. 39(b)/(c) was upheld."
        ),
        "concept_slugs": ["dpsp-conflict", HUB_SLUG],
    },
    {
        "title": "Minerva Mills v. Union of India",
        "slug": "minerva-mills",
        "parties": "Minerva Mills Ltd. v. Union of India",
        "year": 1980,
        "court": CaseLaw.Court.SC,
        "summary": "FR–DPSP balance is basic structure; 42nd expansion of Art. 31C struck.",
        "holding": (
            "The Constitution is founded on the bedrock of the balance between Fundamental Rights "
            "and Directive Principles. Absolute primacy of all DPSP over Arts 14/19 is invalid; "
            "Art. 39(b)/(c) shield under Art. 31C remains."
        ),
        "concept_slugs": ["dpsp-conflict", "dpsp-vs-fr", HUB_SLUG],
    },
]

AMENDMENTS = [
    {
        "number": 25,
        "year": 1971,
        "title": "Twenty-fifth Amendment",
        "summary": "Inserted Article 31C — limited immunity for laws implementing Art. 39(b) and (c).",
        "effect": (
            "Laws for 39(b)/(c) shielded from Arts 14/19/31; non-challenge clause later struck in Kesavananda."
        ),
        "concept_slugs": ["dpsp-conflict", "dpsp-new-amendments", HUB_SLUG],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": "Added four new DPSPs and tried to extend Art. 31C to all Directive Principles.",
        "effect": "Arts 39A, 43A, 48A (+ Art. 39 children); 31C expansion later void in Minerva Mills.",
        "concept_slugs": ["dpsp-new-amendments", "dpsp-conflict", HUB_SLUG],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": "Added Art. 38 duty to minimise inequalities; omitted Art. 31 (property as FR).",
        "effect": "Inequalities clause in Art. 38; property exit from Part III reshaped FR–DPSP landscape.",
        "concept_slugs": ["dpsp-new-amendments", "dpsp-socialistic", HUB_SLUG],
    },
    {
        "number": 86,
        "year": 2002,
        "title": "Eighty-sixth Amendment",
        "summary": "Elementary education became FR (Art. 21A); Art. 45 rewritten for early childhood care.",
        "effect": "Art. 45 now covers care and education until age six.",
        "concept_slugs": ["dpsp-new-amendments", "dpsp-liberal", HUB_SLUG],
    },
    {
        "number": 97,
        "year": 2011,
        "title": "Ninety-seventh Amendment",
        "summary": "Added Art. 43B — promotion of co-operative societies as a Directive Principle.",
        "effect": "Constitutional push for voluntary, autonomous, democratic, professional co-ops.",
        "concept_slugs": ["dpsp-new-amendments", "dpsp-gandhian", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed Directive Principles of State Policy chapter (Laxmikanth Ch.9)."

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
                "title": "Directive Principles of State Policy",
                "sort_order": 9,
                "book_ref": "Laxmikanth 8th Ed, Ch. 9",
                "summary": (
                    "Visual revision of Part IV — compass mental model, classification, "
                    "FR–DPSP conflict timeline, and article glance map."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Directive Principles of State Policy",
                "summary": (
                    "Part IV non-justiciable guidelines for a welfare state — "
                    "social & economic democracy; fundamental in governance (Art. 37)."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **compass mental model**, then scan the **twelve clusters**. "
                    "Drill classification and the FR–DPSP conflict timeline hardest. "
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
            ref="Part IV (Arts 36–51)",
            excerpt="Directive Principles — socialistic, Gandhian, liberal–intellectual; non-justiciable.",
            sort_order=0,
        )

        dpsp_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=dpsp_slugs, source__subject=subject
        ).filter(
            target__slug__in=dpsp_slugs | {"fundamental-rights"}
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
                case.concepts.set(concepts)

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
                amendment.concepts.set(concepts)

        self.stdout.write(
            self.style.SUCCESS(
                f"DPSP chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments."
            )
        )
