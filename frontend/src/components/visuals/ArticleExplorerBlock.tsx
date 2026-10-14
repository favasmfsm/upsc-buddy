"use client";

import { useState } from "react";

import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type ArticleExplorerBlockProps = Extract<
  VisualBlock,
  { type: "article_explorer" }
>;

export function ArticleExplorerBlock({
  title,
  article_ref,
  stages,
}: ArticleExplorerBlockProps) {
  const [activeId, setActiveId] = useState<string | null>(stages[0]?.id ?? null);
  const active = stages.find((s) => s.id === activeId);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5">
      {title && (
        <h3 className="mb-1 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <p className="mb-4 text-sm text-[var(--ink-soft)]">{article_ref}</p>

      <div className="flex flex-wrap gap-2 border-b border-[var(--line)] pb-3">
        {stages.map((stage) => (
          <button
            key={stage.id}
            type="button"
            onClick={() => setActiveId(stage.id)}
            className={cn(
              "rounded-md border px-3 py-1.5 text-sm transition",
              activeId === stage.id
                ? "border-[var(--accent)] bg-[var(--accent)] text-white"
                : "border-[var(--line)] bg-white text-[var(--ink-soft)] hover:border-[var(--accent)]/40",
            )}
          >
            {stage.label}
          </button>
        ))}
      </div>

      <div className="mt-4 rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
        {active ? (
          <>
            <p className="font-medium text-[var(--ink)]">{active.label}</p>
            {active.detail && (
              <p className="mt-2 text-sm text-[var(--ink-soft)]">{active.detail}</p>
            )}
          </>
        ) : (
          <p className="text-sm text-[var(--ink-soft)]">Select a stage.</p>
        )}
      </div>
    </div>
  );
}
