"use client";

import { useState } from "react";
import Image from "next/image";

import type { VisualBlock } from "@/lib/api";
import { cn } from "@/lib/utils";

type AnnotatedImageBlockProps = Extract<
  VisualBlock,
  { type: "annotated_image" }
>;

export function AnnotatedImageBlock({
  title,
  src,
  alt,
  caption,
  source,
  markers,
}: AnnotatedImageBlockProps) {
  const [activeId, setActiveId] = useState<string | null>(
    markers[0]?.id ?? null,
  );
  const active = markers.find((m) => m.id === activeId);

  return (
    <figure className="rounded-lg border border-[var(--line)] bg-white/60 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="grid gap-6 lg:grid-cols-[1fr_240px]">
        <div className="relative overflow-hidden rounded-md border border-[var(--line)] bg-[var(--paper)]">
          <Image
            src={src}
            alt={alt}
            width={0}
            height={0}
            sizes="(min-width: 1024px) 640px, 100vw"
            style={{ width: "100%", height: "auto" }}
            className="block"
          />
          {markers.map((marker, index) => (
            <button
              key={marker.id}
              type="button"
              aria-label={marker.label}
              onMouseEnter={() => setActiveId(marker.id)}
              onFocus={() => setActiveId(marker.id)}
              onClick={() => setActiveId(marker.id)}
              style={{ left: `${marker.x}%`, top: `${marker.y}%` }}
              className={cn(
                "absolute flex h-6 w-6 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border text-xs font-semibold shadow transition",
                activeId === marker.id
                  ? "border-[var(--accent)] bg-[var(--accent)] text-white"
                  : "border-[var(--accent)] bg-white text-[var(--accent)] hover:bg-[var(--accent-soft)]",
              )}
            >
              {index + 1}
            </button>
          ))}
        </div>
        <aside className="rounded-md border border-[var(--line)] bg-[var(--paper)] p-4">
          <p className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
            Labels
          </p>
          <ol className="mt-2 space-y-1">
            {markers.map((marker, index) => (
              <li key={marker.id}>
                <button
                  type="button"
                  onMouseEnter={() => setActiveId(marker.id)}
                  onFocus={() => setActiveId(marker.id)}
                  onClick={() => setActiveId(marker.id)}
                  className={cn(
                    "flex w-full items-start gap-2 rounded px-2 py-1 text-left text-sm transition",
                    activeId === marker.id
                      ? "bg-[var(--accent-soft)] text-[var(--ink)]"
                      : "text-[var(--ink-soft)] hover:bg-[var(--muted)]",
                  )}
                >
                  <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full border border-[var(--accent)] text-xs font-semibold text-[var(--accent)]">
                    {index + 1}
                  </span>
                  <span>{marker.label}</span>
                </button>
              </li>
            ))}
          </ol>
          {active?.detail && (
            <p className="mt-3 border-t border-[var(--line)] pt-3 text-sm text-[var(--ink-soft)]">
              {active.detail}
            </p>
          )}
        </aside>
      </div>
      {(caption || source) && (
        <figcaption className="mt-3 space-y-1">
          {caption && (
            <p className="text-sm text-[var(--ink-soft)]">{caption}</p>
          )}
          {source && (
            <p className="text-xs text-[var(--ink-soft)]/80">Source: {source}</p>
          )}
        </figcaption>
      )}
    </figure>
  );
}
