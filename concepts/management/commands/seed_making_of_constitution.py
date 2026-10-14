"""Seed Laxmikanth Ch.2 Making of the Constitution (visual chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "making-of-constitution"
CHAPTER_SLUG = "making-of-constitution"

CHAPTER_PILLARS = [
    {
        "id": "demand",
        "articles": "1934–1946",
        "label": "Demand for Constituent Assembly",
        "slug": "moc-demand",
        "detail": "MN Roy → INC → August Offer → Cripps → Cabinet Mission.",
        "tone": "teal",
    },
    {
        "id": "composition",
        "articles": "389 seats",
        "label": "Composition of the Assembly",
        "slug": "moc-composition",
        "detail": "296 British India + 93 princely; partly elected, partly nominated.",
        "tone": "olive",
    },
    {
        "id": "working",
        "articles": "Dec 1946+",
        "label": "Working of the Assembly",
        "slug": "moc-working",
        "detail": "Officers, Objectives Resolution, Independence Act changes, other functions.",
        "tone": "gold",
    },
    {
        "id": "committees",
        "articles": "8 major",
        "label": "Committees of the Assembly",
        "slug": "moc-committees",
        "detail": "Major & minor committees; Drafting Committee under Ambedkar.",
        "tone": "orange",
    },
    {
        "id": "enactment",
        "articles": "Art. 394",
        "label": "Enactment & Enforcement",
        "slug": "moc-enactment-enforcement",
        "detail": "26 Nov 1949 adoption; 26 Jan 1950 commencement (Republic Day).",
        "tone": "terracotta",
    },
    {
        "id": "experts",
        "articles": "Jul 1946",
        "label": "Congress Experts Committee",
        "slug": "moc-experts-committee",
        "detail": "Nehru-chaired prep body; drafted Objectives-like resolution.",
        "tone": "maroon",
    },
    {
        "id": "criticism",
        "articles": "Facts",
        "label": "Criticism & Important Facts",
        "slug": "moc-criticism-facts",
        "detail": "Six critiques, key personalities, Hindi text (Art. 394-A).",
        "tone": "teal",
    },
    {
        "id": "tables",
        "articles": "2.1–2.8",
        "label": "Reference Tables",
        "slug": "moc-reference-tables",
        "detail": "Seats, elections, communities, sessions, time comparison, Art. 393–395.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "moc-forge-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Constitutional forge",
        "topic_label": "Making of the Constitution",
        "subject_label": "Demand → Draft → Republic",
        "relation_label": "Helps you avoid",
        "protects_from": [
            "Mixing adoption (26 Nov) with commencement (26 Jan)",
            "Confusing temporary vs permanent Chairman",
            "Mixing Cabinet Mission strength with post-partition strength",
            "Forgetting Drafting Committee replacements",
        ],
        "insight": (
            "Forge the Constitution in sequence — demand, assemble, resolve, "
            "committee-draft, enact, then commence."
        ),
    },
    {
        "id": "moc-chapter-pillars",
        "type": "pillars",
        "title": "Chapter clusters to open",
        "items": CHAPTER_PILLARS,
    },
    {
        "id": "moc-hub-tip",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchors",
        "body": (
            "Date chain: 9 Dec 1946 (first meeting) → 22 Jan 1947 (Objectives adopted) → "
            "26 Nov 1949 (enacted) → 26 Jan 1950 (commenced). "
            "Numbers: 389 → 299; 11 sessions; ₹64 lakh; 114 days on Draft."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Demand for a Constituent Assembly",
        "slug": "moc-demand",
        "sort_order": 1,
        "summary": (
            "Idea from MN Roy (1934) to Cabinet Mission (1946) — how India won the right "
            "to frame its own Constitution."
        ),
        "body": (
            "## Demand for a Constituent Assembly\n\n"
            "### Timeline of the demand\n"
            "1. **1934** — **M.N. Roy** (pioneer of the communist movement) first put forward "
            "the idea of a Constituent Assembly for India.\n"
            "2. **1935** — INC officially demanded a Constituent Assembly to frame the "
            "Constitution of India.\n"
            "3. **1938** — **Jawaharlal Nehru**, on behalf of the INC, declared that the "
            "Constitution of free India must be framed **without outside interference**, by a "
            "Constituent Assembly elected on the basis of **adult franchise**. INC reiterated "
            "this by resolution in **1939**.\n"
            "4. **1940** — British Government accepted the demand **in principle** in the "
            "**August Offer**.\n"
            "5. **1942** — **Sir Stafford Cripps** brought draft proposals for an independent "
            "Constitution after WWII. **Muslim League rejected** Cripps Proposals — it wanted "
            "India divided into two autonomous states with **two separate Constituent Assemblies**.\n"
            "6. **1946** — **Cabinet Mission** (Lord Pethick-Lawrence, Sir Stafford Cripps, "
            "A.V. Alexander) arrived 24 March; plan published **16 May 1946**. It **rejected** "
            "two Assemblies but offered a scheme that more or less satisfied the League.\n\n"
            "### Exam anchors\n"
            "- First idea → **MN Roy (1934)**; first INC demand → **1935**.\n"
            "- Adult franchise + no outside interference → **Nehru 1938**.\n"
            "- Principle acceptance → **August Offer 1940**."
        ),
        "articles": [
            (
                "Cabinet Mission, 1946",
                "Pethick-Lawrence, Cripps, Alexander — plan 16 May 1946; one Assembly scheme.",
            ),
            (
                "August Offer, 1940",
                "British accepted Constituent Assembly demand in principle.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "moc-demand-timeline",
                "type": "timeline",
                "title": "From idea to Cabinet Mission",
                "events": [
                    {
                        "id": "e1934",
                        "year": 1934,
                        "label": "MN Roy",
                        "detail": "First idea of a Constituent Assembly for India.",
                    },
                    {
                        "id": "e1935",
                        "year": 1935,
                        "label": "INC demand",
                        "detail": "Congress officially demanded a CA.",
                    },
                    {
                        "id": "e1938",
                        "year": 1938,
                        "label": "Nehru statement",
                        "detail": "No outside interference; adult franchise.",
                    },
                    {
                        "id": "e1940",
                        "year": 1940,
                        "label": "August Offer",
                        "detail": "British accept demand in principle.",
                    },
                    {
                        "id": "e1942",
                        "year": 1942,
                        "label": "Cripps Mission",
                        "detail": "League rejects — wants two Assemblies.",
                    },
                    {
                        "id": "e1946",
                        "year": 1946,
                        "label": "Cabinet Mission",
                        "detail": "One Assembly scheme; elections follow.",
                    },
                ],
            },
            {
                "id": "moc-demand-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Cripps was rejected by the League over **two Assemblies**. "
                    "Cabinet Mission rejected two Assemblies but still offered a scheme "
                    "the League could live with."
                ),
            },
        ],
    },
    {
        "title": "Composition of the Constituent Assembly",
        "slug": "moc-composition",
        "sort_order": 2,
        "summary": (
            "Cabinet Mission scheme: 389 seats; indirect election by provincial assemblies; "
            "princely nominees; July–August 1946 results."
        ),
        "body": (
            "## Composition of the Constituent Assembly\n\n"
            "Constituted in **November 1946** under the Cabinet Mission Plan.\n\n"
            "### Scheme features\n"
            "1. Total strength **389** — **296** British India + **93** princely states. "
            "Of 296: **292** from eleven governors’ provinces + **4** from Chief Commissioners’ "
            "provinces (one each).\n"
            "2. Seats allotted roughly **one per million** population.\n"
            "3. Provincial seats divided among **Muslims, Sikhs, and General** "
            "(all except Muslims and Sikhs) in proportion to population.\n"
            "4. Community representatives elected by that community’s members in the "
            "provincial legislative assembly by **proportional representation (single transferable vote)**.\n"
            "5. Princely state representatives **nominated** by the heads of the states.\n\n"
            "### Nature of the body\n"
            "- **Partly elected, partly nominated**.\n"
            "- Members **indirectly** elected by provincial assemblies (themselves elected "
            "on limited franchise under GoI Act 1935).\n\n"
            "### July–August 1946 elections (296 British India seats)\n"
            "- **INC 208**, **Muslim League 73**, others/independents **15**.\n"
            "- **93 princely seats not filled** initially — states stayed away.\n"
            "- Assembly represented all sections (Hindus, Muslims, Sikhs, Parsis, "
            "Anglo-Indians, Indian Christians, SCs, STs, women) — but **not Gandhi**.\n\n"
            "Governors’ provinces (11): Madras, Bombay, UP, Bihar, Central Provinces, "
            "Orissa, Punjab, NWFP, Sindh, Bengal, Assam. "
            "CC provinces (4): Delhi, Ajmer–Merwara, Coorg, British Baluchistan."
        ),
        "articles": [
            (
                "Cabinet Mission Plan",
                "389 = 296 (British India) + 93 (princely). Indirect PR-STV election.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "moc-comp-pillars",
                "type": "pillars",
                "title": "389 seats at a glance",
                "items": [
                    {
                        "id": "bi",
                        "articles": "296",
                        "label": "British India",
                        "slug": "moc-composition",
                        "detail": "292 governors’ provinces + 4 CC provinces.",
                        "tone": "teal",
                    },
                    {
                        "id": "ps",
                        "articles": "93",
                        "label": "Princely states",
                        "slug": "moc-composition",
                        "detail": "Nominated by rulers; initially vacant.",
                        "tone": "olive",
                    },
                    {
                        "id": "method",
                        "articles": "PR-STV",
                        "label": "Election method",
                        "slug": "moc-composition",
                        "detail": "Indirect; by community in provincial assemblies.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "moc-comp-compare",
                "type": "comparison",
                "title": "1946 election snapshot (British India)",
                "columns": [
                    {
                        "id": "congress",
                        "heading": "Congress",
                        "points": ["208 seats", "Clear majority of filled seats"],
                    },
                    {
                        "id": "league",
                        "heading": "Muslim League",
                        "points": ["73 seats", "Boycotted first meeting later"],
                    },
                    {
                        "id": "others",
                        "heading": "Others",
                        "points": [
                            "15 seats (groups + independents)",
                            "Total filled = 296",
                        ],
                    },
                ],
            },
            {
                "id": "moc-comp-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Not directly elected on adult franchise — provincial assemblies used "
                    "**limited franchise**. Do not call the 1946 CA a universal-franchise body."
                ),
            },
        ],
    },
    {
        "title": "Working of the Constituent Assembly",
        "slug": "moc-working",
        "sort_order": 3,
        "summary": (
            "First meeting to Objectives Resolution, Independence Act changes, other "
            "functions, and key session statistics."
        ),
        "body": (
            "## Working of the Constituent Assembly\n\n"
            "### First meeting & officers\n"
            "- First meeting: **9 December 1946** — League boycotted; **207** members present.\n"
            "- Temporary Chairman (French practice — oldest member): "
            "**Dr. Sachchidananda Sinha**.\n"
            "- Permanent President: **Dr. Rajendra Prasad** (11 Dec 1946).\n"
            "- Vice-President: **H.C. Mukherjee** (25 Jan 1947); later a second VP — "
            "**V.T. Krishnamachari** (16 July 1947).\n\n"
            "### Objectives Resolution\n"
            "Moved by **Nehru on 13 December 1946**; unanimously adopted **22 January 1947**.\n"
            "Laid down fundamentals and philosophy — Independent Sovereign Republic; "
            "Union of territories; power from the people; justice, equality, freedom; "
            "safeguards for minorities/backward/tribal areas; integrity; world peace.\n"
            "**Modified version forms the Preamble.**\n\n"
            "### Changes by the Independence Act, 1947\n"
            "1. Assembly became a **fully sovereign** body — could frame any Constitution "
            "and alter British laws relating to India.\n"
            "2. Also a **legislative body** (Dominion Legislature / first Parliament of free India). "
            "Constitution days chaired by **Rajendra Prasad**; legislative days by "
            "**G.V. Mavlankar**. Dual role till **26 Nov 1949**. First Dominion Legislature "
            "meeting: **17 Nov 1947** (Mavlankar elected Speaker).\n"
            "3. League members from Pakistan areas withdrew → strength **389 → 299** "
            "(provinces 296→229; princely 93→70).\n"
            "Princely representatives gradually joined after Mountbatten Plan (3 June 1947); "
            "six states seated by 28 April 1947 (Baroda, Bikaner, Jaipur, Patiala, Rewa, Udaipur).\n\n"
            "### Other functions\n"
            "1. Ratified Commonwealth membership (May 1949).\n"
            "2. National Flag — **22 July 1947**.\n"
            "3. National Anthem — **24 Jan 1950**.\n"
            "4. National Song — **24 Jan 1950**.\n"
            "5. Elected **Rajendra Prasad** first President — **24 Jan 1950**.\n\n"
            "### Scale facts\n"
            "- **11 sessions**; **2 years, 11 months, 18 days**.\n"
            "- Studied ~**60** constitutions; Draft considered **114 days**; cost **₹64 lakh**.\n"
            "- Final CA session **24 Jan 1950**; continued as **provisional Parliament** "
            "from 26 Jan 1950 until new Parliament after 1951–52 elections."
        ),
        "articles": [
            (
                "Objectives Resolution, 1947",
                "Nehru 13 Dec 1946; adopted 22 Jan 1947 — basis of the Preamble.",
            ),
            (
                "Indian Independence Act, 1947",
                "Sovereign CA + Dominion Legislature; League exit → 299 members.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "moc-work-timeline",
                "type": "timeline",
                "title": "Working milestones",
                "events": [
                    {
                        "id": "e1946-12-09",
                        "year": 1946,
                        "label": "First meeting",
                        "detail": "9 Dec — Sinha temporary Chairman; League boycott.",
                    },
                    {
                        "id": "e1946-12-13",
                        "year": 1946,
                        "label": "Objectives moved",
                        "detail": "Nehru introduces Objectives Resolution.",
                    },
                    {
                        "id": "e1947-01-22",
                        "year": 1947,
                        "label": "Objectives adopted",
                        "detail": "22 Jan — philosophy locked for the Constitution.",
                    },
                    {
                        "id": "e1947-act",
                        "year": 1947,
                        "label": "Independence Act",
                        "detail": "Sovereign CA + legislature; strength → 299.",
                    },
                    {
                        "id": "e1950-01-24",
                        "year": 1950,
                        "label": "Final CA session",
                        "detail": "Flag/anthem/song; Prasad elected President.",
                    },
                ],
            },
            {
                "id": "moc-work-compare",
                "type": "comparison",
                "title": "Two hats of the Assembly (after Independence Act)",
                "columns": [
                    {
                        "id": "const",
                        "heading": "Constituent body",
                        "points": [
                            "Frames the Constitution",
                            "Chaired by Dr. Rajendra Prasad",
                            "Ends constitution-making on 26 Nov 1949",
                        ],
                    },
                    {
                        "id": "leg",
                        "heading": "Legislative body",
                        "points": [
                            "Enacts ordinary laws (Dominion Legislature)",
                            "Chaired by G.V. Mavlankar",
                            "First such sitting 17 Nov 1947",
                        ],
                    },
                ],
            },
            {
                "id": "moc-work-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Temporary Chairman = **Sinha**; permanent President = **Prasad**. "
                    "Legislative chair = **Mavlankar** (not Prasad)."
                ),
            },
        ],
    },
    {
        "title": "Committees of the Constituent Assembly",
        "slug": "moc-committees",
        "sort_order": 4,
        "summary": (
            "Eight major committees, key minor ones, and the seven-member Drafting "
            "Committee under Dr. B.R. Ambedkar."
        ),
        "body": (
            "## Committees of the Constituent Assembly\n\n"
            "### Eight major committees\n"
            "1. **Union Powers** — Jawaharlal Nehru\n"
            "2. **Union Constitution** — Jawaharlal Nehru\n"
            "3. **Provincial Constitution** — Sardar Patel\n"
            "4. **Drafting Committee** — Dr. B.R. Ambedkar\n"
            "5. **Advisory Committee** on FR, Minorities and Tribal & Excluded Areas — "
            "Sardar Patel, with sub-committees:\n"
            "   - Fundamental Rights — J.B. Kripalani\n"
            "   - Minorities — H.C. Mukherjee\n"
            "   - NE Frontier Tribal Areas & Assam Excluded/Partially Excluded — "
            "Gopinath Bardoloi\n"
            "   - Excluded/Partially Excluded (other than Assam) — A.V. Thakkar\n"
            "   - NW Frontier Tribal Areas (sub-committee)\n"
            "6. **Rules of Procedure** — Dr. Rajendra Prasad\n"
            "7. **States Committee** (negotiating with states) — Jawaharlal Nehru\n"
            "8. **Steering Committee** — Dr. Rajendra Prasad\n\n"
            "### Drafting Committee (most important)\n"
            "Set up **29 August 1947**; prepared the draft Constitution.\n"
            "Seven members:\n"
            "1. **Dr. B.R. Ambedkar** (Chairman)\n"
            "2. N. Gopalaswamy Ayyangar\n"
            "3. Alladi Krishnaswamy Ayyar\n"
            "4. Dr. K.M. Munshi\n"
            "5. Syed Mohammad Saadullah\n"
            "6. **N. Madhava Rau** (replaced B.L. Mitter — resigned, ill-health)\n"
            "7. **T.T. Krishnamachari** (replaced D.P. Khaitan — died 1948)\n\n"
            "First draft published **February 1948** (8 months public comment); "
            "second draft **October 1948**. Sat **141 days**; draft prepared in "
            "less than six months.\n\n"
            "### Minor committees (high-yield names)\n"
            "Finance & Staff / Ad-hoc National Flag / Functions of CA — Prasad / "
            "Prasad / **G.V. Mavalankar**; Credentials — Alladi Krishnaswami Ayyar; "
            "House / Chief Commissioners’ Provinces — B. Pattabhi Sitaramayya; "
            "Order of Business — K.M. Munshi; SC / Citizenship ad-hoc — "
            "S. Varadachari (not Assembly member); Linguistic Provinces — S.K. Dar "
            "(not member); Expert Financial Provisions — Nalini Ranjan Sarkar "
            "(not member); Special Committee on Draft — Nehru."
        ),
        "articles": [
            (
                "Drafting Committee, 29 Aug 1947",
                "Ambedkar chair; 7 members; 141 sitting days; drafts Feb & Oct 1948.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "moc-comm-pillars",
                "type": "pillars",
                "title": "Major committees — chair memory",
                "items": [
                    {
                        "id": "nehru",
                        "articles": "3 chairs",
                        "label": "Nehru chairs",
                        "slug": "moc-committees",
                        "detail": "Union Powers, Union Constitution, States Committee.",
                        "tone": "teal",
                    },
                    {
                        "id": "patel",
                        "articles": "2 chairs",
                        "label": "Patel chairs",
                        "slug": "moc-committees",
                        "detail": "Provincial Constitution + Advisory (FR/Minorities/Tribal).",
                        "tone": "olive",
                    },
                    {
                        "id": "prasad",
                        "articles": "2 chairs",
                        "label": "Prasad chairs",
                        "slug": "moc-committees",
                        "detail": "Rules of Procedure + Steering.",
                        "tone": "gold",
                    },
                    {
                        "id": "ambedkar",
                        "articles": "Drafting",
                        "label": "Ambedkar",
                        "slug": "moc-committees",
                        "detail": "Drafting Committee — the constitutional forge.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "moc-draft-compare",
                "type": "comparison",
                "title": "Drafting Committee — original vs replacements",
                "columns": [
                    {
                        "id": "core",
                        "heading": "Core five (unchanged)",
                        "points": [
                            "Ambedkar (Chair)",
                            "N. Gopalaswamy Ayyangar",
                            "Alladi Krishnaswamy Ayyar",
                            "K.M. Munshi",
                            "Syed Mohammad Saadullah",
                        ],
                    },
                    {
                        "id": "repl",
                        "heading": "Replacements",
                        "points": [
                            "N. Madhava Rau ← B.L. Mitter (ill-health)",
                            "T.T. Krishnamachari ← D.P. Khaitan (died 1948)",
                        ],
                    },
                ],
            },
            {
                "id": "moc-comm-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Memorise the seven Drafting members and the two replacements. "
                    "Naziruddin Ahmed mocked it as the “Drifting Committee”."
                ),
            },
        ],
    },
    {
        "title": "Enactment and Enforcement",
        "slug": "moc-enactment-enforcement",
        "sort_order": 5,
        "summary": (
            "Three readings to 26 November 1949 adoption; major part commenced "
            "26 January 1950 — Republic Day and Purna Swaraj link."
        ),
        "body": (
            "## Enactment of the Constitution\n\n"
            "- **First reading**: Ambedkar introduced final draft **4 Nov 1948**; "
            "general discussion till **9 Nov 1948** (5 days).\n"
            "- **Second reading** (clause by clause): **15 Nov 1948 – 17 Oct 1949**. "
            "**7,653** amendments proposed; **2,473** discussed.\n"
            "- **Third reading**: from **14 Nov 1949**. Motion that the Constitution "
            "as settled be passed — declared passed **26 November 1949**. "
            "**284 of 299** members present signed.\n"
            "- Date in the **Preamble** = adoption/enactment date.\n"
            "- Adopted text: **Preamble + 395 Articles + 8 Schedules**. "
            "Preamble enacted **after** the rest of the Constitution.\n"
            "- Ambedkar (Law Minister) piloted the Draft — ‘**Father of the Constitution**’ / "
            "‘**chief architect**’.\n"
            "- From **2015**, **26 November** = **Constitution Day (Samvidhan Divas)**.\n\n"
            "## Enforcement of the Constitution\n\n"
            "- Some provisions in force from **26 Nov 1949** itself: citizenship, elections, "
            "provisional parliament, temporary/transitional, short title — "
            "Arts. **5–9, 60, 324, 366, 367, 379, 380, 388, 391, 392, 393**.\n"
            "- Remaining (major) part from **26 January 1950** — ‘**date of commencement**’; "
            "**Republic Day**.\n"
            "- **26 Jan** chosen for historical link to **Purna Swaraj Day 1930** "
            "(Lahore Session, Dec 1929).\n"
            "- With commencement: **Independence Act 1947** and **GoI Act 1935** "
            "(and amending/supplementing Acts) **repealed**. "
            "**Abolition of Privy Council Jurisdiction Act (1949)** continued."
        ),
        "articles": [
            (
                "Art. 394",
                "Commencement — some Arts from 26 Nov 1949; major part from 26 Jan 1950.",
            ),
            (
                "Art. 395",
                "Repeals — Independence Act 1947 and GoI Act 1935 (with supplements).",
            ),
            (
                "Preamble date",
                "26 November 1949 — adopted, enacted and given to ourselves.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "moc-enact-journey",
                "type": "journey",
                "title": "From draft to Republic",
                "stages": [
                    {
                        "id": "s1",
                        "label": "First reading",
                        "detail": "4–9 Nov 1948 — Ambedkar introduces final draft.",
                    },
                    {
                        "id": "s2",
                        "label": "Second reading",
                        "detail": "15 Nov 1948 – 17 Oct 1949 — clause by clause.",
                    },
                    {
                        "id": "s3",
                        "label": "Third reading & adoption",
                        "detail": "14–26 Nov 1949 — Constitution passed & signed.",
                        "slug": "moc-enactment-enforcement",
                    },
                    {
                        "id": "s4",
                        "label": "Partial force",
                        "detail": "26 Nov 1949 — selected Articles operate.",
                    },
                    {
                        "id": "s5",
                        "label": "Commencement",
                        "detail": "26 Jan 1950 — Republic Day; major part in force.",
                    },
                ],
            },
            {
                "id": "moc-enact-flow",
                "type": "flowchart",
                "title": "Which date applies?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What are you asked about?",
                        "detail": "Match the event to the right date.",
                        "options": [
                            {"label": "Adopted / enacted / Preamble date", "next": "adopt"},
                            {"label": "Date of commencement / Republic Day", "next": "commence"},
                            {"label": "Constitution Day (from 2015)", "next": "day"},
                        ],
                    },
                    {
                        "id": "adopt",
                        "label": "26 November 1949",
                        "detail": "Passed & signed; some Articles already in force.",
                    },
                    {
                        "id": "commence",
                        "label": "26 January 1950",
                        "detail": "Major part begins; Purna Swaraj anniversary logic.",
                    },
                    {
                        "id": "day",
                        "label": "26 November (Samvidhan Divas)",
                        "detail": "Observed every year from 2015 to promote constitutional values.",
                    },
                ],
            },
            {
                "id": "moc-enact-tip",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Do not mix **adoption (26 Nov 1949)** with **commencement (26 Jan 1950)**. "
                    "Preamble carries the adoption date, not Republic Day."
                ),
            },
        ],
    },
    {
        "title": "Experts Committee of the Congress",
        "slug": "moc-experts-committee",
        "sort_order": 6,
        "summary": (
            "July 1946 Congress Experts Committee under Nehru prepared material and "
            "a draft objectives resolution for the Assembly."
        ),
        "body": (
            "## Experts Committee of the Congress\n\n"
            "Appointed **8 July 1946** while CA elections were still in progress, "
            "to prepare material for the Constituent Assembly.\n\n"
            "### Members\n"
            "1. **Jawaharlal Nehru** (Chairman)\n"
            "2. M. Asaf Ali\n"
            "3. K.M. Munshi\n"
            "4. N. Gopalaswami Ayyangar\n"
            "5. K.T. Shah\n"
            "6. D.R. Gadgil\n"
            "7. Humayun Kabir\n"
            "8. K. Santhanam\n"
            "Later co-opted: **Krishna Kripalani** (member and convener).\n\n"
            "### Sittings\n"
            "- New Delhi: **20–22 July 1946**\n"
            "- Bombay: **15–17 August 1946**\n\n"
            "Discussed CA procedure, appointment of committees, and a draft resolution "
            "on constitutional objectives for the first session.\n\n"
            "### Granville Austin\n"
            "“It was the Congress Experts Committee that set India on the road to her "
            "present Constitution.” Working within the Cabinet Mission framework, it "
            "suggested lines on autonomous areas, Centre–province powers, princely "
            "states, amending power — and drafted a resolution closely resembling the "
            "**Objectives Resolution**."
        ),
        "articles": [
            (
                "Congress Experts Committee, Jul 1946",
                "Nehru chair; drafted Objectives-like resolution before CA first session.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "moc-experts-pillars",
                "type": "pillars",
                "title": "Why this committee matters",
                "items": [
                    {
                        "id": "prep",
                        "articles": "Jul 1946",
                        "label": "Pre-Assembly prep",
                        "slug": "moc-experts-committee",
                        "detail": "Material ready while elections were still on.",
                        "tone": "teal",
                    },
                    {
                        "id": "obj",
                        "articles": "Draft",
                        "label": "Objectives draft",
                        "slug": "moc-experts-committee",
                        "detail": "Resolution closely resembling Objectives Resolution.",
                        "tone": "olive",
                    },
                    {
                        "id": "austin",
                        "articles": "Austin",
                        "label": "Austin’s verdict",
                        "slug": "moc-experts-committee",
                        "detail": "Set India on the road to her present Constitution.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "moc-experts-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Link to Working cluster",
                "body": (
                    "Experts Committee draft → Nehru’s Objectives Resolution in the Assembly "
                    "→ modified version becomes the Preamble."
                ),
            },
        ],
    },
    {
        "title": "Criticism and Important Facts",
        "slug": "moc-criticism-facts",
        "sort_order": 7,
        "summary": (
            "Six classic critiques of the Assembly, high-yield personality facts, "
            "and Hindi authoritative text (Art. 394-A / 58th Amendment)."
        ),
        "body": (
            "## Criticism of the Constituent Assembly\n\n"
            "1. **Not representative** — not directly elected on universal adult franchise.\n"
            "2. **Not sovereign** — created by British proposals; sessions with British permission "
            "(critics’ view; Independence Act later made it fully sovereign).\n"
            "3. **Time-consuming** — unduly long vs USA (~4 months). "
            "Naziruddin Ahmed called Drafting Committee a “**Drifting Committee**”.\n"
            "4. **Congress-dominated** — Austin: “The Assembly was the Congress and the "
            "Congress was India.”\n"
            "5. **Lawyer–politician domination** — other sections under-represented; blamed "
            "for bulk and complex language.\n"
            "6. **Hindu-dominated** — Viscount Simon: ‘a body of Hindus’; Churchill: "
            "represented ‘only one major community’.\n\n"
            "## Important facts\n\n"
            "1. **Elephant** — seal/symbol of the Constituent Assembly.\n"
            "2. **Sir B.N. Rau** — constitutional advisor (Legal Advisor).\n"
            "3. **H.V.R. Iyengar** — Secretary to the Assembly.\n"
            "4. **S.N. Mukherjee** — chief draftsman.\n"
            "5. **Prem Behari Narain Raizada** — calligrapher (flowing italic original).\n"
            "6. Beautified by Shantiniketan artists including **Nand Lal Bose** and "
            "**Beohar Rammanohar Sinha**.\n"
            "7. **Beohar Rammanohar Sinha** illuminated/ornamented the original Preamble.\n"
            "8. Hindi calligraphy by **Vasant Krishan Vaidya**; decorated by **Nand Lal Bose**.\n\n"
            "## Hindi text of the Constitution\n\n"
            "Originally no authoritative Hindi text. **58th Amendment Act, 1987** inserted "
            "**Article 394-A** (Part XXII):\n"
            "- President causes publication of Hindi translation of the Constitution "
            "(with necessary language conformity) including prior amendments, and Hindi "
            "of every amendment made in English.\n"
            "- Published translation construed to have the **same meaning** as English; "
            "President may revise Hindi text if difficulty arises.\n"
            "- Published translation deemed **authoritative Hindi text** for all purposes."
        ),
        "articles": [
            (
                "Art. 394-A",
                "Authoritative Hindi text — inserted by 58th Amendment, 1987.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "moc-crit-pillars",
                "type": "pillars",
                "title": "Six criticisms — scan list",
                "items": [
                    {
                        "id": "c1",
                        "articles": "1",
                        "label": "Not representative",
                        "slug": "moc-criticism-facts",
                        "detail": "No direct adult-franchise election.",
                        "tone": "teal",
                    },
                    {
                        "id": "c2",
                        "articles": "2",
                        "label": "Not sovereign",
                        "slug": "moc-criticism-facts",
                        "detail": "British-created; permission critique.",
                        "tone": "olive",
                    },
                    {
                        "id": "c3",
                        "articles": "3",
                        "label": "Time-consuming",
                        "slug": "moc-criticism-facts",
                        "detail": "“Drifting Committee” jibe.",
                        "tone": "gold",
                    },
                    {
                        "id": "c4",
                        "articles": "4–6",
                        "label": "Dominance critiques",
                        "slug": "moc-criticism-facts",
                        "detail": "Congress / lawyers-politicians / Hindus.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "moc-facts-compare",
                "type": "comparison",
                "title": "Who did what?",
                "columns": [
                    {
                        "id": "legal",
                        "heading": "Legal / drafting roles",
                        "points": [
                            "B.N. Rau — constitutional advisor",
                            "S.N. Mukherjee — chief draftsman",
                            "Ambedkar — Drafting Chair / Father of Constitution",
                        ],
                    },
                    {
                        "id": "art",
                        "heading": "Calligraphy / art",
                        "points": [
                            "Raizada — English calligraphy",
                            "Beohar Rammanohar Sinha — Preamble ornament",
                            "Nand Lal Bose — decoration / Hindi illumination",
                            "Vasant Krishan Vaidya — Hindi calligraphy",
                        ],
                    },
                ],
            },
            {
                "id": "moc-crit-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "Pair criticisms with counters from Working/Enactment: "
                    "sovereignty after Independence Act; broad social representation; "
                    "scale of the task vs USA’s shorter document."
                ),
            },
        ],
    },
    {
        "title": "Reference Tables — Seats, Sessions, Articles",
        "slug": "moc-reference-tables",
        "sort_order": 8,
        "summary": (
            "Condensed Tables 2.1–2.8 — allocation, elections, communities, women members, "
            "post-partition strength, sessions, comparative time, and Art. 393–395."
        ),
        "body": (
            "## Reference tables (condensed)\n\n"
            "### Table 2.1 — Allocation (1946)\n"
            "- British Indian Provinces (11): **292**\n"
            "- Princely States: **93**\n"
            "- Chief Commissioners’ Provinces (4): **4**\n"
            "- **Total: 389**\n\n"
            "### Table 2.2 — Election results (Jul–Aug 1946)\n"
            "Congress **208**; Muslim League **73**; Unionist Party / Unionist Muslims / "
            "Unionist SCs / Krishak–Praja / SCF / Sikhs (Non-Congress) / Communist — "
            "**1 each**; Independents **8**; **Total 296**.\n\n"
            "### Table 2.3 — Community-wise (1946)\n"
            "Hindus **163**; Muslims **80**; SCs **31**; Indian Christians **6**; "
            "Backward Tribes **6**; Sikhs **4**; Anglo-Indians **3**; Parsees **3**; "
            "**Total 296**.\n\n"
            "### Table 2.4 — Women members\n"
            "**15** women including Sarojini Naidu, Vijayalakshmi Pandit, "
            "Rajkumari Amrit Kaur, Sucheta Kripalani, Hansa Mehta, Dakshayani Velayudan, "
            "Begum Aizaz Rasul, and others.\n\n"
            "### Table 2.5 — Membership on 31 Dec 1947\n"
            "Provinces **229** + Indian States **70** = **299**. "
            "Largest provincial blocs: UP **55**, Madras **49**, Bihar **36**.\n\n"
            "### Table 2.6 — Sessions\n"
            "Eleven sessions from **9–23 Dec 1946** to **14–26 Nov 1949**; "
            "Assembly met again **24 Jan 1950** for signatures.\n\n"
            "### Table 2.7 — Time taken elsewhere\n"
            "- USA: 7 Articles — **< 4 months** (1787)\n"
            "- Canada: 147 — ~**2 years 6 months**\n"
            "- Australia: 128 — ~**9 years**\n"
            "- South Africa: 153 — **1 year**\n\n"
            "### Table 2.8 — Closing Articles\n"
            "- **393** — Short title\n"
            "- **394** — Commencement\n"
            "- **394-A** — Authoritative text in Hindi\n"
            "- **395** — Repeals"
        ),
        "articles": [
            ("Art. 393", "Short title."),
            ("Art. 394", "Commencement."),
            ("Art. 394-A", "Authoritative Hindi text."),
            ("Art. 395", "Repeals."),
        ],
        "visual_blocks": [
            {
                "id": "moc-tables-tree",
                "type": "tree",
                "title": "389 → 299 strength path",
                "root": {
                    "id": "total",
                    "label": "Cabinet Mission total",
                    "detail": "389 seats planned (1946)",
                    "children": [
                        {
                            "id": "bi",
                            "label": "British India 296",
                            "detail": "292 + 4 CC provinces → later 229 after partition",
                        },
                        {
                            "id": "ps",
                            "label": "Princely 93",
                            "detail": "Initially vacant → later 70 after joining",
                        },
                        {
                            "id": "final",
                            "label": "Post-partition Assembly",
                            "detail": "299 members (229 + 70) by 31 Dec 1947",
                        },
                    ],
                },
            },
            {
                "id": "moc-tables-compare",
                "type": "comparison",
                "title": "Closing Articles (Part XXII themes)",
                "columns": [
                    {
                        "id": "title-commence",
                        "heading": "Title & start",
                        "points": [
                            "393 — Short title",
                            "394 — Commencement (26 Nov / 26 Jan split)",
                        ],
                    },
                    {
                        "id": "hindi-repeals",
                        "heading": "Hindi & repeals",
                        "points": [
                            "394-A — Authoritative Hindi (58th Amendment)",
                            "395 — Repeals Independence Act & GoI Act 1935",
                        ],
                    },
                ],
            },
            {
                "id": "moc-tables-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "Drill 389→299, Congress 208 / League 73, 11 sessions, "
                    "and Art. 393–395 before full table dumps."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "moc-demand"),
    (HUB_SLUG, "parent", "moc-composition"),
    (HUB_SLUG, "parent", "moc-working"),
    (HUB_SLUG, "parent", "moc-committees"),
    (HUB_SLUG, "parent", "moc-enactment-enforcement"),
    (HUB_SLUG, "parent", "moc-experts-committee"),
    (HUB_SLUG, "parent", "moc-criticism-facts"),
    (HUB_SLUG, "parent", "moc-reference-tables"),
    ("moc-demand", "related", "moc-composition"),
    ("moc-composition", "related", "moc-criticism-facts"),
    ("moc-working", "related", "moc-experts-committee"),
    ("moc-working", "related", "historical-background"),
    ("moc-working", "related", "moc-enactment-enforcement"),
    ("moc-committees", "related", "moc-enactment-enforcement"),
    ("moc-experts-committee", "related", "moc-working"),
    ("moc-enactment-enforcement", "related", "moc-reference-tables"),
    ("moc-criticism-facts", "related", "moc-reference-tables"),
    ("moc-composition", "related", "moc-reference-tables"),
]

SAMPLE_PYQS = [
    (
        2012,
        "The members of the Constituent Assembly which drafted the Constitution of India were:",
        "Elected by the Legislative Assemblies of the then Provinces (indirect election under Cabinet Mission scheme).",
        ["moc-composition"],
    ),
    (
        2016,
        "Who among the following was the chairman of the Drafting Committee of the Indian Constitution?",
        "Dr. B.R. Ambedkar.",
        ["moc-committees"],
    ),
    (
        2018,
        "The Constitution of India was adopted by the Constituent Assembly on:",
        "26 November 1949 (enforcement/commencement of major part: 26 January 1950).",
        ["moc-enactment-enforcement"],
    ),
    (
        2009,
        "Who was the temporary Chairman of the Constituent Assembly?",
        "Dr. Sachchidananda Sinha (oldest member; French practice).",
        ["moc-working"],
    ),
]


class Command(BaseCommand):
    help = "Seed Making of the Constitution chapter (Laxmikanth Ch.2)."

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
                "title": "Making of the Constitution",
                "sort_order": 2,
                "book_ref": "Laxmikanth 8th Ed, Ch. 2",
                "summary": (
                    "Visual revision of Ch.2 — Constituent Assembly demand, composition, "
                    "working, committees, enactment/enforcement, criticism, and tables."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Making of the Constitution",
                "summary": (
                    "How India forged its Constitution — from demand for a Constituent "
                    "Assembly to adoption and commencement."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **constitutional forge** mental model and the chapter "
                    "**pillars**. Drill Demand → Composition → Working, then Committees and "
                    "Enactment/Enforcement. Finish with Criticism/Facts and Reference Tables. "
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
            ref="Laxmikanth Ch. 2",
            excerpt=(
                "Making of the Constitution — Constituent Assembly, Objectives Resolution, "
                "Drafting Committee, enactment, and commencement."
            ),
            sort_order=0,
        )

        moc_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=moc_slugs, source__subject=subject
        ).filter(
            target__slug__in=moc_slugs | {"historical-background"}
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
                f"Making of the Constitution chapter seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(SAMPLE_PYQS)} sample PYQs."
            )
        )
