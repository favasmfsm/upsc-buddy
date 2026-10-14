"""Seed Laxmikanth Ch.29 Public Interest Litigation (visual revision)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "public-interest-litigation"
CHAPTER_SLUG = "public-interest-litigation"

ENTRY_PILLARS = [
    {
        "id": "meaning",
        "articles": "Locus standi",
        "label": "Meaning & locus standi",
        "slug": "pil-meaning",
        "detail": "Sufficient interest; proxy for those who cannot knock.",
        "tone": "teal",
    },
    {
        "id": "evolution",
        "articles": "1960s → 2010",
        "label": "Evolution timeline",
        "slug": "pil-evolution",
        "detail": "USA → India 1980s → SC guidelines → misuse curbs.",
        "tone": "olive",
    },
    {
        "id": "vs-trad",
        "articles": "9 features",
        "label": "PIL vs traditional",
        "slug": "pil-vs-traditional",
        "detail": "Cooperative, public, assertive court — not adversarial duel.",
        "tone": "gold",
    },
    {
        "id": "const",
        "articles": "32 · 226 · 14 · 21 · 142",
        "label": "Constitution & procedure",
        "slug": "pil-constitutional-procedure",
        "detail": "Writ door, epistolary path, commissions, hard limits.",
        "tone": "orange",
    },
    {
        "id": "scope",
        "articles": "10 vs 5",
        "label": "Scope: entertainable",
        "slug": "pil-scope",
        "detail": "1988 SC letter categories — what is in, what is out.",
        "tone": "terracotta",
    },
    {
        "id": "principles",
        "articles": "Guruvayur 12",
        "label": "Twelve principles",
        "slug": "pil-principles",
        "detail": "Access · substance · tools · limits — one case spine.",
        "tone": "maroon",
    },
    {
        "id": "misuse",
        "articles": "8 guidelines",
        "label": "Misuse & reforms",
        "slug": "pil-misuse",
        "detail": "5P + MIL; Balwant Singh Chaupal admission rules.",
        "tone": "teal",
    },
    {
        "id": "landmarks",
        "articles": "Core + classics",
        "label": "Landmark cases",
        "slug": "pil-landmarks",
        "detail": "Book trio + short UPSC classic bank.",
        "tone": "olive",
    },
    {
        "id": "exam",
        "articles": "Prelims · Mains",
        "label": "Exam revision",
        "slug": "pil-exam-revision",
        "detail": "Facts strip, PYQ themes, mains value-adds, traps.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pil-load-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "A public-spirited proxy who knocks the court door for those who cannot",
        "topic_label": "Public Interest Litigation",
        "subject_label": "Judicial activism · Ch. 29",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating PIL as a private dispute duel",
            "Confusing Art. 32 with Art. 226",
            "Thinking High Courts have Art. 142 power",
            "Memorising only the ‘entertained’ list",
            "Calling every letter a PIL without SC category filters",
        ],
        "insight": (
            "Relaxed locus standi for public interest — cooperative justice for the "
            "disadvantaged, not a panacea for every grievance."
        ),
    },
    {
        "id": "pil-entry-pillars",
        "type": "pillars",
        "title": "Nine revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "pil-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Scan Meaning → Evolution → vs Traditional → Arts & procedure → "
            "Scope 10/5 → 12 principles → Misuse 8 + 5P/MIL → Cases → Exam box. "
            "Anchors: Iyer + Bhagwati; Arts 32/226/14/21/142; Guruvayur 2003; "
            "Balwant Singh Chaupal 2010."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Meaning & Locus Standi",
        "slug": "pil-meaning",
        "sort_order": 1,
        "summary": (
            "PIL relaxes traditional locus standi — any public-spirited person with "
            "sufficient interest can seek enforcement of others’ rights."
        ),
        "body": (
            "## One-liner\n\n"
            "PIL = legal action for **public / general interest** where a class of the "
            "community has rights or liabilities affected.\n\n"
            "## Who may file?\n\n"
            "- Public-spirited **citizen** or **social organisation**\n"
            "- On behalf of persons unable to approach court due to poverty, ignorance, "
            "or social/economic disadvantage\n"
            "- Test: **sufficient interest** (not personal injury alone)\n\n"
            "## Three real purposes\n\n"
            "1. Vindication of the **rule of law**\n"
            "2. Effective **access to justice** for weaker sections\n"
            "3. Meaningful realisation of **fundamental rights**\n\n"
            "## Memory aid\n\n"
            "**PIL = Proxy for the Invisible Low-visibility** poor."
        ),
        "articles": [
            (
                "Locus standi",
                "Traditional rule: only the injured person may move the court; PIL is the exception.",
            ),
            (
                "Sufficient interest",
                "Any member of the public with sufficient interest may seek enforcement of others’ rights / common grievance.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pil-meaning-compare",
                "type": "comparison",
                "title": "Traditional locus standi vs PIL",
                "columns": [
                    {
                        "id": "traditional",
                        "heading": "Traditional rule",
                        "points": [
                            "Only the person whose right is infringed can sue",
                            "Strict personal injury / standing",
                            "Private dispute framing",
                            "Barrier for poor / voiceless",
                        ],
                    },
                    {
                        "id": "pil",
                        "heading": "PIL exception",
                        "points": [
                            "Public-spirited citizen / social org may sue",
                            "‘Sufficient interest’ standard",
                            "Public / class / diffused rights",
                            "Door opened for disadvantaged",
                        ],
                    },
                ],
            },
            {
                "id": "pil-meaning-tip",
                "type": "callout",
                "tone": "tip",
                "title": "SC definition (compressed)",
                "body": (
                    "Legal action for enforcement of **public interest or general interest** "
                    "in which the public or a class of the community have pecuniary interest "
                    "or some interest affecting their legal rights or liabilities."
                ),
            },
        ],
    },
    {
        "title": "Evolution & Origin",
        "slug": "pil-evolution",
        "sort_order": 2,
        "summary": (
            "USA 1960s origin; India early 1980s via Krishna Iyer and Bhagwati; "
            "PIL as the leading face of judicial activism."
        ),
        "body": (
            "## Origin story\n\n"
            "- **USA, 1960s** — legal representation for unrepresented groups "
            "(poor, environmentalists, consumers, racial/ethnic minorities)\n"
            "- **India, early 1980s** — pioneered by Justices **V.R. Krishna Iyer** "
            "and **P.N. Bhagwati**\n"
            "- Closely tied to **judicial activism**; PIL = most popular form / "
            "manifestation of activism\n\n"
            "## Also known as\n\n"
            "- Social Action Litigation (**SAL**)\n"
            "- Social Interest Litigation (**SIL**)\n"
            "- Class Action Litigation (**CAL**)\n\n"
            "## Guideline milestones\n\n"
            "SC letter/petition categories: **1988** → modified **1993** & **2003**. "
            "Misuse curbs crystallised in **Balwant Singh Chaupal (2010)**."
        ),
        "articles": [
            (
                "Judicial activism",
                "PIL is an outcome — and the most popular form — of the Supreme Court’s judicial activism.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pil-evolution-tl",
                "type": "timeline",
                "title": "PIL evolution (revision spine)",
                "events": [
                    {
                        "id": "e1960s",
                        "year": 1960,
                        "label": "USA origin",
                        "detail": "1960s — legal aid for unrepresented groups and interests.",
                    },
                    {
                        "id": "e1980s",
                        "year": 1980,
                        "label": "India introduces PIL",
                        "detail": "Early 1980s — Krishna Iyer + Bhagwati pioneer the concept.",
                    },
                    {
                        "id": "e1988",
                        "year": 1988,
                        "label": "SC letter guidelines",
                        "detail": "Categories for entertaining letters/petitions as PIL.",
                    },
                    {
                        "id": "e1993",
                        "year": 1993,
                        "label": "Guidelines modified",
                        "detail": "Scope list refined (again in 2003).",
                    },
                    {
                        "id": "e2003",
                        "year": 2003,
                        "label": "Guruvayur + 2003 mods",
                        "detail": "12 principles (Guruvayur); letter guidelines modified again.",
                    },
                    {
                        "id": "e2010",
                        "year": 2010,
                        "label": "Balwant Singh Chaupal",
                        "detail": "Eight admission guidelines to curb misuse.",
                    },
                ],
            },
            {
                "id": "pil-evolution-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook",
                "body": (
                    "India: **early 1980s**. Pioneers: **Krishna Iyer + Bhagwati**. "
                    "Also called **SAL / SIL / CAL**. PIL = top form of **judicial activism**."
                ),
            },
        ],
    },
    {
        "title": "PIL vs Traditional Litigation",
        "slug": "pil-vs-traditional",
        "sort_order": 3,
        "summary": (
            "Nine compressed features — cooperative public-interest justice versus "
            "adversarial private-right adjudication."
        ),
        "body": (
            "## Features (revision spine)\n\n"
            "1. Strategic arm of **legal aid** — justice for the ‘low visibility area of humanity’\n"
            "2. **Not adversarial** like ordinary two-party litigation\n"
            "3. Promotes/vindicates **public interest**, not one individual’s right vs another\n"
            "4. Rights of large numbers of poor/ignorant/disadvantaged must not go unnoticed\n"
            "5. **Co-operative triad**: petitioner + State/Public Authority + Court → social justice\n"
            "6. Redresses public injury; enforces public duty; protects social/collective/**diffused** rights\n"
            "7. Court role more **assertive, creative, positive** (not passive)\n"
            "8. Procedural **flexibility**, but still a **judicial proceeding** with known judicial tenets\n"
            "9. **No adjudication of individual rights** as in traditional dispute resolution\n\n"
            "## Trap\n\n"
            "Flexibility ≠ free-for-all. Procedure must still be recognisably judicial."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pil-vs-compare",
                "type": "comparison",
                "title": "Traditional litigation vs PIL",
                "columns": [
                    {
                        "id": "trad",
                        "heading": "Traditional",
                        "points": [
                            "Adversarial — claim vs resistance",
                            "Private right of one vs another",
                            "Strict locus standi",
                            "Court relatively passive",
                            "Adjudicates individual rights",
                            "Rigid private-law procedure",
                        ],
                    },
                    {
                        "id": "pil",
                        "heading": "PIL",
                        "points": [
                            "Co-operative — petitioner + State + Court",
                            "Public / collective / diffused interest",
                            "Relaxed ‘sufficient interest’",
                            "Court assertive & creative",
                            "No individual-rights adjudication focus",
                            "Flexible but still judicial",
                        ],
                    },
                ],
            },
            {
                "id": "pil-vs-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Procedural flexibility in PIL does **not** mean non-judicial free-for-all. "
                    "Whatever procedure the court adopts must remain known to judicial tenets."
                ),
            },
        ],
    },
    {
        "title": "Constitutional Basis & Procedure",
        "slug": "pil-constitutional-procedure",
        "sort_order": 4,
        "summary": (
            "Arts 32/226 open the door; 14 and 21 supply substance; Art. 142 is SC-only; "
            "epistolary jurisdiction and commissions with hard jurisdictional limits."
        ),
        "body": (
            "## Constitutional hooks\n\n"
            "| Article | Role in PIL |\n"
            "|---------|-------------|\n"
            "| **32** | SC writ jurisdiction — PIL for FR enforcement |\n"
            "| **226** | HC writ jurisdiction — broader, but with limits below |\n"
            "| **14 & 21** | Invoked for large-scale injustice + fair-trial norms |\n"
            "| **142** | SC power to do complete justice — **HC has no akin power** |\n\n"
            "## Procedure highlights\n\n"
            "- **Epistolary jurisdiction** — letter/telegram may be treated as PIL\n"
            "- Prima facie FR violation of disadvantaged → State may not raise maintainability\n"
            "- Court may appoint **Commission**/bodies to investigate; may direct management "
            "of a public institution\n"
            "- Private-interest petition may be expanded into **public-interest enquiry**\n"
            "- *Res judicata* depends on nature/facts — procedural laws still apply\n\n"
            "## Hard limits\n\n"
            "- No pure **private-law** war between two groups as PIL\n"
            "- Ordinarily no entry into **policy**; stay within known **judicial review**\n"
            "- HC ordinarily should **not** entertain PIL questioning **constitutionality** "
            "of a statute/rule\n\n"
            "## Memory\n\n"
            "**32/226 open the door; 14+21 fill the room; 142 is SC-only paintbrush.**"
        ),
        "articles": [
            ("Article 32", "Supreme Court writ jurisdiction — PIL for enforcement of Fundamental Rights."),
            ("Article 226", "High Court writ jurisdiction — can entertain PIL, subject to limits."),
            ("Article 14", "Equality — invoked when large-scale injustice is meted out."),
            ("Article 21", "Life and personal liberty — plus fair-trial norms / IHRL references."),
            ("Article 142", "SC power to do complete justice; High Court has no power akin to Art. 142."),
        ],
        "visual_blocks": [
            {
                "id": "pil-procedure-flow",
                "type": "flowchart",
                "title": "PIL path (decision spine)",
                "root": "who",
                "steps": [
                    {
                        "id": "who",
                        "label": "Who is approaching?",
                        "detail": "Public-spirited person / org with sufficient interest for disadvantaged.",
                        "options": [
                            {"label": "Supreme Court path", "next": "sc"},
                            {"label": "High Court path", "next": "hc"},
                        ],
                    },
                    {
                        "id": "sc",
                        "label": "Article 32",
                        "detail": "Writ PIL for FR; letter/telegram may be treated as petition.",
                        "options": [
                            {"label": "Proceed to process", "next": "process"},
                        ],
                    },
                    {
                        "id": "hc",
                        "label": "Article 226",
                        "detail": "Writ PIL possible — but HC ≠ Art. 142; ordinarily no statute-validity PIL.",
                        "options": [
                            {"label": "Proceed to process", "next": "process"},
                        ],
                    },
                    {
                        "id": "process",
                        "label": "Process tools",
                        "detail": "Epistolary flexibility; commissions; possible expansion of private petition into public enquiry.",
                        "options": [
                            {"label": "Check limits", "next": "limits"},
                        ],
                    },
                    {
                        "id": "limits",
                        "label": "Hard stops",
                        "detail": (
                            "No pure private-law duel; policy restraint; known JR only; "
                            "HC no Art. 142; HC ordinarily no constitutionality PIL."
                        ),
                    },
                ],
            },
            {
                "id": "pil-arts-pillars",
                "type": "pillars",
                "title": "Five constitutional anchors",
                "items": [
                    {
                        "id": "a32",
                        "articles": "Art. 32",
                        "label": "SC writ door",
                        "detail": "PIL for Fundamental Rights enforcement in the Supreme Court.",
                        "tone": "teal",
                    },
                    {
                        "id": "a226",
                        "articles": "Art. 226",
                        "label": "HC writ door",
                        "detail": "Broader HC writs — with statute-validity & Art. 142 limits.",
                        "tone": "olive",
                    },
                    {
                        "id": "a14",
                        "articles": "Art. 14",
                        "label": "Equality substance",
                        "detail": "Large-scale injustice → equality + fair process norms.",
                        "tone": "gold",
                    },
                    {
                        "id": "a21",
                        "articles": "Art. 21",
                        "label": "Life & liberty",
                        "detail": "Core substantive hook; pairs with IHRL fair-trial ideas.",
                        "tone": "orange",
                    },
                    {
                        "id": "a142",
                        "articles": "Art. 142",
                        "label": "SC-only brush",
                        "detail": "Complete justice — High Court has no akin power.",
                        "tone": "terracotta",
                    },
                ],
            },
        ],
    },
    {
        "title": "Scope: Entertained vs Not",
        "slug": "pil-scope",
        "sort_order": 5,
        "summary": (
            "SC 1988 letter guidelines (modified 1993 & 2003) — ten entertainable "
            "categories versus five that will not be entertained as PIL."
        ),
        "body": (
            "## Entertainable (10) — group mnemonic\n\n"
            "**Labour / children**\n"
            "1. Bonded labour  2. Neglected children  "
            "3. Minimum wages / casual-worker exploitation / labour-law violations "
            "(**except individual cases**)\n\n"
            "**Jail / police**\n"
            "4. Jail petitions (harassment, premature release, release after **14 years**, "
            "death in jail, transfer, personal bond, **speedy trial as FR**)  "
            "5. Police (refusal to register, harassment, custodial death)\n\n"
            "**Women / SC-ST / backward**\n"
            "6. Atrocities on women  7. Harassment/torture of villagers (SC/ST & economically backward)\n\n"
            "**Environment / public importance**\n"
            "8. Environment, ecology, drugs, food adulteration, heritage, antiques, forest & wildlife, "
            "other public importance\n\n"
            "**Riot / pension**\n"
            "9. Riot victims  10. **Family pension**\n\n"
            "## Not entertained (5)\n\n"
            "1. Landlord–tenant  2. Service matters; pension & gratuity  "
            "3. Complaints vs govt/local bodies **except** items 1–10  "
            "4. Admission to medical/other educational institutions  "
            "5. Early hearing of pending HC/subordinate cases"
        ),
        "articles": [
            (
                "SC PIL guidelines 1988",
                "Formulated for entertaining letters/petitions as PIL; modified in 1993 and 2003.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pil-scope-compare",
                "type": "comparison",
                "title": "Entertained (10) vs Not entertained (5)",
                "columns": [
                    {
                        "id": "yes",
                        "heading": "Ordinarily entertained",
                        "points": [
                            "Bonded labour; neglected children",
                            "Min. wages / casual labour (not individual)",
                            "Jail petitions (incl. 14 yrs; speedy trial as FR)",
                            "Police refusal / harassment / custodial death",
                            "Atrocities on women; SC/ST / EBC village torture",
                            "Environment, ecology, heritage, wildlife…",
                            "Riot victims; family pension",
                        ],
                    },
                    {
                        "id": "no",
                        "heading": "Not entertained as PIL",
                        "points": [
                            "Landlord–tenant disputes",
                            "Service matters; pension & gratuity",
                            "Govt/local-body complaints outside the 10",
                            "Medical / educational admissions",
                            "Early hearing of pending HC/lower-court cases",
                        ],
                    },
                ],
            },
            {
                "id": "pil-scope-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Three traps inside the list",
                "body": (
                    "(1) Labour category excludes **individual** cases. "
                    "(2) **Speedy trial as FR** sits inside jail petitions. "
                    "(3) **Family pension** is entertainable — do not confuse with "
                    "service/pension & gratuity (not entertained)."
                ),
            },
        ],
    },
    {
        "title": "Twelve Principles of PIL",
        "slug": "pil-principles",
        "sort_order": 6,
        "summary": (
            "Guruvayur Devaswom Managing Committee vs C.K. Rajan (2003) — twelve "
            "principles grouped into Access, Substance, Tools, and Limits."
        ),
        "body": (
            "## Source case\n\n"
            "**Guruvayur Devaswom Managing Committee vs C.K. Rajan (2003)** — "
            "twelve principles of PIL.\n\n"
            "## Full twelve (quick scan)\n\n"
            "1. Interested person may petition for disadvantaged; court bound under **32/226**\n"
            "2. Letter/telegram as PIL; relax procedure & pleadings (**epistolary**)\n"
            "3. Large-scale injustice → **Arts 14 & 21** + IHRL fair-trial norms\n"
            "4. **Locus standi relaxed** for poor, deprived, illiterate, disabled\n"
            "5. Prima facie FR violation → State may not raise maintainability\n"
            "6. Procedural laws apply; **res judicata** depends on nature/facts\n"
            "7. Pure private-law disputes between two groups → **not PIL**\n"
            "8. Private-interest petition may expand into **public-interest enquiry**\n"
            "9. Court may appoint **Commission**; may direct management of public institution\n"
            "10. Ordinarily no entry into **policy**; no jurisdictional overreach\n"
            "11. Stay within known **judicial review**; HC has no power akin to **Art. 142**\n"
            "12. HC ordinarily should **not** entertain PIL questioning **statute/rule validity**"
        ),
        "articles": [
            (
                "Guruvayur Devaswom Managing Committee vs C.K. Rajan, 2003",
                "Supreme Court evolved the twelve principles of PIL in this case.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pil-principles-pillars",
                "type": "pillars",
                "title": "Twelve principles → four buckets",
                "items": [
                    {
                        "id": "access",
                        "articles": "1 · 2 · 4",
                        "label": "Access",
                        "detail": (
                            "Interested person for disadvantaged (32/226); "
                            "epistolary letter/telegram; locus standi relaxed."
                        ),
                        "tone": "teal",
                    },
                    {
                        "id": "substance",
                        "articles": "3 · 5",
                        "label": "Substance",
                        "detail": (
                            "Arts 14 & 21 + IHRL for mass injustice; "
                            "prima facie FR breach → maintainability bar on State."
                        ),
                        "tone": "olive",
                    },
                    {
                        "id": "tools",
                        "articles": "6 · 8 · 9",
                        "label": "Tools",
                        "detail": (
                            "Res judicata fact-dependent; private petition → public enquiry; "
                            "commissions / institutional management directions."
                        ),
                        "tone": "gold",
                    },
                    {
                        "id": "limits",
                        "articles": "7 · 10 · 11 · 12",
                        "label": "Limits",
                        "detail": (
                            "No pure private-law war; policy restraint; known JR only; "
                            "HC ≠ Art. 142; HC ordinarily no statute-validity PIL."
                        ),
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pil-principles-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Case tag",
                "body": (
                    "Memorise as one unit: **Guruvayur (2003) = 12 principles**. "
                    "Pair with **Balwant Singh Chaupal (2010) = 8 admission guidelines**."
                ),
            },
        ],
    },
    {
        "title": "Misuse & Admission Guidelines",
        "slug": "pil-misuse",
        "sort_order": 7,
        "summary": (
            "PIL must not become Publicity/Politics/Private/Paisa/Middle-class Interest "
            "Litigation — eight Balwant Singh Chaupal guidelines curb abuse."
        ),
        "body": (
            "## Misuse labels (5P + MIL)\n\n"
            "Must not become:\n"
            "- **P**ublicity Interest Litigation\n"
            "- **P**olitics Interest Litigation\n"
            "- **P**rivate Interest Litigation\n"
            "- **P**aisa Interest Litigation\n"
            "- **M**iddle-class **I**nterest **L**itigation (**MIL**)\n\n"
            "## BALCO quote (2001)\n\n"
            "“PIL is not a pill or a panacea for all wrongs…” — meant for the weak and "
            "disadvantaged; abuse rising; parameters need re-emphasis.\n\n"
            "## Eight guidelines — State of Uttaranchal vs Balwant Singh Chaupal (2010)\n\n"
            "1. Encourage genuine PIL; curb extraneous ones\n"
            "2. Each **High Court** should formulate **rules** (not judge-wise ad hoc)\n"
            "3. Prima facie verify **credentials** of petitioner\n"
            "4. Prima facie satisfy **correctness of contents**\n"
            "5. Ensure **substantial public interest**\n"
            "6. Priority by larger public interest, gravity, urgency\n"
            "7. Aim = genuine public harm/injury; no personal/private/oblique motive\n"
            "8. Discourage busybodies via **exemplary costs** / novel methods"
        ),
        "articles": [
            (
                "BALCO Employees Union vs Union of India, 2001",
                "PIL is not a pill or panacea; meant for weak/disadvantaged; abuse needs parameter re-emphasis.",
            ),
            (
                "State of Uttaranchal vs Balwant Singh Chaupal, 2010",
                "Eight guidelines for admitting PIL and checking misuse.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pil-misuse-pillars",
                "type": "pillars",
                "title": "Eight admission guidelines (2010)",
                "items": [
                    {
                        "id": "g1",
                        "articles": "1–2",
                        "label": "Encourage + HC rules",
                        "detail": "Bonafide PILs yes; each HC must frame rules — not ad hoc per judge.",
                        "tone": "teal",
                    },
                    {
                        "id": "g2",
                        "articles": "3–4",
                        "label": "Credentials + contents",
                        "detail": "Prima facie verify who is filing and whether petition contents hold.",
                        "tone": "olive",
                    },
                    {
                        "id": "g3",
                        "articles": "5–6",
                        "label": "Public interest + priority",
                        "detail": "Substantial public interest required; triage by gravity and urgency.",
                        "tone": "gold",
                    },
                    {
                        "id": "g4",
                        "articles": "7–8",
                        "label": "Motive + costs",
                        "detail": "No personal/oblique gain; exemplary costs against frivolous busybodies.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pil-misuse-trap",
                "type": "callout",
                "tone": "trap",
                "title": "5P + MIL mnemonic",
                "body": (
                    "Publicity · Politics · Private · Paisa · **MIL** (Middle-class Interest Litigation). "
                    "If the petition smells like any of these, it is misuse — not genuine PIL."
                ),
            },
        ],
    },
    {
        "title": "Landmark Cases",
        "slug": "pil-landmarks",
        "sort_order": 8,
        "summary": (
            "Laxmikanth core trio (Guruvayur, BALCO, Balwant Singh) plus a short classic "
            "UPSC landmark bank marked as revision value-adds."
        ),
        "body": (
            "## Book-core (must)\n\n"
            "| Case | Year | Ratio |\n"
            "|------|------|-------|\n"
            "| **Guruvayur Devaswom Managing Committee vs C.K. Rajan** | 2003 | 12 principles of PIL |\n"
            "| **BALCO Employees Union vs Union of India** | 2001 | Purpose vs abuse — not a panacea |\n"
            "| **State of Uttaranchal vs Balwant Singh Chaupal** | 2010 | 8 admission guidelines |\n\n"
            "## Classic short bank (UPSC value-add — not Ch.29 text)\n\n"
            "| Case | Year | One-line |\n"
            "|------|------|----------|\n"
            "| **Hussainara Khatoon** | 1979 | Undertrials; speedy trial |\n"
            "| **S.P. Gupta** | 1981 | Expanded locus / epistolary culture |\n"
            "| **Bandhua Mukti Morcha** | 1984 | Bonded labour; letter petitions |\n"
            "| **Olga Tellis** | 1985 | Livelihood / pavement dwellers (Art. 21) |\n"
            "| **M.C. Mehta** | 1980s– | Environment as continuing PIL stream |\n"
            "| **Vishaka** | 1997 | Sexual harassment guidelines (Art. 21 edge) |"
        ),
        "articles": [
            ("Guruvayur vs C.K. Rajan, 2003", "Twelve principles of PIL."),
            ("BALCO Employees Union, 2001", "PIL purpose and rising abuse."),
            ("Balwant Singh Chaupal, 2010", "Eight guidelines against misuse."),
        ],
        "visual_blocks": [
            {
                "id": "pil-landmarks-tl",
                "type": "timeline",
                "title": "Landmark arc (classics → book-core)",
                "events": [
                    {
                        "id": "c1979",
                        "year": 1979,
                        "label": "Hussainara Khatoon",
                        "detail": "Value-add — undertrials; speedy trial as justice concern.",
                    },
                    {
                        "id": "c1981",
                        "year": 1981,
                        "label": "S.P. Gupta",
                        "detail": "Value-add — expanded locus standi / epistolary culture.",
                    },
                    {
                        "id": "c1984",
                        "year": 1984,
                        "label": "Bandhua Mukti Morcha",
                        "detail": "Value-add — bonded labour; letter as petition.",
                    },
                    {
                        "id": "c1985",
                        "year": 1985,
                        "label": "Olga Tellis",
                        "detail": "Value-add — livelihood of pavement dwellers under Art. 21.",
                    },
                    {
                        "id": "c1997",
                        "year": 1997,
                        "label": "Vishaka",
                        "detail": "Value-add — workplace sexual harassment guidelines.",
                    },
                    {
                        "id": "c2001",
                        "year": 2001,
                        "label": "BALCO (book-core)",
                        "detail": "Not a pill/panacea — re-emphasise PIL parameters.",
                    },
                    {
                        "id": "c2003",
                        "year": 2003,
                        "label": "Guruvayur (book-core)",
                        "detail": "Twelve principles of PIL crystallised.",
                    },
                    {
                        "id": "c2010",
                        "year": 2010,
                        "label": "Balwant Singh (book-core)",
                        "detail": "Eight guidelines to curb misuse / admit genuine PIL.",
                    },
                ],
            },
            {
                "id": "pil-landmarks-note",
                "type": "callout",
                "tone": "note",
                "title": "Book-core vs value-add",
                "body": (
                    "Only **Guruvayur (2003), BALCO (2001), Balwant Singh Chaupal (2010)** "
                    "appear in Laxmikanth Ch.29. Hussainara, S.P. Gupta, Bandhua Mukti Morcha, "
                    "Olga Tellis, M.C. Mehta, Vishaka are **UPSC revision value-adds**."
                ),
            },
        ],
    },
    {
        "title": "Exam Revision",
        "slug": "pil-exam-revision",
        "sort_order": 9,
        "summary": (
            "Prelims facts strip, mains value-adds, PYQ themes, and last-minute traps "
            "for Public Interest Litigation."
        ),
        "body": (
            "## Prelims facts strip\n\n"
            "- Origin: **USA 1960s**; India **early 1980s**\n"
            "- Pioneers: **Krishna Iyer + Bhagwati**\n"
            "- Also: **SAL / SIL / CAL**\n"
            "- Letter guidelines: **1988 → 1993 → 2003**\n"
            "- Arts: **32, 226, 14, 21, 142** (HC ≠ 142)\n"
            "- Scope: **10 entertained / 5 not**\n"
            "- Misuse: **5P + MIL**; **8** Balwant Singh guidelines (2010)\n"
            "- Core cases: BALCO **2001**, Guruvayur **2003**, Balwant Singh **2010**\n\n"
            "## Mains value-adds\n\n"
            "- PIL = leading instrument of **judicial activism**\n"
            "- **Cooperative triad** (petitioner–State–court) democratises access to justice\n"
            "- Tension: social justice gains vs **separation of powers** / judicial overreach\n"
            "- Reform path: HC rules, credential checks, exemplary costs against busybodies\n\n"
            "## Last-minute traps\n\n"
            "- Family pension ≠ service pension/gratuity\n"
            "- Labour PIL excludes individual disputes\n"
            "- HC cannot wield Art. 142-like power\n"
            "- Pure private-law group fight is not PIL"
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pil-exam-prelims",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims — 30-second strip",
                "body": (
                    "USA 1960s · India early 1980s · Iyer+Bhagwati · SAL/SIL/CAL · "
                    "1988/1993/2003 · Arts 32/226/14/21/142 · 10 vs 5 · 5P+MIL · "
                    "BALCO 2001 · Guruvayur 2003 · Balwant Singh 2010."
                ),
            },
            {
                "id": "pil-exam-mains",
                "type": "callout",
                "tone": "note",
                "title": "Mains value-adds",
                "body": (
                    "Frame answers around: (1) access to justice for the disadvantaged, "
                    "(2) cooperative petitioner–State–court model, "
                    "(3) activism vs overreach, "
                    "(4) misuse reforms (HC rules, credentials, costs)."
                ),
            },
            {
                "id": "pil-exam-themes",
                "type": "comparison",
                "title": "PYQ theme map",
                "columns": [
                    {
                        "id": "themes",
                        "heading": "Asked themes",
                        "points": [
                            "Locus standi relaxation / sufficient interest",
                            "Epistolary jurisdiction (letter as petition)",
                            "Which matters are entertained as PIL",
                            "Art. 142 — HC has no akin power",
                            "Pioneers of PIL in India",
                        ],
                    },
                    {
                        "id": "hooks",
                        "heading": "Answer hooks",
                        "points": [
                            "Exception to traditional standing",
                            "Flexibility + still judicial",
                            "10 vs 5 category lists",
                            "Guruvayur principle 11",
                            "Krishna Iyer + Bhagwati; early 1980s",
                        ],
                    },
                ],
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pil-meaning"),
    (HUB_SLUG, "parent", "pil-evolution"),
    (HUB_SLUG, "parent", "pil-vs-traditional"),
    (HUB_SLUG, "parent", "pil-constitutional-procedure"),
    (HUB_SLUG, "parent", "pil-scope"),
    (HUB_SLUG, "parent", "pil-principles"),
    (HUB_SLUG, "parent", "pil-misuse"),
    (HUB_SLUG, "parent", "pil-landmarks"),
    (HUB_SLUG, "parent", "pil-exam-revision"),
    ("pil-meaning", "related", "pil-vs-traditional"),
    ("pil-evolution", "related", "pil-landmarks"),
    ("pil-constitutional-procedure", "related", "pil-principles"),
    ("pil-scope", "related", "pil-misuse"),
    ("pil-principles", "related", "pil-landmarks"),
    ("pil-misuse", "related", "pil-exam-revision"),
    ("fundamental-rights", "related", HUB_SLUG),
    ("pil-constitutional-procedure", "related", "fundamental-rights"),
]

SAMPLE_PYQS = [
    (
        2015,
        "Public Interest Litigation in India is closely associated with the relaxation of:",
        "The traditional rule of locus standi — any public-spirited person with sufficient interest may approach the court for the disadvantaged.",
        ["pil-meaning", "pil-exam-revision"],
    ),
    (
        2017,
        "Who among the following are regarded as pioneers of Public Interest Litigation in India?",
        "Justice V.R. Krishna Iyer and Justice P.N. Bhagwati — introduced PIL in the early 1980s.",
        ["pil-evolution", "pil-exam-revision"],
    ),
    (
        2019,
        "With reference to PIL, which of the following is ordinarily NOT entertained by the Supreme Court as PIL?",
        "Landlord–tenant matters; service matters / pension & gratuity; educational admissions; early hearing of pending cases — among the five excluded categories.",
        ["pil-scope", "pil-exam-revision"],
    ),
    (
        2021,
        "Which of the following statements about PIL is correct regarding High Courts?",
        "A High Court may pass orders for complete justice to parties but does not have a power akin to Article 142 of the Constitution.",
        ["pil-constitutional-procedure", "pil-principles"],
    ),
]


class Command(BaseCommand):
    help = "Seed Public Interest Litigation chapter (Laxmikanth Ch.29)."

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
                "title": "Public Interest Litigation",
                "sort_order": 14,
                "book_ref": "Laxmikanth 8th Ed, Ch. 29",
                "summary": (
                    "Visual revision of Ch.29 — meaning, locus standi, evolution, "
                    "scope 10/5, twelve principles, misuse guidelines, landmark cases."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Public Interest Litigation",
                "summary": (
                    "Relaxed locus standi for public interest — a public-spirited proxy "
                    "knocks the court door for those who cannot."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **proxy** mental model, then "
                    "**Meaning** → **Evolution** → **vs Traditional** → "
                    "**Constitution & procedure** → **Scope 10/5**. "
                    "Drill **Twelve principles** and **Misuse 8**, finish with "
                    "**Landmark cases** and the **Exam box**. "
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
            ref="Laxmikanth Ch. 29",
            excerpt=(
                "Public Interest Litigation — meaning, features, scope, principles, "
                "and guidelines against misuse."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Articles 32 · 226 · 14 · 21 · 142",
            excerpt="Constitutional anchors for PIL jurisdiction, substance, and SC-only complete justice.",
            sort_order=1,
        )

        pil_slugs = set(by_slug.keys())
        from django.db.models import Q

        ConceptEdge.objects.filter(
            Q(source__slug__in=pil_slugs) | Q(target__slug__in=pil_slugs),
            source__subject=subject,
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

        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Public Interest Litigation chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
