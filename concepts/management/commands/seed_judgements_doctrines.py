"""Seed Laxmikanth Part XII — Judgements & Doctrines (visual revision chapter)."""

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

HUB_SLUG = "judgements-and-doctrines"
CHAPTER_SLUG = "judgements-and-doctrines"
BOOK_REF = "Laxmikanth 8th Ed, Part XII (Ch.91–94), pp.881–949"


def flagship_body(
    year,
    bench,
    articles,
    background,
    question,
    decision,
    ratio,
    significance,
    impact,
    upsc,
    current,
    related,
    themes,
):
    return (
        f"**Year:** {year}\n\n"
        f"**Bench:** {bench}\n\n"
        f"**Constitutional Articles Involved:** {articles}\n\n"
        f"**Background Facts:** {background}\n\n"
        f"**Constitutional Question:** {question}\n\n"
        f"**Decision:** {decision}\n\n"
        f"**Ratio Decidendi:** {ratio}\n\n"
        f"**Constitutional Significance:** {significance}\n\n"
        f"**Long-term Impact:** {impact}\n\n"
        f"**UPSC Importance:** {upsc}\n\n"
        f"**Current Relevance:** {current}\n\n"
        f"**Related Judgements:** {related}\n\n"
        f"**Frequently Asked Themes:** {themes}\n"
    )


def doctrine_body(definition, basis, origin, judgements, principles, exceptions, upsc):
    return (
        f"**Definition:** {definition}\n\n"
        f"**Constitutional Basis:** {basis}\n\n"
        f"**Origin:** {origin}\n\n"
        f"**Leading Judgements:** {judgements}\n\n"
        f"**Key Principles:** {principles}\n\n"
        f"**Exceptions:** {exceptions}\n\n"
        f"**UPSC Relevance:** {upsc}\n"
    )


def callout(cid, title, body, tone="tip"):
    return {"id": cid, "type": "callout", "title": title, "tone": tone, "body": body}


HUB_VISUAL_BLOCKS = [
    {
        "id": "jd-mm",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "GPS",
        "topic_label": "Judgements & Doctrines",
        "subject_label": "Constitution",
        "relation_label": "Interpreted by",
        "protects_from": [
            "Text without meaning",
            "Unlimited amending power",
            "Arbitrary state action",
        ],
        "insight": (
            "Landmark judgements fix what the Constitution means; "
            "doctrines are the toolkit courts use to interpret it."
        ),
    },
    {
        "id": "jd-pillars",
        "type": "pillars",
        "title": "Four revision pillars",
        "items": [
            {
                "id": "p-a",
                "articles": "Part A · Ch.91",
                "label": "Landmark Judgements",
                "slug": "jd-ak-gopalan",
                "detail": "Flagship cases + compact bank — ratio, impact, UPSC themes.",
                "tone": "teal",
            },
            {
                "id": "p-b",
                "articles": "Part B · Ch.92",
                "label": "Art. 21 Expansions",
                "slug": "jd-article-21-expansions",
                "detail": "Rights read into life & personal liberty after Maneka.",
                "tone": "olive",
            },
            {
                "id": "p-c",
                "articles": "Part C · Ch.93",
                "label": "Amendment Battles",
                "slug": "jd-amendments-struck",
                "detail": "Cases striking amendments + cases that triggered amendments.",
                "tone": "gold",
            },
            {
                "id": "p-d",
                "articles": "Part D · Ch.94",
                "label": "Doctrines",
                "slug": "jd-doctrines-map",
                "detail": "Severability, eclipse, pith & substance, harmonious construction…",
                "tone": "orange",
            },
        ],
    },
    callout(
        "jd-exam5",
        "Exam in 5 minutes",
        (
            "**Kesavananda** = basic structure · **Maneka** = expansive Art.21 · "
            "**Bommai** = Art.356 justiciable · **Puttaswamy** = privacy · "
            "**Coelho** = 9th Schedule not immune · Mnemonic **S-G-K-I-M-C** "
            "(Shankari→Golaknath→Kesavananda→Indira→Minerva→Coelho)."
        ),
        "tip",
    ),
]


FLAGSHIPS = [
    {
        "slug": "jd-ak-gopalan",
        "title": "A.K. Gopalan (1950)",
        "summary": "Narrow Art.21 — procedure established by law; FR in silos.",
        "sort_order": 1,
        "articles": [("Art. 21", "Personal liberty"), ("Art. 22", "Preventive detention")],
        "body": flagship_body(
            year="1950",
            bench="Constitution Bench (textualist majority)",
            articles="Arts. 21, 22",
            background="Challenge to Preventive Detention Act, 1950 (detention of A.K. Gopalan).",
            question="Does procedure established by law under Art.21 import due process? Are Arts. 19/21/22 watertight?",
            decision="S.14 PDA struck (Art.22); rest upheld. Personal liberty = physical restraint freedom. Art.21 vs executive, not legislature.",
            ratio="Law in Art.21 = state-made law, not natural justice. Procedure established by law ≠ American due process. FRs read in isolation.",
            significance="Narrow Art.21 baseline for nearly three decades (1950–1978).",
            impact="Logical end in A.D.M. Jabalpur (1976). Overruled in substance by Maneka Gandhi (1978).",
            upsc="Classic contrast with Maneka; procedure established by law theme.",
            current="Cited to show shift from textualist to purposive Art.21 interpretation.",
            related="A.D.M. Jabalpur (1976); Maneka Gandhi (1978).",
            themes="Art.21 scope; preventive detention; FR compartmentalisation.",
        ),
        "visual_blocks": [
            callout("jd-gopalan-trap", "Trap", "Gopalan did **not** equate Art.21 with due process — that is **Maneka (1978)**.", "trap"),
        ],
    },
    {
        "slug": "jd-champakam",
        "title": "Champakam Dorairajan (1951)",
        "summary": "FR override DPSP; Communal GO struck — led to Art.15(4).",
        "sort_order": 2,
        "articles": [("Art. 15", "Non-discrimination"), ("Art. 29", "Admission"), ("Art. 46", "DPSP")],
        "body": flagship_body(
            year="1951",
            bench="Supreme Court",
            articles="Arts. 15, 29(2), 46",
            background="Madras Communal GO reserved college seats by community citing Art.46.",
            question="Can a DPSP justify a measure that violates Fundamental Rights?",
            decision="Communal GO struck (Arts. 15(1), 29(2)). DPSPs cannot override FRs; they run subsidiary to FRs.",
            ratio="Enforceable FRs limit the State; Directive Principles cannot validate FR violations.",
            significance="First major FR–DPSP conflict.",
            impact="1st Amendment inserted Art.15(4) for SEBCs/SCs/STs.",
            upsc="Champakam → 1st Amendment → Art.15(4).",
            current="Reservation debates still start from this FR–DPSP tension.",
            related="Indra Sawhney (1992); Minerva Mills (FR–DPSP harmony).",
            themes="Reservation; FR vs DPSP; 1st Amendment.",
        ),
        "visual_blocks": [
            callout("jd-champakam-tip", "Revision anchor", "**Champakam** → **1st Amendment / Art.15(4)**.", "tip"),
        ],
    },
    {
        "slug": "jd-shankari-prasad",
        "title": "Shankari Prasad (1951)",
        "summary": "Parliament can amend FRs; law in Art.13 ≠ constitutional amendment.",
        "sort_order": 3,
        "articles": [("Art. 13", "Laws inconsistent with FR"), ("Art. 368", "Amendment")],
        "body": flagship_body(
            year="1951",
            bench="Constitution Bench",
            articles="Arts. 13, 368",
            background="Challenge to 1st Amendment (Arts. 31A, 31B / 9th Schedule) curtailing property rights.",
            question="Does Art.368 include power to amend FRs? Is an amendment law under Art.13(2)?",
            decision="1st Amendment upheld. Amending power includes FRs. Art.13(2) law = ordinary law, not constituent law.",
            ratio="Legislative law vs constituent power — amendments outside Art.13(2).",
            significance="Opened the FR-amendability arc; held until Golaknath (1967).",
            impact="Reaffirmed in Sajjan Singh (1964); flipped by Golaknath; reshaped by Kesavananda.",
            upsc="First node of S-G-K-I-M-C timeline.",
            current="Starting point for can Parliament amend FRs?",
            related="Sajjan Singh (1964); Golaknath (1967); Kesavananda (1973).",
            themes="Art.368; Art.13; amendability of FRs.",
        ),
        "visual_blocks": [
            callout("jd-shankari-tip", "Memory", "**Shankari = Yes amend FRs.** **Golaknath = No.** **Kesavananda = Yes, but not basic structure.**", "tip"),
        ],
    },
    {
        "slug": "jd-golaknath",
        "title": "Golaknath (1967)",
        "summary": "FRs transcendental — Parliament cannot abridge them by amendment (later overruled in part).",
        "sort_order": 4,
        "articles": [("Art. 13", "Law includes amendment?"), ("Art. 368", "Amending power")],
        "body": flagship_body(
            year="1967",
            bench="11-judge Bench (narrow majority)",
            articles="Arts. 13, 368; 17th Amendment (in part)",
            background="Challenge to amendments affecting property/agrarian reforms (17th Amendment context).",
            question="Can Parliament amend Part III to abridge or take away Fundamental Rights?",
            decision="Parliament cannot abridge/take away FRs by amendment. Amendment Acts = law under Art.13. Prospective overruling saved past amendments.",
            ratio="FRs have transcendental position; Art.368 cannot take them away.",
            significance="High-water mark of FR supremacy vs amending power; provoked 24th Amendment.",
            impact="24th Amendment (1971); overruled on FR-amendability by Kesavananda (1973) with basic structure limit.",
            upsc="Pair with Kesavananda; Ch.93 Table 93.1; prospective overruling.",
            current="Not present law on amending FRs — Kesavananda/Minerva are.",
            related="Shankari Prasad; Kesavananda; Minerva Mills.",
            themes="Amendability of FRs; prospective overruling; Parliament vs judiciary.",
        ),
        "visual_blocks": [
            callout("jd-golak-trap", "Trap", "Golaknath is **not** current law on amending FRs. **Kesavananda** overruled that core holding.", "trap"),
        ],
    },
    {
        "slug": "jd-kesavananda",
        "title": "Kesavananda Bharati (1973)",
        "summary": "Basic structure doctrine born — amend FRs, but not the Constitution’s basic structure.",
        "sort_order": 5,
        "articles": [("Art. 368", "Amending power"), ("Art. 13", "Law"), ("Art. 31C", "in part")],
        "body": flagship_body(
            year="1973 (24 April)",
            bench="13-judge Bench (7–6)",
            articles="Arts. 13, 368; 24th & 25th Amendments (Art.31C in part)",
            background="Challenge to Kerala land reforms and amendments expanding amending power / Art.31C.",
            question="Is Art.368 unlimited? Can Parliament destroy the Constitution’s basic identity?",
            decision="Parliament may amend any provision including FRs (Golaknath overruled on that point), but cannot alter basic structure. Art.31C judicial-review ouster struck in part.",
            ratio="Amending power is wide but not unlimited; basic features are beyond Art.368.",
            significance="Most important constitutional judgement — identity of the Constitution protected.",
            impact="Applied in Indira, Minerva, Waman Rao, Coelho, NJAC.",
            upsc="Mandatory Prelims & Mains; link basic-structure chapter.",
            current="Still controlling filter for amendment challenges.",
            related="Golaknath; Indira Nehru Gandhi; Minerva Mills; Waman Rao; I.R. Coelho; NJAC.",
            themes="Basic structure; Art.368; judicial review of amendments.",
        ),
        "visual_blocks": [
            callout("jd-kesavananda-tip", "Revision anchor", "**24 April 1973** = Waman Rao / Coelho cut-off for 9th Schedule basic-structure review.", "tip"),
        ],
    },
    {
        "slug": "jd-indira-gandhi",
        "title": "Indira Nehru Gandhi (1975)",
        "summary": "Election Case — basic structure applied; Art.329A(4) void.",
        "sort_order": 6,
        "articles": [("Art. 329A", "39th Amendment"), ("Art. 368", "Basic structure")],
        "body": flagship_body(
            year="1975",
            bench="Constitution Bench",
            articles="Art.329A (39th Amendment); free & fair elections / rule of law",
            background="Allahabad HC set aside Indira Gandhi’s election; 39th Amendment inserted Art.329A to shield PM/Speaker election disputes.",
            question="Can Parliament place high-office election disputes beyond all courts by amendment?",
            decision="Art.329A(4) struck as violating basic structure (democracy, rule of law, judicial review).",
            ratio="Basic structure voids concrete amendment clauses — not merely aspirational.",
            significance="First major application of basic structure after Kesavananda.",
            impact="42nd Amendment reaction; later checked by Minerva Mills.",
            upsc="Election Case — democracy / free & fair elections as basic features.",
            current="Cited when amendments try to oust judicial review of democratic processes.",
            related="Kesavananda; Minerva Mills; Kihoto Hollohan.",
            themes="Basic structure application; judicial review; 39th Amendment.",
        ),
        "visual_blocks": [
            callout("jd-indira-tip", "Name alert", "**Election Case** (Indira Nehru Gandhi vs Raj Narain) — not an Emergency detention case.", "note"),
        ],
    },
    {
        "slug": "jd-adm-jabalpur",
        "title": "A.D.M. Jabalpur (1976)",
        "summary": "Habeas corpus case — Emergency low watermark; later discredited.",
        "sort_order": 7,
        "articles": [("Art. 21", "Life & liberty"), ("Art. 226", "Habeas"), ("Art. 359", "Suspension")],
        "body": flagship_body(
            year="1976",
            bench="Constitution Bench (Khanna J. dissent famous)",
            articles="Arts. 21, 226, 359",
            background="Internal Emergency; FR enforcement suspended; detenus sought habeas corpus.",
            question="Can courts entertain habeas when Art.21 enforcement is suspended?",
            decision="Majority: no habeas remedy during such suspension. Khanna J. dissented.",
            ratio="Majority treated suspended Art.21 as extinguishing judicial remedy; dissent insisted right to life cannot vanish.",
            significance="Nadir of Art.21 jurisprudence; danger of Gopalan-style narrow liberty.",
            impact="Buried by later Benches; Puttaswamy expressly rejected Jabalpur majority logic. 44th Amendment Emergency reforms.",
            upsc="Contrast Maneka/Puttaswamy; Khanna dissent is a Mains favourite.",
            current="Cited as what not to do.",
            related="A.K. Gopalan; Maneka Gandhi; K.S. Puttaswamy.",
            themes="Emergency; habeas corpus; Art.21; judicial independence.",
        ),
        "visual_blocks": [
            callout("jd-jabalpur-trap", "Trap", "**Jabalpur** is not good law today — Emergency aberration.", "trap"),
        ],
    },
    {
        "slug": "jd-maneka-gandhi",
        "title": "Maneka Gandhi (1978)",
        "summary": "Expansive Art.21 — procedure must be just, fair, reasonable; golden triangle.",
        "sort_order": 8,
        "articles": [("Art. 21", "Personal liberty"), ("Art. 14", "Equality"), ("Art. 19", "Freedoms")],
        "body": flagship_body(
            year="1978",
            bench="7-judge Bench",
            articles="Arts. 14, 19, 21",
            background="Passport impounded without hearing.",
            question="Must procedure under Art.21 be fair and non-arbitrary, or is any enacted procedure enough?",
            decision="Procedure must be just, fair and reasonable. Arts. 14, 19, 21 read together. Gopalan silos rejected.",
            ratio="Liberty-restricting law must satisfy Art.14 non-arbitrariness and resonate with Art.19 — due-process-like content in Art.21.",
            significance="Watershed opening Art.21 expansions (privacy, livelihood, environment, health…).",
            impact="Foundation for Ch.92 table and Puttaswamy.",
            upsc="Highest-yield Art.21 case; pair with Gopalan before/after.",
            current="Template for testing liberty-restricting State action.",
            related="A.K. Gopalan; Olga Tellis; Puttaswamy; Anuradha Bhasin.",
            themes="Due process (Indian); golden triangle; audi alteram partem.",
        ),
        "visual_blocks": [
            callout("jd-maneka-tip", "Formula", "**Art.21 procedure = just + fair + reasonable** + link **Arts. 14 & 19**.", "tip"),
        ],
    },
    {
        "slug": "jd-minerva-mills",
        "title": "Minerva Mills (1980)",
        "summary": "Limited amending power is basic; 42nd Art.368(4)&(5) struck; FR–DPSP harmony.",
        "sort_order": 9,
        "articles": [("Art. 368", "cls. 4 & 5"), ("Art. 31C", "expanded")],
        "body": flagship_body(
            year="1980",
            bench="Constitution Bench",
            articles="Arts. 31C, 368(4)–(5)",
            background="42nd Amendment tried to make amending power unreviewable and expand Art.31C to all DPSPs.",
            question="Can Parliament convert limited amending power into unlimited power and oust judicial review?",
            decision="42nd clauses attacking limited amending power/judicial review void; expanded Art.31C struck in relevant part; rest saved by severability.",
            ratio="Limited amending power and judicial review are basic. FR–DPSP harmony is basic — neither destroys the other.",
            significance="Fortified Kesavananda against Emergency-era 42nd assault.",
            impact="Parliament cannot use Art.368 to destroy basic-structure review itself.",
            upsc="Pair with Kesavananda; FR–DPSP harmony phrase.",
            current="Cited against immunising amendments from review.",
            related="Kesavananda; Indira Gandhi; Waman Rao; Coelho.",
            themes="42nd Amendment; basic structure; FR–DPSP; severability.",
        ),
        "visual_blocks": [
            callout("jd-minerva-tip", "Revision", "**Kesavananda** births basic structure · **Minerva** stops Parliament deleting the limit.", "tip"),
        ],
    },
    {
        "slug": "jd-indra-sawhney",
        "title": "Indra Sawhney (1992)",
        "summary": "Mandal case — OBC reservation; 50% ceiling; creamy layer.",
        "sort_order": 10,
        "articles": [("Art. 16", "Public employment equality")],
        "body": flagship_body(
            year="1992",
            bench="9-judge Bench",
            articles="Art.16(4) and equality code",
            background="Challenge to Mandal Commission–based OBC reservations in Central services.",
            question="Scope of Art.16(4); ceiling on reservations; creamy layer; promotions?",
            decision="OBC reservation upheld with limits: creamy layer; generally 50% ceiling; no reservation in promotions (later amended/litigated); caste can be class indicator.",
            ratio="Art.16(4) enables adequate representation of backward classes as a facet of equality.",
            significance="Constitutional grammar of reservation policy for a generation.",
            impact="Triggered 76th, 77th, 81st, 82nd, 85th Amendments.",
            upsc="Creamy layer, 50%, Mandal — Prelims staple.",
            current="Baseline for OBC/promotion/EWS debates (with later law).",
            related="Champakam; M. Nagaraj; later EWS cases.",
            themes="Reservation; creamy layer; 50% ceiling; Art.16(4).",
        ),
        "visual_blocks": [
            callout("jd-mandal-tip", "Remember", "**Creamy layer** + **50%** = Indra Sawhney anchors.", "tip"),
        ],
    },
    {
        "slug": "jd-second-judges",
        "title": "S.C. Advocates-on-Record / Second Judges (1993)",
        "summary": "Collegium born — CJI primacy (concurrence) in appointments.",
        "sort_order": 11,
        "articles": [("Art. 124", "SC judges"), ("Art. 217", "HC judges")],
        "body": flagship_body(
            year="1993",
            bench="9-judge Bench",
            articles="Arts. 124, 217",
            background="Meaning of consultation with CJI after First Judges Case (1981).",
            question="Does consultation mean concurrence? Who has primacy in appointments?",
            decision="CJI opinion has primacy; collegium (CJI + senior judges) for appointments/transfers.",
            ratio="Judicial independence requires appointment primacy with the judiciary via CJI-led collegium.",
            significance="Created India’s collegium model.",
            impact="Third Judges (1998) expanded collegium; NJAC (2015) struck; collegium restored.",
            upsc="First/Second/Third/Fourth Judges sequence.",
            current="Collegium vs reform remains live politics.",
            related="First Judges (1981); Third Judges (1998); Fourth Judges/NJAC (2015).",
            themes="Judicial independence; collegium; consultation vs concurrence.",
        ),
        "visual_blocks": [
            callout("jd-collegium-tip", "Sequence", "**1981** executive primacy → **1993** collegium → **1998** CJI+4 → **2015** NJAC struck.", "tip"),
        ],
    },
    {
        "slug": "jd-sr-bommai",
        "title": "S.R. Bommai (1994)",
        "summary": "Art.356 justiciable; secularism & federalism; floor test.",
        "sort_order": 12,
        "articles": [("Art. 356", "President’s Rule")],
        "body": flagship_body(
            year="1994",
            bench="9-judge Bench",
            articles="Art.356; federalism; secularism",
            background="Challenges to President’s Rule / Assembly dissolutions after Bommai dismissal and related cases.",
            question="Is Art.356 satisfaction unreviewable? What limits President’s Rule?",
            decision="Art.356 is judicially reviewable. Majority preferably tested on House floor. Secularism is basic feature. Federalism reinforced.",
            ratio="Presidential satisfaction is not absolute; mala fides / irrelevant grounds open to review.",
            significance="Most important federalism / State Emergency judgement.",
            impact="Reduced arbitrary Art.356 use; standard cite in Centre–State crises.",
            upsc="Prelims + Mains staple for federalism, secularism, Art.356.",
            current="Checklist whenever President’s Rule is imposed.",
            related="Basic structure secularism cases; later Art.356 practice.",
            themes="Art.356; floor test; secularism; federalism.",
        ),
        "visual_blocks": [
            callout("jd-bommai-tip", "Checklist", "**Floor test** · **judicial review of 356** · **secularism as basic feature**.", "tip"),
        ],
    },
    {
        "slug": "jd-vishaka",
        "title": "Vishaka (1997)",
        "summary": "Workplace sexual harassment guidelines until legislation.",
        "sort_order": 13,
        "articles": [("Art. 14", "Equality"), ("Art. 15", "Sex"), ("Art. 21", "Dignity"), ("Art. 19", "Work")],
        "body": flagship_body(
            year="1997",
            bench="3-judge Bench",
            articles="Arts. 14, 15, 19, 21; CEDAW influence",
            background="Bhanwari Devi case; legislative vacuum on workplace sexual harassment.",
            question="Can the Court fill a vacuum to protect women at workplaces under FRs?",
            decision="Binding Vishaka Guidelines until Parliament legislates — harassment violates equality, dignity, liberty.",
            ratio="International conventions inform constitutional interpretation; Art.32 guidelines can protect FRs.",
            significance="Landmark gender justice / judicial law-making for dignity.",
            impact="POSH Act, 2013.",
            upsc="Art.21 dignity + judicial activism / PIL.",
            current="Act of 2013 is statute; Vishaka remains interpretive foundation.",
            related="Later POSH jurisprudence; Medha Kotwal.",
            themes="Sexual harassment; Art.21 dignity; judicial guidelines.",
        ),
        "visual_blocks": [
            callout("jd-vishaka-tip", "Status", "Guidelines were interim law → **POSH Act 2013**. Still cite Vishaka for FR basis.", "note"),
        ],
    },
    {
        "slug": "jd-ir-coelho",
        "title": "I.R. Coelho (2007)",
        "summary": "9th Schedule not a vault — post-Kesavananda insertions open to basic structure review.",
        "sort_order": 14,
        "articles": [("Art. 31B", "9th Schedule"), ("Art. 368", "Basic structure")],
        "body": flagship_body(
            year="2007",
            bench="9-judge Bench",
            articles="Arts. 31B, 14, 15, 19, 21; Ninth Schedule",
            background="Challenge to laws put in 9th Schedule after 24 April 1973 to escape FR review.",
            question="Does 9th Schedule inclusion immunise a law forever from basic structure review?",
            decision="Post-Kesavananda 9th Schedule insertions can be tested on basic structure (especially if they damage Arts. 14/15/19/21).",
            ratio="Art.31B cannot confer blank immunity against basic structure; judicial review remains.",
            significance="Closed the dump in 9th Schedule escape hatch.",
            impact="Every post-1973 9th Schedule insertion is potentially reviewable.",
            upsc="Pair with Waman Rao cut-off and Kesavananda.",
            current="Still the rule for 9th Schedule challenges.",
            related="Waman Rao; Kesavananda; Minerva Mills.",
            themes="Ninth Schedule; basic structure; judicial review.",
        ),
        "visual_blocks": [
            callout("jd-coelho-tip", "Date", "**24 April 1973** cut-off for Coelho / Waman Rao analysis.", "tip"),
        ],
    },
    {
        "slug": "jd-njac",
        "title": "NJAC / Fourth Judges (2015)",
        "summary": "99th Amendment + NJAC Act struck — collegium restored.",
        "sort_order": 15,
        "articles": [("99th Amendment", "NJAC"), ("Art. 124", "Appointments")],
        "body": flagship_body(
            year="2015",
            bench="5-judge Constitution Bench",
            articles="99th Constitutional Amendment; NJAC Act, 2014",
            background="Parliament replaced collegium with NJAC via 99th Amendment + statute.",
            question="Does NJAC violate judicial independence / basic structure?",
            decision="99th Amendment and NJAC Act unconstitutional and void; collegium revived.",
            ratio="Judicial primacy in appointments is part of judicial independence (basic feature).",
            significance="Constitutional amendment struck in toto on appointments architecture.",
            impact="Collegium remains; reform debate continues.",
            upsc="Must-know with Second/Third Judges; Table 93.1.",
            current="Reform proposals judged against this holding.",
            related="Second Judges (1993); Third Judges (1998); basic structure cases.",
            themes="NJAC; collegium; judicial independence; 99th Amendment.",
        ),
        "visual_blocks": [
            callout("jd-njac-trap", "Trap", "NJAC fell as violating **basic structure** (independence), not merely bad policy.", "trap"),
        ],
    },
    {
        "slug": "jd-shayara-bano",
        "title": "Shayara Bano (2017)",
        "summary": "Instant triple talaq unconstitutional / void.",
        "sort_order": 16,
        "articles": [("Art. 14", "Equality"), ("Art. 21", "Dignity"), ("Art. 25", "Religion")],
        "body": flagship_body(
            year="2017",
            bench="5-judge Bench",
            articles="Arts. 14, 15, 21, 25",
            background="Challenge to talaq-e-biddat as arbitrary and violative of equality and dignity.",
            question="Is instant triple talaq protected essential practice or unconstitutional?",
            decision="Majority: instant triple talaq void (not essential / arbitrary).",
            ratio="Personal law practices can be tested against FRs; arbitrariness fails Art.14.",
            significance="Landmark gender justice / personal law constitutionalisation.",
            impact="Muslim Women (Protection of Rights on Marriage) Act, 2019.",
            upsc="FR vs personal law; don’t confuse with Shah Bano (1985).",
            current="Statute in force; case remains constitutional foundation.",
            related="Shah Bano (1985); Sabarimala (ERP debates).",
            themes="Triple talaq; Art.14/21; personal laws.",
        ),
        "visual_blocks": [
            callout("jd-shayara-tip", "Don’t confuse", "**Shah Bano (1985)** = maintenance · **Shayara Bano (2017)** = triple talaq.", "trap"),
        ],
    },
    {
        "slug": "jd-puttaswamy",
        "title": "K.S. Puttaswamy (2017)",
        "summary": "Right to privacy is a Fundamental Right under Art.21.",
        "sort_order": 17,
        "articles": [("Art. 21", "Privacy"), ("Art. 14", "Dignity"), ("Art. 19", "Autonomy")],
        "body": flagship_body(
            year="2017",
            bench="9-judge Bench",
            articles="Arts. 14, 19, 21",
            background="Reference from Aadhaar challenges — is privacy constitutionally protected?",
            question="Is there a Fundamental Right to privacy?",
            decision="Privacy is a Fundamental Right intrinsic to life and liberty; contrary older dicta overruled to that extent.",
            ratio="Privacy includes bodily, informational, decisional autonomy — restrictions must be just, fair, reasonable (proportionality).",
            significance="Foundation for data protection and dignity jurisprudence.",
            impact="Guided Aadhaar (2018), sexuality cases, surveillance debates.",
            upsc="Core Art.21 expansion; proportionality follow-ons.",
            current="Touchstone for digital rights and bodily autonomy.",
            related="Maneka Gandhi; Navtej Johar; Aadhaar (Puttaswamy-II).",
            themes="Privacy; dignity; proportionality.",
        ),
        "visual_blocks": [
            callout("jd-privacy-tip", "Exam line", "Privacy = **Fundamental Right** (9-judge).", "tip"),
        ],
    },
    {
        "slug": "jd-navtej-johar",
        "title": "Navtej Singh Johar (2018)",
        "summary": "s.377 read down — consensual adult same-sex relations decriminalised.",
        "sort_order": 18,
        "articles": [("Art. 14", "Equality"), ("Art. 15", "Orientation"), ("Art. 19", "Expression"), ("Art. 21", "Dignity")],
        "body": flagship_body(
            year="2018",
            bench="5-judge Bench",
            articles="Arts. 14, 15, 19, 21; s.377 IPC",
            background="Challenge to criminalisation of consensual homosexual acts between adults.",
            question="Does s.377 (as applied to consensual adult same-sex acts) violate equality, dignity, privacy?",
            decision="s.377 unconstitutional to that extent; non-consensual acts/bestiality remain covered.",
            ratio="Sexual orientation intrinsic to identity; constitutional morality over majoritarian morality; privacy + equality + dignity protect intimate choice.",
            significance="Transformative equality/dignity judgement.",
            impact="Decriminalisation; marriage equality litigated separately later.",
            upsc="Puttaswamy → Navtej; constitutional morality; reading down.",
            current="Criminal law settled; civil rights still evolving.",
            related="Puttaswamy; NALSA; Suresh Koushal (overruled in relevant part).",
            themes="s.377; constitutional morality; privacy; equality.",
        ),
        "visual_blocks": [
            callout("jd-navtej-tip", "Reading down", "Court **read down** s.377 — know what remains criminal.", "tip"),
        ],
    },
]


from concepts.management.commands._jd_clusters import build_clusters, build_edges

CLUSTERS = build_clusters(FLAGSHIPS)
CLUSTER_SLUGS = [c["slug"] for c in CLUSTERS]
EDGES = build_edges(CLUSTER_SLUGS)

LANDMARK_CASES = [
    {
        "title": "A.K. Gopalan v. State of Madras",
        "slug": "ak-gopalan",
        "parties": "A.K. Gopalan v. State of Madras",
        "year": 1950,
        "court": CaseLaw.Court.SC,
        "summary": "Narrow Art.21 — procedure established by law; FR silos.",
        "holding": "Personal liberty narrowly read; due process rejected; Art.21 mainly vs executive.",
        "concept_slugs": [HUB_SLUG, "jd-ak-gopalan", "jd-network-art21", "jd-cmp-gopalan-maneka"],
    },
    {
        "title": "State of Madras v. Champakam Dorairajan",
        "slug": "champakam-dorairajan",
        "parties": "State of Madras v. Champakam Dorairajan",
        "year": 1951,
        "court": CaseLaw.Court.SC,
        "summary": "FR override DPSP; Communal GO struck.",
        "holding": "DPSPs cannot override FRs; led to Art.15(4) via 1st Amendment.",
        "concept_slugs": [HUB_SLUG, "jd-champakam", "jd-amendments-triggered"],
    },
    {
        "title": "Shankari Prasad v. Union of India",
        "slug": "shankari-prasad",
        "parties": "Shankari Prasad v. Union of India",
        "year": 1951,
        "court": CaseLaw.Court.SC,
        "summary": "Parliament can amend Fundamental Rights.",
        "holding": "Art.13 law excludes constitutional amendments under Art.368.",
        "concept_slugs": [HUB_SLUG, "jd-shankari-prasad", "jd-network-bs"],
    },
    {
        "title": "I.C. Golak Nath v. State of Punjab",
        "slug": "golak-nath",
        "parties": "I.C. Golak Nath v. State of Punjab",
        "year": 1967,
        "court": CaseLaw.Court.SC,
        "summary": "FRs transcendental — cannot be abridged by amendment.",
        "holding": "Amendment Acts are law under Art.13; prospective overruling applied.",
        "concept_slugs": [HUB_SLUG, "jd-golaknath", "jd-network-bs", "jd-cmp-golaknath-kesavananda"],
    },
    {
        "title": "Kesavananda Bharati v. State of Kerala",
        "slug": "kesavananda-bharati",
        "parties": "Kesavananda Bharati v. State of Kerala",
        "year": 1973,
        "court": CaseLaw.Court.SC,
        "summary": "Basic structure doctrine born.",
        "holding": "Parliament may amend FRs but not the basic structure of the Constitution.",
        "concept_slugs": [HUB_SLUG, "jd-kesavananda", "jd-network-bs", "jd-master-revision"],
    },
    {
        "title": "Indira Nehru Gandhi v. Raj Narain",
        "slug": "indira-nehru-gandhi",
        "parties": "Indira Nehru Gandhi v. Raj Narain",
        "year": 1975,
        "court": CaseLaw.Court.SC,
        "summary": "Election Case — Art.329A(4) void.",
        "holding": "Ousting election disputes from courts violated basic structure.",
        "concept_slugs": [HUB_SLUG, "jd-indira-gandhi", "jd-network-bs", "jd-amendments-struck"],
    },
    {
        "title": "A.D.M. Jabalpur v. Shivkant Shukla",
        "slug": "adm-jabalpur",
        "parties": "A.D.M. Jabalpur v. Shivkant Shukla",
        "year": 1976,
        "court": CaseLaw.Court.SC,
        "summary": "Habeas corpus case — Emergency low watermark.",
        "holding": "Majority denied habeas during FR suspension; later discredited.",
        "concept_slugs": [HUB_SLUG, "jd-adm-jabalpur", "jd-network-art21"],
    },
    {
        "title": "Maneka Gandhi v. Union of India",
        "slug": "maneka-gandhi",
        "parties": "Maneka Gandhi v. Union of India",
        "year": 1978,
        "court": CaseLaw.Court.SC,
        "summary": "Expansive Art.21 — just, fair, reasonable procedure.",
        "holding": "Arts. 14, 19, 21 read together; Gopalan silo approach rejected.",
        "concept_slugs": [HUB_SLUG, "jd-maneka-gandhi", "jd-network-art21", "jd-cmp-gopalan-maneka"],
    },
    {
        "title": "Minerva Mills Ltd. v. Union of India",
        "slug": "minerva-mills",
        "parties": "Minerva Mills Ltd. v. Union of India",
        "year": 1980,
        "court": CaseLaw.Court.SC,
        "summary": "Limited amending power is basic; 42nd checked.",
        "holding": "Art.368(4)&(5) void; FR–DPSP harmony is basic structure.",
        "concept_slugs": [HUB_SLUG, "jd-minerva-mills", "jd-network-bs", "jd-cmp-kesavananda-minerva"],
    },
    {
        "title": "Indra Sawhney v. Union of India",
        "slug": "indra-sawhney",
        "parties": "Indra Sawhney v. Union of India",
        "year": 1992,
        "court": CaseLaw.Court.SC,
        "summary": "Mandal case — OBC reservation framework.",
        "holding": "Creamy layer; generally 50% ceiling; Art.16(4) grammar settled.",
        "concept_slugs": [HUB_SLUG, "jd-indra-sawhney", "jd-amendments-triggered"],
    },
    {
        "title": "Supreme Court Advocates-on-Record Association v. Union of India",
        "slug": "second-judges-case",
        "parties": "SC Advocates-on-Record Assn. v. Union of India",
        "year": 1993,
        "court": CaseLaw.Court.SC,
        "summary": "Second Judges Case — collegium born.",
        "holding": "CJI primacy/concurrence; collegium for appointments.",
        "concept_slugs": [HUB_SLUG, "jd-second-judges", "jd-cmp-njac-collegium"],
    },
    {
        "title": "S.R. Bommai v. Union of India",
        "slug": "sr-bommai",
        "parties": "S.R. Bommai v. Union of India",
        "year": 1994,
        "court": CaseLaw.Court.SC,
        "summary": "Art.356 justiciable; secularism and federalism.",
        "holding": "President Rule reviewable; floor test preferred; secularism basic.",
        "concept_slugs": [HUB_SLUG, "jd-sr-bommai", "jd-master-revision"],
    },
    {
        "title": "Vishaka v. State of Rajasthan",
        "slug": "vishaka",
        "parties": "Vishaka v. State of Rajasthan",
        "year": 1997,
        "court": CaseLaw.Court.SC,
        "summary": "Sexual harassment guidelines until legislation.",
        "holding": "Binding workplace guidelines under Arts. 14, 15, 19, 21.",
        "concept_slugs": [HUB_SLUG, "jd-vishaka", "jd-article-21-expansions"],
    },
    {
        "title": "I.R. Coelho v. State of Tamil Nadu",
        "slug": "ir-coelho",
        "parties": "I.R. Coelho v. State of Tamil Nadu",
        "year": 2007,
        "court": CaseLaw.Court.SC,
        "summary": "9th Schedule laws open to basic structure review.",
        "holding": "Post-24 Apr 1973 9th Schedule insertions not immune.",
        "concept_slugs": [HUB_SLUG, "jd-ir-coelho", "jd-network-bs"],
    },
    {
        "title": "Supreme Court Advocates-on-Record Association v. Union of India (NJAC)",
        "slug": "fourth-judges-case",
        "parties": "SC Advocates-on-Record Assn. v. Union of India",
        "year": 2015,
        "court": CaseLaw.Court.SC,
        "summary": "Fourth Judges / NJAC — 99th Amendment struck.",
        "holding": "NJAC violates judicial independence (basic structure); collegium restored.",
        "concept_slugs": [HUB_SLUG, "jd-njac", "jd-cmp-njac-collegium", "jd-amendments-struck"],
    },
    {
        "title": "Shayara Bano v. Union of India",
        "slug": "shayara-bano",
        "parties": "Shayara Bano v. Union of India",
        "year": 2017,
        "court": CaseLaw.Court.SC,
        "summary": "Instant triple talaq unconstitutional.",
        "holding": "Talaq-e-biddat void for arbitrariness / not essential practice.",
        "concept_slugs": [HUB_SLUG, "jd-shayara-bano", "jd-confused-judgements"],
    },
    {
        "title": "K.S. Puttaswamy v. Union of India",
        "slug": "puttaswamy",
        "parties": "K.S. Puttaswamy v. Union of India",
        "year": 2017,
        "court": CaseLaw.Court.SC,
        "summary": "Right to privacy is a Fundamental Right.",
        "holding": "Privacy intrinsic to Art.21 (and linked to dignity/autonomy).",
        "concept_slugs": [HUB_SLUG, "jd-puttaswamy", "jd-network-art21", "jd-article-21-expansions"],
    },
    {
        "title": "Navtej Singh Johar v. Union of India",
        "slug": "navtej-singh-johar",
        "parties": "Navtej Singh Johar v. Union of India",
        "year": 2018,
        "court": CaseLaw.Court.SC,
        "summary": "s.377 read down for consensual adult same-sex relations.",
        "holding": "Criminalisation of consensual adult same-sex acts unconstitutional.",
        "concept_slugs": [HUB_SLUG, "jd-navtej-johar", "jd-which-case-what"],
    },
]

AMENDMENTS = [
    {
        "number": 1,
        "year": 1951,
        "title": "1st Amendment",
        "summary": "Art.15(4); Art.19 public order etc.; 9th Schedule origins.",
        "effect": "Response to Champakam / Romesh Thappar line.",
        "concept_slugs": [HUB_SLUG, "jd-champakam", "jd-amendments-triggered"],
    },
    {
        "number": 24,
        "year": 1971,
        "title": "24th Amendment",
        "summary": "Restored Parliament power to amend FRs.",
        "effect": "Response to Golaknath; later read with Kesavananda.",
        "concept_slugs": [HUB_SLUG, "jd-golaknath", "jd-kesavananda", "jd-timeline-amendment-cases"],
    },
    {
        "number": 25,
        "year": 1971,
        "title": "25th Amendment",
        "summary": "Art.31C and property/compensation changes.",
        "effect": "Partly limited in Kesavananda.",
        "concept_slugs": [HUB_SLUG, "jd-kesavananda", "jd-amendments-struck"],
    },
    {
        "number": 39,
        "year": 1975,
        "title": "39th Amendment",
        "summary": "Art.329A election disputes shield.",
        "effect": "Clause 4 struck in Indira Nehru Gandhi case.",
        "concept_slugs": [HUB_SLUG, "jd-indira-gandhi", "jd-amendments-struck"],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "42nd Amendment",
        "summary": "Mini-Constitution — attempted to enlarge amending power.",
        "effect": "Key clauses checked in Minerva Mills / L. Chandra Kumar.",
        "concept_slugs": [HUB_SLUG, "jd-minerva-mills", "jd-amendments-struck"],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "44th Amendment",
        "summary": "Emergency and property reforms after Emergency.",
        "effect": "Corrective politics post-Jabalpur era.",
        "concept_slugs": [HUB_SLUG, "jd-adm-jabalpur"],
    },
    {
        "number": 52,
        "year": 1985,
        "title": "52nd Amendment",
        "summary": "Tenth Schedule — anti-defection.",
        "effect": "Para 7 struck in Kihoto Hollohan; rest largely upheld.",
        "concept_slugs": [HUB_SLUG, "jd-amendments-struck", "jd-compact-later"],
    },
    {
        "number": 86,
        "year": 2002,
        "title": "86th Amendment",
        "summary": "Art.21A — Right to Education.",
        "effect": "Codified Unni Krishnan education holding trajectory.",
        "concept_slugs": [HUB_SLUG, "jd-article-21-expansions", "jd-amendments-triggered"],
    },
    {
        "number": 93,
        "year": 2005,
        "title": "93rd Amendment",
        "summary": "Art.15(5) — education reservation including private unaided.",
        "effect": "Response to T.M.A. Pai / Inamdar line.",
        "concept_slugs": [HUB_SLUG, "jd-amendments-triggered", "jd-compact-later"],
    },
    {
        "number": 97,
        "year": 2011,
        "title": "97th Amendment",
        "summary": "Cooperative societies constitutionalisation.",
        "effect": "Partly struck in Rajendra N Shah (2021) for ratification flaw.",
        "concept_slugs": [HUB_SLUG, "jd-amendments-struck"],
    },
    {
        "number": 99,
        "year": 2014,
        "title": "99th Amendment",
        "summary": "NJAC replacing collegium.",
        "effect": "Struck down entirely in Fourth Judges Case (2015).",
        "concept_slugs": [HUB_SLUG, "jd-njac", "jd-amendments-struck"],
    },
]

SAMPLE_PYQS = [
    (
        2019,
        "In the context of Indian polity / Constitution, basic structure doctrine is primarily associated with which case?",
        "Kesavananda Bharati (1973).",
        [HUB_SLUG, "jd-kesavananda", "jd-which-case-what"],
    ),
    (
        2018,
        "Which judgement held that the right to privacy is protected as an intrinsic part of the right to life and personal liberty under Art.21?",
        "K.S. Puttaswamy v. Union of India (2017).",
        [HUB_SLUG, "jd-puttaswamy", "jd-article-21-expansions"],
    ),
    (
        2017,
        "The Supreme Court judgement in S.R. Bommai (1994) is important for which constitutional theme?",
        "Judicial review of Art.356 / federalism and secularism.",
        [HUB_SLUG, "jd-sr-bommai"],
    ),
    (
        2015,
        "The NJAC was declared unconstitutional primarily because it was held to violate which constitutional value?",
        "Independence of the judiciary (basic structure).",
        [HUB_SLUG, "jd-njac", "jd-cmp-njac-collegium"],
    ),
    (
        2013,
        "Doctrine of eclipse in Indian constitutional law is closely related to which Article?",
        "Article 13 (pre-Constitution laws inconsistent with FRs).",
        [HUB_SLUG, "jd-doc-fr-tools", "jd-doctrine-cheatsheet"],
    ),
    (
        2012,
        "Maneka Gandhi (1978) is a landmark for which interpretive shift?",
        "Expansive reading of Art.21 — procedure must be just, fair and reasonable; golden triangle with Arts. 14 and 19.",
        [HUB_SLUG, "jd-maneka-gandhi", "jd-cmp-gopalan-maneka"],
    ),
    (
        2010,
        "I.R. Coelho (2007) dealt with judicial review of laws placed in which Schedule?",
        "Ninth Schedule.",
        [HUB_SLUG, "jd-ir-coelho", "jd-network-bs"],
    ),
    (
        2008,
        "Harmonious construction between Fundamental Rights and Directive Principles is classically associated with?",
        "Minerva Mills (among other cases).",
        [HUB_SLUG, "jd-minerva-mills", "jd-doc-interpretation"],
    ),
    (
        2020,
        "Prospective overruling as a notable technique in Indian constitutional adjudication is famously linked to?",
        "Golaknath (1967).",
        [HUB_SLUG, "jd-golaknath", "jd-doc-interpretation"],
    ),
    (
        2016,
        "Vishaka guidelines were issued in the absence of domestic legislation on?",
        "Sexual harassment of women at the workplace.",
        [HUB_SLUG, "jd-vishaka"],
    ),
]


class Command(BaseCommand):
    help = "Seed Laxmikanth Part XII Judgements & Doctrines visual chapter."

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
                "title": "Judgements & Doctrines",
                "sort_order": 1,
                "book_ref": BOOK_REF,
                "summary": (
                    "Visual revision of Laxmikanth Part XII — landmark judgements, "
                    "Art.21 expansions, amendment cases, and constitutional doctrines."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Judgements & Doctrines",
                "summary": (
                    "Constitution’s case-law GPS — landmark judgements fix meaning; "
                    "doctrines are the interpretation toolkit."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start at the **four pillars**, then drill **flagship cases** (13-field cards). "
                    "Use **compact banks** for breadth, **Art.21** and **amendment** tables for Prelims, "
                    "and **doctrine groups** for one-liners. Finish with **Master Revision**.\n\n"
                    "This is a visual revision layer — not a substitute for Laxmikanth Part XII."
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
            for i, (ref, excerpt) in enumerate(cluster.get("articles") or []):
                ConceptArticle.objects.create(
                    concept=concept,
                    ref=ref,
                    excerpt=excerpt,
                    sort_order=i,
                )

        ConceptArticle.objects.filter(concept=hub).delete()
        ConceptArticle.objects.create(
            concept=hub,
            ref="Laxmikanth Part XII",
            excerpt="Ch.91–94 — judgements, Art.21, amendments, doctrines (pp.881–949).",
            sort_order=0,
        )

        jd_slugs = set(by_slug.keys())
        related_outside = {
            "basic-structure",
            "fundamental-rights",
            "amendment-of-constitution",
            "supreme-court",
            "judicial-activism",
            "emergency-provisions",
        }
        ConceptEdge.objects.filter(
            source__slug__in=jd_slugs, source__subject=subject
        ).filter(target__slug__in=jd_slugs | related_outside).delete()

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
            amendment, _ = ConstitutionalAmendment.objects.update_or_create(
                academy=academy,
                number=payload["number"],
                defaults=payload,
            )
            concepts = [
                by_slug[s] for s in amd_data["concept_slugs"] if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Judgements & Doctrines seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs."
            )
        )
