# Modules

UPSC Buddy is a **passive visual revision** layer across the UPSC syllabus: **Subject → Section → Chapter (syllabus branch) → Concept** with concept **visual blocks**. Polity (Fundamental Rights) is the content pilot; other subjects are skeleton chapters until content is added. **Current Affairs prelims quizzes** are a separate surface.

**Design philosophy:** choose the right **visual grammar** for each concept — see [`docs/VISUAL_GRAMMARS.md`](VISUAL_GRAMMARS.md). Authoring rule: **1 primary + ≤2 support** grammars per concept.

## subjects

UPSC buckets (Polity, History, Art & Culture, Geography, Economy, Environment, S&T, Society, IR, Internal Security, Disaster Management).

- Model: `Subject` (slug, name, `sort_order`)
- Model: `Section` — Laxmikanth-style part under a subject (`sort_order`, optional `summary`, `is_published`)
- Model: `Chapter` — syllabus branch (`sort_order`, optional `section`, optional `book_ref`, `is_published`)
- Seed: `seed_syllabus_skeleton` → Polity sections (Part I filled with Ch.1–12; later parts empty) + chapters; then content seeds for authored chapters
- Catalog: `seed_visual_grammar_catalog` → `/concepts/visual-grammar-catalog`

APIs:

- `GET /api/subjects/`
- `GET /api/subjects/<slug>/sections/`
- `GET /api/subjects/<slug>/chapters/`
- `GET /api/chapters/<slug>/`

## concepts

Core learning unit inside a chapter.

- `Concept` — title, slug, summary, Markdown `body`, `visual_blocks` (JSON), optional `chapter`, `sort_order`, status
- `ConceptEdge` — typed links (`parent`, `related`, `prerequisite`)
- `ConceptArticle` — constitutional / legal refs
- `CaseLaw` — landmark judgments linked M2M to concepts
- `ConstitutionalAmendment` — amendment number/year/effect linked M2M to concepts

**Visual grammars (full catalog):**

| Type | Role |
|------|------|
| `mental_model` | Shield / first intuition |
| `tree` | Hierarchy / constitution map |
| `pillars` | Expandable categories |
| `timeline` | Historical / amendment sequence |
| `relation_graph` | Live concept-edge graph embed |
| `flowchart` | Decision tree **or** restriction tree |
| `journey` | Citizen story path |
| `comparison` | Side-by-side contrast |
| `pyq_heatmap` | Live PYQ frequency |
| `article_explorer` | Article drill stages |
| `case_network` | Cases around a hub |
| `memory_palace` | Place-based recall |
| `simulator` | What-if state machine |
| `map` / `callout` / `markdown` | Utilities |

**Concept page IA (visual-first):** visuals lead → Notes collapsed → Articles only when no visuals → Cases → Amendments → PYQs. Full graph: `/concepts/<slug>/graph`.

Authoring: **Django Admin** + seed commands. TipTap deferred.

Pilot: Laxmikanth Ch.8 Fundamental Rights + `visual-grammar-catalog`.

## questions

Previous year questions linked to concepts (reference only in MVP — not forced drills).

- `PYQ` — year, question text, optional answer key, M2M to concepts
- Hub `pyq_heatmap` blocks enrich counts from these links at read time

## current_affairs

Prelims-focused current affairs quizzes from uploaded daily/monthly PDFs.

- **Gemini once at ingest** (Celery): never called on student quiz requests
- Models: `CADocument`, `CAQuestion` (auto-published MCQ bank), `QuizAttempt`, `QuizAttemptAnswer`
- `subject_tag` normalized to allowlist: Polity, Economy, IR, Environment, S&T, Geography, Defence, History, Society, Other (`current_affairs/subjects.py`)
- **Date-range quizzes:** dailies overlapping the range are always eligible; a **monthly** enters the pool only when the range **fully covers** that month (`start ≤ period_start` and `end ≥ period_end`). Partial weeks → dailies only.
- Staff UI (`/staff/current-affairs`): academy admin/staff + platform superuser upload PDF → worker generates questions → publish/unpublish; **regenerate** (same PDF), **replace PDF**, or **delete** document
- Academy branding UI (`/staff/branding`): **academy admin only** (+ superuser) — display name, tagline, logo, favicon, primary color
- Django Admin remains available for platform ops
- Only upload material you have rights to use

APIs:

- `GET /api/current_affairs/documents/` — READY documents (students)
- `POST /api/current_affairs/quizzes/start/` — daily / monthly / date-range from bank
- `GET /api/current_affairs/quizzes/<id>/`
- `POST /api/current_affairs/quizzes/<id>/submit/` — also writes `QuizAttemptAnswer` rows
- `GET /api/current_affairs/attempts/`
- Analytics:
  - `GET /api/current_affairs/analytics/me/?days=90` — student score series, subject accuracy, weak topics
  - `GET /api/current_affairs/analytics/academy/?days=90` — staff cohort summary + students
  - `GET /api/current_affairs/analytics/academy/students/<user_id>/` — staff student drill-down
- Staff (JWT + academy admin/staff or superuser):
  - `GET/POST /api/current_affairs/staff/documents/`
  - `GET/PATCH/DELETE /api/current_affairs/staff/documents/<id>/` — PATCH replaces PDF (multipart); DELETE removes doc + questions; blocked with 409 while `processing`
  - `POST /api/current_affairs/staff/documents/<id>/regenerate/` — same PDF, force re-run (409 while processing)
  - `GET /api/current_affairs/staff/documents/<id>/questions/`
  - `PATCH /api/current_affairs/staff/questions/<id>/` — `is_published` only
- Academy branding (JWT + academy admin or superuser):
  - `GET /api/academies/current/` — public branding payload (includes tagline, logo_url, favicon_url, primary_color)
  - `GET/PATCH /api/academies/current/branding/` — admin update (multipart for logo/favicon)

Frontend: `/current-affairs` (Practice | Analytics); `/current-affairs/quiz/[attemptId]` (auth required); `/staff/current-affairs` (Library | Analytics); `/staff/branding` (academy admin branding).

Backfill: `python manage.py backfill_quiz_attempt_answers`

Env: `GEMINI_API_KEY`, `GEMINI_MODEL`, optional `CA_*_QUESTION_*` targets.

## learning

Per-user progress (soft, not gated by quizzes).

- `UserConceptProgress` — `not_started` | `studied` | `revise_later`
- `revise-next` API: prefer `revise_later`, then `not_started`

## user

Email-based JWT auth (unchanged foundation).

## Future (out of MVP)

| Module | Notes |
|--------|--------|
| Active learning | Retrieval-before-reveal, blank maps, discrimination drills, PYQ exit loops |
| Auto-hydrate explorers | Pull PYQs/CA into `article_explorer` stages |
| `ai_tutor` | Chat against concept context |
| CA ↔ Concept links | Hot / concept tagging from CA topics |
| TipTap staff editor | Rich body / visual block editing |
| pgvector | Semantic search over concepts |

## Enabling later apps

Add new apps to `INSTALLED_APPS` in `core/settings/shared.py` when you create them.
