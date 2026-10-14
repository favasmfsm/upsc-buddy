"use client";

import Link from "next/link";
import { useState } from "react";

import type { TreeNode, VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type TreeBlockProps = Extract<VisualBlock, { type: "tree" }>;

function TreeBranch({
  node,
  depth,
  activeId,
  onSelect,
}: {
  node: TreeNode;
  depth: number;
  activeId: string | null;
  onSelect: (n: TreeNode) => void;
}) {
  const [open, setOpen] = useState(depth < 2);
  const hasKids = (node.children?.length ?? 0) > 0;
  const isActive = activeId === node.id;

  return (
    <li className={cn(depth > 0 && "ml-4 border-l border-[var(--line)] pl-3")}>
      <div className="flex items-start gap-2 py-1">
        {hasKids ? (
          <button
            type="button"
            onClick={() => setOpen((v) => !v)}
            className="mt-0.5 h-5 w-5 shrink-0 rounded border border-[var(--line)] text-xs text-[var(--ink-soft)]"
            aria-label={open ? "Collapse" : "Expand"}
          >
            {open ? "−" : "+"}
          </button>
        ) : (
          <span className="mt-0.5 h-5 w-5 shrink-0" aria-hidden />
        )}
        <button
          type="button"
          onClick={() => onSelect(node)}
          className={cn(
            "flex-1 rounded-md border px-2 py-1.5 text-left text-sm transition",
            isActive
              ? "border-[var(--accent)] bg-[var(--accent-soft)]"
              : "border-transparent hover:border-[var(--line)]",
          )}
        >
          {node.label}
        </button>
      </div>
      {hasKids && open && (
        <ul>
          {node.children!.map((child) => (
            <TreeBranch
              key={child.id}
              node={child}
              depth={depth + 1}
              activeId={activeId}
              onSelect={onSelect}
            />
          ))}
        </ul>
      )}
    </li>
  );
}

export function TreeBlock({ title, root }: TreeBlockProps) {
  const [active, setActive] = useState<TreeNode | null>(root);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="grid gap-6 lg:grid-cols-[1fr_220px]">
        <ul>
          <TreeBranch
            node={root}
            depth={0}
            activeId={active?.id ?? null}
            onSelect={setActive}
          />
        </ul>
        <aside className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
          {active ? (
            <>
              <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                Node
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
                  Open concept →
                </Link>
              )}
            </>
          ) : (
            <p className="text-sm text-[var(--ink-soft)]">Select a node.</p>
          )}
        </aside>
      </div>
    </div>
  );
}
