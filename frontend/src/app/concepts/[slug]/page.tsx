import Link from "next/link";
import { notFound } from "next/navigation";

import { ConceptChapterNav } from "@/components/ConceptChapterNav";
import { ConceptToc, type TocSection } from "@/components/ConceptToc";
import { MarkdownBody } from "@/components/MarkdownBody";
import { ProgressActions } from "@/components/ProgressActions";
import { RecordLastConcept } from "@/components/RecordLastConcept";
import { VisualBlocks } from "@/components/visuals/VisualBlocks";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardTitle } from "@/components/ui/card";
import { fetchChapter, fetchConcept } from "@/lib/api";

export default async function ConceptDetailPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  let concept: Awaited<ReturnType<typeof fetchConcept>>;
  try {
    concept = await fetchConcept(slug);
  } catch {
    notFound();
  }

  const hasVisuals = (concept.visual_blocks?.length ?? 0) > 0;
  const caseLaws = concept.case_laws ?? [];
  const amendments = concept.amendments ?? [];
  const showArticlesSection = concept.articles.length > 0 && !hasVisuals;

  let chapterConcepts: {
    slug: string;
    title: string;
    sort_order: number;
  }[] = [];
  let chapterTitle = concept.chapter_title ?? "";
  if (concept.chapter_slug) {
    try {
      const chapter = await fetchChapter(concept.chapter_slug);
      chapterTitle = chapter.title;
      chapterConcepts = chapter.concepts.map((c) => ({
        slug: c.slug,
        title: c.title,
        sort_order: c.sort_order,
      }));
    } catch {
      /* nav optional */
    }
  }

  const ordered = [...chapterConcepts].sort(
    (a, b) => a.sort_order - b.sort_order,
  );
  const currentIndex = ordered.findIndex((c) => c.slug === concept.slug);
  const nextConcept =
    currentIndex >= 0 && currentIndex < ordered.length - 1
      ? ordered[currentIndex + 1]
      : null;

  const tocSections: TocSection[] = [];
  if (hasVisuals) tocSections.push({ id: "visuals", label: "Visuals" });
  if (concept.body) tocSections.push({ id: "notes", label: "Notes" });
  if (showArticlesSection)
    tocSections.push({ id: "articles", label: "Articles" });
  if (caseLaws.length > 0) tocSections.push({ id: "cases", label: "Cases" });
  if (amendments.length > 0)
    tocSections.push({ id: "amendments", label: "Amendments" });
  if (concept.pyqs.length > 0) tocSections.push({ id: "pyqs", label: "PYQs" });

  return (
    <div className="space-y-10">
      <RecordLastConcept
        slug={concept.slug}
        title={concept.title}
        chapterSlug={concept.chapter_slug}
      />

      <div className="space-y-4 border-b border-[var(--line)] pb-8">
        <div className="flex flex-wrap gap-2">
          <Badge>{concept.subject_slug}</Badge>
          {concept.chapter_slug && (
            <Link href={`/chapters/${concept.chapter_slug}`}>
              <Badge variant="outline">
                {concept.chapter_title ?? concept.chapter_slug}
              </Badge>
            </Link>
          )}
          {concept.articles.map((a) => (
            <Badge key={a.id} variant="outline">
              {a.ref}
            </Badge>
          ))}
        </div>
        <h1 className="font-[family-name:var(--font-display)] text-4xl sm:text-5xl">
          {concept.title}
        </h1>
        <p className="max-w-2xl text-lg text-[var(--ink-soft)]">
          {concept.summary}
        </p>
        <div className="flex flex-wrap gap-3">
          {concept.chapter_slug ? (
            <Link href={`/chapters/${concept.chapter_slug}`}>
              <Button variant="outline">Back to chapter</Button>
            </Link>
          ) : (
            <Link href={`/subjects/${concept.subject_slug}`}>
              <Button variant="outline">Chapters</Button>
            </Link>
          )}
        </div>
      </div>

      {concept.chapter_slug && chapterConcepts.length > 0 && (
        <ConceptChapterNav
          chapterTitle={chapterTitle}
          chapterSlug={concept.chapter_slug}
          concepts={chapterConcepts}
          currentSlug={concept.slug}
        />
      )}

      {tocSections.length > 0 && (
        <div className="lg:hidden">
          <ConceptToc sections={tocSections} />
        </div>
      )}

      <div className="grid gap-10 lg:grid-cols-[1fr_280px]">
        <div className="space-y-8">
          {hasVisuals && (
            <section id="visuals" className="scroll-mt-28">
              <VisualBlocks blocks={concept.visual_blocks} />
            </section>
          )}

          {concept.body && (
            <details
              id="notes"
              className="scroll-mt-28 rounded-lg border border-[var(--line)] bg-white/60 px-5 py-4"
            >
              <summary className="cursor-pointer font-[family-name:var(--font-display)] text-xl text-[var(--ink)]">
                Notes
              </summary>
              <div className="mt-4 border-t border-[var(--line)] pt-4">
                <MarkdownBody content={concept.body} />
              </div>
            </details>
          )}

          {!hasVisuals && !concept.body && (
            <MarkdownBody content={concept.summary} />
          )}

          {showArticlesSection && (
            <section id="articles" className="scroll-mt-28">
              <h2 className="mb-4 font-[family-name:var(--font-display)] text-2xl">
                Constitutional references
              </h2>
              <div className="space-y-3">
                {concept.articles.map((article) => (
                  <Card key={article.id}>
                    <CardTitle className="text-lg">{article.ref}</CardTitle>
                    {article.excerpt && (
                      <p className="mt-2 text-sm text-[var(--ink-soft)]">
                        {article.excerpt}
                      </p>
                    )}
                  </Card>
                ))}
              </div>
            </section>
          )}

          {caseLaws.length > 0 && (
            <section id="cases" className="scroll-mt-28">
              <h2 className="mb-4 font-[family-name:var(--font-display)] text-2xl">
                Landmark cases
              </h2>
              <div className="space-y-3">
                {caseLaws.map((c) => (
                  <Card key={c.id}>
                    <div className="flex flex-wrap items-center gap-2">
                      <CardTitle className="text-lg">{c.title}</CardTitle>
                      <Badge variant="muted">{c.year}</Badge>
                      <Badge variant="outline">{c.court.toUpperCase()}</Badge>
                    </div>
                    {c.holding && (
                      <p className="mt-2 text-sm text-[var(--ink)]">{c.holding}</p>
                    )}
                    {c.summary && (
                      <p className="mt-2 text-sm text-[var(--ink-soft)]">
                        {c.summary}
                      </p>
                    )}
                  </Card>
                ))}
              </div>
            </section>
          )}

          {amendments.length > 0 && (
            <section id="amendments" className="scroll-mt-28">
              <h2 className="mb-4 font-[family-name:var(--font-display)] text-2xl">
                Amendments
              </h2>
              <div className="space-y-3">
                {amendments.map((a) => (
                  <Card key={a.id}>
                    <div className="flex flex-wrap items-center gap-2">
                      <CardTitle className="text-lg">
                        {a.number}
                        {a.number === 1
                          ? "st"
                          : a.number === 2
                            ? "nd"
                            : a.number === 3
                              ? "rd"
                              : "th"}{" "}
                        Amendment — {a.title}
                      </CardTitle>
                      <Badge variant="muted">{a.year}</Badge>
                    </div>
                    {a.effect && (
                      <p className="mt-2 text-sm text-[var(--ink)]">{a.effect}</p>
                    )}
                    {a.summary && (
                      <p className="mt-2 text-sm text-[var(--ink-soft)]">
                        {a.summary}
                      </p>
                    )}
                  </Card>
                ))}
              </div>
            </section>
          )}

          {concept.pyqs.length > 0 && (
            <section id="pyqs" className="scroll-mt-28">
              <h2 className="mb-4 font-[family-name:var(--font-display)] text-2xl">
                Previous year questions
              </h2>
              <div className="space-y-4">
                {concept.pyqs.map((pyq) => (
                  <Card key={pyq.id}>
                    <Badge variant="muted">{pyq.year}</Badge>
                    <p className="mt-3 text-[var(--ink)]">{pyq.question}</p>
                    {pyq.answer_key && (
                      <p className="mt-2 text-sm text-[var(--ink-soft)]">
                        <span className="font-medium text-[var(--ink)]">
                          Hint:{" "}
                        </span>
                        {pyq.answer_key}
                      </p>
                    )}
                  </Card>
                ))}
              </div>
            </section>
          )}
        </div>

        <aside className="space-y-6">
          {tocSections.length > 0 && (
            <Card className="hidden lg:block">
              <CardTitle className="text-lg">On this page</CardTitle>
              <div className="mt-3">
                <ConceptToc sections={tocSections} />
              </div>
            </Card>
          )}

          <Card>
            <CardTitle className="text-lg">Your progress</CardTitle>
            <div className="mt-4">
              <ProgressActions
                conceptSlug={concept.slug}
                nextConcept={
                  nextConcept
                    ? { slug: nextConcept.slug, title: nextConcept.title }
                    : null
                }
              />
            </div>
          </Card>

          <Card>
            <CardTitle className="text-lg">Related concepts</CardTitle>
            <ul className="mt-4 space-y-3">
              {concept.related.map((edge) => (
                <li key={edge.id}>
                  <Link
                    href={`/concepts/${edge.target.slug}`}
                    className="group block"
                  >
                    <span className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                      {edge.relation_type}
                    </span>
                    <span className="block font-medium text-[var(--accent)] group-hover:underline">
                      {edge.target.title}
                    </span>
                  </Link>
                </li>
              ))}
              {concept.related.length === 0 && (
                <li className="text-sm text-[var(--ink-soft)]">No links yet.</li>
              )}
            </ul>
          </Card>
        </aside>
      </div>
    </div>
  );
}
