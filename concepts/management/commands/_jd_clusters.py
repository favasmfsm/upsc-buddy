"""Cluster list builder for Judgements & Doctrines (imported by seed command)."""

from concepts.management.commands._jd_bodies_a import (
    AMEND_STRUCK_BODY,
    AMEND_TRIGGERED_BODY,
    ART21_BODY,
    COMPACT_EARLY_BODY,
    COMPACT_LATER_BODY,
    RECENT_EXTRAS_BODY,
)
from concepts.management.commands._jd_bodies_b import (
    DOC_ECLIPSE,
    DOC_EXTRAS_BODY,
    DOC_FEDERAL_BODY,
    DOC_INTERP_BODY,
    DOC_SEVERABILITY,
    DOC_WAIVER,
    MASTER_BODY,
)


def callout(cid, title, body, tone="tip"):
    return {"id": cid, "type": "callout", "title": title, "tone": tone, "body": body}


def build_clusters(flagships):
    clusters = []
    for f in flagships:
        clusters.append(
            {
                "slug": f["slug"],
                "title": f["title"],
                "summary": f["summary"],
                "sort_order": f["sort_order"],
                "body": f["body"],
                "visual_blocks": f["visual_blocks"],
                "articles": f["articles"],
            }
        )

    n = 19
    extra = [
        {
            "slug": "jd-compact-early",
            "title": "Compact Landmarks (1950s–1980s)",
            "summary": "One-line bank of remaining early Ch.91 cases.",
            "sort_order": n,
            "body": COMPACT_EARLY_BODY,
            "articles": [("Ch.91", "Early landmarks")],
            "visual_blocks": [
                callout(
                    "jd-compact-early-tip",
                    "Prelims tip",
                    "Romesh Thappar → 1st Amdt · Berubari → 9th · Waman Rao → 24 Apr 1973 cut-off.",
                    "tip",
                )
            ],
        },
        {
            "slug": "jd-compact-later",
            "title": "Compact Landmarks (1990s–2020)",
            "summary": "One-line bank of later Ch.91 cases.",
            "sort_order": n + 1,
            "body": COMPACT_LATER_BODY,
            "articles": [("Ch.91", "Later landmarks")],
            "visual_blocks": [
                callout(
                    "jd-compact-later-tip",
                    "Prelims tip",
                    "Shreya Singhal (66A) · Anuradha Bhasin (internet) · ADR/PUCL (transparency/NOTA).",
                    "tip",
                )
            ],
        },
        {
            "slug": "jd-recent-extras",
            "title": "UPSC Extras — Sabarimala, Aadhaar, Electoral Bonds",
            "summary": "High-yield extras beyond full Ch.91 write-ups.",
            "sort_order": n + 2,
            "body": RECENT_EXTRAS_BODY,
            "articles": [("Art. 25", "Sabarimala"), ("Art. 21", "Aadhaar/privacy")],
            "visual_blocks": [
                callout(
                    "jd-extras-note",
                    "Scope note",
                    "Compact exam cards — current-affairs grade additions to Part XII spine.",
                    "note",
                )
            ],
        },
        {
            "slug": "jd-network-bs",
            "title": "Case Network — Basic Structure Arc",
            "summary": "Shankari → Golaknath → Kesavananda → Indira → Minerva → Coelho.",
            "sort_order": n + 3,
            "body": (
                "## Basic structure case network\n\n"
                "Trace **S-G-K-I-M-C** (+ Waman Rao for date). "
                "Open linked flagship cards for full 13-field revision.\n"
            ),
            "articles": [("Art. 368", "Basic structure arc")],
            "visual_blocks": [
                {
                    "id": "jd-cn-bs",
                    "type": "case_network",
                    "title": "Basic structure spine",
                    "hub_label": "Art. 368 limit",
                    "cases": [
                        {
                            "id": "sp",
                            "label": "Shankari Prasad",
                            "year": 1951,
                            "detail": "Can amend FRs",
                            "case_slug": "shankari-prasad",
                        },
                        {
                            "id": "gn",
                            "label": "Golaknath",
                            "year": 1967,
                            "detail": "Cannot amend FRs",
                            "case_slug": "golak-nath",
                        },
                        {
                            "id": "kb",
                            "label": "Kesavananda",
                            "year": 1973,
                            "detail": "Basic structure",
                            "case_slug": "kesavananda-bharati",
                        },
                        {
                            "id": "ig",
                            "label": "Indira Gandhi",
                            "year": 1975,
                            "detail": "BS applied",
                            "case_slug": "indira-nehru-gandhi",
                        },
                        {
                            "id": "mm",
                            "label": "Minerva Mills",
                            "year": 1980,
                            "detail": "Limited power basic",
                            "case_slug": "minerva-mills",
                        },
                        {
                            "id": "ic",
                            "label": "I.R. Coelho",
                            "year": 2007,
                            "detail": "9th Schedule review",
                            "case_slug": "ir-coelho",
                        },
                    ],
                },
                callout(
                    "jd-cn-bs-tip",
                    "Mnemonic",
                    "**S-G-K-I-M-C** — Shankari, Golaknath, Kesavananda, Indira, Minerva, Coelho.",
                    "tip",
                ),
            ],
        },
        {
            "slug": "jd-network-art21",
            "title": "Case Network — Article 21 Arc",
            "summary": "Gopalan → Jabalpur → Maneka → Puttaswamy.",
            "sort_order": n + 4,
            "body": (
                "## Article 21 case network\n\n"
                "**GJM + P** — narrow liberty → Emergency nadir → expansive due-process-like reading → privacy.\n"
            ),
            "articles": [("Art. 21", "Life and personal liberty")],
            "visual_blocks": [
                {
                    "id": "jd-cn-21",
                    "type": "case_network",
                    "title": "Art. 21 spine",
                    "hub_label": "Article 21",
                    "cases": [
                        {
                            "id": "akg",
                            "label": "A.K. Gopalan",
                            "year": 1950,
                            "detail": "Narrow reading",
                            "case_slug": "ak-gopalan",
                        },
                        {
                            "id": "adm",
                            "label": "A.D.M. Jabalpur",
                            "year": 1976,
                            "detail": "Emergency low point",
                            "case_slug": "adm-jabalpur",
                        },
                        {
                            "id": "mg",
                            "label": "Maneka Gandhi",
                            "year": 1978,
                            "detail": "Just-fair-reasonable",
                            "case_slug": "maneka-gandhi",
                        },
                        {
                            "id": "kp",
                            "label": "Puttaswamy",
                            "year": 2017,
                            "detail": "Privacy FR",
                            "case_slug": "puttaswamy",
                        },
                    ],
                }
            ],
        },
        {
            "slug": "jd-article-21-expansions",
            "title": "Part B — Article 21 Expansions",
            "summary": "Ch.92 table — rights read into life and personal liberty.",
            "sort_order": n + 5,
            "body": ART21_BODY,
            "articles": [("Art. 21", "Expanded rights")],
            "visual_blocks": [
                {
                    "id": "jd-a21-pillars",
                    "type": "pillars",
                    "title": "Priority Art.21 rights",
                    "items": [
                        {
                            "id": "priv",
                            "articles": "2017",
                            "label": "Privacy",
                            "slug": "jd-puttaswamy",
                            "detail": "Puttaswamy — FR confirmed.",
                            "tone": "teal",
                        },
                        {
                            "id": "edu",
                            "articles": "86th",
                            "label": "Education",
                            "slug": "jd-compact-later",
                            "detail": "Unni Krishnan → Art.21A.",
                            "tone": "olive",
                        },
                        {
                            "id": "live",
                            "articles": "1985",
                            "label": "Livelihood",
                            "detail": "Olga Tellis — not absolute.",
                            "tone": "gold",
                        },
                        {
                            "id": "env",
                            "articles": "PIL",
                            "label": "Environment",
                            "detail": "RLEK / M.C. Mehta line.",
                            "tone": "orange",
                        },
                        {
                            "id": "dig",
                            "articles": "1981",
                            "label": "Dignity",
                            "detail": "Francis Coralie core.",
                            "tone": "terracotta",
                        },
                        {
                            "id": "aid",
                            "articles": "1978–79",
                            "label": "Legal aid / Speedy trial",
                            "detail": "Hoskot · Hussainara.",
                            "tone": "maroon",
                        },
                    ],
                },
                callout(
                    "jd-a21-trap",
                    "Trap",
                    "Most Art.21 rights are **judge-made** unless codified (education → 21A).",
                    "trap",
                ),
            ],
        },
        {
            "slug": "jd-amendments-struck",
            "title": "Part C — Amendments Struck Down",
            "summary": "Table 93.1 — amendments declared unconstitutional.",
            "sort_order": n + 6,
            "body": AMEND_STRUCK_BODY,
            "articles": [("Art. 368", "Limits on amending power")],
            "visual_blocks": [
                {
                    "id": "jd-amd-struck-tl",
                    "type": "timeline",
                    "title": "Amendments struck — timeline",
                    "events": [
                        {
                            "id": "e1",
                            "year": 1967,
                            "label": "Golaknath",
                            "detail": "17th in part",
                        },
                        {
                            "id": "e2",
                            "year": 1973,
                            "label": "Kesavananda",
                            "detail": "Art.31C in part",
                        },
                        {
                            "id": "e3",
                            "year": 1975,
                            "label": "Indira Gandhi",
                            "detail": "39th / 329A(4)",
                        },
                        {
                            "id": "e4",
                            "year": 1980,
                            "label": "Minerva Mills",
                            "detail": "42nd clauses",
                        },
                        {
                            "id": "e5",
                            "year": 2015,
                            "label": "NJAC",
                            "detail": "99th total",
                        },
                        {
                            "id": "e6",
                            "year": 2021,
                            "label": "Rajendra N Shah",
                            "detail": "97th in part",
                        },
                    ],
                },
                callout(
                    "jd-amd-struck-tip",
                    "Theme",
                    "Parliament vs Judiciary · Basic Structure · Limits of Art.368 · Evolution of JR.",
                    "tip",
                ),
            ],
        },
        {
            "slug": "jd-amendments-triggered",
            "title": "Part C — Amendments Triggered by Cases",
            "summary": "Table 93.2 — judgements that led to constitutional amendments.",
            "sort_order": n + 7,
            "body": AMEND_TRIGGERED_BODY,
            "articles": [("Art. 368", "Political response to judgements")],
            "visual_blocks": [
                callout(
                    "jd-amd-trig-tip",
                    "Pattern",
                    "Court restricts → Parliament amends. Classic: Champakam→15(4), Golaknath→24th, Unni Krishnan→86th.",
                    "tip",
                )
            ],
        },
        {
            "slug": "jd-doctrines-map",
            "title": "Part D — Doctrines Map",
            "summary": "Ch.94 doctrines + UPSC extras at a glance.",
            "sort_order": n + 8,
            "body": (
                "## Doctrines map\n\n"
                "Open clusters below for definition · basis · origin · cases · principles · exceptions · UPSC use.\n\n"
                "**Book spine:** Severability · Waiver · Eclipse · Territorial Nexus · Pith & Substance · "
                "Colourable Legislation · Implied / Incidental Powers · Precedent · Occupied Field · "
                "Prospective Overruling · Harmonious Construction · Liberal Interpretation.\n\n"
                "**Extras:** Basic Structure · Judicial Review · Reading Down · Proportionality · "
                "Public Trust · Legitimate Expectation · Pleasure · Lapse.\n"
            ),
            "articles": [("Ch.94", "Constitutional doctrines")],
            "visual_blocks": [
                {
                    "id": "jd-doc-pillars",
                    "type": "pillars",
                    "title": "Doctrine groups",
                    "items": [
                        {
                            "id": "frtools",
                            "articles": "Art.13",
                            "label": "FR tools",
                            "slug": "jd-doc-fr-tools",
                            "detail": "Severability · Waiver · Eclipse",
                            "tone": "teal",
                        },
                        {
                            "id": "fed",
                            "articles": "Lists",
                            "label": "Federal competence",
                            "slug": "jd-doc-federal",
                            "detail": "Pith · Colour · Occupied · Nexus · Incidental",
                            "tone": "olive",
                        },
                        {
                            "id": "interp",
                            "articles": "Art.141",
                            "label": "Interpretation",
                            "slug": "jd-doc-interpretation",
                            "detail": "Harmonious · Liberal · Prospective · Precedent",
                            "tone": "gold",
                        },
                        {
                            "id": "extra",
                            "articles": "UPSC",
                            "label": "Extra toolkit",
                            "slug": "jd-doc-extras",
                            "detail": "BS · JR · Proportionality · Public Trust…",
                            "tone": "orange",
                        },
                    ],
                }
            ],
        },
        {
            "slug": "jd-doc-fr-tools",
            "title": "Doctrines — Severability, Waiver, Eclipse",
            "summary": "Art.13 toolkit for unconstitutional laws.",
            "sort_order": n + 9,
            "body": (
                "## Severability\n\n"
                + DOC_SEVERABILITY
                + "\n## Waiver\n\n"
                + DOC_WAIVER
                + "\n## Eclipse\n\n"
                + DOC_ECLIPSE
            ),
            "articles": [("Art. 13", "FR and laws")],
            "visual_blocks": [
                {
                    "id": "jd-eclipse-vs-sev",
                    "type": "comparison",
                    "title": "Eclipse vs Severability",
                    "columns": [
                        {
                            "id": "ecl",
                            "heading": "Eclipse",
                            "points": [
                                "Mostly pre-Constitution laws",
                                "Law sleeps while inconsistent",
                                "Can revive if inconsistency removed",
                            ],
                        },
                        {
                            "id": "sev",
                            "heading": "Severability",
                            "points": [
                                "Valid part can be saved",
                                "Invalid part cut out",
                                "Works on pre- and post-Constitution laws",
                            ],
                        },
                    ],
                },
                callout(
                    "jd-waiver-trap",
                    "Trap",
                    "Doctrine of **waiver does not apply to Fundamental Rights** in India.",
                    "trap",
                ),
            ],
        },
        {
            "slug": "jd-doc-federal",
            "title": "Doctrines — Federal & Legislative Competence",
            "summary": "Pith & substance, colourable, occupied field, nexus, incidental powers.",
            "sort_order": n + 10,
            "body": DOC_FEDERAL_BODY,
            "articles": [("Arts. 245–254", "Federal distribution")],
            "visual_blocks": [
                {
                    "id": "jd-fed-flow",
                    "type": "flowchart",
                    "title": "Which federal doctrine?",
                    "root": "start",
                    "steps": [
                        {
                            "id": "start",
                            "label": "List conflict?",
                            "detail": "Pick the tool",
                            "options": [
                                {"label": "Wrong list packaging?", "next": "colour"},
                                {"label": "Incidental trench on other list?", "next": "pith"},
                                {"label": "Concurrent clash?", "next": "occupied"},
                                {"label": "State law hits outsiders?", "next": "nexus"},
                            ],
                        },
                        {
                            "id": "colour",
                            "label": "Colourable legislation",
                            "detail": "Indirect trespass on competence.",
                        },
                        {
                            "id": "pith",
                            "label": "Pith and substance",
                            "detail": "True nature decides validity.",
                        },
                        {
                            "id": "occupied",
                            "label": "Occupied field / Art.254",
                            "detail": "Union exhaustive law may prevail.",
                        },
                        {
                            "id": "nexus",
                            "label": "Territorial nexus",
                            "detail": "Real link to State needed.",
                        },
                    ],
                },
                callout(
                    "jd-fed-mn",
                    "Mnemonic",
                    "**Pith – Colour – Occupied – Nexus** (+ Incidental).",
                    "tip",
                ),
            ],
        },
        {
            "slug": "jd-doc-interpretation",
            "title": "Doctrines — Interpretation Toolkit",
            "summary": "Harmonious construction, liberal interpretation, prospective overruling, precedent.",
            "sort_order": n + 11,
            "body": DOC_INTERP_BODY,
            "articles": [("Art. 141", "Precedent"), ("Art. 368", "Basic structure creativity")],
            "visual_blocks": [
                callout(
                    "jd-prospective-tip",
                    "Associate",
                    "**Prospective overruling** ↔ **Golaknath (1967)** first famous use.",
                    "tip",
                )
            ],
        },
        {
            "slug": "jd-doc-extras",
            "title": "Doctrines — UPSC Extras",
            "summary": "Basic structure, JR, reading down, proportionality, public trust, and more.",
            "sort_order": n + 12,
            "body": DOC_EXTRAS_BODY,
            "articles": [("Art. 368", "Basic structure"), ("Art. 13", "Judicial review")],
            "visual_blocks": [
                callout(
                    "jd-extras-link",
                    "Deep dive",
                    "For basic structure elements table, open the dedicated Basic Structure chapter.",
                    "note",
                )
            ],
        },
        {
            "slug": "jd-cmp-golaknath-kesavananda",
            "title": "Compare — Golaknath vs Kesavananda",
            "summary": "FR amendability flip and birth of basic structure.",
            "sort_order": n + 13,
            "body": "Side-by-side revision of the two hinge judgements on amending power.\n",
            "articles": [("Art. 368", "Amending power")],
            "visual_blocks": [
                {
                    "id": "jd-cmp-gk",
                    "type": "comparison",
                    "title": "Golaknath vs Kesavananda",
                    "columns": [
                        {
                            "id": "g",
                            "heading": "Golaknath (1967)",
                            "points": [
                                "Cannot amend FRs",
                                "Amendment = law under Art.13",
                                "Prospective overruling",
                                "Provoked 24th Amendment",
                            ],
                        },
                        {
                            "id": "k",
                            "heading": "Kesavananda (1973)",
                            "points": [
                                "Can amend FRs",
                                "Cannot alter basic structure",
                                "Golaknath overruled on FR point",
                                "Still controlling limit",
                            ],
                        },
                    ],
                }
            ],
        },
        {
            "slug": "jd-cmp-kesavananda-minerva",
            "title": "Compare — Kesavananda vs Minerva Mills",
            "summary": "Birth vs fortification of basic structure.",
            "sort_order": n + 14,
            "body": "Kesavananda invents the limit; Minerva stops Parliament from deleting it.\n",
            "articles": [("Art. 368", "Basic structure")],
            "visual_blocks": [
                {
                    "id": "jd-cmp-km",
                    "type": "comparison",
                    "title": "Kesavananda vs Minerva",
                    "columns": [
                        {
                            "id": "k",
                            "heading": "Kesavananda",
                            "points": [
                                "Creates basic structure",
                                "24th upheld; 25th partly limited",
                                "Identity of Constitution",
                            ],
                        },
                        {
                            "id": "m",
                            "heading": "Minerva Mills",
                            "points": [
                                "Limited amending power is itself basic",
                                "Strikes 42nd Art.368(4)&(5)",
                                "FR–DPSP harmony basic",
                            ],
                        },
                    ],
                }
            ],
        },
        {
            "slug": "jd-cmp-gopalan-maneka",
            "title": "Compare — Gopalan vs Maneka (Art.21)",
            "summary": "Article 21 before and after Maneka Gandhi.",
            "sort_order": n + 15,
            "body": "The single most important Art.21 contrast in Indian constitutional law.\n",
            "articles": [("Art. 21", "Personal liberty")],
            "visual_blocks": [
                {
                    "id": "jd-cmp-gm",
                    "type": "comparison",
                    "title": "Art.21 before vs after Maneka",
                    "columns": [
                        {
                            "id": "before",
                            "heading": "Before (Gopalan)",
                            "points": [
                                "Procedure established by law = any law",
                                "FR silos (19/21/22 separate)",
                                "Protects mainly vs executive",
                            ],
                        },
                        {
                            "id": "after",
                            "heading": "After (Maneka)",
                            "points": [
                                "Procedure must be just, fair, reasonable",
                                "Golden triangle 14–19–21",
                                "Opens expansive Art.21 rights",
                            ],
                        },
                    ],
                },
                {
                    "id": "jd-gm-flow",
                    "type": "flowchart",
                    "title": "Art.21 evolution path",
                    "root": "g",
                    "steps": [
                        {
                            "id": "g",
                            "label": "Gopalan 1950",
                            "detail": "Narrow",
                            "options": [{"label": "Emergency nadir", "next": "j"}],
                        },
                        {
                            "id": "j",
                            "label": "Jabalpur 1976",
                            "detail": "Habeas denied",
                            "options": [{"label": "Course correction", "next": "m"}],
                        },
                        {
                            "id": "m",
                            "label": "Maneka 1978",
                            "detail": "Expansive Art.21",
                            "options": [{"label": "Privacy era", "next": "p"}],
                        },
                        {
                            "id": "p",
                            "label": "Puttaswamy 2017",
                            "detail": "Privacy FR",
                        },
                    ],
                },
            ],
        },
        {
            "slug": "jd-cmp-njac-collegium",
            "title": "Compare — NJAC vs Collegium",
            "summary": "Appointment models and the 2015 basic structure holding.",
            "sort_order": n + 16,
            "body": "Second/Third Judges created collegium; 99th tried NJAC; Fourth Judges restored collegium.\n",
            "articles": [("Art. 124", "Appointments")],
            "visual_blocks": [
                {
                    "id": "jd-cmp-njac",
                    "type": "comparison",
                    "title": "Collegium vs NJAC",
                    "columns": [
                        {
                            "id": "col",
                            "heading": "Collegium",
                            "points": [
                                "Judicial primacy",
                                "Second/Third Judges",
                                "Operative after 2015",
                            ],
                        },
                        {
                            "id": "njac",
                            "heading": "NJAC",
                            "points": [
                                "99th Amendment + Act",
                                "Executive/other members",
                                "Struck — independence basic",
                            ],
                        },
                    ],
                }
            ],
        },
        {
            "slug": "jd-cmp-review-activism",
            "title": "Compare — Judicial Review vs Judicial Activism",
            "summary": "Power to invalidate vs proactive rights expansion.",
            "sort_order": n + 17,
            "body": "Review is the constitutional power; activism is the style/intensity of using it (esp. PIL/Art.21).\n",
            "articles": [("Art. 13", "Judicial review"), ("Art. 32", "PIL/activism")],
            "visual_blocks": [
                {
                    "id": "jd-cmp-jr",
                    "type": "comparison",
                    "title": "Review vs Activism",
                    "columns": [
                        {
                            "id": "jr",
                            "heading": "Judicial Review",
                            "points": [
                                "Test legality/constitutionality",
                                "Basic feature",
                                "Amendments + statutes + actions",
                            ],
                        },
                        {
                            "id": "ja",
                            "heading": "Judicial Activism",
                            "points": [
                                "Creative/expansive use of power",
                                "PIL, guidelines (Vishaka)",
                                "Debated vs restraint",
                            ],
                        },
                    ],
                }
            ],
        },
        {
            "slug": "jd-timeline-amendment-cases",
            "title": "Timeline — Amendment Cases",
            "summary": "Chronology of amendment battles.",
            "sort_order": n + 18,
            "body": "Use with Part C tables for Prelims chronology questions.\n",
            "articles": [("Art. 368", "Amendment chronology")],
            "visual_blocks": [
                {
                    "id": "jd-tl-amd",
                    "type": "timeline",
                    "title": "Amendment case chronology",
                    "events": [
                        {"id": "a1", "year": 1951, "label": "Shankari", "detail": "FR amendable"},
                        {"id": "a2", "year": 1967, "label": "Golaknath", "detail": "FR locked"},
                        {"id": "a3", "year": 1971, "label": "24th Amdt", "detail": "Political response"},
                        {"id": "a4", "year": 1973, "label": "Kesavananda", "detail": "Basic structure"},
                        {"id": "a5", "year": 1975, "label": "Indira", "detail": "39th struck in part"},
                        {"id": "a6", "year": 1976, "label": "42nd", "detail": "Mini-Constitution"},
                        {"id": "a7", "year": 1980, "label": "Minerva", "detail": "42nd checked"},
                        {"id": "a8", "year": 2007, "label": "Coelho", "detail": "9th Schedule"},
                        {"id": "a9", "year": 2015, "label": "NJAC", "detail": "99th void"},
                    ],
                }
            ],
        },
        {
            "slug": "jd-timeline-fr-evolution",
            "title": "Timeline — FR Evolution through Case Law",
            "summary": "How Fundamental Rights grew via judgements.",
            "sort_order": n + 19,
            "body": "From textual silos to dignity, privacy, and transformative equality.\n",
            "articles": [("Part III", "FR evolution")],
            "visual_blocks": [
                {
                    "id": "jd-tl-fr",
                    "type": "timeline",
                    "title": "FR through case law",
                    "events": [
                        {"id": "f1", "year": 1950, "label": "Gopalan", "detail": "Narrow liberty"},
                        {"id": "f2", "year": 1951, "label": "Champakam", "detail": "FR > DPSP"},
                        {"id": "f3", "year": 1973, "label": "Kesavananda", "detail": "FR amendable but BS"},
                        {"id": "f4", "year": 1978, "label": "Maneka", "detail": "Expansive Art.21"},
                        {"id": "f5", "year": 1992, "label": "Indra Sawhney", "detail": "Reservation grammar"},
                        {"id": "f6", "year": 2017, "label": "Puttaswamy", "detail": "Privacy FR"},
                        {"id": "f7", "year": 2018, "label": "Navtej", "detail": "Dignity/equality"},
                    ],
                }
            ],
        },
        {
            "slug": "jd-doctrine-cheatsheet",
            "title": "Doctrine Cheat Sheet",
            "summary": "One-screen doctrine grid for last-minute revision.",
            "sort_order": n + 20,
            "body": (
                "| Doctrine | One-liner |\n"
                "|----------|----------|\n"
                "| Severability | Cut invalid part; save rest if separable |\n"
                "| Eclipse | Pre-Constitution law sleeps; can revive |\n"
                "| Waiver | Not for FRs in India |\n"
                "| Pith & Substance | True nature of law |\n"
                "| Colourable | Cannot do indirectly |\n"
                "| Occupied Field | Exhaustive Union law on Concurrent field |\n"
                "| Territorial Nexus | Real link for State extraterritoriality |\n"
                "| Harmonious Construction | Make provisions coexist |\n"
                "| Prospective Overruling | New rule for future (Golaknath) |\n"
                "| Basic Structure | Art.368 limit |\n"
                "| Reading Down | Save statute by narrowing |\n"
                "| Proportionality | Aim–nexus–necessity–balance |\n"
            ),
            "articles": [("Ch.94", "Doctrines")],
            "visual_blocks": [
                callout(
                    "jd-cheat-mn",
                    "Memory",
                    "FR tools: **Eclipse – Severability – (No) Waiver**. Federal: **Pith – Colour – Occupied – Nexus**.",
                    "tip",
                )
            ],
        },
        {
            "slug": "jd-confused-judgements",
            "title": "Frequently Confused Judgements",
            "summary": "Pairs students mix up in Prelims/Mains.",
            "sort_order": n + 21,
            "body": (
                "| Confused pair | Difference |\n"
                "|---------------|------------|\n"
                "| Shah Bano vs Shayara Bano | Maintenance (1985) vs Triple talaq (2017) |\n"
                "| Golaknath vs Kesavananda | FR locked vs FR amendable + basic structure |\n"
                "| Gopalan vs Maneka | Narrow vs expansive Art.21 |\n"
                "| Second Judges vs Fourth Judges | Collegium created vs NJAC struck |\n"
                "| Waman Rao vs Coelho | Cut-off date vs 9th Schedule review test |\n"
                "| Eclipse vs Severability | Sleep/revive vs cut-and-save |\n"
                "| Judicial review vs activism | Power vs style of using power |\n"
            ),
            "articles": [("Revision", "Confusion killers")],
            "visual_blocks": [
                callout(
                    "jd-confused-trap",
                    "Trap",
                    "Name similarity is intentional bait — always lock **year + holding**.",
                    "trap",
                )
            ],
        },
        {
            "slug": "jd-which-case-what",
            "title": "Which Case Established What?",
            "summary": "Cheat sheet mapping holding → case.",
            "sort_order": n + 22,
            "body": (
                "| Established / Holding | Case |\n"
                "|----------------------|------|\n"
                "| Basic structure doctrine | Kesavananda Bharati (1973) |\n"
                "| Just-fair-reasonable Art.21 | Maneka Gandhi (1978) |\n"
                "| Privacy as FR | Puttaswamy (2017) |\n"
                "| Art.356 justiciable | S.R. Bommai (1994) |\n"
                "| Collegium | Second Judges (1993) |\n"
                "| NJAC unconstitutional | Fourth Judges (2015) |\n"
                "| 9th Schedule reviewable post-1973 | I.R. Coelho (2007) |\n"
                "| Creamy layer / 50% | Indra Sawhney (1992) |\n"
                "| Sexual harassment guidelines | Vishaka (1997) |\n"
                "| s.66A void | Shreya Singhal (2015) |\n"
                "| Prospective overruling (famous) | Golaknath (1967) |\n"
                "| FR > DPSP (early) | Champakam (1951) |\n"
                "| Limited amending power basic | Minerva Mills (1980) |\n"
            ),
            "articles": [("Revision", "Holding → case")],
            "visual_blocks": [
                callout(
                    "jd-which-tip",
                    "Drill",
                    "Cover the right column and recall the case — reverse drill for Prelims speed.",
                    "tip",
                )
            ],
        },
        {
            "slug": "jd-master-revision",
            "title": "Master Revision — One-Page Summary",
            "summary": "Final sheet: tables, mnemonics, PYQ themes, Exam-in-5.",
            "sort_order": n + 23,
            "body": MASTER_BODY,
            "articles": [("Part XII", "Master revision")],
            "visual_blocks": [
                {
                    "id": "jd-master-pillars",
                    "type": "pillars",
                    "title": "Last-day stack",
                    "items": [
                        {
                            "id": "m1",
                            "articles": "Arc",
                            "label": "S-G-K-I-M-C",
                            "slug": "jd-network-bs",
                            "detail": "Amendment / BS arc",
                            "tone": "teal",
                        },
                        {
                            "id": "m2",
                            "articles": "Art.21",
                            "label": "GJM + Privacy",
                            "slug": "jd-network-art21",
                            "detail": "Liberty evolution",
                            "tone": "olive",
                        },
                        {
                            "id": "m3",
                            "articles": "Federal",
                            "label": "Bommai",
                            "slug": "jd-sr-bommai",
                            "detail": "356 + secularism",
                            "tone": "gold",
                        },
                        {
                            "id": "m4",
                            "articles": "Doctrines",
                            "label": "Cheat sheet",
                            "slug": "jd-doctrine-cheatsheet",
                            "detail": "One-liners",
                            "tone": "orange",
                        },
                    ],
                },
                callout(
                    "jd-master-exam5",
                    "Exam in 5 minutes",
                    "Kesavananda · Maneka · Bommai · Puttaswamy · Coelho · Eclipse≠Severability · NJAC void.",
                    "tip",
                ),
            ],
        },
    ]
    clusters.extend(extra)
    return clusters


def build_edges(cluster_slugs):
    edges = [( "judgements-and-doctrines", "parent", s) for s in cluster_slugs]
    related = [
        ("judgements-and-doctrines", "related", "basic-structure"),
        ("judgements-and-doctrines", "related", "fundamental-rights"),
        ("judgements-and-doctrines", "related", "amendment-of-constitution"),
        ("judgements-and-doctrines", "related", "supreme-court"),
        ("judgements-and-doctrines", "related", "judicial-activism"),
        ("judgements-and-doctrines", "related", "emergency-provisions"),
        ("jd-kesavananda", "related", "basic-structure"),
        ("jd-maneka-gandhi", "related", "fundamental-rights"),
        ("jd-sr-bommai", "related", "emergency-provisions"),
        ("jd-njac", "related", "supreme-court"),
        ("jd-puttaswamy", "related", "fundamental-rights"),
        ("jd-doc-extras", "related", "basic-structure"),
    ]
    edges.extend(related)
    return edges
