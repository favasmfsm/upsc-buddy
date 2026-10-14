import type { VisualBlock } from "@/lib/api";

type ComparisonBlockProps = Extract<VisualBlock, { type: "comparison" }>;

export function ComparisonBlock({ title, columns }: ComparisonBlockProps) {
  return (
    <div className="rounded-lg border border-[var(--line)] bg-white/60 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div
        className="grid gap-4"
        style={{
          gridTemplateColumns: `repeat(${Math.min(columns.length, 3)}, minmax(0, 1fr))`,
        }}
      >
        {columns.map((col) => (
          <div
            key={col.id}
            className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4"
          >
            <h4 className="font-medium text-[var(--ink)]">{col.heading}</h4>
            <ul className="mt-3 space-y-2 text-sm text-[var(--ink-soft)]">
              {col.points.map((point) => (
                <li key={point} className="flex gap-2">
                  <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--accent)]" />
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
