import Link from "next/link";
import { notFound } from "next/navigation";

import { Button } from "@/components/ui/button";
import { Card, CardTitle } from "@/components/ui/card";
import { fetchSections, fetchSubjects } from "@/lib/api";

export default async function SubjectChaptersPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  let subjectName = slug;
  let subjectDescription = "";
  let sections: Awaited<ReturnType<typeof fetchSections>> = [];
  let error: string | null = null;

  try {
    const subjects = await fetchSubjects();
    const match = subjects.find((s) => s.slug === slug);
    if (!match) {
      notFound();
    }
    subjectName = match.name;
    subjectDescription = match.description;
    sections = await fetchSections(slug);
  } catch {
    error = "Could not load chapters. Is the API running on :8300?";
  }

  return (
    <div className="space-y-8">
      <div className="border-b border-[var(--line)] pb-8">
        <p className="mb-2 text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
          <Link href="/subjects" className="hover:underline">
            Subjects
          </Link>
          {" / "}
          syllabus parts
        </p>
        <h1 className="font-[family-name:var(--font-display)] text-4xl sm:text-5xl">
          {subjectName}
        </h1>
        {subjectDescription && (
          <p className="mt-3 max-w-2xl text-lg text-[var(--ink-soft)]">
            {subjectDescription}
          </p>
        )}
        <div className="mt-4 flex flex-wrap gap-4">
          <Link
            href={`/concepts?subject=${slug}`}
            className="text-sm text-[var(--accent)] hover:underline"
          >
            Browse all concepts →
          </Link>
          {slug === "polity" && (
            <Link
              href="/concepts/visual-grammar-catalog"
              className="text-sm text-[var(--accent)] hover:underline"
            >
              Visual grammar catalog →
            </Link>
          )}
        </div>
      </div>

      {error ? (
        <p className="rounded-md bg-[var(--accent-soft)] px-4 py-3 text-sm text-[var(--accent)]">
          {error}
        </p>
      ) : sections.length === 0 ? (
        <p className="text-[var(--ink-soft)]">
          No published sections yet. Run{" "}
          <code className="text-sm">seed_syllabus_skeleton</code>.
        </p>
      ) : (
        <div className="space-y-10">
          {sections.map((section) => (
            <section key={section.id} className="space-y-4">
              <div>
                <p className="text-xs uppercase tracking-[0.18em] text-[var(--ink-soft)]">
                  Part {section.sort_order}
                </p>
                <h2 className="mt-1 font-[family-name:var(--font-display)] text-2xl sm:text-3xl">
                  {section.title}
                </h2>
                {section.summary && (
                  <p className="mt-2 max-w-2xl text-sm text-[var(--ink-soft)]">
                    {section.summary}
                  </p>
                )}
              </div>

              {section.chapters.length === 0 ? (
                <p className="text-sm text-[var(--ink-soft)]">
                  Chapters coming soon
                </p>
              ) : (
                <div className="space-y-4">
                  {section.chapters.map((chapter) => (
                    <Link
                      key={chapter.id}
                      href={`/chapters/${chapter.slug}`}
                      className="block transition hover:-translate-y-0.5"
                    >
                      <Card className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                        <div className="min-w-0">
                          <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                            Branch {chapter.sort_order}
                            {chapter.book_ref ? ` · ${chapter.book_ref}` : ""}
                          </p>
                          <CardTitle className="mt-1">{chapter.title}</CardTitle>
                          {chapter.summary && (
                            <p className="mt-2 line-clamp-2 text-sm text-[var(--ink-soft)]">
                              {chapter.summary}
                            </p>
                          )}
                          <p className="mt-2 text-xs text-[var(--ink-soft)]">
                            {chapter.concept_count > 0
                              ? `${chapter.concept_count} concepts`
                              : "Content coming soon"}
                          </p>
                        </div>
                        <Button className="shrink-0 self-start sm:self-center">
                          Open
                        </Button>
                      </Card>
                    </Link>
                  ))}
                </div>
              )}
            </section>
          ))}
        </div>
      )}
    </div>
  );
}
