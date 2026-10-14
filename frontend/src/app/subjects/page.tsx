import Link from "next/link";

import { Card, CardTitle } from "@/components/ui/card";
import { fetchSubjects } from "@/lib/api";

export default async function SubjectsPage() {
  let subjects: Awaited<ReturnType<typeof fetchSubjects>> = [];
  let error: string | null = null;

  try {
    subjects = await fetchSubjects();
  } catch {
    error = "Could not load subjects. Is the API running on :8300?";
  }

  return (
    <div className="space-y-8">
      <div className="border-b border-[var(--line)] pb-8">
        <p className="mb-2 text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
          Syllabus
        </p>
        <h1 className="font-[family-name:var(--font-display)] text-4xl sm:text-5xl">
          Subjects
        </h1>
        <p className="mt-3 max-w-2xl text-lg text-[var(--ink-soft)]">
          UPSC buckets with syllabus-branch chapters. Open a subject to revise
          by topic — content fills in over time.
        </p>
      </div>

      {error ? (
        <p className="rounded-md bg-[var(--accent-soft)] px-4 py-3 text-sm text-[var(--accent)]">
          {error}
        </p>
      ) : subjects.length === 0 ? (
        <p className="text-[var(--ink-soft)]">
          No subjects yet. Run{" "}
          <code className="text-sm">seed_syllabus_skeleton</code>.
        </p>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
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
                {subject.description && (
                  <p className="mt-2 line-clamp-3 text-sm text-[var(--ink-soft)]">
                    {subject.description}
                  </p>
                )}
              </Card>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
