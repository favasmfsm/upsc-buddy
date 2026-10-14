"use client";

import { useMutation, useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useMemo, useState } from "react";

import { StudentAnalyticsPanels } from "@/components/current-affairs/AnalyticsPanels";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  fetchCAAttempts,
  fetchCADocuments,
  fetchCAMyAnalytics,
  startCAQuiz,
  type CADocument,
  type QuizAttemptSummary,
} from "@/lib/api";
import { getAccessToken } from "@/lib/auth";
import {
  estimatedSecondsForQuestions,
  formatDuration,
  type QuizExamMode,
} from "@/lib/caAttemptStorage";
import {
  CA_QUESTION_LIMIT_PRESETS,
  CA_SUBJECT_TAGS,
  type CASubjectTag,
} from "@/lib/caSubjects";

type PracticeTab = "daily" | "monthly" | "range";
type PageTab = "practice" | "analytics";
type LimitChoice = "all" | "10" | "20" | "30" | "custom";
type AttemptFilter = "all" | "attempted" | "not_attempted";
type QuizSort = "newest" | "last_score" | "last_attempt";

type PendingStart =
  | {
      kind: "daily" | "monthly";
      date: string;
      title: string;
      questionCount: number;
    }
  | { kind: "range"; start: string; end: string; questionCount: null };

type DocLastAttempt = {
  score: number;
  total: number;
  completed_at: string;
};

function formatDate(iso: string) {
  return new Date(iso + "T00:00:00").toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

function formatDateTime(iso: string) {
  return new Date(iso).toLocaleString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
}

function monthInputValue(iso: string) {
  return iso.slice(0, 7);
}

function allSubjectsSelected(): Set<CASubjectTag> {
  return new Set(CA_SUBJECT_TAGS);
}

function docAttemptKey(doc: CADocument) {
  return `${doc.doc_type}:${doc.period_start}:${doc.period_end}`;
}

function attemptKey(a: QuizAttemptSummary) {
  return `${a.mode}:${a.period_start}:${a.period_end}`;
}

/** Latest completed attempt per daily/monthly period (range ignored). */
function buildLastAttemptByDoc(
  attempts: QuizAttemptSummary[],
): Map<string, DocLastAttempt> {
  const map = new Map<string, DocLastAttempt>();
  for (const a of attempts) {
    if (!a.completed_at || a.score == null) continue;
    if (a.mode !== "daily" && a.mode !== "monthly") continue;
    const key = attemptKey(a);
    const prev = map.get(key);
    if (!prev || a.completed_at > prev.completed_at) {
      map.set(key, {
        score: a.score,
        total: a.total,
        completed_at: a.completed_at,
      });
    }
  }
  return map;
}

function filterAndSortDocs(
  docs: CADocument[],
  lastByDoc: Map<string, DocLastAttempt>,
  attemptFilter: AttemptFilter,
  sort: QuizSort,
): CADocument[] {
  let list = docs;
  if (attemptFilter === "attempted") {
    list = list.filter((d) => lastByDoc.has(docAttemptKey(d)));
  } else if (attemptFilter === "not_attempted") {
    list = list.filter((d) => !lastByDoc.has(docAttemptKey(d)));
  }

  const copy = [...list];
  copy.sort((a, b) => {
    const la = lastByDoc.get(docAttemptKey(a));
    const lb = lastByDoc.get(docAttemptKey(b));
    if (sort === "last_score") {
      const sa = la ? la.score / Math.max(1, la.total) : -1;
      const sb = lb ? lb.score / Math.max(1, lb.total) : -1;
      if (sb !== sa) return sb - sa;
      return b.source_date.localeCompare(a.source_date);
    }
    if (sort === "last_attempt") {
      const ta = la?.completed_at ?? "";
      const tb = lb?.completed_at ?? "";
      if (tb !== ta) return tb.localeCompare(ta);
      return b.source_date.localeCompare(a.source_date);
    }
    // newest (document date)
    return b.source_date.localeCompare(a.source_date) || b.id - a.id;
  });
  return copy;
}

export default function CurrentAffairsPage() {
  const router = useRouter();
  const [token, setToken] = useState<string | null>(null);
  const [pageTab, setPageTab] = useState<PageTab>("practice");
  const [tab, setTab] = useState<PracticeTab>("daily");
  const [rangeStart, setRangeStart] = useState("");
  const [rangeEnd, setRangeEnd] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [analyticsDays, setAnalyticsDays] = useState(90);

  const [pendingStart, setPendingStart] = useState<PendingStart | null>(null);
  const [examMode, setExamMode] = useState<QuizExamMode>("simulated");
  const [selectedSubjects, setSelectedSubjects] = useState<Set<CASubjectTag>>(
    () => allSubjectsSelected(),
  );
  const [limitChoice, setLimitChoice] = useState<LimitChoice>("all");
  const [customLimit, setCustomLimit] = useState("15");
  const [attemptFilter, setAttemptFilter] = useState<AttemptFilter>("all");
  const [quizSort, setQuizSort] = useState<QuizSort>("newest");

  useEffect(() => {
    const access = getAccessToken();
    if (!access) {
      router.replace("/login?next=/current-affairs");
      return;
    }
    setToken(access);
  }, [router]);

  const docsQuery = useQuery({
    queryKey: ["ca-documents"],
    enabled: Boolean(token),
    queryFn: () => fetchCADocuments(),
  });

  const attemptsQuery = useQuery({
    queryKey: ["ca-attempts"],
    enabled: Boolean(token),
    queryFn: () => fetchCAAttempts(token!),
  });

  const analyticsQuery = useQuery({
    queryKey: ["ca-analytics-me", analyticsDays],
    enabled: Boolean(token) && pageTab === "analytics",
    queryFn: () => fetchCAMyAnalytics(token!, analyticsDays),
  });

  const lastAttemptByDoc = useMemo(
    () => buildLastAttemptByDoc(attemptsQuery.data || []),
    [attemptsQuery.data],
  );

  const dailyDocs = useMemo(
    () =>
      filterAndSortDocs(
        (docsQuery.data || []).filter((d) => d.doc_type === "daily"),
        lastAttemptByDoc,
        attemptFilter,
        quizSort,
      ),
    [docsQuery.data, lastAttemptByDoc, attemptFilter, quizSort],
  );
  const monthlyDocs = useMemo(
    () =>
      filterAndSortDocs(
        (docsQuery.data || []).filter((d) => d.doc_type === "monthly"),
        lastAttemptByDoc,
        attemptFilter,
        quizSort,
      ),
    [docsQuery.data, lastAttemptByDoc, attemptFilter, quizSort],
  );

  const incompleteAttempts = useMemo(
    () => (attemptsQuery.data || []).filter((a) => !a.completed_at),
    [attemptsQuery.data],
  );

  const resolvedLimit = useMemo(() => {
    if (limitChoice === "all") return undefined;
    if (limitChoice === "custom") {
      const n = Number.parseInt(customLimit, 10);
      if (!Number.isFinite(n) || n < 1) return null;
      return Math.min(200, n);
    }
    return Number(limitChoice);
  }, [limitChoice, customLimit]);

  const allTopicsOn =
    selectedSubjects.size === CA_SUBJECT_TAGS.length &&
    CA_SUBJECT_TAGS.every((t) => selectedSubjects.has(t));

  const startMutation = useMutation({
    mutationFn: async (
      body:
        | {
            mode: "daily" | "monthly";
            date: string;
            limit?: number;
            subject_tags?: string[];
          }
        | {
            mode: "range";
            start: string;
            end: string;
            limit?: number;
            subject_tags?: string[];
          },
    ) => startCAQuiz(token!, body),
    onSuccess: (data) => {
      setPendingStart(null);
      router.push(`/current-affairs/quiz/${data.id}?mode=${examMode}`);
    },
    onError: (err: Error) => setError(err.message),
  });

  if (!token) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">Redirecting to login…</p>
    );
  }

  function resetStartOptions() {
    setExamMode("simulated");
    setSelectedSubjects(allSubjectsSelected());
    setLimitChoice("all");
    setCustomLimit("15");
  }

  function openDaily(doc: CADocument) {
    setError(null);
    resetStartOptions();
    setPendingStart({
      kind: "daily",
      date: doc.source_date,
      title: doc.title,
      questionCount: doc.question_count,
    });
  }

  function openMonthly(doc: CADocument) {
    setError(null);
    resetStartOptions();
    setPendingStart({
      kind: "monthly",
      date: doc.source_date,
      title: doc.title,
      questionCount: doc.question_count,
    });
  }

  function openRange() {
    setError(null);
    if (!rangeStart || !rangeEnd) {
      setError("Pick a start and end date.");
      return;
    }
    if (rangeStart > rangeEnd) {
      setError("End date must be on or after start date.");
      return;
    }
    resetStartOptions();
    setPendingStart({
      kind: "range",
      start: rangeStart,
      end: rangeEnd,
      questionCount: null,
    });
  }

  function toggleSubject(tag: CASubjectTag) {
    setSelectedSubjects((prev) => {
      const next = new Set(prev);
      if (next.has(tag)) next.delete(tag);
      else next.add(tag);
      return next;
    });
  }

  function confirmStart() {
    if (!pendingStart) return;
    if (selectedSubjects.size === 0) {
      setError("Select at least one topic.");
      return;
    }
    if (resolvedLimit === null) {
      setError("Enter a valid question limit (1–200).");
      return;
    }
    setError(null);

    const subject_tags = allTopicsOn
      ? undefined
      : Array.from(selectedSubjects);
    const limit = resolvedLimit;

    if (pendingStart.kind === "range") {
      startMutation.mutate({
        mode: "range",
        start: pendingStart.start,
        end: pendingStart.end,
        ...(limit != null ? { limit } : {}),
        ...(subject_tags ? { subject_tags } : {}),
      });
      return;
    }
    startMutation.mutate({
      mode: pendingStart.kind,
      date: pendingStart.date,
      ...(limit != null ? { limit } : {}),
      ...(subject_tags ? { subject_tags } : {}),
    });
  }

  const estimatedForTimer =
    pendingStart &&
    examMode === "simulated" &&
    resolvedLimit != null &&
    resolvedLimit !== undefined
      ? formatDuration(estimatedSecondsForQuestions(resolvedLimit))
      : pendingStart &&
          examMode === "simulated" &&
          pendingStart.questionCount != null &&
          limitChoice === "all"
        ? formatDuration(
            estimatedSecondsForQuestions(pendingStart.questionCount),
          )
        : examMode === "simulated"
          ? "60s × questions"
          : null;

  return (
    <div className="space-y-10">
      <div>
        <h1 className="font-[family-name:var(--font-display)] text-4xl">
          Current Affairs
        </h1>
        <p className="mt-2 max-w-2xl text-[var(--ink-soft)]">
          Prelims MCQs generated once from each uploaded compilation, then reused
          for every student. Choose a daily set, a monthly set, or a date range.
        </p>
      </div>

      <div className="flex flex-wrap gap-2 border-b border-[var(--line)] pb-2">
        {(
          [
            ["practice", "Practice"],
            ["analytics", "Analytics"],
          ] as const
        ).map(([id, label]) => (
          <Button
            key={id}
            size="sm"
            variant={pageTab === id ? "default" : "outline"}
            onClick={() => setPageTab(id)}
          >
            {label}
          </Button>
        ))}
      </div>

      {pageTab === "analytics" && (
        <section className="space-y-6">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <h2 className="font-[family-name:var(--font-display)] text-2xl">
              Your performance
            </h2>
            <label className="text-sm text-[var(--ink-soft)]">
              Window{" "}
              <select
                className="ml-2 h-9 rounded-md border border-[var(--line)] bg-white/70 px-2 text-[var(--ink)]"
                value={analyticsDays}
                onChange={(e) => setAnalyticsDays(Number(e.target.value))}
              >
                <option value={30}>30 days</option>
                <option value={90}>90 days</option>
                <option value={180}>180 days</option>
                <option value={365}>365 days</option>
              </select>
            </label>
          </div>
          {analyticsQuery.isLoading && (
            <p className="text-sm text-[var(--ink-soft)]">Loading analytics…</p>
          )}
          {analyticsQuery.isError && (
            <p className="text-sm text-[var(--accent)]" role="alert">
              {(analyticsQuery.error as Error).message}
            </p>
          )}
          {analyticsQuery.data && (
            <StudentAnalyticsPanels data={analyticsQuery.data} />
          )}
        </section>
      )}

      {pageTab === "practice" && (
        <>
          {incompleteAttempts.length > 0 && (
            <section className="space-y-3 rounded-lg border border-[var(--accent)]/30 bg-[var(--accent-soft)]/50 px-4 py-4">
              <h2 className="font-[family-name:var(--font-display)] text-xl text-[var(--ink)]">
                Resume in progress
              </h2>
              <ul className="space-y-2">
                {incompleteAttempts.slice(0, 3).map((a) => (
                  <li
                    key={a.id}
                    className="flex flex-wrap items-center justify-between gap-3"
                  >
                    <div className="text-sm">
                      <Badge variant="muted">{a.mode}</Badge>
                      <span className="ml-2 text-[var(--ink)]">
                        {formatDate(a.period_start)}
                        {a.period_start !== a.period_end
                          ? ` – ${formatDate(a.period_end)}`
                          : ""}
                      </span>
                      <span className="ml-2 text-[var(--ink-soft)]">
                        {a.total} questions
                      </span>
                    </div>
                    <Link href={`/current-affairs/quiz/${a.id}`}>
                      <Button size="sm">Resume</Button>
                    </Link>
                  </li>
                ))}
              </ul>
            </section>
          )}

          <div className="flex flex-wrap gap-2">
            {(
              [
                ["daily", "Daily"],
                ["monthly", "Monthly"],
                ["range", "Date range"],
              ] as const
            ).map(([id, label]) => (
              <Button
                key={id}
                size="sm"
                variant={tab === id ? "default" : "outline"}
                onClick={() => setTab(id)}
              >
                {label}
              </Button>
            ))}
          </div>

          {(tab === "daily" || tab === "monthly") && (
            <div className="flex flex-wrap items-end gap-4">
              <div className="space-y-2">
                <p className="text-sm font-medium text-[var(--ink)]">Filter</p>
                <div className="flex flex-wrap gap-2">
                  {(
                    [
                      ["all", "All"],
                      ["attempted", "Attempted"],
                      ["not_attempted", "Not attempted"],
                    ] as const
                  ).map(([id, label]) => (
                    <Button
                      key={id}
                      size="sm"
                      variant={attemptFilter === id ? "default" : "outline"}
                      onClick={() => setAttemptFilter(id)}
                    >
                      {label}
                    </Button>
                  ))}
                </div>
              </div>
              <label className="text-sm">
                <span className="mb-1 block font-medium text-[var(--ink)]">
                  Sort
                </span>
                <select
                  className="h-9 rounded-md border border-[var(--line)] bg-white/70 px-2 text-[var(--ink)]"
                  value={quizSort}
                  onChange={(e) => setQuizSort(e.target.value as QuizSort)}
                >
                  <option value="newest">Newest</option>
                  <option value="last_score">Last score</option>
                  <option value="last_attempt">Last attempt</option>
                </select>
              </label>
            </div>
          )}

          {error && (
            <p className="text-sm text-[var(--accent)]" role="alert">
              {error}
            </p>
          )}

          {docsQuery.isLoading && (
            <p className="text-sm text-[var(--ink-soft)]">Loading documents…</p>
          )}

          {tab === "daily" && (
            <section className="space-y-4">
              <h2 className="font-[family-name:var(--font-display)] text-2xl">
                Daily quizzes
              </h2>
              {dailyDocs.length === 0 && !docsQuery.isLoading && (
                <p className="text-sm text-[var(--ink-soft)]">
                  {attemptFilter === "all"
                    ? "No quiz ready yet — check back after your academy uploads a compilation."
                    : attemptFilter === "attempted"
                      ? "No attempted daily quizzes yet."
                      : "No unattempted daily quizzes."}
                </p>
              )}
              <ul className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
                {dailyDocs.map((doc) => {
                  const last = lastAttemptByDoc.get(docAttemptKey(doc));
                  return (
                    <li
                      key={doc.id}
                      className="flex flex-wrap items-center justify-between gap-3 py-4"
                    >
                      <div>
                        <p className="font-medium text-[var(--ink)]">
                          {doc.title}
                        </p>
                        <p className="mt-1 text-sm text-[var(--ink-soft)]">
                          {formatDate(doc.source_date)} · {doc.question_count}{" "}
                          questions
                        </p>
                        {last ? (
                          <p className="mt-1 text-sm text-[var(--ink)]">
                            Last: {last.score}/{last.total} ·{" "}
                            {formatDateTime(last.completed_at)}
                          </p>
                        ) : (
                          <p className="mt-1 text-sm text-[var(--ink-soft)]">
                            Not attempted
                          </p>
                        )}
                      </div>
                      <Button
                        size="sm"
                        disabled={
                          startMutation.isPending || doc.question_count === 0
                        }
                        onClick={() => openDaily(doc)}
                      >
                        {last ? "Retake quiz" : "Start quiz"}
                      </Button>
                    </li>
                  );
                })}
              </ul>
            </section>
          )}

          {tab === "monthly" && (
            <section className="space-y-4">
              <h2 className="font-[family-name:var(--font-display)] text-2xl">
                Monthly quizzes
              </h2>
              {monthlyDocs.length === 0 && !docsQuery.isLoading && (
                <p className="text-sm text-[var(--ink-soft)]">
                  {attemptFilter === "all"
                    ? "No quiz ready yet — check back after your academy uploads a compilation."
                    : attemptFilter === "attempted"
                      ? "No attempted monthly quizzes yet."
                      : "No unattempted monthly quizzes."}
                </p>
              )}
              <ul className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
                {monthlyDocs.map((doc) => {
                  const last = lastAttemptByDoc.get(docAttemptKey(doc));
                  return (
                    <li
                      key={doc.id}
                      className="flex flex-wrap items-center justify-between gap-3 py-4"
                    >
                      <div>
                        <p className="font-medium text-[var(--ink)]">
                          {doc.title}
                        </p>
                        <p className="mt-1 text-sm text-[var(--ink-soft)]">
                          {monthInputValue(doc.source_date)} ·{" "}
                          {doc.question_count} questions
                        </p>
                        {last ? (
                          <p className="mt-1 text-sm text-[var(--ink)]">
                            Last: {last.score}/{last.total} ·{" "}
                            {formatDateTime(last.completed_at)}
                          </p>
                        ) : (
                          <p className="mt-1 text-sm text-[var(--ink-soft)]">
                            Not attempted
                          </p>
                        )}
                      </div>
                      <Button
                        size="sm"
                        disabled={
                          startMutation.isPending || doc.question_count === 0
                        }
                        onClick={() => openMonthly(doc)}
                      >
                        {last ? "Retake quiz" : "Start quiz"}
                      </Button>
                    </li>
                  );
                })}
              </ul>
            </section>
          )}

          {tab === "range" && (
            <section className="space-y-4">
              <h2 className="font-[family-name:var(--font-display)] text-2xl">
                Date-range quiz
              </h2>
              <p className="text-sm text-[var(--ink-soft)]">
                Assembles published questions whose source period overlaps your
                range (no new Gemini call).
              </p>
              <div className="flex flex-wrap items-end gap-4">
                <label className="text-sm">
                  <span className="mb-1 block text-[var(--ink-soft)]">From</span>
                  <input
                    type="date"
                    value={rangeStart}
                    onChange={(e) => setRangeStart(e.target.value)}
                    className="h-10 rounded-md border border-[var(--line)] bg-white/70 px-3"
                  />
                </label>
                <label className="text-sm">
                  <span className="mb-1 block text-[var(--ink-soft)]">To</span>
                  <input
                    type="date"
                    value={rangeEnd}
                    onChange={(e) => setRangeEnd(e.target.value)}
                    className="h-10 rounded-md border border-[var(--line)] bg-white/70 px-3"
                  />
                </label>
                <Button
                  disabled={startMutation.isPending}
                  onClick={openRange}
                >
                  Start range quiz
                </Button>
              </div>
            </section>
          )}

          <section className="space-y-4">
            <h2 className="font-[family-name:var(--font-display)] text-2xl">
              Recent attempts
            </h2>
            {(attemptsQuery.data || []).length === 0 && (
              <p className="text-sm text-[var(--ink-soft)]">No attempts yet.</p>
            )}
            <ul className="space-y-2">
              {(attemptsQuery.data || []).slice(0, 8).map((a) => (
                <li key={a.id}>
                  <Link
                    href={`/current-affairs/quiz/${a.id}`}
                    className="flex flex-wrap items-center gap-3 text-sm hover:text-[var(--accent)]"
                  >
                    <Badge variant="muted">{a.mode}</Badge>
                    <span>
                      {formatDate(a.period_start)}
                      {a.period_start !== a.period_end
                        ? ` – ${formatDate(a.period_end)}`
                        : ""}
                    </span>
                    {a.completed_at ? (
                      <span className="text-[var(--ink-soft)]">
                        {a.score}/{a.total}
                      </span>
                    ) : (
                      <span className="text-[var(--ink-soft)]">In progress</span>
                    )}
                  </Link>
                </li>
              ))}
            </ul>
          </section>
        </>
      )}

      {pendingStart && (
        <div
          className="fixed inset-0 z-50 flex items-end justify-center bg-black/35 p-4 sm:items-center"
          role="dialog"
          aria-modal="true"
          aria-labelledby="ca-start-title"
        >
          <div className="max-h-[90vh] w-full max-w-lg space-y-5 overflow-y-auto border border-[var(--line)] bg-[var(--paper)] p-6 shadow-lg">
            <div>
              <h2
                id="ca-start-title"
                className="font-[family-name:var(--font-display)] text-2xl"
              >
                Begin quiz
              </h2>
              <p className="mt-1 text-sm text-[var(--ink-soft)]">
                {pendingStart.kind === "range"
                  ? `${formatDate(pendingStart.start)} – ${formatDate(pendingStart.end)}`
                  : pendingStart.title}
              </p>
              {pendingStart.questionCount != null && (
                <p className="mt-1 text-sm text-[var(--ink-soft)]">
                  Bank has {pendingStart.questionCount} published questions
                </p>
              )}
            </div>

            <div className="space-y-2">
              <p className="text-sm font-medium text-[var(--ink)]">Mode</p>
              <div className="flex gap-2">
                <Button
                  type="button"
                  size="sm"
                  variant={examMode === "simulated" ? "default" : "outline"}
                  onClick={() => setExamMode("simulated")}
                  className="flex-1"
                >
                  Simulated
                </Button>
                <Button
                  type="button"
                  size="sm"
                  variant={examMode === "practice" ? "default" : "outline"}
                  onClick={() => setExamMode("practice")}
                  className="flex-1"
                >
                  Practice
                </Button>
              </div>
              <p className="text-xs text-[var(--ink-soft)]">
                {examMode === "simulated"
                  ? estimatedForTimer
                    ? `Timed (~${estimatedForTimer}). Auto-submits when time runs out.`
                    : "Timed at 60 seconds per question."
                  : "No timer. Review and submit at your own pace."}
              </p>
            </div>

            <div className="space-y-2">
              <p className="text-sm font-medium text-[var(--ink)]">
                Number of questions
              </p>
              <div className="flex flex-wrap gap-2">
                <Button
                  type="button"
                  size="sm"
                  variant={limitChoice === "all" ? "default" : "outline"}
                  onClick={() => setLimitChoice("all")}
                >
                  All
                </Button>
                {CA_QUESTION_LIMIT_PRESETS.map((n) => (
                  <Button
                    key={n}
                    type="button"
                    size="sm"
                    variant={limitChoice === String(n) ? "default" : "outline"}
                    onClick={() => setLimitChoice(String(n) as LimitChoice)}
                  >
                    {n}
                  </Button>
                ))}
                <Button
                  type="button"
                  size="sm"
                  variant={limitChoice === "custom" ? "default" : "outline"}
                  onClick={() => setLimitChoice("custom")}
                >
                  Custom
                </Button>
              </div>
              {limitChoice === "custom" && (
                <label className="block text-sm">
                  <span className="mb-1 block text-[var(--ink-soft)]">
                    Custom count (1–200)
                  </span>
                  <input
                    type="number"
                    min={1}
                    max={200}
                    value={customLimit}
                    onChange={(e) => setCustomLimit(e.target.value)}
                    className="h-10 w-28 rounded-md border border-[var(--line)] bg-white/70 px-3"
                  />
                </label>
              )}
            </div>

            <div className="space-y-2">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <p className="text-sm font-medium text-[var(--ink)]">Topics</p>
                <div className="flex gap-2">
                  <Button
                    type="button"
                    size="sm"
                    variant="outline"
                    onClick={() => setSelectedSubjects(allSubjectsSelected())}
                  >
                    Select all
                  </Button>
                  <Button
                    type="button"
                    size="sm"
                    variant="outline"
                    onClick={() => setSelectedSubjects(new Set())}
                  >
                    Clear
                  </Button>
                </div>
              </div>
              <div className="flex flex-wrap gap-2">
                {CA_SUBJECT_TAGS.map((tag) => {
                  const on = selectedSubjects.has(tag);
                  return (
                    <Button
                      key={tag}
                      type="button"
                      size="sm"
                      variant={on ? "default" : "outline"}
                      onClick={() => toggleSubject(tag)}
                      aria-pressed={on}
                    >
                      {tag}
                    </Button>
                  );
                })}
              </div>
              <p className="text-xs text-[var(--ink-soft)]">
                {allTopicsOn
                  ? "All topics included."
                  : `${selectedSubjects.size} topic${selectedSubjects.size === 1 ? "" : "s"} selected.`}
              </p>
            </div>

            <div className="flex flex-wrap justify-end gap-2 pt-1">
              <Button
                type="button"
                variant="outline"
                disabled={startMutation.isPending}
                onClick={() => {
                  setPendingStart(null);
                  setError(null);
                }}
              >
                Cancel
              </Button>
              <Button
                type="button"
                disabled={startMutation.isPending}
                onClick={confirmStart}
              >
                {startMutation.isPending ? "Preparing…" : "Begin quiz"}
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
