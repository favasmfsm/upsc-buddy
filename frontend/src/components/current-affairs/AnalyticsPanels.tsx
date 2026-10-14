"use client";

import type {
  CAScorePoint,
  CAStudentAnalytics,
  CASubjectAccuracy,
  CAWeakTopic,
} from "@/lib/api";

function fmtPct(value: number | null | undefined) {
  if (value == null) return "—";
  return `${value}%`;
}

export function AnalyticsSummaryStrip({
  items,
}: {
  items: { label: string; value: string }[];
}) {
  return (
    <dl className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {items.map((item) => (
        <div key={item.label} className="border-t border-[var(--line)] pt-3">
          <dt className="text-xs uppercase tracking-wide text-[var(--ink-soft)]">
            {item.label}
          </dt>
          <dd className="mt-1 font-[family-name:var(--font-display)] text-2xl text-[var(--ink)]">
            {item.value}
          </dd>
        </div>
      ))}
    </dl>
  );
}

export function ScoreSeries({ series }: { series: CAScorePoint[] }) {
  if (series.length === 0) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">No completed quizzes yet.</p>
    );
  }
  const maxHeight = 96;
  return (
    <div className="space-y-3">
      <div className="flex h-28 items-end gap-1.5 overflow-x-auto pb-1">
        {series.map((point) => {
          const pct = point.accuracy_pct ?? 0;
          const h = Math.max(4, Math.round((pct / 100) * maxHeight));
          return (
            <div
              key={point.attempt_id}
              className="group flex min-w-5 flex-1 flex-col items-center justify-end"
              title={`${point.score}/${point.total} (${fmtPct(point.accuracy_pct)})`}
            >
              <div
                className="w-full max-w-8 rounded-t-sm bg-[var(--ink)]/80 transition-opacity group-hover:opacity-100"
                style={{ height: h }}
              />
            </div>
          );
        })}
      </div>
      <p className="text-xs text-[var(--ink-soft)]">
        Each bar is one quiz (oldest → newest). Hover for score.
      </p>
    </div>
  );
}

export function SubjectBreakdown({ rows }: { rows: CASubjectAccuracy[] }) {
  if (rows.length === 0) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">No subject data yet.</p>
    );
  }
  return (
    <ul className="space-y-3">
      {rows.map((row) => {
        const pct = row.accuracy_pct ?? 0;
        return (
          <li key={row.subject_tag}>
            <div className="mb-1 flex items-baseline justify-between gap-3 text-sm">
              <span className="font-medium text-[var(--ink)]">
                {row.subject_tag}
              </span>
              <span className="text-[var(--ink-soft)]">
                {fmtPct(row.accuracy_pct)} · {row.correct}/{row.total}
              </span>
            </div>
            <div className="h-2 overflow-hidden rounded-full bg-[var(--line)]">
              <div
                className="h-full rounded-full bg-[var(--ink)]"
                style={{ width: `${Math.min(100, pct)}%` }}
              />
            </div>
          </li>
        );
      })}
    </ul>
  );
}

export function WeakTopics({ topics }: { topics: CAWeakTopic[] }) {
  if (topics.length === 0) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">
        Not enough topic signal yet (needs ≥3 answers on a topic).
      </p>
    );
  }
  return (
    <ul className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
      {topics.map((t) => (
        <li
          key={`${t.subject_tag}:${t.source_topic}`}
          className="flex flex-wrap items-baseline justify-between gap-2 py-3 text-sm"
        >
          <div>
            <p className="font-medium text-[var(--ink)]">{t.source_topic}</p>
            <p className="text-[var(--ink-soft)]">{t.subject_tag}</p>
          </div>
          <span className="text-[var(--ink-soft)]">
            {fmtPct(t.accuracy_pct)} · {t.correct}/{t.total}
          </span>
        </li>
      ))}
    </ul>
  );
}

export function StudentAnalyticsPanels({
  data,
}: {
  data: CAStudentAnalytics;
}) {
  return (
    <div className="space-y-10">
      <AnalyticsSummaryStrip
        items={[
          { label: "Attempts", value: String(data.summary.attempts) },
          {
            label: "Questions",
            value: String(data.summary.questions_answered),
          },
          {
            label: "Accuracy",
            value: fmtPct(data.summary.accuracy_pct),
          },
          {
            label: "Avg quiz score",
            value: fmtPct(data.summary.avg_score_pct),
          },
        ]}
      />

      <section className="space-y-3">
        <h3 className="font-[family-name:var(--font-display)] text-xl">
          Score over time
        </h3>
        <ScoreSeries series={data.score_series} />
      </section>

      <section className="space-y-3">
        <h3 className="font-[family-name:var(--font-display)] text-xl">
          By subject
        </h3>
        <SubjectBreakdown rows={data.by_subject} />
      </section>

      <section className="space-y-3">
        <h3 className="font-[family-name:var(--font-display)] text-xl">
          Weak topics
        </h3>
        <WeakTopics topics={data.weak_topics} />
      </section>
    </div>
  );
}
