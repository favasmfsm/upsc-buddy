"use client";

import { useState } from "react";

import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type TimelineBlockProps = Extract<VisualBlock, { type: "timeline" }>;

export function TimelineBlock({ title, events }: TimelineBlockProps) {
  const [activeId, setActiveId] = useState<string | null>(events[0]?.id ?? null);
  const active = events.find((e) => e.id === activeId);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="grid gap-6 lg:grid-cols-[1fr_220px]">
        <ol className="space-y-0">
          {events.map((event, index) => (
            <li key={event.id} className="relative flex gap-3 pb-5 last:pb-0">
              {index < events.length - 1 && (
                <span
                  className="absolute left-[15px] top-8 h-[calc(100%-1.5rem)] w-px bg-[var(--line)]"
                  aria-hidden
                />
              )}
              <button
                type="button"
                onClick={() => setActiveId(event.id)}
                onMouseEnter={() => setActiveId(event.id)}
                className={cn(
                  "relative z-[1] flex h-8 w-8 shrink-0 items-center justify-center rounded-full border text-[10px] font-semibold",
                  activeId === event.id
                    ? "border-[var(--accent)] bg-[var(--accent)] text-white"
                    : "border-[var(--line)] bg-white text-[var(--ink-soft)]",
                )}
              >
                {String(event.year).slice(-2)}
              </button>
              <button
                type="button"
                onClick={() => setActiveId(event.id)}
                onMouseEnter={() => setActiveId(event.id)}
                className={cn(
                  "flex-1 rounded-md border px-3 py-2 text-left text-sm transition",
                  activeId === event.id
                    ? "border-[var(--accent)] bg-[var(--accent-soft)]"
                    : "border-transparent hover:border-[var(--line)]",
                )}
              >
                <span className="text-xs text-[var(--ink-soft)]">{event.year}</span>
                <span className="mt-0.5 block font-medium">{event.label}</span>
              </button>
            </li>
          ))}
        </ol>
        <aside className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
          {active ? (
            <>
              <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                {active.year}
              </p>
              <p className="mt-1 font-medium text-[var(--ink)]">{active.label}</p>
              {active.detail && (
                <p className="mt-2 text-sm text-[var(--ink-soft)]">
                  {active.detail}
                </p>
              )}
            </>
          ) : (
            <p className="text-sm text-[var(--ink-soft)]">Select an event.</p>
          )}
        </aside>
      </div>
    </div>
  );
}
