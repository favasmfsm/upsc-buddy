"""Seed Laxmikanth Ch.1 Historical Background (visual chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "historical-background"
CHAPTER_SLUG = "historical-background"

ACT_PILLARS = [
    {
        "id": "regulating-1773",
        "articles": "1773",
        "label": "Regulating Act",
        "slug": "hb-regulating-1773",
        "detail": "First parliamentary control of the Company; GG of Bengal; SC at Calcutta.",
        "tone": "teal",
    },
    {
        "id": "amending-1781",
        "articles": "1781",
        "label": "Amending Act (Settlement)",
        "slug": "hb-amending-1781",
        "detail": "Fixed SC jurisdiction clashes with the Governor-General-in-Council.",
        "tone": "olive",
    },
    {
        "id": "pitts-1784",
        "articles": "1784",
        "label": "Pitt’s India Act",
        "slug": "hb-pitts-1784",
        "detail": "Commercial vs political split; Board of Control; dual government.",
        "tone": "gold",
    },
    {
        "id": "charter-1793",
        "articles": "1793",
        "label": "Charter Act 1793",
        "slug": "hb-charter-1793",
        "detail": "Cornwallis override extended; Company monopoly renewed 20 years.",
        "tone": "orange",
    },
    {
        "id": "charter-1813",
        "articles": "1813",
        "label": "Charter Act 1813",
        "slug": "hb-charter-1813",
        "detail": "Trade monopoly ended (tea/China excepted); Crown sovereignty asserted.",
        "tone": "terracotta",
    },
    {
        "id": "charter-1833",
        "articles": "1833",
        "label": "Charter Act 1833",
        "slug": "hb-charter-1833",
        "detail": "GG of India; exclusive central legislation; Company becomes trustee.",
        "tone": "maroon",
    },
    {
        "id": "charter-1853",
        "articles": "1853",
        "label": "Charter Act 1853",
        "slug": "hb-charter-1853",
        "detail": "Separate legislative council; open ICS competition; local representation.",
        "tone": "teal",
    },
    {
        "id": "goi-1858",
        "articles": "1858",
        "label": "GoI Act 1858",
        "slug": "hb-goi-1858",
        "detail": "Crown assumes rule; Viceroy; Secretary of State + India Council.",
        "tone": "olive",
    },
    {
        "id": "councils-1861",
        "articles": "1861",
        "label": "Indian Councils Act 1861",
        "slug": "hb-councils-1861",
        "detail": "Indians nominated; portfolio system; legislative devolution begins.",
        "tone": "gold",
    },
    {
        "id": "councils-1892",
        "articles": "1892",
        "label": "Indian Councils Act 1892",
        "slug": "hb-councils-1892",
        "detail": "Larger councils; budget discussion; indirect election beginnings.",
        "tone": "orange",
    },
    {
        "id": "councils-1909",
        "articles": "1909",
        "label": "Morley–Minto (1909)",
        "slug": "hb-councils-1909",
        "detail": "Separate electorates for Muslims; Indians on executive councils.",
        "tone": "terracotta",
    },
    {
        "id": "goi-1919",
        "articles": "1919",
        "label": "Montagu–Chelmsford (1919)",
        "slug": "hb-goi-1919",
        "detail": "Dyarchy in provinces; bicameral Centre; direct elections.",
        "tone": "maroon",
    },
    {
        "id": "goi-1935",
        "articles": "1935",
        "label": "GoI Act 1935",
        "slug": "hb-goi-1935",
        "detail": "Provincial autonomy; federal scheme (never formed); Federal Court / RBI.",
        "tone": "teal",
    },
    {
        "id": "independence-1947",
        "articles": "1947",
        "label": "Independence Act 1947",
        "slug": "hb-independence-1947",
        "detail": "Two Dominions; end of paramountcy; Mountbatten Plan into statute.",
        "tone": "olive",
    },
    {
        "id": "reference-tables",
        "articles": "Tables",
        "label": "Interim Govt & First Cabinet",
        "slug": "hb-reference-tables",
        "detail": "Table 1.1 (1946) and Table 1.2 (1947) — portfolios at a glance.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "hb-ladder-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Constitutional ladder",
        "topic_label": "Historical Background",
        "subject_label": "British India → Republic",
        "relation_label": "Helps you avoid",
        "protects_from": [
            "Mixing Company Rule with Crown Rule",
            "Confusing GG of Bengal with GG of India",
            "Mixing dyarchy (1919) with provincial autonomy (1935)",
            "Forgetting which federation never came into being",
        ],
        "insight": (
            "Climb Act by Act — Company Rule builds central administration; "
            "Crown Rule builds representation and responsible government."
        ),
    },
    {
        "id": "hb-chapter-timeline",
        "type": "timeline",
        "title": "Company Rule → Crown Rule → Independence",
        "events": [
            {
                "id": "e1773",
                "year": 1773,
                "label": "Regulating Act",
                "detail": "First central administration under GG of Bengal.",
            },
            {
                "id": "e1784",
                "year": 1784,
                "label": "Pitt’s India Act",
                "detail": "Dual government; ‘British possessions in India’.",
            },
            {
                "id": "e1833",
                "year": 1833,
                "label": "Charter Act 1833",
                "detail": "Governor-General of India; exclusive legislation.",
            },
            {
                "id": "e1858",
                "year": 1858,
                "label": "GoI Act 1858",
                "detail": "Crown rule; Viceroy; Secretary of State.",
            },
            {
                "id": "e1909",
                "year": 1909,
                "label": "Morley–Minto",
                "detail": "Separate electorates legalised.",
            },
            {
                "id": "e1919",
                "year": 1919,
                "label": "Montford",
                "detail": "Dyarchy; bicameral Centre; direct elections.",
            },
            {
                "id": "e1935",
                "year": 1935,
                "label": "GoI Act 1935",
                "detail": "Provincial autonomy; federal blueprint (not formed).",
            },
            {
                "id": "e1947",
                "year": 1947,
                "label": "Independence Act",
                "detail": "Two Dominions; British rule ends 15 Aug.",
            },
        ],
    },
    {
        "id": "hb-act-pillars",
        "type": "pillars",
        "title": "Acts & landmarks to open",
        "items": ACT_PILLARS,
    },
    {
        "id": "hb-hub-tip",
        "type": "callout",
        "tone": "tip",
        "title": "Revision tip",
        "body": (
            "Memorise the ladder first (timeline), then drill high-yield Acts: "
            "1773, 1784, 1833, 1858, 1909, 1919, 1935, 1947. "
            "Finish with Interim Government / First Cabinet tables."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Regulating Act of 1773",
        "slug": "hb-regulating-1773",
        "sort_order": 1,
        "summary": (
            "First British parliamentary step to control the East India Company; "
            "laid foundations of central administration in India."
        ),
        "body": (
            "## Regulating Act of 1773\n\n"
            "Constitutional importance: (a) first step by the British Government to control "
            "and regulate Company affairs in India; (b) first recognition of the Company’s "
            "political and administrative functions; (c) foundation of central administration.\n\n"
            "### Features\n"
            "1. Governor of Bengal redesignated **Governor-General of Bengal** with a "
            "four-member Executive Council — first GG: **Lord Warren Hastings**.\n"
            "2. Governors of Bombay and Madras made **subordinate** to the GG of Bengal "
            "(earlier the three presidencies were independent).\n"
            "3. **Supreme Court at Calcutta (1774)** — one Chief Justice + three judges.\n"
            "4. Company servants barred from private trade and from accepting presents/bribes.\n"
            "5. Court of Directors required to report to the British Government on revenue, "
            "civil, and military affairs in India."
        ),
        "articles": [
            (
                "Regulating Act, 1773",
                "First GG of Bengal: Warren Hastings. SC at Calcutta (1774).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1773-pillars",
                "type": "pillars",
                "title": "Why 1773 matters",
                "items": [
                    {
                        "id": "control",
                        "articles": "First",
                        "label": "Parliamentary control",
                        "slug": "hb-regulating-1773",
                        "detail": "Britain begins regulating Company rule in India.",
                        "tone": "teal",
                    },
                    {
                        "id": "political",
                        "articles": "Recognition",
                        "label": "Political functions",
                        "slug": "hb-regulating-1773",
                        "detail": "Company treated as a political/administrative actor.",
                        "tone": "olive",
                    },
                    {
                        "id": "central",
                        "articles": "Foundation",
                        "label": "Central administration",
                        "slug": "hb-regulating-1773",
                        "detail": "GG of Bengal + subordinate presidencies.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "hb-1773-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Warren Hastings = first Governor-General of **Bengal** (1773). "
                    "William Bentinck = first Governor-General of **India** (1833). "
                    "Do not mix the two titles."
                ),
            },
        ],
    },
    {
        "title": "Amending Act of 1781",
        "slug": "hb-amending-1781",
        "sort_order": 2,
        "summary": (
            "Also called the Act of Settlement — fixed jurisdiction clashes between the "
            "Supreme Court and the Governor-General-in-Council."
        ),
        "body": (
            "## Amending Act of 1781 (Act of Settlement)\n\n"
            "Passed to rectify defects of the Regulating Act of 1773.\n\n"
            "### Features\n"
            "1. Exempted the GG and Council (and Company servants) from SC jurisdiction "
            "for **official** acts.\n"
            "2. Excluded **revenue matters** from SC jurisdiction.\n"
            "3. SC jurisdiction over all Calcutta inhabitants; personal law of defendants "
            "(Hindu / Mohammedan law).\n"
            "4. Appeals from Provincial Courts → **Governor-General-in-Council**, not the SC.\n"
            "5. GG-in-Council empowered to frame regulations for Provincial Courts and Councils."
        ),
        "articles": [
            (
                "Amending Act, 1781",
                "Act of Settlement — clarified Supreme Court vs Company executive.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1781-compare",
                "type": "comparison",
                "title": "Before vs after the Act of Settlement",
                "columns": [
                    {
                        "id": "before",
                        "heading": "Problem after 1773",
                        "points": [
                            "SC vs GG-in-Council jurisdiction clashes",
                            "Uncertainty over revenue cases",
                            "Company servants exposed for official acts",
                        ],
                    },
                    {
                        "id": "after",
                        "heading": "1781 fixes",
                        "points": [
                            "Official acts exempt from SC",
                            "Revenue matters out of SC",
                            "Provincial appeals → GG-in-Council",
                        ],
                    },
                ],
            },
            {
                "id": "hb-1781-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": "Link 1781 with ‘Act of Settlement’ and personal law of Calcutta inhabitants.",
            },
        ],
    },
    {
        "title": "Pitt’s India Act of 1784",
        "slug": "hb-pitts-1784",
        "sort_order": 3,
        "summary": (
            "Separated commercial and political functions; created the Board of Control — "
            "system of double government."
        ),
        "body": (
            "## Pitt’s India Act of 1784\n\n"
            "Named after Prime Minister William Pitt.\n\n"
            "### Features\n"
            "1. Distinguished **commercial** and **political** functions of the Company.\n"
            "2. Court of Directors managed commercial affairs; a new **Board of Control** "
            "managed political affairs → **double government**.\n"
            "3. Board of Control could supervise and direct civil/military government and "
            "revenues of British possessions in India.\n\n"
            "### Why it mattered\n"
            "- Company’s territories first called **‘British possessions in India’**.\n"
            "- British Government given **supreme control** over Company affairs in India.\n\n"
            "### Act of 1786 (folded here)\n"
            "Cornwallis accepted GG of Bengal on two conditions, enacted in 1786:\n"
            "1. Power to **override** the council in special cases.\n"
            "2. He would also be **Commander-in-Chief**."
        ),
        "articles": [
            (
                "Pitt’s India Act, 1784",
                "Board of Control + Court of Directors = dual government.",
            ),
            (
                "Act of 1786",
                "Cornwallis: override council + Commander-in-Chief.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1784-dual",
                "type": "comparison",
                "title": "Double government after Pitt’s Act",
                "columns": [
                    {
                        "id": "directors",
                        "heading": "Court of Directors",
                        "points": [
                            "Commercial affairs",
                            "Company’s trading side",
                        ],
                    },
                    {
                        "id": "board",
                        "heading": "Board of Control",
                        "points": [
                            "Political affairs",
                            "Civil & military government / revenues",
                            "British Government supremacy",
                        ],
                    },
                ],
            },
            {
                "id": "hb-1786-callout",
                "type": "callout",
                "tone": "note",
                "title": "Act of 1786",
                "body": (
                    "Cornwallis package: council override in special cases + C-in-C. "
                    "1793 later extended the override to all future GGs and Governors."
                ),
            },
        ],
    },
    {
        "title": "Charter Act of 1793",
        "slug": "hb-charter-1793",
        "sort_order": 4,
        "summary": (
            "Extended Cornwallis’s override powers; renewed Company trade monopoly for "
            "twenty years; Board of Control paid from Indian revenues."
        ),
        "body": (
            "## Charter Act of 1793\n\n"
            "### Features\n"
            "1. Extended Cornwallis’s **override** power over council to all future "
            "Governor-Generals and Presidency Governors.\n"
            "2. Strengthened GG control over Bombay and Madras.\n"
            "3. Extended Company **trade monopoly** in India for another **20 years**.\n"
            "4. Commander-in-Chief not a council member unless so appointed.\n"
            "5. Board of Control members and staff to be paid from **Indian revenues**."
        ),
        "articles": [
            (
                "Charter Act, 1793",
                "Override generalised; monopoly +20 years; Board paid from Indian revenues.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1793-pillars",
                "type": "pillars",
                "title": "1793 at a glance",
                "items": [
                    {
                        "id": "override",
                        "articles": "Power",
                        "label": "Override generalised",
                        "slug": "hb-charter-1793",
                        "detail": "All future GGs and Governors get Cornwallis-style override.",
                        "tone": "teal",
                    },
                    {
                        "id": "monopoly",
                        "articles": "Trade",
                        "label": "Monopoly +20 years",
                        "slug": "hb-charter-1793",
                        "detail": "Company trade monopoly extended.",
                        "tone": "olive",
                    },
                    {
                        "id": "revenues",
                        "articles": "Finance",
                        "label": "Indian revenues",
                        "slug": "hb-charter-1793",
                        "detail": "Board of Control paid from Indian revenues.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "hb-1793-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": "1793 = last major Charter that still **extends** the Company’s trade monopoly.",
            },
        ],
    },
    {
        "title": "Charter Act of 1813",
        "slug": "hb-charter-1813",
        "sort_order": 5,
        "summary": (
            "Ended Company trade monopoly in India (tea and China excepted); asserted "
            "Crown sovereignty; opened the door to missionaries and western education."
        ),
        "body": (
            "## Charter Act of 1813\n\n"
            "### Features\n"
            "1. Abolished Company **trade monopoly** in India — trade open to all British "
            "merchants; monopoly continued only for **tea** and **trade with China**.\n"
            "2. Asserted **sovereignty of the British Crown** over Company territories.\n"
            "3. Allowed Christian **missionaries** to come to India.\n"
            "4. Provided for spread of **western education**.\n"
            "5. Local Governments authorised to impose taxes and punish non-payment."
        ),
        "articles": [
            (
                "Charter Act, 1813",
                "Monopoly ended except tea & China; Crown sovereignty asserted.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1813-compare",
                "type": "comparison",
                "title": "Trade monopoly: what changed in 1813",
                "columns": [
                    {
                        "id": "ended",
                        "heading": "Opened up",
                        "points": [
                            "Indian trade to all British merchants",
                            "Missionaries allowed",
                            "Western education encouraged",
                        ],
                    },
                    {
                        "id": "kept",
                        "heading": "Still with Company",
                        "points": [
                            "Monopoly in tea",
                            "Monopoly in trade with China",
                        ],
                    },
                ],
            },
            {
                "id": "hb-1813-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": "1813 = Crown sovereignty asserted + monopoly ends (tea/China exception).",
            },
        ],
    },
    {
        "title": "Charter Act of 1833",
        "slug": "hb-charter-1833",
        "sort_order": 6,
        "summary": (
            "Final step toward centralisation — Governor-General of India, exclusive "
            "legislation, Company becomes a pure administrative trustee."
        ),
        "body": (
            "## Charter Act of 1833\n\n"
            "Final step towards **centralisation** in British India.\n\n"
            "### Features\n"
            "1. GG of Bengal becomes **Governor-General of India** with all civil and "
            "military powers — first GG of India: **Lord William Bentinck**. "
            "Government of India now covers the entire British territorial area.\n"
            "2. Bombay and Madras Governors lose **legislative** powers; GG of India gets "
            "exclusive legislation. Earlier laws = Regulations; under this Act = **Acts**.\n"
            "3. Company ends as a commercial body → purely **administrative**; territories "
            "held **in trust** for the Crown.\n"
            "4. Attempted **open competition** for civil servants and said Indians should "
            "not be debarred — **negated** after Court of Directors’ opposition."
        ),
        "articles": [
            (
                "Charter Act, 1833",
                "First GG of India: Bentinck. Exclusive central legislation. Company as trustee.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1833-pillars",
                "type": "pillars",
                "title": "1833 centralisation package",
                "items": [
                    {
                        "id": "ggi",
                        "articles": "Title",
                        "label": "GG of India",
                        "slug": "hb-charter-1833",
                        "detail": "Bentinck first Governor-General of India.",
                        "tone": "teal",
                    },
                    {
                        "id": "laws",
                        "articles": "Legislation",
                        "label": "Exclusive Acts",
                        "slug": "hb-charter-1833",
                        "detail": "Central exclusive law-making; Regulations → Acts.",
                        "tone": "olive",
                    },
                    {
                        "id": "trustee",
                        "articles": "Company",
                        "label": "Trustee, not trader",
                        "slug": "hb-charter-1833",
                        "detail": "Commercial role ends; holds India in trust for the Crown.",
                        "tone": "gold",
                    },
                    {
                        "id": "ics",
                        "articles": "ICS",
                        "label": "Open competition (failed)",
                        "slug": "hb-charter-1833",
                        "detail": "Attempt blocked by Court of Directors — realised later in 1853.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "hb-1833-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Open competition for ICS is **attempted** in 1833 but **implemented** "
                    "by the Charter Act of 1853 (Macaulay Committee, 1854)."
                ),
            },
        ],
    },
    {
        "title": "Charter Act of 1853",
        "slug": "hb-charter-1853",
        "sort_order": 7,
        "summary": (
            "Last Charter Act — separate Central Legislative Council, open ICS competition, "
            "and first local representation in the legislature."
        ),
        "body": (
            "## Charter Act of 1853\n\n"
            "Last in the Charter series (1793–1853); major constitutional landmark.\n\n"
            "### Features\n"
            "1. Separated **legislative** and **executive** functions of the GG’s council. "
            "Six legislative councillors added → Indian (Central) Legislative Council — "
            "a mini-Parliament; legislation treated as a special function.\n"
            "2. Introduced **open competition** for covenanted civil service (open to Indians). "
            "Macaulay Committee on the ICS appointed in **1854**.\n"
            "3. Extended Company possession **in trust** for the Crown but **without** "
            "fixing a renewal period — signal that Parliament could end Company rule anytime.\n"
            "4. First **local representation** in the Central Legislative Council — four of "
            "six new members appointed by Madras, Bombay, Bengal, and Agra."
        ),
        "articles": [
            (
                "Charter Act, 1853",
                "Separate legislative council; open ICS; local representation; no fixed term.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1853-pillars",
                "type": "pillars",
                "title": "1853 landmarks",
                "items": [
                    {
                        "id": "leg",
                        "articles": "Council",
                        "label": "Separate legislature",
                        "slug": "hb-charter-1853",
                        "detail": "Legislative wing of GG’s council = mini-Parliament.",
                        "tone": "teal",
                    },
                    {
                        "id": "ics",
                        "articles": "ICS",
                        "label": "Open competition",
                        "slug": "hb-charter-1853",
                        "detail": "Covenanted civil service open; Macaulay Committee 1854.",
                        "tone": "olive",
                    },
                    {
                        "id": "local",
                        "articles": "Representation",
                        "label": "Local members",
                        "slug": "hb-charter-1853",
                        "detail": "Four of six legislative members from provinces.",
                        "tone": "gold",
                    },
                    {
                        "id": "term",
                        "articles": "Charter",
                        "label": "No fixed term",
                        "slug": "hb-charter-1853",
                        "detail": "Company rule could be ended whenever Parliament chose.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "hb-1853-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Bridge to 1858",
                "body": (
                    "No fixed Charter period (1853) foreshadows the end of Company rule "
                    "after 1857 — completed by the GoI Act of 1858."
                ),
            },
        ],
    },
    {
        "title": "Government of India Act of 1858",
        "slug": "hb-goi-1858",
        "sort_order": 8,
        "summary": (
            "Act for the Good Government of India — Company abolished; Crown assumes "
            "direct rule; Viceroy and Secretary of State created."
        ),
        "body": (
            "## Government of India Act of 1858\n\n"
            "Enacted after the Revolt of 1857 (First War of Independence / sepoy mutiny). "
            "Also called the **Act for the Good Government of India**. Abolished the East "
            "India Company; transferred government, territories, and revenues to the Crown.\n\n"
            "### Features\n"
            "1. India governed by and in the name of Her Majesty. GG of India redesignated "
            "**Viceroy of India** — first Viceroy: **Lord Canning**.\n"
            "2. Ended **double government** — abolished Board of Control and Court of Directors.\n"
            "3. Created **Secretary of State for India** with complete authority over Indian "
            "administration; Cabinet member responsible to British Parliament.\n"
            "4. 15-member **Council of India** to advise the Secretary of State (who chaired it).\n"
            "5. Secretary of State-in-Council made a body corporate (can sue / be sued).\n\n"
            "Note: the Act mainly improved **control machinery in England**; it did not "
            "substantially redesign government *inside* India."
        ),
        "articles": [
            (
                "GoI Act, 1858",
                "Crown rule begins. First Viceroy: Canning. Secretary of State + India Council.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1858-compare",
                "type": "comparison",
                "title": "Company Rule ends → Crown Rule begins",
                "columns": [
                    {
                        "id": "before",
                        "heading": "Before 1858",
                        "points": [
                            "East India Company",
                            "Dual government (Directors + Board)",
                            "Governor-General of India",
                        ],
                    },
                    {
                        "id": "after",
                        "heading": "After 1858",
                        "points": [
                            "British Crown",
                            "Secretary of State + Council of India",
                            "Viceroy of India (Canning first)",
                        ],
                    },
                ],
            },
            {
                "id": "hb-1858-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "1858 = end of dual government + first Viceroy (Canning). "
                    "Company Rule (1773–1858) → Crown Rule (1858–1947)."
                ),
            },
        ],
    },
    {
        "title": "Indian Councils Act of 1861",
        "slug": "hb-councils-1861",
        "sort_order": 9,
        "summary": (
            "Beginning of representative institutions — Indians nominated to the Viceroy’s "
            "council; portfolio system; legislative powers restored to Bombay and Madras."
        ),
        "body": (
            "## Indian Councils Act of 1861\n\n"
            "After 1857 the British sought Indian cooperation in administration. Landmark "
            "in association of Indians with law-making.\n\n"
            "### Features\n"
            "1. Viceroy to nominate some Indians as **non-official** members of the expanded "
            "council. In 1862 Canning nominated three Indians (Raja of Benaras, Maharaja of "
            "Patiala, Sir Dinkar Rao).\n"
            "2. Restored **legislative powers** to Bombay and Madras — began decentralisation "
            "(reversing the 1773→1833 centralising trend).\n"
            "3. New legislative councils for Bengal, North-Western Provinces, and Punjab "
            "(1862, 1886, 1897).\n"
            "4. Recognised the **portfolio system** (Canning, 1859) — council members head "
            "departments and issue final orders for them.\n"
            "5. Viceroy can issue **ordinances** in emergency (life: six months) without "
            "legislative council concurrence."
        ),
        "articles": [
            (
                "Indian Councils Act, 1861",
                "Indian nominees; portfolio system; legislative devolution; ordinance power.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1861-pillars",
                "type": "pillars",
                "title": "1861 pillars",
                "items": [
                    {
                        "id": "assoc",
                        "articles": "Representation",
                        "label": "Indian nominees",
                        "slug": "hb-councils-1861",
                        "detail": "Non-official Indians on the Viceroy’s legislative council.",
                        "tone": "teal",
                    },
                    {
                        "id": "devol",
                        "articles": "Devolution",
                        "label": "Bombay & Madras laws",
                        "slug": "hb-councils-1861",
                        "detail": "Legislative powers restored — start of devolution.",
                        "tone": "olive",
                    },
                    {
                        "id": "port",
                        "articles": "Cabinet-like",
                        "label": "Portfolio system",
                        "slug": "hb-councils-1861",
                        "detail": "Departmental charge recognised (from Canning 1859).",
                        "tone": "gold",
                    },
                    {
                        "id": "ord",
                        "articles": "Emergency",
                        "label": "Ordinances",
                        "slug": "hb-councils-1861",
                        "detail": "Viceroy ordinances for six months.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "hb-1861-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Association trilogy",
                "body": "1861 → 1892 → 1909 form the association/representation trilogy after 1857.",
            },
        ],
    },
    {
        "title": "Indian Councils Act of 1892",
        "slug": "hb-councils-1892",
        "sort_order": 10,
        "summary": (
            "Enlarged councils, budget discussion and questions, and limited indirect "
            "election — without using the word ‘election’ in the Act."
        ),
        "body": (
            "## Indian Councils Act of 1892\n\n"
            "### Features\n"
            "1. Increased additional (non-official) members in Central and provincial "
            "legislative councils — **official majority** retained.\n"
            "2. Councils could **discuss the budget** and address **questions** to the executive.\n"
            "3. Some non-official Central members nominated by the Viceroy on recommendation "
            "of provincial councils and Bengal Chamber of Commerce; provincial non-officials "
            "on recommendation of district boards, municipalities, universities, trade "
            "associations, zamindars, chambers.\n\n"
            "Limited and **indirect** provision for filling some non-official seats — the "
            "word **election** was not used; process described as nomination on recommendation."
        ),
        "articles": [
            (
                "Indian Councils Act, 1892",
                "Budget discussion + questions; indirect election without saying ‘election’.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1892-compare",
                "type": "comparison",
                "title": "What 1892 added",
                "columns": [
                    {
                        "id": "powers",
                        "heading": "New council powers",
                        "points": [
                            "Discuss the budget",
                            "Address questions to the executive",
                            "More non-official members",
                        ],
                    },
                    {
                        "id": "limits",
                        "heading": "Still limited",
                        "points": [
                            "Official majority retained",
                            "No word ‘election’ in the Act",
                            "Nomination on recommendation only",
                        ],
                    },
                ],
            },
            {
                "id": "hb-1892-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "1892 begins indirect election practice but does **not** use the word "
                    "‘election’. Direct elections arrive with the 1919 Act."
                ),
            },
        ],
    },
    {
        "title": "Indian Councils Act of 1909",
        "slug": "hb-councils-1909",
        "sort_order": 11,
        "summary": (
            "Morley–Minto Reforms — enlarged councils, Indians on executive councils, and "
            "communal separate electorates for Muslims."
        ),
        "body": (
            "## Indian Councils Act of 1909 (Morley–Minto Reforms)\n\n"
            "Lord Morley = Secretary of State; Lord Minto = Viceroy.\n\n"
            "### Features\n"
            "1. Enlarged Central and provincial legislative councils (Central: 16 → **60**).\n"
            "2. Official majority retained at Centre; **non-official majority** allowed in "
            "provinces.\n"
            "3. Enlarged deliberative functions — supplementary questions, budget resolutions.\n"
            "4. Indians associated with executive councils of Viceroy and Governors — "
            "**Satyendra Prasad Sinha** first Indian on Viceroy’s executive council (Law Member).\n"
            "5. **Separate electorate** for Muslims — Muslim voters elect Muslim members. "
            "Act ‘legalised communalism’; Minto = **Father of Communal Electorate**.\n"
            "6. Separate representation also for presidency corporations, chambers, "
            "universities, zamindars."
        ),
        "articles": [
            (
                "Indian Councils Act, 1909",
                "Morley–Minto. Separate Muslim electorates. S.P. Sinha first Indian Law Member.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1909-pillars",
                "type": "pillars",
                "title": "Morley–Minto headlines",
                "items": [
                    {
                        "id": "size",
                        "articles": "Size",
                        "label": "Larger councils",
                        "slug": "hb-councils-1909",
                        "detail": "Central council members raised from 16 to 60.",
                        "tone": "teal",
                    },
                    {
                        "id": "exec",
                        "articles": "Executive",
                        "label": "Indians in executive",
                        "slug": "hb-councils-1909",
                        "detail": "S.P. Sinha — first Indian Law Member.",
                        "tone": "olive",
                    },
                    {
                        "id": "sep",
                        "articles": "Communal",
                        "label": "Separate electorates",
                        "slug": "hb-councils-1909",
                        "detail": "Muslims elect Muslims — communalism legalised.",
                        "tone": "gold",
                    },
                    {
                        "id": "minto",
                        "articles": "Label",
                        "label": "Father of Communal Electorate",
                        "slug": "hb-councils-1909",
                        "detail": "Lord Minto’s lasting Prelims tag.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "hb-1909-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "1909 introduces separate electorates for **Muslims**. "
                    "1919 extends them to Sikhs, Indian Christians, Anglo-Indians, Europeans."
                ),
            },
        ],
    },
    {
        "title": "Government of India Act of 1919",
        "slug": "hb-goi-1919",
        "sort_order": 12,
        "summary": (
            "Montagu–Chelmsford Reforms — dyarchy in provinces, bicameral Centre, direct "
            "elections, and a path toward responsible government."
        ),
        "body": (
            "## Government of India Act of 1919 (Montagu–Chelmsford Reforms)\n\n"
            "Followed the August 20, 1917 declaration that British policy aimed at gradual "
            "introduction of **responsible government** in India. Came into force in 1921. "
            "Montagu = Secretary of State; Chelmsford = Viceroy.\n\n"
            "### Features (core)\n"
            "1. Subjects split into **central** and **provincial** (Devolution Rules) — "
            "relaxed central control, but structure remained unitary.\n"
            "2. Provincial subjects split into **transferred** (Governor + ministers "
            "responsible to legislature) and **reserved** (Governor + executive council, "
            "not responsible) → **dyarchy** (di-arche = double rule); largely unsuccessful.\n"
            "3. First **bicameralism** and **direct elections** at the Centre "
            "(Council of State + Legislative Assembly).\n"
            "4. Three of six Viceroy’s executive councillors (other than C-in-C) to be Indian.\n"
            "5. Separate electorates extended to Sikhs, Indian Christians, Anglo-Indians, Europeans.\n"
            "6. Limited franchise (property / tax / other qualifications).\n"
            "7. High Commissioner for India in London.\n"
            "8. Public service commission → Central PSC set up in **1926**.\n"
            "9. Provincial budgets separated from Central budget.\n"
            "10. Statutory commission after ten years (→ Simon Commission).\n"
            "11. Chamber of Princes (Narendra Mandal) proposed; inaugurated 1921.\n\n"
            "### Bridge to 1935\n"
            "**Simon Commission** (1927, all-British, boycotted) → Round Table Conferences → "
            "White Paper → Joint Select Committee → GoI Act 1935.\n\n"
            "**Communal Award** (1932) extended separate electorates to depressed classes; "
            "Gandhi’s fast → **Poona Pact** (joint electorate + reserved seats) incorporated "
            "into the 1935 Act."
        ),
        "articles": [
            (
                "GoI Act, 1919",
                "Dyarchy in provinces; bicameral Centre; direct elections; Montford Reforms.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1919-dyarchy",
                "type": "flowchart",
                "title": "Provincial dyarchy — which list?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Provincial subject type?",
                        "detail": "1919 split provincial subjects into two baskets.",
                        "options": [
                            {
                                "label": "Transferred (health, education, LSG, agriculture…)",
                                "next": "transferred",
                            },
                            {
                                "label": "Reserved (police, justice, prisons, land revenue, finance…)",
                                "next": "reserved",
                            },
                        ],
                    },
                    {
                        "id": "transferred",
                        "label": "Transferred subjects",
                        "detail": (
                            "Governor + ministers responsible to the legislative council."
                        ),
                    },
                    {
                        "id": "reserved",
                        "label": "Reserved subjects",
                        "detail": (
                            "Governor + executive council — not responsible to the legislature."
                        ),
                    },
                ],
            },
            {
                "id": "hb-1919-pillars",
                "type": "pillars",
                "title": "Montford firsts",
                "items": [
                    {
                        "id": "dyarchy",
                        "articles": "Provinces",
                        "label": "Dyarchy",
                        "slug": "hb-goi-1919",
                        "detail": "Double rule in provinces — largely unsuccessful.",
                        "tone": "teal",
                    },
                    {
                        "id": "bicam",
                        "articles": "Centre",
                        "label": "Bicameral Centre",
                        "slug": "hb-goi-1919",
                        "detail": "Council of State + Legislative Assembly.",
                        "tone": "olive",
                    },
                    {
                        "id": "direct",
                        "articles": "Elections",
                        "label": "Direct elections",
                        "slug": "hb-goi-1919",
                        "detail": "Majority of both Houses chosen by direct election.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "hb-1919-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Dyarchy is in the **provinces** under 1919. "
                    "1935 **abolishes** provincial dyarchy and places (unused) dyarchy at the Centre."
                ),
            },
        ],
    },
    {
        "title": "Government of India Act of 1935",
        "slug": "hb-goi-1935",
        "sort_order": 13,
        "summary": (
            "Lengthy federal blueprint — provincial autonomy worked; All-India Federation "
            "and central dyarchy never came into operation."
        ),
        "body": (
            "## Government of India Act of 1935\n\n"
            "Second milestone toward responsible government. Lengthy statute: **321 Sections**, "
            "**10 Schedules**. Deep source for many features of the Indian Constitution.\n\n"
            "### Features\n"
            "1. **All-India Federation** of provinces + princely states; three lists "
            "(Federal 59, Provincial 54, Concurrent 36); residuary with Viceroy. "
            "**Federation never came into being** — princely states did not join.\n"
            "2. Abolished provincial dyarchy; introduced **provincial autonomy** and "
            "responsible government in provinces (in effect 1937–1939).\n"
            "3. Provided for **dyarchy at the Centre** (reserved / transferred federal "
            "subjects) — **never operated**.\n"
            "4. Bicameralism in 6 of 11 provinces (Bengal, Bombay, Madras, Bihar, Assam, UP).\n"
            "5. Reserved seats for depressed classes; special representation for women and labour.\n"
            "6. Abolished Council of India (1858); Secretary of State got advisors.\n"
            "7. Franchise ~**14%** of population.\n"
            "8. **Reserve Bank of India**.\n"
            "9. Federal / Provincial / Joint Public Service Commissions.\n"
            "10. **Federal Court** (set up 1937).\n"
            "11. Separated Burma from India.\n"
            "12. New provinces: Orissa and Sind.\n"
            "13. Minority safeguards.\n"
            "14. Federal Railway Authority.\n"
            "15. Auditor-General of India."
        ),
        "articles": [
            (
                "GoI Act, 1935",
                "Provincial autonomy yes; All-India Federation & central dyarchy never operated.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1935-compare",
                "type": "comparison",
                "title": "What worked vs what never operated",
                "columns": [
                    {
                        "id": "worked",
                        "heading": "Came into effect",
                        "points": [
                            "Provincial autonomy (1937–39)",
                            "Responsible govt in provinces",
                            "Federal Court (1937)",
                            "RBI; PSC structure; AG",
                        ],
                    },
                    {
                        "id": "never",
                        "heading": "Never operated",
                        "points": [
                            "All-India Federation (states stayed out)",
                            "Dyarchy at the Centre",
                        ],
                    },
                ],
            },
            {
                "id": "hb-1935-lists",
                "type": "pillars",
                "title": "Three lists (federal scheme)",
                "items": [
                    {
                        "id": "fed",
                        "articles": "59",
                        "label": "Federal List",
                        "slug": "hb-goi-1935",
                        "detail": "Centre subjects.",
                        "tone": "teal",
                    },
                    {
                        "id": "prov",
                        "articles": "54",
                        "label": "Provincial List",
                        "slug": "hb-goi-1935",
                        "detail": "Province subjects.",
                        "tone": "olive",
                    },
                    {
                        "id": "conc",
                        "articles": "36",
                        "label": "Concurrent List",
                        "slug": "hb-goi-1935",
                        "detail": "Both Centre and provinces.",
                        "tone": "gold",
                    },
                    {
                        "id": "res",
                        "articles": "Residuary",
                        "label": "Viceroy",
                        "slug": "hb-goi-1935",
                        "detail": "Residuary powers with the Governor-General.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "hb-1935-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Memorise: federation never formed; provincial autonomy yes; "
                    "central dyarchy never operated; 321 Sections / 10 Schedules."
                ),
            },
        ],
    },
    {
        "title": "Indian Independence Act of 1947",
        "slug": "hb-independence-1947",
        "sort_order": 14,
        "summary": (
            "Ended British rule, created Dominions of India and Pakistan, lapsed paramountcy, "
            "and empowered Constituent Assemblies to frame constitutions."
        ),
        "body": (
            "## Indian Independence Act of 1947\n\n"
            "Atlee (20 Feb 1947) announced end of British rule by 30 June 1948. "
            "Muslim League pressed partition. On **3 June 1947** Mountbatten Plan accepted; "
            "enacted as the Independence Act (Bill 4 July; Royal Assent 18 July; in force "
            "15 August 1947).\n\n"
            "### Features\n"
            "1. Ended British rule; India independent from **15 August 1947**.\n"
            "2. Partition into Dominions of India and Pakistan (right to secede from Commonwealth).\n"
            "3. Abolished office of Viceroy; each Dominion gets a Governor-General appointed "
            "by the King on dominion cabinet advice.\n"
            "4. Constituent Assemblies empowered to frame/adopt any constitution and repeal "
            "British Acts (including this Act).\n"
            "5. Assemblies legislate until new constitutions; post-15 Aug British Acts do not "
            "extend unless adopted.\n"
            "6. Abolished Secretary of State for India → Commonwealth Affairs.\n"
            "7. Lapse of British **paramountcy** over princely states and tribal treaties.\n"
            "8. Princely states free to join India, Pakistan, or remain independent.\n"
            "9. Governance under **GoI Act 1935** (modifiable) until new constitutions.\n"
            "10. British Monarch loses veto/reservation; GG assents in King’s name.\n"
            "11. GG and provincial governors become **constitutional (nominal)** heads.\n"
            "12. Dropped ‘Emperor of India’ from royal titles.\n"
            "13. Ended SoS appointments/reservations in civil services (pre-15 Aug appointees "
            "kept benefits).\n\n"
            "Midnight 14–15 August 1947: power transferred. **Lord Mountbatten** first "
            "GG of Dominion of India; **Jawaharlal Nehru** first PM. 1946 Constituent "
            "Assembly became the Dominion Parliament."
        ),
        "articles": [
            (
                "Indian Independence Act, 1947",
                "Two Dominions; paramountcy lapses; Mountbatten GG; Nehru PM.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-1947-timeline",
                "type": "timeline",
                "title": "Road to 15 August 1947",
                "events": [
                    {
                        "id": "atlee",
                        "year": 1947,
                        "label": "20 Feb — Atlee declaration",
                        "detail": "British rule to end by 30 June 1948.",
                    },
                    {
                        "id": "plan",
                        "year": 1947,
                        "label": "3 June — Mountbatten Plan",
                        "detail": "Partition plan accepted by Congress and League.",
                    },
                    {
                        "id": "act",
                        "year": 1947,
                        "label": "18 July — Royal Assent",
                        "detail": "Independence Act enacted; in force 15 August.",
                    },
                    {
                        "id": "transfer",
                        "year": 1947,
                        "label": "15 Aug — Transfer of power",
                        "detail": "Two Dominions; Mountbatten GG; Nehru PM.",
                    },
                ],
            },
            {
                "id": "hb-1947-pillars",
                "type": "pillars",
                "title": "Independence Act headlines",
                "items": [
                    {
                        "id": "dom",
                        "articles": "Partition",
                        "label": "Two Dominions",
                        "slug": "hb-independence-1947",
                        "detail": "India and Pakistan; Commonwealth exit option.",
                        "tone": "teal",
                    },
                    {
                        "id": "param",
                        "articles": "States",
                        "label": "Paramountcy lapses",
                        "slug": "hb-independence-1947",
                        "detail": "Princes free to join either Dominion or stay independent.",
                        "tone": "olive",
                    },
                    {
                        "id": "ca",
                        "articles": "Constitution",
                        "label": "Assemblies empowered",
                        "slug": "hb-independence-1947",
                        "detail": "Frame constitutions; repeal British Acts including this one.",
                        "tone": "gold",
                    },
                    {
                        "id": "bridge",
                        "articles": "Interim law",
                        "label": "1935 Act continues",
                        "slug": "hb-independence-1947",
                        "detail": "GoI Act 1935 governs until new constitutions (modifiable).",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "hb-1947-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Mountbatten = first GG of Dominion of India; Nehru = first PM. "
                    "Constituent Assembly (1946) becomes Dominion Parliament."
                ),
            },
        ],
    },
    {
        "title": "Reference Tables — Interim Government & First Cabinet",
        "slug": "hb-reference-tables",
        "sort_order": 15,
        "summary": (
            "Table 1.1 Interim Government (1946) and Table 1.2 First Cabinet of Independent "
            "India (1947) — portfolios for quick revision."
        ),
        "body": (
            "## Reference tables\n\n"
            "### Table 1.1 — Interim Government (1946)\n"
            "Members were on the **Viceroy’s Executive Council**. The Viceroy remained head; "
            "**Nehru** was **Vice-President** of the Council.\n\n"
            "| Member | Portfolio |\n"
            "|---|---|\n"
            "| Jawaharlal Nehru | Vice-President; External Affairs & Commonwealth Relations |\n"
            "| Sardar Vallabhbhai Patel | Home; Information & Broadcasting |\n"
            "| Dr. Rajendra Prasad | Food and Agriculture |\n"
            "| Dr. John Mathai | Industries and Supplies |\n"
            "| Jagjivan Ram | Labour |\n"
            "| Sardar Baldev Singh | Defence |\n"
            "| C.H. Bhabha | Works, Mines and Power |\n"
            "| Liaquat Ali Khan | Finance |\n"
            "| Abdur Rab Nishtar | Posts and Air |\n"
            "| Asaf Ali | Railways and Transport |\n"
            "| C. Rajagopalachari | Education and Arts |\n"
            "| I.I. Chundrigar | Commerce |\n"
            "| Ghaznafar Ali Khan | Health |\n"
            "| Jogendra Nath Mandal | Law |\n\n"
            "### Table 1.2 — First Cabinet of Independent India (1947)\n\n"
            "| Member | Portfolio |\n"
            "|---|---|\n"
            "| Jawaharlal Nehru | PM; External Affairs & Commonwealth; Scientific Research |\n"
            "| Sardar Vallabhbhai Patel | Home; I&B; States |\n"
            "| Dr. Rajendra Prasad | Food and Agriculture |\n"
            "| Maulana Abul Kalam Azad | Education |\n"
            "| Dr. John Mathai | Railways and Transport |\n"
            "| R.K. Shanmukham Chetty | Finance |\n"
            "| Dr. B.R. Ambedkar | Law |\n"
            "| Jagjivan Ram | Labour |\n"
            "| Sardar Baldev Singh | Defence |\n"
            "| Rajkumari Amrit Kaur | Health |\n"
            "| C.H. Bhabha | Commerce |\n"
            "| Rafi Ahmed Kidwai | Communication |\n"
            "| Dr. Syama Prasad Mukherjee | Industries and Supplies |\n"
            "| V.N. Gadgil | Works, Mines and Power |"
        ),
        "articles": [
            (
                "Table 1.1 — Interim Government (1946)",
                "Nehru as Vice-President of Viceroy’s Executive Council; mixed Congress–League team.",
            ),
            (
                "Table 1.2 — First Cabinet (1947)",
                "Nehru PM; Patel Home/States; Ambedkar Law; Azad Education.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "hb-tables-compare",
                "type": "comparison",
                "title": "1946 Interim vs 1947 First Cabinet — key shifts",
                "columns": [
                    {
                        "id": "interim",
                        "heading": "Interim Government (1946)",
                        "points": [
                            "Viceroy remains head of Council",
                            "Nehru = Vice-President (not PM)",
                            "Includes League members (e.g. Liaquat — Finance)",
                            "Ambedkar not in this list",
                        ],
                    },
                    {
                        "id": "cabinet",
                        "heading": "First Cabinet (1947)",
                        "points": [
                            "Nehru = Prime Minister",
                            "Patel adds States portfolio",
                            "Ambedkar = Law; Azad = Education",
                            "Dominion cabinet after transfer of power",
                        ],
                    },
                ],
            },
            {
                "id": "hb-tables-pillars",
                "type": "pillars",
                "title": "High-yield names",
                "items": [
                    {
                        "id": "nehru",
                        "articles": "1946→47",
                        "label": "Nehru",
                        "slug": "hb-reference-tables",
                        "detail": "Vice-President (1946) → Prime Minister (1947).",
                        "tone": "teal",
                    },
                    {
                        "id": "patel",
                        "articles": "Home",
                        "label": "Patel",
                        "slug": "hb-reference-tables",
                        "detail": "Home + I&B; adds States in 1947.",
                        "tone": "olive",
                    },
                    {
                        "id": "ambedkar",
                        "articles": "1947",
                        "label": "Ambedkar",
                        "slug": "hb-reference-tables",
                        "detail": "Law Minister in the First Cabinet.",
                        "tone": "gold",
                    },
                    {
                        "id": "liaquat",
                        "articles": "1946",
                        "label": "Liaquat Ali Khan",
                        "slug": "hb-reference-tables",
                        "detail": "Finance in Interim Government (League).",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "hb-tables-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "Do not call Nehru ‘PM’ of the 1946 Interim Government — he was "
                    "Vice-President of the Viceroy’s Executive Council."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "hb-regulating-1773"),
    (HUB_SLUG, "parent", "hb-amending-1781"),
    (HUB_SLUG, "parent", "hb-pitts-1784"),
    (HUB_SLUG, "parent", "hb-charter-1793"),
    (HUB_SLUG, "parent", "hb-charter-1813"),
    (HUB_SLUG, "parent", "hb-charter-1833"),
    (HUB_SLUG, "parent", "hb-charter-1853"),
    (HUB_SLUG, "parent", "hb-goi-1858"),
    (HUB_SLUG, "parent", "hb-councils-1861"),
    (HUB_SLUG, "parent", "hb-councils-1892"),
    (HUB_SLUG, "parent", "hb-councils-1909"),
    (HUB_SLUG, "parent", "hb-goi-1919"),
    (HUB_SLUG, "parent", "hb-goi-1935"),
    (HUB_SLUG, "parent", "hb-independence-1947"),
    (HUB_SLUG, "parent", "hb-reference-tables"),
    ("hb-regulating-1773", "related", "hb-amending-1781"),
    ("hb-amending-1781", "related", "hb-pitts-1784"),
    ("hb-pitts-1784", "related", "hb-charter-1793"),
    ("hb-charter-1793", "related", "hb-charter-1813"),
    ("hb-charter-1813", "related", "hb-charter-1833"),
    ("hb-charter-1833", "related", "hb-charter-1853"),
    ("hb-charter-1853", "related", "hb-goi-1858"),
    ("hb-goi-1858", "related", "hb-councils-1861"),
    ("hb-councils-1861", "related", "hb-councils-1892"),
    ("hb-councils-1892", "related", "hb-councils-1909"),
    ("hb-councils-1909", "related", "hb-goi-1919"),
    ("hb-goi-1919", "related", "hb-goi-1935"),
    ("hb-goi-1935", "related", "hb-independence-1947"),
    ("hb-independence-1947", "related", "hb-reference-tables"),
    ("hb-goi-1935", "related", "salient-features-constitution"),
]

SAMPLE_PYQS = [
    (
        2013,
        (
            "The Government of India Act of 1919 clearly defined:"
        ),
        (
            "The separation of powers of the Centre and the provinces (central vs provincial "
            "subjects under Devolution Rules) — linked to Montford / dyarchy theme."
        ),
        ["hb-goi-1919"],
    ),
    (
        2015,
        (
            "The ‘Instrument of Instructions’ contained in the Government of India Act, 1935 "
            "laid down which of the following?"
        ),
        (
            "Often linked to directions to Governors under the 1935 framework — revise "
            "provincial autonomy and Governor’s special responsibilities with this Act."
        ),
        ["hb-goi-1935"],
    ),
    (
        2017,
        (
            "The Indian Councils Act of 1909 is also known as:"
        ),
        "Morley–Minto Reforms — introduced separate electorates for Muslims.",
        ["hb-councils-1909"],
    ),
    (
        2019,
        (
            "With reference to the British colonial rule in India, consider reforms that "
            "introduced dyarchy in the provinces."
        ),
        "Government of India Act, 1919 (Montagu–Chelmsford Reforms).",
        ["hb-goi-1919"],
    ),
    (
        2021,
        (
            "Which of the following best describes the Government of India Act, 1858?"
        ),
        (
            "Transferred powers from the East India Company to the British Crown; created "
            "Secretary of State and redesignated GG as Viceroy."
        ),
        ["hb-goi-1858"],
    ),
]


class Command(BaseCommand):
    help = "Seed Historical Background chapter (Laxmikanth Ch.1)."

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
                "title": "Historical Background",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 1",
                "summary": (
                    "Visual revision of Ch.1 — constitutional ladder from Company Rule "
                    "(1773–1858) through Crown Rule to the Independence Act, plus cabinet tables."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Historical Background",
                "summary": (
                    "British constitutional landmarks that shaped Indian polity — "
                    "Company Rule, Crown Rule, and Independence."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **constitutional ladder** mental model and the chapter "
                    "**timeline**. Drill Company Rule Acts first (1773–1853), then Crown Rule "
                    "(1858–1947). Finish with Interim Government / First Cabinet tables. "
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
            ref="Laxmikanth Ch. 1",
            excerpt=(
                "Historical Background — Company Rule (1773–1858), Crown Rule (1858–1947), "
                "Independence Act, and cabinet tables."
            ),
            sort_order=0,
        )

        hb_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=hb_slugs, source__subject=subject
        ).filter(
            target__slug__in=hb_slugs | {"salient-features-constitution"}
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
                f"Historical Background chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} sample PYQs."
            )
        )
