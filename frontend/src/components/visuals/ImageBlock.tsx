import Image from "next/image";

import type { VisualBlock } from "@/lib/api";

type ImageBlockProps = Extract<VisualBlock, { type: "image" }>;

export function ImageBlock({ title, src, alt, caption, source }: ImageBlockProps) {
  return (
    <figure className="rounded-lg border border-[var(--line)] bg-white/60 p-5">
      {title && (
        <h3 className="mb-4 font-[family-name:var(--font-display)] text-xl">
          {title}
        </h3>
      )}
      <div className="overflow-hidden rounded-md border border-[var(--line)] bg-[var(--paper)]">
        <Image
          src={src}
          alt={alt}
          width={0}
          height={0}
          sizes="(min-width: 1024px) 720px, 100vw"
          style={{ width: "100%", height: "auto" }}
          className="block"
        />
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
