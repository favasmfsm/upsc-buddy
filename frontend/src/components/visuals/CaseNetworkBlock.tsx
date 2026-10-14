"use client";

import { useState } from "react";

import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type CaseNetworkBlockProps = Extract<VisualBlock, { type: "case_network" }>;

export function CaseNetworkBlock({
  title,
  hub_label,
  cases,
}: CaseNetworkBlockProps) {
  const [activeId, setActiveId] = useState<string | null>(cases[0]?.id ?? null);
  const active = cases.find((c) => c.id === activeId);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="grid gap-6 lg:grid-cols-[1fr_220px]">
        <div className="flex flex-col items-center gap-4">
          <div className="rounded-md border-2 border-[var(--accent)] bg-[var(--accent-soft)] px-5 py-3 text-center font-semibold text-[var(--ink)]">
            {hub_label}
          </div>
          <div className="h-4 w-px bg-[var(--line)]" aria-hidden />
          <ul className="grid w-full gap-2 sm:grid-cols-2">
            {cases.map((c) => (
              <li key={c.id}>
                <button
                  type="button"
                  onClick={() => setActiveId(c.id)}
                  onMouseEnter={() => setActiveId(c.id)}
                  className={cn(
                    "w-full rounded-md border px-3 py-2 text-left text-sm transition",
                    activeId === c.id
                      ? "border-[var(--accent)] bg-[var(--accent-soft)]"
                      : "border-[var(--line)] bg-white hover:border-[var(--accent)]/40",
                  )}
                >
                  <span className="font-medium text-[var(--ink)]">{c.label}</span>
                  {c.year != null && (
                    <span className="mt-0.5 block text-xs text-[var(--ink-soft)]">
                      {c.year}
                    </span>
                  )}
                </button>
              </li>
            ))}
          </ul>
        </div>
        <aside className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
          {active ? (
            <>
              <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                Case
              </p>
              <p className="mt-1 font-medium text-[var(--ink)]">{active.label}</p>
              {active.year != null && (
                <p className="text-xs text-[var(--ink-soft)]">{active.year}</p>
              )}
              {active.detail && (
                <p className="mt-2 text-sm text-[var(--ink-soft)]">
                  {active.detail}
                </p>
              )}
              {active.case_slug && (
                <p className="mt-2 text-xs text-[var(--ink-soft)]">
                  Ref: {active.case_slug}
                </p>
              )}
            </>
          ) : (
            <p className="text-sm text-[var(--ink-soft)]">Select a case.</p>
          )}
        </aside>
      </div>
    </div>
  );
}
