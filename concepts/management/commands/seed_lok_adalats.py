"""Seed Laxmikanth Ch.38 Lok Adalats and Other Courts (visual revision)."""

from django.core.management.base import BaseCommand

from concepts.models import CaseLaw, Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "lok-adalats-other-courts"
CHAPTER_SLUG = "lok-adalats-other-courts"

ENTRY_PILLARS = [
    {
        "id": "nalsa",
        "articles": "Art. 39A",
        "label": "Legal Services & NALSA",
        "slug": "la-nalsa-lsaa",
        "detail": "LSAA 1987 → NALSA hierarchy; free legal aid + Lok Adalats + awareness.",
        "tone": "teal",
    },
    {
        "id": "lok",
        "articles": "ADR",
        "label": "Lok Adalats",
        "slug": "la-lok-adalats",
        "detail": "People’s Court — pending + pre-litigation; award = decree, no appeal.",
        "tone": "olive",
    },
    {
        "id": "pla",
        "articles": "2002",
        "label": "Permanent Lok Adalats",
        "slug": "la-permanent-lok-adalats",
        "detail": "Public utility services; can decide on merits; ₹1 crore (2015).",
        "tone": "gold",
    },
    {
        "id": "family",
        "articles": "1984",
        "label": "Family Courts",
        "slug": "la-family-courts",
        "detail": "Mandatory above 1M pop; conciliation first; one appeal to HC.",
        "tone": "orange",
    },
    {
        "id": "gram",
        "articles": "2008",
        "label": "Gram Nyayalayas",
        "slug": "la-gram-nyayalayas",
        "detail": "Mobile JMFC at intermediate Panchayat; civil + criminal; not mandatory.",
        "tone": "terracotta",
    },
    {
        "id": "commercial",
        "articles": "2015",
        "label": "Commercial Courts",
        "slug": "la-commercial-courts",
        "detail": "Specified value ≥ ₹3 lakh; pre-institution mediation; investor confidence.",
        "tone": "maroon",
    },
    {
        "id": "ftc",
        "articles": "UPSC+",
        "label": "Fast Track Courts",
        "slug": "la-fast-track-courts",
        "detail": "Lean add-on — priority backlog courts, not statutory ADR.",
        "tone": "teal",
    },
    {
        "id": "compare",
        "articles": "Map",
        "label": "Compare forums",
        "slug": "la-compare-forums",
        "detail": "One table — LA · PLA · Family · Gram · Commercial · FTC.",
        "tone": "olive",
    },
    {
        "id": "reforms",
        "articles": "Timeline",
        "label": "Reforms & issues",
        "slug": "la-reforms-issues",
        "detail": "Key dates, operational bottlenecks, mains angles on access to justice.",
        "tone": "gold",
    },
    {
        "id": "exam",
        "articles": "Exam",
        "label": "Exam kit",
        "slug": "la-exam-kit",
        "detail": "Prelims facts, memory aids, PYQ themes, mains value-adds.",
        "tone": "orange",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "la-doorstep-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Justice at the doorstep",
        "topic_label": "Lok Adalats & Other Courts",
        "subject_label": "Art. 39A · Ch. 38",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating every specialised forum as a Lok Adalat",
            "Confusing ordinary LA (settle only) with PLA (can decide merits)",
            "Saying Gram Nyayalayas hear only civil cases",
            "Missing Art. 39A as the constitutional anchor",
        ],
        "insight": (
            "Art. 39A drives free legal aid and equal justice. LSAA builds the network; "
            "Lok Adalats settle; specialised courts speed or localise adjudication."
        ),
    },
    {
        "id": "la-entry-pillars",
        "type": "pillars",
        "title": "Chapter map — open a cluster",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "la-hub-anchor",
        "type": "callout",
        "tone": "note",
        "title": "Constitutional anchor",
        "body": (
            "**Art. 39A** — equal justice and free legal aid. "
            "Supporting hooks: **Art. 14** (equality before law) and **Art. 22(1)** "
            "(legal system / fair process expectations). This chapter is the institutional delivery layer."
        ),
    },
]

CLUSTERS = [
    {
        "slug": "la-nalsa-lsaa",
        "title": "Legal Services & NALSA",
        "sort_order": 1,
        "summary": (
            "Legal Services Authorities Act 1987 (in force 9 Nov 1995) — "
            "NALSA hierarchy, free legal services, eligible persons."
        ),
        "articles": [
            ("Article 39A", "Equal justice and free legal aid — constitutional driver for LSAA/NALSA."),
            ("Arts 14 & 22(1)", "Equality before law and fair legal process — supporting hooks."),
            ("LSAA 1987", "Nationwide network for free legal services; force from 9 November 1995."),
        ],
        "body": (
            "## Why it exists\n\n"
            "Art. **39A** directs equal justice and free legal aid. Arts **14** and **22(1)** "
            "reinforce equality and a fair legal system. Parliament enacted the "
            "**Legal Services Authorities Act, 1987** (force from **9 November 1995**) "
            "to build a uniform nationwide network.\n\n"
            "## Who does what\n\n"
            "- **NALSA** — policies, principles, schemes; monitors and evaluates legal-aid programmes.\n"
            "- **SLSA** (every State) + **HCLSC** (every High Court).\n"
            "- **DLSA** + **Taluk LSC** — implement on ground; organise Lok Adalats.\n"
            "- **SCLSC** — legal services relating to the Supreme Court.\n\n"
            "**Memory:** *NALSA polices policy; States do the work.*\n\n"
            "## Three standing functions\n\n"
            "1. Free and competent legal services to eligible persons.\n"
            "2. Organise Lok Adalats for amicable settlement.\n"
            "3. Legal awareness camps (especially rural).\n\n"
            "## What “free legal services” cover\n\n"
            "- Court fee, process fees, and related charges.\n"
            "- Lawyer’s services in proceedings.\n"
            "- Certified copies of orders/documents.\n"
            "- Appeal paper-book preparation (printing/translation).\n\n"
            "## Who is eligible\n\n"
            "Women & children · SC/ST · industrial workmen · mass-disaster/violence/"
            "flood/drought/earthquake/industrial-disaster victims · disabled persons · "
            "persons in custody · trafficking/begar victims · income-capped persons.\n\n"
            "**Income caps:** annual income ≤ **₹1 lakh** (general); "
            "**₹5 lakh** before the Supreme Court Legal Services Committee.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-nalsa-tree",
                "type": "tree",
                "title": "Legal services hierarchy",
                "root": {
                    "id": "nalsa",
                    "label": "NALSA",
                    "detail": "Policy · schemes · monitor",
                    "children": [
                        {
                            "id": "slsa",
                            "label": "State Legal Services Authority",
                            "detail": "Every State",
                            "children": [
                                {
                                    "id": "dlsa",
                                    "label": "District LSA",
                                    "children": [
                                        {
                                            "id": "taluk",
                                            "label": "Taluk LSC",
                                            "detail": "Most Taluks",
                                        }
                                    ],
                                },
                                {
                                    "id": "hclsc",
                                    "label": "High Court LSC",
                                    "detail": "Every HC",
                                },
                            ],
                        },
                        {
                            "id": "sclsc",
                            "label": "Supreme Court LSC",
                            "detail": "SC-related legal services",
                        },
                    ],
                },
            },
            {
                "id": "la-nalsa-functions",
                "type": "pillars",
                "title": "Three functions on the ground",
                "items": [
                    {
                        "id": "free",
                        "articles": "1",
                        "label": "Free legal services",
                        "detail": "Fee · lawyer · copies · appeal papers.",
                        "tone": "teal",
                    },
                    {
                        "id": "lok",
                        "articles": "2",
                        "label": "Organise Lok Adalats",
                        "detail": "Amicable settlement of disputes.",
                        "tone": "olive",
                    },
                    {
                        "id": "aware",
                        "articles": "3",
                        "label": "Awareness camps",
                        "detail": "Especially in rural areas.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "la-nalsa-elig",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims — eligibility + income",
                "body": (
                    "Eight categories including women/children, SC/ST, workmen, disaster victims, "
                    "disabled, custody, trafficking/begar, and income-poor. "
                    "Remember **₹1 lakh** vs **₹5 lakh** (SC Legal Services Committee)."
                ),
            },
        ],
    },
    {
        "slug": "la-lok-adalats",
        "title": "Lok Adalats",
        "sort_order": 2,
        "summary": (
            "People’s Court under LSAA — pending and pre-litigation settlement; "
            "award final as Civil Court decree; no appeal."
        ),
        "articles": [
            ("LSAA 1987", "Statutory status for Lok Adalats after voluntary Gujarat camps (1982)."),
            ("P.T. Thomas (2005)", "SC on meaning and benefits of Lok Adalat."),
        ],
        "body": (
            "## Meaning\n\n"
            "**Lok Adalat** = People’s Court — ancient Indian form revived as modern **ADR**. "
            "Gandhian spirit: no victors/vanquished, no rancour. Settles disputes that are "
            "**pending in court** or still at **pre-litigation** stage.\n\n"
            "## Origin → statute\n\n"
            "- First post-independence camp: **Gujarat, 1982** (voluntary, no statutory backing).\n"
            "- Growing popularity → statutory status under **Legal Services Authorities Act, 1987**.\n\n"
            "## Composition\n\n"
            "Organised by SLSA / DLSA / SCLSC / HCLSC / Taluk LSC. "
            "Typically: **judicial officer (chair) + advocate + social worker**.\n\n"
            "## Jurisdiction\n\n"
            "- Any case pending before a court, **or**\n"
            "- Matter within a court’s jurisdiction but not yet filed.\n"
            "- **No jurisdiction** over offences **not compoundable** under any law.\n\n"
            "## How a pending case reaches LA\n\n"
            "1. Both parties agree to settle in Lok Adalat; **or**\n"
            "2. One party applies to the court for reference; **or**\n"
            "3. Court is satisfied the matter is fit for Lok Adalat.\n\n"
            "Pre-litigation: organising agency refers on application by any party.\n\n"
            "## Powers & character of proceedings\n\n"
            "Same Civil Court powers (CPC) for summons, discovery, affidavits, public records, etc. "
            "May specify its own procedure. Proceedings = **judicial proceedings** (IPC sense); "
            "Lok Adalat deemed a **Civil Court** for CrPC purposes.\n\n"
            "## Award\n\n"
            "Deemed a **decree of a Civil Court** (or order of another court). "
            "**Final and binding. No appeal** to any court.\n\n"
            "## Types\n\n"
            "1. **National Lok Adalats** — same day nationwide (SC to Taluk). From **2015**, "
            "subject-wise every month.\n"
            "2. **State / Regular Lok Adalats** — Continuous · Daily · Mobile · Mega.\n"
            "3. **Permanent Lok Adalats** — next cluster (public utility services).\n\n"
            "## Benefits (SC)\n\n"
            "No court fee (refund if paid) · procedural flexibility · parties can interact "
            "directly with the judge via counsel · binding non-appealable decree → finality.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-lok-flow",
                "type": "flowchart",
                "title": "How a case reaches Lok Adalat",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Where is the dispute?",
                        "options": [
                            {"label": "Pending in court", "next": "pending"},
                            {"label": "Pre-litigation", "next": "pre"},
                            {"label": "Non-compoundable offence", "next": "bar"},
                        ],
                    },
                    {
                        "id": "pending",
                        "label": "Pending — reference if…",
                        "options": [
                            {"label": "Both parties agree", "next": "settle"},
                            {"label": "One party applies", "next": "settle"},
                            {"label": "Court finds it fit", "next": "settle"},
                        ],
                    },
                    {
                        "id": "pre",
                        "label": "Organising agency refers on any party’s application",
                        "options": [{"label": "Proceed to LA", "next": "settle"}],
                    },
                    {
                        "id": "bar",
                        "label": "Outside LA jurisdiction — no settlement forum here",
                    },
                    {
                        "id": "settle",
                        "label": "Compromise → award = Civil Court decree (final, no appeal)",
                    },
                ],
            },
            {
                "id": "la-lok-pending-pre",
                "type": "comparison",
                "title": "Pending vs pre-litigation",
                "columns": [
                    {
                        "id": "pending",
                        "heading": "Pending before court",
                        "points": [
                            "Parties agree, or",
                            "One party applies to court, or",
                            "Court itself refers as fit",
                        ],
                    },
                    {
                        "id": "pre",
                        "heading": "Pre-litigation",
                        "points": [
                            "Not yet filed in court",
                            "Still within some court’s jurisdiction",
                            "Organising agency refers on application",
                        ],
                    },
                ],
            },
            {
                "id": "la-lok-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Ordinary Lok Adalat **settles by compromise** — award is non-appealable. "
                    "Do **not** confuse with Permanent Lok Adalat, which can **decide on merits** "
                    "if settlement fails. Non-compoundable offences are out for both."
                ),
            },
        ],
    },
    {
        "slug": "la-permanent-lok-adalats",
        "title": "Permanent Lok Adalats",
        "sort_order": 3,
        "summary": (
            "2002 amendment — public utility services; settle first, else decide on merits; "
            "pecuniary jurisdiction up to ₹1 crore (2015)."
        ),
        "articles": [
            ("LSAA 2002 amendment", "Created Permanent Lok Adalats for public utility services."),
            ("Pecuniary limit", "Originally ₹10 lakh; raised to ₹1 crore in 2015."),
        ],
        "body": (
            "## Why PLA\n\n"
            "LSAA amended in **2002** to create **Permanent Lok Adalats** for "
            "**public utility services (PUS)** — standing forum, not a one-day camp.\n\n"
            "## Composition\n\n"
            "- **Chair:** serving/retired District Judge / Additional DJ / higher judicial office.\n"
            "- **Two members** with adequate experience in public utility services.\n\n"
            "## Public utility services\n\n"
            "Transport (air/road/water) · postal/telegraph/telephone · power/light/water supply · "
            "public conservancy/sanitation · hospital/dispensary services · insurance.\n\n"
            "## Key rules\n\n"
            "- Pecuniary jurisdiction: originally **₹10 lakh** → **₹1 crore (2015)** "
            "(Centre may raise further).\n"
            "- No non-compoundable offences.\n"
            "- Party may apply **before** any court is approached; after application, "
            "**no parallel court** in the same dispute.\n"
            "- Try settlement first; if parties fail to agree → **decide on merits**.\n"
            "- Award final & binding; by **majority** of the PLA.\n\n"
            "**Memory:** *PLA = PUS + Decide on merits.*\n"
        ),
        "visual_blocks": [
            {
                "id": "la-pla-vs-lok",
                "type": "comparison",
                "title": "Ordinary Lok Adalat vs Permanent Lok Adalat",
                "columns": [
                    {
                        "id": "lok",
                        "heading": "Ordinary LA",
                        "points": [
                            "Camp / organised sittings",
                            "Any compoundable / civil-type disputes (broad)",
                            "Compromise / settlement only",
                            "Award = decree; no appeal",
                            "No fixed pecuniary cap in Act text here",
                        ],
                    },
                    {
                        "id": "pla",
                        "heading": "Permanent LA",
                        "points": [
                            "Standing body (2002)",
                            "Public utility services only",
                            "Settle first; else decide on merits",
                            "Award final; majority decision",
                            "Up to ₹1 crore (from 2015)",
                        ],
                    },
                ],
            },
            {
                "id": "la-pla-pus",
                "type": "pillars",
                "title": "Public utility services — scan list",
                "items": [
                    {
                        "id": "transport",
                        "articles": "PUS",
                        "label": "Transport",
                        "detail": "Passengers/goods by air, road, water.",
                        "tone": "teal",
                    },
                    {
                        "id": "comms",
                        "articles": "PUS",
                        "label": "Postal & telecom",
                        "detail": "Postal, telegraph, telephone.",
                        "tone": "olive",
                    },
                    {
                        "id": "utils",
                        "articles": "PUS",
                        "label": "Power · water · sanitation",
                        "detail": "Supply + conservancy/sanitation.",
                        "tone": "gold",
                    },
                    {
                        "id": "care",
                        "articles": "PUS",
                        "label": "Hospitals · insurance",
                        "detail": "Dispensaries/hospitals + insurance services.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "la-pla-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook",
                "body": (
                    "**₹1 crore (2015)** pecuniary cap + **decide on merits** if settlement fails + "
                    "application **bars parallel court**. These three separate ordinary LA from PLA."
                ),
            },
        ],
    },
    {
        "slug": "la-family-courts",
        "title": "Family Courts",
        "sort_order": 4,
        "summary": (
            "Family Courts Act 1984 — mandatory in cities/towns above 1 million; "
            "conciliation first; one appeal to High Court."
        ),
        "articles": [
            ("Family Courts Act, 1984", "Specialised courts for marriage and family disputes."),
            ("59th Law Commission Report (1974)", "Urged a radically different, conciliatory approach."),
        ],
        "body": (
            "## Purpose\n\n"
            "Promote **conciliation** and **speedy settlement** of marriage and family disputes — "
            "not ordinary adversarial civil trial culture.\n\n"
            "## Why a separate court\n\n"
            "- Women’s associations / public demand for conciliation-first family forums.\n"
            "- **Law Commission 59th Report (1974)** — different approach; settle before trial.\n"
            "- CPC amended **1976** for family suits, but courts stayed adversarial → need for Act.\n\n"
            "## Objectives\n\n"
            "Specialised expertise · conciliation mechanism · inexpensive remedy · "
            "flexible/informal atmosphere.\n\n"
            "## Establishment\n\n"
            "- State Government **in consultation with the High Court**.\n"
            "- **Obligatory** in every city/town with population **exceeding one million**.\n"
            "- Optional elsewhere if State deems necessary.\n\n"
            "## Exclusive jurisdiction (five heads)\n\n"
            "1. Matrimonial relief (nullity, separation, divorce, restitution, validity/status).\n"
            "2. Property of spouses (or either).\n"
            "3. Declaration of legitimacy.\n"
            "4. Guardianship / custody of a minor.\n"
            "5. Maintenance of wife, children, parents.\n\n"
            "## Procedure highlights\n\n"
            "- First endeavour: **reconciliation/settlement** (informal; rigid procedure off).\n"
            "- Social welfare agencies, counsellors, medical/welfare experts.\n"
            "- Parties **not entitled as of right** to a lawyer; court may use legal expert as "
            "**amicus curiae**.\n"
            "- Simplified evidence/procedure.\n"
            "- **Only one appeal → High Court**.\n\n"
            "**Mains:** specialised, gender-sensitive justice with ADR inside a formal court.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-fc-jurisdiction",
                "type": "pillars",
                "title": "Five exclusive heads",
                "items": [
                    {
                        "id": "matri",
                        "articles": "1",
                        "label": "Matrimonial relief",
                        "detail": "Nullity · separation · divorce · restitution · status.",
                        "tone": "teal",
                    },
                    {
                        "id": "prop",
                        "articles": "2",
                        "label": "Spouse property",
                        "detail": "Property of spouses or either of them.",
                        "tone": "olive",
                    },
                    {
                        "id": "legit",
                        "articles": "3",
                        "label": "Legitimacy",
                        "detail": "Declaration as to legitimacy of any person.",
                        "tone": "gold",
                    },
                    {
                        "id": "custody",
                        "articles": "4",
                        "label": "Guardianship / custody",
                        "detail": "Person or custody of any minor.",
                        "tone": "orange",
                    },
                    {
                        "id": "maint",
                        "articles": "5",
                        "label": "Maintenance",
                        "detail": "Wife, children, and parents.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "la-fc-flow",
                "type": "flowchart",
                "title": "Family Court process instinct",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "Family dispute filed",
                        "options": [
                            {"label": "First duty", "next": "concile"},
                        ],
                    },
                    {
                        "id": "concile",
                        "label": "Endeavour reconciliation (informal stage)",
                        "options": [
                            {"label": "Settlement succeeds", "next": "done"},
                            {"label": "Fails", "next": "trial"},
                        ],
                    },
                    {
                        "id": "trial",
                        "label": "Simplified procedure · experts/counsellors · no lawyer as of right",
                        "options": [
                            {"label": "Decision", "next": "appeal"},
                        ],
                    },
                    {
                        "id": "appeal",
                        "label": "Only one appeal → High Court",
                    },
                    {
                        "id": "done",
                        "label": "Dispute settled at conciliation stage",
                    },
                ],
            },
            {
                "id": "la-fc-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Prelims traps",
                "body": (
                    "**> 1 million** population → Family Court is **mandatory**. "
                    "Lawyer is **not a right** (amicus possible). "
                    "**One** appeal only — to the **High Court**."
                ),
            },
        ],
    },
    {
        "slug": "la-gram-nyayalayas",
        "title": "Gram Nyayalayas",
        "sort_order": 5,
        "summary": (
            "Gram Nyayalayas Act 2008 — mobile JMFC at intermediate Panchayat; "
            "civil + criminal; not mandatory for States."
        ),
        "articles": [
            ("Gram Nyayalayas Act, 2008", "Doorstep justice at intermediate Panchayat level."),
            ("114th Law Commission Report", "Recommended Gram Nyayalayas for speedy rural justice."),
            ("Article 39A", "Equal justice / free legal aid spirit behind rural access reforms."),
        ],
        "body": (
            "## Purpose\n\n"
            "Access to justice at citizens’ **doorsteps** — so social/economic disability "
            "does not deny justice (Art. **39A** spirit). Based broadly on "
            "**Law Commission 114th Report**.\n\n"
            "## Structure\n\n"
            "- Court of **Judicial Magistrate First Class**.\n"
            "- Presiding officer = **Nyayadhikari** — State appoints **in consultation with HC**; "
            "same salary/powers as FC Magistrates under HC.\n"
            "- Established for every **intermediate Panchayat** (or contiguous group); "
            "if no intermediate tier, for a group of contiguous Panchayats.\n"
            "- **Mobile court** — seat at intermediate HQ; goes to villages.\n"
            "- Exercises **both criminal and civil** powers (First & Second Schedules; "
            "Centre/State may amend per competence).\n\n"
            "## Procedure\n\n"
            "- Summary procedure in criminal trials.\n"
            "- Civil Court powers with Act modifications / special procedure.\n"
            "- Prefer **conciliation** (appointed conciliators).\n"
            "- Judgment/order = **decree**; summary execution.\n"
            "- **Not bound by Evidence Act** — guided by natural justice + HC rules.\n"
            "- Plea bargaining available to accused.\n\n"
            "## Appeals (6-month disposal target)\n\n"
            "- Criminal → **Court of Session**.\n"
            "- Civil → **District Court**.\n\n"
            "## Establishment reality\n\n"
            "States set up Gram Nyayalayas **in consultation with HCs**, but the Act "
            "**does not make them mandatory**. Bottlenecks: existing taluka courts, "
            "police/State reluctance, lukewarm Bar, concurrent jurisdiction, logistics.\n\n"
            "**2013 CJ–CM Conference:** establish where feasible — focus on Talukas "
            "**without** regular courts.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-gn-tree",
                "type": "tree",
                "title": "Gram Nyayalaya — structure & appeals",
                "root": {
                    "id": "gn",
                    "label": "Gram Nyayalaya",
                    "detail": "Mobile JMFC · Nyayadhikari",
                    "children": [
                        {
                            "id": "seat",
                            "label": "Seat at intermediate Panchayat HQ",
                            "detail": "Goes to villages",
                        },
                        {
                            "id": "jurisdiction",
                            "label": "Criminal + Civil",
                            "detail": "Schedules I & II",
                            "children": [
                                {
                                    "id": "crim-appeal",
                                    "label": "Criminal appeal → Sessions",
                                    "detail": "Dispose in 6 months",
                                },
                                {
                                    "id": "civil-appeal",
                                    "label": "Civil appeal → District Court",
                                    "detail": "Dispose in 6 months",
                                },
                            ],
                        },
                    ],
                },
            },
            {
                "id": "la-gn-vs-lok",
                "type": "comparison",
                "title": "Gram Nyayalaya vs Lok Adalat",
                "columns": [
                    {
                        "id": "gn",
                        "heading": "Gram Nyayalaya",
                        "points": [
                            "Formal court (JMFC)",
                            "Civil + criminal (scheduled)",
                            "Can adjudicate; prefers conciliation",
                            "Appeals to Sessions / District Court",
                            "Not mandatory for States",
                        ],
                    },
                    {
                        "id": "lok",
                        "heading": "Lok Adalat",
                        "points": [
                            "ADR forum under LSAA",
                            "Pending + pre-litigation settlement",
                            "Compromise only (ordinary LA)",
                            "Award final — no appeal",
                            "Organised by legal services bodies",
                        ],
                    },
                ],
            },
            {
                "id": "la-gn-trap",
                "type": "callout",
                "tone": "trap",
                "title": "PYQ trap",
                "body": (
                    "Gram Nyayalayas hear **both civil and criminal** cases (not civil only). "
                    "Local social activists may act as **mediators/reconciliators**. "
                    "Setting them up is **not mandatory** under the Act."
                ),
            },
        ],
    },
    {
        "slug": "la-commercial-courts",
        "title": "Commercial Courts",
        "sort_order": 6,
        "summary": (
            "Commercial Courts Act 2015 — commercial disputes of specified value "
            "(≥ ₹3 lakh from 2018); pre-institution mediation."
        ),
        "articles": [
            ("Commercial Courts Act, 2015", "Specialised commercial adjudication architecture."),
            ("253rd Law Commission Report", "Recommended Commercial Courts / Divisions in HCs."),
        ],
        "body": (
            "## Purpose\n\n"
            "Speedy disposal of **high-value commercial disputes** — complex facts/law; "
            "signal a responsive system to investors (**ease of doing business** narrative).\n\n"
            "## What is a commercial dispute\n\n"
            "Ordinary transactions of merchants, bankers, financiers, traders — e.g. mercantile "
            "documents, joint venture/partnership, IP rights, insurance, and related areas.\n\n"
            "## Architecture\n\n"
            "- **Commercial Courts** at District level (specified-value disputes).\n"
            "- Where HC has ordinary original civil jurisdiction: Commercial Courts at "
            "**District Judge level** as provided.\n"
            "- **Commercial Appellate Courts** (District Judge level) where HC lacks "
            "ordinary original civil jurisdiction — for appeals from courts below DJ level.\n"
            "- HC **Commercial Division** (CJ constitutes) for specified-value suits in that HC.\n"
            "- HC **Commercial Appellate Division** — appeals from Commercial Courts at DJ level "
            "and from Commercial Division.\n\n"
            "## Specified value\n\n"
            "Not less than **₹3 lakh** (or higher notified value). "
            "Reduced in **2018** from earlier **₹1 crore** to **₹3 lakh**.\n\n"
            "## Pre-institution mediation\n\n"
            "Compulsory mediation before suit if **no urgent interim relief** sought "
            "(Pre-Institution Mediation and Settlement). Centre may empower "
            "**LSAA authorities** to run this mechanism.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-cc-tree",
                "type": "tree",
                "title": "Commercial courts architecture",
                "root": {
                    "id": "cc-root",
                    "label": "Commercial dispute (specified value)",
                    "children": [
                        {
                            "id": "trial",
                            "label": "Trial forums",
                            "children": [
                                {
                                    "id": "dist",
                                    "label": "Commercial Court (District)",
                                },
                                {
                                    "id": "hc-div",
                                    "label": "HC Commercial Division",
                                    "detail": "Where HC has original civil jurisdiction",
                                },
                            ],
                        },
                        {
                            "id": "appeal",
                            "label": "Appeal forums",
                            "children": [
                                {
                                    "id": "app-dist",
                                    "label": "Commercial Appellate Court (DJ level)",
                                },
                                {
                                    "id": "app-hc",
                                    "label": "HC Commercial Appellate Division",
                                },
                            ],
                        },
                    ],
                },
            },
            {
                "id": "la-cc-timeline",
                "type": "timeline",
                "title": "Commercial Courts — key beats",
                "events": [
                    {
                        "id": "lc253",
                        "year": 2015,
                        "label": "Law Commission 253rd + Act",
                        "detail": "253rd Report recommendations fed into Commercial Courts Act, 2015.",
                    },
                    {
                        "id": "act2015",
                        "year": 2015,
                        "label": "Commercial Courts Act",
                        "detail": "District / appellate / HC division architecture for commercial disputes.",
                    },
                    {
                        "id": "val2018",
                        "year": 2018,
                        "label": "Specified value → ₹3 lakh",
                        "detail": "Floor reduced from earlier ₹1 crore to ₹3 lakh.",
                    },
                ],
            },
            {
                "id": "la-cc-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims + mains",
                "body": (
                    "Remember **₹3 lakh** floor (2018) and **compulsory pre-institution mediation** "
                    "(unless urgent interim relief). Mains: investor confidence / economic growth "
                    "via faster commercial justice."
                ),
            },
        ],
    },
    {
        "slug": "la-fast-track-courts",
        "title": "Fast Track Courts",
        "sort_order": 7,
        "summary": (
            "UPSC add-on (not in Laxmikanth Ch.38) — priority backlog courts under the "
            "regular judiciary; not a statutory ADR forum like Lok Adalat."
        ),
        "articles": [
            (
                "UPSC revision note",
                "Not a Ch.38 topic — lean contrast with LA / GN / Commercial Courts.",
            ),
        ],
        "body": (
            "## What FTCs are (revision frame)\n\n"
            "**Fast Track Courts** are specialised or designated courts meant for "
            "**time-bound disposal** of priority categories — e.g. sexual offences, "
            "heinous crimes, or long-pending cases (exact lists vary by scheme/State).\n\n"
            "They sit inside the **regular adjudicatory judiciary**, not under the "
            "Lok Adalat / LSAA settlement model.\n\n"
            "## How they typically arise\n\n"
            "- Policy / scheme-driven (historically Centre–State funded phases).\n"
            "- Established through **State / High Court** administrative measures.\n"
            "- No single “Fast Track Courts Act” to memorise as a Ch.38 parallel — "
            "treat as a **delivery reform**, not a statutory ADR chapter twin.\n\n"
            "## Contrast instinct\n\n"
            "| Forum | Core job |\n"
            "|---|---|\n"
            "| Lok Adalat / PLA | Settle (PLA can also decide PUS merits) |\n"
            "| Gram Nyayalaya | Rural doorstep formal court |\n"
            "| Commercial Court | High-value commercial speed |\n"
            "| Fast Track Court | Priority backlog / sensitive cases speed |\n\n"
            "**Trap:** Do not call FTCs “Lok Adalats” or assume their awards are "
            "non-appealable compromise decrees.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-ftc-compare",
                "type": "comparison",
                "title": "FTC vs Lok Adalat vs Gram Nyayalaya",
                "columns": [
                    {
                        "id": "ftc",
                        "heading": "Fast Track Court",
                        "points": [
                            "Regular judiciary (designated)",
                            "Priority / backlog cases",
                            "Adjudicates (trial court logic)",
                            "Appeals follow normal court path",
                            "Scheme/HC-admin driven",
                        ],
                    },
                    {
                        "id": "lok",
                        "heading": "Lok Adalat",
                        "points": [
                            "ADR under LSAA",
                            "Pending + pre-litigation",
                            "Compromise / settlement",
                            "Award final — no appeal",
                            "Legal services bodies organise",
                        ],
                    },
                    {
                        "id": "gn",
                        "heading": "Gram Nyayalaya",
                        "points": [
                            "Statutory rural court (2008)",
                            "Mobile JMFC at Panchayat tier",
                            "Civil + criminal (schedules)",
                            "Appeals to Sessions / District",
                            "Not mandatory for States",
                        ],
                    },
                ],
            },
            {
                "id": "la-ftc-note",
                "type": "callout",
                "tone": "note",
                "title": "Revision note",
                "body": (
                    "FTCs are **not** in Laxmikanth Ch.38. Use them only to contrast "
                    "**speed-for-priority-cases** with **ADR settlement** (LA) and "
                    "**rural access courts** (GN). Avoid inventing a fake Act year."
                ),
            },
        ],
    },
    {
        "slug": "la-compare-forums",
        "title": "Compare forums",
        "sort_order": 8,
        "summary": (
            "One-page forum map — Ordinary LA, PLA, Family Court, Gram Nyayalaya, "
            "Commercial Court, FTC."
        ),
        "articles": [
            ("Ch. 38 synthesis", "Cross-cutting comparison for last-minute revision."),
        ],
        "body": (
            "## Ecosystem instinct\n\n"
            "**Art. 39A** → **LSAA/NALSA network** (aid + Lok Adalats) → "
            "**specialised courts** (Family, Gram, Commercial) + **FTC** (priority speed).\n\n"
            "## Quick hooks\n\n"
            "- **LA settles; PLA can decide** (PUS).\n"
            "- **Family Court** = conciliation-first formal court; 1M pop rule.\n"
            "- **Gram Nyayalaya** = mobile JMFC; civil+criminal; not mandatory.\n"
            "- **Commercial Court** = specified value ≥ ₹3 lakh; mediation first.\n"
            "- **FTC** = priority backlog speed (not statutory ADR).\n"
        ),
        "visual_blocks": [
            {
                "id": "la-ecosystem-tree",
                "type": "tree",
                "title": "Access-to-justice ecosystem",
                "root": {
                    "id": "art39a",
                    "label": "Art. 39A — equal justice & free legal aid",
                    "children": [
                        {
                            "id": "lsaa",
                            "label": "LSAA / NALSA network",
                            "children": [
                                {"id": "aid", "label": "Free legal services"},
                                {"id": "lok", "label": "Lok Adalats"},
                                {"id": "pla", "label": "Permanent Lok Adalats (PUS)"},
                            ],
                        },
                        {
                            "id": "special",
                            "label": "Specialised courts",
                            "children": [
                                {"id": "fc", "label": "Family Courts (1984)"},
                                {"id": "gn", "label": "Gram Nyayalayas (2008)"},
                                {"id": "cc", "label": "Commercial Courts (2015)"},
                                {"id": "ftc", "label": "Fast Track Courts (policy)"},
                            ],
                        },
                    ],
                },
            },
            {
                "id": "la-big-compare",
                "type": "comparison",
                "title": "Forum strip — statute · nature · appeal hook",
                "columns": [
                    {
                        "id": "lok",
                        "heading": "Ordinary LA",
                        "points": [
                            "LSAA 1987",
                            "ADR settlement",
                            "No appeal (award = decree)",
                        ],
                    },
                    {
                        "id": "pla",
                        "heading": "PLA",
                        "points": [
                            "LSAA 2002 amend.",
                            "PUS; can decide merits",
                            "Final majority award",
                        ],
                    },
                    {
                        "id": "fc",
                        "heading": "Family Court",
                        "points": [
                            "Act 1984",
                            "Formal + conciliation",
                            "One appeal → HC",
                        ],
                    },
                    {
                        "id": "gn",
                        "heading": "Gram Nyayalaya",
                        "points": [
                            "Act 2008",
                            "Mobile JMFC court",
                            "Sessions / District (6 mo)",
                        ],
                    },
                    {
                        "id": "cc",
                        "heading": "Commercial",
                        "points": [
                            "Act 2015",
                            "Specified-value commercial",
                            "Dedicated appellate track",
                        ],
                    },
                    {
                        "id": "ftc",
                        "heading": "FTC",
                        "points": [
                            "Scheme / HC admin",
                            "Priority adjudication",
                            "Normal appeal path",
                        ],
                    },
                ],
            },
            {
                "id": "la-compare-tip",
                "type": "callout",
                "tone": "tip",
                "title": "30-second scan",
                "body": (
                    "Ask: **settle or try?** → LA/PLA vs courts. "
                    "**Whose dispute?** → family / rural / commercial / priority crime. "
                    "**Appeal?** → LA none; FC one to HC; GN Sessions/District."
                ),
            },
        ],
    },
    {
        "slug": "la-reforms-issues",
        "title": "Reforms & issues",
        "sort_order": 9,
        "summary": (
            "Key reform timeline from the chapter plus operational issues and mains angles "
            "on access to justice."
        ),
        "articles": [
            ("Ch. 38 reforms", "PLA ₹1 crore; National LA monthly subjects; Commercial ₹3 lakh; GN bottlenecks."),
        ],
        "body": (
            "## Book-linked reforms\n\n"
            "- **2015:** PLA pecuniary jurisdiction raised to **₹1 crore**.\n"
            "- **From 2015:** National Lok Adalats held on a **specific subject every month**.\n"
            "- **2015 Act / 2018 tweak:** Commercial Courts; specified value cut to **₹3 lakh**; "
            "pre-institution mediation.\n"
            "- **Gram Nyayalayas:** operational issues; **2013 CJ–CM Conference** — set up where "
            "feasible, especially Talukas without regular courts.\n\n"
            "## Issues to remember\n\n"
            "- GN: concurrent jurisdiction with regular courts; weak police/Bar buy-in; logistics.\n"
            "- LA: quality of consent / unequal bargaining power in “amicable” settlements "
            "(mains critique angle).\n"
            "- Commercial: mediation compulsory only when no urgent interim relief.\n\n"
            "## Mains value-adds\n\n"
            "- Access to justice = constitutional promise (39A) + institutional design.\n"
            "- ADR reduces pendency but must not dilute fair consent.\n"
            "- Rural formal courts (GN) vs camp ADR (LA) — complementary, not substitutes.\n"
            "- Commercial courts = legal infrastructure for investment climate.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-reforms-timeline",
                "type": "timeline",
                "title": "Chapter timeline",
                "events": [
                    {
                        "id": "fc84",
                        "year": 1984,
                        "label": "Family Courts Act",
                        "detail": "Conciliation-first specialised family justice.",
                    },
                    {
                        "id": "lsaa87",
                        "year": 1987,
                        "label": "Legal Services Authorities Act",
                        "detail": "Nationwide free legal services + Lok Adalat statute.",
                    },
                    {
                        "id": "force95",
                        "year": 1995,
                        "label": "LSAA in force (9 Nov)",
                        "detail": "Act of 1987 becomes operational nationwide.",
                    },
                    {
                        "id": "pla02",
                        "year": 2002,
                        "label": "Permanent Lok Adalats",
                        "detail": "Amendment creates PLA for public utility services.",
                    },
                    {
                        "id": "gn08",
                        "year": 2008,
                        "label": "Gram Nyayalayas Act",
                        "detail": "Mobile JMFC courts at intermediate Panchayat level.",
                    },
                    {
                        "id": "cc15",
                        "year": 2015,
                        "label": "Commercial Act · PLA ₹1 cr · monthly National LAs",
                        "detail": "Commercial Courts Act; PLA pecuniary hike; subject-wise National LAs.",
                    },
                    {
                        "id": "val18",
                        "year": 2018,
                        "label": "Commercial value → ₹3 lakh",
                        "detail": "Specified value floor reduced from ₹1 crore.",
                    },
                ],
            },
            {
                "id": "la-reforms-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains one-liners",
                "body": (
                    "“Art. 39A is the promise; LSAA/Lok Adalat/special courts are the plumbing.” "
                    "Critique pendency with ADR **and** consent quality. For rural justice, "
                    "pair GN (formal doorstep) with LA (settlement camps)."
                ),
            },
        ],
    },
    {
        "slug": "la-exam-kit",
        "title": "Exam kit",
        "sort_order": 10,
        "summary": (
            "Prelims facts, memory aids, PYQ themes, and mains value-adds for last-minute revision."
        ),
        "articles": [
            ("Revision strip", "Dates, caps, traps, and one-liners for Ch.38 + FTC add-on."),
        ],
        "body": (
            "## Prelims strip\n\n"
            "- LSAA **1987**; force **9 Nov 1995**.\n"
            "- Free legal aid income: **₹1 lakh** / **₹5 lakh** (SC LSC).\n"
            "- First LA camp post-Independence: **Gujarat 1982**.\n"
            "- Ordinary LA award = Civil Court decree; **no appeal**.\n"
            "- PLA: PUS; settle then **merits**; **₹1 crore** (2015).\n"
            "- Family Court: mandatory if pop **> 1 million**; **no lawyer as of right**; "
            "**one appeal → HC**.\n"
            "- Gram Nyayalaya: **civil + criminal**; **not mandatory**; Evidence Act not binding.\n"
            "- Commercial: specified value ≥ **₹3 lakh** (2018); pre-institution mediation.\n\n"
            "## Memory aids\n\n"
            "- *LA settles; PLA can decide.*\n"
            "- *39A → LSAA → NALSA.*\n"
            "- *FC: 1M + 1 appeal to HC.*\n"
            "- *GN: mobile JMFC + Sch I/II.*\n"
            "- *Commercial: 3 lakh + mediate first.*\n\n"
            "## PYQ themes\n\n"
            "- Gram Nyayalaya: civil-only claim is wrong; conciliators allowed.\n"
            "- Art. 39A ↔ legal aid / Lok Adalat link.\n"
            "- Finality of Lok Adalat award.\n"
            "- Eligibility for free legal services.\n\n"
            "## Mains VA\n\n"
            "Access, pendency, consent quality in ADR, rural doorstep justice, "
            "commercial dispute infrastructure for investment.\n"
        ),
        "visual_blocks": [
            {
                "id": "la-exam-memory",
                "type": "pillars",
                "title": "Four memory locks",
                "items": [
                    {
                        "id": "m1",
                        "articles": "ADR",
                        "label": "LA settles; PLA decides",
                        "detail": "Ordinary compromise vs PUS merits power.",
                        "tone": "teal",
                    },
                    {
                        "id": "m2",
                        "articles": "39A",
                        "label": "39A → LSAA → NALSA",
                        "detail": "Constitution → statute → apex authority.",
                        "tone": "olive",
                    },
                    {
                        "id": "m3",
                        "articles": "FC",
                        "label": "FC: 1M + 1 HC appeal",
                        "detail": "Mandatory threshold + appeal path.",
                        "tone": "gold",
                    },
                    {
                        "id": "m4",
                        "articles": "GN",
                        "label": "GN: mobile JMFC",
                        "detail": "Civil+criminal; not mandatory.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "la-exam-prelims",
                "type": "callout",
                "tone": "trap",
                "title": "Highest-yield traps",
                "body": (
                    "GN ≠ civil only · LA award ≠ appealable · PLA ≠ settle-only · "
                    "FC lawyer ≠ as of right · Commercial floor ≠ still ₹1 crore · "
                    "LSAA force year ≠ 1987 (force is 1995)."
                ),
            },
            {
                "id": "la-exam-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains kit",
                "body": (
                    "Frame answers around **access to justice (39A)**, **pendency**, "
                    "**ADR vs adjudication**, and **forum fit** (family / rural / commercial / priority). "
                    "End with one reform line (mediation quality, GN rollout where gaps remain)."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "la-nalsa-lsaa"),
    (HUB_SLUG, "parent", "la-lok-adalats"),
    (HUB_SLUG, "parent", "la-permanent-lok-adalats"),
    (HUB_SLUG, "parent", "la-family-courts"),
    (HUB_SLUG, "parent", "la-gram-nyayalayas"),
    (HUB_SLUG, "parent", "la-commercial-courts"),
    (HUB_SLUG, "parent", "la-fast-track-courts"),
    (HUB_SLUG, "parent", "la-compare-forums"),
    (HUB_SLUG, "parent", "la-reforms-issues"),
    (HUB_SLUG, "parent", "la-exam-kit"),
    ("la-nalsa-lsaa", "related", "la-lok-adalats"),
    ("la-lok-adalats", "related", "la-permanent-lok-adalats"),
    ("la-gram-nyayalayas", "related", "la-compare-forums"),
    ("la-family-courts", "related", "la-compare-forums"),
    ("la-commercial-courts", "related", "la-compare-forums"),
    ("la-fast-track-courts", "related", "la-compare-forums"),
    ("la-reforms-issues", "related", "la-compare-forums"),
    ("la-exam-kit", "related", "la-lok-adalats"),
    ("la-exam-kit", "related", "la-permanent-lok-adalats"),
    ("la-exam-kit", "related", "la-gram-nyayalayas"),
    ("la-exam-kit", "related", "la-nalsa-lsaa"),
    ("la-nalsa-lsaa", "related", "sf-dpsp"),
    ("la-nalsa-lsaa", "related", "directive-principles"),
]

SAMPLE_PYQS = [
    (
        2016,
        "With reference to the Gram Nyayalayas Act, which statement(s) is/are correct? "
        "(1) Gram Nyayalayas can hear only civil cases and not criminal cases. "
        "(2) The Act allows local social activists as mediators/reconciliators.",
        "Statement 1 is incorrect — Gram Nyayalayas hear both civil and criminal cases "
        "(as scheduled). Statement 2 is correct — conciliators/mediators are contemplated. "
        "Answer pattern in UPSC: (b) 2 only.",
        ["la-gram-nyayalayas", "la-exam-kit", HUB_SLUG],
    ),
    (
        2020,
        "An award of a Lok Adalat is best described as:",
        "Deemed a decree of a Civil Court (or order of another court); final and binding; "
        "no appeal lies to any court against the award.",
        ["la-lok-adalats", "la-exam-kit", HUB_SLUG],
    ),
    (
        2021,
        "Which feature distinguishes Permanent Lok Adalats from ordinary Lok Adalats?",
        "PLAs deal with public utility services and, if settlement fails, can decide the "
        "dispute on merits. Pecuniary jurisdiction raised to ₹1 crore in 2015.",
        ["la-permanent-lok-adalats", "la-exam-kit", HUB_SLUG],
    ),
    (
        2022,
        "Under the Family Courts Act, 1984, which of the following is correct?",
        "State Governments must establish a Family Court in every city/town with population "
        "exceeding one million; parties are not entitled as of right to be represented by a "
        "legal practitioner; only one appeal lies to the High Court.",
        ["la-family-courts", "la-exam-kit", HUB_SLUG],
    ),
    (
        2019,
        "Free legal services under the Legal Services Authorities Act are available, inter alia, to:",
        "Women and children, SC/ST, industrial workmen, disaster victims, disabled persons, "
        "persons in custody, trafficking/begar victims, and persons below the income ceiling "
        "(₹1 lakh generally; ₹5 lakh for SC Legal Services Committee).",
        ["la-nalsa-lsaa", "la-exam-kit", HUB_SLUG],
    ),
]

LANDMARK_CASES = [
    {
        "title": "P.T. Thomas v. Thomas Job",
        "slug": "pt-thomas-thomas-job",
        "parties": "P.T. Thomas v. Thomas Job",
        "year": 2005,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Supreme Court explanation of the meaning and benefits of the Lok Adalat "
            "as an ADR institution."
        ),
        "holding": (
            "Lok Adalat is a people’s court rooted in older Indian adjudication and "
            "Gandhian principles — informal, cheap, expeditious ADR for pending and "
            "pre-litigation disputes. Benefits include no court fee (refund if settled), "
            "procedural flexibility, direct interaction, and a binding non-appealable award "
            "with the status of a civil court decree."
        ),
        "concept_slugs": ["la-lok-adalats", HUB_SLUG, "la-exam-kit"],
    },
]


class Command(BaseCommand):
    help = (
        "Seed Lok Adalats and Other Courts chapter (Laxmikanth Ch.38) "
        "under Part IV State Government."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug to seed into (default: fortuneias).",
        )

    def handle(self, *args, **options):
        from academies.seed_utils import get_academy_or_fail
        from subjects.models import Section

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
                "title": "Lok Adalats and Other Courts",
                "sort_order": 9,
                "book_ref": "Laxmikanth 8th Ed, Ch. 38",
                "summary": (
                    "Visual revision of Ch.38 — NALSA/LSAA, Lok Adalats, Permanent Lok Adalats, "
                    "Family Courts, Gram Nyayalayas, Commercial Courts, plus Fast Track Courts add-on."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="state-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Lok Adalats and Other Courts",
                "summary": (
                    "Justice at the doorstep — Art. 39A delivered through legal services, "
                    "Lok Adalats, and specialised courts that decongest the regular hierarchy."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **doorstep justice** mental model, then "
                    "**NALSA** → **Lok Adalats** → **PLA** → **Family / Gram / Commercial** → "
                    "**FTC (lean)** → **Compare** → **Reforms** → **Exam kit**. "
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
            ref="Laxmikanth Ch. 38",
            excerpt=(
                "Lok Adalats and Other Courts — NALSA, Lok Adalats, PLA, "
                "Family Courts, Gram Nyayalayas, Commercial Courts."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Article 39A",
            excerpt="Equal justice and free legal aid — constitutional anchor for this chapter.",
            sort_order=1,
        )

        la_slugs = set(by_slug.keys())
        related_outside = {"sf-dpsp", "directive-principles"}
        ConceptEdge.objects.filter(
            source__slug__in=la_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=la_slugs | related_outside).delete()

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
            concepts = [by_slug[s] for s in slugs if s in by_slug]
            if concepts:
                existing = list(pyq.concepts.all())
                pyq.concepts.set({*existing, *concepts})

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

        self.stdout.write(
            self.style.SUCCESS(
                f"Lok Adalats chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(SAMPLE_PYQS)} PYQs linked."
            )
        )
