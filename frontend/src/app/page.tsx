import Link from "next/link";
import { headers } from "next/headers";

import { HomeContinue } from "@/components/HomeContinue";
import { Card, CardTitle } from "@/components/ui/card";
import { academySlugFromHost } from "@/lib/academy";
import { fetchCurrentAcademy, fetchSubjects } from "@/lib/api";

async function ApexLanding() {
  return (
    <div className="mx-auto max-w-xl space-y-6 py-16 text-center">
      <p className="text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
        UPSC Buddy
      </p>
      <h1 className="font-[family-name:var(--font-display)] text-4xl text-[var(--ink)] sm:text-5xl">
        Academy access only
      </h1>
      <p className="text-lg text-[var(--ink-soft)]">
        Learning lives on your academy subdomain. Open the link your coaching
        institute shared — for example{" "}
        <code className="rounded bg-[var(--accent-soft)] px-1.5 py-0.5 text-sm text-[var(--accent)]">
          fortuneias.upscbuddy.com
        </code>
        .
      </p>
      <p className="text-sm text-[var(--ink-soft)]">
        Local development:{" "}
        <code className="text-[var(--ink)]">http://fortuneias.localhost:3000</code>
      </p>
    </div>
  );
}

async function TenantHome({ slug }: { slug: string }) {
  let subjects: Awaited<ReturnType<typeof fetchSubjects>> = [];
  let error: string | null = null;
  let academyName = slug;
  let tagline =
    "Visual revision across the UPSC syllabus — maps and flowcharts instead of re-reading notes.";

  try {
    const academy = await fetchCurrentAcademy();
    academyName = academy.display_name || academy.name;
    if (academy.tagline?.trim()) {
      tagline = academy.tagline.trim();
    }
  } catch {
    /* branding optional */
  }

  try {
    subjects = await fetchSubjects();
  } catch {
    error = "Could not load subjects. Is the API running on :8300?";
  }

  return (
    <div className="space-y-12">
      <section className="relative overflow-hidden border-b border-[var(--line)] pb-12">
        <p className="mb-3 text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
          Visual revision
        </p>
        <h1 className="max-w-3xl font-[family-name:var(--font-display)] text-5xl leading-[1.05] text-[var(--ink)] sm:text-6xl">
          {academyName}
        </h1>
        <p className="mt-4 max-w-xl text-lg text-[var(--ink-soft)]">
          {tagline}
        </p>
        <HomeContinue />
      </section>

      <section>
        <h2 className="mb-6 font-[family-name:var(--font-display)] text-3xl">
          Subjects
        </h2>
        {error ? (
          <p className="rounded-md bg-[var(--accent-soft)] px-4 py-3 text-sm text-[var(--accent)]">
            {error}
          </p>
        ) : subjects.length === 0 ? (
          <p className="text-sm text-[var(--ink-soft)]">
            No subjects published yet.
          </p>
        ) : (
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {subjects.map((subject) => (
              <Link
                key={subject.id}
                href={`/subjects/${subject.slug}`}
                className="block transition hover:-translate-y-0.5"
              >
                <Card className="h-full">
                  <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                    {String(subject.sort_order).padStart(2, "0")}
                  </p>
                  <CardTitle className="mt-1">{subject.name}</CardTitle>
                  <p className="mt-2 line-clamp-3 text-sm text-[var(--ink-soft)]">
                    {subject.description}
                  </p>
                </Card>
              </Link>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

export default async function HomePage() {
  const h = await headers();
  const host = h.get("host") || "localhost";
  const slug =
    h.get("x-academy-slug") || academySlugFromHost(host);

  if (!slug) {
    return <ApexLanding />;
  }
  return <TenantHome slug={slug} />;
}
