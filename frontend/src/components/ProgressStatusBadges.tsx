export type ProgressStatus = "not_started" | "studied" | "revise_later";

/**
 * Card/row surface tone from progress flags.
 * Status drives fill; difficult adds a rose border (or fill when status is unset).
 */
export function progressCardToneClass(
  status?: string | null,
  isDifficult?: boolean,
): string {
  const parts: string[] = [];

  if (status === "studied") {
    parts.push(
      "border-[color-mix(in_srgb,var(--studied)_35%,var(--line))] bg-[var(--studied-soft)]",
    );
  } else if (status === "revise_later") {
    parts.push(
      "border-[color-mix(in_srgb,var(--revise)_35%,var(--line))] bg-[var(--revise-soft)]",
    );
  } else if (isDifficult) {
    parts.push(
      "border-[color-mix(in_srgb,var(--difficult)_35%,var(--line))] bg-[var(--difficult-soft)]",
    );
  }

  if (isDifficult && (status === "studied" || status === "revise_later")) {
    parts.push("border-[var(--difficult)]");
  }

  return parts.join(" ");
}

/** @deprecated Use progressCardToneClass */
export function progressCardAccentClass(
  status?: string | null,
  isDifficult?: boolean,
): string {
  return progressCardToneClass(status, isDifficult);
}
