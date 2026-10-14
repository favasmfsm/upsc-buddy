"""Seed Geography → Geomorphology visual-revision chapter (Vision IAS CCAB-2 Ch.1).

Mirrors the Polity seed pattern: one hub concept plus topic clusters, each with
`visual_blocks` mixing existing grammars and the new image / annotated_image
blocks. Diagrams live under frontend/public/geo/geomorphology/ (see
`fetch_geo_images`); attributions are in that folder's _attributions.json.
"""

from __future__ import annotations

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptEdge
from subjects.models import Chapter, Subject

SUBJECT_SLUG = "geography"
CHAPTER_SLUG = "geomorphology"
HUB_SLUG = "geomorphology"

IMG = "/geo/geomorphology/"

# Attribution lines shown under each figure.
SRC_PDF = "Vision IAS CCAB-2 Geography (private revision use)"
SRC_USGS = "Wikimedia Commons — USGS (public domain)"
SRC_NPS = "Wikimedia Commons — NPS (public domain)"
SRC_USDA = "Wikimedia Commons — USDA NRCS (public domain)"
SRC_CRAMERI = "Wikimedia Commons — Fabio Crameri (CC BY-SA 4.0)"
SRC_EARLE = "Wikimedia Commons — Panchuk & Earle (CC BY-SA 4.0)"

HUB_BLOCKS = [
    {
        "id": "geo-hub-mm",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "A restless, layered planet",
        "topic_label": "Geomorphology",
        "subject_label": "Earth's surface",
        "relation_label": "Is shaped by",
        "protects_from": [
            "Endogenic forces (from within) — build relief",
            "Exogenic forces (from outside) — wear it down",
            "The rock cycle recycling all material",
        ],
        "insight": "Interior heat builds; surface agents grade. Landforms are the running balance of the two.",
    },
    {
        "id": "geo-hub-pillars",
        "type": "pillars",
        "title": "Chapter map — open a cluster",
        "items": [
            {"id": "p-origin", "articles": "1.1", "label": "Origin of Earth", "slug": "geo-origin-earth", "detail": "Big Bang to a differentiated planet.", "tone": "teal"},
            {"id": "p-interior", "articles": "1.2", "label": "Earth's Interior", "slug": "geo-earth-interior", "detail": "Crust–mantle–core and discontinuities.", "tone": "olive"},
            {"id": "p-seismic", "articles": "1.2.2", "label": "Seismic Waves", "slug": "geo-seismic-waves", "detail": "P vs S waves and the shadow zone.", "tone": "gold"},
            {"id": "p-plates", "articles": "1.3.1", "label": "Plate Tectonics", "slug": "geo-plate-tectonics", "detail": "Boundaries and their landforms.", "tone": "orange"},
            {"id": "p-folds", "articles": "1.3.1", "label": "Folds & Faults", "slug": "geo-folds-faults", "detail": "Rock response to compression/tension.", "tone": "terracotta"},
            {"id": "p-eq", "articles": "1.4.1", "label": "Earthquakes", "slug": "geo-earthquakes", "detail": "Belts of the world and India's zones.", "tone": "maroon"},
            {"id": "p-volc", "articles": "1.4.2", "label": "Volcanoes", "slug": "geo-volcanoes", "detail": "Shield, strato, dome, cinder.", "tone": "teal"},
            {"id": "p-exo", "articles": "1.3.2", "label": "Exogenic Forces", "slug": "geo-exogenic-forces", "detail": "Weathering, erosion, deposition.", "tone": "olive"},
            {"id": "p-rocks", "articles": "1.5", "label": "Rocks & Rock Cycle", "slug": "geo-rocks-rock-cycle", "detail": "Igneous, sedimentary, metamorphic.", "tone": "gold"},
            {"id": "p-soils", "articles": "1.6", "label": "Soils", "slug": "geo-soils", "detail": "Forming factors and conservation.", "tone": "orange"},
        ],
    },
    {
        "id": "geo-hub-callout",
        "type": "callout",
        "tone": "note",
        "title": "How to revise",
        "body": "Start with the interior (what Earth is made of), then the forces (endogenic vs exogenic), then the phenomena (earthquakes, volcanoes) and materials (rocks, soils). Maps in the Earthquakes cluster are high-yield for prelims.",
    },
]

CLUSTERS = [
    {
        "slug": "geo-origin-earth",
        "title": "Origin and Evolution of Earth",
        "summary": "From the Big Bang to a layered, differentiated planet.",
        "sort_order": 1,
        "body": "## Origin and Evolution\n\nThe modern view combines the Big Bang (universe) with the nebular hypothesis (solar system). Early Earth differentiated into layers as heavy metals sank to the core.",
        "visual_blocks": [
            {
                "id": "origin-tl",
                "type": "timeline",
                "title": "Key milestones (million years ago)",
                "events": [
                    {"id": "bb", "year": 13800, "label": "Big Bang", "detail": "~13.8 billion years ago — expansion of space; hydrogen and helium form."},
                    {"id": "ss", "year": 4600, "label": "Solar system forms", "detail": "~4.6 billion years ago — nebular disc; planetesimals accrete into Earth."},
                    {"id": "diff", "year": 4500, "label": "Differentiation", "detail": "Heavy Fe/Ni sink to form the core; lighter silicates form mantle and crust."},
                    {"id": "moon", "year": 4400, "label": "Moon-forming impact", "detail": "Giant impact (Theia) hypothesis; debris coalesces into the Moon."},
                    {"id": "life", "year": 3800, "label": "Earliest life", "detail": "First microbial life in early oceans."},
                ],
            },
            {
                "id": "origin-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Exam hook",
                "body": "Big Bang explains the universe; the nebular hypothesis explains the solar system. Don't conflate the two.",
            },
        ],
    },
    {
        "slug": "geo-earth-interior",
        "title": "Internal Structure of the Earth",
        "summary": "Crust, mantle, and core — and the discontinuities between them.",
        "sort_order": 2,
        "body": "## Internal Structure\n\nEarth is layered by density: a thin **crust**, a thick **mantle**, and an Fe–Ni **core** (liquid outer, solid inner). Layers are separated by seismic **discontinuities**.",
        "visual_blocks": [
            {
                "id": "interior-annot",
                "type": "annotated_image",
                "title": "Label the layers",
                "src": IMG + "earth-interior.png",
                "alt": "Cutaway of Earth showing crust, mantle, outer core and inner core",
                "caption": "Hover a marker to reveal each layer.",
                "source": SRC_PDF,
                "markers": [
                    {"id": "crust", "x": 12, "y": 29, "label": "Crust", "detail": "5–70 km. Continental crust (~30–40 km) is thicker than oceanic (~7–10 km)."},
                    {"id": "mantle", "x": 15, "y": 35, "label": "Mantle", "detail": "To ~2900 km. The asthenosphere (partially molten) allows plate motion."},
                    {"id": "outer-core", "x": 17, "y": 41, "label": "Outer core", "detail": "Liquid Fe–Ni. Blocks S-waves and generates Earth's magnetic field."},
                    {"id": "inner-core", "x": 19, "y": 46, "label": "Inner core", "detail": "Solid Fe–Ni (~1250 km radius); the hottest, densest part."},
                ],
            },
            {
                "id": "interior-disc",
                "type": "image",
                "title": "Seismic discontinuities",
                "src": IMG + "seismic-discontinuity.png",
                "alt": "Diagram of Conrad, Moho, Repetti, Gutenberg and Lehmann discontinuities",
                "caption": "Conrad (intra-crust), Moho (crust–mantle), Repetti (upper–lower mantle), Gutenberg (mantle–core), Lehmann (outer–inner core).",
                "source": SRC_PDF,
            },
        ],
    },
    {
        "slug": "geo-seismic-waves",
        "title": "Seismic Waves and the Shadow Zone",
        "summary": "Body waves reveal the interior; the shadow zone proves a liquid outer core.",
        "sort_order": 3,
        "body": "## Seismic Waves\n\n**P-waves** (primary, compressional) travel through solids, liquids and gases; **S-waves** (secondary, transverse) travel only through solids. Their behaviour maps the interior.",
        "visual_blocks": [
            {
                "id": "seismic-img",
                "type": "image",
                "title": "P-wave and S-wave paths",
                "src": IMG + "seismic-shadow-zone.png",
                "alt": "S-wave and P-wave paths through Earth showing shadow zones",
                "caption": "S-waves are stopped by the liquid outer core (shadow beyond 103°); P-waves bend, leaving a shadow zone between 103° and 143°.",
                "source": SRC_EARLE,
            },
            {
                "id": "seismic-cmp",
                "type": "comparison",
                "title": "P-waves vs S-waves",
                "columns": [
                    {"id": "p", "heading": "P-waves (Primary)", "points": ["Compressional (push–pull)", "Fastest — arrive first", "Travel through solid, liquid, gas", "Partial shadow zone 103°–143°"]},
                    {"id": "s", "heading": "S-waves (Secondary)", "points": ["Transverse (shear)", "Slower — arrive second", "Travel only through solids", "Shadow beyond 103° — proves liquid outer core"]},
                ],
            },
            {
                "id": "seismic-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Common trap",
                "body": "The S-wave shadow zone (no S-waves beyond 103°) is the classic evidence for a LIQUID outer core — not the inner core.",
            },
        ],
    },
    {
        "slug": "geo-plate-tectonics",
        "title": "Endogenic Forces: Plate Tectonics",
        "summary": "Three boundary types and the landforms they create.",
        "sort_order": 4,
        "body": "## Plate Tectonics\n\nThe lithosphere is broken into plates riding the asthenosphere. Interactions at **convergent**, **divergent** and **transform** boundaries generate most of Earth's major relief.",
        "visual_blocks": [
            {
                "id": "plate-img",
                "type": "image",
                "title": "Plate boundaries and their landforms",
                "src": IMG + "plate-boundaries.png",
                "alt": "Cross-section of convergent, divergent and transform plate boundaries",
                "caption": "Convergent → trenches, island arcs, fold mountains; divergent → mid-ocean ridges, rift valleys; transform → faults.",
                "source": SRC_USGS,
            },
            {
                "id": "plate-cmp",
                "type": "comparison",
                "title": "Boundary types",
                "columns": [
                    {"id": "conv", "heading": "Convergent", "points": ["Plates collide", "Subduction / collision", "Trenches, arcs, Himalayas", "Explosive volcanism"]},
                    {"id": "div", "heading": "Divergent", "points": ["Plates move apart", "Sea-floor spreading", "Mid-ocean ridges, rifts", "Basaltic (effusive) volcanism"]},
                    {"id": "trans", "heading": "Transform", "points": ["Plates slide past", "Crust neither made nor lost", "Transform faults (e.g. San Andreas)", "Shallow-focus earthquakes"]},
                ],
            },
        ],
    },
    {
        "slug": "geo-folds-faults",
        "title": "Folds and Faults",
        "summary": "How rocks bend (folds) and break (faults) under stress.",
        "sort_order": 5,
        "body": "## Folds and Faults\n\n**Compression** bends ductile rock into **folds** (anticlines/synclines); brittle rock **breaks** along **faults** under tension, compression or shear.",
        "visual_blocks": [
            {
                "id": "fold-img",
                "type": "image",
                "title": "Folds: anticline and syncline",
                "src": IMG + "fold-types.png",
                "alt": "Anticline and syncline folds with axial planes",
                "caption": "Anticline = up-arch (oldest rocks in core); syncline = down-fold (youngest rocks in core).",
                "source": SRC_CRAMERI,
            },
            {
                "id": "fault-img",
                "type": "image",
                "title": "Fault types",
                "src": IMG + "fault-types.png",
                "alt": "Thrust, normal and strike-slip faults",
                "caption": "Normal fault (tension, divergent), thrust/reverse fault (compression, convergent), strike-slip fault (shear, transform).",
                "source": SRC_PDF,
            },
        ],
    },
    {
        "slug": "geo-earthquakes",
        "title": "Earthquakes",
        "summary": "Seismic belts of the world and India's seismic zones.",
        "sort_order": 6,
        "body": "## Earthquakes\n\nSudden release of energy in the crust/upper mantle. Most quakes cluster along plate boundaries — the **Circum-Pacific** and **Mediterranean–Himalayan** belts.",
        "visual_blocks": [
            {
                "id": "eq-world",
                "type": "image",
                "title": "World seismic belts",
                "src": IMG + "world-seismic-belts.png",
                "alt": "Global distribution of earthquakes along plate margins",
                "caption": "Circum-Pacific ('Ring of Fire') is the most active; Mediterranean–Himalayan belt runs through northern India.",
                "source": SRC_PDF,
            },
            {
                "id": "eq-india",
                "type": "image",
                "title": "Seismic zones of India",
                "src": IMG + "india-seismic-zones.png",
                "alt": "Map of India's seismic zones II to V",
                "caption": "Zone V (highest risk) — NE India, Kashmir, Kutch; Zone II (lowest) — peninsular interior.",
                "source": SRC_PDF,
            },
            {
                "id": "eq-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Remember",
                "body": "Focus (hypocentre) is where rupture starts inside Earth; the epicentre is the point vertically above it on the surface.",
            },
        ],
    },
    {
        "slug": "geo-volcanoes",
        "title": "Volcanoes",
        "summary": "Types by shape and eruption style.",
        "sort_order": 7,
        "body": "## Volcanoes\n\nA vent where magma, gases and pyroclasts reach the surface. Shape and explosivity depend on lava viscosity (silica content).",
        "visual_blocks": [
            {
                "id": "volc-img",
                "type": "image",
                "title": "Types of volcanoes",
                "src": IMG + "volcano-types.png",
                "alt": "Shield, stratovolcano, volcanic dome and cinder cone",
                "caption": "Shield (fluid basalt, gentle), stratovolcano (viscous, explosive), lava dome, and cinder cone.",
                "source": SRC_PDF,
            },
            {
                "id": "volc-cmp",
                "type": "comparison",
                "title": "Shield vs Stratovolcano",
                "columns": [
                    {"id": "shield", "heading": "Shield", "points": ["Low-silica basaltic lava", "Low viscosity — flows far", "Gentle slopes, broad base", "Effusive (e.g. Mauna Kea)"]},
                    {"id": "strato", "heading": "Stratovolcano", "points": ["High-silica andesitic lava", "High viscosity — traps gas", "Steep, tall cone", "Explosive (e.g. Fuji, St. Helens)"]},
                ],
            },
        ],
    },
    {
        "slug": "geo-exogenic-forces",
        "title": "Exogenic Forces",
        "summary": "Weathering, erosion, transport and deposition grade the land down.",
        "sort_order": 8,
        "body": "## Exogenic Forces\n\nExternally driven (sun, gravity, water, wind, ice) processes that break down and redistribute material, lowering relief.",
        "visual_blocks": [
            {
                "id": "exo-pillars",
                "type": "pillars",
                "title": "The degradation sequence",
                "items": [
                    {"id": "weather", "articles": "In situ", "label": "Weathering", "slug": "geo-exogenic-forces", "detail": "Physical, chemical and biological breakdown of rock in place.", "tone": "teal"},
                    {"id": "mass", "articles": "Gravity", "label": "Mass movement", "slug": "geo-exogenic-forces", "detail": "Downslope movement — creep, slides, flows.", "tone": "olive"},
                    {"id": "erosion", "articles": "Agents", "label": "Erosion & transport", "slug": "geo-exogenic-forces", "detail": "Running water, wind, glaciers and waves detach and carry material.", "tone": "gold"},
                    {"id": "deposit", "articles": "Sink", "label": "Deposition", "slug": "geo-exogenic-forces", "detail": "Sediments settle — deltas, dunes, moraines, beaches.", "tone": "orange"},
                ],
            },
            {
                "id": "exo-flow",
                "type": "flowchart",
                "title": "Weathering → erosion → deposition",
                "steps": [
                    {"id": "s1", "label": "Weathering", "detail": "Rock disintegrates/decomposes in situ (no transport)."},
                    {"id": "s2", "label": "Erosion", "detail": "Weathered material is detached by an agent."},
                    {"id": "s3", "label": "Transport", "detail": "Water, wind, or ice carries the load."},
                    {"id": "s4", "label": "Deposition", "detail": "Load is dropped as energy falls, forming depositional landforms."},
                ],
            },
        ],
    },
    {
        "slug": "geo-rocks-rock-cycle",
        "title": "Rocks and the Rock Cycle",
        "summary": "Three rock families continuously recycled.",
        "sort_order": 9,
        "body": "## Rocks and the Rock Cycle\n\n**Igneous** (from magma), **sedimentary** (from compacted sediments) and **metamorphic** (from heat/pressure) rocks transform into one another over geological time.",
        "visual_blocks": [
            {
                "id": "rock-img",
                "type": "image",
                "title": "The rock cycle",
                "src": IMG + "rock-cycle.png",
                "alt": "Diagram of the rock cycle across the lithosphere",
                "caption": "Melting, cooling, weathering, deposition, burial and metamorphism convert rocks between the three families.",
                "source": SRC_NPS,
            },
            {
                "id": "rock-cmp",
                "type": "comparison",
                "title": "Three rock families",
                "columns": [
                    {"id": "ig", "heading": "Igneous", "points": ["Solidified magma/lava", "Intrusive (granite) / extrusive (basalt)", "Crystalline, no fossils"]},
                    {"id": "sed", "heading": "Sedimentary", "points": ["Compacted/cemented sediments", "Layered (strata)", "May contain fossils (e.g. limestone)"]},
                    {"id": "met", "heading": "Metamorphic", "points": ["Altered by heat/pressure", "Foliated (slate, schist)", "Marble ← limestone; quartzite ← sandstone"]},
                ],
            },
        ],
    },
    {
        "slug": "geo-soils",
        "title": "Soils",
        "summary": "Forming factors, the profile, and conservation.",
        "sort_order": 10,
        "body": "## Soils\n\nSoil is the weathered, biologically active top layer. It develops in **horizons** (O-A-B-C-R) under the control of five forming factors.",
        "visual_blocks": [
            {
                "id": "soil-pillars",
                "type": "pillars",
                "title": "Five soil-forming factors (CLORPT)",
                "items": [
                    {"id": "cl", "articles": "CL", "label": "Climate", "slug": "geo-soils", "detail": "Temperature and rainfall control weathering rate and leaching.", "tone": "teal"},
                    {"id": "o", "articles": "O", "label": "Organisms", "slug": "geo-soils", "detail": "Vegetation, microbes and fauna add humus and mix layers.", "tone": "olive"},
                    {"id": "r", "articles": "R", "label": "Relief", "slug": "geo-soils", "detail": "Slope and aspect affect drainage, erosion and depth.", "tone": "gold"},
                    {"id": "p", "articles": "P", "label": "Parent material", "slug": "geo-soils", "detail": "Underlying rock sets texture and mineral content.", "tone": "orange"},
                    {"id": "t", "articles": "T", "label": "Time", "slug": "geo-soils", "detail": "Mature soils show well-developed horizons.", "tone": "terracotta"},
                ],
            },
            {
                "id": "soil-img",
                "type": "image",
                "title": "Soil horizons",
                "src": IMG + "soil-profile.jpg",
                "alt": "Soil horizon boundaries and profile",
                "caption": "Horizons grade from organic-rich topsoil (A) into subsoil (B) and parent material (C).",
                "source": SRC_USDA,
            },
            {
                "id": "soil-callout",
                "type": "callout",
                "tone": "note",
                "title": "Conservation",
                "body": "Contour bunding, terracing, shelter belts and afforestation reduce soil erosion and degradation.",
            },
        ],
    },
]

# (source, relation, target) — hub parents each cluster; a few cross-links.
EDGES = [
    (HUB_SLUG, "parent", c["slug"]) for c in CLUSTERS
] + [
    ("geo-plate-tectonics", "related", "geo-folds-faults"),
    ("geo-plate-tectonics", "related", "geo-earthquakes"),
    ("geo-plate-tectonics", "related", "geo-volcanoes"),
    ("geo-earth-interior", "related", "geo-seismic-waves"),
    ("geo-exogenic-forces", "related", "geo-soils"),
    ("geo-exogenic-forces", "related", "geo-rocks-rock-cycle"),
]


class Command(BaseCommand):
    help = "Seed Geography → Geomorphology visual chapter (Vision IAS CCAB-2 Ch.1)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug to seed into (default: fortuneias).",
        )

    def handle(self, *args, **options):
        from academies.seed_utils import get_academy_or_fail

        academy = get_academy_or_fail(options["academy"])

        subject, _ = Subject.objects.update_or_create(
            academy=academy,
            slug=SUBJECT_SLUG,
            defaults={
                "name": "Geography",
                "description": (
                    "Physical and Indian geography for UPSC — geomorphology, "
                    "climatology, oceanography, and resources."
                ),
                "is_active": True,
                "sort_order": 2,
            },
        )

        chapter, _ = Chapter.objects.update_or_create(
            subject=subject,
            slug=CHAPTER_SLUG,
            defaults={
                "title": "Geomorphology",
                "sort_order": 1,
                "book_ref": "Vision IAS CCAB-2 Geography, Ch. 1",
                "summary": (
                    "Visual revision of Ch.1 — Earth's origin and interior, "
                    "seismic waves, plate tectonics, folds/faults, earthquakes, "
                    "volcanoes, exogenic forces, rocks, and soils."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Geomorphology",
                "summary": (
                    "The study of landforms and the endogenic/exogenic processes "
                    "that shape Earth's surface."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Work inward-out: the **interior** (structure, seismic evidence), "
                    "then the **forces** (endogenic plate tectonics vs exogenic "
                    "gradation), then the **phenomena** (earthquakes, volcanoes) and "
                    "**materials** (rocks, soils). This is a visual layer — pair it "
                    "with the source notes."
                ),
                "visual_blocks": HUB_BLOCKS,
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

        created_edges = 0
        for src, rel, tgt in EDGES:
            source = by_slug.get(src)
            target = by_slug.get(tgt)
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
            created_edges += int(was_created)

        self.stdout.write(
            self.style.SUCCESS(
                f"Geomorphology seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts and {created_edges} new edges."
            )
        )
