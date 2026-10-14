"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import type { GraphPayload } from "@/lib/api";
import { fetchConceptGraph } from "@/lib/api";
import { layoutGraph } from "@/lib/graphLayout";
import { cn } from "@/lib/utils";

export function ConceptGraphView({
  payload,
  compact = false,
}: {
  payload: GraphPayload;
  compact?: boolean;
}) {
  const layout = useMemo(() => layoutGraph(payload), [payload]);

  return (
    <div
      className={cn(
        "relative overflow-auto rounded-md border border-[var(--line)] bg-[#faf7f0]",
        compact ? "h-[360px]" : "h-[560px]",
      )}
    >
      <div
        className="relative"
        style={{ width: layout.width, height: layout.height, minWidth: "100%" }}
      >
        <svg
          className="pointer-events-none absolute inset-0"
          width={layout.width}
          height={layout.height}
        >
          {layout.edges.map((edge) => {
            const from = layout.nodes.find((n) => n.slug === edge.source_slug);
            const to = layout.nodes.find((n) => n.slug === edge.target_slug);
            if (!from || !to) return null;
            return (
              <line
                key={edge.id}
                x1={from.x + 80}
                y1={from.y + 28}
                x2={to.x + 80}
                y2={to.y + 28}
                stroke={edge.relation_type === "parent" ? "#0f5c4c" : "#6b645a"}
                strokeWidth={edge.relation_type === "parent" ? 2 : 1}
              />
            );
          })}
        </svg>
        {layout.nodes.map((node) => (
          <Link
            key={node.slug}
            href={`/concepts/${node.slug}`}
            className={cn(
              "absolute block w-40 rounded-md border px-2 py-2 text-xs transition hover:-translate-y-0.5",
              node.isRoot
                ? "border-[var(--accent)] bg-[var(--accent-soft)] font-semibold shadow-[3px_3px_0_0_#0f5c4c33]"
                : "border-[var(--line)] bg-white",
            )}
            style={{ left: node.x, top: node.y }}
            title={node.summary}
          >
            {node.title}
          </Link>
        ))}
      </div>
    </div>
  );
}

export function RelationGraphBlock({
  title,
  root_slug,
  depth = 2,
}: {
  id: string;
  type: "relation_graph";
  title?: string;
  root_slug: string;
  depth?: number;
}) {
  const [payload, setPayload] = useState<GraphPayload | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetchConceptGraph(root_slug, depth)
      .then((data) => {
        if (!cancelled) setPayload(data);
      })
      .catch(() => {
        if (!cancelled) setError("Could not load graph.");
      });
    return () => {
      cancelled = true;
    };
  }, [root_slug, depth]);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5">
      {title && (
        <h3 className="mb-3 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      {error && (
        <p className="text-sm text-[var(--ink-soft)]">{error}</p>
      )}
      {!error && !payload && (
        <p className="text-sm text-[var(--ink-soft)]">Loading graph…</p>
      )}
      {payload && <ConceptGraphView payload={payload} compact />}
      <Link
        href={`/concepts/${root_slug}/graph`}
        className="mt-3 inline-block text-sm text-[var(--accent)] hover:underline"
      >
        Open full graph →
      </Link>
    </div>
  );
}
