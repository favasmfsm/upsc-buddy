import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/** Insert line breaks before jammed numbered statements in UPSC-style MCQ stems. */
export function formatMcqStem(stem: string): string {
  let text = stem.trim();
  if (!text) return text;
  // "...statements:1. Foo" / "...text?1. Foo" / "...grounds.2. Bar"
  text = text.replace(
    /([:?.\)"'”’])\s*(\d{1,2})\.\s+(?=[A-Z"'“‘])/g,
    "$1\n$2. ",
  );
  // Closing ask only when it follows end of a prior sentence/statement
  text = text.replace(
    /(?<=[.!"'”’])\s*(?=(?:Which of the (?:statements|above)|Select the correct|Choose the correct|Codes?\s*:))/gi,
    "\n",
  );
  text = text.replace(/\n{3,}/g, "\n\n");
  return text.trim();
}
