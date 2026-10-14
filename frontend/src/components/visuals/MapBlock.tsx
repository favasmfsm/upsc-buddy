"use client";

import { useState } from "react";
import Link from "next/link";

import type { VisualMapNode, VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type MapBlockProps = Extract<VisualBlock, { type: "map" }>;

export function MapBlock({ title, nodes, edges = [] }: MapBlockProps) {
  const [activeId, setActiveId] = useState<string | null>(nodes[0]?.id ?? null);
  const active: VisualMapNode | undefined = nodes.find((n) => n.id === activeId);
  const nodeIds = new Set(nodes.map((n) => n.id));

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/60 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="grid gap-6 lg:grid-cols-[1fr_240px]">
        <div className="space-y-4">
          <div className="flex flex-wrap gap-3">
            {nodes.map((node) => (
              <button
                key={node.id}
                type="button"
                onMouseEnter={() => setActiveId(node.id)}
                onFocus={() => setActiveId(node.id)}
                onClick={() => setActiveId(node.id)}
                className={cn(
                  "rounded-md border px-3 py-2 text-left text-sm transition",
                  activeId === node.id
                    ? "border-[var(--accent)] bg-[var(--accent-soft)] text-[var(--ink)]"
                    : "border-[var(--line)] bg-[var(--paper)] text-[var(--ink-soft)] hover:border-[var(--accent)]",
                )}
              >
                {node.label}
              </button>
            ))}
          </div>
          {edges.length > 0 && (
            <ul className="space-y-1 text-xs text-[var(--ink-soft)]">
              {edges
                .filter((e) => nodeIds.has(e.from) && nodeIds.has(e.to))
                .map((e) => {
                  const from = nodes.find((n) => n.id === e.from)?.label ?? e.from;
                  const to = nodes.find((n) => n.id === e.to)?.label ?? e.to;
                  return (
                    <li key={`${e.from}-${e.to}`}>
                      {from} → {to}
                    </li>
                  );
                })}
            </ul>
          )}
        </div>
        <aside className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
          {active ? (
            <>
              <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                Detail
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
                  className="mt-3 inline-block text-sm text-[var(--accent)] hover:underline"
                >
                  Open cluster →
                </Link>
              )}
            </>
          ) : (
            <p className="text-sm text-[var(--ink-soft)]">
              Hover or click a node.
            </p>
          )}
        </aside>
      </div>
    </div>
  );
}
