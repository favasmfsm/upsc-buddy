# Deploying UPSC Buddy on Railway

Everything runs in one Railway project: **backend** (Django API + admin), **frontend** (Next.js), **Postgres** and **Redis**. Each `git push` to `main` redeploys automatically.

This setup covers the website and its seeded content (subjects, chapters, concepts). The PDF / current-affairs pipeline (Celery worker + beat, file uploads) is intentionally left out for now — see [Not included yet](#not-included-yet).

Time needed: ~30 minutes the first time.

---

## 1. Create the project + backend

1. Go to <https://railway.com> → **Login with GitHub**.
2. **New Project → Deploy from GitHub repo → `favasmfsm/upsc-buddy`**.
   (If the repo isn't listed, click **Configure GitHub App** and give Railway access to it.)
3. A service appears on the canvas. Click it → **Settings** → rename it to **`backend`** (the name matters: other variables reference it).
4. Still in **Settings → Networking**, click **Generate Domain**. You'll get something like `backend-production-xxxx.up.railway.app`.

The first deploy will fail — that's expected, it has no database or variables yet.

## 2. Add Postgres and Redis

On the project canvas: **+ Create → Database → PostgreSQL**, then again **+ Create → Database → Redis**.
Leave their names as `Postgres` and `Redis`.

## 3. Backend variables

Generate a secret key in your terminal:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

Open **backend → Variables → Raw Editor**, paste this, replace the secret key, and click **Update Variables**:

```
DJANGO_SECRET_KEY=paste-the-generated-key-here
DB_NAME=${{Postgres.PGDATABASE}}
DB_USERNAME=${{Postgres.PGUSER}}
DB_PASSWORD=${{Postgres.PGPASSWORD}}
DB_HOST=${{Postgres.PGHOST}}
DB_PORT=${{Postgres.PGPORT}}
REDIS_URL=${{Redis.REDIS_URL}}
CACHE_URL=${{Redis.REDIS_URL}}
ALLOWED_HOSTS=${{RAILWAY_PUBLIC_DOMAIN}}
CSRF_TRUSTED_ORIGINS=https://${{RAILWAY_PUBLIC_DOMAIN}}
CORS_ALLOWED_ORIGINS=https://${{frontend.RAILWAY_PUBLIC_DOMAIN}}
FRONTEND_URL=https://${{frontend.RAILWAY_PUBLIC_DOMAIN}}
RUN_SEEDS=true
GEMINI_API_KEY=
```

`${{...}}` values are filled in by Railway — paste them exactly as written. The `frontend` ones resolve once step 4 is done.

## 4. Frontend service

1. On the canvas: **+ Create → GitHub Repo → `favasmfsm/upsc-buddy`** again.
2. Click the new service → **Settings**:
   - Rename it to **`frontend`**.
   - **Source → Root Directory**: `/frontend`
   - **Config-as-code → Railway Config File**: `/frontend/railway.toml`
   - **Networking → Generate Domain**.
3. **Variables → Raw Editor**:

```
NEXT_PUBLIC_API_URL=https://${{backend.RAILWAY_PUBLIC_DOMAIN}}
NEXT_PUBLIC_DEFAULT_ACADEMY=fortuneias
```

`NEXT_PUBLIC_DEFAULT_ACADEMY` makes the `*.up.railway.app` link open the Fortune IAS academy, so you can use the site before you have your own domain.

## 5. Deploy

Click **Deploy** (top of the canvas) to apply all pending changes. If the backend already failed earlier, open it → **Deployments → ⋯ → Redeploy**.

What happens on each backend deploy (`scripts/predeploy.sh`):
1. Database migrations run.
2. If `RUN_SEEDS=true`, all content seeds run (`scripts/seed_all.sh`).

Open the backend's **Deployments → View logs → Pre-deploy** tab and look for:

```
invite_code: XXXXXXXXXX
```

That's the code students use to join Fortune IAS. (You can also see it later in Django admin → Academies.)

## 6. Create your admin login

Install the Railway CLI and connect to the project once:

```bash
brew install railway
```

```bash
railway login
```

```bash
cd /Users/favasm/Desktop/UPSC/upsc_buddy && railway link
```

Then open a shell inside the running backend and create the admin user:

```bash
railway ssh --service backend
```

Inside that shell:

```bash
python manage.py createsuperuser
```

Admin is at `https://<backend domain>/admin/`.

## 7. Check it works

- `https://<frontend domain>/` → the Fortune IAS site.
- `https://<backend domain>/admin/` → Django admin (styled, not plain HTML).
- Join with the invite code, log in, open Polity.

---

## Day-to-day

- **Ship a change:** commit and `git push`. Railway rebuilds whichever service's files changed.
- **Content seeds:** with `RUN_SEEDS=true`, every backend deploy re-applies the seed files. That is what you want while content lives in the `seed_*.py` files. If you start editing concepts in Django admin instead, set `RUN_SEEDS=false`, otherwise the next deploy overwrites those edits.
- **Logs:** click a service → **Deployments → View logs**.
- **Database backups:** Postgres service → **Backups** (enable scheduled backups).

## Custom domain (when you have one)

The app is built for `upscbuddy.com` with academy subdomains (`fortuneias.upscbuddy.com`). If your domain is different, set `NEXT_PUBLIC_BASE_DOMAIN=yourdomain.com` on the frontend.

1. **frontend → Settings → Networking → Custom Domain**: add `upscbuddy.com` and `*.upscbuddy.com`.
2. **backend → Settings → Networking → Custom Domain**: add `api.upscbuddy.com`.
3. At your domain registrar, add the DNS records Railway shows for each domain. HTTPS certificates are issued automatically.
4. Update variables:
   - backend: `ALLOWED_HOSTS=api.upscbuddy.com,${{RAILWAY_PUBLIC_DOMAIN}}`, `CSRF_TRUSTED_ORIGINS=https://api.upscbuddy.com`, `FRONTEND_URL=https://fortuneias.upscbuddy.com`
   - frontend: `NEXT_PUBLIC_API_URL=https://api.upscbuddy.com`
   - CORS for `https://*.upscbuddy.com` is already allowed by default (`CORS_ALLOWED_ORIGIN_REGEXES` in `core/settings/prod.py`).

## Not included yet

These need extra pieces; add them when you need them:

- **Current-affairs PDFs / quiz generation** — needs Celery `worker` + `beat` services and shared file storage (S3 or a Railway Bucket), because the API and worker run on separate machines.
- **Uploaded files (academy logos/favicons)** — without S3 they are saved on the container's disk and are lost on the next deploy. Set `AWS_STORAGE_BUCKET_NAME`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_REGION_NAME` to store them in S3.
- **Email** — without AWS SES credentials, emails are only printed to the backend logs.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Backend crash: `DJANGO_SECRET_KEY ... required` or `DB_NAME ... required` | Variables missing — redo step 3, then redeploy. |
| `Bad Request (400)` on the backend URL | `ALLOWED_HOSTS` doesn't include the domain you're visiting. |
| Frontend loads but shows no data / network errors | `NEXT_PUBLIC_API_URL` is wrong, or backend `CORS_ALLOWED_ORIGINS` doesn't match the frontend URL. Changing `NEXT_PUBLIC_*` needs a **redeploy** of the frontend (it's baked in at build time). |
| Admin pages have no styling | Check the backend build log for a `collectstatic` error. |
| "Academy access only" page on the Railway URL | `NEXT_PUBLIC_DEFAULT_ACADEMY` not set on the frontend, or it wasn't redeployed after setting it. |
