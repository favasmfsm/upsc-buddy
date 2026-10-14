"""Seed Laxmikanth Ch.7 Citizenship (visual revision chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "citizenship"
CHAPTER_SLUG = "citizenship"

THEME_PILLARS = [
    {
        "id": "meaning",
        "articles": "Theme 1",
        "label": "Meaning & Significance",
        "slug": "cit-meaning",
        "detail": "Citizens vs aliens; rights only citizens enjoy.",
        "tone": "teal",
    },
    {
        "id": "single",
        "articles": "Theme 2",
        "label": "Single Citizenship",
        "slug": "cit-single",
        "detail": "One Indian citizenship despite dual polity — plus exceptions.",
        "tone": "olive",
    },
    {
        "id": "constitution",
        "articles": "Arts 5–11",
        "label": "Constitutional Provisions",
        "slug": "cit-constitution",
        "detail": "Who became citizens on 26 Jan 1950; Parliament fills the rest.",
        "tone": "gold",
    },
    {
        "id": "acquisition",
        "articles": "Act 1955",
        "label": "Acquisition",
        "slug": "cit-acquisition",
        "detail": "Birth, descent, registration, naturalisation, territory.",
        "tone": "orange",
    },
    {
        "id": "assam",
        "articles": "1985",
        "label": "Assam Accord",
        "slug": "cit-assam",
        "detail": "1966 / 1971 cutoffs and the ten-year wait.",
        "tone": "terracotta",
    },
    {
        "id": "caa",
        "articles": "CAA 2019",
        "label": "CAA 2019",
        "slug": "cit-caa",
        "detail": "Persecuted minorities path; residence cut; Sixth Schedule carve-outs.",
        "tone": "maroon",
    },
    {
        "id": "loss",
        "articles": "Act 1955",
        "label": "Loss of Citizenship",
        "slug": "cit-loss",
        "detail": "Renunciation, termination, deprivation.",
        "tone": "teal",
    },
    {
        "id": "oci",
        "articles": "OCI",
        "label": "OCI / NRI / PIO",
        "slug": "cit-oci",
        "detail": "Overseas card ≠ dual citizenship (Art. 9).",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "cit-membership-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Membership card",
        "topic_label": "Citizenship",
        "subject_label": "Indian State",
        "relation_label": "Gives you",
        "protects_from": [
            "Mixing citizen vs alien rights",
            "USA-style dual citizenship myths",
            "Confusing OCI with dual nationality",
            "Wrong birth / Assam / CAA cutoffs",
        ],
        "insight": (
            "Citizenship is the State’s membership card — Part II names who joined on day one; "
            "the Citizenship Act (1955) rules who joins or leaves after."
        ),
    },
    {
        "id": "cit-theme-pillars",
        "type": "pillars",
        "title": "Eight revision themes",
        "items": THEME_PILLARS,
    },
    {
        "id": "cit-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Scan themes → lock date cutoffs (birth, Assam, CAA) → finish with OCI vs NRI. "
            "This is a visual revision layer — not a substitute for Laxmikanth."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Meaning & Significance",
        "slug": "cit-meaning",
        "sort_order": 1,
        "summary": "Citizens are full members; aliens have fewer rights — especially enemy aliens.",
        "body": (
            "## Meaning and significance\n\n"
            "India has **citizens** and **aliens**. Citizens owe allegiance and enjoy full civil and "
            "political rights. Aliens are citizens of another state.\n\n"
            "- **Friendly aliens** — subjects of countries with cordial relations.\n"
            "- **Enemy aliens** — subjects of a country at war with India; fewer rights "
            "(e.g. no Art. 22 protection against arrest and detention).\n\n"
            "### Citizen-only privileges (denied to aliens)\n"
            "1. Art. 15 — non-discrimination (religion, race, caste, sex, place of birth).\n"
            "2. Art. 16 — equality of opportunity in public employment.\n"
            "3. Art. 19 — six freedoms.\n"
            "4. Arts. 29 & 30 — cultural and educational rights.\n"
            "5. Right to vote for Lok Sabha / state assembly.\n"
            "6. Right to contest Parliament / state legislature.\n"
            "7. Eligibility for certain offices — President, VP, SC/HC judges, Governor, AG, Advocate General.\n\n"
            "Citizens also owe duties (taxes, respect for flag/anthem, defence, etc.).\n\n"
            "**India vs USA:** both birth and naturalised citizens can be President in India; "
            "USA requires natural-born citizen for President."
        ),
        "articles": [
            ("Article 15", "Citizen-only: non-discrimination on religion, race, caste, sex, place of birth."),
            ("Article 16", "Citizen-only: equality of opportunity in public employment."),
            ("Article 19", "Citizen-only: six freedoms."),
            ("Articles 29–30", "Citizen-only: cultural and educational rights."),
            ("Article 22", "Enemy aliens do not enjoy protection against arrest and detention."),
        ],
        "visual_blocks": [
            {
                "id": "cit-citizen-alien",
                "type": "comparison",
                "title": "Citizens vs aliens",
                "columns": [
                    {
                        "id": "citizens",
                        "heading": "Citizens",
                        "points": [
                            "Full members of the Indian State",
                            "Owe allegiance to India",
                            "Full civil & political rights",
                            "Can vote, contest, hold key offices",
                        ],
                    },
                    {
                        "id": "aliens",
                        "heading": "Aliens",
                        "points": [
                            "Citizens of another state",
                            "Friendly or enemy aliens",
                            "Do not enjoy all citizen rights",
                            "Enemy aliens: no Art. 22 arrest protection",
                        ],
                    },
                ],
            },
            {
                "id": "cit-only-rights",
                "type": "pillars",
                "title": "Seven citizen-only privileges",
                "items": [
                    {
                        "id": "a15",
                        "articles": "Art. 15",
                        "label": "Non-discrimination",
                        "slug": "cit-meaning",
                        "detail": "Religion, race, caste, sex, place of birth.",
                        "tone": "teal",
                    },
                    {
                        "id": "a16",
                        "articles": "Art. 16",
                        "label": "Public employment",
                        "slug": "cit-meaning",
                        "detail": "Equality of opportunity.",
                        "tone": "olive",
                    },
                    {
                        "id": "a19",
                        "articles": "Art. 19",
                        "label": "Six freedoms",
                        "slug": "cit-meaning",
                        "detail": "Speech, assembly, association, movement, residence, profession.",
                        "tone": "gold",
                    },
                    {
                        "id": "a2930",
                        "articles": "Arts 29–30",
                        "label": "Culture & education",
                        "slug": "cit-meaning",
                        "detail": "Minority cultural and educational rights.",
                        "tone": "orange",
                    },
                    {
                        "id": "vote",
                        "articles": "Franchise",
                        "label": "Vote",
                        "slug": "cit-meaning",
                        "detail": "Lok Sabha and state assembly elections.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "contest",
                        "articles": "Membership",
                        "label": "Contest elections",
                        "slug": "cit-meaning",
                        "detail": "Parliament and state legislature.",
                        "tone": "maroon",
                    },
                    {
                        "id": "offices",
                        "articles": "Offices",
                        "label": "Key public offices",
                        "slug": "cit-meaning",
                        "detail": "President, VP, judges, Governor, AG, Adv. General.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "cit-meaning-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Enemy aliens lose Art. 22 protection — not all aliens. "
                    "Naturalised citizens can be President in India (unlike USA)."
                ),
            },
        ],
    },
    {
        "title": "Single Citizenship",
        "slug": "cit-single",
        "sort_order": 2,
        "summary": "Dual polity but one Indian citizenship — same rights nationwide, with four exceptions.",
        "body": (
            "## Single citizenship\n\n"
            "Despite a **federal dual polity** (Centre + states), India has **only Indian citizenship**. "
            "No separate state citizenship. Allegiance is to the Union alone.\n\n"
            "USA / Australia use **double citizenship** (national + state), which can enable "
            "state-level discrimination. India avoids that — all citizens enjoy the same political "
            "and civil rights across the country.\n\n"
            "Model is closer to **Canada**. Goal: fraternity and national integration "
            "(still incomplete in social practice).\n\n"
            "### Four exceptions to ‘no discrimination’\n"
            "1. **Art. 16** — Parliament may prescribe residence for certain state/UT posts "
            "(Public Employment Act 1957; now mainly Andhra Pradesh & Telangana).\n"
            "2. **Art. 15** — bars discrimination on place of *birth*, not *residence* — "
            "states may prefer residents for non-constitutional benefits (e.g. fee concessions).\n"
            "3. **Art. 19** — movement/residence restricted to protect Scheduled Tribes.\n"
            "4. **Erstwhile J&K** — permanent-resident privileges via Art. 35-A / 1954 Order; "
            "**abolished 2019** (superseding presidential order)."
        ),
        "articles": [
            ("Article 16", "Residence can be prescribed by Parliament for certain state/UT employments."),
            ("Article 15", "Bars place of birth — not residence — as a discrimination ground."),
            ("Article 19", "Movement/residence subject to Scheduled Tribe interests."),
        ],
        "visual_blocks": [
            {
                "id": "cit-india-usa",
                "type": "comparison",
                "title": "India vs USA on citizenship",
                "columns": [
                    {
                        "id": "india",
                        "heading": "India",
                        "points": [
                            "Single citizenship (Indian only)",
                            "Dual polity (Centre + states)",
                            "Same civil/political rights nationwide",
                            "Like Canada’s model",
                        ],
                    },
                    {
                        "id": "usa",
                        "heading": "USA",
                        "points": [
                            "Dual citizenship (national + state)",
                            "Allegiance to both",
                            "States may favour their own citizens",
                            "Classic federal citizenship model",
                        ],
                    },
                ],
            },
            {
                "id": "cit-single-exceptions",
                "type": "pillars",
                "title": "Four exceptions",
                "items": [
                    {
                        "id": "res-emp",
                        "articles": "Art. 16",
                        "label": "Residence for jobs",
                        "slug": "cit-single",
                        "detail": "Parliament may require residence for certain state/UT posts.",
                        "tone": "teal",
                    },
                    {
                        "id": "res-benefits",
                        "articles": "Art. 15",
                        "label": "Resident benefits",
                        "slug": "cit-single",
                        "detail": "States may prefer residents outside constitutional citizen rights.",
                        "tone": "olive",
                    },
                    {
                        "id": "st",
                        "articles": "Art. 19",
                        "label": "ST areas",
                        "slug": "cit-single",
                        "detail": "Outsiders’ entry/settlement restricted to protect tribes.",
                        "tone": "gold",
                    },
                    {
                        "id": "jk",
                        "articles": "till 2019",
                        "label": "Erstwhile J&K",
                        "slug": "cit-single",
                        "detail": "Art. 35-A permanent residents — abolished in 2019.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "cit-single-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Single citizenship = unitary feature. Link also to Salient Features → "
                    "sf-single-citizenship. J&K special citizenship privileges ended in 2019."
                ),
            },
        ],
    },
    {
        "title": "Constitutional Provisions (Arts 5–11)",
        "slug": "cit-constitution",
        "sort_order": 3,
        "summary": "Part II only names who became citizens on 26 Jan 1950; Art. 11 hands the rest to Parliament.",
        "body": (
            "## Constitutional provisions\n\n"
            "Part II (**Arts 5–11**) is **neither permanent nor elaborate**. It identifies who became "
            "citizens at commencement (**26 Jan 1950**). Later acquisition/loss is left to Parliament.\n\n"
            "### Four commencement categories\n"
            "1. **Art. 5** — domicile in India + born in India / parent born in India / 5 years ordinary residence.\n"
            "2. **Art. 6** — migrants from Pakistan (undivided-India birth link + pre/post **19 Jul 1948** rules).\n"
            "3. **Art. 7** — migrated to Pakistan after **1 Mar 1947**, then returned for resettlement "
            "(6 months residence + registration).\n"
            "4. **Art. 8** — persons of Indian origin abroad registered by diplomatic/consular rep.\n\n"
            "### Other Part II rules\n"
            "- **Art. 9** — voluntary foreign citizenship → not / cease to be Indian citizen.\n"
            "- **Art. 10** — continuance subject to Parliamentary law.\n"
            "- **Art. 11** — Parliament may legislate acquisition, termination, and all citizenship matters "
            "→ **Citizenship Act, 1955**."
        ),
        "articles": [
            ("Article 5", "Citizenship at commencement — domicile + birth/parent/residence conditions."),
            ("Article 6", "Rights of citizenship of certain persons who migrated from Pakistan."),
            ("Article 7", "Rights of citizenship of certain migrants to Pakistan (returnees)."),
            ("Article 8", "Rights of citizenship of certain persons of Indian origin residing outside India."),
            ("Article 9", "Persons voluntarily acquiring foreign citizenship not to be citizens."),
            ("Article 10", "Continuance of the rights of citizenship."),
            ("Article 11", "Parliament to regulate the right of citizenship by law."),
        ],
        "visual_blocks": [
            {
                "id": "cit-part2-tree",
                "type": "tree",
                "title": "Part II — who was a citizen on day one",
                "root": {
                    "id": "part2",
                    "label": "Part II · Arts 5–11",
                    "detail": "Commencement + Parliament’s power",
                    "children": [
                        {
                            "id": "a5",
                            "label": "Art. 5 · Domiciled",
                            "slug": "cit-constitution",
                            "detail": "Born / parent born / 5 yrs resident",
                        },
                        {
                            "id": "a6",
                            "label": "Art. 6 · From Pakistan",
                            "slug": "cit-constitution",
                            "detail": "Cut-off 19 Jul 1948",
                        },
                        {
                            "id": "a7",
                            "label": "Art. 7 · Returnees",
                            "slug": "cit-constitution",
                            "detail": "Left after 1 Mar 1947, then returned",
                        },
                        {
                            "id": "a8",
                            "label": "Art. 8 · Overseas origin",
                            "slug": "cit-constitution",
                            "detail": "Registered abroad",
                        },
                        {
                            "id": "a9-11",
                            "label": "Arts 9–11",
                            "slug": "cit-constitution",
                            "detail": "No dual; continuance; Parliament legislates",
                        },
                    ],
                },
            },
            {
                "id": "cit-art11-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Constitution = who on 26 Jan 1950. Citizenship Act 1955 = who after. "
                    "Art. 11 is the bridge. Art. 9 forbids dual nationality."
                ),
            },
            {
                "id": "cit-july1948-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "19 July 1948 is the Pakistan-migrant registration cut-off — "
                    "not Independence Day and not Republic Day."
                ),
            },
        ],
    },
    {
        "title": "Acquisition of Citizenship",
        "slug": "cit-acquisition",
        "sort_order": 4,
        "summary": "Five modes after 1950 — birth cutoffs are the highest-yield memorisation spine.",
        "body": (
            "## Acquisition (Citizenship Act, 1955)\n\n"
            "Five ways: **birth, descent, registration, naturalisation, incorporation of territory**. "
            "Illegal migrants are barred from registration/naturalisation (subject to CAA carve-outs).\n\n"
            "### By birth (date spine)\n"
            "| Born in India | Rule |\n"
            "|---|---|\n"
            "| 26 Jan 1950 – before 1 Jul 1987 | Citizen by birth (parents’ nationality irrelevant) |\n"
            "| 1 Jul 1987 – before 3 Dec 2004 | Either parent Indian citizen at birth |\n"
            "| On/after 3 Dec 2004 | Both parents citizens, **or** one citizen + other not illegal migrant |\n\n"
            "Children of foreign diplomats / enemy aliens **cannot** get citizenship by birth.\n\n"
            "### By descent (born outside India)\n"
            "- 26 Jan 1950 – before 10 Dec 1992: **father** must be Indian citizen.\n"
            "- On/after 10 Dec 1992: **either parent** Indian citizen.\n"
            "- On/after 3 Dec 2004: consulate registration within 1 year (or CG permission) + no other passport undertaking.\n\n"
            "### Registration / naturalisation / territory\n"
            "- **Registration** — listed categories (PIO resident 7 yrs, spouse of citizen, OCI 5 yrs + 12 months, etc.) + oath.\n"
            "- **Naturalisation** — good character, 8th Schedule language, renunciation of other citizenship, "
            "12 months + 11 of preceding 14 years (CAA shortens aggregate to **5 years** for listed communities).\n"
            "- **Territory** — CG notifies who becomes citizens (e.g. Pondicherry Order 1962).\n\n"
            "Commonwealth citizenship provision was **repealed** by the 2003 amendment."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "cit-five-modes",
                "type": "pillars",
                "title": "Five modes of acquisition",
                "items": [
                    {
                        "id": "birth",
                        "articles": "Birth",
                        "label": "By Birth",
                        "slug": "cit-acquisition",
                        "detail": "Three eras: 1950–87 / 1987–2004 / from 3 Dec 2004.",
                        "tone": "teal",
                    },
                    {
                        "id": "descent",
                        "articles": "Descent",
                        "label": "By Descent",
                        "slug": "cit-acquisition",
                        "detail": "Father-only till 1992; either parent after; register from 2004.",
                        "tone": "olive",
                    },
                    {
                        "id": "reg",
                        "articles": "Registration",
                        "label": "By Registration",
                        "slug": "cit-acquisition",
                        "detail": "PIO, spouse, minors, OCI path — not illegal migrants.",
                        "tone": "gold",
                    },
                    {
                        "id": "nat",
                        "articles": "Naturalisation",
                        "label": "By Naturalisation",
                        "slug": "cit-acquisition",
                        "detail": "Residence + character + 8th Schedule language; CAA shortens.",
                        "tone": "orange",
                    },
                    {
                        "id": "terr",
                        "articles": "Territory",
                        "label": "By Incorporation",
                        "slug": "cit-acquisition",
                        "detail": "CG notifies citizens of new territory (e.g. Pondicherry).",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "cit-birth-timeline",
                "type": "timeline",
                "title": "Citizenship by birth — cutoffs",
                "events": [
                    {
                        "id": "b1",
                        "year": 1950,
                        "label": "From 26 Jan 1950",
                        "detail": "Born in India → citizen by birth (till before 1 Jul 1987).",
                    },
                    {
                        "id": "b2",
                        "year": 1987,
                        "label": "From 1 Jul 1987",
                        "detail": "Either parent must be Indian citizen at birth.",
                    },
                    {
                        "id": "b3",
                        "year": 2004,
                        "label": "From 3 Dec 2004",
                        "detail": "Both parents citizens, or one citizen + other not illegal migrant.",
                    },
                ],
            },
            {
                "id": "cit-acq-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Memorise 26 Jan 1950 / 1 Jul 1987 / 3 Dec 2004 for birth, and 10 Dec 1992 for descent. "
                    "Diplomat/enemy-alien children: no citizenship by birth."
                ),
            },
        ],
    },
    {
        "title": "Assam Accord Provisions",
        "slug": "cit-assam",
        "sort_order": 5,
        "summary": "1985 amendment — 1 Jan 1966 and 25 Mar 1971 cutoffs; middle cohort waits 10 years to vote.",
        "body": (
            "## Assam Accord (Citizenship Amendment Act, 1985)\n\n"
            "Special rules for persons of Indian origin who came to Assam from Bangladesh:\n\n"
            "1. **Before 1 Jan 1966** — ordinarily resident since entry → deemed citizens **from 1 Jan 1966**.\n"
            "2. **1 Jan 1966 to before 25 Mar 1971** — detected as foreigner → must register; "
            "deemed citizen for all purposes after **10 years from detection**, but in the interval "
            "has citizen-like rights **except the right to vote**.\n\n"
            "These cutoffs are Prelims favourites — do not confuse with CAA’s 31 Dec 2014 date."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "cit-assam-timeline",
                "type": "timeline",
                "title": "Assam Accord cutoffs",
                "events": [
                    {
                        "id": "a1",
                        "year": 1966,
                        "label": "Before 1 Jan 1966",
                        "detail": "Deemed citizen from 1 Jan 1966 if ordinarily resident since entry.",
                    },
                    {
                        "id": "a2",
                        "year": 1971,
                        "label": "1 Jan 1966 – before 25 Mar 1971",
                        "detail": "Register as foreigner; citizen after 10 years from detection.",
                    },
                    {
                        "id": "a3",
                        "year": 1985,
                        "label": "Amendment Act 1985",
                        "detail": "Wrote Assam Accord citizenship rules into the Citizenship Act.",
                    },
                ],
            },
            {
                "id": "cit-assam-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "1966–1971 cohort: during the 10-year wait they lack **voting rights** only — "
                    "not all citizenship rights. Do not mix with CAA 31 Dec 2014."
                ),
            },
            {
                "id": "cit-assam-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": "Pair dates: Assam 1 Jan 1966 + 25 Mar 1971 · CAA entry on/before 31 Dec 2014.",
            },
        ],
    },
    {
        "title": "CAA 2019",
        "slug": "cit-caa",
        "sort_order": 6,
        "summary": "Path for Hindu/Sikh/Buddhist/Jain/Parsi/Christian migrants from AFG/BD/PK entered by 31 Dec 2014.",
        "body": (
            "## Citizenship (Amendment) Act, 2019\n\n"
            "Applies to migrants from **Hindu, Sikh, Buddhist, Jain, Parsi or Christian** communities "
            "from **Afghanistan, Bangladesh or Pakistan** who entered India **on or before 31 Dec 2014** "
            "and were exempted from Passport (Entry) Act / Foreigners Act penalties.\n\n"
            "### What it does\n"
            "- Makes them eligible for **registration or naturalisation** (earlier treated as illegal migrants).\n"
            "- Citizenship deemed from **date of entry** into India.\n"
            "- Pending illegal-migration / citizenship proceedings **abate** on conferment.\n"
            "- Naturalisation residence aggregate cut from **11 of 14 years → 5 years** for these persons.\n"
            "- Came into force **10 Jan 2020**.\n\n"
            "### Background steps\n"
            "2015 exemption from penal consequences → 2016 long-term visa eligibility → 2019 Act.\n\n"
            "### Not applicable to\n"
            "- Sixth Schedule tribal areas of Assam, Meghalaya, Mizoram, Tripura.\n"
            "- Inner Line areas under Bengal Eastern Frontier Regulation, 1873."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "cit-caa-compare",
                "type": "comparison",
                "title": "Before vs after CAA 2019",
                "columns": [
                    {
                        "id": "before",
                        "heading": "Before CAA",
                        "points": [
                            "Listed migrants without valid docs = illegal migrants",
                            "Ineligible for registration / naturalisation",
                            "Standard 11-of-14 years naturalisation residence",
                        ],
                    },
                    {
                        "id": "after",
                        "heading": "After CAA",
                        "points": [
                            "Eligible if entered by 31 Dec 2014 + exempted",
                            "Registration / naturalisation path opens",
                            "Aggregate residence cut to 5 years for them",
                            "Citizenship deemed from date of entry",
                        ],
                    },
                ],
            },
            {
                "id": "cit-caa-timeline",
                "type": "timeline",
                "title": "CAA path",
                "events": [
                    {
                        "id": "c1",
                        "year": 2015,
                        "label": "Exemption",
                        "detail": "Exempted from Passport Entry / Foreigners Act penalties.",
                    },
                    {
                        "id": "c2",
                        "year": 2016,
                        "label": "Long-term visa",
                        "detail": "Made eligible for long-term stay in India.",
                    },
                    {
                        "id": "c3",
                        "year": 2019,
                        "label": "CAA enacted",
                        "detail": "Citizenship path; in force 10 Jan 2020.",
                    },
                ],
            },
            {
                "id": "cit-caa-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Communities: 6 religions · Countries: AFG, BD, PK · Cutoff: 31 Dec 2014. "
                    "Does **not** apply in Sixth Schedule areas or Inner Line notified areas."
                ),
            },
        ],
    },
    {
        "title": "Loss of Citizenship",
        "slug": "cit-loss",
        "sort_order": 7,
        "summary": "Three ways out — renunciation, termination, deprivation — with war-time pauses.",
        "body": (
            "## Loss of citizenship\n\n"
            "Citizenship Act provides three modes (whether acquired under the Act or under the Constitution):\n\n"
            "### 1. Renunciation\n"
            "Full age & capacity → declaration → ceases on registration. "
            "If made during a war involving India, registration is **withheld**. "
            "Minor children also lose citizenship; may **resume within one year of turning 18**.\n\n"
            "### 2. Termination\n"
            "Voluntarily acquiring another country’s citizenship → Indian citizenship "
            "**automatically terminates** (conscious, knowing, without duress). "
            "**Does not apply during a war** in which India is engaged.\n\n"
            "### 3. Deprivation (compulsory by Central Government)\n"
            "1. Citizenship obtained by fraud.\n"
            "2. Disloyalty to the Constitution.\n"
            "3. Unlawful trade/communication with the enemy during war.\n"
            "4. Within 5 years of registration/naturalisation, imprisoned 2 years in any country.\n"
            "5. Ordinarily resident outside India continuously for **7 years** (with stated exceptions)."
        ),
        "articles": [
            ("Article 9", "Voluntarily acquiring foreign citizenship — constitutional bar / cease."),
        ],
        "visual_blocks": [
            {
                "id": "cit-loss-pillars",
                "type": "pillars",
                "title": "Three ways to lose citizenship",
                "items": [
                    {
                        "id": "renounce",
                        "articles": "Voluntary",
                        "label": "Renunciation",
                        "slug": "cit-loss",
                        "detail": "Declaration by adult; withheld in wartime; minors may resume at 18.",
                        "tone": "teal",
                    },
                    {
                        "id": "terminate",
                        "articles": "Automatic",
                        "label": "Termination",
                        "slug": "cit-loss",
                        "detail": "Voluntary foreign citizenship ends Indian citizenship — paused in war.",
                        "tone": "olive",
                    },
                    {
                        "id": "deprive",
                        "articles": "Compulsory",
                        "label": "Deprivation",
                        "slug": "cit-loss",
                        "detail": "Fraud, disloyalty, enemy trade, jail, 7-year absence abroad.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "cit-loss-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Termination is automatic on voluntary foreign citizenship — but **not during war**. "
                    "Renunciation registration is also withheld in wartime. Do not conflate the two."
                ),
            },
            {
                "id": "cit-loss-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": "Deprivation grounds: fraud · disloyalty · enemy dealing · 2-yr jail within 5 yrs · 7 yrs abroad.",
            },
        ],
    },
    {
        "title": "OCI, NRI & PIO",
        "slug": "cit-oci",
        "sort_order": 8,
        "summary": "OCI card is not dual citizenship — Art. 9 forbids dual nationality.",
        "body": (
            "## Overseas Citizenship of India\n\n"
            "L.M. Singhvi Committee (2002) recommended diaspora dual citizenship. "
            "Parliament created **OCI** (2003; expanded 2005) — **not actual dual citizenship**. "
            "Art. 9 forbids dual nationality.\n\n"
            "- **2015**: PIO + OCI schemes merged → **OCI Cardholder**; PIO cards deemed OCI from 9 Jan 2015.\n"
            "- OCI gets notified rights (lifelong multi-entry visa, parity in many economic/educational fields) "
            "but **not** political rights or constitutional offices.\n\n"
            "### OCI is not entitled to\n"
            "- Vote or contest for Lok Sabha / Rajya Sabha / state legislature / local bodies.\n"
            "- Hold office of President, VP, Judge of SC/HC, etc.\n"
            "- Appointment to public services / government posts (except notified exceptions like some faculty).\n\n"
            "**NRI** = Indian citizen ordinarily abroad (holds Indian passport). "
            "**PIO** = foreign national of Indian origin (scheme rescinded; historical label). "
            "**OCI** = registered cardholder under the Act."
        ),
        "articles": [
            ("Article 9", "No dual citizenship / dual nationality."),
        ],
        "visual_blocks": [
            {
                "id": "cit-nri-pio-oci",
                "type": "comparison",
                "title": "NRI vs PIO vs OCI (distilled)",
                "columns": [
                    {
                        "id": "nri",
                        "heading": "NRI",
                        "points": [
                            "Indian citizen abroad",
                            "Holds Indian passport",
                            "Full political rights of a citizen",
                            "No visa for India",
                        ],
                    },
                    {
                        "id": "pio",
                        "heading": "PIO (legacy)",
                        "points": [
                            "Foreign national of Indian origin",
                            "Foreign passport",
                            "Scheme rescinded 2015",
                            "Needed visa / police registration rules",
                        ],
                    },
                    {
                        "id": "oci",
                        "heading": "OCI Cardholder",
                        "points": [
                            "Registered under Citizenship Act",
                            "Foreign passport + OCI card",
                            "Not dual citizenship (Art. 9)",
                            "Lifelong multi-entry visa; no vote/office",
                        ],
                    },
                ],
            },
            {
                "id": "cit-oci-timeline",
                "type": "timeline",
                "title": "OCI evolution",
                "events": [
                    {
                        "id": "o1",
                        "year": 2003,
                        "label": "OCI introduced",
                        "detail": "Amendment Act 2003 — PIOs of 16 specified countries.",
                    },
                    {
                        "id": "o2",
                        "year": 2005,
                        "label": "Expanded",
                        "detail": "All countries except Pakistan & Bangladesh (if dual citizenship allowed there).",
                    },
                    {
                        "id": "o3",
                        "year": 2015,
                        "label": "PIO + OCI merged",
                        "detail": "OCI Cardholder scheme; PIO cards deemed OCI.",
                    },
                ],
            },
            {
                "id": "cit-oci-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "OCI ≠ dual citizenship. Cardholders cannot vote or hold constitutional posts. "
                    "Pakistan/Bangladesh nationals are outside the OCI scheme."
                ),
            },
        ],
    },
    {
        "title": "Reference & Revision Checklist",
        "slug": "cit-reference",
        "sort_order": 9,
        "summary": "Arts 5–11 at a glance plus the date checklist for last-minute revision.",
        "body": (
            "## Reference tables\n\n"
            "### Articles related to citizenship\n"
            "| Article | Theme |\n"
            "|---|---|\n"
            "| 5 | Citizenship at commencement (domicile) |\n"
            "| 6 | Migrants from Pakistan |\n"
            "| 7 | Returnees from Pakistan |\n"
            "| 8 | Persons of Indian origin abroad |\n"
            "| 9 | No voluntary foreign citizenship |\n"
            "| 10 | Continuance subject to law |\n"
            "| 11 | Parliament’s power to legislate |\n\n"
            "### Last-minute date checklist\n"
            "- Commencement citizenship: **26 Jan 1950**\n"
            "- Pakistan migrant cut-off: **19 Jul 1948**\n"
            "- Birth eras: **1 Jul 1987**, **3 Dec 2004**\n"
            "- Descent parent rule flip: **10 Dec 1992**\n"
            "- Assam: **1 Jan 1966**, **25 Mar 1971**\n"
            "- CAA entry cut-off: **31 Dec 2014** (in force 10 Jan 2020)\n"
            "- OCI merge: **2015**"
        ),
        "articles": [
            ("Article 5", "Citizenship at the commencement of the Constitution."),
            ("Article 6", "Rights of citizenship of certain persons who have migrated to India from Pakistan."),
            ("Article 7", "Rights of citizenship of certain migrants to Pakistan."),
            ("Article 8", "Rights of citizenship of certain persons of Indian origin residing outside India."),
            ("Article 9", "Persons voluntarily acquiring citizenship of a foreign State not to be citizens."),
            ("Article 10", "Continuance of the rights of citizenship."),
            ("Article 11", "Parliament to regulate the right of citizenship by law."),
        ],
        "visual_blocks": [
            {
                "id": "cit-arts-pillars",
                "type": "pillars",
                "title": "Arts 5–11 at a glance",
                "items": [
                    {
                        "id": "r5",
                        "articles": "Art. 5",
                        "label": "Commencement",
                        "slug": "cit-constitution",
                        "detail": "Domicile + birth / parent / 5-year residence.",
                        "tone": "teal",
                    },
                    {
                        "id": "r6",
                        "articles": "Art. 6",
                        "label": "From Pakistan",
                        "slug": "cit-constitution",
                        "detail": "Migration rules; 19 Jul 1948 cut-off.",
                        "tone": "olive",
                    },
                    {
                        "id": "r7",
                        "articles": "Art. 7",
                        "label": "Returnees",
                        "slug": "cit-constitution",
                        "detail": "Left after 1 Mar 1947, then returned.",
                        "tone": "gold",
                    },
                    {
                        "id": "r8",
                        "articles": "Art. 8",
                        "label": "Overseas origin",
                        "slug": "cit-constitution",
                        "detail": "Registered by diplomatic/consular rep.",
                        "tone": "orange",
                    },
                    {
                        "id": "r9",
                        "articles": "Art. 9",
                        "label": "No dual",
                        "slug": "cit-oci",
                        "detail": "Voluntary foreign citizenship bar.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "r10",
                        "articles": "Art. 10",
                        "label": "Continuance",
                        "slug": "cit-constitution",
                        "detail": "Subject to law made by Parliament.",
                        "tone": "maroon",
                    },
                    {
                        "id": "r11",
                        "articles": "Art. 11",
                        "label": "Parliament",
                        "slug": "cit-acquisition",
                        "detail": "Power to legislate all citizenship matters.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "cit-checklist",
                "type": "callout",
                "tone": "tip",
                "title": "Revision checklist",
                "body": (
                    "Citizen-only rights → single citizenship exceptions → Arts 5–11 → "
                    "birth/descent dates → Assam → CAA carve-outs → loss trio → OCI ≠ dual."
                ),
            },
            {
                "id": "cit-ref-note",
                "type": "callout",
                "tone": "note",
                "title": "Book bridge",
                "body": (
                    "Tables 7.1–7.2 in Laxmikanth are the full statutory compare. "
                    "Use this cluster for speed; open the book only for disputed edge cases."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "cit-meaning"),
    (HUB_SLUG, "parent", "cit-single"),
    (HUB_SLUG, "parent", "cit-constitution"),
    (HUB_SLUG, "parent", "cit-acquisition"),
    (HUB_SLUG, "parent", "cit-assam"),
    (HUB_SLUG, "parent", "cit-caa"),
    (HUB_SLUG, "parent", "cit-loss"),
    (HUB_SLUG, "parent", "cit-oci"),
    (HUB_SLUG, "parent", "cit-reference"),
    (HUB_SLUG, "related", "sf-single-citizenship"),
    (HUB_SLUG, "related", "fundamental-rights"),
    ("cit-single", "related", "sf-single-citizenship"),
    ("cit-meaning", "related", "fundamental-rights"),
    ("cit-constitution", "related", "cit-acquisition"),
    ("cit-acquisition", "related", "cit-caa"),
    ("cit-acquisition", "related", "cit-assam"),
    ("cit-caa", "related", "cit-assam"),
    ("cit-loss", "related", "cit-constitution"),
    ("cit-oci", "related", "cit-loss"),
    ("cit-reference", "related", "cit-constitution"),
    ("cit-reference", "related", "cit-acquisition"),
]

SAMPLE_PYQS = [
    (
        2021,
        "With reference to India, consider the following statements: "
        "1. There is only one citizenship and one domicile. "
        "2. A citizen by birth only can become the Head of State. "
        "Which of the statements given above is/are correct?",
        "Statement 1 aligns with single citizenship (domicile nuances aside in practice). "
        "Statement 2 is incorrect — naturalised citizens can also be President in India.",
        ["cit-single", "cit-meaning"],
    ),
    (
        2019,
        "Consider the following statements about the Citizenship Amendment Act / related themes: "
        "illegal migrants and eligibility for citizenship.",
        "Focus CAA 2019: listed communities from AFG/BD/PK; entry on/before 31 Dec 2014; "
        "Sixth Schedule / Inner Line exclusions; residence reduction for naturalisation.",
        ["cit-caa", "cit-acquisition"],
    ),
    (
        2018,
        "Which of the following are provided under Part II of the Constitution of India "
        "relating to citizenship?",
        "Arts 5–11 — commencement categories + Art. 11 power of Parliament. "
        "Post-1950 modes live in the Citizenship Act, 1955.",
        ["cit-constitution"],
    ),
    (
        2014,
        "The power to grant / regulate citizenship in India primarily rests with:",
        "Parliament under Article 11; detailed in the Citizenship Act, 1955.",
        ["cit-constitution", "cit-acquisition"],
    ),
]

# Citizenship Act amendments (1985 Assam, 2003/2005/2015 OCI, 2019 CAA) live in
# cluster timelines — they are ordinary statutes, not ConstitutionalAmendment rows.


class Command(BaseCommand):
    help = "Seed Citizenship chapter (Laxmikanth Ch.7) — visual revision."

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
                "title": "Citizenship",
                "sort_order": 7,
                "book_ref": "Laxmikanth 8th Ed, Ch. 7",
                "summary": (
                    "Visual revision of Ch.7 — membership-card mental model, single citizenship, "
                    "Arts 5–11, acquisition/loss, Assam Accord, CAA 2019, and OCI."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Citizenship",
                "summary": (
                    "Part II membership rules — who is a citizen, how citizenship is acquired or lost, "
                    "and how OCI differs from dual nationality."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **membership-card mental model**, then scan the **eight themes**. "
                    "Drill date cutoffs (birth, Assam, CAA) and finish with OCI vs NRI. "
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
            ref="Laxmikanth Ch. 7",
            excerpt="Citizenship — Part II (Arts 5–11) and the Citizenship Act, 1955.",
            sort_order=0,
        )

        cit_slugs = set(by_slug.keys())
        related_outside = {"sf-single-citizenship", "fundamental-rights"}
        ConceptEdge.objects.filter(
            source__slug__in=cit_slugs, source__subject=subject
        ).filter(target__slug__in=cit_slugs | related_outside).delete()

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
                f"Citizenship chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} PYQs."
            )
        )
