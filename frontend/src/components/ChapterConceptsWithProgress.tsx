"use client";

import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import { progressCardToneClass } from "@/components/ProgressStatusBadges";
import { Button } from "@/components/ui/button";
import { Card, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import {
  apiAuthGet,
  ensureAccessToken,
  type ChapterConcept,
  type ProgressItem,
} from "@/lib/api";
import { isLoggedIn } from "@/lib/auth";

type ProgressFilter =
  | "all"
  | "studied"
  | "revise_later"
  | "difficult"
  | "not_started";

const FILTERS: { id: ProgressFilter; label: string }[] = [
  { id: "all", label: "All" },
  { id: "studied", label: "Studied" },
  { id: "revise_later", label: "Revise later" },
  { id: "difficult", label: "Difficult" },
  { id: "not_started", label: "Not started" },
];

function useProgressBySlug(conceptSlugs: string[]) {
  const [token, setToken] = useState<string | null>(null);

  useEffect(() => {
    if (!isLoggedIn()) return;
    ensureAccessToken().then((access) => {
      if (access) setToken(access);
    });
  }, []);

  const progressQuery = useQuery({
    queryKey: ["progress"],
    enabled: Boolean(token) && conceptSlugs.length > 0,
    queryFn: () =>
      apiAuthGet<ProgressItem[]>("/api/learning/progress/", token!),
  });

  const bySlug = useMemo(() => {
    const map = new Map<string, ProgressItem>();
    const slugSet = new Set(conceptSlugs);
    for (const item of progressQuery.data || []) {
      if (slugSet.has(item.concept_slug)) {
        map.set(item.concept_slug, item);
      }
    }
    return map;
  }, [conceptSlugs, progressQuery.data]);

  return { bySlug, isLoggedIn: Boolean(token) };
}

function matchesFilter(
  progress: ProgressItem | undefined,
  filter: ProgressFilter,
): boolean {
  if (filter === "all") return true;
  if (filter === "difficult") return Boolean(progress?.is_difficult);
  if (filter === "studied") return progress?.status === "studied";
  if (filter === "revise_later") return progress?.status === "revise_later";
  // not_started: no row, or explicitly not_started, and not only-difficult tracked
  const status = progress?.status ?? "not_started";
  return status === "not_started";
}

function filterActiveClass(filter: ProgressFilter, active: boolean): string {
  if (!active) return "";
  if (filter === "studied") {
    return "border-[var(--studied)] bg-[var(--studied-soft)] text-[var(--studied)]";
  }
  if (filter === "revise_later") {
    return "border-[var(--revise)] bg-[var(--revise-soft)] text-[var(--revise)]";
  }
  if (filter === "difficult") {
    return "border-[var(--difficult)] bg-[var(--difficult-soft)] text-[var(--difficult)]";
  }
  return "";
}

function ConceptTile({
  concept,
  progress,
  eyebrow,
}: {
  concept: ChapterConcept;
  progress?: ProgressItem;
  eyebrow: string;
}) {
  const tone = progressCardToneClass(progress?.status, progress?.is_difficult);
  return (
    <Link
      href={`/concepts/${concept.slug}`}
      className="block transition hover:-translate-y-0.5"
    >
      <Card className={cn("h-full", tone)}>
        <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
          {eyebrow}
        </p>
        <CardTitle className="mt-1 text-lg">{concept.title}</CardTitle>
        <p className="mt-2 line-clamp-3 text-sm text-[var(--ink-soft)]">
          {concept.summary}
        </p>
      </Card>
    </Link>
  );
}

export function ChapterConceptsWithProgress({
  hub,
  clusters,
}: {
  hub: ChapterConcept | null;
  clusters: ChapterConcept[];
}) {
  const [filter, setFilter] = useState<ProgressFilter>("all");
  const allConcepts = useMemo(
    () => (hub ? [hub, ...clusters] : clusters),
    [hub, clusters],
  );
  const slugs = useMemo(() => allConcepts.map((c) => c.slug), [allConcepts]);
  const { bySlug, isLoggedIn: loggedIn } = useProgressBySlug(slugs);

  const counts = useMemo(() => {
    const result: Record<ProgressFilter, number> = {
      all: allConcepts.length,
      studied: 0,
      revise_later: 0,
      difficult: 0,
      not_started: 0,
    };
    for (const concept of allConcepts) {
      const progress = bySlug.get(concept.slug);
      if (progress?.status === "studied") result.studied += 1;
      if (progress?.status === "revise_later") result.revise_later += 1;
      if (progress?.is_difficult) result.difficult += 1;
      if ((progress?.status ?? "not_started") === "not_started") {
        result.not_started += 1;
      }
    }
    return result;
  }, [allConcepts, bySlug]);

  const showHub =
    hub && matchesFilter(bySlug.get(hub.slug), filter);
  const filteredClusters = clusters.filter((c) =>
    matchesFilter(bySlug.get(c.slug), filter),
  );

  if (allConcepts.length === 0) {
    return <p className="text-[var(--ink-soft)]">Content coming soon.</p>;
  }

  return (
    <div className="space-y-8">
      {loggedIn && (
        <div
          className="flex flex-wrap gap-2"
          role="group"
          aria-label="Filter by progress"
        >
          {FILTERS.map((item) => {
            const active = filter === item.id;
            return (
              <Button
                key={item.id}
                type="button"
                size="sm"
                variant="outline"
                aria-pressed={active}
                className={cn(
                  active && item.id === "all" && "border-[var(--accent)] bg-[var(--accent-soft)] text-[var(--accent)]",
                  filterActiveClass(item.id, active),
                )}
                onClick={() => setFilter(item.id)}
              >
                {item.label}
                <span className="tabular-nums opacity-70">{counts[item.id]}</span>
              </Button>
            );
          })}
        </div>
      )}

      {showHub && hub && (
        <section>
          <p className="mb-3 text-xs uppercase tracking-wide text-[var(--ink-soft)]">
            Chapter hub
          </p>
          <ConceptTile
            concept={hub}
            progress={bySlug.get(hub.slug)}
            eyebrow="Overview"
          />
        </section>
      )}

      {filteredClusters.length > 0 ? (
        <section>
          <h2 className="mb-2 font-[family-name:var(--font-display)] text-2xl">
            Clusters
          </h2>
          <p className="mb-4 text-sm text-[var(--ink-soft)]">
            Deep dives under this chapter — open after the overview.
          </p>
          <div className="grid gap-4 sm:grid-cols-2">
            {filteredClusters.map((concept) => (
              <ConceptTile
                key={concept.id}
                concept={concept}
                progress={bySlug.get(concept.slug)}
                eyebrow={String(concept.sort_order).padStart(2, "0")}
              />
            ))}
          </div>
        </section>
      ) : !showHub ? (
        <p className="text-sm text-[var(--ink-soft)]">
          No concepts match this filter.
        </p>
      ) : null}
    </div>
  );
}

/** @deprecated Prefer ChapterConceptsWithProgress */
export function ChapterHubWithProgress({ hub }: { hub: ChapterConcept }) {
  return <ChapterConceptsWithProgress hub={hub} clusters={[]} />;
}

/** @deprecated Prefer ChapterConceptsWithProgress */
export function ChapterClustersWithProgress({
  clusters,
}: {
  clusters: ChapterConcept[];
}) {
  return <ChapterConceptsWithProgress hub={null} clusters={clusters} />;
}
