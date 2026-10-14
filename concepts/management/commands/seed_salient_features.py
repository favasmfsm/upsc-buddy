"""Seed Laxmikanth Ch.4 Salient Features of the Constitution (visual chapter)."""

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

HUB_SLUG = "salient-features-constitution"
CHAPTER_SLUG = "salient-features-constitution"

FEATURE_PILLARS = [
    {
        "id": "lengthiest",
        "articles": "Feature 1",
        "label": "Lengthiest Written Constitution",
        "slug": "sf-lengthiest",
        "detail": "Most detailed written constitution — Parts, Articles, Schedules.",
        "tone": "teal",
    },
    {
        "id": "sources",
        "articles": "Feature 2",
        "label": "Drawn from Various Sources",
        "slug": "sf-sources",
        "detail": "Ransacked world constitutions; GoI Act 1935 is the main material source.",
        "tone": "olive",
    },
    {
        "id": "rigidity",
        "articles": "Feature 3 · Art. 368",
        "label": "Blend of Rigidity & Flexibility",
        "slug": "sf-rigidity-flexibility",
        "detail": "Simple majority, special majority, and special majority + state ratification.",
        "tone": "gold",
    },
    {
        "id": "federal",
        "articles": "Feature 4 · Art. 1",
        "label": "Federal System with Unitary Bias",
        "slug": "sf-federal-unitary",
        "detail": "Union of States — federal form, unitary spirit / quasi-federal.",
        "tone": "orange",
    },
    {
        "id": "parliamentary",
        "articles": "Feature 5",
        "label": "Parliamentary Form of Government",
        "slug": "sf-parliamentary",
        "detail": "Westminster model at Centre and in the states.",
        "tone": "terracotta",
    },
    {
        "id": "sovereignty",
        "articles": "Feature 6 · Art. 21",
        "label": "Parliamentary Sovereignty + Judicial Supremacy",
        "slug": "sf-sovereignty-judiciary",
        "detail": "Synthesis of British and American principles; procedure established by law.",
        "tone": "maroon",
    },
    {
        "id": "judiciary",
        "articles": "Feature 7",
        "label": "Integrated & Independent Judiciary",
        "slug": "sf-integrated-judiciary",
        "detail": "Single hierarchy SC → HC → subordinate courts; enforces Centre and state laws.",
        "tone": "teal",
    },
    {
        "id": "fr",
        "articles": "Feature 8 · Part III",
        "label": "Fundamental Rights",
        "slug": "sf-fundamental-rights",
        "detail": "Six justiciable rights; political democracy; open the FR chapter for depth.",
        "tone": "olive",
    },
    {
        "id": "dpsp",
        "articles": "Feature 9 · Part IV",
        "label": "Directive Principles of State Policy",
        "slug": "sf-dpsp",
        "detail": "Novel feature — social & economic democracy; non-justiciable.",
        "tone": "gold",
    },
    {
        "id": "fd",
        "articles": "Feature 10 · Art. 51A",
        "label": "Fundamental Duties",
        "slug": "sf-fundamental-duties",
        "detail": "Eleven duties (42nd + 86th); reminder alongside rights.",
        "tone": "orange",
    },
    {
        "id": "secular",
        "articles": "Feature 11",
        "label": "A Secular State",
        "slug": "sf-secular",
        "detail": "Positive secularism — equal respect to all religions.",
        "tone": "terracotta",
    },
    {
        "id": "franchise",
        "articles": "Feature 12 · 61st",
        "label": "Universal Adult Franchise",
        "slug": "sf-adult-franchise",
        "detail": "Vote at 18 for Lok Sabha and state assemblies — no literacy/wealth bar.",
        "tone": "maroon",
    },
    {
        "id": "citizenship",
        "articles": "Feature 13",
        "label": "Single Citizenship",
        "slug": "sf-single-citizenship",
        "detail": "One Indian citizenship despite dual polity (unlike USA).",
        "tone": "teal",
    },
    {
        "id": "bodies",
        "articles": "Feature 14",
        "label": "Independent Bodies",
        "slug": "sf-independent-bodies",
        "detail": "EC, CAG, UPSC, SPSC — bulwarks of democratic government.",
        "tone": "olive",
    },
    {
        "id": "emergency",
        "articles": "Feature 15 · 352/356/360",
        "label": "Emergency Provisions",
        "slug": "sf-emergency",
        "detail": "National, state (President’s Rule), and financial — federal → unitary shift.",
        "tone": "gold",
    },
    {
        "id": "three-tier",
        "articles": "Feature 16 · 73rd/74th",
        "label": "Three-tier Government",
        "slug": "sf-three-tier",
        "detail": "Centre, states, and constitutional local governments.",
        "tone": "orange",
    },
    {
        "id": "coops",
        "articles": "Feature 17 · 97th",
        "label": "Co-operative Societies",
        "slug": "sf-cooperative-societies",
        "detail": "Constitutional status — Part IX-B, Art. 19, Art. 43-B.",
        "tone": "terracotta",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "sf-identity-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Identity card",
        "topic_label": "Salient Features",
        "subject_label": "Indian Constitution",
        "relation_label": "Helps you avoid",
        "protects_from": [
            "Confusion with other constitutions",
            "One-line stereotypes",
            "Mixing federal vs unitary labels",
            "Forgetting amendment pathways",
        ],
        "insight": (
            "Salient features are the Constitution’s identity card — "
            "scan the 17 traits first, then drill into each cluster."
        ),
    },
    {
        "id": "sf-seventeen-pillars",
        "type": "pillars",
        "title": "Seventeen salient features",
        "items": FEATURE_PILLARS,
    },
    {
        "id": "sf-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Start from the identity card, then the 17 features. "
            "Add Criticism and Reference Tables after a full feature pass. "
            "42nd Amendment = Mini-Constitution; Kesavananda = basic structure limit."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Lengthiest Written Constitution",
        "slug": "sf-lengthiest",
        "sort_order": 1,
        "summary": "India has the world’s lengthiest written constitution — comprehensive and detailed.",
        "body": (
            "## Lengthiest written constitution\n\n"
            "Constitutions are written (e.g. USA) or unwritten (e.g. Britain). "
            "India’s is the lengthiest written constitution — comprehensive, elaborate, and detailed.\n\n"
            "### Size then and now\n"
            "- **Originally (1949):** Preamble, 395 Articles (22 Parts), 8 Schedules.\n"
            "- **Presently:** Preamble, about 470 Articles (25 Parts), 12 Schedules.\n"
            "- Amendments since 1951 deleted ~20 Articles and Part VII; added ~95 Articles, "
            "Parts IVA, IXA, IXB, XIVA, and Schedules 9–12.\n\n"
            "### Why so large?\n"
            "1. Geographical factors — vastness and diversity.\n"
            "2. Historical factors — bulky GoI Act 1935.\n"
            "3. Single Constitution for Centre and states.\n"
            "4. Dominance of legal luminaries in the Constituent Assembly.\n\n"
            "It includes not only fundamental principles but detailed administrative provisions "
            "often left to ordinary law or convention elsewhere.\n\n"
            "### J&K note\n"
            "Till 2019, J&K had its own constitution under Art. 370. "
            "The 2019 presidential order extended the Constitution of India fully; "
            "the Reorganisation Act created UTs of J&K and Ladakh."
        ),
        "articles": [
            (
                "Preamble + Parts + Schedules",
                "Original: 395 Articles / 22 Parts / 8 Schedules. Present: ~470 Articles / 25 Parts / 12 Schedules.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-size-compare",
                "type": "comparison",
                "title": "Original (1949) vs present Constitution",
                "columns": [
                    {
                        "id": "original",
                        "heading": "Originally (1949)",
                        "points": [
                            "Preamble",
                            "395 Articles in 22 Parts",
                            "8 Schedules",
                        ],
                    },
                    {
                        "id": "present",
                        "heading": "Presently",
                        "points": [
                            "Preamble",
                            "~470 Articles in 25 Parts",
                            "12 Schedules",
                            "~95 Articles / 4 Parts / 4 Schedules added; ~20 Articles + Part VII deleted",
                        ],
                    },
                ],
            },
            {
                "id": "sf-size-factors",
                "type": "pillars",
                "title": "Four factors behind elephantine size",
                "items": [
                    {
                        "id": "geo",
                        "articles": "Factor 1",
                        "label": "Geographical",
                        "slug": "sf-lengthiest",
                        "detail": "Vastness of the country and its diversity.",
                        "tone": "teal",
                    },
                    {
                        "id": "hist",
                        "articles": "Factor 2",
                        "label": "Historical",
                        "slug": "sf-lengthiest",
                        "detail": "Influence of the bulky Government of India Act, 1935.",
                        "tone": "olive",
                    },
                    {
                        "id": "single",
                        "articles": "Factor 3",
                        "label": "Single Constitution",
                        "slug": "sf-lengthiest",
                        "detail": "One document for both the Centre and the states.",
                        "tone": "gold",
                    },
                    {
                        "id": "legal",
                        "articles": "Factor 4",
                        "label": "Legal luminaries",
                        "slug": "sf-lengthiest",
                        "detail": "Dominance of lawyers in the Constituent Assembly.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "sf-size-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Memorise original vs present counts, then the four size factors. "
                    "J&K special status end (2019) is a frequent current-affairs bridge."
                ),
            },
        ],
    },
    {
        "title": "Drawn from Various Sources",
        "slug": "sf-sources",
        "sort_order": 2,
        "summary": "Borrowed widely after ‘ransacking’ world constitutions; GoI Act 1935 is the deepest source.",
        "body": (
            "## Drawn from various sources\n\n"
            "Dr. Ambedkar: framed after ‘ransacking all the known Constitutions of the World’.\n\n"
            "- **Structural part** — largely from the Government of India Act, 1935.\n"
            "- **Philosophical part** — FR (USA) and DPSP (Ireland).\n"
            "- **Political part** — Cabinet government / executive–legislature relations (Britain).\n\n"
            "Also drawn from Canada, Australia, Germany, USSR (Russia), France, South Africa, Japan, etc.\n\n"
            "GoI Act 1935 is the most profound material source: federal scheme, judiciary, governors, "
            "emergency powers, PSCs, and most administrative details — more than half the Constitution "
            "is identical or closely resembles the 1935 Act."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "sf-sources-pillars",
                "type": "pillars",
                "title": "Sources at a glance (Table 4.4)",
                "items": [
                    {
                        "id": "goi1935",
                        "articles": "GoI Act 1935",
                        "label": "Government of India Act, 1935",
                        "slug": "sf-sources",
                        "detail": (
                            "Federal scheme, Governor, Judiciary, PSCs, Emergency, "
                            "advisory jurisdiction of SC, administrative details."
                        ),
                        "tone": "teal",
                    },
                    {
                        "id": "uk",
                        "articles": "Britain",
                        "label": "British Constitution",
                        "slug": "sf-sources",
                        "detail": (
                            "Parliamentary government, Rule of Law, legislative procedure, "
                            "single citizenship, cabinet, writs, privileges, bicameralism."
                        ),
                        "tone": "olive",
                    },
                    {
                        "id": "usa",
                        "articles": "USA",
                        "label": "US Constitution",
                        "slug": "sf-sources",
                        "detail": (
                            "Fundamental rights, independent judiciary, judicial review, "
                            "impeachment, judge removal, Vice-President."
                        ),
                        "tone": "gold",
                    },
                    {
                        "id": "ireland",
                        "articles": "Ireland",
                        "label": "Irish Constitution",
                        "slug": "sf-sources",
                        "detail": "DPSP, Rajya Sabha nominations, method of electing the President.",
                        "tone": "orange",
                    },
                    {
                        "id": "canada",
                        "articles": "Canada",
                        "label": "Canadian Constitution",
                        "slug": "sf-sources",
                        "detail": "Strong Centre, residuary powers with Centre, Centre-appointed state governors.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "australia",
                        "articles": "Australia",
                        "label": "Australian Constitution",
                        "slug": "sf-sources",
                        "detail": "Concurrent List; freedom of trade/commerce/intercourse; joint sitting.",
                        "tone": "maroon",
                    },
                    {
                        "id": "weimar",
                        "articles": "Germany",
                        "label": "Weimar Constitution",
                        "slug": "sf-sources",
                        "detail": "Suspension of Fundamental Rights during Emergency.",
                        "tone": "teal",
                    },
                    {
                        "id": "ussr",
                        "articles": "USSR",
                        "label": "Soviet Constitution",
                        "slug": "sf-sources",
                        "detail": "Fundamental duties; justice (social, economic, political) in the Preamble.",
                        "tone": "olive",
                    },
                    {
                        "id": "france",
                        "articles": "France",
                        "label": "French Constitution",
                        "slug": "sf-sources",
                        "detail": "Republic; liberty, equality, fraternity in the Preamble.",
                        "tone": "gold",
                    },
                    {
                        "id": "sa",
                        "articles": "South Africa",
                        "label": "South African Constitution",
                        "slug": "sf-sources",
                        "detail": "Amendment procedure; election of Rajya Sabha members.",
                        "tone": "orange",
                    },
                    {
                        "id": "japan",
                        "articles": "Japan",
                        "label": "Japanese Constitution",
                        "slug": "sf-sources",
                        "detail": "Procedure established by law.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "sf-sources-layers",
                "type": "callout",
                "tone": "tip",
                "title": "Three layers to remember",
                "body": (
                    "Structural ← GoI Act 1935 · Philosophical ← USA (FR) + Ireland (DPSP) · "
                    "Political ← Britain (Cabinet). Then drill Table 4.4 country-by-country."
                ),
            },
        ],
    },
    {
        "title": "Blend of Rigidity and Flexibility",
        "slug": "sf-rigidity-flexibility",
        "sort_order": 3,
        "summary": "Neither purely rigid nor flexible — three amendment pathways, only some under Art. 368.",
        "body": (
            "## Blend of rigidity and flexibility\n\n"
            "Rigid constitutions need a special amendment procedure (e.g. USA). "
            "Flexible ones amend like ordinary laws (e.g. Britain).\n\n"
            "India is a **synthesis**. Article 368 provides two types:\n"
            "1. Special majority of Parliament (2/3 of members present and voting + majority of total membership of each House).\n"
            "2. Special majority of Parliament **plus** ratification by half of the states.\n\n"
            "Some provisions can also be amended by **simple majority** like ordinary legislation — "
            "these do **not** fall under Article 368."
        ),
        "articles": [
            (
                "Article 368",
                "Power of Parliament to amend the Constitution and procedure therefor — special majority; some need state ratification.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-amend-flow",
                "type": "flowchart",
                "title": "Which amendment path?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What kind of provision?",
                        "detail": "Pick the procedural track before memorising examples.",
                        "options": [
                            {"label": "Ordinary / non-368 provision", "next": "simple"},
                            {"label": "Federal / state-sensitive provision", "next": "ratify"},
                            {"label": "Other constitutional provision under 368", "next": "special"},
                        ],
                    },
                    {
                        "id": "simple",
                        "label": "Simple majority of Parliament",
                        "detail": "Like ordinary law-making — NOT under Article 368.",
                    },
                    {
                        "id": "special",
                        "label": "Special majority (Art. 368)",
                        "detail": "2/3 of members present and voting + majority of total membership of each House.",
                    },
                    {
                        "id": "ratify",
                        "label": "Special majority + state ratification",
                        "detail": "Art. 368 path plus ratification by half of the states.",
                    },
                ],
            },
            {
                "id": "sf-amend-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Simple-majority constitutional changes exist but are outside Art. 368. "
                    "Do not say ‘all amendments need special majority’."
                ),
            },
        ],
    },
    {
        "title": "Federal System with Unitary Bias",
        "slug": "sf-federal-unitary",
        "sort_order": 4,
        "summary": "Federal features with a strong unitary tilt — Union of States, not a compact of states.",
        "body": (
            "## Federal system with unitary bias\n\n"
            "Federal features: two governments, division of powers, written Constitution, supremacy of "
            "Constitution, rigidity, independent judiciary, bicameralism.\n\n"
            "Unitary / non-federal features: strong Centre, single Constitution, single citizenship, "
            "flexibility of Constitution, integrated judiciary, Centre-appointed Governors, All-India Services, "
            "emergency provisions, etc.\n\n"
            "The word ‘Federation’ is unused. **Article 1** calls India a **Union of States** — "
            "(1) not the result of an agreement by the states; (2) no right to secede.\n\n"
            "Labels: ‘federal in form, unitary in spirit’; K.C. Wheare — quasi-federal; Morris Jones — "
            "bargaining federalism; Granville Austin — co-operative federalism; Ivor Jennings — "
            "federation with a centralising tendency.\n\n"
            "Open the **Federal System** chapter for full Ch.14 depth (7 vs 14 features, Canadian model, Bommai)."
        ),
        "articles": [
            (
                "Article 1",
                "India, that is Bharat, shall be a Union of States — not an agreement-based federation; no secession.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-federal-compare",
                "type": "comparison",
                "title": "Federal features vs unitary bias",
                "columns": [
                    {
                        "id": "federal",
                        "heading": "Federal features",
                        "points": [
                            "Two governments",
                            "Division of powers",
                            "Written Constitution",
                            "Supremacy of the Constitution",
                            "Rigidity of the Constitution",
                            "Independent judiciary",
                            "Bicameralism",
                        ],
                    },
                    {
                        "id": "unitary",
                        "heading": "Unitary / non-federal features",
                        "points": [
                            "Strong Centre",
                            "Single Constitution",
                            "Single citizenship",
                            "Flexibility of Constitution",
                            "Integrated judiciary",
                            "Centre appoints state Governors",
                            "All-India Services",
                            "Emergency provisions",
                        ],
                    },
                ],
            },
            {
                "id": "sf-federal-labels",
                "type": "callout",
                "tone": "tip",
                "title": "Scholar labels (memorise)",
                "body": (
                    "K.C. Wheare — quasi-federal · Morris Jones — bargaining federalism · "
                    "Granville Austin — co-operative federalism · Ivor Jennings — federation with a centralising tendency."
                ),
            },
            {
                "id": "sf-federal-depth",
                "type": "callout",
                "tone": "note",
                "title": "Go deeper",
                "body": (
                    "This is the Salient Features overview. Open the **Federal System** chapter "
                    "(Part II, Ch.14) for Union of States, Canadian model, full 7+14 lists, and Bommai."
                ),
            },
        ],
    },
    {
        "title": "Parliamentary Form of Government",
        "slug": "sf-parliamentary",
        "sort_order": 5,
        "summary": "Westminster / Cabinet / responsible government at Centre and in the states.",
        "body": (
            "## Parliamentary form of government\n\n"
            "India chose the British parliamentary system over the American presidential system. "
            "Parliamentary = co-operation/co-ordination of legislature and executive; "
            "presidential = separation of powers.\n\n"
            "Also called Westminster model, responsible government, Cabinet government — "
            "established at Centre and in the states.\n\n"
            "### Features in India\n"
            "1. Nominal and real executives\n"
            "2. Majority party rule\n"
            "3. Collective responsibility of executive to legislature\n"
            "4. Ministers are members of the legislature\n"
            "5. Leadership of PM / CM\n"
            "6. Dissolution of the lower House\n\n"
            "### vs Britain\n"
            "Indian Parliament is **not** sovereign like the British Parliament. "
            "India has an elected republican head; Britain has a hereditary monarch. "
            "PM’s centrality → often called ‘Prime Ministerial Government’."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "sf-parl-compare",
                "type": "comparison",
                "title": "Parliamentary (India) vs Presidential (USA)",
                "columns": [
                    {
                        "id": "parl",
                        "heading": "Parliamentary (India)",
                        "points": [
                            "Co-operation of legislature & executive",
                            "Nominal + real executive",
                            "Collective responsibility to legislature",
                            "Ministers sit in the legislature",
                            "Lower House can be dissolved",
                        ],
                    },
                    {
                        "id": "pres",
                        "heading": "Presidential (USA)",
                        "points": [
                            "Doctrine of separation of powers",
                            "President is real executive",
                            "Executive not responsible to legislature daily",
                            "Ministers generally not legislators",
                            "Fixed executive tenure (no dissolution logic)",
                        ],
                    },
                ],
            },
            {
                "id": "sf-parl-features",
                "type": "pillars",
                "title": "Six features of parliamentary government in India",
                "items": [
                    {
                        "id": "nominal",
                        "articles": "1",
                        "label": "Nominal & real executives",
                        "slug": "sf-parliamentary",
                        "detail": "President/Governor (nominal) and PM/CM with Council of Ministers (real).",
                        "tone": "teal",
                    },
                    {
                        "id": "majority",
                        "articles": "2",
                        "label": "Majority party rule",
                        "slug": "sf-parliamentary",
                        "detail": "Ministry drawn from the majority in the lower House.",
                        "tone": "olive",
                    },
                    {
                        "id": "collective",
                        "articles": "3",
                        "label": "Collective responsibility",
                        "slug": "sf-parliamentary",
                        "detail": "Executive collectively responsible to the legislature.",
                        "tone": "gold",
                    },
                    {
                        "id": "membership",
                        "articles": "4",
                        "label": "Ministerial membership",
                        "slug": "sf-parliamentary",
                        "detail": "Ministers must be (or become) members of the legislature.",
                        "tone": "orange",
                    },
                    {
                        "id": "pm",
                        "articles": "5",
                        "label": "PM / CM leadership",
                        "slug": "sf-parliamentary",
                        "detail": "Prime Minister or Chief Minister leads the real executive.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "dissolve",
                        "articles": "6",
                        "label": "Dissolution of lower House",
                        "slug": "sf-parliamentary",
                        "detail": "Lok Sabha / Assembly can be dissolved.",
                        "tone": "maroon",
                    },
                ],
            },
        ],
    },
    {
        "title": "Parliamentary Sovereignty & Judicial Supremacy",
        "slug": "sf-sovereignty-judiciary",
        "sort_order": 6,
        "summary": "India synthesises British parliamentary sovereignty and American judicial supremacy.",
        "body": (
            "## Synthesis of parliamentary sovereignty and judicial supremacy\n\n"
            "Parliamentary sovereignty ≈ Britain; judicial supremacy ≈ USA.\n\n"
            "Indian judicial review is narrower than in the US because India uses "
            "**‘procedure established by law’** (Art. 21) rather than American **‘due process of law’**.\n\n"
            "Synthesis: SC can strike down parliamentary laws via judicial review; "
            "Parliament can amend most of the Constitution via constituent power "
            "(subject to basic structure — Kesavananda)."
        ),
        "articles": [
            (
                "Article 21",
                "No person shall be deprived of life or personal liberty except according to procedure established by law.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-sov-compare",
                "type": "comparison",
                "title": "UK · USA · India",
                "columns": [
                    {
                        "id": "uk",
                        "heading": "Britain",
                        "points": [
                            "Parliamentary sovereignty",
                            "No written constitution in the US sense",
                            "Courts do not strike down Acts as unconstitutional in the classic sense",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Judicial supremacy",
                            "Due process of law",
                            "Broader judicial review of legislation",
                        ],
                    },
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Synthesis of both principles",
                            "Procedure established by law (Art. 21)",
                            "SC reviews laws; Parliament amends (with basic-structure limit)",
                        ],
                    },
                ],
            },
            {
                "id": "sf-sov-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Due process vs procedure established by law",
                "body": (
                    "USA — due process of law. India — procedure established by law (Art. 21). "
                    "This is why Indian judicial review is classically narrower than the American model."
                ),
            },
        ],
    },
    {
        "title": "Integrated and Independent Judiciary",
        "slug": "sf-integrated-judiciary",
        "sort_order": 7,
        "summary": "One hierarchy from Supreme Court to subordinate courts; independence safeguarded.",
        "body": (
            "## Integrated and independent judiciary\n\n"
            "Supreme Court at the apex → High Courts → subordinate courts (district and below). "
            "This **single system** enforces both central and state laws — unlike the USA’s dual court systems.\n\n"
            "SC is a federal court, highest court of appeal, guarantor of FR, and guardian of the Constitution.\n\n"
            "Independence safeguards include: security of tenure, fixed service conditions, expenses on "
            "Consolidated Fund of India, bar on discussing judges’ conduct in legislatures, ban on practice "
            "after retirement, contempt power, separation of judiciary from executive, etc."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "sf-jud-tree",
                "type": "tree",
                "title": "Integrated judicial hierarchy",
                "root": {
                    "id": "sc",
                    "label": "Supreme Court",
                    "detail": "Apex — federal court, final appeal, FR guarantor, Constitution’s guardian",
                    "children": [
                        {
                            "id": "hc",
                            "label": "High Courts",
                            "detail": "State-level apex under SC",
                            "children": [
                                {
                                    "id": "sub",
                                    "label": "Subordinate courts",
                                    "detail": "District courts and other lower courts — enforce Centre + state laws",
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "id": "sf-jud-tip",
                "type": "callout",
                "tone": "tip",
                "title": "vs USA",
                "body": (
                    "India: one integrated judiciary for Union and state laws. "
                    "USA: federal judiciary for federal laws; state judiciary for state laws."
                ),
            },
        ],
    },
    {
        "title": "Fundamental Rights (overview)",
        "slug": "sf-fundamental-rights",
        "sort_order": 8,
        "summary": "Part III — six justiciable rights for political democracy; deep dive in the FR chapter.",
        "body": (
            "## Fundamental Rights (salient-feature view)\n\n"
            "Six FRs: Equality (14–18), Freedom (19–22), Exploitation (23–24), Religion (25–28), "
            "Cultural & Educational (29–30), Constitutional Remedies (32).\n\n"
            "Originally seven; Right to Property (Art. 31) removed by **44th Amendment (1978)** → "
            "legal right under **Art. 300-A**.\n\n"
            "Justiciable limits on executive tyranny and arbitrary laws; SC writs under Art. 32. "
            "Not absolute (reasonable restrictions); amendable; suspendable in National Emergency "
            "except Arts 20 and 21.\n\n"
            "Open the **Fundamental Rights** chapter for full visual clusters."
        ),
        "articles": [
            (
                "Part III (Arts 12–35)",
                "Fundamental Rights — equality, freedom, exploitation, religion, culture, remedies.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-fr-pillars",
                "type": "pillars",
                "title": "Six Fundamental Rights",
                "items": [
                    {
                        "id": "eq",
                        "articles": "Arts 14–18",
                        "label": "Right to Equality",
                        "slug": "fundamental-rights",
                        "detail": "Equality before law, non-discrimination, untouchability, titles.",
                        "tone": "teal",
                    },
                    {
                        "id": "free",
                        "articles": "Arts 19–22",
                        "label": "Right to Freedom",
                        "slug": "fundamental-rights",
                        "detail": "Six freedoms, conviction safeguards, life & liberty, arrest safeguards.",
                        "tone": "olive",
                    },
                    {
                        "id": "exp",
                        "articles": "Arts 23–24",
                        "label": "Right against Exploitation",
                        "slug": "fundamental-rights",
                        "detail": "Traffic in humans, forced labour, child labour bans.",
                        "tone": "gold",
                    },
                    {
                        "id": "rel",
                        "articles": "Arts 25–28",
                        "label": "Freedom of Religion",
                        "slug": "fundamental-rights",
                        "detail": "Conscience, practice, manage religious affairs — with limits.",
                        "tone": "orange",
                    },
                    {
                        "id": "cul",
                        "articles": "Arts 29–30",
                        "label": "Cultural & Educational",
                        "slug": "fundamental-rights",
                        "detail": "Conserve language/culture; minority educational institutions.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "rem",
                        "articles": "Art. 32",
                        "label": "Constitutional Remedies",
                        "slug": "fundamental-rights",
                        "detail": "Move SC to enforce FR — heart and soul of the Constitution.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "sf-fr-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Go deeper",
                "body": (
                    "This cluster is the Ch.4 overview. For shield model, decision trees, and cases, "
                    "open the Fundamental Rights chapter hub."
                ),
            },
        ],
    },
    {
        "title": "Directive Principles of State Policy",
        "slug": "sf-dpsp",
        "sort_order": 9,
        "summary": "Part IV — novel feature for social & economic democracy; non-justiciable but fundamental in governance.",
        "body": (
            "## Directive Principles of State Policy\n\n"
            "Ambedkar called DPSP a **novel feature**. Part IV; categories — socialistic, Gandhian, "
            "liberal–intellectual.\n\n"
            "Aim: social and economic democracy / welfare state. **Non-justiciable** (unlike FR), "
            "yet ‘fundamental in the governance of the country’ — moral obligation on the State; "
            "real sanction is political (public opinion).\n\n"
            "**Minerva Mills (1980):** Constitution founded on the bedrock of balance between FR and DPSP."
        ),
        "articles": [
            (
                "Part IV (Arts 36–51)",
                "Directive Principles — socialistic, Gandhian, and liberal–intellectual; non-justiciable.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-fr-dpsp",
                "type": "comparison",
                "title": "Fundamental Rights vs Directive Principles",
                "columns": [
                    {
                        "id": "fr",
                        "heading": "Fundamental Rights",
                        "points": [
                            "Part III — justiciable",
                            "Political democracy",
                            "Limits on State tyranny / arbitrary laws",
                            "Courts enforce via writs",
                        ],
                    },
                    {
                        "id": "dpsp",
                        "heading": "Directive Principles",
                        "points": [
                            "Part IV — non-justiciable",
                            "Social & economic democracy",
                            "Welfare-state programmes for the State",
                            "Moral + political sanction (public opinion)",
                        ],
                    },
                ],
            },
            {
                "id": "sf-dpsp-cats",
                "type": "pillars",
                "title": "Three categories of DPSP",
                "items": [
                    {
                        "id": "soc",
                        "articles": "Socialistic",
                        "label": "Socialistic",
                        "slug": "sf-dpsp",
                        "detail": "Social and economic justice; minimise inequalities; welfare orientation.",
                        "tone": "teal",
                    },
                    {
                        "id": "gandhi",
                        "articles": "Gandhian",
                        "label": "Gandhian",
                        "slug": "sf-dpsp",
                        "detail": "Village panchayats, cottage industries, weaker sections, prohibition themes.",
                        "tone": "olive",
                    },
                    {
                        "id": "lib",
                        "articles": "Liberal–intellectual",
                        "label": "Liberal–intellectual",
                        "slug": "sf-dpsp",
                        "detail": "Uniform civil code, separation of judiciary, international peace, etc.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "sf-dpsp-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Case hook",
                "body": "Minerva Mills (1980) — FR–DPSP balance is the bedrock of the Constitution.",
            },
        ],
    },
    {
        "title": "Fundamental Duties",
        "slug": "sf-fundamental-duties",
        "sort_order": 10,
        "summary": "Part IVA · Art. 51A — eleven non-justiciable duties (42nd + 86th Amendments).",
        "body": (
            "## Fundamental Duties\n\n"
            "Absent in the original Constitution. Added during Internal Emergency by the "
            "**42nd Amendment (1976)** on Swaran Singh Committee recommendation. "
            "**86th Amendment (2002)** added one more duty.\n\n"
            "Part IVA — only **Article 51A** — eleven duties (respect Constitution/flag/anthem; "
            "protect sovereignty/unity/integrity; common brotherhood; preserve composite culture; etc.).\n\n"
            "Reminder that rights come with duties to country, society, and fellow citizens. "
            "Like DPSP, **non-justiciable**. "
            "Go deeper → [Fundamental Duties](/concepts/fundamental-duties) chapter."
        ),
        "articles": [
            (
                "Article 51A",
                "Eleven Fundamental Duties of citizens — Part IVA; non-justiciable.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-fd-timeline",
                "type": "timeline",
                "title": "How Fundamental Duties entered the Constitution",
                "events": [
                    {
                        "id": "e1950",
                        "year": 1950,
                        "label": "No duties in original text",
                        "detail": "Original Constitution had no Fundamental Duties chapter.",
                    },
                    {
                        "id": "e1976",
                        "year": 1976,
                        "label": "42nd Amendment",
                        "detail": "Part IVA / Art. 51A added on Swaran Singh Committee advice (Emergency era).",
                    },
                    {
                        "id": "e2002",
                        "year": 2002,
                        "label": "86th Amendment",
                        "detail": "One more Fundamental Duty added — total eleven.",
                    },
                ],
            },
            {
                "id": "sf-fd-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision trio",
                "body": "FR justiciable · DPSP non-justiciable · FD non-justiciable — duties remind citizens alongside rights.",
            },
        ],
    },
    {
        "title": "A Secular State",
        "slug": "sf-secular",
        "sort_order": 11,
        "summary": "No official religion; positive secularism — equal respect to all religions.",
        "body": (
            "## A Secular State\n\n"
            "India does not uphold any religion as the official religion of the State.\n\n"
            "Key hooks: ‘secular’ in Preamble via **42nd Amendment (1976)**; liberty of belief/faith/worship; "
            "Arts 14–16, 25–30, and Art. 44 (UCC endeavour).\n\n"
            "**Western (negative) secularism** = complete church–state separation. "
            "**Indian (positive) secularism** = equal respect / equal protection to all religions "
            "(fits a multi-religious society).\n\n"
            "Communal representation by religion abolished; temporary SC/ST reservation retained for representation."
        ),
        "articles": [
            (
                "Articles 25–28",
                "Freedom of religion cluster — conscience, manage affairs, no tax for religion, no state religious instruction.",
            ),
            (
                "Article 44",
                "State shall endeavour to secure a Uniform Civil Code for citizens.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-sec-compare",
                "type": "comparison",
                "title": "Western vs Indian secularism",
                "columns": [
                    {
                        "id": "west",
                        "heading": "Western (negative)",
                        "points": [
                            "Complete separation of religion and State",
                            "Church vs politics wall",
                            "Less suited to multi-religious India as a sole model",
                        ],
                    },
                    {
                        "id": "india",
                        "heading": "Indian (positive)",
                        "points": [
                            "Equal respect / equal protection to all religions",
                            "No official State religion",
                            "FR + DPSP (UCC) provisions operationalise it",
                        ],
                    },
                ],
            },
            {
                "id": "sf-sec-pillars",
                "type": "pillars",
                "title": "Key secular provisions (scan)",
                "items": [
                    {
                        "id": "preamble",
                        "articles": "42nd",
                        "label": "Secular in Preamble",
                        "slug": "sf-secular",
                        "detail": "Term ‘secular’ added by the 42nd Amendment, 1976.",
                        "tone": "teal",
                    },
                    {
                        "id": "eq",
                        "articles": "Arts 14–16",
                        "label": "Equality & non-discrimination",
                        "slug": "sf-secular",
                        "detail": "Equality before law; no religion-based discrimination; public employment equality.",
                        "tone": "olive",
                    },
                    {
                        "id": "rel",
                        "articles": "Arts 25–28",
                        "label": "Freedom of religion",
                        "slug": "sf-secular",
                        "detail": "Profession, practice, propagation; manage affairs; tax & instruction limits.",
                        "tone": "gold",
                    },
                    {
                        "id": "min",
                        "articles": "Arts 29–30",
                        "label": "Culture & minorities",
                        "slug": "sf-secular",
                        "detail": "Conserve language/culture; minority educational institutions.",
                        "tone": "orange",
                    },
                    {
                        "id": "ucc",
                        "articles": "Art. 44",
                        "label": "Uniform Civil Code",
                        "slug": "sf-secular",
                        "detail": "DPSP — endeavour to secure UCC for all citizens.",
                        "tone": "terracotta",
                    },
                ],
            },
        ],
    },
    {
        "title": "Universal Adult Franchise",
        "slug": "sf-adult-franchise",
        "sort_order": 12,
        "summary": "Vote at 18 for Lok Sabha and assemblies — bold democratic experiment in 1950s India.",
        "body": (
            "## Universal adult franchise\n\n"
            "Basis of elections to Lok Sabha and state legislative assemblies. "
            "Every citizen **not less than 18** may vote without discrimination of caste, race, religion, "
            "sex, literacy, wealth, etc.\n\n"
            "Voting age cut from 21 to 18 by the **61st Amendment Act, 1988** (effective 1989).\n\n"
            "Bold given India’s size, poverty, inequality, and illiteracy at independence — "
            "broadens democracy, equality, minority protection, and hope for weaker sections."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "sf-uaf-timeline",
                "type": "timeline",
                "title": "Voting age evolution",
                "events": [
                    {
                        "id": "e1950",
                        "year": 1950,
                        "label": "Adult franchise from the start",
                        "detail": "Constitution adopts universal adult franchise — originally 21 years.",
                    },
                    {
                        "id": "e1988",
                        "year": 1988,
                        "label": "61st Amendment Act",
                        "detail": "Voting age reduced from 21 to 18 (came into effect 1989).",
                    },
                ],
            },
            {
                "id": "sf-uaf-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook",
                "body": "61st Amendment (1988) — voting age 21 → 18. Applies to Lok Sabha and state assemblies.",
            },
        ],
    },
    {
        "title": "Single Citizenship",
        "slug": "sf-single-citizenship",
        "sort_order": 13,
        "summary": "Dual polity but one citizenship — same civil/political rights across India.",
        "body": (
            "## Single citizenship\n\n"
            "Despite federal dual polity, India provides **only Indian citizenship** "
            "(unlike USA’s national + state citizenship).\n\n"
            "All citizens enjoy the same political and civil rights nationwide regardless of birth/residence state.\n\n"
            "Constitution-makers sought a united nation; communal/caste/linguistic conflicts show "
            "the goal is still a work in progress — but the legal design remains single citizenship."
        ),
        "articles": [
            (
                "Part II (Arts 5–11)",
                "Citizenship provisions — single Indian citizenship despite Centre–state dual polity.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-cit-compare",
                "type": "comparison",
                "title": "India vs USA on citizenship",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Single citizenship (Indian only)",
                            "Same civil & political rights across the country",
                            "Supports national unity in a diverse federation",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Dual citizenship (national + state)",
                            "Allegiance and rights from both levels",
                            "Classic federal citizenship model",
                        ],
                    },
                ],
            },
            {
                "id": "sf-cit-tip",
                "type": "callout",
                "tone": "note",
                "title": "Link to federalism",
                "body": "Single citizenship is also listed among unitary / non-federal features of the Constitution.",
            },
        ],
    },
    {
        "title": "Independent Bodies",
        "slug": "sf-independent-bodies",
        "sort_order": 14,
        "summary": "Constitutional bulwarks beyond legislature, executive, judiciary — EC, CAG, UPSC, SPSC.",
        "body": (
            "## Independent bodies\n\n"
            "Besides legislative, executive, and judicial organs, the Constitution creates independent "
            "bulwarks of democratic government:\n\n"
            "1. **Election Commission** — free and fair elections to Parliament, state legislatures, President, VP.\n"
            "2. **CAG** — audits Centre and states; guardian of the public purse.\n"
            "3. **UPSC** — All-India and higher Central services exams; advises President on discipline.\n"
            "4. **SPSC** — state services exams; advises Governor on discipline.\n\n"
            "Independence via security of tenure, fixed service conditions, expenses charged on the "
            "Consolidated Fund of India, and related safeguards."
        ),
        "articles": [
            (
                "Article 324",
                "Superintendence, direction and control of elections vested in an Election Commission.",
            ),
            (
                "Article 148 / 315",
                "CAG of India; Public Service Commissions for the Union and the states.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-bodies-pillars",
                "type": "pillars",
                "title": "Four independent constitutional bodies",
                "items": [
                    {
                        "id": "ec",
                        "articles": "Art. 324",
                        "label": "Election Commission",
                        "slug": "sf-independent-bodies",
                        "detail": "Free and fair elections to Parliament, state legislatures, President, Vice-President.",
                        "tone": "teal",
                    },
                    {
                        "id": "cag",
                        "articles": "Art. 148",
                        "label": "CAG of India",
                        "slug": "sf-independent-bodies",
                        "detail": "Audits Centre and states; guardian of public purse; legality & propriety of spend.",
                        "tone": "olive",
                    },
                    {
                        "id": "upsc",
                        "articles": "Art. 315",
                        "label": "Union Public Service Commission",
                        "slug": "sf-independent-bodies",
                        "detail": "All-India & higher Central services exams; advises President on discipline.",
                        "tone": "gold",
                    },
                    {
                        "id": "spsc",
                        "articles": "Art. 315",
                        "label": "State Public Service Commissions",
                        "slug": "sf-independent-bodies",
                        "detail": "State services exams; advise the Governor on disciplinary matters.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "sf-bodies-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Independence toolkit",
                "body": (
                    "Security of tenure · fixed service conditions · expenses on Consolidated Fund of India — "
                    "classic Prelims checklist for ‘why independent’."
                ),
            },
        ],
    },
    {
        "title": "Emergency Provisions",
        "slug": "sf-emergency",
        "sort_order": 15,
        "summary": "Three emergencies — national, state (President’s Rule), financial — can convert federal into unitary.",
        "body": (
            "## Emergency provisions\n\n"
            "Elaborate powers for the President to meet extraordinary situations — "
            "safeguard sovereignty, unity, integrity, security, democracy, and the Constitution.\n\n"
            "1. **National Emergency** — war / external aggression / armed rebellion (Art. 352).\n"
            "2. **State Emergency (President’s Rule)** — failure of constitutional machinery (Art. 356) "
            "or failure to comply with Centre’s directions (Art. 365).\n"
            "3. **Financial Emergency** — threat to financial stability or credit of India (Art. 360).\n\n"
            "During emergency the Centre becomes all-powerful; states come under Centre’s control — "
            "federal structure becomes unitary **without formal amendment**. Unique transformation feature."
        ),
        "articles": [
            (
                "Article 352",
                "National Emergency — war, external aggression, or armed rebellion.",
            ),
            (
                "Article 356 / 365",
                "President’s Rule — failure of constitutional machinery or failure to comply with Union directions.",
            ),
            (
                "Article 360",
                "Financial Emergency — threat to financial stability or credit of India.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-emg-flow",
                "type": "flowchart",
                "title": "Which emergency?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What is the crisis?",
                        "detail": "Match the ground to the Article.",
                        "options": [
                            {"label": "War / aggression / armed rebellion", "next": "352"},
                            {"label": "State constitutional machinery fails", "next": "356"},
                            {"label": "State ignores Union directions", "next": "365"},
                            {"label": "Financial stability / credit threatened", "next": "360"},
                        ],
                    },
                    {
                        "id": "352",
                        "label": "Art. 352 — National Emergency",
                        "detail": "War, external aggression, or armed rebellion.",
                    },
                    {
                        "id": "356",
                        "label": "Art. 356 — President’s Rule",
                        "detail": "Failure of constitutional machinery in a state.",
                    },
                    {
                        "id": "365",
                        "label": "Art. 365 → President’s Rule pathway",
                        "detail": "Failure to comply with directions given by the Union.",
                    },
                    {
                        "id": "360",
                        "label": "Art. 360 — Financial Emergency",
                        "detail": "Threat to financial stability or credit of India.",
                    },
                ],
            },
            {
                "id": "sf-emg-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Unique feature",
                "body": (
                    "Emergency can turn the federal system into a unitary one without amending the Constitution — "
                    "a classic ‘salient feature’ line for Mains."
                ),
            },
        ],
    },
    {
        "title": "Three-tier Government",
        "slug": "sf-three-tier",
        "sort_order": 16,
        "summary": "73rd and 74th Amendments added a constitutional third tier — local government.",
        "body": (
            "## Three-tier government\n\n"
            "Originally a dual polity (Centre + states) like other federations. "
            "**73rd and 74th Amendments (1992)** added a third tier of local government — "
            "not found in any other constitution of the world.\n\n"
            "- **73rd** — Part IX + Schedule 11 — Panchayats (village, intermediate, district).\n"
            "- **74th** — Part IX-A + Schedule 12 — Municipalities (nagar panchayat, municipal council, "
            "municipal corporation)."
        ),
        "articles": [
            (
                "Part IX / Schedule 11",
                "Panchayats — three-tier rural local government (73rd Amendment, 1992).",
            ),
            (
                "Part IX-A / Schedule 12",
                "Municipalities — three types of urban local government (74th Amendment, 1992).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-tier-timeline",
                "type": "timeline",
                "title": "From dual polity to three-tier government",
                "events": [
                    {
                        "id": "e1950",
                        "year": 1950,
                        "label": "Dual polity",
                        "detail": "Constitution provides for Centre and states only.",
                    },
                    {
                        "id": "e1992a",
                        "year": 1992,
                        "label": "73rd Amendment",
                        "detail": "Part IX + 11th Schedule — constitutional Panchayats.",
                    },
                    {
                        "id": "e1992b",
                        "year": 1992,
                        "label": "74th Amendment",
                        "detail": "Part IX-A + 12th Schedule — constitutional Municipalities.",
                    },
                ],
            },
            {
                "id": "sf-tier-tree",
                "type": "tree",
                "title": "Three tiers of government",
                "root": {
                    "id": "union",
                    "label": "Union (Centre)",
                    "detail": "First tier",
                    "children": [
                        {
                            "id": "state",
                            "label": "States",
                            "detail": "Second tier",
                            "children": [
                                {
                                    "id": "local",
                                    "label": "Local governments",
                                    "detail": "Third tier — Panchayats (rural) & Municipalities (urban)",
                                }
                            ],
                        }
                    ],
                },
            },
        ],
    },
    {
        "title": "Co-operative Societies",
        "slug": "sf-cooperative-societies",
        "sort_order": 17,
        "summary": "97th Amendment (2011) — constitutional status via FR, DPSP, and Part IX-B.",
        "body": (
            "## Co-operative societies\n\n"
            "**97th Constitutional Amendment Act, 2011** gave constitutional status and protection "
            "to co-operative societies via three changes:\n\n"
            "1. Right to form co-operative societies as a **Fundamental Right** (Art. 19).\n"
            "2. New **DPSP** on promotion of co-operatives (Art. 43-B).\n"
            "3. New **Part IX-B** — The Co-operative Societies (Arts 243-ZH to 243-ZT).\n\n"
            "Part IX-B aims at democratic, professional, autonomous, economically sound co-ops. "
            "Parliament legislates for multi-state co-ops; state legislatures for others."
        ),
        "articles": [
            (
                "Article 19",
                "Right to form co-operative societies made a Fundamental Right (97th Amendment).",
            ),
            (
                "Article 43-B",
                "DPSP — promotion of co-operative societies.",
            ),
            (
                "Part IX-B (Arts 243-ZH to 243-ZT)",
                "Constitutional framework for co-operative societies.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-coop-timeline",
                "type": "timeline",
                "title": "97th Amendment — three constitutional inserts",
                "events": [
                    {
                        "id": "e2011a",
                        "year": 2011,
                        "label": "FR — Art. 19",
                        "detail": "Right to form co-operative societies becomes a Fundamental Right.",
                    },
                    {
                        "id": "e2011b",
                        "year": 2011,
                        "label": "DPSP — Art. 43-B",
                        "detail": "State to promote co-operative societies.",
                    },
                    {
                        "id": "e2011c",
                        "year": 2011,
                        "label": "Part IX-B",
                        "detail": "Arts 243-ZH to 243-ZT — democratic, professional, autonomous co-ops.",
                    },
                ],
            },
            {
                "id": "sf-coop-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims trio",
                "body": "97th = Art. 19 + Art. 43-B + Part IX-B. Remember the three-pronged constitutionalisation.",
            },
        ],
    },
    {
        "title": "Criticism of the Constitution",
        "slug": "sf-criticism",
        "sort_order": 18,
        "summary": "Six classic critiques — and why Ambedkar and others pushed back.",
        "body": (
            "## Criticism of the Constitution\n\n"
            "1. **Borrowed / bag of borrowings** — unfair: framers adapted features to Indian conditions.\n"
            "2. **Carbon copy of 1935 Act** — Ambedkar: no patents on ideas; mostly administrative details borrowed.\n"
            "3. **Un-Indian / anti-Indian** — foreign spirit; ‘English band’ not Veena/Sitar (Hanumanthaiya).\n"
            "4. **Un-Gandhian** — not built primarily on village panchayats as Gandhi envisaged.\n"
            "5. **Elephantine size** — too bulky and complicated (Jennings; Kamath).\n"
            "6. **Paradise of the lawyers** — overly legalistic and litigious (Jennings; Maheswari; Deshmukh).\n\n"
            "Ambedkar’s Constituent Assembly replies are high-yield for Mains critique-and-defence answers."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "sf-crit-pillars",
                "type": "pillars",
                "title": "Six criticisms at a glance",
                "items": [
                    {
                        "id": "borrowed",
                        "articles": "1",
                        "label": "Borrowed Constitution",
                        "slug": "sf-criticism",
                        "detail": "Bag of borrowings / patchwork — Ambedkar: all late constitutions look similar in fundamentals.",
                        "tone": "teal",
                    },
                    {
                        "id": "1935",
                        "articles": "2",
                        "label": "Carbon copy of 1935 Act",
                        "slug": "sf-criticism",
                        "detail": "Jennings / Srinivasan / Deshmukh — Ambedkar: mostly administrative details.",
                        "tone": "olive",
                    },
                    {
                        "id": "unindian",
                        "articles": "3",
                        "label": "Un-Indian / Anti-Indian",
                        "slug": "sf-criticism",
                        "detail": "Foreign spirit unsuitable to India — ‘English band’ critique.",
                        "tone": "gold",
                    },
                    {
                        "id": "gandhi",
                        "articles": "4",
                        "label": "Un-Gandhian",
                        "slug": "sf-criticism",
                        "detail": "Not raised on village/district panchayats as Gandhi wanted.",
                        "tone": "orange",
                    },
                    {
                        "id": "size",
                        "articles": "5",
                        "label": "Elephantine size",
                        "slug": "sf-criticism",
                        "detail": "Too long and complicated — Jennings; elephant emblem joke (Kamath).",
                        "tone": "terracotta",
                    },
                    {
                        "id": "lawyers",
                        "articles": "6",
                        "label": "Paradise of the lawyers",
                        "slug": "sf-criticism",
                        "detail": "Over-legalistic language breeds litigation — ‘lawyer’s paradise’.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "sf-crit-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Answer structure",
                "body": (
                    "State the criticism → give the critic’s line → close with Ambedkar’s defence or a balancing point. "
                    "Do not only memorise the pejorative labels."
                ),
            },
        ],
    },
    {
        "title": "Reference Tables — Parts, Schedules, Sources",
        "slug": "sf-reference-tables",
        "sort_order": 19,
        "summary": "High-yield extracts from Tables 4.1, 4.3, and 4.4 for rapid revision.",
        "body": (
            "## Reference tables (condensed)\n\n"
            "### Parts (selected)\n"
            "- I Union & territory (1–4) · II Citizenship (5–11) · III FR (12–35) · IV DPSP (36–51) · "
            "IVA FD (51A) · IX Panchayats · IXA Municipalities · IXB Co-operatives · "
            "XVIII Emergency · XX Amendment (368).\n\n"
            "### Schedules (memory map)\n"
            "1 States/UTs · 2 Emoluments · 3 Oaths · 4 Rajya Sabha seats · 5 Scheduled areas · "
            "6 Tribal areas (NE) · 7 Union/State/Concurrent Lists · 8 Languages · 9 Land reform shield · "
            "10 Anti-defection · 11 Panchayat subjects · 12 Municipality subjects.\n\n"
            "### Sources\n"
            "See the Sources cluster (Table 4.4) for country-wise borrowings."
        ),
        "articles": [
            (
                "Seventh Schedule",
                "Union List, State List, Concurrent List — division of powers (Art. 246).",
            ),
            (
                "Article 368",
                "Amendment of the Constitution — Part XX.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sf-parts-tree",
                "type": "tree",
                "title": "High-yield Parts map",
                "root": {
                    "id": "const",
                    "label": "Constitution of India",
                    "detail": "Selected Parts for rapid revision",
                    "children": [
                        {
                            "id": "i-ii",
                            "label": "Parts I–II",
                            "detail": "Union & territory (1–4); Citizenship (5–11)",
                        },
                        {
                            "id": "iii-iva",
                            "label": "Parts III–IVA",
                            "detail": "FR (12–35); DPSP (36–51); FD (51A)",
                            "children": [
                                {
                                    "id": "fr",
                                    "label": "Part III FR",
                                    "slug": "fundamental-rights",
                                    "detail": "Justiciable rights",
                                },
                                {
                                    "id": "dpsp",
                                    "label": "Part IV DPSP",
                                    "slug": "sf-dpsp",
                                    "detail": "Non-justiciable directives",
                                },
                            ],
                        },
                        {
                            "id": "ix",
                            "label": "Parts IX / IXA / IXB",
                            "detail": "Panchayats, Municipalities, Co-operatives",
                        },
                        {
                            "id": "emg",
                            "label": "Emergency & Amendment",
                            "detail": "Part XVIII emergencies; Part XX Art. 368",
                        },
                    ],
                },
            },
            {
                "id": "sf-schedules-compare",
                "type": "comparison",
                "title": "Schedules — pair memory",
                "columns": [
                    {
                        "id": "s1",
                        "heading": "Schedules 1–6",
                        "points": [
                            "1 — States & UTs",
                            "2 — Emoluments / allowances",
                            "3 — Oaths & affirmations",
                            "4 — Rajya Sabha seat allocation",
                            "5 — Scheduled areas & tribes",
                            "6 — Tribal areas (Assam, Meghalaya, Tripura, Mizoram)",
                        ],
                    },
                    {
                        "id": "s2",
                        "heading": "Schedules 7–12",
                        "points": [
                            "7 — Union / State / Concurrent Lists",
                            "8 — Languages (22)",
                            "9 — Land reform / validation shield",
                            "10 — Anti-defection",
                            "11 — Panchayat subjects (29)",
                            "12 — Municipality subjects (18)",
                        ],
                    },
                ],
            },
            {
                "id": "sf-ref-tip",
                "type": "callout",
                "tone": "tip",
                "title": "How to use this page",
                "body": (
                    "Scan Parts tree → Schedules pairs → jump to Sources cluster for Table 4.4. "
                    "This is a revision index, not a substitute for full tables in Laxmikanth."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "sf-lengthiest"),
    (HUB_SLUG, "parent", "sf-sources"),
    (HUB_SLUG, "parent", "sf-rigidity-flexibility"),
    (HUB_SLUG, "parent", "sf-federal-unitary"),
    (HUB_SLUG, "parent", "sf-parliamentary"),
    (HUB_SLUG, "parent", "sf-sovereignty-judiciary"),
    (HUB_SLUG, "parent", "sf-integrated-judiciary"),
    (HUB_SLUG, "parent", "sf-fundamental-rights"),
    (HUB_SLUG, "parent", "sf-dpsp"),
    (HUB_SLUG, "parent", "sf-fundamental-duties"),
    (HUB_SLUG, "parent", "sf-secular"),
    (HUB_SLUG, "parent", "sf-adult-franchise"),
    (HUB_SLUG, "parent", "sf-single-citizenship"),
    (HUB_SLUG, "parent", "sf-independent-bodies"),
    (HUB_SLUG, "parent", "sf-emergency"),
    (HUB_SLUG, "parent", "sf-three-tier"),
    (HUB_SLUG, "parent", "sf-cooperative-societies"),
    (HUB_SLUG, "parent", "sf-criticism"),
    (HUB_SLUG, "parent", "sf-reference-tables"),
    ("sf-fundamental-rights", "related", "fundamental-rights"),
    ("sf-dpsp", "related", "sf-fundamental-rights"),
    ("sf-dpsp", "related", "directive-principles"),
    ("sf-fundamental-duties", "related", "sf-dpsp"),
    ("sf-fundamental-duties", "related", "fundamental-duties"),
    ("sf-federal-unitary", "related", "sf-emergency"),
    ("sf-federal-unitary", "related", "sf-single-citizenship"),
    ("sf-federal-unitary", "related", "federal-system"),
    ("sf-sources", "related", "sf-reference-tables"),
    ("sf-rigidity-flexibility", "related", "sf-sovereignty-judiciary"),
    ("sf-three-tier", "related", "sf-cooperative-societies"),
    ("sf-secular", "related", "sf-fundamental-rights"),
    ("sf-integrated-judiciary", "related", "sf-sovereignty-judiciary"),
]

SAMPLE_PYQS = [
    (
        2015,
        "The ideal of 'Welfare State' in the Indian Constitution is enshrined in its:",
        "Directive Principles of State Policy (Part IV).",
        ["sf-dpsp"],
    ),
    (
        2017,
        "Which one of the following statements correctly describes the Fourth Schedule of the Constitution of India?",
        "It allocates seats in the Rajya Sabha to states and union territories.",
        ["sf-reference-tables"],
    ),
    (
        2019,
        "Under which Schedule of the Constitution of India can the transfer of tribal land to private parties for mining be declared null and void?",
        "Often linked to Fifth Schedule protections for scheduled areas (context-dependent).",
        ["sf-reference-tables"],
    ),
    (
        2020,
        "A constitutional government by definition is a:",
        "Limited government — constitution constrains organs (link to written constitution + judicial review themes).",
        ["sf-lengthiest", "sf-sovereignty-judiciary"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Kesavananda Bharati v. State of Kerala",
        "slug": "kesavananda-bharati",
        "parties": "Kesavananda Bharati v. State of Kerala",
        "year": 1973,
        "court": CaseLaw.Court.SC,
        "summary": "Landmark basic-structure ruling limiting constituent power under Art. 368.",
        "holding": (
            "Parliament’s constituent power under Art. 368 does not enable it to alter the "
            "basic structure of the Constitution."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "sf-rigidity-flexibility",
            "sf-sovereignty-judiciary",
        ],
    },
    {
        "title": "Minerva Mills v. Union of India",
        "slug": "minerva-mills",
        "parties": "Minerva Mills Ltd. v. Union of India",
        "year": 1980,
        "court": CaseLaw.Court.SC,
        "summary": "Balance between Fundamental Rights and Directive Principles.",
        "holding": (
            "The Indian Constitution is founded on the bedrock of the balance between "
            "Fundamental Rights and Directive Principles."
        ),
        "concept_slugs": ["sf-dpsp", "sf-fundamental-rights", HUB_SLUG],
    },
]

AMENDMENTS = [
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Often called the Mini-Constitution — large changes including secular/socialist in Preamble "
            "and Fundamental Duties (Part IVA)."
        ),
        "effect": "Reshaped several original features; FD added; secular added to Preamble.",
        "concept_slugs": [
            HUB_SLUG,
            "sf-fundamental-duties",
            "sf-secular",
            "sf-lengthiest",
        ],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": "Rolled back Emergency-era excesses; Right to Property ceased to be a Fundamental Right.",
        "effect": "Property moved to Art. 300-A; FR catalogue reduced to six rights.",
        "concept_slugs": ["sf-fundamental-rights", HUB_SLUG],
    },
    {
        "number": 61,
        "year": 1988,
        "title": "Sixty-first Amendment",
        "summary": "Reduced voting age from 21 to 18 years.",
        "effect": "Universal adult franchise threshold became 18 (effective 1989).",
        "concept_slugs": ["sf-adult-franchise"],
    },
    {
        "number": 73,
        "year": 1992,
        "title": "Seventy-third Amendment",
        "summary": "Constitutional status to Panchayats — Part IX and Eleventh Schedule.",
        "effect": "Created the rural third tier of government.",
        "concept_slugs": ["sf-three-tier", HUB_SLUG],
    },
    {
        "number": 74,
        "year": 1992,
        "title": "Seventy-fourth Amendment",
        "summary": "Constitutional status to Municipalities — Part IX-A and Twelfth Schedule.",
        "effect": "Created the urban third tier of government.",
        "concept_slugs": ["sf-three-tier", HUB_SLUG],
    },
    {
        "number": 97,
        "year": 2011,
        "title": "Ninety-seventh Amendment",
        "summary": "Constitutional status and protection for co-operative societies.",
        "effect": "Art. 19 + Art. 43-B + Part IX-B.",
        "concept_slugs": ["sf-cooperative-societies", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed Salient Features of the Constitution chapter (Laxmikanth Ch.4)."

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
                "title": "Salient Features of the Constitution",
                "sort_order": 4,
                "book_ref": "Laxmikanth 8th Ed, Ch. 4",
                "summary": (
                    "Visual revision of Ch.4 — identity-card mental model, seventeen features, "
                    "criticism, and Parts/Schedules/Sources reference tables."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Salient Features of the Constitution",
                "summary": (
                    "Seventeen traits that distinguish the Indian Constitution — plus criticism "
                    "and revision tables."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **identity-card mental model**, then scan the **seventeen features**. "
                    "Drill dense clusters (sources, federalism, emergency). "
                    "Finish with Criticism and Reference Tables. "
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
            ref="Laxmikanth Ch. 4",
            excerpt="Salient Features of the Constitution — 17 features, criticism, and tables.",
            sort_order=0,
        )

        sf_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=sf_slugs, source__subject=subject
        ).filter(
            target__slug__in=sf_slugs
            | {
                "fundamental-rights",
                "fundamental-duties",
                "directive-principles",
                "federal-system",
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
                # Merge with any existing FR links rather than wiping them.
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
                f"Salient Features chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments."
            )
        )
