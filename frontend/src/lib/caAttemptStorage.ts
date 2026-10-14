export type QuizExamMode = "simulated" | "practice";

export type CAAttemptDraft = {
  answers: Record<string, "A" | "B" | "C" | "D">;
  flaggedIds: string[];
  endsAt: number | null;
  mode: QuizExamMode;
  started: boolean;
};

function storageKey(attemptId: number) {
  return `ca-attempt-${attemptId}`;
}

export function getCAAttemptDraft(attemptId: number): CAAttemptDraft | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = localStorage.getItem(storageKey(attemptId));
    if (!raw) return null;
    const parsed = JSON.parse(raw) as Partial<CAAttemptDraft>;
    if (!parsed || typeof parsed !== "object") return null;
    return {
      answers: (parsed.answers || {}) as CAAttemptDraft["answers"],
      flaggedIds: Array.isArray(parsed.flaggedIds)
        ? parsed.flaggedIds.map(String)
        : [],
      endsAt:
        typeof parsed.endsAt === "number" && Number.isFinite(parsed.endsAt)
          ? parsed.endsAt
          : null,
      mode: parsed.mode === "practice" ? "practice" : "simulated",
      started: Boolean(parsed.started),
    };
  } catch {
    return null;
  }
}

export function setCAAttemptDraft(
  attemptId: number,
  draft: CAAttemptDraft,
): void {
  if (typeof window === "undefined") return;
  try {
    localStorage.setItem(storageKey(attemptId), JSON.stringify(draft));
  } catch {
    // Quota / private mode — ignore
  }
}

export function clearCAAttemptDraft(attemptId: number): void {
  if (typeof window === "undefined") return;
  try {
    localStorage.removeItem(storageKey(attemptId));
  } catch {
    // ignore
  }
}

export function formatDuration(totalSeconds: number): string {
  const s = Math.max(0, Math.floor(totalSeconds));
  const m = Math.floor(s / 60);
  const r = s % 60;
  return `${m}:${r.toString().padStart(2, "0")}`;
}

export function estimatedSecondsForQuestions(count: number): number {
  return Math.max(0, count) * 60;
}
