import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type CalloutBlockProps = Extract<VisualBlock, { type: "callout" }>;

const toneStyles: Record<string, string> = {
  tip: "border-[var(--accent)] bg-[var(--accent-soft)]",
  trap: "border-[#a35d3a] bg-[#f3e6dc]",
  note: "border-[var(--line)] bg-[var(--muted)]",
};

export function CalloutBlock({ title, body, tone = "note" }: CalloutBlockProps) {
  return (
    <div
      className={cn(
        "rounded-lg border px-4 py-3",
        toneStyles[tone] ?? toneStyles.note,
      )}
    >
      <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
        {tone}
        {title ? ` · ${title}` : ""}
      </p>
      <p className="mt-1 text-sm text-[var(--ink)]">{body}</p>
    </div>
  );
}
