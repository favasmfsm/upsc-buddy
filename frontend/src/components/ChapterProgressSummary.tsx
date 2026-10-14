"use client";

import { useQuery } from "@tanstack/react-query";
import { useEffect, useMemo, useState } from "react";

import {
  apiAuthGet,
  ensureAccessToken,
  type ProgressItem,
} from "@/lib/api";
import { isLoggedIn } from "@/lib/auth";

export function ChapterProgressSummary({
  conceptSlugs,
}: {
  conceptSlugs: string[];
}) {
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

  const stats = useMemo(() => {
    const total = conceptSlugs.length;
    if (total === 0) {
      return { total: 0, studied: 0, reviseLater: 0, difficult: 0, remaining: 0 };
    }
    const slugSet = new Set(conceptSlugs);
    const items = (progressQuery.data || []).filter((p) =>
      slugSet.has(p.concept_slug),
    );
    const studied = items.filter((p) => p.status === "studied").length;
    const reviseLater = items.filter((p) => p.status === "revise_later").length;
    const difficult = items.filter((p) => p.is_difficult).length;
    const remaining = Math.max(0, total - studied - reviseLater);
    return { total, studied, reviseLater, difficult, remaining };
  }, [conceptSlugs, progressQuery.data]);

  if (!token || conceptSlugs.length === 0) return null;
  if (progressQuery.isLoading) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">Loading progress…</p>
    );
  }
  if (progressQuery.isError) return null;

  return (
    <p className="text-sm text-[var(--ink-soft)]">
      <span className="font-medium text-[var(--ink)]">
        {stats.studied} of {stats.total} studied
      </span>
      {stats.reviseLater > 0 && (
        <>
          <span className="mx-1.5 text-[var(--line)]">·</span>
          <span className="text-[var(--revise)]">
            {stats.reviseLater} revise later
          </span>
        </>
      )}
      {stats.difficult > 0 && (
        <>
          <span className="mx-1.5 text-[var(--line)]">·</span>
          <span className="text-[var(--difficult)]">
            {stats.difficult} difficult
          </span>
        </>
      )}
      {stats.remaining > 0 && (
        <>
          <span className="mx-1.5 text-[var(--line)]">·</span>
          {stats.remaining} remaining
        </>
      )}
    </p>
  );
}
