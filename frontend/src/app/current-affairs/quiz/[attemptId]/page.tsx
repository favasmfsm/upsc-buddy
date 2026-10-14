"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import Link from "next/link";
import { useParams, useRouter, useSearchParams } from "next/navigation";
import {
  Suspense,
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  fetchCAQuiz,
  submitCAQuiz,
  type CAQuestionPublic,
  type CAQuestionResult,
} from "@/lib/api";
import { getAccessToken } from "@/lib/auth";
import {
  clearCAAttemptDraft,
  estimatedSecondsForQuestions,
  formatDuration,
  getCAAttemptDraft,
  setCAAttemptDraft,
  type QuizExamMode,
} from "@/lib/caAttemptStorage";
import { formatMcqStem } from "@/lib/utils";

const OPTIONS = ["A", "B", "C", "D"] as const;
type OptionKey = (typeof OPTIONS)[number];
type AnswerMap = Record<string, OptionKey>;
type ReviewFilter = "incorrect" | "all" | "correct" | "unattempted";

function optionText(q: CAQuestionPublic, key: OptionKey) {
  switch (key) {
    case "A":
      return q.option_a;
    case "B":
      return q.option_b;
    case "C":
      return q.option_c;
    case "D":
      return q.option_d;
  }
}

function parseMode(raw: string | null): QuizExamMode {
  return raw === "practice" ? "practice" : "simulated";
}

function reviewStatus(q: CAQuestionResult): ReviewFilter {
  if (q.selected == null || q.selected === "") return "unattempted";
  return q.is_correct ? "correct" : "incorrect";
}

function CAQuizPageInner() {
  const params = useParams();
  const searchParams = useSearchParams();
  const attemptId = Number(params.attemptId);
  const router = useRouter();
  const queryClient = useQueryClient();
  const [token, setToken] = useState<string | null>(null);
  const [answers, setAnswers] = useState<AnswerMap>({});
  const [flaggedIds, setFlaggedIds] = useState<string[]>([]);
  const [index, setIndex] = useState(0);
  const [examMode, setExamMode] = useState<QuizExamMode>(() =>
    parseMode(searchParams.get("mode")),
  );
  const [started, setStarted] = useState(false);
  const [endsAt, setEndsAt] = useState<number | null>(null);
  const [now, setNow] = useState(() => Date.now());
  const [showSubmitConfirm, setShowSubmitConfirm] = useState(false);
  const [hydrated, setHydrated] = useState(false);
  const [reviewFilter, setReviewFilter] = useState<ReviewFilter>("incorrect");
  const autoSubmitFired = useRef(false);
  const answersRef = useRef(answers);
  answersRef.current = answers;

  useEffect(() => {
    const access = getAccessToken();
    if (!access) {
      router.replace(`/login?next=/current-affairs/quiz/${attemptId}`);
      return;
    }
    setToken(access);
  }, [router, attemptId]);

  const quizQuery = useQuery({
    queryKey: ["ca-quiz", attemptId],
    enabled: Boolean(token) && Number.isFinite(attemptId),
    queryFn: () => fetchCAQuiz(token!, attemptId),
  });

  const submitMutation = useMutation({
    mutationFn: (payload: AnswerMap) =>
      submitCAQuiz(token!, attemptId, payload),
    onSuccess: (data) => {
      clearCAAttemptDraft(attemptId);
      queryClient.setQueryData(["ca-quiz", attemptId], data);
      queryClient.invalidateQueries({ queryKey: ["ca-attempts"] });
      setShowSubmitConfirm(false);
    },
  });

  const completed = Boolean(quizQuery.data?.completed_at);
  const questions = useMemo(() => {
    if (completed) return quizQuery.data?.results || [];
    return quizQuery.data?.questions || [];
  }, [completed, quizQuery.data]);

  // Hydrate draft + server answers once quiz loads
  useEffect(() => {
    if (!quizQuery.data || completed || hydrated) return;

    const draft = getCAAttemptDraft(attemptId);
    const serverAnswers = (quizQuery.data.answers || {}) as AnswerMap;
    const queryMode = parseMode(searchParams.get("mode"));

    if (draft) {
      setExamMode(draft.mode);
      setAnswers({ ...serverAnswers, ...draft.answers });
      setFlaggedIds(draft.flaggedIds);
      setEndsAt(draft.endsAt);
      setStarted(
        draft.mode === "practice"
          ? true
          : draft.started && draft.endsAt != null,
      );
    } else {
      setExamMode(queryMode);
      setAnswers(serverAnswers);
      if (queryMode === "practice") {
        setStarted(true);
      }
    }
    setHydrated(true);
  }, [quizQuery.data, completed, hydrated, attemptId, searchParams]);

  // Debounced localStorage persistence
  useEffect(() => {
    if (!hydrated || completed || !Number.isFinite(attemptId)) return;
    const handle = window.setTimeout(() => {
      setCAAttemptDraft(attemptId, {
        answers,
        flaggedIds,
        endsAt,
        mode: examMode,
        started,
      });
    }, 300);
    return () => window.clearTimeout(handle);
  }, [
    answers,
    flaggedIds,
    endsAt,
    examMode,
    started,
    hydrated,
    completed,
    attemptId,
  ]);

  // Timer tick
  useEffect(() => {
    if (completed || examMode !== "simulated" || !started || endsAt == null) {
      return;
    }
    setNow(Date.now());
    const id = window.setInterval(() => setNow(Date.now()), 1000);
    return () => window.clearInterval(id);
  }, [completed, examMode, started, endsAt]);

  const remainingMs =
    examMode === "simulated" && endsAt != null ? endsAt - now : null;
  const remainingSec =
    remainingMs != null ? Math.max(0, Math.ceil(remainingMs / 1000)) : null;

  const doSubmit = useCallback(
    (payload?: AnswerMap) => {
      if (submitMutation.isPending || completed) return;
      submitMutation.mutate(payload ?? answersRef.current);
    },
    [submitMutation, completed],
  );

  // Auto-submit when time expires (or draft already expired on hydrate)
  useEffect(() => {
    if (
      !hydrated ||
      completed ||
      examMode !== "simulated" ||
      !started ||
      endsAt == null ||
      autoSubmitFired.current
    ) {
      return;
    }
    if (Date.now() >= endsAt) {
      autoSubmitFired.current = true;
      doSubmit();
    }
  }, [hydrated, completed, examMode, started, endsAt, now, doSubmit]);

  const current = questions[index] as CAQuestionPublic | CAQuestionResult | undefined;
  const answeredCount = Object.keys(answers).length;
  const unansweredCount = Math.max(0, questions.length - answeredCount);
  const currentId = current ? String(current.id) : null;
  const isFlagged = currentId ? flaggedIds.includes(currentId) : false;

  const beginSimulated = () => {
    const total = quizQuery.data?.total ?? questions.length;
    const nextEnds = Date.now() + estimatedSecondsForQuestions(total) * 1000;
    setEndsAt(nextEnds);
    setStarted(true);
    autoSubmitFired.current = false;
  };

  const selectOption = useCallback(
    (key: OptionKey) => {
      if (!current || completed || !started) return;
      setAnswers((prev) => ({ ...prev, [String(current.id)]: key }));
    },
    [current, completed, started],
  );

  const toggleFlag = () => {
    if (!currentId) return;
    setFlaggedIds((prev) =>
      prev.includes(currentId)
        ? prev.filter((id) => id !== currentId)
        : [...prev, currentId],
    );
  };

  const requestSubmit = () => {
    if (unansweredCount > 0) {
      setShowSubmitConfirm(true);
      return;
    }
    doSubmit();
  };

  // Keyboard shortcuts
  useEffect(() => {
    if (completed || !started) return;
    const onKey = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement | null;
      if (
        target &&
        (target.tagName === "INPUT" ||
          target.tagName === "TEXTAREA" ||
          target.isContentEditable)
      ) {
        return;
      }
      const k = e.key.toLowerCase();
      if (k === "1" || k === "a") {
        e.preventDefault();
        selectOption("A");
      } else if (k === "2" || k === "b") {
        e.preventDefault();
        selectOption("B");
      } else if (k === "3" || k === "c") {
        e.preventDefault();
        selectOption("C");
      } else if (k === "4" || k === "d") {
        e.preventDefault();
        selectOption("D");
      } else if (k === "n") {
        e.preventDefault();
        setIndex((i) => Math.min(questions.length - 1, i + 1));
      } else if (k === "p") {
        e.preventDefault();
        setIndex((i) => Math.max(0, i - 1));
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [completed, started, selectOption, questions.length]);

  const results = quizQuery.data?.results;
  const summary = useMemo(() => {
    if (!results) return null;
    let correct = 0;
    let wrong = 0;
    let unattempted = 0;
    for (const q of results) {
      const s = reviewStatus(q);
      if (s === "correct") correct += 1;
      else if (s === "incorrect") wrong += 1;
      else unattempted += 1;
    }
    return { correct, wrong, unattempted };
  }, [results]);

  const filteredResults = useMemo(() => {
    if (!results) return [];
    if (reviewFilter === "all") return results.map((q, i) => ({ q, i }));
    return results
      .map((q, i) => ({ q, i }))
      .filter(({ q }) => reviewStatus(q) === reviewFilter);
  }, [results, reviewFilter]);

  if (!token) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">Redirecting to login…</p>
    );
  }

  if (quizQuery.isLoading) {
    return <p className="text-sm text-[var(--ink-soft)]">Loading quiz…</p>;
  }

  if (quizQuery.isError || !quizQuery.data) {
    return (
      <div className="space-y-4">
        <p className="text-sm text-[var(--accent)]">Could not load this quiz.</p>
        <Link href="/current-affairs" className="text-sm text-[var(--accent)]">
          ← Back to Current Affairs
        </Link>
      </div>
    );
  }

  const periodLabel = `${quizQuery.data.period_start}${
    quizQuery.data.period_start !== quizQuery.data.period_end
      ? ` – ${quizQuery.data.period_end}`
      : ""
  }`;
  const durationSec = estimatedSecondsForQuestions(quizQuery.data.total);
  const showBriefing =
    !completed && examMode === "simulated" && hydrated && !started;

  const timerWarn =
    remainingSec != null && remainingSec <= 60
      ? "critical"
      : remainingSec != null && remainingSec <= 300
        ? "warn"
        : "ok";

  return (
    <div className="mx-auto max-w-3xl space-y-6 pb-16">
      <div>
        <Link
          href="/current-affairs"
          className="text-sm text-[var(--ink-soft)] hover:text-[var(--ink)]"
        >
          ← Current Affairs
        </Link>
        <h1 className="mt-2 font-[family-name:var(--font-display)] text-3xl">
          {completed ? "Results" : "Quiz"}
        </h1>
        <p className="mt-1 text-sm text-[var(--ink-soft)]">
          {quizQuery.data.mode} · {periodLabel} · {quizQuery.data.total}{" "}
          questions
          {!completed && (
            <>
              {" "}
              · {examMode === "simulated" ? "Simulated" : "Practice"}
            </>
          )}
        </p>
      </div>

      {showBriefing && (
        <div className="space-y-5 border border-[var(--line)] bg-white/60 px-5 py-6">
          <div>
            <h2 className="font-[family-name:var(--font-display)] text-2xl">
              Exam briefing
            </h2>
            <p className="mt-2 text-sm text-[var(--ink-soft)]">
              {periodLabel} · {quizQuery.data.total} questions ·{" "}
              {formatDuration(durationSec)} on the clock
            </p>
          </div>
          <ul className="list-disc space-y-1 pl-5 text-sm text-[var(--ink-soft)]">
            <li>Timer starts when you press Begin and auto-submits at zero.</li>
            <li>
              Keys: <kbd className="font-medium text-[var(--ink)]">1–4</kbd> /{" "}
              <kbd className="font-medium text-[var(--ink)]">A–D</kbd> select ·{" "}
              <kbd className="font-medium text-[var(--ink)]">N</kbd> /{" "}
              <kbd className="font-medium text-[var(--ink)]">P</kbd> next/prev
            </li>
            <li>Use the palette to jump; flag questions to revisit.</li>
          </ul>
          <Button type="button" onClick={beginSimulated}>
            Begin
          </Button>
        </div>
      )}

      {!completed && started && (
        <>
          <div className="sticky top-0 z-20 -mx-1 space-y-3 border-b border-[var(--line)] bg-[var(--paper)]/95 px-1 py-3 backdrop-blur-sm">
            <div className="flex flex-wrap items-center justify-between gap-3 text-sm">
              <span className="text-[var(--ink-soft)]">
                Q {index + 1}/{questions.length} · Answered {answeredCount}/
                {questions.length}
              </span>
              <div className="flex flex-wrap items-center gap-2">
                {examMode === "simulated" && remainingSec != null && (
                  <span
                    className={`font-[family-name:var(--font-display)] text-lg tabular-nums ${
                      timerWarn === "critical"
                        ? "text-red-700"
                        : timerWarn === "warn"
                          ? "text-amber-800"
                          : "text-[var(--accent)]"
                    }`}
                    aria-live="polite"
                  >
                    {formatDuration(remainingSec)}
                  </span>
                )}
                <Button
                  size="sm"
                  disabled={submitMutation.isPending}
                  onClick={requestSubmit}
                >
                  {submitMutation.isPending ? "Submitting…" : "Submit"}
                </Button>
              </div>
            </div>
            <div
              className="flex max-h-28 flex-wrap gap-1.5 overflow-y-auto"
              role="navigation"
              aria-label="Question palette"
            >
              {questions.map((q, i) => {
                const id = String(q.id);
                const answered = id in answers;
                const flagged = flaggedIds.includes(id);
                const isCurrent = i === index;
                return (
                  <button
                    key={id}
                    type="button"
                    onClick={() => setIndex(i)}
                    title={
                      flagged
                        ? `Question ${i + 1} (flagged)`
                        : `Question ${i + 1}`
                    }
                    className={`relative h-8 min-w-8 px-1.5 text-xs font-medium transition-colors ${
                      isCurrent
                        ? "bg-[var(--accent)] text-white"
                        : answered
                          ? "border border-[var(--accent)] bg-[var(--accent-soft)] text-[var(--accent)]"
                          : "border border-[var(--line)] bg-white/70 text-[var(--ink-soft)]"
                    }`}
                  >
                    {i + 1}
                    {flagged && (
                      <span
                        className={`absolute -right-0.5 -top-0.5 h-1.5 w-1.5 rounded-full ${
                          isCurrent ? "bg-white" : "bg-amber-700"
                        }`}
                      />
                    )}
                  </button>
                );
              })}
            </div>
          </div>

          {current && "stem" in current && (
            <div className="space-y-6">
              <div className="flex flex-wrap items-center gap-2">
                {(current as CAQuestionPublic).subject_tag && (
                  <Badge variant="muted">
                    {(current as CAQuestionPublic).subject_tag}
                  </Badge>
                )}
                <Button
                  type="button"
                  size="sm"
                  variant={isFlagged ? "default" : "outline"}
                  onClick={toggleFlag}
                >
                  {isFlagged ? "Flagged" : "Flag"}
                </Button>
              </div>
              <p className="whitespace-pre-line text-lg leading-relaxed text-[var(--ink)]">
                {formatMcqStem((current as CAQuestionPublic).stem)}
              </p>
              <div className="space-y-2" role="radiogroup">
                {OPTIONS.map((key) => {
                  const q = current as CAQuestionPublic;
                  const selected = answers[String(q.id)] === key;
                  return (
                    <button
                      key={key}
                      type="button"
                      role="radio"
                      aria-checked={selected}
                      onClick={() => selectOption(key)}
                      className={`flex w-full items-start gap-3 border px-4 py-3 text-left transition-colors ${
                        selected
                          ? "border-[var(--accent)] bg-[var(--accent-soft)]"
                          : "border-[var(--line)] bg-white/50 hover:border-[var(--ink-soft)]"
                      }`}
                    >
                      <span className="mt-0.5 font-medium text-[var(--accent)]">
                        {key}.
                      </span>
                      <span>{optionText(q, key)}</span>
                    </button>
                  );
                })}
              </div>
              <div className="flex flex-wrap justify-between gap-3">
                <Button
                  variant="outline"
                  disabled={index === 0}
                  onClick={() => setIndex((i) => Math.max(0, i - 1))}
                >
                  Previous
                </Button>
                <Button
                  disabled={index >= questions.length - 1}
                  onClick={() =>
                    setIndex((i) => Math.min(questions.length - 1, i + 1))
                  }
                >
                  Next
                </Button>
              </div>
              {submitMutation.isError && (
                <p className="text-sm text-[var(--accent)]" role="alert">
                  {(submitMutation.error as Error).message}
                </p>
              )}
            </div>
          )}
        </>
      )}

      {completed && results && summary && (
        <div className="space-y-8">
          <div className="space-y-4 border border-[var(--line)] bg-white/60 px-5 py-6">
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="text-sm text-[var(--ink-soft)]">Score</p>
                <p className="font-[family-name:var(--font-display)] text-4xl text-[var(--accent)]">
                  {quizQuery.data.score}/{quizQuery.data.total}
                </p>
                <p className="mt-1 text-sm text-[var(--ink-soft)]">
                  {quizQuery.data.total
                    ? Math.round(
                        ((quizQuery.data.score ?? 0) / quizQuery.data.total) *
                          100,
                      )
                    : 0}
                  %
                </p>
              </div>
              <dl className="grid grid-cols-3 gap-4 text-sm">
                <div>
                  <dt className="text-[var(--ink-soft)]">Correct</dt>
                  <dd className="text-lg font-medium text-[var(--accent)]">
                    {summary.correct}
                  </dd>
                </div>
                <div>
                  <dt className="text-[var(--ink-soft)]">Wrong</dt>
                  <dd className="text-lg font-medium">{summary.wrong}</dd>
                </div>
                <div>
                  <dt className="text-[var(--ink-soft)]">Unattempted</dt>
                  <dd className="text-lg font-medium">{summary.unattempted}</dd>
                </div>
              </dl>
            </div>
            <Link
              href="/current-affairs"
              className="inline-block text-sm text-[var(--accent)] hover:underline"
            >
              ← Back to Current Affairs
            </Link>
          </div>

          <div className="flex flex-wrap gap-2">
            {(
              [
                ["incorrect", "Incorrect"],
                ["all", "All"],
                ["correct", "Correct"],
                ["unattempted", "Unattempted"],
              ] as const
            ).map(([id, label]) => (
              <Button
                key={id}
                size="sm"
                variant={reviewFilter === id ? "default" : "outline"}
                onClick={() => setReviewFilter(id)}
              >
                {label}
                {id === "incorrect" ? ` (${summary.wrong})` : ""}
                {id === "correct" ? ` (${summary.correct})` : ""}
                {id === "unattempted" ? ` (${summary.unattempted})` : ""}
                {id === "all" ? ` (${results.length})` : ""}
              </Button>
            ))}
          </div>

          {filteredResults.length === 0 && (
            <p className="text-sm text-[var(--ink-soft)]">
              No questions in this filter.
            </p>
          )}

          <ol className="space-y-8">
            {filteredResults.map(({ q, i }) => {
              const status = reviewStatus(q);
              return (
                <li
                  key={q.id}
                  className="space-y-3 border-t border-[var(--line)] pt-6"
                >
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-sm text-[var(--ink-soft)]">
                      Q{i + 1}
                    </span>
                    {q.subject_tag && (
                      <Badge variant="muted">{q.subject_tag}</Badge>
                    )}
                    <Badge
                      variant={
                        status === "correct"
                          ? "default"
                          : status === "unattempted"
                            ? "muted"
                            : "outline"
                      }
                    >
                      {status === "correct"
                        ? "Correct"
                        : status === "unattempted"
                          ? "Unattempted"
                          : "Incorrect"}
                    </Badge>
                  </div>
                  {q.source_topic && (
                    <p className="text-xs text-[var(--ink-soft)]">
                      {q.source_topic}
                    </p>
                  )}
                  <p className="whitespace-pre-line leading-relaxed">
                    {formatMcqStem(q.stem)}
                  </p>
                  <ul className="space-y-2">
                    {OPTIONS.map((key) => {
                      const text = optionText(q, key);
                      const isCorrect = q.correct_option === key;
                      const isSelected = q.selected === key;
                      const isWrongPick = isSelected && !isCorrect;
                      return (
                        <li
                          key={key}
                          className={`flex items-start gap-3 border px-4 py-3 text-sm ${
                            isCorrect
                              ? "border-[var(--accent)] bg-[var(--accent-soft)] text-[var(--ink)]"
                              : isWrongPick
                                ? "border-red-800/40 bg-red-50 text-[var(--ink)]"
                                : "border-[var(--line)] bg-white/40 text-[var(--ink-soft)]"
                          }`}
                        >
                          <span className="mt-0.5 font-medium">{key}.</span>
                          <span className="flex-1">{text}</span>
                          {isCorrect && (
                            <span className="shrink-0 text-xs font-medium text-[var(--accent)]">
                              Correct
                            </span>
                          )}
                          {isWrongPick && (
                            <span className="shrink-0 text-xs font-medium text-red-800">
                              Your answer
                            </span>
                          )}
                        </li>
                      );
                    })}
                  </ul>
                  {q.explanation && (
                    <p className="text-sm text-[var(--ink-soft)]">
                      <span className="font-medium text-[var(--ink)]">
                        Explanation:{" "}
                      </span>
                      {q.explanation}
                    </p>
                  )}
                </li>
              );
            })}
          </ol>
        </div>
      )}

      {showSubmitConfirm && (
        <div
          className="fixed inset-0 z-50 flex items-end justify-center bg-black/35 p-4 sm:items-center"
          role="dialog"
          aria-modal="true"
          aria-labelledby="ca-submit-title"
        >
          <div className="w-full max-w-md space-y-4 border border-[var(--line)] bg-[var(--paper)] p-6 shadow-lg">
            <h2
              id="ca-submit-title"
              className="font-[family-name:var(--font-display)] text-xl"
            >
              Submit quiz?
            </h2>
            <p className="text-sm text-[var(--ink-soft)]">
              {unansweredCount} unanswered — submit anyway?
            </p>
            <div className="flex flex-wrap justify-end gap-2">
              <Button
                type="button"
                variant="outline"
                disabled={submitMutation.isPending}
                onClick={() => setShowSubmitConfirm(false)}
              >
                Keep answering
              </Button>
              <Button
                type="button"
                disabled={submitMutation.isPending}
                onClick={() => doSubmit()}
              >
                {submitMutation.isPending ? "Submitting…" : "Submit anyway"}
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default function CAQuizPage() {
  return (
    <Suspense
      fallback={<p className="text-sm text-[var(--ink-soft)]">Loading quiz…</p>}
    >
      <CAQuizPageInner />
    </Suspense>
  );
}
