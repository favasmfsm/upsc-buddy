"use client";

import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useMemo, useState } from "react";

import { ConceptCard } from "@/components/ConceptCard";
import { progressCardToneClass } from "@/components/ProgressStatusBadges";
import { Button } from "@/components/ui/button";
import { Card, CardTitle } from "@/components/ui/card";
import {
  apiAuthGet,
  ensureAccessToken,
  type ConceptListItem,
  type ProgressItem,
} from "@/lib/api";
import { isLoggedIn } from "@/lib/auth";
import { cn } from "@/lib/utils";

export default function ProgressPage() {
  const router = useRouter();
  const [token, setToken] = useState<string | null>(null);

  useEffect(() => {
    if (!isLoggedIn()) {
      router.replace("/login?next=/progress");
      return;
    }
    ensureAccessToken().then((access) => {
      if (!access) {
        router.replace("/login?next=/progress");
        return;
      }
      setToken(access);
    });
  }, [router]);

  const progressQuery = useQuery({
    queryKey: ["progress"],
    enabled: Boolean(token),
    queryFn: () => apiAuthGet<ProgressItem[]>("/api/learning/progress/", token!),
  });

  const reviseQuery = useQuery({
    queryKey: ["revise-next"],
    enabled: Boolean(token),
    queryFn: () =>
      apiAuthGet<ConceptListItem[]>("/api/learning/revise-next/", token!),
  });

  const summary = useMemo(() => {
    const items = progressQuery.data || [];
    const studied = items.filter((p) => p.status === "studied").length;
    const reviseLater = items.filter((p) => p.status === "revise_later").length;
    const difficult = items.filter((p) => p.is_difficult).length;
    const upNext = (reviseQuery.data || []).length;
    return { studied, reviseLater, difficult, upNext };
  }, [progressQuery.data, reviseQuery.data]);

  const firstRevise = (reviseQuery.data || [])[0] ?? null;

  if (!token) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">Redirecting to login…</p>
    );
  }

  return (
    <div className="space-y-10">
      <div>
        <h1 className="font-[family-name:var(--font-display)] text-4xl">
          Your progress
        </h1>
        <p className="mt-2 text-[var(--ink-soft)]">
          Revise later items first, then concepts you have not started.
        </p>
      </div>

      <section className="flex flex-col gap-4 rounded-lg border border-[var(--line)] bg-white/60 px-5 py-4 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex flex-wrap gap-x-5 gap-y-2 text-sm text-[var(--ink-soft)]">
          <span>
            <span className="font-medium text-[var(--studied)]">
              {summary.studied}
            </span>{" "}
            studied
          </span>
          <span>
            <span className="font-medium text-[var(--revise)]">
              {summary.reviseLater}
            </span>{" "}
            revise later
          </span>
          <span>
            <span className="font-medium text-[var(--difficult)]">
              {summary.difficult}
            </span>{" "}
            difficult
          </span>
          <span>
            <span className="font-medium text-[var(--ink)]">
              {summary.upNext}
            </span>{" "}
            up next
          </span>
        </div>
        {firstRevise ? (
          <Link href={`/concepts/${firstRevise.slug}`}>
            <Button>Start revise session</Button>
          </Link>
        ) : (
          <Button disabled>Start revise session</Button>
        )}
      </section>

      <section className="space-y-4">
        <h2 className="font-[family-name:var(--font-display)] text-2xl">
          Revise next
        </h2>
        {reviseQuery.isLoading && (
          <p className="text-sm text-[var(--ink-soft)]">Loading…</p>
        )}
        {reviseQuery.isError && (
          <p className="text-sm text-[var(--accent)]">Could not load revise list.</p>
        )}
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {(reviseQuery.data || []).map((concept) => (
            <ConceptCard key={concept.id} concept={concept} />
          ))}
        </div>
      </section>

      <section className="space-y-4">
        <h2 className="font-[family-name:var(--font-display)] text-2xl">
          Tracked concepts
        </h2>
        {progressQuery.isLoading && (
          <p className="text-sm text-[var(--ink-soft)]">Loading…</p>
        )}
        {(progressQuery.data || []).length === 0 && !progressQuery.isLoading && (
          <Card>
            <CardTitle className="text-lg">Nothing tracked yet</CardTitle>
            <p className="mt-2 text-sm text-[var(--ink-soft)]">
              Open{" "}
              <Link
                href="/chapters/fundamental-rights"
                className="text-[var(--accent)]"
              >
                Fundamental Rights
              </Link>{" "}
              and mark concepts studied, revise later, or difficult.
            </p>
          </Card>
        )}
        <ul className="space-y-3">
          {(progressQuery.data || []).map((item) => (
            <li key={item.id}>
              <Link
                href={`/concepts/${item.concept_slug}`}
                className={cn(
                  "flex items-center justify-between gap-3 rounded-lg border border-[var(--line)] bg-white/70 px-4 py-3 transition hover:opacity-90",
                  progressCardToneClass(item.status, item.is_difficult),
                )}
              >
                <span className="font-medium">{item.concept_title}</span>
              </Link>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
