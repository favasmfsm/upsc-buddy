import Link from "next/link";
import { notFound } from "next/navigation";

import { ChapterConceptsWithProgress } from "@/components/ChapterConceptsWithProgress";
import { ChapterProgressSummary } from "@/components/ChapterProgressSummary";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { fetchChapter } from "@/lib/api";

export default async function ChapterDetailPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  let chapter: Awaited<ReturnType<typeof fetchChapter>>;
  try {
    chapter = await fetchChapter(slug);
  } catch {
    notFound();
  }

  const hub = chapter.concepts.find((c) => c.slug === chapter.slug) ?? null;
  const clusters = chapter.concepts.filter((c) => c.slug !== chapter.slug);
  const conceptSlugs = chapter.concepts.map((c) => c.slug);

  return (
    <div className="space-y-10">
      <div className="space-y-4 border-b border-[var(--line)] pb-8">
        <div className="flex flex-wrap gap-2">
          <Badge>{chapter.subject_slug}</Badge>
          <Badge variant="outline">Ch. {chapter.sort_order}</Badge>
        </div>
        <h1 className="font-[family-name:var(--font-display)] text-4xl sm:text-5xl">
          {chapter.title}
        </h1>
        {chapter.book_ref && (
          <p className="text-sm text-[var(--ink-soft)]">{chapter.book_ref}</p>
        )}
        <p className="max-w-2xl text-lg text-[var(--ink-soft)]">
          {chapter.summary}
        </p>
        <ChapterProgressSummary conceptSlugs={conceptSlugs} />
        {hub && (
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center">
            <Link href={`/concepts/${hub.slug}`}>
              <Button>Open chapter overview</Button>
            </Link>
            <p className="text-sm text-[var(--ink-soft)]">
              Start with the chapter overview, then open a feature or cluster
              below.
            </p>
          </div>
        )}
        <div className="flex flex-wrap gap-3">
          <Link href={`/subjects/${chapter.subject_slug}`}>
            <Button variant="outline">All chapters</Button>
          </Link>
        </div>
      </div>

      <ChapterConceptsWithProgress hub={hub} clusters={clusters} />
    </div>
  );
}
