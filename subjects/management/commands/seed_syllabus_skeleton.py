"""Seed UPSC Subject → Section → Chapter syllabus skeleton (no concepts).

Only subjects/chapters with real content are seeded for now. Re-run to prune
empty skeleton rows left from earlier full-syllabus seeds.
"""

from __future__ import annotations

from django.core.management.base import BaseCommand

from subjects.models import Chapter, Section, Subject

# Subject = UPSC bucket; Section = Laxmikanth-style part; Chapter = syllabus branch.
# Chapter slugs must be unique within an academy (GET /api/chapters/<slug>/ looks
# up by slug alone). Expand chapter lists as visual chapter content is authored.
SYLLABUS: list[dict] = [
    {
        "slug": "polity",
        "name": "Polity",
        "sort_order": 1,
        "description": (
            "Indian Constitution, political system, governance, and related institutions."
        ),
        "sections": [
            {
                "slug": "constitutional-framework",
                "title": "Constitutional Framework",
                "sort_order": 1,
                "summary": (
                    "Laxmikanth Part I — historical background through basic structure."
                ),
                "chapters": [
                    (
                        "historical-background",
                        "Historical Background",
                        1,
                        "Laxmikanth Ch.1 — Company Rule to Crown Rule, key Acts, and Independence.",
                    ),
                    (
                        "making-of-constitution",
                        "Making of the Constitution",
                        2,
                        "Laxmikanth Ch.2 — Constituent Assembly, Objectives Resolution, drafting, enactment, and commencement.",
                    ),
                    (
                        "concept-of-constitution",
                        "Concept of the Constitution",
                        3,
                        "Laxmikanth Ch.3 — meaning, functions, qualities, classification, and constitutionalism.",
                    ),
                    (
                        "salient-features-constitution",
                        "Salient Features of the Constitution",
                        4,
                        "Laxmikanth Ch.4 — lengthiest constitution, federalism, parliamentary system, and related features.",
                    ),
                    (
                        "preamble",
                        "Preamble of the Constitution",
                        5,
                        "Laxmikanth Ch.5 — ingredients, key words, significance, part-of status, and amendability.",
                    ),
                    (
                        "union-and-its-territory",
                        "Union and Its Territory",
                        6,
                        "Laxmikanth Ch.6 — Arts 1–4, Union of States, reorganisation, and the present map.",
                    ),
                    (
                        "citizenship",
                        "Citizenship",
                        7,
                        "Laxmikanth Ch.7 — single citizenship, Arts 5–11, Citizenship Act, Assam Accord, CAA, OCI.",
                    ),
                    (
                        "fundamental-rights",
                        "Fundamental Rights",
                        8,
                        "Justiciable rights under Part III — equality, freedom, remedies, and related themes.",
                    ),
                    (
                        "directive-principles",
                        "Directive Principles of State Policy",
                        9,
                        "Laxmikanth Ch.9 — Part IV, classification, FR–DPSP conflict, and articles at a glance.",
                    ),
                    (
                        "fundamental-duties",
                        "Fundamental Duties",
                        10,
                        "Laxmikanth Ch.10 — Part IVA, Art. 51A, eleven duties, Verma Committee, FR–DPSP–FD.",
                    ),
                    (
                        "amendment-of-constitution",
                        "Amendment of the Constitution",
                        11,
                        "Laxmikanth Ch.11 — Art. 368, three amendment paths, procedure, and criticism.",
                    ),
                    (
                        "basic-structure",
                        "Basic Structure of the Constitution",
                        12,
                        "Laxmikanth Ch.12 — emergence, Art. 368 limit, elements, and Table 12.1 case map.",
                    ),
                ],
            },
            {
                "slug": "system-of-government",
                "title": "System of Government",
                "sort_order": 2,
                "summary": "Laxmikanth Part II — parliamentary system, federalism, and emergency provisions.",
                "chapters": [
                    (
                        "parliamentary-system",
                        "Parliamentary System",
                        1,
                        "Laxmikanth Ch.13 — features, merits/demerits, why adopted, India vs Britain.",
                    ),
                    (
                        "federal-system",
                        "Federal System",
                        2,
                        "Laxmikanth Ch.14 — federal vs unitary, Union of States, 7+14 features, expert labels, Bommai.",
                    ),
                    (
                        "emergency-provisions",
                        "Emergency Provisions",
                        5,
                        "Laxmikanth Ch.17 — Part XVIII Arts 352–360; national, President’s Rule, financial; 44th & Bommai.",
                    ),
                ],
            },
            {
                "slug": "central-government",
                "title": "Central Government",
                "sort_order": 3,
                "summary": "Laxmikanth Part III — President, Parliament, PM, Council of Ministers, and Supreme Court.",
                "chapters": [
                    (
                        "president",
                        "President",
                        1,
                        "Laxmikanth Ch.18 — election, powers, vetoes, ordinances, pardon, impeachment, and constitutional position.",
                    ),
                    (
                        "vice-president",
                        "Vice-President",
                        2,
                        "Laxmikanth Ch.19 — election, qualifications, term/removal, powers, RS Chairman, India vs USA.",
                    ),
                    (
                        "prime-minister",
                        "Prime Minister",
                        3,
                        "Laxmikanth Ch.20 — appointment, powers, President/CoM relations, caretaker.",
                    ),
                    (
                        "central-council-of-ministers",
                        "Central Council of Ministers",
                        4,
                        "Laxmikanth Ch.21 — Arts 74–75/77–78/88, responsibility, CoM vs Cabinet, kitchen cabinet.",
                    ),
                    (
                        "cabinet-committees",
                        "Cabinet Committees",
                        5,
                        "Laxmikanth Ch.22 — features, standing/ad hoc, eight committees, GoMs, and 2nd ARC.",
                    ),
                    (
                        "parliament-structure-membership",
                        "Parliament: Structure & Membership",
                        6,
                        "Laxmikanth Ch.23 (pp. 326–348) — organisation, composition, elections, officers, sessions, majority.",
                    ),
                    (
                        "parliament-procedure-budget",
                        "Parliament: Procedure & Budget",
                        7,
                        "Laxmikanth Ch.23 (pp. 349–369) — devices, legislative procedure, joint sitting, budget.",
                    ),
                    (
                        "parliament-powers-privileges",
                        "Parliament: Powers, Rajya Sabha & Privileges",
                        8,
                        "Laxmikanth Ch.23 (pp. 370–392) — multifunctional role, RS position, privileges, sovereignty.",
                    ),
                    (
                        "parliamentary-committees",
                        "Parliamentary Committees",
                        9,
                        "Laxmikanth Ch.24 — meaning, standing/ad hoc, financial trio, DRSCs, consultative.",
                    ),
                    (
                        "supreme-court",
                        "Supreme Court",
                        11,
                        "Laxmikanth Ch.26 — organisation, collegium, independence, jurisdiction, India vs USA.",
                    ),
                    (
                        "judicial-activism",
                        "Judicial Activism",
                        13,
                        "Laxmikanth Ch.28 — meaning, JR vs JA, justifications, Baxi activators/fears, activism vs restraint.",
                    ),
                    (
                        "public-interest-litigation",
                        "Public Interest Litigation",
                        14,
                        "Laxmikanth Ch.29 — meaning, locus standi, scope 10/5, principles, misuse guidelines, landmarks.",
                    ),
                ],
            },
            {
                "slug": "state-government",
                "title": "State Government",
                "sort_order": 4,
                "summary": (
                    "Laxmikanth Part IV — Governor, Chief Minister, State Legislature, "
                    "High Courts, Subordinate Courts, Tribunals, Consumer Commissions, and Lok Adalats."
                ),
                "chapters": [
                    (
                        "governor",
                        "Governor",
                        1,
                        "Laxmikanth Ch.30 — dual role, powers, discretion, Sarkaria issues.",
                    ),
                    (
                        "chief-minister",
                        "Chief Minister",
                        2,
                        "Laxmikanth Ch.31 — appointment, Sarkaria, powers, Governor/CoM relations.",
                    ),
                    (
                        "state-council-of-ministers",
                        "State Council of Ministers",
                        3,
                        "Laxmikanth Ch.32 — Arts 163–164/166–167/177, responsibility to Assembly, size cap.",
                    ),
                    (
                        "state-legislature",
                        "State Legislature",
                        4,
                        "Laxmikanth Ch.33 — organisation, Assembly/Council, procedure, privileges, Arts 168–212.",
                    ),
                    (
                        "high-court",
                        "High Court",
                        5,
                        "Laxmikanth Ch.34 — organisation, appointment, independence, jurisdiction, writs, Arts 214–231.",
                    ),
                    (
                        "subordinate-courts",
                        "Subordinate Courts",
                        6,
                        "Laxmikanth Ch.35 — Part VI Arts 233–237, appointments, HC control, district judiciary hierarchy.",
                    ),
                    (
                        "tribunals",
                        "Tribunals",
                        7,
                        "Laxmikanth Ch.36 — Part XIV-A, Arts 323A/323B, CAT/SAT/JAT, Chandra Kumar.",
                    ),
                    (
                        "consumer-commissions",
                        "Consumer Commissions",
                        8,
                        "Laxmikanth Ch.37 — CPA 2019, District/State/National commissions, jurisdiction, appeals.",
                    ),
                    (
                        "lok-adalats-other-courts",
                        "Lok Adalats and Other Courts",
                        9,
                        "Laxmikanth Ch.38 — NALSA, Lok Adalats, PLA, Family/Gram/Commercial Courts, FTC.",
                    ),
                ],
            },
            {
                "slug": "local-government",
                "title": "Local Government",
                "sort_order": 5,
                "summary": "Laxmikanth Part V — Panchayati Raj and municipalities.",
                "chapters": [
                    (
                        "panchayati-raj",
                        "Panchayati Raj",
                        1,
                        "Laxmikanth Ch.39 — evolution, 73rd Amendment, Part IX, 11th Schedule, PESA.",
                    ),
                ],
            },
            {
                "slug": "union-territories-and-special-areas",
                "title": "Union Territories and Special Areas",
                "sort_order": 6,
                "summary": "Laxmikanth Part VI — UTs, scheduled areas, and tribal areas.",
                "chapters": [
                    (
                        "union-territories",
                        "Union Territories",
                        1,
                        "Laxmikanth Ch.41 — Part VIII Arts 239–241, administration, NCT Delhi, "
                        "UTs with legislature, States vs UTs.",
                    ),
                ],
            },
            {
                "slug": "constitutional-bodies",
                "title": "Constitutional Bodies",
                "sort_order": 7,
                "summary": "Laxmikanth Part VII — Election Commission, UPSC, Finance Commission, and related bodies.",
                "chapters": [
                    (
                        "constitutional-bodies",
                        "Constitutional Bodies",
                        1,
                        "Laxmikanth Ch.43–54 (pp. 599–643) — ECI, UPSC, SPSC, Finance Commission, "
                        "GST Council, NCSC/NCST/NCBC, Linguistic Minorities, CAG, AG, Advocate General.",
                    ),
                ],
            },
            {
                "slug": "non-constitutional-bodies",
                "title": "Non-Constitutional Bodies",
                "sort_order": 8,
                "summary": "Laxmikanth Part VIII — NITI Aayog, NHRC, CBI, and related institutions.",
                "chapters": [
                    (
                        "non-constitutional-bodies",
                        "Non-Constitutional Bodies",
                        1,
                        "Laxmikanth Ch.56–72 (pp. 667–760+) — NITI Aayog, rights commissions, "
                        "CIC/SIC, CVC, CBI, Lokpal, NIA, NDMA, BCI, Law Commission, "
                        "Delimitation Commission, NEC.",
                    ),
                ],
            },
            {
                "slug": "other-constitutional-dimensions",
                "title": "Other Constitutional Dimensions",
                "sort_order": 9,
                "summary": (
                    "Laxmikanth Part IX — co-operative societies, official language, "
                    "public services, and related themes."
                ),
                "chapters": [
                    (
                        "other-constitutional-dimensions",
                        "Other Constitutional Dimensions",
                        1,
                        "Laxmikanth Part IX (Ch.73–78) — co-operatives, language, services, "
                        "government liability, special classes, and special states.",
                    ),
                ],
            },
            {
                "slug": "political-dynamics",
                "title": "Political Dynamics",
                "sort_order": 10,
                "summary": "Laxmikanth Part X — parties, elections, voting behaviour, and pressure groups.",
                "chapters": [
                    (
                        "political-dynamics",
                        "Political Dynamics",
                        1,
                        "Laxmikanth Part X (Ch.79–89) — parties, elections, reforms, "
                        "coalitions, anti-defection, pressure groups, integration, foreign policy.",
                    ),
                ],
            },
            {
                "slug": "working-of-the-constitution",
                "title": "Working of the Constitution",
                "sort_order": 11,
                "summary": "Laxmikanth Part XI — how the Constitution operates in practice.",
                "chapters": [
                    (
                        "working-of-the-constitution",
                        "Working of the Constitution",
                        1,
                        "Laxmikanth Ch.90 — National Commission to Review the Working of the "
                        "Constitution (NCRWC): mandate, recommendations, and exam revision.",
                    ),
                ],
            },
            {
                "slug": "judgements-and-doctrines",
                "title": "Judgements & Doctrines",
                "sort_order": 12,
                "summary": "Laxmikanth Part XII — landmark judgements, Art.21 expansions, amendment cases, and constitutional doctrines.",
                "chapters": [
                    (
                        "judgements-and-doctrines",
                        "Judgements & Doctrines",
                        1,
                        "Laxmikanth Part XII (Ch.91–94, pp.881–949) — landmark judgements, "
                        "Art.21 case law, amendment judgements, and doctrines of interpretation.",
                    ),
                ],
            },
            {
                "slug": "comparison-of-constitutions",
                "title": "Comparison of the Constitutions",
                "sort_order": 13,
                "summary": "Laxmikanth Part XIII — world constitutions compared with India, plus sources borrowed.",
                "chapters": [
                    (
                        "world-constitutions",
                        "World Constitutions",
                        1,
                        "Laxmikanth Ch.95 (pp.949–979) — USA, Britain, France, Japan, USSR, "
                        "Russia, China, Switzerland; sources borrowed; exam comparison matrices.",
                    ),
                ],
            },
        ],
    },
    {
        "slug": "geography",
        "name": "Geography",
        "sort_order": 2,
        "description": (
            "Physical and Indian geography for UPSC — geomorphology, climatology, "
            "oceanography, physiography, resources, and industries."
        ),
        "sections": [
            {
                "slug": "physical-geography",
                "title": "Physical Geography",
                "sort_order": 1,
                "summary": "Vision IAS CCAB-2 — geomorphology, climatology, and oceanography.",
                "chapters": [
                    (
                        "geomorphology",
                        "Geomorphology",
                        1,
                        "Vision IAS CCAB-2 Ch.1 — Earth's origin/interior, seismic waves, "
                        "plate tectonics, folds/faults, earthquakes, volcanoes, exogenic "
                        "forces, rocks, and soils.",
                    ),
                ],
            },
        ],
    },
]

CONTENT_OWNED_CHAPTERS = {
    "historical-background",
    "making-of-constitution",
    "concept-of-constitution",
    "fundamental-rights",
    "directive-principles",
    "salient-features-constitution",
    "citizenship",
    "preamble",
    "union-and-its-territory",
    "fundamental-duties",
    "amendment-of-constitution",
    "basic-structure",
    "parliamentary-system",
    "federal-system",
    "emergency-provisions",
    "president",
    "vice-president",
    "prime-minister",
    "central-council-of-ministers",
    "cabinet-committees",
    "parliament-structure-membership",
    "parliament-procedure-budget",
    "parliament-powers-privileges",
    "parliamentary-committees",
    "supreme-court",
    "judicial-activism",
    "public-interest-litigation",
    "governor",
    "chief-minister",
    "state-council-of-ministers",
    "state-legislature",
    "high-court",
    "subordinate-courts",
    "tribunals",
    "consumer-commissions",
    "lok-adalats-other-courts",
    "panchayati-raj",
    "union-territories",
    "constitutional-bodies",
    "non-constitutional-bodies",
    "other-constitutional-dimensions",
    "political-dynamics",
    "working-of-the-constitution",
    "judgements-and-doctrines",
    "world-constitutions",
    "geomorphology",
}


class Command(BaseCommand):
    help = (
        "Seed subjects, Laxmikanth-style sections, and chapters that have content "
        "(Polity Part I–III authored chapters including Prime Minister). "
        "Later parts are empty placeholders. Prunes empty extras."
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
        subjects_n = 0
        sections_n = 0
        chapters_n = 0

        keep_subject_slugs = {entry["slug"] for entry in SYLLABUS}
        keep_section_slugs_by_subject = {
            entry["slug"]: {s["slug"] for s in entry["sections"]} for entry in SYLLABUS
        }
        keep_chapter_slugs_by_subject = {
            entry["slug"]: {
                c[0] for s in entry["sections"] for c in s["chapters"]
            }
            for entry in SYLLABUS
        }

        for entry in SYLLABUS:
            subject, _ = Subject.objects.update_or_create(
                academy=academy,
                slug=entry["slug"],
                defaults={
                    "name": entry["name"],
                    "description": entry["description"],
                    "sort_order": entry["sort_order"],
                    "is_active": True,
                },
            )
            subjects_n += 1

            for section_entry in entry["sections"]:
                section, _ = Section.objects.update_or_create(
                    subject=subject,
                    slug=section_entry["slug"],
                    defaults={
                        "title": section_entry["title"],
                        "sort_order": section_entry["sort_order"],
                        "summary": section_entry.get("summary", ""),
                        "is_published": True,
                    },
                )
                sections_n += 1

                for slug, title, sort_order, summary in section_entry["chapters"]:
                    existing = Chapter.objects.filter(
                        subject=subject, slug=slug
                    ).first()
                    # Content seeds own visual-chapter metadata (Laxmikanth book_ref).
                    if (
                        slug in CONTENT_OWNED_CHAPTERS
                        and existing is not None
                        and existing.book_ref
                    ):
                        Chapter.objects.filter(pk=existing.pk).update(
                            sort_order=sort_order,
                            section=section,
                            is_published=True,
                        )
                        chapters_n += 1
                        continue

                    defaults = {
                        "title": title,
                        "sort_order": sort_order,
                        "summary": summary,
                        "section": section,
                        "is_published": True,
                    }
                    if slug not in CONTENT_OWNED_CHAPTERS:
                        defaults["book_ref"] = ""

                    Chapter.objects.update_or_create(
                        subject=subject,
                        slug=slug,
                        defaults=defaults,
                    )
                    chapters_n += 1

            # Hide sections that are no longer in the seed.
            pruned_sections = (
                Section.objects.filter(subject=subject)
                .exclude(slug__in=keep_section_slugs_by_subject[entry["slug"]])
                .update(is_published=False)
            )
            if pruned_sections:
                self.stdout.write(
                    f"Unpublished {pruned_sections} extra section(s) under {subject.slug}."
                )

            # Hide Polity chapters that are no longer in the seed.
            pruned_chapters = (
                Chapter.objects.filter(subject=subject)
                .exclude(slug__in=keep_chapter_slugs_by_subject[entry["slug"]])
                .update(is_published=False)
            )
            if pruned_chapters:
                self.stdout.write(
                    f"Unpublished {pruned_chapters} extra chapter(s) under {subject.slug}."
                )

        # Hide subjects with no authored content yet.
        extra_subjects = Subject.objects.filter(academy=academy).exclude(
            slug__in=keep_subject_slugs
        )
        pruned_subjects = extra_subjects.filter(is_active=True).update(is_active=False)
        pruned_extra_chapters = Chapter.objects.filter(
            subject__in=extra_subjects
        ).update(is_published=False)
        pruned_extra_sections = Section.objects.filter(
            subject__in=extra_subjects
        ).update(is_published=False)
        if pruned_subjects or pruned_extra_chapters or pruned_extra_sections:
            self.stdout.write(
                f"Deactivated {pruned_subjects} subject(s); "
                f"unpublished {pruned_extra_sections} section(s) and "
                f"{pruned_extra_chapters} chapter(s) without content yet."
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded syllabus skeleton ({academy.slug}): "
                f"{subjects_n} subjects, {sections_n} sections, {chapters_n} chapters."
            )
        )
