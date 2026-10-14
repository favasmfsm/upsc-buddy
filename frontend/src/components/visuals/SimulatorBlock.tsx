"use client";

import { useState } from "react";

import type { VisualBlock } from "@/lib/api";

type SimulatorBlockProps = Extract<VisualBlock, { type: "simulator" }>;

export function SimulatorBlock({
  title,
  start,
  nodes,
}: SimulatorBlockProps) {
  const [current, setCurrent] = useState(start);
  const node = nodes[current];

  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/70 p-5 sm:p-6">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}

      {node ? (
        <>
          <p className="text-base text-[var(--ink)]">{node.prompt}</p>
          {node.choices.length > 0 ? (
            <ul className="mt-4 space-y-2">
              {node.choices.map((choice) => (
                <li key={`${choice.next}-${choice.label}`}>
                  <button
                    type="button"
                    onClick={() => setCurrent(choice.next)}
                    className="w-full rounded-md border border-[var(--line)] bg-[var(--paper)] px-4 py-3 text-left text-sm transition hover:border-[var(--accent)] hover:bg-[var(--accent-soft)]"
                  >
                    {choice.label}
                  </button>
                </li>
              ))}
            </ul>
          ) : (
            <p className="mt-4 text-sm text-[var(--ink-soft)]">End of path.</p>
          )}
        </>
      ) : (
        <p className="text-sm text-[var(--ink-soft)]">
          Missing node: {current}
        </p>
      )}

      <button
        type="button"
        onClick={() => setCurrent(start)}
        className="mt-5 text-sm text-[var(--accent)] hover:underline"
      >
        Restart scenario
      </button>
    </div>
  );
}
