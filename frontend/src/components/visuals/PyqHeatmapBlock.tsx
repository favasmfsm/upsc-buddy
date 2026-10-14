"use client";

import Link from "next/link";

import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type PyqHeatmapBlockProps = Extract<VisualBlock, { type: "pyq_heatmap" }>;

export function PyqHeatmapBlock({ title, items }: PyqHeatmapBlockProps) {
  const max = Math.max(1, ...items.map((item) => item.count ?? 0));

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5 sm:p-6">
      {title && (
        <h3 className="mb-2 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <p className="mb-5 text-sm text-[var(--ink-soft)]">
        Frequency from linked previous-year questions (live counts).
      </p>

      <ul className="space-y-3">
        {items.map((item) => {
          const count = item.count ?? 0;
          const pct = Math.round((count / max) * 100);

          return (
            <li key={item.concept_slug}>
              <div className="mb-1 flex items-baseline justify-between gap-3">
                <Link
                  href={`/concepts/${item.concept_slug}`}
                  className="text-sm font-medium text-[var(--ink)] hover:text-[var(--accent)] hover:underline"
                >
                  {item.label}
                </Link>
                <span className="text-xs tabular-nums text-[var(--ink-soft)]">
                  {count} PYQ{count === 1 ? "" : "s"}
                </span>
              </div>
              <div className="h-2.5 overflow-hidden rounded-sm bg-[var(--paper)]">
                <div
                  className={cn(
                    "h-full rounded-sm bg-[#0f5c4c] transition-all",
                    count === 0 && "bg-[var(--line)]",
                  )}
                  style={{ width: `${count === 0 ? 4 : pct}%` }}
                  role="img"
                  aria-label={`${item.label}: ${count} previous year questions`}
                />
              </div>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
