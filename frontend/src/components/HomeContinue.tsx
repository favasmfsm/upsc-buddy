"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { Button } from "@/components/ui/button";
import {
  apiAuthGet,
  ensureAccessToken,
  fetchCAAttempts,
  type ConceptListItem,
  type QuizAttemptSummary,
} from "@/lib/api";
import { isLoggedIn } from "@/lib/auth";
import { getLastConcept } from "@/lib/studyStorage";

type ContinueTarget =
  | { kind: "quiz"; href: string; label: string }
  | { kind: "concept"; href: string; label: string }
  | { kind: "fallback"; href: string; label: string };

const FALLBACK: ContinueTarget = {
  kind: "fallback",
  href: "/chapters/fundamental-rights",
  label: "Start Fundamental Rights",
};

function formatDate(iso: string) {
  return new Date(iso + "T00:00:00").toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

export function HomeContinue() {
  const [target, setTarget] = useState<ContinueTarget>(FALLBACK);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    let cancelled = false;

    async function resolve() {
      const last = getLastConcept();
      let incomplete: QuizAttemptSummary | undefined;
      let reviseFirst: ConceptListItem | undefined;

      if (isLoggedIn()) {
        const token = await ensureAccessToken();
        if (token) {
          try {
            const attempts = await fetchCAAttempts(token);
            incomplete = attempts.find((a) => !a.completed_at);
          } catch {
            /* ignore */
          }
          try {
            const revise = await apiAuthGet<ConceptListItem[]>(
              "/api/learning/revise-next/",
              token,
            );
            reviseFirst = revise[0];
          } catch {
            /* ignore */
          }
        }
      }

      if (cancelled) return;

      if (incomplete) {
        const period =
          incomplete.period_start !== incomplete.period_end
            ? `${formatDate(incomplete.period_start)} – ${formatDate(incomplete.period_end)}`
            : formatDate(incomplete.period_start);
        setTarget({
          kind: "quiz",
          href: `/current-affairs/quiz/${incomplete.id}`,
          label: `Resume quiz · ${period}`,
        });
      } else if (last) {
        setTarget({
          kind: "concept",
          href: `/concepts/${last.slug}`,
          label: `Continue ${last.title}`,
        });
      } else if (reviseFirst) {
        setTarget({
          kind: "concept",
          href: `/concepts/${reviseFirst.slug}`,
          label: `Continue ${reviseFirst.title}`,
        });
      } else {
        setTarget(FALLBACK);
      }
      setReady(true);
    }

    void resolve();
    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <div className="mt-8 flex flex-wrap items-center gap-x-5 gap-y-3">
      <Link href={target.href}>
        <Button>{ready ? target.label : "Continue"}</Button>
      </Link>
      <Link
        href="/current-affairs"
        className="text-sm text-[var(--accent)] hover:underline"
      >
        Practice Current Affairs →
      </Link>
    </div>
  );
}
