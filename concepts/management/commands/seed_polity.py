from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Subject

# Thin seed_polity stubs → rich chapter twins (same-topic only).
STUB_TO_TWIN = {
    "anti-defection": "pd-anti-defection",
    "attorney-general": "cb-attorney-general",
    "cag": "cb-cag",
    "collective-responsibility": "com-collective-responsibility",
    "election-commission": "cb-election-commission",
    "ordinance": "pr-ordinance",
    "public-accounts-committee": "pc-pac",
    "article-356": "emg-presidents-rule",
    "article-368": "amendment-of-constitution",
    "constitution-amendment-bill": "amendment-of-constitution",
    "federalism": "federal-system",
    "cabinet": "com-cabinet-role",
    "council-of-ministers": "central-council-of-ministers",
}

# Hubs owned by dedicated chapter seeds — do not overwrite when chapter exists.
CHAPTER_OWNED_CONCEPT_SLUGS = {
    "president",
    "vice-president",
    "prime-minister",
    "supreme-court",
    "high-court",
    "basic-structure",
    "fundamental-rights",
    "directive-principles",
    "fundamental-duties",
    "parliamentary-committees",
    "emergency-provisions",
}

# Keep published if present in CONCEPTS (none today — chapter hubs are skipped above).
KEEP_PUBLISHED_SLUGS: set[str] = set()


def resolve_slug(slug: str) -> str:
    return STUB_TO_TWIN.get(slug, slug)


# (title, slug, summary, body)
CONCEPTS = [
    (
        "Constitution",
        "constitution",
        "The supreme law of India that defines the structure of government and fundamental rights.",
        """## What it is

The Constitution of India is the supreme law. It lays down the framework for political principles, establishes the structure, procedures, powers and duties of government institutions, and sets out fundamental rights and duties of citizens.

## Why it matters for UPSC

Almost every Polity topic traces back to a constitutional provision, amendment, or convention. Treat the Constitution as the map root for Parliament, Judiciary, Executive, and rights.
""",
    ),
    (
        "Fundamental Rights",
        "fundamental-rights",
        "Justiciable rights guaranteed under Part III of the Constitution.",
        "Articles 12–35. Include equality, freedom, against exploitation, religion, cultural/educational rights, and constitutional remedies (Art. 32).",
    ),
    (
        "Directive Principles",
        "directive-principles",
        "Non-justiciable guidelines for the State under Part IV.",
        "DPSP aim at social and economic democracy. Conflict with Fundamental Rights is a classic UPSC theme (e.g. Minerva Mills).",
    ),
    (
        "Fundamental Duties",
        "fundamental-duties",
        "Citizen duties under Article 51A (Part IVA).",
        "Added by the 42nd Amendment on the Swaran Singh Committee recommendations.",
    ),
    (
        "Parliament",
        "parliament",
        "The Union legislature consisting of the President, Lok Sabha and Rajya Sabha.",
        """## Composition

Parliament = President + Lok Sabha + Rajya Sabha.

## Core powers

Law-making, budget, oversight of the executive, amendment of the Constitution (with special procedures), and impeachment-related roles.
""",
    ),
    (
        "Lok Sabha",
        "lok-sabha",
        "House of the People — directly elected lower house.",
        "Maximum strength and composition are set by the Constitution. Money Bills can only be introduced in Lok Sabha.",
    ),
    (
        "Rajya Sabha",
        "rajya-sabha",
        "Council of States — indirectly elected upper house.",
        "Permanent house; one-third members retire every two years. Limited role on Money Bills.",
    ),
    (
        "President of India",
        "president",
        "Constitutional head of the Union executive; part of Parliament.",
        "Elected by an electoral college. Assents to bills; has ordinance power under Article 123.",
    ),
    (
        "Vice-President",
        "vice-president",
        "Ex-officio Chairman of Rajya Sabha; acts as President when the office is vacant.",
        "Elected by members of both Houses of Parliament.",
    ),
    (
        "Speaker of Lok Sabha",
        "speaker",
        "Presiding officer of Lok Sabha; decisive role in Money Bill certification.",
        """## Key powers

- Maintains order in the House
- Certifies whether a bill is a Money Bill (Article 110) — decision is final
- Decides on disqualification under the Tenth Schedule (subject to judicial review after Kihoto Hollohan)
""",
    ),
    (
        "Deputy Speaker",
        "deputy-speaker",
        "Presides over Lok Sabha in the Speaker's absence.",
        "Elected by the Lok Sabha from among its members.",
    ),
    (
        "Money Bill",
        "money-bill",
        "A bill dealing only with matters listed in Article 110; special Lok Sabha-centric procedure.",
        """## Definition (Article 110)

A Money Bill contains **only** provisions dealing with taxation, borrowing, Consolidated Fund, Contingency Fund, appropriation, expenditure charged on the Consolidated Fund, receipt of money, or incidental matters.

## Procedure highlights

- Can be introduced **only in Lok Sabha** and only on the President's recommendation
- Rajya Sabha can suggest amendments within 14 days but cannot reject
- Speaker's certificate that a bill is a Money Bill is final

## Compare with Finance Bill

Finance Bills may include taxation plus other provisions and follow ordinary bill procedures (with nuances).
""",
    ),
    (
        "Article 110",
        "article-110",
        "Constitutional article defining Money Bills.",
        "Lists the exclusive subjects that make a bill a Money Bill. Also states that the Speaker's decision is final.",
    ),
    (
        "Finance Bill",
        "finance-bill",
        "Bill dealing with financial matters; broader than a Money Bill.",
        "Category A Finance Bills contain taxation plus other provisions. Not all Finance Bills are Money Bills.",
    ),
    (
        "Ordinary Bill",
        "ordinary-bill",
        "Legislative proposal that is neither a Money Bill nor a Constitution Amendment Bill.",
        "Can originate in either House. Deadlock may lead to a joint sitting under Article 108.",
    ),
    (
        "Constitution Amendment Bill",
        "constitution-amendment-bill",
        "Bill to amend the Constitution under Article 368.",
        "Different majorities and, for federal provisions, ratification by half the states.",
    ),
    (
        "Article 368",
        "article-368",
        "Procedure for amendment of the Constitution.",
        "Basic structure doctrine limits Parliament's amending power (Kesavananda Bharati).",
    ),
    (
        "Joint Sitting",
        "joint-sitting",
        "Mechanism under Article 108 to resolve deadlock on ordinary bills.",
        "Not available for Money Bills or Constitution Amendment Bills. Presided over by the Speaker.",
    ),
    (
        "Budget",
        "budget",
        "Annual financial statement presented to Parliament.",
        "Includes estimates of receipts and expenditure. Closely linked to Appropriation and Finance Bills.",
    ),
    (
        "Consolidated Fund of India",
        "consolidated-fund",
        "The main account of the Government of India into which revenues flow.",
        "No money can be withdrawn except under appropriation by law (Article 266).",
    ),
    (
        "Contingency Fund of India",
        "contingency-fund",
        "Fund for unforeseen expenditure placed at the disposal of the President.",
        "Advances are later authorized by Parliament (Article 267).",
    ),
    (
        "Public Account of India",
        "public-account",
        "Account for moneys received by the government other than revenues (e.g. provident funds).",
        "Does not require appropriation by Parliament for withdrawal in the same way as the Consolidated Fund.",
    ),
    (
        "Appropriation Bill",
        "appropriation-bill",
        "Bill authorizing withdrawal from the Consolidated Fund.",
        "Follows debate on demands for grants. Related to the budget cycle.",
    ),
    (
        "Cut Motion",
        "cut-motion",
        "Device to reduce a demand for grant in Lok Sabha.",
        "Types: policy cut, economy cut, token cut. Expresses disapproval of policy or expenditure.",
    ),
    (
        "Question Hour",
        "question-hour",
        "First hour of a sitting when MPs ask questions of ministers.",
        "Starred, unstarred, and short-notice questions.",
    ),
    (
        "Zero Hour",
        "zero-hour",
        "Informal device after Question Hour for raising urgent matters.",
        "Not mentioned in the Rules of Procedure; an Indian parliamentary innovation.",
    ),
    (
        "Parliamentary Committees",
        "parliamentary-committees",
        "Smaller bodies that scrutinize bills, budgets, and administration.",
        "Includes Financial Committees (PAC, Estimates, Public Undertakings) and Departmentally Related Standing Committees.",
    ),
    (
        "Public Accounts Committee",
        "public-accounts-committee",
        "Examines accounts showing appropriation of sums granted by Parliament.",
        "Assisted by the CAG. Chair traditionally from the Opposition in Lok Sabha practice.",
    ),
    (
        "Cabinet",
        "cabinet",
        "Core of the Council of Ministers; collective decision-making body.",
        "Real executive authority under the parliamentary system. Collective responsibility to Lok Sabha.",
    ),
    (
        "Council of Ministers",
        "council-of-ministers",
        "Body of ministers headed by the Prime Minister (Article 74).",
        "Includes Cabinet Ministers, Ministers of State, and Deputy Ministers.",
    ),
    (
        "Prime Minister",
        "prime-minister",
        "Head of government; leader of the majority in Lok Sabha in practice.",
        "Appointed by the President. Channels advice of the Council of Ministers.",
    ),
    (
        "Collective Responsibility",
        "collective-responsibility",
        "Council of Ministers is collectively responsible to Lok Sabha (Article 75).",
        "A no-confidence motion tests this responsibility.",
    ),
    (
        "No-Confidence Motion",
        "no-confidence-motion",
        "Motion expressing lack of confidence in the Council of Ministers.",
        "Can be moved only in Lok Sabha. If passed, the government must resign.",
    ),
    (
        "Ordinance",
        "ordinance",
        "Temporary law promulgated by the President when Parliament is not in session (Art. 123).",
        "Must be laid before Parliament and ceases if not approved within six weeks of reassembly.",
    ),
    (
        "Judiciary",
        "judiciary",
        "Independent third organ; Supreme Court at the apex.",
        "Guardian of the Constitution and Fundamental Rights. Judicial review is a basic feature.",
    ),
    (
        "Supreme Court",
        "supreme-court",
        "Highest court; original, appellate, and advisory jurisdiction.",
        "Articles 124–147. Writ jurisdiction under Article 32.",
    ),
    (
        "High Court",
        "high-court",
        "Apex court of a state / group of states.",
        "Writs under Article 226 have a wider scope than Article 32 in some respects.",
    ),
    (
        "Judicial Review",
        "judicial-review",
        "Power of courts to examine constitutionality of laws and executive action.",
        "Central to the basic structure doctrine and federal balance.",
    ),
    (
        "Basic Structure of the Constitution",
        "basic-structure",
        "Parliament’s Art. 368 power is wide but not unlimited — the basic structure is the unamendable foundation.",
        "Enriched by seed_basic_structure (Laxmikanth Ch.12 visual revision).",
    ),
    (
        "Executive",
        "executive",
        "Union executive: President, Vice-President, PM, Council of Ministers, Attorney General.",
        "In practice, real power rests with the Council of Ministers headed by the PM.",
    ),
    (
        "Federalism",
        "federalism",
        "Division of powers between Union and States.",
        "India is often described as a quasi-federal system with a strong Centre (Seventh Schedule).",
    ),
    (
        "Seventh Schedule",
        "seventh-schedule",
        "Union, State, and Concurrent Lists of legislative subjects.",
        "Residuary powers with the Union (Article 248).",
    ),
    (
        "Emergency Provisions",
        "emergency-provisions",
        "Articles 352, 356, 360 — national, state, and financial emergencies.",
        "Transform the federal balance; heavily tested in UPSC with 44th Amendment safeguards.",
    ),
    (
        "Article 356",
        "article-356",
        "President's Rule in a state when constitutional machinery fails.",
        "Subject to judicial review after S.R. Bommai.",
    ),
    (
        "Election Commission",
        "election-commission",
        "Autonomous body for elections to Parliament, state legislatures, and offices of President/VP.",
        "Article 324. Multi-member body headed by the CEC.",
    ),
    (
        "CAG",
        "cag",
        "Comptroller and Auditor General — audits government accounts.",
        "Reports examined by the Public Accounts Committee. Article 148.",
    ),
    (
        "Attorney General",
        "attorney-general",
        "Highest law officer of the Union (Article 76).",
        "Right of audience in all courts; can participate in Parliament without voting.",
    ),
    (
        "Anti-Defection Law",
        "anti-defection",
        "Tenth Schedule — disqualification for defection.",
        "Speaker/Chairman decides; judicial review available. Exceptions for mergers.",
    ),
    (
        "Whip",
        "whip",
        "Party official who ensures attendance and voting discipline.",
        "Direction of the whip is central to anti-defection voting cases.",
    ),
    (
        "Quorum",
        "quorum",
        "Minimum members required to constitute a sitting of a House.",
        "One-tenth of total membership of the House (Article 100).",
    ),
    (
        "Lame Duck Session",
        "lame-duck-session",
        "Last session of an existing Lok Sabha after a new one has been elected.",
        "Useful terminology for parliamentary procedure questions.",
    ),
]

DRAFT_STUB_SLUGS = {
    slug
    for _, slug, _, _ in CONCEPTS
    if slug not in CHAPTER_OWNED_CONCEPT_SLUGS and slug not in KEEP_PUBLISHED_SLUGS
}

# (source_slug, relation, target_slug) — twin-mapped stubs resolved at seed time.
EDGES = [
    ("constitution", "parent", "preamble"),
    ("constitution", "parent", "fundamental-rights"),
    ("constitution", "parent", "directive-principles"),
    ("constitution", "parent", "fundamental-duties"),
    ("constitution", "parent", "parliament"),
    ("constitution", "parent", "executive"),
    ("constitution", "parent", "judiciary"),
    ("constitution", "parent", "federalism"),
    ("constitution", "related", "article-368"),
    ("constitution", "related", "basic-structure"),
    ("parliament", "parent", "lok-sabha"),
    ("parliament", "parent", "rajya-sabha"),
    ("parliament", "parent", "president"),
    ("parliament", "related", "speaker"),
    ("parliament", "related", "money-bill"),
    ("parliament", "related", "ordinary-bill"),
    ("parliament", "related", "parliamentary-committees"),
    ("lok-sabha", "parent", "speaker"),
    ("lok-sabha", "parent", "deputy-speaker"),
    ("lok-sabha", "related", "money-bill"),
    ("lok-sabha", "related", "no-confidence-motion"),
    ("lok-sabha", "related", "cut-motion"),
    ("rajya-sabha", "related", "money-bill"),
    ("rajya-sabha", "related", "vice-president"),
    ("speaker", "related", "money-bill"),
    ("speaker", "related", "anti-defection"),
    ("speaker", "related", "joint-sitting"),
    ("money-bill", "prerequisite", "article-110"),
    ("money-bill", "related", "finance-bill"),
    ("money-bill", "related", "lok-sabha"),
    ("money-bill", "related", "rajya-sabha"),
    ("money-bill", "related", "speaker"),
    ("money-bill", "related", "budget"),
    ("money-bill", "related", "consolidated-fund"),
    ("article-110", "related", "money-bill"),
    ("finance-bill", "related", "money-bill"),
    ("finance-bill", "related", "budget"),
    ("ordinary-bill", "related", "joint-sitting"),
    ("ordinary-bill", "related", "parliament"),
    ("constitution-amendment-bill", "prerequisite", "article-368"),
    ("constitution-amendment-bill", "related", "basic-structure"),
    ("article-368", "related", "basic-structure"),
    ("budget", "related", "appropriation-bill"),
    ("budget", "related", "consolidated-fund"),
    ("budget", "related", "contingency-fund"),
    ("budget", "related", "cut-motion"),
    ("consolidated-fund", "related", "public-account"),
    ("consolidated-fund", "related", "appropriation-bill"),
    ("parliamentary-committees", "parent", "public-accounts-committee"),
    ("public-accounts-committee", "related", "cag"),
    ("executive", "parent", "president"),
    ("executive", "parent", "prime-minister"),
    ("executive", "parent", "council-of-ministers"),
    ("executive", "parent", "cabinet"),
    ("executive", "related", "ordinance"),
    ("council-of-ministers", "related", "collective-responsibility"),
    ("council-of-ministers", "related", "cabinet"),
    ("prime-minister", "related", "cabinet"),
    ("collective-responsibility", "related", "no-confidence-motion"),
    ("judiciary", "parent", "supreme-court"),
    ("judiciary", "parent", "high-court"),
    ("judiciary", "related", "judicial-review"),
    ("supreme-court", "related", "basic-structure"),
    ("supreme-court", "related", "judicial-review"),
    ("federalism", "related", "seventh-schedule"),
    ("federalism", "related", "emergency-provisions"),
    ("emergency-provisions", "parent", "article-356"),
    ("anti-defection", "related", "whip"),
    ("anti-defection", "related", "speaker"),
    ("question-hour", "related", "zero-hour"),
    ("question-hour", "related", "parliament"),
    ("president", "related", "ordinance"),
    ("president", "related", "parliament"),
    ("vice-president", "related", "rajya-sabha"),
    ("cag", "related", "public-accounts-committee"),
    ("attorney-general", "related", "executive"),
    ("election-commission", "related", "constitution"),
    ("quorum", "related", "lok-sabha"),
    ("quorum", "related", "rajya-sabha"),
    ("lame-duck-session", "related", "lok-sabha"),
]

ARTICLES = [
    ("money-bill", "Article 110", "Defines Money Bill and makes the Speaker's decision final."),
    ("article-110", "Article 110", "Full text reference for Money Bill definition."),
    ("finance-bill", "Article 117", "Special provisions as to financial bills."),
    ("ordinance", "Article 123", "Power of President to promulgate ordinances."),
    ("collective-responsibility", "Article 75", "Council of Ministers collectively responsible to Lok Sabha."),
    ("joint-sitting", "Article 108", "Joint sitting of both Houses in certain cases."),
    ("article-368", "Article 368", "Power of Parliament to amend the Constitution."),
    ("article-356", "Article 356", "Provisions in case of failure of constitutional machinery in States."),
    ("consolidated-fund", "Article 266", "Consolidated Funds and public accounts of India and of the States."),
    ("contingency-fund", "Article 267", "Contingency Fund."),
    ("cag", "Article 148", "Comptroller and Auditor-General of India."),
    ("attorney-general", "Article 76", "Attorney-General for India."),
    ("election-commission", "Article 324", "Superintendence, direction and control of elections."),
    ("quorum", "Article 100", "Voting in Houses, power of Houses to act notwithstanding vacancies and quorum."),
    ("supreme-court", "Article 32", "Remedies for enforcement of rights conferred by Part III."),
    ("high-court", "Article 226", "Power of High Courts to issue certain writs."),
]

PYQS = [
    (
        2015,
        "The Speaker of the Lok Sabha can certify a bill as a Money Bill. Which constitutional provision is related to this?",
        "Article 110 — Speaker's decision on whether a bill is a Money Bill is final.",
        ["money-bill", "article-110", "speaker"],
    ),
    (
        2018,
        "With reference to Money Bills, which of the following statements is/are correct?",
        "Focus on: introduction only in Lok Sabha; Rajya Sabha's limited 14-day recommendatory role; Speaker's certificate.",
        ["money-bill", "lok-sabha", "rajya-sabha"],
    ),
    (
        2013,
        "Consider the following statements: The Parliamentary Committee on Public Accounts... (role of CAG).",
        "PAC examines appropriation accounts with CAG assistance.",
        ["public-accounts-committee", "cag"],
    ),
    (
        2019,
        "Which one of the following is not a feature of Money Bill?",
        "Recall Article 110 list; contrast with Finance Bill / ordinary bill features.",
        ["money-bill", "finance-bill"],
    ),
    (
        2020,
        "Rajya Sabha has equal powers with Lok Sabha in which of the following matters?",
        "Not Money Bills — equal powers typically for ordinary legislation subjects like impeachment initiation nuances etc. Classic comparison question.",
        ["rajya-sabha", "lok-sabha", "money-bill"],
    ),
    (
        2016,
        "Which of the following is/are the exclusive power(s) of Lok Sabha?",
        "Money Bills, no-confidence, budget introduction — exclusive/special roles of Lok Sabha.",
        ["lok-sabha", "money-bill", "no-confidence-motion"],
    ),
    (
        2017,
        "The main advantage of the parliamentary form of government is that...",
        "Collective responsibility and harmony between legislature and executive.",
        ["collective-responsibility", "cabinet", "parliament"],
    ),
    (
        2014,
        "Which of the following are the discretionary powers given to the Governor of a State? / related federal questions often paired with Art 356 themes.",
        "Link to emergency and federalism themes for revision.",
        ["article-356", "federalism", "emergency-provisions"],
    ),
    (
        2021,
        "Constitutional government means...",
        "Limited government; supremacy of constitution; often linked to basic structure and judicial review.",
        ["constitution", "basic-structure", "judicial-review"],
    ),
    (
        2011,
        "The authorization for the withdrawal of funds from the Consolidated Fund of India must come from...",
        "Parliament via Appropriation Act.",
        ["consolidated-fund", "appropriation-bill", "budget"],
    ),
]


def _retire_polity_stubs(subject: Subject, stdout=None, style=None) -> dict[str, int]:
    """Unpublish thin stubs; rewire edges and PYQs onto rich twins where mapped."""
    drafted = Concept.objects.filter(
        subject=subject, slug__in=DRAFT_STUB_SLUGS
    ).update(status=Concept.Status.DRAFT)

    twin_slugs = set(STUB_TO_TWIN.values())
    twins = {
        c.slug: c
        for c in Concept.objects.filter(subject=subject, slug__in=twin_slugs)
    }
    stubs = {
        c.slug: c
        for c in Concept.objects.filter(subject=subject, slug__in=STUB_TO_TWIN.keys())
    }

    edges_rewired = 0
    edges_dropped = 0
    for stub_slug, twin_slug in STUB_TO_TWIN.items():
        stub = stubs.get(stub_slug)
        twin = twins.get(twin_slug)
        if not stub or not twin:
            continue

        for edge in list(
            ConceptEdge.objects.filter(Q(source=stub) | Q(target=stub))
        ):
            new_source = twin if edge.source_id == stub.id else edge.source
            new_target = twin if edge.target_id == stub.id else edge.target
            if new_source.id == new_target.id:
                edge.delete()
                edges_dropped += 1
                continue
            exists = ConceptEdge.objects.filter(
                source=new_source,
                target=new_target,
                relation_type=edge.relation_type,
            ).exists()
            if exists:
                edge.delete()
                edges_dropped += 1
            else:
                edge.source = new_source
                edge.target = new_target
                edge.save(update_fields=["source", "target"])
                edges_rewired += 1

        for pyq in stub.pyqs.all():
            pyq.concepts.add(twin)
            pyq.concepts.remove(stub)

    if stdout and style:
        stdout.write(
            style.SUCCESS(
                f"Retired stubs: drafted={drafted}, edges_rewired={edges_rewired}, "
                f"edges_dropped={edges_dropped}."
            )
        )
    return {
        "drafted": drafted,
        "edges_rewired": edges_rewired,
        "edges_dropped": edges_dropped,
    }


class Command(BaseCommand):
    help = (
        "Seed Polity subject stubs (as draft), edges, articles, sample PYQs, "
        "then enrich visual Laxmikanth chapters."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug to seed into (default: fortuneias).",
        )
        parser.add_argument(
            "--skip-chapters",
            action="store_true",
            help="Skip dedicated chapter seed commands (stubs + retirement only).",
        )

    def handle(self, *args, **options):
        from academies.seed_utils import get_academy_or_fail

        academy = get_academy_or_fail(options["academy"])
        subject, _ = Subject.objects.update_or_create(
            academy=academy,
            slug="polity",
            defaults={
                "name": "Polity",
                "description": "Indian Constitution, Parliament, Executive, Judiciary, and related concepts.",
                "is_active": True,
            },
        )

        concept_map: dict[str, Concept] = {}
        for title, slug, summary, body in CONCEPTS:
            if slug in CHAPTER_OWNED_CONCEPT_SLUGS:
                existing = Concept.objects.filter(subject=subject, slug=slug).first()
                if existing is not None and existing.chapter_id is not None:
                    concept_map[slug] = existing
                    continue
            status = (
                Concept.Status.PUBLISHED
                if slug in KEEP_PUBLISHED_SLUGS
                else Concept.Status.DRAFT
                if slug in DRAFT_STUB_SLUGS
                else Concept.Status.PUBLISHED
            )
            # Chapter-owned hubs created before their chapter seed still publish;
            # dedicated seeds overwrite them later.
            if slug in CHAPTER_OWNED_CONCEPT_SLUGS:
                status = Concept.Status.PUBLISHED
            concept, _ = Concept.objects.update_or_create(
                subject=subject,
                slug=slug,
                defaults={
                    "title": title,
                    "summary": summary,
                    "body": body,
                    "status": status,
                },
            )
            concept_map[slug] = concept

        # Resolve twin targets already in DB (from prior chapter seeds).
        needed: set[str] = set(STUB_TO_TWIN.values())
        for src, _, tgt in EDGES:
            needed.add(resolve_slug(src))
            needed.add(resolve_slug(tgt))
        for *_, slugs in PYQS:
            for slug in slugs:
                needed.add(resolve_slug(slug))
        for c in Concept.objects.filter(subject=subject, slug__in=needed):
            concept_map.setdefault(c.slug, c)

        # Only refresh edges that involve draft stubs (do not wipe chapter graphs).
        ConceptEdge.objects.filter(
            Q(source__subject=subject) | Q(target__subject=subject),
        ).filter(
            Q(source__slug__in=DRAFT_STUB_SLUGS) | Q(target__slug__in=DRAFT_STUB_SLUGS)
        ).delete()

        edges_created = 0
        seen_edges: set[tuple[str, str, str]] = set()
        for source_slug, relation, target_slug in EDGES:
            source_slug = resolve_slug(source_slug)
            target_slug = resolve_slug(target_slug)
            if source_slug == target_slug:
                continue
            key = (source_slug, relation, target_slug)
            if key in seen_edges:
                continue
            seen_edges.add(key)
            source = concept_map.get(source_slug)
            target = concept_map.get(target_slug)
            if not source or not target:
                self.stderr.write(f"Skipping edge {source_slug} -> {target_slug}")
                continue
            _, created = ConceptEdge.objects.get_or_create(
                source=source,
                target=target,
                relation_type=relation,
            )
            if created:
                edges_created += 1

        # Refresh articles for draft stubs / twin-mapped article targets only.
        article_targets = {
            resolve_slug(slug) if slug in STUB_TO_TWIN else slug
            for slug, _, _ in ARTICLES
            if slug in DRAFT_STUB_SLUGS or slug in STUB_TO_TWIN
        }
        ConceptArticle.objects.filter(
            concept__subject=subject,
            concept__slug__in=article_targets | (DRAFT_STUB_SLUGS & {s for s, _, _ in ARTICLES}),
        ).delete()

        articles_created = 0
        for concept_slug, ref, excerpt in ARTICLES:
            if concept_slug in CHAPTER_OWNED_CONCEPT_SLUGS:
                # Chapter seeds own these articles; do not clobber.
                continue
            resolved = resolve_slug(concept_slug)
            concept = concept_map.get(resolved) or concept_map.get(concept_slug)
            if not concept:
                continue
            ConceptArticle.objects.get_or_create(
                concept=concept,
                ref=ref,
                defaults={"excerpt": excerpt},
            )
            articles_created += 1

        for year, question, answer_key, concept_slugs in PYQS:
            pyq, _ = PYQ.objects.update_or_create(
                academy=academy,
                year=year,
                question=question,
                defaults={"answer_key": answer_key},
            )
            linked: list[Concept] = []
            seen: set[int] = set()
            for slug in concept_slugs:
                resolved = resolve_slug(slug)
                concept = concept_map.get(resolved) or concept_map.get(slug)
                if concept and concept.id not in seen:
                    linked.append(concept)
                    seen.add(concept.id)
            managed = DRAFT_STUB_SLUGS | set(STUB_TO_TWIN.keys()) | set(
                STUB_TO_TWIN.values()
            )
            keep = [
                c
                for c in pyq.concepts.all()
                if c.slug not in managed and c.id not in seen
            ]
            pyq.concepts.set(keep + linked)

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded Polity stubs ({academy.slug}): {len(concept_map)} concepts, "
                f"{edges_created} new edges, {articles_created} articles, {len(PYQS)} PYQs."
            )
        )

        if not options["skip_chapters"]:
            from django.core.management import call_command

            call_command("seed_historical_background", academy=academy.slug)
            call_command("seed_making_of_constitution", academy=academy.slug)
            call_command("seed_concept_of_constitution", academy=academy.slug)
            call_command("seed_salient_features", academy=academy.slug)
            call_command("seed_preamble", academy=academy.slug)
            call_command("seed_union_territory", academy=academy.slug)
            call_command("seed_citizenship", academy=academy.slug)
            call_command("seed_fundamental_rights", academy=academy.slug)
            call_command("seed_directive_principles", academy=academy.slug)
            call_command("seed_fundamental_duties", academy=academy.slug)
            call_command("seed_amendment_constitution", academy=academy.slug)
            call_command("seed_basic_structure", academy=academy.slug)
            call_command("seed_parliamentary_system", academy=academy.slug)
            call_command("seed_federal_system", academy=academy.slug)
            call_command("seed_emergency_provisions", academy=academy.slug)
            call_command("seed_president", academy=academy.slug)
            call_command("seed_vice_president", academy=academy.slug)
            call_command("seed_prime_minister", academy=academy.slug)
            call_command("seed_chief_minister", academy=academy.slug)
            call_command("seed_central_council_of_ministers", academy=academy.slug)
        call_command("seed_cabinet_committees", academy=academy.slug)
        call_command("seed_parliament_structure", academy=academy.slug)
        call_command("seed_parliament_procedure", academy=academy.slug)
        call_command("seed_parliament_powers", academy=academy.slug)
        call_command("seed_parliamentary_committees", academy=academy.slug)
            call_command("seed_supreme_court", academy=academy.slug)
            call_command("seed_judicial_activism", academy=academy.slug)
            call_command("seed_public_interest_litigation", academy=academy.slug)
            call_command("seed_governor", academy=academy.slug)
            call_command("seed_state_council_of_ministers", academy=academy.slug)
            call_command("seed_state_legislature", academy=academy.slug)
            call_command("seed_high_court", academy=academy.slug)
            call_command("seed_subordinate_courts", academy=academy.slug)
            call_command("seed_tribunals", academy=academy.slug)
            call_command("seed_consumer_commissions", academy=academy.slug)
            call_command("seed_lok_adalats", academy=academy.slug)
            call_command("seed_panchayati_raj", academy=academy.slug)
            call_command("seed_other_constitutional_dimensions", academy=academy.slug)
            call_command("seed_political_dynamics", academy=academy.slug)
            call_command("seed_union_territories", academy=academy.slug)
            call_command("seed_constitutional_bodies", academy=academy.slug)
            call_command("seed_non_constitutional_bodies", academy=academy.slug)
            call_command("seed_working_of_the_constitution", academy=academy.slug)
            call_command("seed_judgements_doctrines", academy=academy.slug)
            call_command("seed_world_constitutions", academy=academy.slug)

        # After chapter seeds (or when twins already exist), unpublish stubs and rewire.
        _retire_polity_stubs(subject, stdout=self.stdout, style=self.style)
