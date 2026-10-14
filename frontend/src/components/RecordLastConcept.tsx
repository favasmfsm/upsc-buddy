"use client";

import { useEffect } from "react";

import { setLastConcept } from "@/lib/studyStorage";

export function RecordLastConcept({
  slug,
  title,
  chapterSlug,
}: {
  slug: string;
  title: string;
  chapterSlug?: string | null;
}) {
  useEffect(() => {
    setLastConcept({ slug, title, chapterSlug });
  }, [slug, title, chapterSlug]);

  return null;
}
