"""Seed Laxmikanth Ch.28 Judicial Activism (visual revision)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import CaseLaw, Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Section, Subject

HUB_SLUG = "judicial-activism"
CHAPTER_SLUG = "judicial-activism"

ENTRY_PILLARS = [
    {
        "id": "meaning",
        "articles": "1947 → 1970s",
        "label": "Meaning & origin",
        "slug": "ja-meaning-origin",
        "detail": "Schlesinger → Indian founders → dynamism vs restraint.",
        "tone": "teal",
    },
    {
        "id": "aspects",
        "articles": "PIL · 14/19/21",
        "label": "Two aspects",
        "slug": "ja-two-aspects",
        "detail": "Court directions via PIL + expansive FR reading.",
        "tone": "olive",
    },
    {
        "id": "jr-vs-ja",
        "articles": "5 contrasts",
        "label": "Review vs activism",
        "slug": "ja-review-vs-activism",
        "detail": "JR interprets; JA moulds with policy preference.",
        "tone": "gold",
    },
    {
        "id": "why",
        "articles": "Wadehra 5 · Kashyap 6",
        "label": "Why activism arises",
        "slug": "ja-justification",
        "detail": "Vacuum, weak organs, rights failure, enthusiasm.",
        "tone": "orange",
    },
    {
        "id": "activators",
        "articles": "Baxi 15 → 5",
        "label": "Who activates it",
        "slug": "ja-activators",
        "detail": "Five memory buckets of social activators.",
        "tone": "terracotta",
    },
    {
        "id": "fears",
        "articles": "Baxi 6",
        "label": "Criticisms & fears",
        "slug": "ja-criticisms",
        "detail": "Usurpation → expertise → arrears → legitimacy.",
        "tone": "maroon",
    },
    {
        "id": "restraint",
        "articles": "Dec 2007",
        "label": "Activism vs restraint",
        "slug": "ja-activism-vs-restraint",
        "detail": "Original intent; adventurism warning; Aravali.",
        "tone": "teal",
    },
    {
        "id": "cases",
        "articles": "7 landmarks",
        "label": "Landmark map",
        "slug": "ja-landmark-map",
        "detail": "Art.21 / PIL classics + restraint case.",
        "tone": "olive",
    },
    {
        "id": "exam",
        "articles": "Prelims · Mains",
        "label": "Exam anchors",
        "slug": "ja-exam-anchors",
        "detail": "Facts, PYQ themes, memory spine, traps.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "ja-safety-valve-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Safety valve",
        "topic_label": "Judicial Activism",
        "subject_label": "Judiciary",
        "relation_label": "Fills gaps when",
        "protects_from": [
            "Legislature / executive failure",
            "Rights without remedy",
            "Legislative vacuum",
            "Ignoring constitutional duties",
        ],
        "insight": (
            "Judicial activism is the safety valve of constitutional justice — "
            "if it sticks open, it becomes judicial adventurism."
        ),
    },
    {
        "id": "ja-entry-pillars",
        "type": "pillars",
        "title": "Nine revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "ja-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "JA = assertive use of judicial review for rights and justice; "
            "opposite = judicial restraint; excess = judicial adventurism. "
            "Indian face: PIL directions + expansive Arts 14, 19, 21. "
            "Spine: Justify → Activate → Fear → Restrain."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Meaning & Origin",
        "slug": "ja-meaning-origin",
        "sort_order": 1,
        "summary": (
            "Schlesinger coined the term (1947); India mid-1970s foundations; "
            "five definitional strands condensed for revision."
        ),
        "body": (
            "## Meaning of judicial activism\n\n"
            "**Core idea:** Proactive / assertive judiciary protecting rights and promoting justice — "
            "forcing legislature and executive to discharge constitutional duties.\n\n"
            "- Also called **judicial dynamism**.\n"
            "- Antithesis: **judicial restraint** (self-control by courts).\n"
            "- Contrast with **judicial pessimism**: interpret law as written, without enhancing "
            "its beneficial social reach.\n\n"
            "## Origin\n\n"
            "- **USA, 1947:** Arthur Schlesinger Jr. coins the term (*Fortune* — "
            "“The Supreme Court: 1947”).\n"
            "- **India, mid-1970s:** Foundations by Justices **V.R. Krishna Iyer**, "
            "**P.N. Bhagwati**, **O. Chinnappa Reddy**, **D.A. Desai**.\n\n"
            "## Five definitional strands (flashcards)\n\n"
            "1. **Social engineering** — depart from strict precedent for progressive policy "
            "(may intrude on legislative/executive space).\n"
            "2. **Rights expansion** — protect/expand individual rights even against "
            "precedent or supposed legislative intent.\n"
            "3. **Judicial legislation** — active interpretation to enhance social utility of law "
            "(vs judicial pessimism).\n"
            "4. **Policy-guided judging** — personal public-policy views help guide decisions.\n"
            "5. **New standing & societal litigation** — evolve principles, expand locus standi, "
            "entertain litigation affecting society or a section of it.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 28",
                "Meaning, origin (Schlesinger 1947), Indian founders, five definitions.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ja-origin-timeline",
                "type": "timeline",
                "title": "Origin timeline",
                "events": [
                    {
                        "id": "e1947",
                        "year": 1947,
                        "label": "Term coined (USA)",
                        "detail": "Arthur Schlesinger Jr. in Fortune magazine.",
                    },
                    {
                        "id": "e1970s",
                        "year": 1975,
                        "label": "India mid-1970s",
                        "detail": "Doctrine introduced; activist foundations laid.",
                    },
                    {
                        "id": "e-founders",
                        "year": 1978,
                        "label": "Founding judges",
                        "detail": "Krishna Iyer, Bhagwati, Chinnappa Reddy, Desai.",
                    },
                ],
            },
            {
                "id": "ja-meaning-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Who coined ‘judicial activism’? Arthur Schlesinger Jr. (1947). "
                    "India’s foundation judges: Krishna Iyer, Bhagwati, Chinnappa Reddy, Desai. "
                    "Dynamism = activism; opposite = restraint."
                ),
            },
        ],
    },
    {
        "title": "Two Aspects (Indian Practice)",
        "slug": "ja-two-aspects",
        "sort_order": 2,
        "summary": (
            "Indian judicial activism has two faces: directions via PIL, and expansive "
            "interpretation of Arts 14, 19 and 21."
        ),
        "body": (
            "## Two major aspects\n\n"
            "### 1. Directions to government (PIL vehicle)\n\n"
            "Courts issue directions to authorities for protecting rights and fulfilling "
            "public interest. **Public Interest Litigation (PIL)** is the main procedural "
            "vehicle — expanded locus standi lets public-spirited persons approach courts "
            "for the voiceless.\n\n"
            "→ Drill deep in **Public Interest Litigation** (Ch.29).\n\n"
            "### 2. Expansive Fundamental Rights reading\n\n"
            "Especially:\n"
            "- **Article 14** — equality / non-arbitrariness.\n"
            "- **Article 19** — freedoms.\n"
            "- **Article 21** — life and personal liberty (widest activist canvas).\n\n"
            "Courts have enlarged these rights through interpretation — the second face of "
            "Indian activism.\n"
        ),
        "articles": [
            ("Art. 14", "Equality — expanded against arbitrariness."),
            ("Art. 19", "Freedoms — interpreted with activist lens."),
            ("Art. 21", "Life & liberty — primary expansion field."),
        ],
        "visual_blocks": [
            {
                "id": "ja-two-pillars",
                "type": "pillars",
                "title": "Two faces of Indian JA",
                "items": [
                    {
                        "id": "pil",
                        "articles": "Aspect 1",
                        "label": "PIL directions",
                        "slug": "public-interest-litigation",
                        "detail": "Court orders to State for rights / public interest.",
                        "tone": "teal",
                    },
                    {
                        "id": "fr",
                        "articles": "Aspect 2",
                        "label": "FR expansion",
                        "slug": "fr-life-liberty-21",
                        "detail": "Arts 14, 19, 21 read liberally for justice.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "ja-aspects-flow",
                "type": "flowchart",
                "title": "How activism reaches the courtroom",
                "root": "harm",
                "steps": [
                    {
                        "id": "harm",
                        "label": "Rights / public interest at stake",
                        "detail": "Citizens or groups face State failure or rights denial.",
                        "options": [
                            {"label": "Proxy / societal petition", "next": "pil"},
                            {"label": "FR interpretation path", "next": "fr"},
                        ],
                    },
                    {
                        "id": "pil",
                        "label": "Expanded locus standi (PIL)",
                        "detail": "Court entertains public-interest matter → issues directions.",
                        "slug": "public-interest-litigation",
                    },
                    {
                        "id": "fr",
                        "label": "Expansive Arts 14 / 19 / 21",
                        "detail": "Creative constitutional reading to make rights real.",
                        "slug": "fr-life-liberty-21",
                    },
                ],
            },
        ],
    },
    {
        "title": "Judicial Review vs Judicial Activism",
        "slug": "ja-review-vs-activism",
        "sort_order": 3,
        "summary": (
            "JR interprets law against the Constitution; JA is the creative / "
            "policy-oriented use of that power — often conflated in Indian debate."
        ),
        "body": (
            "## Exam hook\n\n"
            "**JR = interpret within the Constitution; JA = creative / policy-oriented use of JR.**\n\n"
            "Since mid-20th century (esp. USA), a version of judicial review acquired the "
            "nickname ‘judicial activism’. In India, debates often **mix up** the two.\n\n"
            "## Five contrasts (revision)\n\n"
            "1. **JR** interprets law against constitutional parameters; "
            "**JA** moulds law for changing socio-economic needs and constitutional ideals.\n"
            "2. **JR** upholds or invalidates laws; **JA** adds judges’ **policy preferences** "
            "while doing so (activism as a form of review).\n"
            "3. **JR** is the core constitutional check; **JA** stresses a powerful judiciary "
            "protecting **core rights**.\n"
            "4. Expanded **locus standi** (PIL) enlarges review’s reach — critics label this activism.\n"
            "5. At the broadest level, activism under constitutional cases falls under the "
            "rubric of judicial review (any strike-down of enacted law).\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 28",
                "Five contrasts between judicial review and judicial activism.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ja-jr-comparison",
                "type": "comparison",
                "title": "Judicial Review vs Judicial Activism",
                "columns": [
                    {
                        "id": "jr",
                        "heading": "Judicial Review",
                        "points": [
                            "Interpret law vs Constitution",
                            "Uphold or strike on constitutional grounds",
                            "Core check & balance",
                            "Traditional standing (classic)",
                            "Parent doctrine",
                        ],
                    },
                    {
                        "id": "ja",
                        "heading": "Judicial Activism",
                        "points": [
                            "Mould law for socio-economic change",
                            "Same + judges’ policy preferences",
                            "Powerful judiciary + core rights",
                            "Expanded locus standi (PIL)",
                            "Form / nickname of review",
                        ],
                    },
                ],
            },
            {
                "id": "ja-jr-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Do not treat JR and JA as unrelated. Activism is a style/intensity of "
                    "using review — especially when courts invent policy or expand standing. "
                    "Saying ‘India has JR but not JA’ is usually wrong."
                ),
            },
        ],
    },
    {
        "title": "Why Activism Arises",
        "slug": "ja-justification",
        "sort_order": 4,
        "summary": (
            "Wadehra’s five reasons and Kashyap’s six eventualities — when courts "
            "overstep the ‘normal’ lane."
        ),
        "body": (
            "## Dr. B.L. Wadehra — five reasons\n\n"
            "1. **Collapse of responsible government** — legislature/executive fail → "
            "erosion of confidence in Constitution and democracy.\n"
            "2. **Citizen pressure** — people look to courts for rights → judiciary steps in.\n"
            "3. **Judicial enthusiasm** — judges join social reform → PIL + liberal locus standi.\n"
            "4. **Legislative vacuum** — unlegislated areas → judicial legislation.\n"
            "5. **Constitutional space** — Constitution itself gives judiciary room for an active role.\n\n"
            "## Subhash Kashyap — six eventualities\n\n"
            "1. Legislature fails its responsibilities.\n"
            "2. **Hung / weak** government — survival politics, fear of hard decisions.\n"
            "3. Power-holders **park hard issues** in courts to delay or shift odium.\n"
            "4. Failure to protect basic rights / decent life / just administration.\n"
            "5. Authoritarian majority **misuses courts** (Emergency aberration).\n"
            "6. Judges’ **populism / media** craving — human weakness of the bench.\n\n"
            "**Mains tip:** Always pair justification with a restraint / overreach caveat.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 28",
                "Wadehra five reasons; Kashyap six eventualities.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ja-why-flow",
                "type": "flowchart",
                "title": "When does JA kick in?",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "Elected organs under strain?",
                        "detail": "Collapse, hung House, vacuum, or rights failure.",
                        "options": [
                            {"label": "Yes — organs fail / vacuum", "next": "court"},
                            {"label": "Hard issue parked in court", "next": "park"},
                            {"label": "Judges push reform themselves", "next": "enth"},
                        ],
                    },
                    {
                        "id": "court",
                        "label": "Citizen pressure → court steps in",
                        "detail": "Wadehra: confidence erosion + rights protection demand.",
                    },
                    {
                        "id": "park",
                        "label": "Political hot potato → judiciary",
                        "detail": "Kashyap: delay or shift odium of hard decisions.",
                    },
                    {
                        "id": "enth",
                        "label": "Judicial enthusiasm / PIL",
                        "detail": "Liberal locus standi; risk of populism (Kashyap #6).",
                    },
                ],
            },
            {
                "id": "ja-why-mains",
                "type": "callout",
                "tone": "tip",
                "title": "Mains value-add",
                "body": (
                    "Structure an answer: (1) define JA, (2) Wadehra/Kashyap ‘why’, "
                    "(3) Indian faces PIL + 14/19/21, (4) Baxi fears / SC restraint close. "
                    "Never only praise activism."
                ),
            },
        ],
    },
    {
        "title": "Who Activates It (Baxi 15)",
        "slug": "ja-activators",
        "sort_order": 5,
        "summary": (
            "Upendra Baxi’s fifteen activator types grouped into five memory buckets "
            "for quick revision."
        ),
        "body": (
            "## Baxi’s typology — compressed\n\n"
            "Upendra Baxi lists **15** social/human-rights activator types. For revision, "
            "group them as **R-S-E-I-I** (Rights · Socio-economic · Environment · "
            "Identity/consumer · Institutional petitioners).\n\n"
            "### Rights & liberty\n"
            "Civil rights; custodial rights; child rights; women’s rights.\n\n"
            "### Socio-economic\n"
            "People’s (SE) rights; bonded labour; poverty rights (drought/famine/urban poor).\n\n"
            "### Environment & projects\n"
            "Environmental action; citizen groups against mega irrigation projects.\n\n"
            "### Identity & consumer\n"
            "Indigenous peoples (Fifth & Sixth Schedules); consumer rights groups.\n\n"
            "### Institutional petitioners\n"
            "Bar-based groups; media autonomy groups; lawyer-based groups; "
            "assorted individual petitioners.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 28",
                "Upendra Baxi — fifteen activators of judicial activism.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ja-activator-pillars",
                "type": "pillars",
                "title": "Five activator buckets (Baxi 15)",
                "items": [
                    {
                        "id": "rights",
                        "articles": "4 types",
                        "label": "Rights & liberty",
                        "detail": "Civil · custodial · child · women.",
                        "tone": "teal",
                    },
                    {
                        "id": "socio",
                        "articles": "3 types",
                        "label": "Socio-economic",
                        "detail": "People’s rights · bonded labour · poverty.",
                        "tone": "olive",
                    },
                    {
                        "id": "env",
                        "articles": "2 types",
                        "label": "Environment & projects",
                        "detail": "Pollution · anti–mega irrigation.",
                        "tone": "gold",
                    },
                    {
                        "id": "id-cons",
                        "articles": "2 types",
                        "label": "Identity & consumer",
                        "detail": "5th/6th Schedules · consumer.",
                        "tone": "orange",
                    },
                    {
                        "id": "inst",
                        "articles": "4 types",
                        "label": "Institutional petitioners",
                        "detail": "Bar · media · lawyers · individuals.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "ja-activator-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid · R-S-E-I-I",
                "body": (
                    "**R**ights & liberty · **S**ocio-economic · **E**nvironment · "
                    "**I**dentity/consumer · **I**nstitutional petitioners. "
                    "15 names → 5 buckets; don’t memorise the full list for Prelims."
                ),
            },
        ],
    },
    {
        "title": "Criticisms, Fears & Overreach",
        "slug": "ja-criticisms",
        "sort_order": 6,
        "summary": (
            "Baxi’s six fears — ideological to biographic — and the bridge from "
            "legitimate activism to judicial overreach / adventurism."
        ),
        "body": (
            "## Upendra Baxi — six fears\n\n"
            "| Fear | Exam phrase |\n"
            "|------|-------------|\n"
            "| **Ideological** | Usurping legislature / executive / civil institutions |\n"
            "| **Epistemic** | Lack of specialised knowledge (economy, science…) |\n"
            "| **Management** | Adding to staggering arrears |\n"
            "| **Legitimation** | Ignored orders → faith in courts erodes |\n"
            "| **Democratic** | PIL may deplete democracy’s future potential |\n"
            "| **Biographic** | Judges’ post-superannuation career concerns |\n\n"
            "## Activism → overreach\n\n"
            "- Legitimate **activism** fills gaps and protects core rights.\n"
            "- **Overreach / adventurism** = courts running government, inventing policy "
            "without institutional competence, or embarrassing administration.\n"
            "- Exam trap: **activism ≠ always overreach** — criticise excess, not the "
            "entire rights-protecting role.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 28",
                "Baxi’s six apprehensions of judicial activism.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ja-six-fears",
                "type": "pillars",
                "title": "Baxi’s six fears",
                "items": [
                    {
                        "id": "ideo",
                        "articles": "1",
                        "label": "Ideological",
                        "detail": "Usurpation of other organs.",
                        "tone": "maroon",
                    },
                    {
                        "id": "epis",
                        "articles": "2",
                        "label": "Epistemic",
                        "detail": "Expertise gap.",
                        "tone": "orange",
                    },
                    {
                        "id": "mgmt",
                        "articles": "3",
                        "label": "Management",
                        "detail": "Arrears / workload.",
                        "tone": "gold",
                    },
                    {
                        "id": "legit",
                        "articles": "4",
                        "label": "Legitimation",
                        "detail": "Ignored orders → lost faith.",
                        "tone": "olive",
                    },
                    {
                        "id": "demo",
                        "articles": "5",
                        "label": "Democratic",
                        "detail": "May deplete democracy’s potential.",
                        "tone": "teal",
                    },
                    {
                        "id": "bio",
                        "articles": "6",
                        "label": "Biographic",
                        "detail": "Post-retirement concerns.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "ja-overreach-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Activism is not automatically overreach. Overreach = crossing into "
                    "executive/legislative functions without competence or constitutional "
                    "warrant. Use Baxi’s six fears as a balanced critique checklist."
                ),
            },
        ],
    },
    {
        "title": "Activism vs Restraint",
        "slug": "ja-activism-vs-restraint",
        "sort_order": 7,
        "summary": (
            "Restraint philosophy, six US assumptions (five fit India), and the "
            "December 2007 Supreme Court anti-adventurism warning."
        ),
        "body": (
            "## Meaning of judicial restraint\n\n"
            "Judges should **say what the law is**, leave law-making to legislators/executives, "
            "and not let personal political values colour opinions. Guided by "
            "**original intent** of the Constitution’s authors.\n\n"
            "## Assumptions of restraint (USA → India)\n\n"
            "1. Court is unelected → defer to democratic branches.\n"
            "2. Questionable origins of judicial review *(USA-specific — less apt for India)*.\n"
            "3. Separation of powers.\n"
            "4. Federalism — deference to states.\n"
            "5. Dependence on legislature & public acceptance → don’t overstep.\n"
            "6. Law as reason vs politics as power — stay above politics.\n\n"
            "**Prelims:** All except #2 hold good in the Indian context too.\n\n"
            "## Supreme Court warning (Dec 2007)\n\n"
            "*Divisional Manager, Aravali Golf Club v. Chander Hass* (reported 2008) — "
            "Laxmikanth cites *The Hindu*, 11 Dec 2007.\n\n"
            "Revision bullets:\n"
            "1. Judges must not take over executive/legislative functions — unconstitutional.\n"
            "2. Know limits; modesty; not ‘emperors’.\n"
            "3. Montesquieu (*Spirit of Laws*) — overreach warning for Indian judiciary.\n"
            "4. Activism must not become **judicial adventurism**; minimise personal preferences.\n"
            "5. Don’t embarrass administration; executives have field expertise.\n"
            "6. ‘Other organs failing’ is no licence — judiciary has its own arrears; "
            "remedy = franchise / peaceful protest; judiciary lacks expertise & resources; "
            "restraint protects balance **and** judicial independence.\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 28",
                "Restraint meaning, six assumptions, Dec 2007 SC observations.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ja-restraint-compare",
                "type": "comparison",
                "title": "Activism vs Restraint",
                "columns": [
                    {
                        "id": "act",
                        "heading": "Judicial Activism",
                        "points": [
                            "Proactive / assertive role",
                            "May mould law & policy",
                            "Expanded standing / PIL",
                            "Social engineering impulse",
                            "Risk: adventurism / overreach",
                        ],
                    },
                    {
                        "id": "res",
                        "heading": "Judicial Restraint",
                        "points": [
                            "Self-control; say what law is",
                            "Defer law-making to elected organs",
                            "Original intent guidance",
                            "Respect separation of powers",
                            "Protects balance + independence",
                        ],
                    },
                ],
            },
            {
                "id": "ja-aravali-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims / quote anchors",
                "body": (
                    "‘Judges must not behave like emperors.’ "
                    "‘Judicial activism must not become judicial adventurism.’ "
                    "Case cue: Aravali Golf Club (Dec 2007 / 2008). "
                    "Assumption #2 on JR origins is the USA-only exception."
                ),
            },
        ],
    },
    {
        "title": "Landmark Case Map",
        "slug": "ja-landmark-map",
        "sort_order": 8,
        "summary": (
            "Curated landmarks illustrating FR expansion, PIL activism, legislative vacuum, "
            "and the restraint warning — full PIL depth in Ch.29."
        ),
        "body": (
            "## How to use this map\n\n"
            "Ch.28 is concept-heavy; these cases illustrate its **two aspects** and the "
            "**restraint** closer. One-line holdings below — expand in PIL / Art.21 clusters.\n\n"
            "| Case | Year | Angle |\n"
            "|------|------|-------|\n"
            "| *Maneka Gandhi* | 1978 | Art.21 — procedure must be fair, just, reasonable |\n"
            "| *Hussainara Khatoon* | 1979 | Speedy trial; early activist Art.21 phase |\n"
            "| *Bandhua Mukti Morcha* | 1984 | Bonded labour; PIL standing |\n"
            "| *Olga Tellis* | 1985 | Livelihood under Art.21 |\n"
            "| *M.C. Mehta* (Oleum/Ganga line) | 1986–87 | Environment as activism vehicle |\n"
            "| *Vishaka* | 1997 | Guidelines filling legislative vacuum |\n"
            "| *Aravali Golf Club* | 2007–08 | Restraint; anti-adventurism |\n\n"
            "→ Full PIL case bank: **Public Interest Litigation** chapter.\n"
        ),
        "articles": [
            ("Art. 21", "Primary expansion field for activist jurisprudence."),
            ("Art. 32 / 226", "Writ door for PIL-style activism."),
        ],
        "visual_blocks": [
            {
                "id": "ja-case-network",
                "type": "case_network",
                "title": "Activism landmark network",
                "hub_label": "Judicial Activism",
                "cases": [
                    {
                        "id": "maneka",
                        "label": "Maneka Gandhi",
                        "year": 1978,
                        "detail": "Art.21 expansion — fair procedure.",
                        "case_slug": "maneka-gandhi",
                    },
                    {
                        "id": "hussainara",
                        "label": "Hussainara Khatoon",
                        "year": 1979,
                        "detail": "Speedy trial; undertrial rights.",
                        "case_slug": "hussainara-khatoon",
                    },
                    {
                        "id": "bmm",
                        "label": "Bandhua Mukti Morcha",
                        "year": 1984,
                        "detail": "Bonded labour; PIL standing.",
                        "case_slug": "bandhua-mukti-morcha",
                    },
                    {
                        "id": "olga",
                        "label": "Olga Tellis",
                        "year": 1985,
                        "detail": "Livelihood as part of Art.21.",
                        "case_slug": "olga-tellis",
                    },
                    {
                        "id": "mcmehta",
                        "label": "M.C. Mehta",
                        "year": 1987,
                        "detail": "Environmental activism vehicle.",
                        "case_slug": "mc-mehta-oleum",
                    },
                    {
                        "id": "vishaka",
                        "label": "Vishaka",
                        "year": 1997,
                        "detail": "Guidelines in legislative vacuum.",
                        "case_slug": "vishaka",
                    },
                    {
                        "id": "aravali",
                        "label": "Aravali Golf Club",
                        "year": 2008,
                        "detail": "Restraint; no judicial emperors.",
                        "case_slug": "aravali-golf-club",
                    },
                ],
            },
            {
                "id": "ja-cases-note",
                "type": "callout",
                "tone": "tip",
                "title": "Revision note",
                "body": (
                    "Link cases to aspect: Maneka/Hussainara/Olga → Art.21 face; "
                    "Bandhua/M.C. Mehta → PIL face; Vishaka → legislative vacuum; "
                    "Aravali → restraint closer. Deep PIL digests live in Ch.29."
                ),
            },
        ],
    },
    {
        "title": "Exam Anchors",
        "slug": "ja-exam-anchors",
        "sort_order": 9,
        "summary": (
            "Prelims facts, PYQ themes, mains value-adds, memory aids, and last-minute "
            "revision sheet."
        ),
        "body": (
            "## Prelims facts\n\n"
            "- Term coined **1947** by **Arthur Schlesinger Jr.** (*Fortune*).\n"
            "- India mid-1970s; founders: Krishna Iyer, Bhagwati, Chinnappa Reddy, Desai.\n"
            "- Dynamism = activism; opposite = restraint; excess = **adventurism**.\n"
            "- Indian faces: **PIL** + Arts **14, 19, 21**.\n"
            "- Baxi 6 fear labels: ideological, epistemic, management, legitimation, "
            "democratic, biographic.\n"
            "- Restraint assumption #2 (JR origins) is **USA-only**.\n"
            "- Aravali Golf Club / Dec 2007: judges not emperors; activism ≠ adventurism.\n\n"
            "## PYQ themes\n\n"
            "- Distinguish **judicial review** and **judicial activism**.\n"
            "- Activism vs **restraint**; meaning of adventurism.\n"
            "- When activism is **justified** (Wadehra/Kashyap).\n"
            "- Risks of **overreach**; separation of powers.\n"
            "- PIL as a **form** of activism.\n\n"
            "## Mains value-adds\n\n"
            "- **Why:** Wadehra 5 + Kashyap 6.\n"
            "- **Critique:** Baxi 6 fears.\n"
            "- **Close:** Aravali / Dec 2007 balanced paragraph.\n\n"
            "## Memory spine\n\n"
            "1. JA = rights + justice + push other organs.\n"
            "2. Two faces: PIL directions + 14/19/21.\n"
            "3. **Justify → Activate → Fear → Restrain.**\n"
        ),
        "articles": [
            (
                "Laxmikanth Ch. 28",
                "Full chapter revision sheet — prelims, mains, memory.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "ja-exam-pillars",
                "type": "pillars",
                "title": "Exam three-pack",
                "items": [
                    {
                        "id": "pre",
                        "articles": "Facts",
                        "label": "Prelims",
                        "detail": "1947 · founders · 14/19/21 · adventurism · Aravali.",
                        "tone": "teal",
                    },
                    {
                        "id": "mains",
                        "articles": "Structure",
                        "label": "Mains",
                        "detail": "Define → why → faces → fears → restraint close.",
                        "tone": "olive",
                    },
                    {
                        "id": "traps",
                        "articles": "Avoid",
                        "label": "Traps",
                        "detail": "JR≠JA unrelated; activism≠always overreach; #2 USA-only.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "ja-revision-sheet",
                "type": "callout",
                "tone": "tip",
                "title": "60-second revision",
                "body": (
                    "Safety valve → two faces (PIL + 14/19/21) → JR parent / JA style → "
                    "Wadehra+Kashyap why → Baxi R-S-E-I-I activators → six fears → "
                    "restraint + Aravali. Justify → Activate → Fear → Restrain."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "ja-meaning-origin"),
    (HUB_SLUG, "parent", "ja-two-aspects"),
    (HUB_SLUG, "parent", "ja-review-vs-activism"),
    (HUB_SLUG, "parent", "ja-justification"),
    (HUB_SLUG, "parent", "ja-activators"),
    (HUB_SLUG, "parent", "ja-criticisms"),
    (HUB_SLUG, "parent", "ja-activism-vs-restraint"),
    (HUB_SLUG, "parent", "ja-landmark-map"),
    (HUB_SLUG, "parent", "ja-exam-anchors"),
    ("ja-two-aspects", "related", "public-interest-litigation"),
    ("ja-two-aspects", "related", "fr-life-liberty-21"),
    ("ja-review-vs-activism", "related", "supreme-court"),
    ("ja-review-vs-activism", "related", "basic-structure"),
    ("ja-landmark-map", "related", "public-interest-litigation"),
    ("ja-landmark-map", "related", "fr-life-liberty-21"),
    ("ja-activism-vs-restraint", "related", "ja-criticisms"),
    ("ja-justification", "related", "ja-criticisms"),
    ("ja-exam-anchors", "related", "ja-review-vs-activism"),
]

SAMPLE_PYQS = [
    (
        2018,
        "Judicial activism and judicial review are often used interchangeably in Indian debates. "
        "How are they related yet distinct?",
        "Judicial review is interpretation of law against constitutional parameters; "
        "judicial activism is a creative/policy-oriented form of that power — moulding law "
        "for socio-economic needs and core rights, often via expanded standing (PIL).",
        [HUB_SLUG, "ja-review-vs-activism"],
    ),
    (
        2015,
        "Distinguish between judicial activism and judicial restraint. Why has the Supreme Court "
        "cautioned against judicial adventurism?",
        "Activism = assertive rights/justice role; restraint = say what law is, defer "
        "law-making, original intent. Adventurism = courts taking over executive/legislative "
        "functions — Aravali Golf Club (Dec 2007) warned judges are not emperors.",
        ["ja-activism-vs-restraint", "ja-exam-anchors"],
    ),
    (
        2012,
        "Under what circumstances may judicial activism be justified in a constitutional democracy?",
        "Wadehra/Kashyap: collapse of responsible government, legislative vacuum, rights "
        "protection failure, hung/weak governments, hard decisions parked in courts — "
        "balanced by separation of powers and restraint.",
        ["ja-justification", HUB_SLUG],
    ),
    (
        2020,
        "Public Interest Litigation is often described as a form of judicial activism. Explain.",
        "PIL expands locus standi and invites court directions to government for public "
        "interest/rights — Aspect 1 of Indian judicial activism (alongside expansive Arts 14/19/21).",
        ["ja-two-aspects", "public-interest-litigation"],
    ),
    (
        2009,
        "Critically examine the apprehensions associated with judicial activism in India.",
        "Baxi’s six fears: ideological (usurpation), epistemic (expertise), management "
        "(arrears), legitimation (ignored orders), democratic (PIL depleting democracy), "
        "biographic (post-retirement). Activism ≠ always overreach.",
        ["ja-criticisms", "ja-exam-anchors"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Maneka Gandhi v. Union of India",
        "slug": "maneka-gandhi",
        "parties": "Maneka Gandhi v. Union of India",
        "year": 1978,
        "court": CaseLaw.Court.SC,
        "summary": "Landmark expansion of Article 21 — procedure must be fair, just and reasonable.",
        "holding": (
            "‘Procedure established by law’ under Art.21 must be fair, just and reasonable; "
            "Arts 14, 19 and 21 form a golden triangle of mutual reinforcement."
        ),
        "concept_slugs": [HUB_SLUG, "ja-landmark-map", "ja-two-aspects"],
    },
    {
        "title": "Hussainara Khatoon v. State of Bihar",
        "slug": "hussainara-khatoon",
        "parties": "Hussainara Khatoon v. State of Bihar",
        "year": 1979,
        "court": CaseLaw.Court.SC,
        "summary": "Speedy trial as part of Art.21; early wave of activist undertrial jurisprudence.",
        "holding": (
            "Right to speedy trial is an essential ingredient of Art.21; prolonged undertrial "
            "detention without trial violates personal liberty."
        ),
        "concept_slugs": [HUB_SLUG, "ja-landmark-map", "ja-two-aspects"],
    },
    {
        "title": "Bandhua Mukti Morcha v. Union of India",
        "slug": "bandhua-mukti-morcha",
        "parties": "Bandhua Mukti Morcha v. Union of India",
        "year": 1984,
        "court": CaseLaw.Court.SC,
        "summary": "Bonded labour PIL — expanded standing and socio-economic rights activism.",
        "holding": (
            "Public-spirited persons may approach the Court for bonded labourers; "
            "Art.21 includes dignity and freedom from forced labour contexts."
        ),
        "concept_slugs": [HUB_SLUG, "ja-landmark-map", "ja-activators"],
    },
    {
        "title": "Olga Tellis v. Bombay Municipal Corporation",
        "slug": "olga-tellis",
        "parties": "Olga Tellis v. Bombay Municipal Corporation",
        "year": 1985,
        "court": CaseLaw.Court.SC,
        "summary": "Livelihood read into Article 21 for pavement dwellers.",
        "holding": (
            "Right to livelihood is an integral facet of the right to life under Art.21; "
            "eviction must respect fair procedure."
        ),
        "concept_slugs": [HUB_SLUG, "ja-landmark-map", "ja-two-aspects"],
    },
    {
        "title": "M.C. Mehta v. Union of India (Oleum Gas Leak)",
        "slug": "mc-mehta-oleum",
        "parties": "M.C. Mehta v. Union of India",
        "year": 1987,
        "court": CaseLaw.Court.SC,
        "summary": "Environmental activism vehicle — absolute liability and public interest litigation.",
        "holding": (
            "Enterprises engaged in hazardous activities owe absolute liability for harm; "
            "environment/public safety as core activist PIL field."
        ),
        "concept_slugs": [HUB_SLUG, "ja-landmark-map", "ja-activators"],
    },
    {
        "title": "Vishaka v. State of Rajasthan",
        "slug": "vishaka",
        "parties": "Vishaka v. State of Rajasthan",
        "year": 1997,
        "court": CaseLaw.Court.SC,
        "summary": "Sexual harassment guidelines filling a legislative vacuum — classic activism.",
        "holding": (
            "In the absence of enacted law, Court laid down binding workplace sexual harassment "
            "guidelines under Arts 14, 19 and 21 until Parliament legislates."
        ),
        "concept_slugs": [HUB_SLUG, "ja-landmark-map", "ja-justification"],
    },
    {
        "title": "Divisional Manager, Aravali Golf Club v. Chander Hass",
        "slug": "aravali-golf-club",
        "parties": "Divisional Manager, Aravali Golf Club v. Chander Hass",
        "year": 2008,
        "court": CaseLaw.Court.SC,
        "summary": (
            "December 2007 restraint warning — activism must not become adventurism; "
            "judges are not emperors."
        ),
        "holding": (
            "Courts must not take over legislative or executive functions; judicial activism "
            "must not become judicial adventurism; restraint protects separation of powers "
            "and judicial independence."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "ja-landmark-map",
            "ja-activism-vs-restraint",
            "ja-exam-anchors",
        ],
    },
]


class Command(BaseCommand):
    help = "Seed Judicial Activism chapter (Laxmikanth Ch.28 visual revision)."

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
                "title": "Judicial Activism",
                "sort_order": 13,
                "book_ref": "Laxmikanth 8th Ed, Ch. 28, pp. 438–444",
                "summary": (
                    "Visual revision of Ch.28 — meaning, JR vs JA, justifications, "
                    "Baxi activators/fears, activism vs restraint, landmarks, exam anchors."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Judicial Activism",
                "summary": (
                    "Assertive use of judicial review for rights and justice — "
                    "opposite of restraint; excess is adventurism."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **safety valve** mental model, then scan the nine stops. "
                    "Lock **JR vs JA** and **activism vs restraint**, then Wadehra/Kashyap "
                    "justifications and Baxi fears. Finish with landmarks + exam anchors. "
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
            ref="Laxmikanth Ch. 28",
            excerpt=(
                "Judicial Activism — meaning, JR vs JA, justifications, Baxi lists, "
                "activism vs restraint."
            ),
            sort_order=0,
        )

        ja_slugs = set(by_slug.keys())
        related_outside = {
            "public-interest-litigation",
            "fr-life-liberty-21",
            "supreme-court",
            "basic-structure",
        }
        ConceptEdge.objects.filter(
            Q(source__slug__in=ja_slugs) | Q(target__slug__in=ja_slugs),
            source__subject=subject,
        ).filter(
            Q(source__slug__in=ja_slugs | related_outside)
            | Q(target__slug__in=ja_slugs | related_outside)
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
            # Also link external concept slugs when present.
            for s in slugs:
                if s not in by_slug:
                    extra = Concept.objects.filter(subject=subject, slug=s).first()
                    if extra:
                        concepts.append(extra)
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

        self.stdout.write(
            self.style.SUCCESS(
                f"Judicial Activism chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(SAMPLE_PYQS)} PYQs."
            )
        )
