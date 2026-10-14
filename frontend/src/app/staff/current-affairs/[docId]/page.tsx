"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import Link from "next/link";
import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";

import { Badge } from "@/components/ui/badge";
import {
  ensureAccessToken,
  fetchAuthMe,
  fetchStaffCADocument,
  fetchStaffCAQuestions,
  patchStaffCAQuestion,
  type StaffCAQuestion,
} from "@/lib/api";
import { isLoggedIn, isStaffRole, setRole } from "@/lib/auth";

export default function StaffQuestionBankPage() {
  const router = useRouter();
  const params = useParams();
  const docId = Number(params.docId);
  const queryClient = useQueryClient();
  const [token, setToken] = useState<string | null>(null);
  const [allowed, setAllowed] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isLoggedIn()) {
      router.replace(`/login?next=/staff/current-affairs/${docId}`);
      return;
    }
    ensureAccessToken()
      .then((access) => {
        if (!access) {
          router.replace(`/login?next=/staff/current-affairs/${docId}`);
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
        router.replace(`/login?next=/staff/current-affairs/${docId}`);
      });
  }, [router, docId]);

  const docQuery = useQuery({
    queryKey: ["staff-ca-document", docId],
    queryFn: () => fetchStaffCADocument(token!, docId),
    enabled: Boolean(token && allowed && Number.isFinite(docId)),
  });

  const questionsQuery = useQuery({
    queryKey: ["staff-ca-questions", docId],
    queryFn: () => fetchStaffCAQuestions(token!, docId),
    enabled: Boolean(token && allowed && Number.isFinite(docId)),
  });

  const toggleMutation = useMutation({
    mutationFn: ({
      id,
      is_published,
    }: {
      id: number;
      is_published: boolean;
    }) => patchStaffCAQuestion(token!, id, { is_published }),
    onSuccess: (updated) => {
      setError(null);
      queryClient.setQueryData<StaffCAQuestion[]>(
        ["staff-ca-questions", docId],
        (prev) =>
          (prev || []).map((q) => (q.id === updated.id ? updated : q)),
      );
      queryClient.invalidateQueries({ queryKey: ["staff-ca-documents"] });
      queryClient.invalidateQueries({
        queryKey: ["staff-ca-document", docId],
      });
    },
    onError: (e: Error) => setError(e.message),
  });

  if (!token || !allowed) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">Checking access…</p>
    );
  }

  const doc = docQuery.data;
  const questions = questionsQuery.data || [];

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      <header className="space-y-2">
        <p className="text-sm text-[var(--ink-soft)]">
          <Link href="/staff/current-affairs" className="underline">
            ← Library
          </Link>
        </p>
        <h1 className="font-[family-name:var(--font-display)] text-4xl tracking-tight text-[var(--ink)]">
          {doc?.title || "Question bank"}
        </h1>
        {doc && (
          <p className="text-sm text-[var(--ink-soft)]">
            {doc.doc_type} · {doc.source_date} · {doc.status} ·{" "}
            {doc.published_question_count}/{doc.question_count} published
          </p>
        )}
      </header>

      {error && (
        <p className="text-sm text-[var(--accent)]" role="alert">
          {error}
        </p>
      )}

      {questionsQuery.isLoading && (
        <p className="text-sm text-[var(--ink-soft)]">Loading questions…</p>
      )}

      {!questionsQuery.isLoading && questions.length === 0 && (
        <p className="text-sm text-[var(--ink-soft)]">
          No questions yet. Wait for generation to finish, or regenerate from
          the library.
        </p>
      )}

      <ul className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
        {questions.map((q, index) => (
          <li key={q.id} className="space-y-3 py-5">
            <div className="flex flex-wrap items-start justify-between gap-3">
              <p className="font-medium text-[var(--ink)]">
                <span className="text-[var(--ink-soft)]">{index + 1}. </span>
                {q.stem}
              </p>
              <label className="flex shrink-0 items-center gap-2 text-sm text-[var(--ink-soft)]">
                <input
                  type="checkbox"
                  checked={q.is_published}
                  disabled={toggleMutation.isPending}
                  onChange={(e) =>
                    toggleMutation.mutate({
                      id: q.id,
                      is_published: e.target.checked,
                    })
                  }
                />
                Published
              </label>
            </div>
            <div className="grid gap-1 text-sm text-[var(--ink-soft)] sm:grid-cols-2">
              <p>
                <span className="font-medium text-[var(--ink)]">A.</span>{" "}
                {q.option_a}
              </p>
              <p>
                <span className="font-medium text-[var(--ink)]">B.</span>{" "}
                {q.option_b}
              </p>
              <p>
                <span className="font-medium text-[var(--ink)]">C.</span>{" "}
                {q.option_c}
              </p>
              <p>
                <span className="font-medium text-[var(--ink)]">D.</span>{" "}
                {q.option_d}
              </p>
            </div>
            <div className="flex flex-wrap gap-2">
              <Badge>Answer {q.correct_option}</Badge>
              {q.subject_tag && <Badge variant="muted">{q.subject_tag}</Badge>}
              {q.source_topic && (
                <Badge variant="outline">{q.source_topic}</Badge>
              )}
            </div>
            {q.explanation && (
              <p className="text-sm text-[var(--ink-soft)]">{q.explanation}</p>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
