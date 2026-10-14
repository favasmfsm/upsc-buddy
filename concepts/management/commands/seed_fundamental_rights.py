"""Seed Laxmikanth Ch.8 Fundamental Rights pilot (visual grammar MVP)."""

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

HUB_SLUG = "fundamental-rights"
CHAPTER_SLUG = "fundamental-rights"

PILLAR_ITEMS = [
    {
        "id": "equality",
        "articles": "Articles 14 to 18",
        "label": "Right to Equality",
        "slug": "fr-equality-14-18",
        "detail": "Equality before law, non-discrimination, untouchability, titles.",
        "tone": "teal",
    },
    {
        "id": "freedom",
        "articles": "Articles 19 to 22",
        "label": "Right to Freedom",
        "slug": "fr-right-to-freedom",
        "detail": "Six freedoms, protection in conviction, life & liberty, safeguards in arrest.",
        "tone": "olive",
    },
    {
        "id": "exploitation",
        "articles": "Articles 23 to 24",
        "label": "Right against Exploitation",
        "slug": "fr-against-exploitation",
        "detail": "Traffic in humans, forced labour, and child labour bans.",
        "tone": "gold",
    },
    {
        "id": "religion",
        "articles": "Articles 25 to 28",
        "label": "Right to Freedom of Religion",
        "slug": "fr-freedom-religion",
        "detail": "Conscience, practice, and manage religious affairs — with public-order limits.",
        "tone": "orange",
    },
    {
        "id": "cultural",
        "articles": "Articles 29 to 30",
        "label": "Cultural and Educational Rights",
        "slug": "fr-cultural-educational",
        "detail": "Protect language/culture of minorities; minority educational institutions.",
        "tone": "terracotta",
    },
    {
        "id": "remedies",
        "articles": "Article 32",
        "label": "Right to Constitutional Remedies",
        "slug": "fr-remedies-32",
        "detail": "Move the Supreme Court to enforce FR — heart and soul of the Constitution.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "fr-shield-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Shield",
        "topic_label": "Fundamental Rights",
        "subject_label": "Citizen",
        "relation_label": "Protects you from",
        "protects_from": [
            "State abuse",
            "Discrimination",
            "Arbitrary arrest",
            "Exploitation",
        ],
        "insight": (
            "Fundamental Rights are constitutional protective shields around every citizen. "
            "Build this intuition before memorising Articles."
        ),
    },
    {
        "id": "fr-six-pillars",
        "type": "pillars",
        "title": "Six pillars of Fundamental Rights",
        "items": PILLAR_ITEMS,
    },
    {
        "id": "fr-features-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Start from the shield, then the six pillars. "
            "Art. 12 (State) sits beside the pillars — open it before applying any right."
        ),
    },
    {
        "id": "fr-constitution-tree",
        "type": "tree",
        "title": "Where FR sits in the Constitution",
        "root": {
            "id": "constitution",
            "label": "Constitution",
            "detail": "Supreme law of India",
            "children": [
                {
                    "id": "fr",
                    "label": "Fundamental Rights",
                    "slug": "fundamental-rights",
                    "detail": "Part III — justiciable",
                    "children": [
                        {
                            "id": "eq",
                            "label": "Equality",
                            "slug": "fr-equality-14-18",
                        },
                        {
                            "id": "free",
                            "label": "Freedom",
                            "slug": "fr-right-to-freedom",
                        },
                        {
                            "id": "exp",
                            "label": "Exploitation",
                            "slug": "fr-against-exploitation",
                        },
                        {
                            "id": "rel",
                            "label": "Religion",
                            "slug": "fr-freedom-religion",
                        },
                        {
                            "id": "cul",
                            "label": "Culture & Education",
                            "slug": "fr-cultural-educational",
                        },
                        {
                            "id": "rem",
                            "label": "Constitutional Remedies",
                            "slug": "fr-remedies-32",
                        },
                    ],
                },
                {
                    "id": "dpsp",
                    "label": "DPSP",
                    "slug": "directive-principles",
                    "detail": "Part IV — non-justiciable",
                },
                {
                    "id": "fd",
                    "label": "Fundamental Duties",
                    "detail": "Part IVA",
                },
            ],
        },
    },
    {
        "id": "fr-vs-dpsp",
        "type": "comparison",
        "title": "Fundamental Rights vs Directive Principles",
        "columns": [
            {
                "id": "fr",
                "heading": "Fundamental Rights",
                "points": [
                    "Justiciable / enforceable in courts",
                    "Mostly negative obligations on the State",
                    "Courts protect the individual",
                ],
            },
            {
                "id": "dpsp",
                "heading": "Directive Principles",
                "points": [
                    "Non-justiciable (Art. 37)",
                    "Positive obligations — programmes for the State",
                    "Government implements; courts may interpret in light of them",
                ],
            },
        ],
    },
    {
        "id": "fr-which-article",
        "type": "flowchart",
        "title": "Which Article applies?",
        "root": "problem",
        "steps": [
            {
                "id": "problem",
                "label": "What is the problem?",
                "detail": "Start from the fact pattern, then pick the cluster.",
                "options": [
                    {"label": "Arrest / detention", "next": "arrest"},
                    {"label": "Speech / expression", "next": "speech"},
                    {"label": "Equality / discrimination", "next": "equality"},
                    {"label": "Religion", "next": "religion"},
                    {"label": "Remedy / enforcement", "next": "remedy"},
                ],
            },
            {
                "id": "arrest",
                "label": "Article 22",
                "detail": "Safeguards in arrest and preventive detention — also check Art. 21 fairness.",
            },
            {
                "id": "speech",
                "label": "Article 19(1)(a)",
                "detail": "Freedom of speech — then test reasonable restrictions under 19(2).",
            },
            {
                "id": "equality",
                "label": "Article 14 (and 15–16)",
                "detail": "Equality before law; non-discrimination and public employment as needed.",
            },
            {
                "id": "religion",
                "label": "Article 25",
                "detail": "Freedom of conscience and free profession, practice, and propagation — with public-order limits.",
            },
            {
                "id": "remedy",
                "label": "Article 32",
                "detail": "Move the Supreme Court to enforce FR; High Courts via Art. 226.",
            },
        ],
    },
    {
        "id": "fr-pyq-heatmap",
        "type": "pyq_heatmap",
        "title": "PYQ focus across Fundamental Rights",
        "items": [
            {"concept_slug": "fr-equality-14-18", "label": "Equality"},
            {"concept_slug": "fr-right-to-freedom", "label": "Freedom"},
            {"concept_slug": "fr-against-exploitation", "label": "Exploitation"},
            {"concept_slug": "fr-freedom-religion", "label": "Religion"},
            {
                "concept_slug": "fr-cultural-educational",
                "label": "Culture & Education",
            },
            {"concept_slug": "fr-remedies-32", "label": "Constitutional Remedies"},
        ],
    },
    {
        "id": "fr-property-timeline",
        "type": "timeline",
        "title": "Right to Property — evolution",
        "events": [
            {
                "id": "e1950",
                "year": 1950,
                "label": "Property as FR",
                "detail": "Constitution in force — property in Part III.",
            },
            {
                "id": "e1978a",
                "year": 1978,
                "label": "44th Amendment",
                "detail": "Property ceases to be a Fundamental Right.",
            },
            {
                "id": "e1978b",
                "year": 1978,
                "label": "Legal right (Art. 300A)",
                "detail": "Present Constitution — constitutional/legal right.",
            },
        ],
    },
]

CLUSTERS = [
    {
        "title": "State — Article 12",
        "slug": "fr-state-article-12",
        "sort_order": 1,
        "summary": "Who counts as 'State' for Fundamental Rights — government and its instrumentalities.",
        "body": "Art. 12 is the gate: decide if the body is State before applying any FR.",
        "articles": [
            (
                "Article 12",
                "Defines State to include Government and Parliament of India, Governments and Legislatures of States, and all local or other authorities within India or under the control of the Government of India.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "art12-tree",
                "type": "flowchart",
                "title": "Is this body 'State'?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What kind of body?",
                        "detail": "Match the body to an Art. 12 pathway.",
                        "options": [
                            {"label": "Union / State govt or legislature", "next": "yes-state"},
                            {"label": "Local authority", "next": "yes-state"},
                            {"label": "Other authority / board / PSU", "next": "instrumentality"},
                            {"label": "Judiciary acting judicially", "next": "not-classic"},
                        ],
                    },
                    {
                        "id": "yes-state",
                        "label": "Treat as State",
                        "detail": "FR can apply — pick the relevant Articles next.",
                    },
                    {
                        "id": "instrumentality",
                        "label": "Run instrumentality tests",
                        "detail": "Deep/pervasive control, public function, financial dependence (Ajay Hasia line).",
                        "options": [
                            {"label": "Tests point to State", "next": "yes-state"},
                            {"label": "Borderline / unclear", "next": "case-by-case"},
                        ],
                    },
                    {
                        "id": "case-by-case",
                        "label": "Case-by-case",
                        "detail": "UPSC loves borderline bodies — argue both sides briefly.",
                    },
                    {
                        "id": "not-classic",
                        "label": "Generally not 'State' (classic framing)",
                        "detail": "Do not confuse with judicial review of FR violations.",
                    },
                ],
            },
            {
                "id": "art12-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": "Judiciary when acting judicially is generally not 'State' for Art. 12 in the classic framing.",
            },
        ],
    },
    {
        "title": "Right to Equality (Arts 14–18)",
        "slug": "fr-equality-14-18",
        "sort_order": 2,
        "summary": "Equality before law, equal protection, non-discrimination, and related equality rights.",
        "body": "Revise 14–18 as one equality package: general rule (14), then specific bans (15–18).",
        "articles": [
            ("Article 14", "Equality before law and equal protection of the laws."),
            (
                "Article 15",
                "Prohibition of discrimination on grounds of religion, race, caste, sex or place of birth.",
            ),
            ("Article 16", "Equality of opportunity in public employment."),
            ("Article 17", "Abolition of untouchability."),
            ("Article 18", "Abolition of titles."),
        ],
        "visual_blocks": [
            {
                "id": "eq-pillars",
                "type": "pillars",
                "title": "Equality articles",
                "items": [
                    {
                        "id": "a14",
                        "articles": "Article 14",
                        "label": "Equality before law",
                        "slug": "fr-equality-14-18",
                        "detail": "Equality before law + equal protection; reasonable classification allowed.",
                        "tone": "teal",
                    },
                    {
                        "id": "a15",
                        "articles": "Article 15",
                        "label": "Non-discrimination",
                        "slug": "fr-equality-14-18",
                        "detail": "No discrimination by State; special provisions for women, children, SEBCs, etc.",
                        "tone": "olive",
                    },
                    {
                        "id": "a16",
                        "articles": "Article 16",
                        "label": "Public employment",
                        "slug": "fr-equality-14-18",
                        "detail": "Equality of opportunity; reservation exceptions.",
                        "tone": "gold",
                    },
                    {
                        "id": "a17",
                        "articles": "Article 17",
                        "label": "Untouchability",
                        "slug": "fr-equality-14-18",
                        "detail": "Abolished — enforceable with supporting law.",
                        "tone": "orange",
                    },
                    {
                        "id": "a18",
                        "articles": "Article 18",
                        "label": "Titles",
                        "slug": "fr-equality-14-18",
                        "detail": "No titles (military/academic distinctions excepted).",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "eq-comparison",
                "type": "comparison",
                "title": "Art. 14 tests",
                "columns": [
                    {
                        "id": "classification",
                        "heading": "Reasonable classification",
                        "points": [
                            "Intelligible differentia",
                            "Rational relation to object",
                        ],
                    },
                    {
                        "id": "arbitrariness",
                        "heading": "Non-arbitrariness",
                        "points": [
                            "State action must not be arbitrary",
                            "Often read with Arts 19 & 21",
                        ],
                    },
                ],
            },
            {
                "id": "eq-journey",
                "type": "journey",
                "title": "Citizen wants a government job",
                "stages": [
                    {
                        "id": "s1",
                        "label": "Citizen",
                        "detail": "Seeks public employment.",
                    },
                    {
                        "id": "s2",
                        "label": "Article 16",
                        "detail": "Equality of opportunity in public employment.",
                        "slug": "fr-equality-14-18",
                    },
                    {
                        "id": "s3",
                        "label": "Reservation / exceptions",
                        "detail": "Special provisions and constitutional limits.",
                    },
                    {
                        "id": "s4",
                        "label": "Case law",
                        "detail": "Indra Sawhney themes on reservations.",
                        "case_slug": "indra-sawhney",
                    },
                ],
            },
        ],
    },
    {
        "title": "Right to Freedom (Arts 19–22)",
        "slug": "fr-right-to-freedom",
        "sort_order": 3,
        "summary": "Umbrella for Arts 19–22 — drill into Art. 19 and Art. 21 for deep revision.",
        "body": "Use this page to place 19–22, then open Art. 19 and Art. 21 for depth.",
        "articles": [
            ("Article 19", "Six freedoms of citizens with reasonable restrictions."),
            ("Article 20", "Protection in respect of conviction for offences."),
            ("Article 21", "Life and personal liberty."),
            ("Article 22", "Protection against arrest and detention in certain cases."),
        ],
        "visual_blocks": [
            {
                "id": "freedom-pillars",
                "type": "pillars",
                "title": "Arts 19–22",
                "items": [
                    {
                        "id": "a19",
                        "articles": "Article 19",
                        "label": "Six freedoms",
                        "slug": "fr-freedom-19",
                        "detail": "Speech, assembly, association, movement, residence, profession — citizens only.",
                        "tone": "olive",
                    },
                    {
                        "id": "a20",
                        "articles": "Article 20",
                        "label": "Conviction safeguards",
                        "slug": "fr-right-to-freedom",
                        "detail": "Ex post facto, double jeopardy, self-incrimination.",
                        "tone": "gold",
                    },
                    {
                        "id": "a21",
                        "articles": "Article 21",
                        "label": "Life & liberty",
                        "slug": "fr-life-liberty-21",
                        "detail": "Open-textured right — Maneka / privacy / dignity themes.",
                        "tone": "teal",
                    },
                    {
                        "id": "a22",
                        "articles": "Article 22",
                        "label": "Arrest & detention",
                        "slug": "fr-right-to-freedom",
                        "detail": "Arrest safeguards and preventive detention regime.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "freedom-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Where to go next",
                "body": "Open Art. 19 for restrictions and Art. 21 for the expansion engine. Keep 20 and 22 as one-liners until you drill deeper.",
            },
        ],
    },
    {
        "title": "Freedom under Article 19",
        "slug": "fr-freedom-19",
        "sort_order": 4,
        "summary": "Six freedoms of citizens and the scheme of reasonable restrictions.",
        "body": "Freedom → restriction by law → listed ground → reasonableness.",
        "articles": [
            (
                "Article 19(1)",
                "Six freedoms: speech & expression, assembly, association, movement, residence, profession.",
            ),
            (
                "Article 19(2)–(6)",
                "Grounds of reasonable restrictions for each freedom.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "a19-speech-restrictions",
                "type": "flowchart",
                "title": "Freedom of speech — reasonable restrictions",
                "root": "speech",
                "steps": [
                    {
                        "id": "speech",
                        "label": "Freedom of speech (Art. 19(1)(a))",
                        "detail": "Citizens may speak and express — subject to 19(2).",
                        "options": [
                            {"label": "Allowed zone", "next": "allowed"},
                            {"label": "Restricted by", "next": "restricted"},
                        ],
                    },
                    {
                        "id": "allowed",
                        "label": "Expression is protected",
                        "detail": "Unless a valid law imposes a listed, reasonable restriction.",
                    },
                    {
                        "id": "restricted",
                        "label": "Grounds under Art. 19(2)",
                        "detail": "Restriction must be by law, on a listed ground, and reasonable.",
                        "options": [
                            {"label": "Security of the State", "next": "security"},
                            {"label": "Public order", "next": "public-order"},
                            {"label": "Decency or morality", "next": "morality"},
                            {"label": "Contempt of court", "next": "contempt"},
                            {"label": "Defamation", "next": "defamation"},
                        ],
                    },
                    {
                        "id": "security",
                        "label": "Security of the State",
                        "detail": "Classic ground — distinguish from vague 'interest of the government'.",
                    },
                    {
                        "id": "public-order",
                        "label": "Public order",
                        "detail": "Narrower than 'law and order' in some SC readings.",
                    },
                    {
                        "id": "morality",
                        "label": "Decency or morality",
                        "detail": "Often tested with obscenity / community standards themes.",
                    },
                    {
                        "id": "contempt",
                        "label": "Contempt of court",
                        "detail": "Speech vs court authority — listed ground under 19(2).",
                    },
                    {
                        "id": "defamation",
                        "label": "Defamation",
                        "detail": "Criminal / civil defamation as a restriction theme in PYQs.",
                    },
                ],
            },
            {
                "id": "a19-vs-21",
                "type": "comparison",
                "title": "Art. 19 vs Art. 21",
                "columns": [
                    {
                        "id": "a19",
                        "heading": "Article 19",
                        "points": [
                            "Citizens only",
                            "Six enumerated freedoms",
                            "Reasonable restrictions listed",
                        ],
                    },
                    {
                        "id": "a21",
                        "heading": "Article 21",
                        "points": [
                            "All persons",
                            "Life & personal liberty (open-textured)",
                            "Procedure established by law + fairness (Maneka)",
                        ],
                    },
                ],
            },
            {
                "id": "a19-explorer",
                "type": "article_explorer",
                "title": "Article 19 explorer",
                "article_ref": "Article 19",
                "stages": [
                    {
                        "id": "topic",
                        "label": "Freedom of Speech",
                        "detail": "Art. 19(1)(a) — citizens; expression includes press themes.",
                    },
                    {
                        "id": "exceptions",
                        "label": "Exceptions",
                        "detail": "Reasonable restrictions under 19(2) — listed grounds + reasonableness.",
                    },
                    {
                        "id": "cases",
                        "label": "Landmark Cases",
                        "detail": "Use restriction + golden-triangle cases in revision notes.",
                    },
                    {
                        "id": "pyqs",
                        "label": "PYQs",
                        "detail": "Grounds under 19(2) and citizen-only framing are high-yield.",
                    },
                    {
                        "id": "ca",
                        "label": "Current Affairs",
                        "detail": "Placeholder until CA module links news to Art. 19.",
                    },
                ],
            },
            {
                "id": "a19-simulator",
                "type": "simulator",
                "title": "What if: Government bans a newspaper",
                "start": "q1",
                "nodes": {
                    "q1": {
                        "prompt": "Which right is primarily engaged?",
                        "choices": [
                            {"label": "Article 19(1)(a)", "next": "q2"},
                            {"label": "Article 21 only", "next": "wrong1"},
                        ],
                    },
                    "q2": {
                        "prompt": "Can Government do this?",
                        "choices": [
                            {
                                "label": "Yes, if a reasonable restriction under 19(2)",
                                "next": "end_ok",
                            },
                            {
                                "label": "Never, under any circumstances",
                                "next": "wrong2",
                            },
                        ],
                    },
                    "end_ok": {
                        "prompt": "Correct — listed ground + reasonableness still required.",
                        "choices": [],
                    },
                    "wrong1": {
                        "prompt": "Press/speech is classically Art. 19 — try again.",
                        "choices": [{"label": "Back", "next": "q1"}],
                    },
                    "wrong2": {
                        "prompt": "Speech is not absolute — 19(2) exists. Try again.",
                        "choices": [{"label": "Back", "next": "q2"}],
                    },
                },
            },
        ],
    },
    {
        "title": "Life and Personal Liberty — Article 21",
        "slug": "fr-life-liberty-21",
        "sort_order": 5,
        "summary": "Expanded right to life and personal liberty — procedure, dignity, and derived rights.",
        "body": "After Maneka: deprivation needs fair, just, reasonable procedure — often with Arts 14 & 19.",
        "articles": [
            (
                "Article 21",
                "No person shall be deprived of life or personal liberty except according to procedure established by law.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "a21-flowchart",
                "type": "flowchart",
                "title": "Art. 21 path",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Is life / personal liberty affected?",
                        "detail": "Includes dignity, privacy, livelihood themes — stick to high-yield examples.",
                        "options": [
                            {"label": "Yes — check the law", "next": "law"},
                            {"label": "No clear deprivation", "next": "stop"},
                        ],
                    },
                    {
                        "id": "stop",
                        "label": "Art. 21 may not be the lead Article",
                        "detail": "Re-check whether another FR fits better.",
                    },
                    {
                        "id": "law",
                        "label": "Is there a valid law?",
                        "detail": "Deprivation needs legal backing.",
                        "options": [
                            {"label": "Law exists — test procedure", "next": "procedure"},
                            {"label": "No law / pure executive whim", "next": "fails"},
                        ],
                    },
                    {
                        "id": "procedure",
                        "label": "Is procedure fair, just, reasonable?",
                        "detail": "Maneka Gandhi — links to Arts 14 & 19 (golden triangle).",
                        "options": [
                            {"label": "Yes", "next": "passes"},
                            {"label": "Arbitrary / unfair", "next": "fails"},
                        ],
                    },
                    {
                        "id": "passes",
                        "label": "Art. 21 likely satisfied",
                        "detail": "Still check related rights and remedies.",
                    },
                    {
                        "id": "fails",
                        "label": "Art. 21 challenge is strong",
                        "detail": "Privacy (Puttaswamy), livelihood (Olga Tellis) are classic expansions.",
                    },
                ],
            },
            {
                "id": "a21-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Golden triangle",
                "body": "Arts 14, 19, and 21 are often read together after Maneka. High-yield themes: fair procedure, privacy, livelihood — not an endless list.",
            },
            {
                "id": "a21-case-network",
                "type": "case_network",
                "title": "Article 21 — landmark cases",
                "hub_label": "Article 21",
                "cases": [
                    {
                        "id": "mg",
                        "label": "Maneka Gandhi",
                        "year": 1978,
                        "detail": "Procedure must be fair, just, and reasonable.",
                        "case_slug": "maneka-gandhi",
                    },
                    {
                        "id": "putt",
                        "label": "Puttaswamy",
                        "year": 2017,
                        "detail": "Privacy as part of life and liberty.",
                        "case_slug": "puttaswamy",
                    },
                    {
                        "id": "olga",
                        "label": "Olga Tellis",
                        "year": 1985,
                        "detail": "Livelihood as a facet of life.",
                        "case_slug": "olga-tellis",
                    },
                    {
                        "id": "vish",
                        "label": "Vishaka",
                        "year": 1997,
                        "detail": "Workplace dignity — Arts 14, 15, 19, 21.",
                        "case_slug": "vishaka",
                    },
                    {
                        "id": "navtej",
                        "label": "Navtej Johar",
                        "year": 2018,
                        "detail": "Dignity, equality, and privacy readings.",
                        "case_slug": "navtej-johar",
                    },
                ],
            },
        ],
    },
    {
        "title": "Right against Exploitation (Arts 23–24)",
        "slug": "fr-against-exploitation",
        "sort_order": 6,
        "summary": "Traffic in human beings, forced labour, and child labour bans.",
        "body": "Two Articles as a pair: 23 (traffic / forced labour) and 24 (child labour).",
        "articles": [
            ("Article 23", "Prohibition of traffic in human beings and forced labour."),
            ("Article 24", "Prohibition of employment of children in factories, etc."),
        ],
        "visual_blocks": [
            {
                "id": "exploit-tree",
                "type": "flowchart",
                "title": "Which exploitation Article?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What is the fact pattern?",
                        "detail": "Pick 23 or 24 from the harm described.",
                        "options": [
                            {"label": "Traffic / begar / forced labour", "next": "a23"},
                            {"label": "Child under 14 in hazardous work", "next": "a24"},
                        ],
                    },
                    {
                        "id": "a23",
                        "label": "Article 23",
                        "detail": "Traffic in human beings and forced labour — also binds private persons in the core framing.",
                    },
                    {
                        "id": "a24",
                        "label": "Article 24",
                        "detail": "No child below 14 in factories, mines, or other hazardous employment.",
                    },
                ],
            },
            {
                "id": "exploit-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision pair",
                "body": "Remember 23 and 24 together — UPSC often tests which Article fits the vignette.",
            },
        ],
    },
    {
        "title": "Right to Freedom of Religion (Arts 25–28)",
        "slug": "fr-freedom-religion",
        "sort_order": 7,
        "summary": "Conscience, practice, and manage religious affairs — with public-order limits.",
        "body": "Start with 25 (person) vs 26 (denomination); 27–28 are tax and education limits.",
        "articles": [
            ("Article 25", "Freedom of conscience and free profession, practice and propagation of religion."),
            ("Article 26", "Freedom to manage religious affairs."),
            ("Article 27", "Freedom from taxation for promotion of any religion."),
            ("Article 28", "Freedom as to attendance at religious instruction in certain institutions."),
        ],
        "visual_blocks": [
            {
                "id": "religion-comparison",
                "type": "comparison",
                "title": "Individual vs denomination",
                "columns": [
                    {
                        "id": "a25",
                        "heading": "Art. 25 (person)",
                        "points": [
                            "Conscience + practice + propagation",
                            "Subject to public order, morality, health",
                            "State can regulate secular aspects",
                        ],
                    },
                    {
                        "id": "a26",
                        "heading": "Art. 26 (denomination)",
                        "points": [
                            "Establish & maintain institutions",
                            "Manage own affairs in religion",
                            "Own and administer property",
                        ],
                    },
                ],
            },
            {
                "id": "religion-tip",
                "type": "callout",
                "tone": "tip",
                "title": "27 & 28 one-liners",
                "body": "27 — no tax for promoting a religion. 28 — limits on religious instruction in certain State-funded institutions.",
            },
        ],
    },
    {
        "title": "Cultural and Educational Rights (Arts 29–30)",
        "slug": "fr-cultural-educational",
        "sort_order": 8,
        "summary": "Protect minority language/culture and educational institutions.",
        "body": "29 protects culture/language of sections; 30 is the minority educational-institution right.",
        "articles": [
            ("Article 29", "Protection of interests of minorities."),
            ("Article 30", "Right of minorities to establish and administer educational institutions."),
        ],
        "visual_blocks": [
            {
                "id": "cultural-comparison",
                "type": "comparison",
                "title": "Article 29 vs Article 30",
                "columns": [
                    {
                        "id": "a29",
                        "heading": "Article 29",
                        "points": [
                            "Conserve language, script, culture",
                            "No denial of admission on religion/race/caste/language in State-aided institutions",
                        ],
                    },
                    {
                        "id": "a30",
                        "heading": "Article 30",
                        "points": [
                            "Minorities: establish & administer schools",
                            "Classic UPSC theme with aid and regulation",
                        ],
                    },
                ],
            },
            {
                "id": "cultural-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Wording trap",
                "body": "Do not casually conflate 'any section of citizens' (29) with 'religious or linguistic minorities' (30).",
            },
        ],
    },
    {
        "title": "Constitutional Remedies — Article 32",
        "slug": "fr-remedies-32",
        "sort_order": 9,
        "summary": "Right to move the Supreme Court for enforcement of Fundamental Rights; writs.",
        "body": "Art. 32 is itself a Fundamental Right — pick the writ from the harm.",
        "articles": [
            (
                "Article 32",
                "Right to move the Supreme Court by appropriate proceedings for enforcement of FR; SC may issue writs.",
            ),
            (
                "Article 226",
                "High Courts may issue writs for FR and for other purposes — wider than Art. 32.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "writs-tree",
                "type": "flowchart",
                "title": "Which writ?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What do you need the court to do?",
                        "detail": "Match the remedy to the writ.",
                        "options": [
                            {"label": "Free someone illegally detained", "next": "habeas"},
                            {"label": "Compel a public duty", "next": "mandamus"},
                            {"label": "Stop a lower body mid-proceeding", "next": "prohibition"},
                            {"label": "Quash an order already made", "next": "certiorari"},
                            {"label": "Challenge claim to public office", "next": "quo"},
                        ],
                    },
                    {
                        "id": "habeas",
                        "label": "Habeas corpus",
                        "detail": "Produce the person — illegal detention.",
                    },
                    {
                        "id": "mandamus",
                        "label": "Mandamus",
                        "detail": "Command a public authority to perform a duty.",
                    },
                    {
                        "id": "prohibition",
                        "label": "Prohibition",
                        "detail": "Stop a lower court/tribunal from exceeding jurisdiction.",
                    },
                    {
                        "id": "certiorari",
                        "label": "Certiorari",
                        "detail": "Quash an order already made without/excess jurisdiction.",
                    },
                    {
                        "id": "quo",
                        "label": "Quo warranto",
                        "detail": "Challenge someone's claim to a public office.",
                    },
                ],
            },
            {
                "id": "32-vs-226",
                "type": "comparison",
                "title": "Art. 32 vs Art. 226",
                "columns": [
                    {
                        "id": "a32",
                        "heading": "Article 32 (SC)",
                        "points": [
                            "Only for Fundamental Rights",
                            "Itself a FR",
                            "Cannot be suspended except as Constitution provides",
                        ],
                    },
                    {
                        "id": "a226",
                        "heading": "Article 226 (HC)",
                        "points": [
                            "FR + other legal rights",
                            "Wider jurisdiction",
                            "Often first forum in practice",
                        ],
                    },
                ],
            },
            {
                "id": "32-memory-palace",
                "type": "memory_palace",
                "title": "Courtroom memory palace",
                "setting": "Supreme Court courtroom",
                "loci": [
                    {
                        "id": "l1",
                        "place": "Judge's bench",
                        "association": "Article 32",
                        "detail": "Right to move the Supreme Court to enforce FR.",
                    },
                    {
                        "id": "l2",
                        "place": "Ambedkar bust",
                        "association": "Heart and soul",
                        "detail": "Classic Prelims one-liner for Art. 32.",
                    },
                    {
                        "id": "l3",
                        "place": "Writ tray",
                        "association": "Five writs",
                        "detail": "Habeas, mandamus, prohibition, certiorari, quo warranto.",
                    },
                    {
                        "id": "l4",
                        "place": "Side door to High Court",
                        "association": "Article 226",
                        "detail": "Wider jurisdiction — FR plus other legal rights.",
                    },
                ],
            },
        ],
    },
]

STUBS = [
]
EDGES = [
    ("fundamental-rights", "parent", "fr-state-article-12"),
    ("fundamental-rights", "parent", "fr-equality-14-18"),
    ("fundamental-rights", "parent", "fr-right-to-freedom"),
    ("fundamental-rights", "parent", "fr-against-exploitation"),
    ("fundamental-rights", "parent", "fr-freedom-religion"),
    ("fundamental-rights", "parent", "fr-cultural-educational"),
    ("fundamental-rights", "parent", "fr-remedies-32"),
    ("fr-right-to-freedom", "parent", "fr-freedom-19"),
    ("fr-right-to-freedom", "parent", "fr-life-liberty-21"),
    ("fr-equality-14-18", "related", "fr-right-to-freedom"),
    ("fr-freedom-19", "related", "fr-life-liberty-21"),
    ("fr-life-liberty-21", "related", "fr-remedies-32"),
    ("fr-state-article-12", "related", "fr-equality-14-18"),
    ("fr-against-exploitation", "related", "fr-right-to-freedom"),
    ("fr-freedom-religion", "related", "fr-cultural-educational"),
    ("fr-remedies-32", "related", "supreme-court"),
    ("fundamental-rights", "related", "directive-principles"),
]

SAMPLE_PYQS = [
    (
        2018,
        "Which of the following are regarded as the 'heart and soul' of the Indian Constitution according to Dr. B.R. Ambedkar?",
        "Article 32 — Right to Constitutional Remedies.",
        ["fr-remedies-32", "fundamental-rights"],
    ),
    (
        2017,
        "Right to vote and to be elected in India is a:",
        "Often framed as constitutional/legal right distinct from FR — link equality & citizenship themes carefully.",
        ["fr-equality-14-18"],
    ),
    (
        2019,
        "Which of the following are covered under Article 14 of the Constitution?",
        "Equality before law and equal protection of the laws.",
        ["fr-equality-14-18"],
    ),
    (
        2020,
        "Under Article 19, reasonable restrictions on freedom of speech may be imposed on grounds of:",
        "Security of the State, public order, decency/morality, contempt, defamation, and related 19(2) grounds.",
        ["fr-freedom-19", "fr-right-to-freedom"],
    ),
    (
        2015,
        "The freedom under Article 19 is available to:",
        "Citizens of India (not all persons).",
        ["fr-freedom-19", "fr-right-to-freedom"],
    ),
    (
        2016,
        "Article 21 of the Constitution guarantees:",
        "Protection of life and personal liberty — expanded after Maneka Gandhi.",
        ["fr-life-liberty-21", "fr-right-to-freedom"],
    ),
    (
        2021,
        "Which Article abolishes untouchability?",
        "Article 17.",
        ["fr-equality-14-18"],
    ),
    (
        2014,
        "Right against exploitation under the Constitution prohibits:",
        "Traffic in human beings, begar, and related forced labour (Arts 23–24).",
        ["fr-against-exploitation"],
    ),
    (
        2013,
        "Article 25 guarantees freedom of:",
        "Conscience and free profession, practice and propagation of religion — subject to public order, morality, health.",
        ["fr-freedom-religion"],
    ),
    (
        2012,
        "Article 30 relates to:",
        "Right of minorities to establish and administer educational institutions.",
        ["fr-cultural-educational"],
    ),
    (
        2011,
        "Writ jurisdiction of the Supreme Court under Article 32 is for enforcement of:",
        "Fundamental Rights.",
        ["fr-remedies-32"],
    ),
    (
        2009,
        "The 'procedure established by law' under Article 21 was given a broader meaning in:",
        "Maneka Gandhi v. Union of India.",
        ["fr-life-liberty-21", "fr-right-to-freedom"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Maneka Gandhi v. Union of India",
        "slug": "maneka-gandhi",
        "parties": "Maneka Gandhi v. Union of India",
        "year": 1978,
        "court": CaseLaw.Court.SC,
        "summary": "Passport impoundment case that transformed Art. 21 procedure.",
        "holding": (
            "Procedure under Art. 21 must be fair, just, and reasonable; "
            "Arts 14, 19, and 21 are read together (golden triangle)."
        ),
        "concept_slugs": ["fr-life-liberty-21", "fr-right-to-freedom", "fundamental-rights"],
    },
    {
        "title": "Justice K.S. Puttaswamy v. Union of India",
        "slug": "puttaswamy",
        "parties": "Justice K.S. Puttaswamy (Retd.) v. Union of India",
        "year": 2017,
        "court": CaseLaw.Court.SC,
        "summary": "Nine-judge bench on the right to privacy.",
        "holding": "Privacy is a Fundamental Right protected under Art. 21 (and related Part III values).",
        "concept_slugs": ["fr-life-liberty-21", "fundamental-rights"],
    },
    {
        "title": "Olga Tellis v. Bombay Municipal Corporation",
        "slug": "olga-tellis",
        "parties": "Olga Tellis v. Bombay Municipal Corporation",
        "year": 1985,
        "court": CaseLaw.Court.SC,
        "summary": "Pavement dwellers and livelihood as part of life.",
        "holding": "Right to livelihood is an important facet of the right to life under Art. 21.",
        "concept_slugs": ["fr-life-liberty-21"],
    },
    {
        "title": "Vishaka v. State of Rajasthan",
        "slug": "vishaka",
        "parties": "Vishaka v. State of Rajasthan",
        "year": 1997,
        "court": CaseLaw.Court.SC,
        "summary": "Guidelines against sexual harassment at workplace.",
        "holding": "Used Arts 14, 15, 19, and 21 to frame workplace sexual harassment guidelines pending legislation.",
        "concept_slugs": ["fr-equality-14-18", "fr-life-liberty-21", "fr-right-to-freedom"],
    },
    {
        "title": "Navtej Singh Johar v. Union of India",
        "slug": "navtej-johar",
        "parties": "Navtej Singh Johar v. Union of India",
        "year": 2018,
        "court": CaseLaw.Court.SC,
        "summary": "Decriminalisation of consensual same-sex relations (s. 377).",
        "holding": "Sexual orientation protected under equality, dignity, and privacy (Arts 14, 15, 21).",
        "concept_slugs": ["fr-equality-14-18", "fr-life-liberty-21"],
    },
    {
        "title": "Ajay Hasia v. Khalid Mujib",
        "slug": "ajay-hasia",
        "parties": "Ajay Hasia v. Khalid Mujib Sehravardi",
        "year": 1981,
        "court": CaseLaw.Court.SC,
        "summary": "Instrumentality / agency tests for 'other authorities' under Art. 12.",
        "holding": "Bodies that are instrumentalities of the State can fall within Art. 12.",
        "concept_slugs": ["fr-state-article-12", "fundamental-rights"],
    },
    {
        "title": "Indra Sawhney v. Union of India",
        "slug": "indra-sawhney",
        "parties": "Indra Sawhney v. Union of India",
        "year": 1992,
        "court": CaseLaw.Court.SC,
        "summary": "Mandal case on reservations in public employment.",
        "holding": "Key holdings on Art. 16 reservations, creamy layer, and related limits.",
        "concept_slugs": ["fr-equality-14-18"],
    },
]

AMENDMENTS = [
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": (
            "Rolled back Emergency-era changes; Right to Property ceased to be a Fundamental Right "
            "and became a constitutional/legal right under Art. 300A."
        ),
        "effect": "Property moved out of Part III; FR catalogue reshaped for the present Constitution.",
        "concept_slugs": ["fundamental-rights", "fr-right-to-freedom"],
    },
    {
        "number": 1,
        "year": 1951,
        "title": "First Amendment",
        "summary": (
            "Early restrictions on speech (public order, etc.) and validation of land reform measures "
            "affecting property / equality themes."
        ),
        "effect": "Shaped Art. 19(2) grounds and special provisions related to property and equality.",
        "concept_slugs": ["fr-freedom-19", "fr-right-to-freedom", "fundamental-rights"],
    },
]


class Command(BaseCommand):
    help = "Seed Fundamental Rights chapter (Laxmikanth Ch.8 pilot clusters)."

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
                "title": "Fundamental Rights",
                "sort_order": 8,
                "book_ref": "Laxmikanth 8th Ed, Ch. 8",
                "summary": (
                    "Visual revision of Part III — shield mental model, six pillars, "
                    "decision trees, and deep clusters for State, Equality, Freedom, and Remedies."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Fundamental Rights",
                "summary": "Justiciable rights guaranteed under Part III of the Constitution.",
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **shield mental model**, then the **six pillars**. "
                    "Use the decision tree before Prelims drills. "
                    "This is a visual revision layer — not a substitute for Laxmikanth."
                ),
                "visual_blocks": HUB_VISUAL_BLOCKS,
                "chapter": chapter,
                "sort_order": 0,
                "status": Concept.Status.PUBLISHED,
            },
        )

        by_slug = {HUB_SLUG: hub}

        for cluster in [*CLUSTERS, *STUBS]:
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

        # Hub articles
        ConceptArticle.objects.filter(concept=hub).delete()
        ConceptArticle.objects.create(
            concept=hub,
            ref="Part III (Arts 12–35)",
            excerpt="Fundamental Rights — equality, freedom, exploitation, religion, culture, remedies.",
            sort_order=0,
        )

        # FR-related edges: add without wiping the whole subject's edges
        fr_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=fr_slugs, source__subject=subject
        ).filter(
            target__slug__in=fr_slugs
            | {"supreme-court", "directive-principles"}
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
                f"FR chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + len(STUBS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments."
            )
        )
