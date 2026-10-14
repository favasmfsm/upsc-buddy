"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useMemo, useState } from "react";

import {
  AnalyticsSummaryStrip,
  StudentAnalyticsPanels,
  SubjectBreakdown,
} from "@/components/current-affairs/AnalyticsPanels";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  ensureAccessToken,
  fetchAuthMe,
  fetchCAAcademyAnalytics,
  fetchCAAcademyStudentAnalytics,
  deleteStaffCADocument,
  fetchStaffCADocuments,
  regenerateStaffCADocument,
  replaceStaffCADocument,
  syncStaffFinderRange,
  uploadStaffCADocument,
  type StaffCADocument,
} from "@/lib/api";
import { isLoggedIn, isStaffRole, setRole } from "@/lib/auth";

type LibraryTab = "daily" | "monthly";
type PageTab = "library" | "analytics";

function formatDate(iso: string) {
  return new Date(iso + "T00:00:00").toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

function formatDateTime(iso: string | null) {
  if (!iso) return "—";
  return new Date(iso).toLocaleString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

function statusVariant(
  status: string,
): "default" | "muted" | "outline" {
  if (status === "ready") return "default";
  if (status === "failed") return "outline";
  return "muted";
}

function titleFromFile(file: File) {
  return file.name.replace(/\.pdf$/i, "").replace(/[_]+/g, " ");
}

function fmtPct(value: number | null | undefined) {
  if (value == null) return "—";
  return `${value}%`;
}

export default function StaffCurrentAffairsPage() {
  const router = useRouter();
  const queryClient = useQueryClient();
  const [token, setToken] = useState<string | null>(null);
  const [allowed, setAllowed] = useState(false);
  const [pageTab, setPageTab] = useState<PageTab>("library");
  const [tab, setTab] = useState<LibraryTab>("daily");
  const [title, setTitle] = useState("");
  const [sourceDate, setSourceDate] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [syncMessage, setSyncMessage] = useState<string | null>(null);
  const [syncStart, setSyncStart] = useState("");
  const [syncEnd, setSyncEnd] = useState("");
  const [syncRegenerate, setSyncRegenerate] = useState(false);
  const [analyticsDays, setAnalyticsDays] = useState(90);
  const [selectedStudentId, setSelectedStudentId] = useState<number | null>(
    null,
  );

  useEffect(() => {
    if (!isLoggedIn()) {
      router.replace("/login?next=/staff/current-affairs");
      return;
    }
    ensureAccessToken()
      .then((access) => {
        if (!access) {
          router.replace("/login?next=/staff/current-affairs");
          return null;
        }
        setToken(access);
        return fetchAuthMe(access);
      })
      .then((me) => {
        if (!me) return;
        setRole(me.role);
        if (!isStaffRole(me.role)) {
          router.replace("/current-affairs");
          return;
        }
        setAllowed(true);
      })
      .catch(() => {
        router.replace("/login?next=/staff/current-affairs");
      });
  }, [router]);

  const docsQuery = useQuery({
    queryKey: ["staff-ca-documents", tab],
    queryFn: () => fetchStaffCADocuments(token!, tab),
    enabled: Boolean(token && allowed && pageTab === "library"),
    refetchInterval: (query) => {
      const docs = query.state.data || [];
      const busy = docs.some(
        (d) => d.status === "pending" || d.status === "processing",
      );
      return busy ? 3000 : false;
    },
  });

  const academyAnalyticsQuery = useQuery({
    queryKey: ["ca-analytics-academy", analyticsDays],
    queryFn: () => fetchCAAcademyAnalytics(token!, analyticsDays),
    enabled: Boolean(token && allowed && pageTab === "analytics"),
  });

  const studentDrillQuery = useQuery({
    queryKey: ["ca-analytics-student", selectedStudentId, analyticsDays],
    queryFn: () =>
      fetchCAAcademyStudentAnalytics(token!, selectedStudentId!, analyticsDays),
    enabled: Boolean(
      token && allowed && pageTab === "analytics" && selectedStudentId,
    ),
  });

  const docs = useMemo(() => docsQuery.data || [], [docsQuery.data]);
  const docsBusy = docs.some(
    (d) => d.status === "pending" || d.status === "processing",
  );
  const anyProcessing = docs.some((d) => d.status === "processing");

  const uploadMutation = useMutation({
    mutationFn: () =>
      uploadStaffCADocument(token!, {
        doc_type: tab,
        title: title.trim() || (file ? titleFromFile(file) : "Untitled"),
        source_date:
          tab === "monthly" && sourceDate.length === 7
            ? `${sourceDate}-01`
            : sourceDate,
        file: file!,
      }),
    onSuccess: () => {
      setError(null);
      setFile(null);
      setTitle("");
      setSourceDate("");
      queryClient.invalidateQueries({ queryKey: ["staff-ca-documents"] });
    },
    onError: (e: Error) => setError(e.message),
  });

  const regenerateMutation = useMutation({
    mutationFn: (id: number) => regenerateStaffCADocument(token!, id),
    onSuccess: () => {
      setError(null);
      queryClient.invalidateQueries({ queryKey: ["staff-ca-documents"] });
    },
    onError: (e: Error) => setError(e.message),
  });

  const deleteMutation = useMutation({
    mutationFn: (id: number) => deleteStaffCADocument(token!, id),
    onSuccess: () => {
      setError(null);
      queryClient.invalidateQueries({ queryKey: ["staff-ca-documents"] });
    },
    onError: (e: Error) => setError(e.message),
  });

  const replaceMutation = useMutation({
    mutationFn: ({ id, file }: { id: number; file: File }) =>
      replaceStaffCADocument(token!, id, { file }),
    onSuccess: () => {
      setError(null);
      queryClient.invalidateQueries({ queryKey: ["staff-ca-documents"] });
    },
    onError: (e: Error) => setError(e.message),
  });

  const syncMutation = useMutation({
    mutationFn: () =>
      syncStaffFinderRange(token!, {
        start: syncStart,
        end: syncEnd,
        regenerate: syncRegenerate,
      }),
    onSuccess: (data) => {
      setError(null);
      setSyncMessage(data.message);
      queryClient.invalidateQueries({ queryKey: ["staff-ca-documents"] });
    },
    onError: (e: Error) => {
      setSyncMessage(null);
      setError(e.message);
    },
  });

  const rowBusy =
    regenerateMutation.isPending ||
    deleteMutation.isPending ||
    replaceMutation.isPending;

  if (!token || !allowed) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">Checking access…</p>
    );
  }

  const selectedEmail =
    academyAnalyticsQuery.data?.students.find(
      (s) => s.user_id === selectedStudentId,
    )?.email || null;

  return (
    <div className="mx-auto max-w-3xl space-y-10">
      <header className="space-y-2">
        <p className="text-sm text-[var(--ink-soft)]">
          <Link href="/current-affairs" className="underline">
            Student quizzes
          </Link>
        </p>
        <h1 className="font-[family-name:var(--font-display)] text-4xl tracking-tight text-[var(--ink)]">
          Current Affairs library
        </h1>
        <p className="max-w-2xl text-[var(--ink-soft)]">
          Upload daily FINDER or monthly Prelims Precise PDFs. Questions generate
          automatically — usually 1–3 minutes.
        </p>
      </header>

      <div className="flex gap-2 border-b border-[var(--line)] pb-2">
        {(
          [
            ["library", "Library"],
            ["analytics", "Analytics"],
          ] as const
        ).map(([id, label]) => (
          <button
            key={id}
            type="button"
            onClick={() => {
              setPageTab(id);
              setError(null);
            }}
            className={
              pageTab === id
                ? "rounded-md bg-[var(--ink)] px-3 py-1.5 text-sm text-[var(--paper)]"
                : "rounded-md px-3 py-1.5 text-sm text-[var(--ink-soft)] hover:text-[var(--ink)]"
            }
          >
            {label}
          </button>
        ))}
      </div>

      {pageTab === "analytics" && (
        <section className="space-y-8">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <h2 className="font-[family-name:var(--font-display)] text-2xl">
              Cohort performance
            </h2>
            <label className="text-sm text-[var(--ink-soft)]">
              Window{" "}
              <select
                className="ml-2 h-9 rounded-md border border-[var(--line)] bg-white/70 px-2 text-[var(--ink)]"
                value={analyticsDays}
                onChange={(e) => {
                  setAnalyticsDays(Number(e.target.value));
                  setSelectedStudentId(null);
                }}
              >
                <option value={30}>30 days</option>
                <option value={90}>90 days</option>
                <option value={180}>180 days</option>
                <option value={365}>365 days</option>
              </select>
            </label>
          </div>

          {academyAnalyticsQuery.isLoading && (
            <p className="text-sm text-[var(--ink-soft)]">Loading analytics…</p>
          )}
          {academyAnalyticsQuery.isError && (
            <p className="text-sm text-[var(--accent)]" role="alert">
              {(academyAnalyticsQuery.error as Error).message}
            </p>
          )}

          {academyAnalyticsQuery.data && (
            <>
              <AnalyticsSummaryStrip
                items={[
                  {
                    label: "Active students",
                    value: String(
                      academyAnalyticsQuery.data.summary.active_students,
                    ),
                  },
                  {
                    label: "Attempts",
                    value: String(
                      academyAnalyticsQuery.data.summary.total_attempts,
                    ),
                  },
                  {
                    label: "Avg accuracy",
                    value: fmtPct(
                      academyAnalyticsQuery.data.summary.avg_accuracy_pct,
                    ),
                  },
                ]}
              />

              <div className="space-y-3">
                <h3 className="font-[family-name:var(--font-display)] text-xl">
                  Subjects
                </h3>
                <SubjectBreakdown
                  rows={academyAnalyticsQuery.data.by_subject}
                />
              </div>

              <div className="space-y-3">
                <h3 className="font-[family-name:var(--font-display)] text-xl">
                  Students
                </h3>
                {academyAnalyticsQuery.data.students.length === 0 ? (
                  <p className="text-sm text-[var(--ink-soft)]">
                    No completed attempts in this window.
                  </p>
                ) : (
                  <ul className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
                    {academyAnalyticsQuery.data.students.map((student) => (
                      <li key={student.user_id}>
                        <button
                          type="button"
                          onClick={() =>
                            setSelectedStudentId(
                              selectedStudentId === student.user_id
                                ? null
                                : student.user_id,
                            )
                          }
                          className="flex w-full flex-wrap items-baseline justify-between gap-2 py-3 text-left text-sm hover:text-[var(--accent)]"
                        >
                          <span className="font-medium text-[var(--ink)]">
                            {student.email}
                          </span>
                          <span className="text-[var(--ink-soft)]">
                            {fmtPct(student.accuracy_pct)} · {student.attempts}{" "}
                            attempts · {formatDateTime(student.last_attempt_at)}
                          </span>
                        </button>
                      </li>
                    ))}
                  </ul>
                )}
              </div>

              {selectedStudentId && (
                <div className="space-y-4 border-t border-[var(--line)] pt-8">
                  <div className="flex flex-wrap items-center justify-between gap-2">
                    <h3 className="font-[family-name:var(--font-display)] text-xl">
                      {selectedEmail || "Student"} detail
                    </h3>
                    <Button
                      size="sm"
                      variant="outline"
                      onClick={() => setSelectedStudentId(null)}
                    >
                      Close
                    </Button>
                  </div>
                  {studentDrillQuery.isLoading && (
                    <p className="text-sm text-[var(--ink-soft)]">
                      Loading student…
                    </p>
                  )}
                  {studentDrillQuery.data && (
                    <StudentAnalyticsPanels data={studentDrillQuery.data} />
                  )}
                </div>
              )}
            </>
          )}
        </section>
      )}

      {pageTab === "library" && (
        <>
          <div className="flex gap-2 border-b border-[var(--line)] pb-2">
            {(["daily", "monthly"] as LibraryTab[]).map((t) => (
              <button
                key={t}
                type="button"
                onClick={() => {
                  setTab(t);
                  setSourceDate("");
                  setError(null);
                  setSyncMessage(null);
                }}
                className={
                  tab === t
                    ? "rounded-md bg-[var(--ink)] px-3 py-1.5 text-sm text-[var(--paper)]"
                    : "rounded-md px-3 py-1.5 text-sm text-[var(--ink-soft)] hover:text-[var(--ink)]"
                }
              >
                {t === "daily" ? "Daily" : "Monthly"}
              </button>
            ))}
          </div>

          {error && (
            <p className="text-sm text-[var(--accent)]" role="alert">
              {error}
            </p>
          )}

          {tab === "daily" && (
            <section className="space-y-4">
              <h2 className="font-[family-name:var(--font-display)] text-2xl">
                Sync FINDER range
              </h2>
              <p className="text-sm text-[var(--ink-soft)]">
                Download missing daily PDFs, create documents for gaps, and
                generate quizzes. Turn on regenerate to replace PDFs and re-run
                Gemini for days already in the library (max 62 days).
              </p>
              <form
                className="space-y-3"
                onSubmit={(e) => {
                  e.preventDefault();
                  if (!syncStart || !syncEnd) {
                    setError("From and To dates are required.");
                    return;
                  }
                  setSyncMessage(null);
                  syncMutation.mutate();
                }}
              >
                <div className="flex flex-wrap gap-3">
                  <label className="space-y-1 text-sm text-[var(--ink-soft)]">
                    From
                    <Input
                      type="date"
                      value={syncStart}
                      onChange={(e) => setSyncStart(e.target.value)}
                      required
                    />
                  </label>
                  <label className="space-y-1 text-sm text-[var(--ink-soft)]">
                    To
                    <Input
                      type="date"
                      value={syncEnd}
                      onChange={(e) => setSyncEnd(e.target.value)}
                      required
                    />
                  </label>
                </div>
                <label className="flex items-center gap-2 text-sm text-[var(--ink)]">
                  <input
                    type="checkbox"
                    checked={syncRegenerate}
                    onChange={(e) => setSyncRegenerate(e.target.checked)}
                    className="h-4 w-4"
                  />
                  Regenerate existing days in range
                </label>
                {syncMessage && (
                  <p className="text-sm text-[var(--ink-soft)]" role="status">
                    {syncMessage}
                    {docsBusy ? " Generation in progress…" : ""}
                  </p>
                )}
                <Button
                  type="submit"
                  disabled={
                    syncMutation.isPending || anyProcessing || !syncStart || !syncEnd
                  }
                >
                  {syncMutation.isPending ? "Queuing…" : "Sync FINDER"}
                </Button>
              </form>
            </section>
          )}

          <section className="space-y-4">
            <h2 className="font-[family-name:var(--font-display)] text-2xl">
              Upload {tab === "daily" ? "daily" : "monthly"} PDF
            </h2>
            <form
              className="space-y-3"
              onSubmit={(e) => {
                e.preventDefault();
                if (!file || !sourceDate) {
                  setError("Date and PDF are required.");
                  return;
                }
                uploadMutation.mutate();
              }}
            >
              <Input
                placeholder="Title (optional — defaults from filename)"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
              <Input
                type={tab === "monthly" ? "month" : "date"}
                value={sourceDate}
                onChange={(e) => setSourceDate(e.target.value)}
                required
              />
              <Input
                type="file"
                accept="application/pdf,.pdf"
                onChange={(e) => {
                  const next = e.target.files?.[0] || null;
                  setFile(next);
                  if (next && !title.trim()) setTitle(titleFromFile(next));
                }}
                required
              />
              <Button type="submit" disabled={uploadMutation.isPending}>
                {uploadMutation.isPending ? "Uploading…" : "Upload & generate"}
              </Button>
            </form>
          </section>

          <section className="space-y-4">
            <h2 className="font-[family-name:var(--font-display)] text-2xl">
              {tab === "daily" ? "Daily" : "Monthly"} documents
            </h2>
            {docsQuery.isLoading && (
              <p className="text-sm text-[var(--ink-soft)]">Loading…</p>
            )}
            {docs.length === 0 && !docsQuery.isLoading && (
              <p className="text-sm text-[var(--ink-soft)]">
                No {tab} documents yet. Upload a PDF above.
              </p>
            )}
            <ul className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
              {docs.map((doc) => (
                <DocRow
                  key={doc.id}
                  doc={doc}
                  busy={rowBusy}
                  onRegenerate={() => regenerateMutation.mutate(doc.id)}
                  onDelete={() => {
                    const ok = window.confirm(
                      `Delete “${doc.title}” and all its generated questions? This cannot be undone.`,
                    );
                    if (ok) deleteMutation.mutate(doc.id);
                  }}
                  onReplace={(file) =>
                    replaceMutation.mutate({ id: doc.id, file })
                  }
                />
              ))}
            </ul>
          </section>
        </>
      )}
    </div>
  );
}

function DocRow({
  doc,
  busy,
  onRegenerate,
  onDelete,
  onReplace,
}: {
  doc: StaffCADocument;
  busy: boolean;
  onRegenerate: () => void;
  onDelete: () => void;
  onReplace: (file: File) => void;
}) {
  const processing = doc.status === "processing";
  const inFlight = doc.status === "pending" || processing;
  const canOpenBank =
    doc.question_count > 0 || doc.status === "ready" || doc.status === "failed";
  const canMutate = !busy && !processing;

  return (
    <li className="flex flex-wrap items-start justify-between gap-3 py-4">
      <div className="min-w-0 space-y-1">
        <div className="flex flex-wrap items-center gap-2">
          <p className="font-medium text-[var(--ink)]">{doc.title}</p>
          <Badge variant={statusVariant(doc.status)}>{doc.status}</Badge>
        </div>
        <p className="text-sm text-[var(--ink-soft)]">
          {formatDate(doc.source_date)} · {doc.published_question_count}/
          {doc.question_count} published
        </p>
        {inFlight && (
          <p className="text-xs text-[var(--ink-soft)]">
            Generating questions… (auto-refreshes)
          </p>
        )}
        {doc.status === "failed" && doc.error_message && (
          <p className="text-sm text-[var(--accent)]">{doc.error_message}</p>
        )}
      </div>
      <div className="flex flex-wrap items-center gap-2">
        {canOpenBank && (
          <Link
            href={`/staff/current-affairs/${doc.id}`}
            className="inline-flex h-8 items-center rounded-md border border-[var(--line)] px-3 text-xs hover:bg-[var(--muted)]"
          >
            Question bank
          </Link>
        )}
        {(doc.status === "ready" ||
          doc.status === "failed" ||
          doc.status === "pending") && (
          <label
            className={`inline-flex h-8 cursor-pointer items-center rounded-md border border-[var(--line)] px-3 text-xs hover:bg-[var(--muted)] ${
              !canMutate ? "pointer-events-none opacity-50" : ""
            }`}
          >
            Replace PDF
            <input
              type="file"
              accept="application/pdf,.pdf"
              className="sr-only"
              disabled={!canMutate}
              onChange={(e) => {
                const next = e.target.files?.[0];
                e.target.value = "";
                if (next) onReplace(next);
              }}
            />
          </label>
        )}
        {(doc.status === "ready" || doc.status === "failed") && (
          <Button size="sm" disabled={!canMutate} onClick={onRegenerate}>
            {doc.status === "failed" ? "Retry" : "Regenerate"}
          </Button>
        )}
        {!processing && (
          <Button
            size="sm"
            variant="outline"
            disabled={!canMutate}
            onClick={onDelete}
          >
            Delete
          </Button>
        )}
      </div>
    </li>
  );
}
