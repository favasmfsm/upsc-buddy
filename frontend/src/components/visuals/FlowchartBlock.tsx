"use client";

import { useMemo, useState } from "react";

import type { VisualBlock, VisualFlowStep } from "@/lib/api";
import { cn } from "@/lib/utils";

type FlowchartBlockProps = Extract<VisualBlock, { type: "flowchart" }>;

function isBranching(steps: VisualFlowStep[]): boolean {
  return steps.some((step) => (step.options?.length ?? 0) > 0);
}

function BranchTree({
  step,
  byId,
  depth,
  activeId,
  onSelect,
}: {
  step: VisualFlowStep;
  byId: Map<string, VisualFlowStep>;
  depth: number;
  activeId: string | null;
  onSelect: (id: string) => void;
}) {
  const options = step.options ?? [];
  const isActive = activeId === step.id;

  return (
    <div className={cn(depth > 0 && "ml-4 border-l border-[var(--line)] pl-4")}>
      <button
        type="button"
        onClick={() => onSelect(step.id)}
        onMouseEnter={() => onSelect(step.id)}
        onFocus={() => onSelect(step.id)}
        className={cn(
          "w-full rounded-md border px-3 py-2 text-left text-sm transition",
          isActive
            ? "border-[var(--accent)] bg-[var(--accent-soft)]"
            : "border-[var(--line)] bg-white hover:border-[var(--accent)]/40",
        )}
      >
        {step.label}
      </button>

      {options.length > 0 && (
        <ul className="mt-3 space-y-3">
          {options.map((opt) => {
            const child = byId.get(opt.next);
            return (
              <li key={`${step.id}-${opt.next}-${opt.label}`}>
                <p className="mb-1 text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                  {opt.label}
                </p>
                {child ? (
                  <BranchTree
                    step={child}
                    byId={byId}
                    depth={depth + 1}
                    activeId={activeId}
                    onSelect={onSelect}
                  />
                ) : (
                  <p className="rounded-md border border-dashed border-[var(--line)] px-3 py-2 text-sm text-[var(--ink-soft)]">
                    Missing step: {opt.next}
                  </p>
                )}
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}

function LinearFlow({
  steps,
  activeId,
  setActiveId,
}: {
  steps: VisualFlowStep[];
  activeId: string | null;
  setActiveId: (id: string) => void;
}) {
  return (
    <ol className="space-y-0">
      {steps.map((step, index) => (
        <li key={step.id} className="relative flex gap-3 pb-4 last:pb-0">
          {index < steps.length - 1 && (
            <span
              className="absolute left-[15px] top-8 h-[calc(100%-1.5rem)] w-px bg-[var(--line)]"
              aria-hidden
            />
          )}
          <button
            type="button"
            onMouseEnter={() => setActiveId(step.id)}
            onFocus={() => setActiveId(step.id)}
            onClick={() => setActiveId(step.id)}
            className={cn(
              "relative z-[1] flex h-8 w-8 shrink-0 items-center justify-center rounded-full border text-xs font-medium transition",
              activeId === step.id
                ? "border-[var(--accent)] bg-[var(--accent)] text-white"
                : "border-[var(--line)] bg-white text-[var(--ink-soft)]",
            )}
          >
            {index + 1}
          </button>
          <button
            type="button"
            onMouseEnter={() => setActiveId(step.id)}
            onFocus={() => setActiveId(step.id)}
            onClick={() => setActiveId(step.id)}
            className={cn(
              "flex-1 rounded-md border px-3 py-2 text-left text-sm transition",
              activeId === step.id
                ? "border-[var(--accent)] bg-[var(--accent-soft)]"
                : "border-transparent hover:border-[var(--line)]",
            )}
          >
            {step.label}
          </button>
        </li>
      ))}
    </ol>
  );
}

export function FlowchartBlock({ title, root, steps }: FlowchartBlockProps) {
  const branching = isBranching(steps);
  const byId = useMemo(
    () => new Map(steps.map((step) => [step.id, step])),
    [steps],
  );
  const rootStep = useMemo(() => {
    if (!branching) return steps[0];
    if (root && byId.has(root)) return byId.get(root);
    return steps[0];
  }, [branching, root, byId, steps]);

  const [activeId, setActiveId] = useState<string | null>(
    rootStep?.id ?? steps[0]?.id ?? null,
  );
  const active = steps.find((s) => s.id === activeId);

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/60 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="grid gap-6 lg:grid-cols-[1fr_240px]">
        {branching && rootStep ? (
          <BranchTree
            step={rootStep}
            byId={byId}
            depth={0}
            activeId={activeId}
            onSelect={setActiveId}
          />
        ) : (
          <LinearFlow
            steps={steps}
            activeId={activeId}
            setActiveId={setActiveId}
          />
        )}
        <aside className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
          {active ? (
            <>
              <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
                {branching ? "Node detail" : "Step detail"}
              </p>
              <p className="mt-1 font-medium text-[var(--ink)]">{active.label}</p>
              {active.detail && (
                <p className="mt-2 text-sm text-[var(--ink-soft)]">
                  {active.detail}
                </p>
              )}
            </>
          ) : (
            <p className="text-sm text-[var(--ink-soft)]">
              Hover or click a step.
            </p>
          )}
        </aside>
      </div>
    </div>
  );
}
