"""Seed Laxmikanth Part IX — Other Constitutional Dimensions (visual revision chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from questions.models import PYQ
from subjects.models import Chapter, Section, Subject

HUB_SLUG = "other-constitutional-dimensions"
CHAPTER_SLUG = "other-constitutional-dimensions"

TOPIC_PILLARS = [
    {
        "id": "coops",
        "articles": "Ch.73 · Part IX-B",
        "label": "Co-operative Societies",
        "slug": "ocd-cooperative-societies",
        "detail": "97th Amendment — Art. 19 + 43-B + 243ZH–ZT; MSCS after 2021 SC.",
        "tone": "teal",
    },
    {
        "id": "lang",
        "articles": "Ch.74 · Part XVII",
        "label": "Official Language",
        "slug": "ocd-official-language",
        "detail": "Arts 343–351 · 8th Schedule · Official Languages Act · classical languages.",
        "tone": "olive",
    },
    {
        "id": "services",
        "articles": "Ch.75 · Part XIV",
        "label": "Public Services",
        "slug": "ocd-public-services",
        "detail": "AIS / Central / State · Arts 309–313 · Doctrine of Pleasure · Art. 311.",
        "tone": "gold",
    },
    {
        "id": "liability",
        "articles": "Ch.76 · Part XII",
        "label": "Rights & Liabilities of Govt",
        "slug": "ocd-rights-liabilities",
        "detail": "Arts 294–300A — property, contracts, suits, sovereign immunity.",
        "tone": "orange",
    },
    {
        "id": "classes",
        "articles": "Ch.77 · Part XVI",
        "label": "Special Provisions — Classes",
        "slug": "ocd-special-classes",
        "detail": "SC/ST/OBC/Anglo-Indian safeguards · Arts 330–342A · 104th/105th.",
        "tone": "terracotta",
    },
    {
        "id": "states",
        "articles": "Ch.78 · Part XXI",
        "label": "Special Provisions — States",
        "slug": "ocd-special-states",
        "detail": "Arts 371–371J — twelve states; boards, Governor roles, Parliament bars.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "ocd-mm",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Toolkit",
        "topic_label": "Other Constitutional Dimensions",
        "subject_label": "Laxmikanth Part IX",
        "relation_label": "Helps you master",
        "protects_from": [
            "Mixing Part IX (Panchayats) with Part IX-B (co-ops)",
            "Confusing official language with Eighth Schedule",
            "Doctrine of Pleasure without Art. 311 limits",
            "Treating Art. 300A as a Fundamental Right",
            "Mixing 371A–371J state-wise traps",
        ],
        "insight": (
            "Part IX of Laxmikanth is a residual constitutional toolkit — "
            "six high-frequency Prelims themes outside the main organs story."
        ),
    },
    {
        "id": "ocd-six-pillars",
        "type": "pillars",
        "title": "Six Part IX themes",
        "items": TOPIC_PILLARS,
    },
    {
        "id": "ocd-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision path",
        "body": (
            "Topic pass (1→6) → Master Comparisons → Final Revision cheat sheets. "
            "This is a visual revision layer — not a substitute for Laxmikanth."
        ),
    },
]

CLUSTERS = [
    # ── 1. Co-operative Societies ──────────────────────────────────────────
    {
        "title": "Co-operative Societies",
        "slug": "ocd-cooperative-societies",
        "sort_order": 1,
        "summary": (
            "97th CAA 2011 constitutionalised co-ops via FR + DPSP + Part IX-B; "
            "SC 2021 confines Part IX-B largely to multi-state co-ops."
        ),
        "body": (
            "## Constitutional Background\n\n"
            "Co-operative societies sit in **Entry 32, State List**. Growth was uneven — "
            "delayed elections, nominated boards, weak professionalism. The **97th Constitutional "
            "Amendment Act, 2011** gave constitutional status and protection.\n\n"
            "## Relevant Constitutional Articles\n\n"
            "- **Art. 19(1)(c)** — right to form co-operative societies (FR).\n"
            "- **Art. 43-B** — DPSP: voluntary formation, autonomous functioning, democratic "
            "control, professional management.\n"
            "- **Part IX-B · Arts 243ZH–243ZT** — The Co-operative Societies.\n"
            "- **243ZR** — Multi-state co-ops: read State Legislature/Act/Govt as "
            "Parliament / Central Act / Central Government.\n"
            "- **243ZS** — applies to UTs (President may exclude).\n"
            "- **243ZT** — inconsistent State laws continue ≤1 year from commencement "
            "(commenced **15 Feb 2012**).\n\n"
            "## Constitutional Amendments\n\n"
            "- **97th CAA, 2011** — the three-pronged constitutionalisation.\n\n"
            "## Objectives\n\n"
            "Democratic, autonomous, professional, economically sound co-ops; curb indefinite "
            "administrators; accountability to members; reduce outside interference.\n\n"
            "## Key Features\n\n"
            "- Incorporation / regulation / winding-up by **state legislature** on voluntary, "
            "democratic, member-economic, autonomous principles.\n"
            "- Board: max **21** directors; term **5 years**; **1 SC/ST + 2 women** seats "
            "(where members from those categories exist).\n"
            "- ≤**2 co-opted** experts (banking/management/finance etc.) — **no vote**, "
            "not eligible as office-bearers; functional directors **extra** to the 21.\n"
            "- Elections before term ends; electoral superintendence as State Act provides.\n"
            "- **Supersession / suspension ≤ 6 months** (co-op banks other than multi-state: "
            "≤ **1 year**). Grounds: persistent default, negligence, prejudicial acts, "
            "stalemate, election-body failure.\n"
            "- **No supersession** where there is no government shareholding / loan / "
            "financial assistance / guarantee.\n"
            "- Audit + AGM + returns within **6 months** of FY close; apex audit report "
            "laid before state legislature.\n"
            "- Member information rights; offences/penalties via State Act.\n\n"
            "## Institutional Framework\n\n"
            "- **State co-ops** → State Act / Registrar (state).\n"
            "- **Multi-State Co-operative Societies (MSCS)** → Central Act; Central Registrar.\n"
            "- Office-bearer = President, VP, chair, secretary, treasurer, etc.\n\n"
            "## Powers and Functions\n\n"
            "Legislature frames incorporation, elections, audit, offences; board manages; "
            "administrator (if superseded) must hold elections within the outer limit and "
            "hand back to elected board.\n\n"
            "## Important Committees/Commissions\n\n"
            "N/A as a standing constitutional commission — reform push came via state "
            "co-operative ministers’ conferences and the 97th Amendment Statement of Objects.\n\n"
            "## Important Judgments\n\n"
            "- **Rajendra N. Shah v. UoI (Gujarat HC, 2013)** — Part IX-B ultra vires for want "
            "of state ratification under Art. 368; Art. 19 + 43-B untouched.\n"
            "- **Union of India v. Rajendra N. Shah (SC, 2021)** — upheld HC except totality "
            "strike-down: **Part IX-B operative for multi-state co-ops** (and in UTs); "
            "state co-ops need ratification path.\n\n"
            "## Recent Constitutional or Legislative Developments\n\n"
            "- **Ministry of Cooperation (2021)** — dedicated Union ministry "
            "(post-8th-edition CA).\n"
            "- **MSCS (Amendment) Act, 2022** — governance / election / audit reforms for "
            "multi-state co-ops (post-book update).\n\n"
            "## Current Affairs Relevance\n\n"
            "SC 2021 holding + MSCS Act + Ministry of Cooperation are frequent Prelims/CA "
            "bridges; do not treat Part IX-B as fully binding on all state co-ops.\n\n"
            "## Frequently Asked UPSC Themes\n\n"
            "Three changes of 97th; max directors / reservation / supersession period; "
            "MSCS reading of 243ZR; SC 2021 operative extent.\n\n"
            "## Common Prelims Traps\n\n"
            "- Part **IX** (Panchayats) ≠ Part **IX-B** (co-ops).\n"
            "- Art. 19 insert ≠ Part IX-B surviving for all state co-ops after 2021.\n"
            "- Co-opted members **cannot** vote or be office-bearers.\n"
            "- Supersession ban when **no** govt financial stake.\n\n"
            "## Mains Value Additions\n\n"
            "Link federalism (Entry 32 + Art. 368 ratification) with democratic deepening; "
            "compare 73rd/74th local govt constitutionalisation with 97th co-op path; "
            "critique autonomy vs accountability after MSCS 2022."
        ),
        "articles": [
            ("Article 19(1)(c)", "Right to form co-operative societies (97th Amendment)."),
            ("Article 43-B", "DPSP — promote co-operative societies."),
            ("Arts 243ZH–243ZT", "Part IX-B — The Co-operative Societies."),
            ("Article 243ZR", "Application to multi-state co-operative societies."),
        ],
        "visual_blocks": [
            {
                "id": "ocd-coop-timeline",
                "type": "timeline",
                "title": "97th Amendment → SC 2021",
                "events": [
                    {
                        "id": "e2011",
                        "year": 2011,
                        "label": "97th CAA",
                        "detail": "Art. 19 + Art. 43-B + Part IX-B (243ZH–ZT).",
                    },
                    {
                        "id": "e2012",
                        "year": 2012,
                        "label": "Commencement",
                        "detail": "15 Feb 2012; states told to align Acts by Feb 2013.",
                    },
                    {
                        "id": "e2013",
                        "year": 2013,
                        "label": "Gujarat HC",
                        "detail": "Rajendra Shah — Part IX-B ultra vires (no ratification).",
                    },
                    {
                        "id": "e2021",
                        "year": 2021,
                        "label": "Supreme Court",
                        "detail": "Part IX-B lives for MSCS (+ UTs); Art. 19 & 43-B intact.",
                    },
                ],
            },
            {
                "id": "ocd-coop-tree",
                "type": "tree",
                "title": "Part IX-B article map",
                "root": {
                    "id": "ixb",
                    "label": "Part IX-B",
                    "detail": "Arts 243ZH–243ZT",
                    "children": [
                        {
                            "id": "gov",
                            "label": "Governance",
                            "detail": "ZI–ZL — incorporation, board, elections, supersession",
                            "children": [
                                {"id": "zi", "label": "243ZI", "detail": "Incorporation"},
                                {"id": "zj", "label": "243ZJ", "detail": "Board · ≤21 · 5 yrs"},
                                {"id": "zk", "label": "243ZK", "detail": "Elections"},
                                {"id": "zl", "label": "243ZL", "detail": "Supersession ≤6m"},
                            ],
                        },
                        {
                            "id": "acct",
                            "label": "Accountability",
                            "detail": "ZM–ZP — audit, AGM, info, returns",
                            "children": [
                                {"id": "zm", "label": "243ZM", "detail": "Audit"},
                                {"id": "zn", "label": "243ZN", "detail": "AGM"},
                                {"id": "zo", "label": "243ZO", "detail": "Member info"},
                                {"id": "zp", "label": "243ZP", "detail": "Returns"},
                            ],
                        },
                        {
                            "id": "scope",
                            "label": "Scope & offences",
                            "detail": "ZQ–ZT",
                            "children": [
                                {"id": "zq", "label": "243ZQ", "detail": "Offences"},
                                {"id": "zr", "label": "243ZR", "detail": "MSCS"},
                                {"id": "zs", "label": "243ZS", "detail": "UTs"},
                                {"id": "zt", "label": "243ZT", "detail": "Existing laws"},
                            ],
                        },
                    ],
                },
            },
            {
                "id": "ocd-coop-exam5",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "97th = 19 + 43-B + IX-B. Board ≤21; SC/ST 1 + women 2; supersession ≤6m "
                    "(no supersession if no govt stake). SC 2021 → Part IX-B mainly for MSCS. "
                    "Trap: Part IX ≠ IX-B."
                ),
            },
        ],
    },
    # ── 2. Official Language ───────────────────────────────────────────────
    {
        "title": "Official Language",
        "slug": "ocd-official-language",
        "sort_order": 2,
        "summary": (
            "Part XVII Arts 343–351 — Union/regional/judiciary language + special directives; "
            "8th Schedule; Official Languages Act; classical languages (now 11)."
        ),
        "body": (
            "## Constitutional Background\n\n"
            "**Part XVII** deals with official language in **Arts 343–351**, under four heads: "
            "Language of the Union; Regional languages; Language of the judiciary & texts of laws; "
            "Special directives.\n\n"
            "## Relevant Constitutional Articles\n\n"
            "- **343–344** — Union official language; Commission & Committee of Parliament.\n"
            "- **345–347** — State official language(s); inter-state/Union communication; "
            "language of a section of population.\n"
            "- **348–349** — SC/HC & authoritative texts; special procedure for certain language laws.\n"
            "- **350 / 350A / 350B** — grievance language; mother-tongue primary education; "
            "Special Officer for linguistic minorities.\n"
            "- **351** — directive to develop Hindi as lingua franca of India’s composite culture.\n"
            "- **Eighth Schedule** — 22 languages (originally 14).\n\n"
            "## Constitutional Amendments\n\n"
            "- **7th (1956)** — 350A / 350B (States Reorganisation).\n"
            "- **21st (1967)** — Sindhi · **71st (1992)** — Konkani, Manipuri, Nepali · "
            "**92nd (2003)** — Bodo, Dogri, Maithili, Santhali · **96th (2011)** — Oriya → Odia.\n\n"
            "## Objectives\n\n"
            "Hindi as Union official language with a managed English transition; protect "
            "linguistic minorities; enrich Hindi from Eighth Schedule languages; keep courts "
            "and authoritative legal texts workable.\n\n"
            "## Key Features\n\n"
            "**Union:** Hindi in Devanagari; **international form of Indian numerals**; "
            "English continues 1950–65; Parliament may extend English thereafter.\n\n"
            "**Official Languages Act, 1963:** English continues **indefinitely** with Hindi "
            "for Union purposes & Parliament; **1967 amendment** makes English **compulsory** "
            "in specified Central instruments (orders, reports laid before Parliament, contracts, etc.).\n\n"
            "**States (345):** may adopt any language **in use** in the state or Hindi — "
            "**not limited** to Eighth Schedule; until then English continues.\n\n"
            "**Link language:** English for Union↔non-Hindi states (OLA); Hindi+English "
            "translation when Hindi used with a non-Hindi state; states may agree Hindi inter se.\n\n"
            "**Art. 347:** President may direct official recognition of a language spoken by a "
            "substantial section of a state’s population.\n\n"
            "**Judiciary:** Until Parliament otherwise — SC & HC proceedings and authoritative "
            "Central/state legal texts in **English**. Governor + prior Presidential consent may "
            "allow Hindi/state language in HC proceedings (judgements still English unless "
            "OLA path + English translation). **SC hears only English** — Parliament has not "
            "authorised Hindi in SC.\n\n"
            "**Special directives:** representation in any used language (350); mother-tongue "
            "primary education for linguistic minorities (350A); Special Officer (350B); "
            "Hindi enrichment primarily from Sanskrit, secondarily other languages (351).\n\n"
            "## Institutional Framework\n\n"
            "- Official Language Commission (Art. 344) — **B.G. Kher**, 1955; report 1956.\n"
            "- Parliamentary committee — **G.B. Pant**, 1957.\n"
            "- Second Art. 344 commission (at 10 years) **not** appointed (1960).\n"
            "- **Committee of Parliament on Official Language** (OLA 1963) set up **1976** — "
            "30 MPs (20 LS + 10 RS); reviews Hindi progress; Chair conventionally Union Home Minister.\n"
            "- Department of Official Language, MHA.\n\n"
            "## Powers and Functions\n\n"
            "Commission recommends progressive Hindi use / English restrictions; Committee "
            "examines and reports to President; President may issue directions after considering "
            "state views; OLA Committee reports progress on Hindi in Central offices.\n\n"
            "## Important Committees/Commissions\n\n"
            "Kher Commission · Pant Committee · Committee of Parliament on Official Language "
            "(1976–).\n\n"
            "## Important Judgments\n\n"
            "N/A as a single leading SC ‘language case’ in the book chapter — Prelims focus is "
            "textual (Arts + OLA + Schedule). Flag linguistic minority / 350A litigation only "
            "if CA-driven.\n\n"
            "## Recent Constitutional or Legislative Developments\n\n"
            "**Classical languages (executive category, not Schedule):** Book lists 6 "
            "(Tamil 2004, Sanskrit 2005, Telugu & Kannada 2008, Malayalam 2013, Odia 2014). "
            "**2024 Cabinet** added Assamese, Bengali, Marathi, Pali, Prakrit → **11** classical "
            "languages (post-8th-edition CA).\n\n"
            "Benefits: international awards; Centre of Excellence; UGC professional chairs.\n"
            "Criteria: ~1500–2000 years antiquity; ancient literature heritage; original tradition; "
            "possible discontinuity with modern forms.\n\n"
            "## Current Affairs Relevance\n\n"
            "Classical-language expansions; Three-language formula debates; Hindi vs English "
            "in Union services exams; linguistic minority education (350A).\n\n"
            "## Frequently Asked UPSC Themes\n\n"
            "343 vs 345; Eighth Schedule count & amendment additions; OLA indefinite English; "
            "SC English-only; 350A/350B; classical vs Schedule languages.\n\n"
            "## Common Prelims Traps\n\n"
            "- Eighth Schedule ≠ list of **state official** languages.\n"
            "- Classical language ≠ constitutional Schedule status.\n"
            "- Devanagari numerals are **not** mandated for Union — international form is.\n"
            "- Art. 351 is a **directive**, not a justiciable FR.\n\n"
            "## Mains Value Additions\n\n"
            "Federal linguistic bargain (Hindi + English + regional autonomy); compare "
            "constitutional language policy with cultural classical-language policy; "
            "minority education (350A) as substantive equality."
        ),
        "articles": [
            ("Articles 343–344", "Language of the Union; Commission and Committee."),
            ("Articles 345–347", "Regional languages and minority-language recognition."),
            ("Articles 348–349", "Language of SC/HC and authoritative legal texts."),
            ("Articles 350–351", "Linguistic minorities and development of Hindi."),
            ("Eighth Schedule", "22 languages — representation in OL Commission; Hindi enrichment."),
        ],
        "visual_blocks": [
            {
                "id": "ocd-lang-tree",
                "type": "tree",
                "title": "Part XVII — four heads",
                "root": {
                    "id": "p17",
                    "label": "Part XVII Official Language",
                    "detail": "Arts 343–351",
                    "children": [
                        {
                            "id": "union",
                            "label": "Union (343–344)",
                            "detail": "Hindi + English transition; Commission & Committee",
                        },
                        {
                            "id": "reg",
                            "label": "Regional (345–347)",
                            "detail": "State official language; link language; Art. 347",
                        },
                        {
                            "id": "jud",
                            "label": "Judiciary & laws (348–349)",
                            "detail": "English default; HC/authoritative texts rules",
                        },
                        {
                            "id": "dir",
                            "label": "Special directives (350–351)",
                            "detail": "350 · 350A · 350B · 351 Hindi development",
                        },
                    ],
                },
            },
            {
                "id": "ocd-lang-compare",
                "type": "comparison",
                "title": "Official vs Schedule vs Classical",
                "columns": [
                    {
                        "id": "union",
                        "heading": "Union official",
                        "points": [
                            "Art. 343 — Hindi (Devanagari)",
                            "English via OLA 1963 (indefinite)",
                            "International numerals",
                        ],
                    },
                    {
                        "id": "state",
                        "heading": "State official",
                        "points": [
                            "Art. 345 — any language in use / Hindi",
                            "Not limited to 8th Schedule",
                            "English until legislature decides",
                        ],
                    },
                    {
                        "id": "sch8",
                        "heading": "8th Schedule",
                        "points": [
                            "22 languages",
                            "OL Commission representation",
                            "Hindi enrichment sources (351)",
                        ],
                    },
                    {
                        "id": "class",
                        "heading": "Classical (policy)",
                        "points": [
                            "Not a Schedule",
                            "11 languages (after 2024)",
                            "Awards / chairs / centres",
                        ],
                    },
                ],
            },
            {
                "id": "ocd-lang-exam5",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "343 Hindi Union · 345 state choice (≠ Schedule) · OLA keeps English forever · "
                    "SC = English only · 22 in 8th Schedule · Classical now 11 (2024). "
                    "Trap: classical ≠ Eighth Schedule."
                ),
            },
        ],
    },
    # ── 3. Public Services ─────────────────────────────────────────────────
    {
        "title": "Public Services",
        "slug": "ocd-public-services",
        "sort_order": 3,
        "summary": (
            "AIS, Central and State services under Part XIV — Arts 308–313; "
            "Doctrine of Pleasure (310) limited by Art. 311; Art. 312 for new AIS."
        ),
        "body": (
            "## Constitutional Background\n\n"
            "Public services classified as **All-India Services (AIS)**, **Central Services**, "
            "and **State Services**. Draft Constitution omitted AIS; Constituent Assembly "
            "inserted them. **Sardar Patel** = Father of All-India Services.\n\n"
            "## Relevant Constitutional Articles\n\n"
            "- **308** — interpretation (Part XIV application).\n"
            "- **309** — recruitment & conditions of service (Parliament / state legislature; "
            "interim rules by President / Governor).\n"
            "- **310** — tenure during pleasure of President / Governor (Doctrine of Pleasure).\n"
            "- **311** — safeguards against arbitrary dismissal / removal / reduction in rank.\n"
            "- **312** — All-India Services (incl. possible all-India judicial service).\n"
            "- **312A** (28th Amdt) — vary/revoke Crown-service conditions of pre-1950 officers.\n"
            "- **313** — transitional continuance of pre-1950 service laws.\n"
            "- **314** — repealed (28th Amdt).\n"
            "- Cross-ref **Part XIVA · 323A** — Administrative Tribunals (see Tribunals chapter).\n\n"
            "## Constitutional Amendments\n\n"
            "- **28th (1972)** — 312A; repeal 314.\n"
            "- **42nd (1976)** — dropped second opportunity at punishment stage under 311; "
            "enabled all-India judicial service provision (not yet created).\n\n"
            "## Objectives\n\n"
            "Professional, impartial administration; federal AIS cadre sharing; protect civil "
            "servants from arbitrary action while retaining executive control via pleasure doctrine.\n\n"
            "## Key Features\n\n"
            "**AIS (3):** IAS, IPS, IFoS (IFoS 1966). Common to Centre & states; recruited/trained "
            "by Centre; state cadres (Centre has no own AIS cadre); deputation tenure system; "
            "Class I / Group A; common rights & pay scales nationwide.\n\n"
            "- Control: **ultimate Centre, immediate state**; salaries/pensions by states; "
            "**disciplinary penalties only by Centre**.\n"
            "- Ministries: IAS — Personnel; IPS — Home; IFoS — Environment, Forest & Climate Change.\n"
            "- **26 cadres** incl. Assam–Meghalaya & AGMUT joint cadres.\n"
            "- Scales: junior → senior → super-time.\n"
            "- Promotion from state services: up to **33⅓%** senior AIS posts (AIS Act 1951); "
            "UPSC chair/member chairs state selection committee.\n\n"
            "**Art. 312:** Parliament may create new AIS **only after** Rajya Sabha resolution "
            "(⅔ present & voting) that it is expedient in national interest — federal safeguard. "
            "Resolution alone does **not** create the service; an Act is needed. IAS & IPS deemed "
            "created under 312. All-India judicial service: no post below district judge; such law "
            "≠ Art. 368 amendment.\n\n"
            "**Central Services:** exclusive Central jurisdiction; Groups A–D (ex Class I–IV; "
            "Third Pay Commission nomenclature). IFS is top Central service (after IAS in prestige; "
            "pay > IPS), MEA-managed.\n\n"
            "**State Services:** exclusive state jurisdiction; lower in hierarchy than AIS officers "
            "in the state; Groups A–D; gazetted usually A/B.\n\n"
            "**Doctrine of Pleasure (310):** defence & civil posts under Centre — pleasure of "
            "President; state civil posts — Governor. Limited compensation-contract exception for "
            "**new entrants** with special qualifications.\n\n"
            "**Art. 311 safeguards** (civil servants / AIS / civil posts — **not** defence):\n"
            "1. Not dismissed/removed by authority **subordinate** to appointing authority.\n"
            "2. Not dismissed/removed/reduced in rank without inquiry + charges + reasonable "
            "hearing — **except** (a) criminal conviction conduct, (b) impracticable inquiry "
            "(reasons recorded), (c) security of state (President/Governor satisfied).\n\n"
            "Dismissal ≠ removal: dismissal bars future govt employment; removal does not.\n\n"
            "## Institutional Framework\n\n"
            "UPSC / SPSC (recruitment); DoPT as central personnel agency; AIS Act 1951 rules "
            "with state consultation; CAT/SAT under Art. 323A for service disputes "
            "(cross-ref Tribunals).\n\n"
            "## Powers and Functions\n\n"
            "Legislatures regulate recruitment/conditions (309); President/Governor hold pleasure "
            "tenure (310); disciplinary inquiry architecture (311); Parliament creates AIS after "
            "RS recommendation (312).\n\n"
            "## Important Committees/Commissions\n\n"
            "Pay Commissions (classification changes); UPSC role in AIS promotion committees.\n\n"
            "## Important Judgments\n\n"
            "SC on ‘reasonable opportunity’ under 311: know charges, cross-examine, get inquiry "
            "report before disciplinary authority decides. Link service disputes to **Chandra Kumar** "
            "/ CAT path in Tribunals chapter.\n\n"
            "## Recent Constitutional or Legislative Developments\n\n"
            "No new AIS created despite past proposals (e.g. medical/engineering AIS ideas); "
            "all-India judicial service remains unimplemented.\n\n"
            "## Current Affairs Relevance\n\n"
            "Lateral entry; AIS cadre management; Art. 311 misuse debates; tribunalisation of "
            "service disputes.\n\n"
            "## Frequently Asked UPSC Themes\n\n"
            "Who creates AIS; RS ⅔ resolution; 310 vs 311; 311 exceptions; dismissal vs removal; "
            "IFS vs AIS ranking; IFoS year.\n\n"
            "## Common Prelims Traps\n\n"
            "- Rajya Sabha resolution **≠** creation of AIS.\n"
            "- Pleasure doctrine **≠** unfettered for civil servants — 311 applies.\n"
            "- 311 inquiry safeguard **does not** cover defence services.\n"
            "- 42nd removed second representation against proposed penalty.\n\n"
            "## Mains Value Additions\n\n"
            "AIS as ‘steel frame’ + federal cement; balance between pleasure doctrine and "
            "natural justice; compare AIS dual control with pure Central/State services."
        ),
        "articles": [
            ("Article 309", "Recruitment and conditions of service."),
            ("Article 310", "Doctrine of Pleasure — tenure of office."),
            ("Article 311", "Safeguards on dismissal, removal, reduction in rank."),
            ("Article 312", "All-India Services — RS resolution + Parliamentary Act."),
            ("Article 312A", "Power to vary/revoke conditions of certain pre-1950 officers."),
        ],
        "visual_blocks": [
            {
                "id": "ocd-svc-compare",
                "type": "comparison",
                "title": "AIS vs Central vs State Services",
                "columns": [
                    {
                        "id": "ais",
                        "heading": "All-India Services",
                        "points": [
                            "IAS · IPS · IFoS",
                            "Common to Centre & states",
                            "State cadres; Centre deputation",
                            "Ultimate control: Centre",
                            "Discipline: Centre only",
                        ],
                    },
                    {
                        "id": "central",
                        "heading": "Central Services",
                        "points": [
                            "Exclusive Central jurisdiction",
                            "Groups A–D",
                            "IFS top Central service",
                            "DoPT / parent ministries",
                            "Functional / technical posts",
                        ],
                    },
                    {
                        "id": "state",
                        "heading": "State Services",
                        "points": [
                            "Exclusive state jurisdiction",
                            "Below AIS in state hierarchy",
                            "Groups A–D; gazetted A/B",
                            "Feed ≤33⅓% AIS senior posts",
                            "State-named cadres",
                        ],
                    },
                ],
            },
            {
                "id": "ocd-svc-311",
                "type": "flowchart",
                "title": "Art. 311 — can inquiry be skipped?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Civil servant facing dismissal / removal / reduction?",
                        "detail": "311 applies to civil services / AIS / civil posts — not defence.",
                        "options": [
                            {"label": "Criminal conviction conduct", "next": "skip"},
                            {"label": "Inquiry not reasonably practicable", "next": "skip"},
                            {"label": "Security of state (Pres/Gov)", "next": "skip"},
                            {"label": "None of the above", "next": "inquiry"},
                        ],
                    },
                    {
                        "id": "skip",
                        "label": "Inquiry safeguard not required",
                        "detail": "Still cannot be dismissed by subordinate authority (first limb).",
                    },
                    {
                        "id": "inquiry",
                        "label": "Full inquiry + hearing required",
                        "detail": "Charges, defence, inquiry report before penalty (post-42nd: no second chance).",
                    },
                ],
            },
            {
                "id": "ocd-svc-exam5",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "AIS = IAS/IPS/IFoS. New AIS: RS ⅔ resolution → Parliament Act (not resolution alone). "
                    "310 pleasure · 311 two shields + 3 exceptions. Dismissal bars future employment; "
                    "removal does not. Trap: IFS is Central, not AIS."
                ),
            },
        ],
    },
    # ── 4. Rights and Liabilities of the Government ────────────────────────
    {
        "title": "Rights and Liabilities of the Government",
        "slug": "ocd-rights-liabilities",
        "sort_order": 4,
        "summary": (
            "Arts 294–300A — Union/state as juristic persons: property, contracts (299), "
            "suits (300), and property as legal right (300A)."
        ),
        "body": (
            "## Constitutional Background\n\n"
            "**Arts 294–300** (Part XII) make the Union and states **juristic persons** for "
            "property, contracts, rights, liabilities, obligations and suits. **Art. 300A** "
            "(44th Amdt) — no person deprived of property save by authority of law "
            "(legal right, **not** FR).\n\n"
            "## Relevant Constitutional Articles\n\n"
            "- **294** — succession to property, assets, rights, liabilities.\n"
            "- **295** — succession in other cases (princely states etc. — related succession).\n"
            "- **296** — escheat, lapse, bona vacantia → state if situated there, else Union.\n"
            "- **297** — things of value in territorial waters, continental shelf, EEZ → **Union**.\n"
            "- **298** — executive power to carry on trade/business; acquire, hold, dispose property.\n"
            "- **299** — government contracts — form & personal immunity.\n"
            "- **300** — suits by or against Government (Union of India / State of X).\n"
            "- **300A** — right to property (legal right).\n\n"
            "## Constitutional Amendments\n\n"
            "- **44th (1978)** — repealed FR to property (19(1)(f), 31); inserted **300A**; "
            "ended general constitutional compensation duty except "
            "(a) minority educational institution property, "
            "(b) land under personal cultivation within ceiling limits.\n\n"
            "## Objectives\n\n"
            "Clear proprietary succession at commencement; enable government as contracting "
            "and suing entity; balance sovereign functions with citizen remedies; retain "
            "property protection as ordinary legal right.\n\n"
            "## Key Features\n\n"
            "**Property:** Dominion/province/princely assets → Union/corresponding state; "
            "escheat/lapse/bona vacantia rules; sea-wealth exclusively Union "
            "(**12 nm** territorial waters; **200 nm** EEZ).\n\n"
            "**Compulsory acquisition:** Parliament & states may legislate; compensation "
            "constitutional mandate narrowed after 44th (two exceptions above).\n\n"
            "**Art. 299 contracts — three mandatory conditions:**\n"
            "1. Expressed to be made by President / Governor.\n"
            "2. Executed on behalf of President / Governor.\n"
            "3. Executed by authorised person/manner.\n"
            "Non-compliance → **void**. President/Governor/officer not personally liable; "
            "government remains contractually suable (ordinary contract law).\n\n"
            "**Art. 300 suits:** sue/be sued as **Union of India** or **State of …** — not "
            "‘Government of …’. Liability continuum from pre-Constitution position until "
            "Parliament/state law otherwise (no general law yet).\n\n"
            "**Contracts:** government suable like private party.\n"
            "**Torts:** historically suable for **non-sovereign** functions only; immunity for "
            "sovereign functions (P&O 1861; Kasturilal 1964). Later SC narrowed sovereign "
            "immunity (e.g. Nagendra Rao 1994) — modern approach: State rarely above law.\n\n"
            "## Institutional Framework\n\n"
            "N/A as a single commission — doctrine developed through Constitution + case law.\n\n"
            "## Powers and Functions\n\n"
            "Executive trade/business & property dealings (298); contracting under 299 form; "
            "litigation personality under 300; legislative acquisition powers subject to 300A.\n\n"
            "## Important Committees/Commissions\n\n"
            "N/A — doctrine is constitutional/judicial.\n\n"
            "## Important Judgments\n\n"
            "- **P&O Steam Navigation Co. (1861)** — sovereign vs non-sovereign functions.\n"
            "- **Kasturilal v. State of UP (1964)** — reaffirmed sovereign immunity (later "
            "weakened in effect).\n"
            "- **N. Nagendra Rao (1994)** — criticises sovereign immunity; State liable for "
            "negligent acts of servants in most modern functions.\n\n"
            "## Recent Constitutional or Legislative Developments\n\n"
            "Land acquisition statutes evolve under ordinary law + 300A; no return of property "
            "as FR.\n\n"
            "## Current Affairs Relevance\n\n"
            "Govt contract formalities; land acquisition challenges under 300A; tort claims "
            "against State; EEZ/resource disputes (297).\n\n"
            "## Frequently Asked UPSC Themes\n\n"
            "299 mandatory form; 300 juristic name; 300A ≠ FR; 297 sea-wealth; 44th property "
            "shift; sovereign immunity trajectory.\n\n"
            "## Common Prelims Traps\n\n"
            "- **300A is not a Fundamental Right.**\n"
            "- Sue as **Union of India**, not ‘Government of India’.\n"
            "- Art. 299 defects make contract **unenforceable**, not a personal liability of President.\n"
            "- Coastal state ≠ owner of EEZ resources (297 → Union).\n\n"
            "## Mains Value Additions\n\n"
            "From ‘King can do no wrong’ to constitutional State liability; property as legal "
            "right vs FR era; contract form as rule-of-law check on executive."
        ),
        "articles": [
            ("Articles 294–298", "Property succession, escheat, sea-wealth, executive trade."),
            ("Article 299", "Government contracts — mandatory form; personal immunity."),
            ("Article 300", "Suits by or against the Union / states."),
            ("Article 300A", "Right to property — legal right, not FR (44th Amendment)."),
        ],
        "visual_blocks": [
            {
                "id": "ocd-liab-tree",
                "type": "tree",
                "title": "Arts 294–300A map",
                "root": {
                    "id": "prop",
                    "label": "Govt as juristic person",
                    "detail": "Part XII slice",
                    "children": [
                        {
                            "id": "assets",
                            "label": "Property (294–298)",
                            "detail": "Succession · escheat · sea-wealth · trade",
                        },
                        {
                            "id": "contract",
                            "label": "Contracts (299)",
                            "detail": "3 mandatory conditions · no personal liability",
                        },
                        {
                            "id": "suits",
                            "label": "Suits (300)",
                            "detail": "Union of India / State of X",
                        },
                        {
                            "id": "300a",
                            "label": "Property right (300A)",
                            "detail": "Authority of law — not Part III",
                        },
                    ],
                },
            },
            {
                "id": "ocd-liab-flow",
                "type": "flowchart",
                "title": "Is the government contract valid?",
                "root": "c1",
                "steps": [
                    {
                        "id": "c1",
                        "label": "Expressed to be made by President / Governor?",
                        "options": [
                            {"label": "No", "next": "void"},
                            {"label": "Yes", "next": "c2"},
                        ],
                    },
                    {
                        "id": "c2",
                        "label": "Executed on behalf of President / Governor?",
                        "options": [
                            {"label": "No", "next": "void"},
                            {"label": "Yes", "next": "c3"},
                        ],
                    },
                    {
                        "id": "c3",
                        "label": "Executed by authorised person / manner?",
                        "options": [
                            {"label": "No", "next": "void"},
                            {"label": "Yes", "next": "ok"},
                        ],
                    },
                    {
                        "id": "ok",
                        "label": "Valid Art. 299 contract",
                        "detail": "Government suable; President/Governor/officer not personally liable.",
                    },
                    {
                        "id": "void",
                        "label": "Void / unenforceable",
                        "detail": "Mandatory conditions failed — nullified in courts.",
                    },
                ],
            },
            {
                "id": "ocd-liab-exam5",
                "type": "callout",
                "tone": "trap",
                "title": "Exam in 5 Minutes",
                "body": (
                    "299 = three mandatory form rules. 300 = sue as Union of India / State of X. "
                    "300A ≠ FR. 297 sea-wealth → Union (12 nm / 200 nm). "
                    "Sovereign immunity diluted after Kasturilal — cite Nagendra Rao."
                ),
            },
        ],
    },
    # ── 5. Special Provisions Relating to Certain Classes ──────────────────
    {
        "title": "Special Provisions Relating to Certain Classes",
        "slug": "ocd-special-classes",
        "sort_order": 5,
        "summary": (
            "Part XVI Arts 330–342A — political, service, educational and commission "
            "safeguards for SCs, STs, OBCs and (historically) Anglo-Indians."
        ),
        "body": (
            "## Constitutional Background\n\n"
            "To realise Preamble ideals of **equality and justice**, Part XVI "
            "(**Arts 330–342A**) creates special provisions for **SCs, STs, Backward Classes "
            "and Anglo-Indians** — political reservation/representation, services, education "
            "grants, and national commissions.\n\n"
            "Classify as **permanent vs temporary** and **protective vs developmental**.\n\n"
            "## Relevant Constitutional Articles\n\n"
            "- **330 / 332** — SC/ST reservation in Lok Sabha / State Assemblies.\n"
            "- **331 / 333** — Anglo-Indian nomination (now ceased — see 104th).\n"
            "- **334** — time limit for reservation/special representation.\n"
            "- **335** — SC/ST claims to services (efficiency caveat) + 82nd relaxation path.\n"
            "- **336 / 337** — Anglo-Indian services/grants (expired on diminution basis by 1960).\n"
            "- **338 / 338A / 338B** — NCSC, NCST, NCBC.\n"
            "- **339** — Union control re Scheduled Areas / ST welfare; obligatory commissions.\n"
            "- **340** — Commission to investigate backward classes.\n"
            "- **341 / 342 / 342A** — Presidential lists for SC, ST, SEBCs (Central List).\n\n"
            "## Constitutional Amendments\n\n"
            "- **82nd (2000)** — relaxation of marks/standards for SC/ST promotion reservation.\n"
            "- **89th (2003)** — bifurcate combined SC/ST commission → NCSC + NCST.\n"
            "- **102nd (2018)** — constitutional NCBC (338B); SEBC Central List architecture.\n"
            "- **104th (2019)** — SC/ST political reservation extended to **2030**; "
            "**Anglo-Indian nomination ended** (ceased 25 Jan 2020).\n"
            "- **105th (2021)** — restored states’ power to prepare own SEBC/OBC lists; "
            "clarified Central List for Union purposes.\n\n"
            "## Objectives\n\n"
            "Protect from injustice/exploitation; promote socio-economic interests; ensure "
            "political voice and fair share in services/education.\n\n"
            "## Key Features\n\n"
            "**Specification:** Constitution does **not** enumerate castes/tribes — President "
            "notifies state/UT-wise SC/ST lists (Governor consulted for states); "
            "**only Parliament** can amend lists. Anglo-Indian is **constitutionally defined** "
            "(European male-line descent + domicile).\n\n"
            "**OBCs / SEBCs:** 102nd/105th — President specifies Central List; states/UTs may "
            "maintain distinct lists **by law** after 105th.\n\n"
            "**Political:** SC/ST reserved seats by population ratio; originally 10 years, "
            "extended decennially → **104th until 2030**. Anglo-Indian LS (2) / SLA (1) "
            "nomination **discontinued** by 104th.\n\n"
            "**Services:** Art. 335 claims + efficiency; 82nd enables relaxation for promotion "
            "reservation.\n\n"
            "**Education/grants:** historical Anglo-Indian special grants ended 1960; ongoing "
            "SC/ST educational measures via statutes + DPSP/FR equality framework.\n\n"
            "## Institutional Framework\n\n"
            "- **NCSC (338)** · **NCST (338A)** · **NCBC (338B)** — investigate safeguards; "
            "report to President → Parliament with action taken.\n"
            "- NCSC also covers Anglo-Indian safeguards.\n"
            "- Scheduled Areas/ST welfare commissions: **U.N. Dhebar (1960–61)**; "
            "**Dilip Singh Bhuria (2002–04)**.\n"
            "- BC investigation commissions: **Kaka Kalelkar (1953–55)**; "
            "**B.P. Mandal (1979–80)** → 27% OBC jobs (1990).\n\n"
            "## Powers and Functions\n\n"
            "Commissions investigate & recommend; President/Parliament control lists; "
            "Centre may direct states on ST welfare schemes (339).\n\n"
            "## Important Committees/Commissions\n\n"
            "Kalelkar · Mandal · Dhebar · Bhuria · NCSC/NCST/NCBC.\n\n"
            "## Important Judgments\n\n"
            "Reservation jurisprudence largely lives in FR/equality case law (Indra Sawhney, "
            "etc.) — cross-link; Part XVI supplies institutional/political scaffolding. "
            "105th responded to federal list disputes after 102nd.\n\n"
            "## Recent Constitutional or Legislative Developments\n\n"
            "104th (2030 + Anglo-Indian end); 105th (state OBC lists); EWS (103rd) is related "
            "equality theme but **not** Part XVI class machinery — light cross-ref only.\n\n"
            "## Current Affairs Relevance\n\n"
            "Census/delimitation & reservation; state vs Central OBC lists; ST commission "
            "reports; sub-categorisation debates.\n\n"
            "## Frequently Asked UPSC Themes\n\n"
            "Who notifies SC/ST lists; 104th twin effects; 102nd vs 105th; 338/338A/338B; "
            "Mandal; Anglo-Indian definition & end of nomination.\n\n"
            "## Common Prelims Traps\n\n"
            "- President notifies; **Parliament** amends SC/ST lists.\n"
            "- 104th **extended** SC/ST seats but **ended** Anglo-Indian nomination.\n"
            "- 105th ≠ repeal of NCBC — it clarifies list federalism.\n"
            "- Anglo-Indian service reservations ended long ago (by 1960).\n\n"
            "## Mains Value Additions\n\n"
            "Protective discrimination as substantive equality; temporary political "
            "reservations vs permanent commission oversight; cooperative federalism after 105th."
        ),
        "articles": [
            ("Articles 330–334", "Political reservation / Anglo-Indian representation & time limit."),
            ("Article 335", "SC/ST claims to services and posts."),
            ("Articles 338–338B", "NCSC, NCST, NCBC."),
            ("Articles 341–342A", "Presidential lists for SCs, STs, SEBCs."),
        ],
        "visual_blocks": [
            {
                "id": "ocd-class-pillars",
                "type": "pillars",
                "title": "Safeguard categories",
                "items": [
                    {
                        "id": "pol",
                        "articles": "330–334",
                        "label": "Political",
                        "slug": "ocd-special-classes",
                        "detail": "LS/SLA reserved seats; Anglo-Indian nomination (ended).",
                        "tone": "teal",
                    },
                    {
                        "id": "svc",
                        "articles": "335–336",
                        "label": "Services",
                        "slug": "ocd-special-classes",
                        "detail": "SC/ST claims + 82nd relaxation; historic AI posts.",
                        "tone": "olive",
                    },
                    {
                        "id": "edu",
                        "articles": "337+",
                        "label": "Educational",
                        "slug": "ocd-special-classes",
                        "detail": "Grants / access measures; AI special grants ended 1960.",
                        "tone": "gold",
                    },
                    {
                        "id": "comm",
                        "articles": "338–340",
                        "label": "Commissions",
                        "slug": "ocd-special-classes",
                        "detail": "NCSC · NCST · NCBC · BC & ST area commissions.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "ocd-class-compare",
                "type": "comparison",
                "title": "SC / ST / OBC / Anglo-Indian — quick contrast",
                "columns": [
                    {
                        "id": "scst",
                        "heading": "SC & ST",
                        "points": [
                            "Lists: President; amend: Parliament",
                            "Political reservation till 2030",
                            "NCSC / NCST",
                            "Art. 335 + 82nd",
                        ],
                    },
                    {
                        "id": "obc",
                        "heading": "OBC / SEBC",
                        "points": [
                            "Central List (102nd/105th)",
                            "State lists by law (105th)",
                            "NCBC (338B)",
                            "Mandal 27% jobs legacy",
                        ],
                    },
                    {
                        "id": "ai",
                        "heading": "Anglo-Indian",
                        "points": [
                            "Constitutionally defined",
                            "Nomination ended (104th)",
                            "Service/grant prefs ended ~1960",
                            "NCSC also covers AI",
                        ],
                    },
                ],
            },
            {
                "id": "ocd-class-exam5",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "104th = SC/ST seats → 2030 + Anglo-Indian nomination gone. "
                    "102nd NCBC · 105th state OBC lists. President notifies SC/ST; Parliament amends. "
                    "Trap: conflating 104th’s two opposite effects."
                ),
            },
        ],
    },
    # ── 6. Special Provisions for Some States ──────────────────────────────
    {
        "title": "Special Provisions for Some States",
        "slug": "ocd-special-states",
        "sort_order": 6,
        "summary": (
            "Arts 371–371J in Part XXI — special arrangements for twelve states: "
            "development boards, tribal/custom protections, Governor responsibilities."
        ),
        "body": (
            "## Constitutional Background\n\n"
            "Originally no special state provisions. **Arts 371–371J** (Part XXI) added by "
            "amendments after reorganisation/statehood to meet regional backwardness, tribal "
            "cultural protection, law-and-order, or local employment/education aspirations. "
            "Cover **12 states:** Maharashtra, Gujarat, Nagaland, Assam, Manipur, Andhra Pradesh, "
            "Telangana, Sikkim, Mizoram, Arunachal Pradesh, Goa, Karnataka.\n\n"
            "## Relevant Constitutional Articles\n\n"
            "- **371** — Maharashtra & Gujarat (development boards).\n"
            "- **371A** — Nagaland (Parliament consent + Governor LoO + Tuensang).\n"
            "- **371B** — Assam (tribal areas Assembly committee).\n"
            "- **371C** — Manipur (Hill Areas committee; Governor report).\n"
            "- **371D / 371E** — AP (& TS for 371D) — local cadres/education/tribunal; "
            "Central University in AP.\n"
            "- **371F** — Sikkim (Assembly size, sectional seats, Governor peace role).\n"
            "- **371G** — Mizoram (Parliament consent like NL; min 40 MLAs).\n"
            "- **371H** — Arunachal Pradesh (Governor LoO; min 30 MLAs).\n"
            "- **371I** — Goa (min 30 MLAs).\n"
            "- **371J** — Karnataka (Hyderabad-Karnataka / Kalyana Karnataka board & reservations).\n\n"
            "## Constitutional Amendments\n\n"
            "Inserted/expanded via successive amendments (statehood & reorganisation). "
            "**98th (2012)** inserted **371J**. **AP Reorganisation Act 2014** extended "
            "**371D to Telangana**.\n\n"
            "## Objectives\n\n"
            "Equitable regional development; protect customary law/land; special LoO "
            "responsibility; local preference in jobs/education; preserve identity after merger "
            "(e.g. Sikkim).\n\n"
            "## Key Features (state-wise)\n\n"
            "**371 MH/GJ:** Governor special responsibility — separate development boards "
            "(Vidarbha/Marathwada/rest MH; Saurashtra/Kutch/rest GJ); annual board report to "
            "Assembly; equitable funds, technical education, state-service opportunities.\n\n"
            "**371A NL:** Parliament Acts on Naga religion/social practice, customary law, "
            "customary justice, **land & resources** apply only if Assembly so decides. "
            "Governor special LoO responsibility (individual judgment; ceases when President "
            "directs). Tuensang regional council (35) + transitional special admin rules.\n\n"
            "**371B AS:** President may provide Assembly committee of tribal-area members "
            "(+ others specified).\n\n"
            "**371C MN:** Hill Areas Assembly committee; Governor special responsibility & "
            "annual report to President; Centre may direct state on Hill Areas admin.\n\n"
            "**371D AP/TS:** equitable opportunities in public employment & education by "
            "parts of state; local cadres; Administrative Tribunal outside HC (SC retains "
            "jurisdiction). **371E:** Parliament may establish Central University in AP.\n\n"
            "**371F SK:** Assembly ≥30; 1 LS seat; Parliament may reserve sectional seats / "
            "delimitation; Governor special responsibility for peace & equitable advancement "
            "(discretion subject to Presidential directions); President may extend other "
            "states’ laws to Sikkim.\n\n"
            "**371G MZ:** Parliament consent for Mizo religion/social practice, customary law, "
            "customary justice, **ownership & transfer of land** (note: not ‘resources’ like "
            "371A). Assembly ≥40.\n\n"
            "**371H AR:** Governor LoO special responsibility (individual judgment); Assembly ≥30.\n\n"
            "**371I GA:** Assembly ≥30.\n\n"
            "**371J KA (98th):** Hyderabad-Karnataka (now **Kalyana Karnataka**) development "
            "board; equitable funds; reservation in regional education/vocational seats and "
            "state posts for region’s persons.\n\n"
            "## Institutional Framework\n\n"
            "Regional/development boards; Assembly committees (AS/MN); Tuensang regional "
            "council; AP/TS Administrative Tribunal under 371D; Governor special-responsibility "
            "channels.\n\n"
            "## Powers and Functions\n\n"
            "President authorises boards/committees/local cadres; Governors exercise specified "
            "discretion/individual judgment; Assemblies gatekeep certain Parliamentary laws "
            "(NL/MZ); Parliament frames Sikkim sectional representation & AP Central University.\n\n"
            "## Important Committees/Commissions\n\n"
            "State development boards / regional councils as above — not a single national "
            "commission for all 371s.\n\n"
            "## Important Judgments\n\n"
            "Prelims-heavy textual area; case law usually state-specific (land/custom, local "
            "cadre). Prefer article→state mapping over case laundry lists unless CA-driven.\n\n"
            "## Recent Constitutional or Legislative Developments\n\n"
            "371D → Telangana (2014); 371J (2012); Hyderabad-Karnataka renamed "
            "**Kalyana Karnataka** in state usage (CA label).\n\n"
            "## Current Affairs Relevance\n\n"
            "Sixth Schedule / tribal autonomy debates vs 371A/G; regional board funding; "
            "local reservation challenges; Northeast special provisions in federal discourse.\n\n"
            "## Frequently Asked UPSC Themes\n\n"
            "Which Article for which state; 371A vs 371G differences; Governor special "
            "responsibilities; 371J year/region; min Assembly sizes (SK/MZ/AR/GA).\n\n"
            "## Common Prelims Traps\n\n"
            "- **371A includes land & resources; 371G says land only.**\n"
            "- 371D applies to **AP and Telangana**; 371E Central University is **AP**.\n"
            "- Goa 371I is only minimum Assembly size — not a tribal Parliament bar.\n"
            "- Art. 370 repeal ≠ deletion of 371–371J.\n\n"
            "## Mains Value Additions\n\n"
            "Asymmetric federalism; cultural autonomy vs national integration; development "
            "boards as equity tools; Governor’s special responsibilities vs aid-and-advice norm."
        ),
        "articles": [
            ("Article 371", "Special provisions — Maharashtra & Gujarat."),
            ("Article 371A", "Special provisions — Nagaland."),
            ("Articles 371B–371C", "Assam tribal committee; Manipur Hill Areas."),
            ("Articles 371D–371E", "AP/Telangana local cadres; Central University in AP."),
            ("Articles 371F–371J", "Sikkim, Mizoram, Arunachal, Goa, Karnataka."),
        ],
        "visual_blocks": [
            {
                "id": "ocd-states-matrix",
                "type": "comparison",
                "title": "Arts 371A–371J — state snapshot",
                "columns": [
                    {
                        "id": "a",
                        "heading": "371A · NL",
                        "points": [
                            "Assembly consent for 4 subjects",
                            "Includes land & resources",
                            "Governor LoO role",
                            "Tuensang council",
                        ],
                    },
                    {
                        "id": "g",
                        "heading": "371G · MZ",
                        "points": [
                            "Assembly consent (similar 4)",
                            "Land (not ‘resources’)",
                            "No Tuensang-type council",
                            "Assembly ≥40",
                        ],
                    },
                    {
                        "id": "d",
                        "heading": "371D · AP/TS",
                        "points": [
                            "Local cadres / education",
                            "Equitable opportunities",
                            "State Admin Tribunal",
                            "TS via 2014 Act",
                        ],
                    },
                    {
                        "id": "j",
                        "heading": "371J · KA",
                        "points": [
                            "98th CAA 2012",
                            "Kalyana Karnataka board",
                            "Education seat reservation",
                            "State post reservation",
                        ],
                    },
                ],
            },
            {
                "id": "ocd-states-gov",
                "type": "tree",
                "title": "Governor special responsibilities (select)",
                "root": {
                    "id": "gov",
                    "label": "Governor special roles",
                    "children": [
                        {
                            "id": "mhgj",
                            "label": "371 MH/GJ",
                            "detail": "Development boards & equitable allocation",
                        },
                        {
                            "id": "nl",
                            "label": "371A NL",
                            "detail": "Law & order (individual judgment)",
                        },
                        {
                            "id": "mn",
                            "label": "371C MN",
                            "detail": "Hill Areas committee functioning",
                        },
                        {
                            "id": "sk",
                            "label": "371F SK",
                            "detail": "Peace & equitable sectional advancement",
                        },
                        {
                            "id": "ar",
                            "label": "371H AR",
                            "detail": "Law & order (individual judgment)",
                        },
                        {
                            "id": "ka",
                            "label": "371J KA",
                            "detail": "Hyderabad-Karnataka / Kalyana Karnataka board",
                        },
                    ],
                },
            },
            {
                "id": "ocd-states-exam5",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Mnemonic: A-B-C-D-E-F-G-H-I-J = NL-AS-MN-AP/TS-AP Univ-SK-MZ-AR-GA-KA. "
                    "371A land+resources · 371G land only. 371J = 98th / Kalyana Karnataka. "
                    "Min MLAs: SK/AR/GA ≥30; MZ ≥40."
                ),
            },
        ],
    },
]

# Extend with master comparisons + final revision (clusters 7–8)
CLUSTERS.extend(
    [
        {
            "title": "Master Comparisons",
            "slug": "ocd-master-comparisons",
            "sort_order": 7,
            "summary": (
                "Side-by-side matrices: language layers, services, FR vs special provisions, "
                "371A–J, safeguards, and reservation snapshots."
            ),
            "body": (
                "## How to use this cluster\n\n"
                "Scan each comparison visual once, then re-test yourself from the Final Revision "
                "cheat sheets. These matrices are Prelims filters — not full notes.\n\n"
                "### Official Language vs Regional Languages\n"
                "Union (343 + OLA English) ≠ state choice (345) ≠ Eighth Schedule (22) ≠ classical "
                "(policy category, now 11).\n\n"
                "### Union vs State vs All-India Services\n"
                "Jurisdiction, cadre, discipline, and control differ — IFS is Central, not AIS.\n\n"
                "### Fundamental Rights vs Special Provisions\n"
                "Part III justiciable rights for all persons/citizens vs Part XVI / 371s targeted "
                "institutional & political arrangements for classes/states.\n\n"
                "### Safeguard categories\n"
                "Political · Educational · Service · Linguistic · Cultural/customary (371A/G).\n\n"
                "### Reservation snapshot\n"
                "SC/ST political seats till 2030; OBC jobs via statutes + lists; Anglo-Indian "
                "nomination ended; EWS is 103rd equality theme (cross-ref, not Part XVI engine)."
            ),
            "articles": [],
            "visual_blocks": [
                {
                    "id": "ocd-cmp-lang",
                    "type": "comparison",
                    "title": "Official Language vs Regional vs Schedule vs Classical",
                    "columns": [
                        {
                            "id": "ol",
                            "heading": "Union official",
                            "points": [
                                "Art. 343 Hindi",
                                "OLA English indefinite",
                                "Union purposes + Parliament",
                            ],
                        },
                        {
                            "id": "rl",
                            "heading": "Regional / state",
                            "points": [
                                "Art. 345 choice",
                                "Any language in use / Hindi",
                                "Art. 347 minority recognition",
                            ],
                        },
                        {
                            "id": "sch",
                            "heading": "8th Schedule",
                            "points": [
                                "22 languages",
                                "OL Commission seats",
                                "Hindi enrichment (351)",
                            ],
                        },
                        {
                            "id": "cl",
                            "heading": "Classical",
                            "points": [
                                "Executive notification",
                                "11 languages (2024)",
                                "Awards / chairs / centres",
                            ],
                        },
                    ],
                },
                {
                    "id": "ocd-cmp-fr",
                    "type": "comparison",
                    "title": "Fundamental Rights vs Special Provisions",
                    "columns": [
                        {
                            "id": "fr",
                            "heading": "Fundamental Rights",
                            "points": [
                                "Part III — justiciable",
                                "Enforceable vs State",
                                "Universal catalogue (+ citizen rights)",
                                "Art. 32 / 226 remedies",
                            ],
                        },
                        {
                            "id": "sp",
                            "heading": "Special Provisions",
                            "points": [
                                "Part XVI classes · Part XXI states",
                                "Targeted / asymmetric",
                                "Reservations, boards, custom bars",
                                "Often time-bound or situational",
                            ],
                        },
                    ],
                },
                {
                    "id": "ocd-cmp-services",
                    "type": "comparison",
                    "title": "Union Services vs State Services vs All India Services",
                    "columns": [
                        {
                            "id": "ais",
                            "heading": "All-India Services",
                            "points": [
                                "IAS · IPS · IFoS",
                                "Shared Centre–state",
                                "State cadres; Centre discipline",
                                "Art. 312 + AIS Act 1951",
                            ],
                        },
                        {
                            "id": "union",
                            "heading": "Central (Union) Services",
                            "points": [
                                "Exclusive Central jurisdiction",
                                "Groups A–D",
                                "IFS top Central service",
                                "DoPT / parent ministries",
                            ],
                        },
                        {
                            "id": "state",
                            "heading": "State Services",
                            "points": [
                                "Exclusive state jurisdiction",
                                "Below AIS in state hierarchy",
                                "Feed ≤33⅓% AIS senior posts",
                                "State-named cadres",
                            ],
                        },
                    ],
                },
            ],
        },
        {
            "title": "Final Revision",
            "slug": "ocd-final-revision",
            "sort_order": 8,
            "summary": (
                "One-pass cheat sheets: articles maps, 371–371J, reservations, language, "
                "services, mnemonics, PYQ themes, and confused pairs."
            ),
            "body": (
                "## Complete articles cheat sheet\n\n"
                "| Theme | Articles |\n"
                "|---|---|\n"
                "| Co-ops (IX-B) | 243ZH–243ZT (+ 19, 43-B) |\n"
                "| Official language | 343–351 · 8th Schedule |\n"
                "| Public services | 308–313 (314 repealed) |\n"
                "| Govt rights/liability | 294–300A |\n"
                "| Special classes | 330–342A |\n"
                "| Special states | 371–371J |\n\n"
                "## Language provisions cheat sheet\n\n"
                "- 343 Hindi Union · OLA English forever · 345 state choice ≠ Schedule · "
                "348 English courts default · 350/350A/350B minorities · 351 Hindi duty · "
                "22 Schedule · 11 classical (2024).\n\n"
                "## Public services comparison (1-liner)\n\n"
                "AIS shared dual control · Central exclusive · State exclusive · "
                "312 = RS resolution + Act · 310 pleasure · 311 shields.\n\n"
                "## Reservation provisions summary\n\n"
                "- SC/ST LS & SLA seats → **2030** (104th).\n"
                "- Anglo-Indian nomination → **ended** (104th).\n"
                "- OBC Central List + state lists (102nd/105th).\n"
                "- Art. 335 + 82nd promotion relaxations for SC/ST.\n\n"
                "## State-wise special provisions summary\n\n"
                "| Art | State | Hook |\n"
                "|---|---|---|\n"
                "| 371 | MH, GJ | Development boards |\n"
                "| 371A | Nagaland | Consent + land & resources + LoO |\n"
                "| 371B | Assam | Tribal areas committee |\n"
                "| 371C | Manipur | Hill Areas committee |\n"
                "| 371D | AP, TS | Local cadres / tribunal |\n"
                "| 371E | AP | Central University |\n"
                "| 371F | Sikkim | ≥30 MLAs; sectional seats |\n"
                "| 371G | Mizoram | Consent + land; ≥40 MLAs |\n"
                "| 371H | Arunachal | LoO; ≥30 MLAs |\n"
                "| 371I | Goa | ≥30 MLAs |\n"
                "| 371J | Karnataka | Kalyana Karnataka board (98th) |\n\n"
                "## Frequently confused concepts\n\n"
                "- Part **IX** (Panchayats) vs **IX-B** (co-ops).\n"
                "- **343** vs **345**; Schedule vs classical.\n"
                "- **310** vs **311**; dismissal vs removal.\n"
                "- **300** vs **300A** (suits vs property right).\n"
                "- **371A** vs **371G** (resources).\n"
                "- 97th: Art. 19/43-B survive; Part IX-B mainly **MSCS** after 2021.\n\n"
                "## Mnemonics / memory tricks\n\n"
                "- **97th trio:** FR + DPSP + IX-B.\n"
                "- **371 ladder:** A NL, B AS, C MN, D AP/TS, E Univ-AP, F SK, G MZ, H AR, I GA, J KA.\n"
                "- **Language heads:** Union → Regional → Judiciary → Directives.\n"
                "- **299 three F’s:** Form (President/Governor) · For (on behalf) · Functionary (authorised).\n\n"
                "## PYQ themes\n\n"
                "Eighth Schedule additions; Art. 312 AIS creation; 97th/SC co-ops; 104th twin effect; "
                "371A Naga land; Doctrine of Pleasure + 311 exceptions; 300A not FR; classical languages.\n\n"
                "## One-page final revision summary\n\n"
                "Part IX toolkit = Co-ops · Language · Services · Liability · Classes · States. "
                "Drill traps first, then article maps, then 371 matrix. Finish with Master Comparisons."
            ),
            "articles": [
                ("Part IX-B · XVII · XIV · XII · XVI · XXI", "Article clusters for Other Constitutional Dimensions."),
            ],
            "visual_blocks": [
                {
                    "id": "ocd-rev-371",
                    "type": "comparison",
                    "title": "Articles 371A–371J comparison table",
                    "columns": [
                        {
                            "id": "ab",
                            "heading": "371A–B",
                            "points": [
                                "A Nagaland — consent + resources",
                                "B Assam — tribal committee",
                            ],
                        },
                        {
                            "id": "cd",
                            "heading": "371C–D",
                            "points": [
                                "C Manipur — Hill Areas",
                                "D AP/TS — local cadres/tribunal",
                            ],
                        },
                        {
                            "id": "ef",
                            "heading": "371E–F",
                            "points": [
                                "E AP Central University",
                                "F Sikkim special (36th legacy)",
                            ],
                        },
                        {
                            "id": "ghij",
                            "heading": "371G–J",
                            "points": [
                                "G Mizoram — land consent",
                                "H Arunachal — LoO",
                                "I Goa — ≥30 MLAs",
                                "J Karnataka — 98th board",
                            ],
                        },
                    ],
                },
                {
                    "id": "ocd-rev-resv",
                    "type": "comparison",
                    "title": "Reservation provisions — at a glance",
                    "columns": [
                        {
                            "id": "scst",
                            "heading": "SC/ST",
                            "points": [
                                "Political seats till 2030",
                                "Services via 335 + 82nd",
                                "Lists: President / Parliament",
                            ],
                        },
                        {
                            "id": "obc",
                            "heading": "OBC",
                            "points": [
                                "Central + state lists",
                                "NCBC constitutional",
                                "Mandal 27% jobs lineage",
                            ],
                        },
                        {
                            "id": "ai",
                            "heading": "Anglo-Indian",
                            "points": [
                                "Nomination ended 2020",
                                "Defined in Constitution",
                                "Historic service prefs ended",
                            ],
                        },
                    ],
                },
                {
                    "id": "ocd-rev-exam5",
                    "type": "callout",
                    "tone": "tip",
                    "title": "Exam in 5 Minutes — whole chapter",
                    "body": (
                        "Co-ops: 97th trio + SC 2021 MSCS. Language: 343/345/8th/classical. "
                        "Services: 312 RS+Act; 310/311. Liability: 299 form; 300A≠FR. "
                        "Classes: 104th twin. States: 371 ladder A→J. Then kill confused pairs."
                    ),
                },
            ],
        },
    ]
)

EDGES = [
    (HUB_SLUG, "parent", "ocd-cooperative-societies"),
    (HUB_SLUG, "parent", "ocd-official-language"),
    (HUB_SLUG, "parent", "ocd-public-services"),
    (HUB_SLUG, "parent", "ocd-rights-liabilities"),
    (HUB_SLUG, "parent", "ocd-special-classes"),
    (HUB_SLUG, "parent", "ocd-special-states"),
    (HUB_SLUG, "parent", "ocd-master-comparisons"),
    (HUB_SLUG, "parent", "ocd-final-revision"),
    ("ocd-cooperative-societies", "related", "sf-cooperative-societies"),
    ("ocd-cooperative-societies", "related", "ocd-master-comparisons"),
    ("ocd-official-language", "related", "ocd-master-comparisons"),
    ("ocd-public-services", "related", "tribunals"),
    ("ocd-public-services", "related", "ocd-master-comparisons"),
    ("ocd-rights-liabilities", "related", "ocd-final-revision"),
    ("ocd-special-classes", "related", "fundamental-rights"),
    ("ocd-special-classes", "related", "ocd-master-comparisons"),
    ("ocd-special-states", "related", "ocd-final-revision"),
    ("ocd-master-comparisons", "related", "ocd-final-revision"),
    ("ocd-cooperative-societies", "related", "ocd-final-revision"),
    ("ocd-official-language", "related", "ocd-final-revision"),
]

SAMPLE_PYQS = [
    (
        2013,
        "Which of the following are included in the original list of languages in the Eighth Schedule?",
        "Focus on original 14 vs later additions (21st/71st/92nd) — Sindhi not original.",
        ["ocd-official-language", "ocd-final-revision"],
    ),
    (
        2015,
        "The provision for creating All-India Services is in which Article, and what is Rajya Sabha’s role?",
        "Art. 312 — RS resolution (⅔ present & voting) recommending creation; Parliament then legislates.",
        ["ocd-public-services"],
    ),
    (
        2018,
        "Consider statements on official language of the Union and continuance of English.",
        "Hindi is Union official language; English continued via Official Languages Act without time-limit.",
        ["ocd-official-language"],
    ),
    (
        2020,
        "With reference to special provisions under Article 371A, which matters need Nagaland Assembly consent?",
        "Religious/social practices, customary law, customary justice, ownership & transfer of land and its resources.",
        ["ocd-special-states"],
    ),
    (
        2021,
        "Which amendment constitutionalised co-operative societies via FR, DPSP and a new Part?",
        "97th Amendment — Art. 19 + Art. 43-B + Part IX-B.",
        ["ocd-cooperative-societies", HUB_SLUG],
    ),
    (
        2020,
        "Right to Property is a Fundamental Right — True or False?",
        "False — after 44th Amendment it is a legal right under Art. 300A.",
        ["ocd-rights-liabilities"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Union of India v. Rajendra N. Shah",
        "slug": "union-of-india-v-rajendra-n-shah",
        "parties": "Union of India v. Rajendra N. Shah",
        "year": 2021,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Supreme Court on Part IX-B (97th Amendment) — operative for multi-state "
            "co-operative societies; Art. 19 and 43-B remain intact."
        ),
        "holding": (
            "Part IX-B is operative insofar as it concerns multi-state co-operative societies "
            "(and in Union territories); provisions affecting state co-ops needed state ratification."
        ),
        "concept_slugs": ["ocd-cooperative-societies", HUB_SLUG],
    },
    {
        "title": "Kasturilal v. State of UP",
        "slug": "kasturilal-v-state-of-up",
        "parties": "Kasturilal Ralia Ram Jain v. State of Uttar Pradesh",
        "year": 1964,
        "court": CaseLaw.Court.SC,
        "summary": "Reaffirmed sovereign/non-sovereign distinction for tort liability of the State.",
        "holding": (
            "State immunity for torts in exercise of sovereign functions was upheld — later "
            "narrowed by subsequent jurisprudence."
        ),
        "concept_slugs": ["ocd-rights-liabilities"],
    },
    {
        "title": "N. Nagendra Rao & Co. v. State of A.P.",
        "slug": "nagendra-rao-v-state-of-ap",
        "parties": "N. Nagendra Rao & Co. v. State of Andhra Pradesh",
        "year": 1994,
        "court": CaseLaw.Court.SC,
        "summary": "Criticised doctrine of sovereign immunity; expanded State tort liability.",
        "holding": (
            "In the modern sense the sovereign/non-sovereign distinction largely fails — "
            "State is ordinarily liable for negligent acts of its servants."
        ),
        "concept_slugs": ["ocd-rights-liabilities", HUB_SLUG],
    },
]

AMENDMENTS = [
    {
        "number": 7,
        "year": 1956,
        "title": "Seventh Amendment",
        "summary": "States Reorganisation changes including linguistic minority education provisions.",
        "effect": "Inserted Arts 350A and 350B.",
        "concept_slugs": ["ocd-official-language", HUB_SLUG],
    },
    {
        "number": 21,
        "year": 1967,
        "title": "Twenty-first Amendment",
        "summary": "Added Sindhi to the Eighth Schedule.",
        "effect": "Eighth Schedule expansion began.",
        "concept_slugs": ["ocd-official-language"],
    },
    {
        "number": 28,
        "year": 1972,
        "title": "Twenty-eighth Amendment",
        "summary": "Service conditions of certain pre-1950 Crown officers; repealed Art. 314.",
        "effect": "Inserted Art. 312A; repealed Art. 314.",
        "concept_slugs": ["ocd-public-services"],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": "Among many changes, altered Art. 311 hearing stages; enabled all-India judicial service clause.",
        "effect": "Removed second opportunity against proposed penalty under Art. 311.",
        "concept_slugs": ["ocd-public-services", HUB_SLUG],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": "Right to Property ceased to be a Fundamental Right.",
        "effect": "Inserted Art. 300A — property as legal right.",
        "concept_slugs": ["ocd-rights-liabilities", HUB_SLUG],
    },
    {
        "number": 71,
        "year": 1992,
        "title": "Seventy-first Amendment",
        "summary": "Added Konkani, Manipuri and Nepali to the Eighth Schedule.",
        "effect": "Eighth Schedule languages increased.",
        "concept_slugs": ["ocd-official-language"],
    },
    {
        "number": 82,
        "year": 2000,
        "title": "Eighty-second Amendment",
        "summary": "Enabled relaxation of marks/standards for SC/ST in promotion reservation.",
        "effect": "Proviso pathway linked to Art. 335 claims.",
        "concept_slugs": ["ocd-special-classes"],
    },
    {
        "number": 89,
        "year": 2003,
        "title": "Eighty-ninth Amendment",
        "summary": "Bifurcated the combined SC/ST commission.",
        "effect": "Separate NCSC (338) and NCST (338A).",
        "concept_slugs": ["ocd-special-classes"],
    },
    {
        "number": 92,
        "year": 2003,
        "title": "Ninety-second Amendment",
        "summary": "Added Bodo, Dogri, Maithili and Santhali to the Eighth Schedule.",
        "effect": "Schedule reached 22 languages (with prior Sindhi etc.).",
        "concept_slugs": ["ocd-official-language"],
    },
    {
        "number": 96,
        "year": 2011,
        "title": "Ninety-sixth Amendment",
        "summary": "Substituted Odia for Oriya in the Eighth Schedule.",
        "effect": "Name change only — still 22 languages.",
        "concept_slugs": ["ocd-official-language"],
    },
    {
        "number": 97,
        "year": 2011,
        "title": "Ninety-seventh Amendment",
        "summary": "Constitutional status and protection for co-operative societies.",
        "effect": "Art. 19 + Art. 43-B + Part IX-B (243ZH–ZT).",
        "concept_slugs": ["ocd-cooperative-societies", HUB_SLUG, "sf-cooperative-societies"],
    },
    {
        "number": 98,
        "year": 2012,
        "title": "Ninety-eighth Amendment",
        "summary": "Special provisions for Hyderabad-Karnataka region.",
        "effect": "Inserted Article 371J.",
        "concept_slugs": ["ocd-special-states", HUB_SLUG],
    },
    {
        "number": 102,
        "year": 2018,
        "title": "One Hundred and Second Amendment",
        "summary": "Constitutional status to the National Commission for Backward Classes.",
        "effect": "Inserted Art. 338B and SEBC Central List framework.",
        "concept_slugs": ["ocd-special-classes", HUB_SLUG],
    },
    {
        "number": 104,
        "year": 2019,
        "title": "One Hundred and Fourth Amendment",
        "summary": "Extended SC/ST political reservation; ended Anglo-Indian nomination.",
        "effect": "SC/ST seats till 2030; Arts 331/333 nomination ceased (Jan 2020).",
        "concept_slugs": ["ocd-special-classes", HUB_SLUG],
    },
    {
        "number": 105,
        "year": 2021,
        "title": "One Hundred and Fifth Amendment",
        "summary": "Restored and clarified states’ power over their own SEBC/OBC lists.",
        "effect": "Central List for Union purposes; states may keep distinct lists by law.",
        "concept_slugs": ["ocd-special-classes", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = (
        "Seed Other Constitutional Dimensions chapter "
        "(Laxmikanth Part IX, Ch. 73–78)."
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
                "title": "Other Constitutional Dimensions",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Part IX (Ch. 73–78)",
                "summary": (
                    "Visual revision of Part IX — co-operatives, official language, "
                    "public services, government liability, special classes, and special states."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="other-constitutional-dimensions"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Other Constitutional Dimensions",
                "summary": (
                    "Six Part IX themes — co-ops, language, services, liability, "
                    "special classes, special states — plus comparison and cheat-sheet clusters."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **toolkit mental model**, then the **six themes**. "
                    "Drill dense clusters (language, services, 371s). "
                    "Finish with **Master Comparisons** and **Final Revision**. "
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
            ref="Laxmikanth Part IX (Ch. 73–78)",
            excerpt=(
                "Other Constitutional Dimensions — co-ops, language, services, "
                "liability, special classes, special states."
            ),
            sort_order=0,
        )

        ocd_slugs = set(by_slug.keys())
        external_targets = {
            "sf-cooperative-societies",
            "tribunals",
            "fundamental-rights",
        }
        ConceptEdge.objects.filter(
            source__slug__in=ocd_slugs, source__subject=subject
        ).filter(target__slug__in=ocd_slugs | external_targets).delete()

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
                by_slug[s] for s in case_data["concept_slugs"] if s in by_slug
            ]
            if concepts:
                existing = list(case.concepts.all())
                case.concepts.set({*existing, *concepts})

        for amd_data in AMENDMENTS:
            payload = {k: v for k, v in amd_data.items() if k != "concept_slugs"}
            # Do not clobber summaries owned by earlier chapter seeds (e.g. 42nd / 44th).
            amendment, created = ConstitutionalAmendment.objects.get_or_create(
                academy=academy,
                number=payload["number"],
                defaults=payload,
            )
            if created is False and not amendment.title:
                for field in ("title", "year", "summary", "effect"):
                    if payload.get(field) and not getattr(amendment, field, None):
                        setattr(amendment, field, payload[field])
                amendment.save()
            concepts = [
                by_slug[s]
                for s in amd_data["concept_slugs"]
                if s in by_slug
            ]
            for s in amd_data["concept_slugs"]:
                if s not in by_slug:
                    extra = Concept.objects.filter(subject=subject, slug=s).first()
                    if extra:
                        concepts.append(extra)
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Other Constitutional Dimensions seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(LANDMARK_CASES)} cases, "
                f"{len(AMENDMENTS)} amendments."
            )
        )
