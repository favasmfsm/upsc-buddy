"use client";

import Link from "next/link";
import { useState } from "react";

import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type JourneyBlockProps = Extract<VisualBlock, { type: "journey" }>;

export function JourneyBlock({ title, stages }: JourneyBlockProps) {
  const [activeId, setActiveId] = useState<string | null>(stages[0]?.id ?? null);
  const active = stages.find((s) => s.id === activeId);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="grid gap-6 lg:grid-cols-[1fr_220px]">
        <ol className="space-y-3">
          {stages.map((stage, index) => (
            <li key={stage.id}>
              <button
                type="button"
                onClick={() => setActiveId(stage.id)}
                onMouseEnter={() => setActiveId(stage.id)}
                className={cn(
                  "flex w-full items-start gap-3 rounded-md border px-3 py-3 text-left transition",
                  activeId === stage.id
                    ? "border-[var(--accent)] bg-[var(--accent-soft)]"
                    : "border-[var(--line)] bg-white hover:border-[var(--accent)]/40",
                )}
              >
                <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-[var(--paper)] text-xs font-semibold text-[var(--ink-soft)]">
                  {index + 1}
                </span>
                <span className="font-medium text-[var(--ink)]">{stage.label}</span>
              </button>
              {index < stages.length - 1 && (
                <div className="ml-6 h-3 w-px bg-[var(--line)]" aria-hidden />
              )}
            </li>
          ))}
        </ol>
        <aside className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
          {active ? (
            <>
              <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                Stage
              </p>
              <p className="mt-1 font-medium text-[var(--ink)]">{active.label}</p>
              {active.detail && (
                <p className="mt-2 text-sm text-[var(--ink-soft)]">
                  {active.detail}
                </p>
              )}
              {active.slug && (
                <Link
                  href={`/concepts/${active.slug}`}
                  className="mt-3 block text-sm text-[var(--accent)] hover:underline"
                >
                  Related concept →
                </Link>
              )}
              {active.case_slug && (
                <p className="mt-2 text-xs text-[var(--ink-soft)]">
                  Case ref: {active.case_slug}
                </p>
              )}
            </>
          ) : (
            <p className="text-sm text-[var(--ink-soft)]">Select a stage.</p>
          )}
        </aside>
      </div>
    </div>
  );
}
