"use client";

import { useState } from "react";

import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type MemoryPalaceBlockProps = Extract<VisualBlock, { type: "memory_palace" }>;

export function MemoryPalaceBlock({
  title,
  setting,
  loci,
}: MemoryPalaceBlockProps) {
  const [index, setIndex] = useState(0);
  const locus = loci[index];

  return (
    <div className="rounded-lg border border-[var(--line)] bg-gradient-to-b from-[#f7f1e6] to-white/80 p-5 sm:p-6">
      {title && (
        <h3 className="mb-1 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <p className="mb-5 text-sm text-[var(--ink-soft)]">Setting: {setting}</p>

      {locus && (
        <div className="rounded-md border border-[var(--line)] bg-white/80 p-5">
          <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
            Locus {index + 1} of {loci.length}
          </p>
          <p className="mt-2 font-[family-name:var(--font-display)] text-2xl text-[var(--ink)]">
            {locus.place}
          </p>
          <p className="mt-3 text-sm font-semibold text-[var(--accent)]">
            → {locus.association}
          </p>
          {locus.detail && (
            <p className="mt-3 text-sm text-[var(--ink-soft)]">{locus.detail}</p>
          )}
        </div>
      )}

      <div className="mt-4 flex flex-wrap gap-2">
        <button
          type="button"
          disabled={index === 0}
          onClick={() => setIndex((i) => Math.max(0, i - 1))}
          className={cn(
            "rounded-md border border-[var(--line)] px-3 py-1.5 text-sm",
            index === 0
              ? "cursor-not-allowed opacity-40"
              : "hover:border-[var(--accent)]",
          )}
        >
          Previous
        </button>
        <button
          type="button"
          disabled={index >= loci.length - 1}
          onClick={() => setIndex((i) => Math.min(loci.length - 1, i + 1))}
          className={cn(
            "rounded-md border border-[var(--line)] px-3 py-1.5 text-sm",
            index >= loci.length - 1
              ? "cursor-not-allowed opacity-40"
              : "hover:border-[var(--accent)]",
          )}
        >
          Next locus
        </button>
      </div>
    </div>
  );
}
