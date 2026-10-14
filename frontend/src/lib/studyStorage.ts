export type LastConcept = {
  slug: string;
  title: string;
  chapterSlug?: string | null;
  at: number;
};

const LAST_CONCEPT_KEY = "upsc_buddy_last_concept";

export function getLastConcept(): LastConcept | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = localStorage.getItem(LAST_CONCEPT_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as Partial<LastConcept>;
    if (!parsed?.slug || !parsed?.title) return null;
    return {
      slug: String(parsed.slug),
      title: String(parsed.title),
      chapterSlug: parsed.chapterSlug ?? null,
      at: typeof parsed.at === "number" ? parsed.at : Date.now(),
    };
  } catch {
    return null;
  }
}

export function setLastConcept(concept: {
  slug: string;
  title: string;
  chapterSlug?: string | null;
}): void {
  if (typeof window === "undefined") return;
  try {
    const payload: LastConcept = {
      slug: concept.slug,
      title: concept.title,
      chapterSlug: concept.chapterSlug ?? null,
      at: Date.now(),
    };
    localStorage.setItem(LAST_CONCEPT_KEY, JSON.stringify(payload));
  } catch {
    // Quota / private mode — ignore
  }
}
