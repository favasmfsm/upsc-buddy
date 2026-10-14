"use client";

import Link from "next/link";
import { useState } from "react";

import type { CategorySpineTone, VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type PillarsBlockProps = Extract<VisualBlock, { type: "pillars" }>;

const TONE_STYLES: Record<
  CategorySpineTone,
  { bar: string; ring: string; soft: string }
> = {
  teal: {
    bar: "bg-[#2a7a6e]",
    ring: "ring-[#2a7a6e]",
    soft: "bg-[#2a7a6e]/10",
  },
  olive: {
    bar: "bg-[#6b7a3a]",
    ring: "ring-[#6b7a3a]",
    soft: "bg-[#6b7a3a]/10",
  },
  gold: {
    bar: "bg-[#c4a035]",
    ring: "ring-[#c4a035]",
    soft: "bg-[#c4a035]/10",
  },
  orange: {
    bar: "bg-[#d4782e]",
    ring: "ring-[#d4782e]",
    soft: "bg-[#d4782e]/10",
  },
  terracotta: {
    bar: "bg-[#b85a3a]",
    ring: "ring-[#b85a3a]",
    soft: "bg-[#b85a3a]/10",
  },
  maroon: {
    bar: "bg-[#8b3a3a]",
    ring: "ring-[#8b3a3a]",
    soft: "bg-[#8b3a3a]/10",
  },
};

export function PillarsBlock({ title, items }: PillarsBlockProps) {
  const [expandedId, setExpandedId] = useState<string | null>(null);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5 sm:p-6">
      {title && (
        <h3 className="mb-2 text-center font-[family-name:var(--font-display)] text-xl sm:text-2xl">
          {title}
        </h3>
      )}
      <p className="mb-6 text-center text-sm text-[var(--ink-soft)]">
        Click a pillar to expand
      </p>

      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {items.map((item) => {
          const tone = TONE_STYLES[item.tone] ?? TONE_STYLES.teal;
          const isOpen = expandedId === item.id;

          return (
            <div
              key={item.id}
              className={cn(
                "overflow-hidden rounded-md border border-[var(--line)] bg-white transition",
                isOpen && `ring-1 ${tone.ring}`,
              )}
            >
              <button
                type="button"
                onClick={() =>
                  setExpandedId((prev) => (prev === item.id ? null : item.id))
                }
                className="flex w-full items-stretch text-left"
              >
                <span className={cn("w-1.5 shrink-0", tone.bar)} aria-hidden />
                <span className="flex flex-1 flex-col gap-1 px-4 py-3">
                  <span className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                    {item.articles}
                  </span>
                  <span className="font-semibold text-[var(--ink)]">
                    {item.label}
                  </span>
                </span>
              </button>

              {isOpen && (
                <div className={cn("border-t border-[var(--line)] px-4 py-3", tone.soft)}>
                  {item.detail && (
                    <p className="text-sm text-[var(--ink-soft)]">{item.detail}</p>
                  )}
                  <Link
                    href={`/concepts/${item.slug}`}
                    className="mt-3 inline-block text-sm text-[var(--accent)] hover:underline"
                  >
                    Open cluster →
                  </Link>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
