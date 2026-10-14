"use client";

import { useEffect, useState } from "react";

import { cn } from "@/lib/utils";

export type TocSection = {
  id: string;
  label: string;
};

export function ConceptToc({ sections }: { sections: TocSection[] }) {
  const [active, setActive] = useState<string | null>(
    sections[0]?.id ?? null,
  );

  useEffect(() => {
    if (sections.length === 0) return;

    const elements = sections
      .map((s) => document.getElementById(s.id))
      .filter((el): el is HTMLElement => Boolean(el));

    if (elements.length === 0) return;

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort(
            (a, b) =>
              a.boundingClientRect.top - b.boundingClientRect.top,
          );
        if (visible[0]?.target?.id) {
          setActive(visible[0].target.id);
        }
      },
      {
        rootMargin: "-20% 0px -55% 0px",
        threshold: [0, 0.25, 0.5],
      },
    );

    for (const el of elements) observer.observe(el);
    return () => observer.disconnect();
  }, [sections]);

  if (sections.length === 0) return null;

  return (
    <nav
      aria-label="On this page"
      className="sticky top-[4.5rem] z-10 -mx-1 mb-2 overflow-x-auto bg-[var(--paper)]/90 px-1 py-2 backdrop-blur lg:static lg:mx-0 lg:mb-0 lg:overflow-visible lg:bg-transparent lg:p-0 lg:backdrop-blur-none"
    >
      <ul className="flex gap-2 lg:flex-col lg:gap-1.5">
        {sections.map((s) => (
          <li key={s.id} className="shrink-0">
            <a
              href={`#${s.id}`}
              className={cn(
                "block rounded-md px-2.5 py-1.5 text-sm transition-colors",
                active === s.id
                  ? "bg-[var(--accent-soft)] font-medium text-[var(--accent)]"
                  : "text-[var(--ink-soft)] hover:text-[var(--ink)]",
              )}
            >
              {s.label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
