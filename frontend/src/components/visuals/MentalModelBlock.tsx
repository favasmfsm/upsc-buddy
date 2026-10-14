"use client";

import type { VisualBlock } from "@/lib/api";

type MentalModelBlockProps = Extract<VisualBlock, { type: "mental_model" }>;

export function MentalModelBlock({
  title,
  metaphor,
  topic_label,
  subject_label,
  relation_label,
  protects_from,
  insight,
}: MentalModelBlockProps) {
  return (
    <div className="rounded-lg border border-[var(--line)] bg-gradient-to-b from-[#f7f1e6] to-white/80 p-6 sm:p-8">
      {title && (
        <h3 className="mb-6 text-center font-[family-name:var(--font-display)] text-xl sm:text-2xl">
          {title}
        </h3>
      )}

      <div className="mx-auto flex max-w-md flex-col items-center text-center">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-[var(--ink-soft)]">
          {subject_label}
        </p>

        <div className="relative mt-4 flex h-28 w-28 items-center justify-center rounded-full border-2 border-[#8b6914] bg-[#fffdf8] shadow-[6px_6px_0_0_#c4a035]/40]">
          <span
            className="absolute inset-3 rounded-full border border-dashed border-[#8b6914]/50"
            aria-hidden
          />
          <span className="font-[family-name:var(--font-display)] text-sm font-semibold uppercase tracking-wide text-[#5c4a1a]">
            {metaphor || "Shield"}
          </span>
        </div>

        <p className="mt-5 font-[family-name:var(--font-display)] text-2xl text-[var(--ink)]">
          {topic_label || metaphor || "Mental model"}
        </p>
        <p className="mt-2 text-sm text-[var(--ink-soft)]">
          {relation_label || "Protects you from"}
        </p>

        <ul className="mt-4 w-full space-y-2 text-left">
          {protects_from.map((item) => (
            <li
              key={item}
              className="rounded-md border border-[var(--line)] bg-white/80 px-3 py-2 text-sm text-[var(--ink)]"
            >
              {item}
            </li>
          ))}
        </ul>

        {insight && (
          <p className="mt-6 border-t border-[var(--line)] pt-4 text-sm italic text-[var(--ink-soft)]">
            {insight}
          </p>
        )}
      </div>
    </div>
  );
}
