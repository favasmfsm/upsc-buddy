import Link from "next/link";

import { ConceptCard } from "@/components/ConceptCard";
import { Input } from "@/components/ui/input";
import { fetchConcepts } from "@/lib/api";

export default async function ConceptsPage({
  searchParams,
}: {
  searchParams: Promise<{ subject?: string; q?: string }>;
}) {
  const params = await searchParams;
  const subject = params.subject || undefined;
  const q = params.q || "";

  let concepts: Awaited<ReturnType<typeof fetchConcepts>>["results"] = [];
  let error: string | null = null;
  let count = 0;

  try {
    const data = await fetchConcepts({ subject, q: q || undefined });
    concepts = data.results;
    count = data.count;
  } catch {
    error = "Could not load concepts.";
  }

  const subjectLabel = subject || "all subjects";
  const chaptersHref = subject ? `/subjects/${subject}` : "/subjects";
  const clearHref = "/concepts";

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-[family-name:var(--font-display)] text-4xl">
          All concepts
        </h1>
        <p className="mt-2 text-[var(--ink-soft)]">
          Secondary browse for {subjectLabel}. Prefer{" "}
          <Link
            href={chaptersHref}
            className="text-[var(--accent)] hover:underline"
          >
            chapters
          </Link>{" "}
          for revision. {count ? `${count} published.` : null}
        </p>
      </div>

      <form className="flex flex-wrap gap-3" action="/concepts" method="get">
        {subject ? <input type="hidden" name="subject" value={subject} /> : null}
        <Input
          name="q"
          defaultValue={q}
          placeholder="Search concepts…"
          className="max-w-md"
        />
        <button
          type="submit"
          className="h-10 rounded-md bg-[var(--accent)] px-4 text-sm font-medium text-white"
        >
          Search
        </button>
      </form>

      {error ? (
        <p className="text-sm text-[var(--accent)]">{error}</p>
      ) : concepts.length === 0 ? (
        <p className="text-sm text-[var(--ink-soft)]">
          No concepts found.{" "}
          <Link href={clearHref} className="text-[var(--accent)]">
            Clear search
          </Link>
        </p>
      ) : (
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {concepts.map((concept) => (
            <ConceptCard key={concept.id} concept={concept} />
          ))}
        </div>
      )}
    </div>
  );
}
