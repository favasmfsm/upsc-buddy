"""Seed Laxmikanth Ch.23 Parliament — Powers, RS & Privileges (visual revision — Part III)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "parliament-powers-privileges"
CHAPTER_SLUG = "parliament-powers-privileges"

ENTRY_PILLARS = [
    {
        "id": "role",
        "articles": "7 heads",
        "label": "Multifunctional role",
        "slug": "pwr-multifunctional",
        "detail": "Legislative · executive · financial · constituent · judicial · electoral · other.",
        "tone": "teal",
    },
    {
        "id": "control",
        "articles": "Limits",
        "label": "Ineffectiveness of control",
        "slug": "pwr-ineffectiveness",
        "detail": "Why parliamentary oversight often falls short in practice.",
        "tone": "olive",
    },
    {
        "id": "rs",
        "articles": "Equal · Unequal · Special",
        "label": "Position of Rajya Sabha",
        "slug": "pwr-rajya-sabha",
        "detail": "Equal with LS · unequal (finance/CoM) · four special powers.",
        "tone": "gold",
    },
    {
        "id": "priv",
        "articles": "Art. 105",
        "label": "Privileges",
        "slug": "pwr-privileges",
        "detail": "Collective vs individual · breach vs contempt · five sources.",
        "tone": "orange",
    },
    {
        "id": "sov",
        "articles": "Limits",
        "label": "Sovereignty",
        "slug": "pwr-sovereignty",
        "detail": "British Dicey vs Indian limits — written · federal · JR · FRs.",
        "tone": "terracotta",
    },
    {
        "id": "tables",
        "articles": "23.5–23.8",
        "label": "Revision tables",
        "slug": "pwr-revision-tables",
        "detail": "Seat allocation · LS durations · Speakers · articles at a glance.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pwr-weight-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "What the Houses can do — and where they stop",
        "topic_label": "Parliament — Powers, RS & Privileges",
        "subject_label": "Arts 105+ · Ch. 23 (pp. 370–392)",
        "relation_label": "Protects you from",
        "protects_from": [
            "Calling the Indian Parliament a sovereign body like the UK’s",
            "Extending privileges to the President",
            "Treating RS as a mere delaying chamber with no special powers",
            "Equating breach of privilege with every contempt",
        ],
        "insight": (
            "Powers, federal second chamber, privileges, and sovereignty limits — "
            "the closing map of Ch.23 before committees."
        ),
    },
    {
        "id": "pwr-entry-pillars",
        "type": "pillars",
        "title": "Six revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "pwr-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "7-function map → why control weakens → RS equal/unequal/4 special → "
            "privileges (collective/individual; not President) → sovereignty four limits. "
            "Prior: Structure & Procedure. Next: Parliamentary Committees (Ch.24)."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Multifunctional Role of Parliament",
        "slug": "pwr-multifunctional",
        "sort_order": 1,
        "summary": (
            "Seven power heads — legislative, executive control, financial, constituent, "
            "judicial, electoral, and residual/other functions."
        ),
        "body": (
            "## Seven heads\n\n"
            "1. **Legislative** — Union & Concurrent Lists; residuary; emergency expansions; "
            "ordinance replacement\n"
            "2. **Executive** — collective responsibility to LS; questions, motions, committees; "
            "ministers must be / become MPs\n"
            "3. **Financial** — budget, DFGs, Appropriation & Finance Bills; no tax without law\n"
            "4. **Constituent** — amend Constitution (Art. 368) within basic structure limits\n"
            "5. **Judicial** — impeachment of President; removal of judges / CAG / CEC etc. by address; "
            "breach of privilege punishments\n"
            "6. **Electoral** — elect President & VP; parts of electoral college; LS elects Speaker/Dy\n"
            "7. **Other** — reports of constitutional bodies; create AIS (via RS Art. 312); "
            "delimit; admit/alter states (Arts 2–3); etc.\n\n"
            "### Memory\n"
            "**L-E-F-C-J-E-O** — Legislative · Executive · Financial · Constituent · "
            "Judicial · Electoral · Other."
        ),
        "articles": [
            ("Laxmikanth Ch. 23", "Multifunctional role of Parliament — seven power categories."),
            ("Arts 79–122", "Organisation through privileges framework for Union Parliament."),
        ],
        "visual_blocks": [
            {
                "id": "pwr-role-pillars",
                "type": "pillars",
                "title": "Seven function chips",
                "items": [
                    {
                        "id": "leg",
                        "articles": "Lists",
                        "label": "Legislative",
                        "slug": "pwr-multifunctional",
                        "detail": "Law-making across Union/Concurrent (+ exceptions).",
                        "tone": "teal",
                    },
                    {
                        "id": "exec",
                        "articles": "Art. 75",
                        "label": "Executive",
                        "slug": "pwr-multifunctional",
                        "detail": "Collective responsibility · oversight tools.",
                        "tone": "olive",
                    },
                    {
                        "id": "fin",
                        "articles": "Art. 112",
                        "label": "Financial",
                        "slug": "ppb-budget",
                        "detail": "Purse of the nation — budget & grants.",
                        "tone": "gold",
                    },
                    {
                        "id": "const",
                        "articles": "Art. 368",
                        "label": "Constituent",
                        "slug": "pwr-multifunctional",
                        "detail": "Amend within basic structure.",
                        "tone": "orange",
                    },
                    {
                        "id": "jud",
                        "articles": "Removal",
                        "label": "Judicial",
                        "slug": "pwr-multifunctional",
                        "detail": "Impeach · address for removal · privileges.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "elec",
                        "articles": "Arts 54–66",
                        "label": "Electoral",
                        "slug": "pwr-multifunctional",
                        "detail": "President · VP · House officers.",
                        "tone": "maroon",
                    },
                ],
            },
        ],
    },
    {
        "title": "Ineffectiveness of Parliamentary Control",
        "slug": "pwr-ineffectiveness",
        "sort_order": 2,
        "summary": (
            "Practical limits on Parliament’s control over the executive — time, majority, "
            "delegated legislation, and information asymmetry."
        ),
        "body": (
            "## Why oversight weakens (typical Laxmikanth points)\n\n"
            "- Volume and complexity of legislative/financial business\n"
            "- Majority party dominance / whip discipline reduces critical scrutiny\n"
            "- Growth of **delegated legislation** shifts detail to executive\n"
            "- Insufficient time for every bill and account on the floor\n"
            "- Information and expertise asymmetry vs bureaucracy\n"
            "- Frequent disruptions and lost sittings\n"
            "- Financial control diluted when DFG voting is guillotined\n\n"
            "Committees (next chapter) exist partly to repair these gaps — "
            "but recommendations remain largely **advisory**."
        ),
        "articles": [
            ("Laxmikanth Ch. 23", "Ineffectiveness of parliamentary control over the executive."),
        ],
        "visual_blocks": [
            {
                "id": "pwr-ineff-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Link forward",
                "body": (
                    "Floor weakness → committee strength. Open **Parliamentary Committees** "
                    "for PAC/Estimates/DRSCs as the specialised workbench."
                ),
            },
        ],
    },
    {
        "title": "Position of Rajya Sabha",
        "slug": "pwr-rajya-sabha",
        "sort_order": 3,
        "summary": (
            "Equal with LS in many spheres; unequal on money/CoM/joint sitting arithmetic; "
            "four exclusive special powers (249, 312, VP removal, emergency approval when LS dissolved)."
        ),
        "body": (
            "## Equal status with Lok Sabha\n\n"
            "Broadly equal on: introduction/passage of ordinary & most financial bills; "
            "constitutional amendments; impeachment; election/removal of President; "
            "approval of ordinances; proclamations (when both Houses sit); "
            "consideration of reports; enlarging SC/HC jurisdiction; etc.\n\n"
            "## Unequal status\n\n"
            "- Money Bills: LS primacy (RS recommends / 14 days)\n"
            "- DFGs: LS alone votes\n"
            "- CoM responsible to **LS** only\n"
            "- Joint sitting: LS numerical advantage\n"
            "- Dissolution: only LS dissolves\n"
            "- Speaker (not RS Chairman) certifies Money Bills / chairs joint sittings\n\n"
            "## Four special powers of Rajya Sabha\n\n"
            "1. **Art. 249** — authorise Parliament to legislate on a State List matter (national interest)\n"
            "2. **Art. 312** — authorise creation of new **All-India Services**\n"
            "3. **Art. 67** — initiate resolution for **removal of Vice-President** (only in RS)\n"
            "4. **Arts 352 / 356 / 360** — if LS dissolved, proclamation can remain effective "
            "if approved by **RS alone** within the allowed period\n\n"
            "## Comparative place\n\n"
            "Not as weak as UK **House of Lords**; not as strong as US **Senate**. "
            "Except finance and CoM control, RS is broadly coordinate with LS.\n\n"
            "### Utility\n"
            "Checks hasty LS legislation · room for nominated experts · federal safeguard for states."
        ),
        "articles": [
            ("Art. 249", "Power of Parliament to legislate with respect to a matter in the State List."),
            ("Art. 312", "All-India Services."),
            ("Art. 67", "Term of office of Vice-President — removal resolution in RS."),
            ("Arts 352, 356, 360", "Emergency proclamations — RS role when LS dissolved."),
        ],
        "visual_blocks": [
            {
                "id": "pwr-rs-tree",
                "type": "tree",
                "title": "RS position map",
                "root": {
                    "id": "rs",
                    "label": "Rajya Sabha",
                    "children": [
                        {
                            "id": "eq",
                            "label": "Equal with LS",
                            "detail": "Ordinary legislation · CAA · impeachment · reports",
                        },
                        {
                            "id": "uneq",
                            "label": "Unequal",
                            "detail": "Money · DFGs · CoM responsibility · joint sitting maths",
                        },
                        {
                            "id": "sp",
                            "label": "Four special",
                            "detail": "249 · 312 · VP removal · emergency if LS dissolved",
                            "slug": "pwr-rajya-sabha",
                        },
                    ],
                },
            },
            {
                "id": "pwr-rs-memory",
                "type": "callout",
                "tone": "tip",
                "title": "Memory — 249 · 312 · 67 · emergency",
                "body": (
                    "State List law · All-India Services · start VP removal · keep emergency alive "
                    "when Lok Sabha is dissolved."
                ),
            },
        ],
    },
    {
        "title": "Parliamentary Privileges",
        "slug": "pwr-privileges",
        "sort_order": 4,
        "summary": (
            "Collective and individual privileges (Art. 105); extend to AG & ministers who speak; "
            "not to President; breach vs contempt; five sources; still largely uncodified."
        ),
        "body": (
            "## Meaning\n\n"
            "Special rights, immunities, exemptions of each House, its committees, and members — "
            "to secure independence and effectiveness.\n\n"
            "Also extend to persons entitled to speak/participate (e.g. **Attorney General**, "
            "**Union ministers**). Do **not** extend to the **President**.\n\n"
            "## Collective privileges\n\n"
            "- Publish debates/proceedings; exclude strangers; secret sittings\n"
            "- Make Rules; punish breach/contempt (reprimand, admonition, imprisonment; "
            "suspension/expulsion for members)\n"
            "- Immediate info of arrest/detention/conviction of a member\n"
            "- Inquire; summon witnesses/papers\n"
            "- Courts barred from inquiring into House proceedings\n"
            "- No arrest / legal process inside precincts without presiding officer’s leave\n\n"
            "44th CAA restored press freedom to publish **true reports** of proceedings "
            "(not secret sittings) without prior House permission.\n\n"
            "## Individual privileges\n\n"
            "1. Freedom from arrest in **civil** cases during session + **40 days** before/after "
            "(not criminal / preventive detention)\n"
            "2. **Freedom of speech** in Parliament / committees — no court proceedings for "
            "speech or vote (subject to Constitution & Rules)\n"
            "3. Exempt from jury service; may refuse to appear as witness while House is in session\n\n"
            "## Breach vs contempt\n\n"
            "- **Breach of privilege** — violation of a specific privilege → always contempt\n"
            "- **Contempt** — broader affront to dignity/authority; may occur **without** a specific breach "
            "(e.g. disobedience to a House order)\n\n"
            "## Sources (five)\n\n"
            "1. Constitutional provisions (Art. 105 — speech & publication expressly)\n"
            "2. Laws of Parliament\n"
            "3. Rules of both Houses\n"
            "4. Parliamentary conventions\n"
            "5. Judicial interpretations\n\n"
            "Other privileges originally tied to UK Commons as on 26 Jan 1950; "
            "44th CAA verbal change to privileges as on 20 June 1979 — still **not exhaustively codified**."
        ),
        "articles": [
            ("Art. 105", "Powers, privileges, etc., of the Houses of Parliament and of the members and committees thereof."),
            ("44th CAA", "Press true reports; verbal change dropping direct Commons reference."),
        ],
        "visual_blocks": [
            {
                "id": "pwr-priv-compare",
                "type": "compare",
                "title": "Collective vs Individual",
                "left": {
                    "title": "Collective",
                    "items": [
                        "Publish / exclude strangers",
                        "Punish breach & contempt",
                        "Control precincts",
                        "Bar court inquiry into proceedings",
                    ],
                },
                "right": {
                    "title": "Individual",
                    "items": [
                        "Civil arrest immunity (±40 days)",
                        "Freedom of speech / vote",
                        "Jury / witness exemptions",
                    ],
                },
            },
            {
                "id": "pwr-priv-trap",
                "type": "callout",
                "tone": "trap",
                "title": "President ≠ privileges",
                "body": (
                    "President is part of Parliament for organisation/assent, but parliamentary "
                    "privileges **do not** extend to the President."
                ),
            },
        ],
    },
    {
        "title": "Sovereignty of Parliament",
        "slug": "pwr-sovereignty",
        "sort_order": 5,
        "summary": (
            "UK Diceyan sovereignty vs Indian Parliament — limited by written Constitution, "
            "federalism, judicial review, and Fundamental Rights (closer to US Congress)."
        ),
        "body": (
            "## British doctrine (Dicey)\n\n"
            "1. Parliament can make / amend / repeal **any** law\n"
            "2. No legal distinction between ordinary and constitutional laws\n"
            "3. Courts **cannot** invalidate Acts of Parliament\n\n"
            "## Why India is different — four limits\n\n"
            "1. **Written Constitution** — Parliament operates within defined spheres; "
            "legislative ≠ constituent authority; some amendments need state ratification\n"
            "2. **Federal system** — Union/State Lists; State List only in exceptional cases\n"
            "3. **Judicial review** — SC/HCs can strike down unconstitutional laws\n"
            "4. **Fundamental Rights (Part III)** — Art. 13 voids inconsistent laws\n\n"
            "Hence Indian Parliament is **not** sovereign in the British sense; "
            "closer to the **US Congress** (written charter + federalism + JR + Bill of Rights).\n\n"
            "### Exam line\n"
            "Nomenclature looks Westminster; legal sovereignty does **not**."
        ),
        "articles": [
            ("Laxmikanth Ch. 23", "Sovereignty of Parliament — British doctrine vs Indian limits."),
            ("Art. 13", "Laws inconsistent with Fundamental Rights."),
            ("Art. 368", "Power of Parliament to amend the Constitution — limited by basic structure."),
        ],
        "visual_blocks": [
            {
                "id": "pwr-sov-compare",
                "type": "compare",
                "title": "UK vs India",
                "left": {
                    "title": "British Parliament",
                    "items": [
                        "Legal sovereignty",
                        "Unwritten constitution",
                        "No judicial review of Acts",
                        "Unitary state",
                    ],
                },
                "right": {
                    "title": "Indian Parliament",
                    "items": [
                        "Legally limited",
                        "Written Constitution",
                        "Judicial review",
                        "Federal division + FRs",
                    ],
                },
            },
            {
                "id": "pwr-sov-pillars",
                "type": "pillars",
                "title": "Four Indian limits",
                "items": [
                    {
                        "id": "writ",
                        "articles": "Const.",
                        "label": "Written Constitution",
                        "slug": "pwr-sovereignty",
                        "detail": "Defined authority; amendment rules.",
                        "tone": "teal",
                    },
                    {
                        "id": "fed",
                        "articles": "Lists",
                        "label": "Federalism",
                        "slug": "pwr-sovereignty",
                        "detail": "Cannot freely invade State List.",
                        "tone": "olive",
                    },
                    {
                        "id": "jr",
                        "articles": "SC/HC",
                        "label": "Judicial review",
                        "slug": "pwr-sovereignty",
                        "detail": "Ultra vires laws can fall.",
                        "tone": "gold",
                    },
                    {
                        "id": "fr",
                        "articles": "Art. 13",
                        "label": "Fundamental Rights",
                        "slug": "pwr-sovereignty",
                        "detail": "Inconsistent laws void.",
                        "tone": "orange",
                    },
                ],
            },
        ],
    },
    {
        "title": "Revision Tables & Articles Glance",
        "slug": "pwr-revision-tables",
        "sort_order": 6,
        "summary": (
            "End-matter of Ch.23 — seat allocation (Table 23.5), LS durations (23.6), "
            "Speakers (23.7), and articles related to Parliament (23.8)."
        ),
        "body": (
            "## What to scan in Laxmikanth tables\n\n"
            "| Table | Use |\n"
            "|-------|-----|\n"
            "| **23.5** | RS/LS seats by state/UT + SC/ST reserved LS seats |\n"
            "| **23.6** | Durations of successive Lok Sabhas |\n"
            "| **23.7** | Speakers of the Lok Sabha |\n"
            "| **23.8** | Articles related to Parliament at a glance |\n\n"
            "## Article clusters (revision)\n\n"
            "- **79–88** — organisation, composition hooks, sessions, ministers/AG rights\n"
            "- **89–98** — officers & secretariat\n"
            "- **99–104** — oath, voting, vacancies, disqualifications\n"
            "- **105–106** — privileges; salaries\n"
            "- **107–122** — legislative procedure, joint sitting, money/financial bills, "
            "budget/estimates, rules, courts barred from inquiring into proceedings, etc.\n\n"
            "Keep Table 23.8 as your **last-night** article sheet for this chapter trio."
        ),
        "articles": [
            ("Table 23.5", "Allocation of seats in Parliament; SC/ST reservation in LS."),
            ("Table 23.8", "Articles related to Parliament at a glance."),
        ],
        "visual_blocks": [
            {
                "id": "pwr-tables-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims habit",
                "body": (
                    "For number traps (max strength, present strength, UT RS seats, freeze year 2026, "
                    "reservation till 2030), pair this cluster with **Structure & Membership**."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pwr-multifunctional"),
    (HUB_SLUG, "parent", "pwr-ineffectiveness"),
    (HUB_SLUG, "parent", "pwr-rajya-sabha"),
    (HUB_SLUG, "parent", "pwr-privileges"),
    (HUB_SLUG, "parent", "pwr-sovereignty"),
    (HUB_SLUG, "parent", "pwr-revision-tables"),
    ("pwr-multifunctional", "related", "pwr-ineffectiveness"),
    ("pwr-multifunctional", "related", "pwr-rajya-sabha"),
    ("pwr-rajya-sabha", "related", "pwr-privileges"),
    ("pwr-privileges", "related", "pwr-sovereignty"),
    ("pwr-sovereignty", "related", "pwr-revision-tables"),
    ("pwr-ineffectiveness", "related", "parliamentary-committees"),
    ("parliament-structure-membership", "related", HUB_SLUG),
    ("parliament-procedure-budget", "related", HUB_SLUG),
    ("basic-structure", "related", "pwr-sovereignty"),
]

SAMPLE_PYQS = [
    (
        2013,
        "Which of the following are the exclusive powers of the Rajya Sabha?",
        "Art. 249 (State List law), Art. 312 (All-India Services), initiate VP removal, "
        "and approve emergencies when LS is dissolved.",
        ["pwr-rajya-sabha", HUB_SLUG],
    ),
    (
        2015,
        "Parliamentary privileges in India:",
        "Belong to each House collectively and to members individually; do not extend to the President.",
        ["pwr-privileges", HUB_SLUG],
    ),
    (
        2017,
        "The Indian Parliament is not a sovereign body mainly because of:",
        "Written Constitution, federalism, judicial review, and Fundamental Rights.",
        ["pwr-sovereignty", HUB_SLUG],
    ),
    (
        2019,
        "Freedom from arrest of MPs as a privilege applies to:",
        "Civil cases during the session and 40 days before and after — not criminal cases or preventive detention.",
        ["pwr-privileges", HUB_SLUG],
    ),
    (
        2021,
        "A resolution for the removal of the Vice-President can be introduced only in:",
        "Rajya Sabha (Art. 67) — one of RS’s special powers.",
        ["pwr-rajya-sabha", "pwr-multifunctional"],
    ),
]


class Command(BaseCommand):
    help = (
        "Seed Parliament: Powers, Rajya Sabha & Privileges "
        "(Laxmikanth Ch.23 pp. 370–392) under Part III Central Government."
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
                "title": "Parliament: Powers, Rajya Sabha & Privileges",
                "sort_order": 8,
                "book_ref": (
                    "Laxmikanth 8th Ed, Ch. 23 (pp. 370–392) — "
                    "Powers, Rajya Sabha & Privileges"
                ),
                "summary": (
                    "Visual revision of Ch.23 part 3 — multifunctional role, RS position, "
                    "privileges, sovereignty, and end tables."
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
                "title": "Parliament: Powers, Rajya Sabha & Privileges",
                "summary": (
                    "What the Houses can do, how strong the second chamber is, "
                    "privileges of members, and why India is not Diceyan sovereignty."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **limits** mental model, then "
                    "**Multifunctional role** → **Ineffectiveness** → **RS position** → "
                    "**Privileges** → **Sovereignty** → **Tables**. "
                    "Prior: Structure & Procedure. Next: Parliamentary Committees. "
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
            ref="Laxmikanth Ch. 23 (pp. 370–392)",
            excerpt=(
                "Parliament — multifunctional role, RS position, privileges, "
                "sovereignty, and revision tables."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 105",
            excerpt="Powers, privileges, etc., of the Houses of Parliament and of members and committees.",
            sort_order=1,
        )

        pwr_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=pwr_slugs) | Q(target__slug__in=pwr_slugs),
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
                existing = list(pyq.concepts.all())
                pyq.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Parliament Powers & Privileges seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(SAMPLE_PYQS)} PYQs linked."
            )
        )
