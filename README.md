# UPSC Buddy

Multi-tenant visual revision for UPSC — academy subdomains, invite-only students, syllabus Subject → Chapter spine + visual concept blocks.

Product vision: [product_info.md](product_info.md)  
Module notes: [docs/MODULES.md](docs/MODULES.md)

## Stack

- **API:** Django 4.2+ / DRF / SimpleJWT
- **DB:** PostgreSQL (SQLite escape hatch via `USE_SQLITE=True`)
- **Cache / Celery broker:** Redis
- **Frontend:** Next.js (App Router) + Tailwind + TanStack Query
- **Tenancy:** Shared DB, row-level `academy_id`; SPA sends `X-Academy-Slug`
- **Ops UI:** Django Admin (academies, concepts, PYQs)

## Quick start (local)

### 1. Infrastructure

```bash
docker compose up -d db redis
```

### 2. Backend

```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_academy_fortuneias   # prints invite code
python manage.py seed_syllabus_skeleton    # all subjects + chapters
python manage.py seed_polity               # Polity content → fortuneias
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8300
```

API: http://127.0.0.1:8300  
Admin: http://127.0.0.1:8300/admin/

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

Use the **academy subdomain** (not apex localhost):

- http://fortuneias.localhost:3000 — Fortune IAS tenant
- http://localhost:3000 — apex “academy access only” landing

Join at `/join` with the invite code printed by `seed_academy_fortuneias`.

### SQLite escape hatch

```bash
export USE_SQLITE=True
source .venv/bin/activate
python manage.py migrate
python manage.py seed_academy_fortuneias
python manage.py seed_syllabus_skeleton
python manage.py seed_polity
```

## Multi-tenant notes

| Role | How |
|------|-----|
| Platform superadmin | Django `is_superuser` |
| Academy admin / staff / student | `AcademyMembership.role` |
| Tenant signal | Header `X-Academy-Slug: fortuneias` (from subdomain) |
| Signup | Invite-only: `POST /api/auth/join/` |

Prod: wildcard DNS `*.upscbuddy.com` → frontend; `ALLOWED_HOSTS=.upscbuddy.com`; CORS regex for `https://*.upscbuddy.com`.

## Public API (v1)

All content routes require `X-Academy-Slug`.

| Method | Path | Auth |
|--------|------|------|
| POST | `/api/auth/join/` | public (invite code) |
| POST | `/api/auth/token/` | public (membership required) |
| POST | `/api/auth/token/refresh/` | public |
| GET | `/api/auth/me/` | JWT |
| POST | `/api/auth/logout/` | JWT |
| GET | `/api/academies/current/` | public |
| GET | `/api/subjects/` | public |
| GET | `/api/subjects/<slug>/chapters/` | public |
| GET | `/api/chapters/<slug>/` | public |
| GET | `/api/concepts/?subject=&q=` | public |
| GET | `/api/concepts/<slug>/` | public |
| GET | `/api/concepts/<slug>/graph/?depth=` | public |
| GET/PATCH | `/api/learning/progress/` | JWT |
| GET | `/api/learning/revise-next/` | JWT |

## Docker full stack

```bash
docker compose up --build
```

Services: `db`, `redis`, `backend`, `worker`, `beat`, `frontend`.

## Post-MVP

- Active learning (retrieval, blank maps, discrimination drills)
- AI tutor (OpenAI/Gemini)
- TipTap / visual-block editing
- Billing / seat limits
- Additional academies beyond Fortune IAS
