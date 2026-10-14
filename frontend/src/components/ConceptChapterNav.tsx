import Link from "next/link";

import { Button } from "@/components/ui/button";

export type ChapterNavConcept = {
  slug: string;
  title: string;
  sort_order: number;
};

export function ConceptChapterNav({
  chapterTitle,
  chapterSlug,
  concepts,
  currentSlug,
}: {
  chapterTitle: string;
  chapterSlug: string;
  concepts: ChapterNavConcept[];
  currentSlug: string;
}) {
  const ordered = [...concepts].sort((a, b) => a.sort_order - b.sort_order);
  const index = ordered.findIndex((c) => c.slug === currentSlug);
  if (index < 0 || ordered.length === 0) return null;

  const prev = index > 0 ? ordered[index - 1] : null;
  const next = index < ordered.length - 1 ? ordered[index + 1] : null;

  return (
    <div className="flex flex-col gap-3 border-b border-[var(--line)] pb-6 sm:flex-row sm:items-center sm:justify-between">
      <p className="text-sm text-[var(--ink-soft)]">
        Concept {index + 1} of {ordered.length}
        <span className="mx-1.5 text-[var(--line)]">·</span>
        <Link
          href={`/chapters/${chapterSlug}`}
          className="text-[var(--accent)] hover:underline"
        >
          {chapterTitle}
        </Link>
      </p>
      <div className="flex flex-wrap gap-2">
        {prev ? (
          <Link href={`/concepts/${prev.slug}`}>
            <Button size="sm" variant="outline">
              ← {prev.title}
            </Button>
          </Link>
        ) : (
          <Button size="sm" variant="outline" disabled>
            ← Previous
          </Button>
        )}
        {next ? (
          <Link href={`/concepts/${next.slug}`}>
            <Button size="sm" variant="secondary">
              {next.title} →
            </Button>
          </Link>
        ) : (
          <Button size="sm" variant="secondary" disabled>
            Next →
          </Button>
        )}
      </div>
    </div>
  );
}
