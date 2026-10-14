"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useMemo, useState } from "react";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import {
  apiAuthGet,
  apiAuthPatch,
  ensureAccessToken,
  type ProgressItem,
} from "@/lib/api";
import { isLoggedIn } from "@/lib/auth";

type ProgressPatch = {
  concept_slug: string;
  status?: ProgressItem["status"];
  is_difficult?: boolean;
};

export function ProgressActions({
  conceptSlug,
  nextConcept,
}: {
  conceptSlug: string;
  nextConcept?: { slug: string; title: string } | null;
}) {
  const router = useRouter();
  const queryClient = useQueryClient();
  const [token, setToken] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [showNext, setShowNext] = useState(false);

  useEffect(() => {
    if (!isLoggedIn()) return;
    ensureAccessToken().then((access) => {
      if (access) setToken(access);
    });
  }, []);

  const progressQuery = useQuery({
    queryKey: ["progress"],
    enabled: Boolean(token),
    queryFn: () =>
      apiAuthGet<ProgressItem[]>("/api/learning/progress/", token!),
  });

  const current = useMemo(
    () =>
      (progressQuery.data || []).find((p) => p.concept_slug === conceptSlug) ??
      null,
    [progressQuery.data, conceptSlug],
  );

  const mutation = useMutation({
    mutationFn: async (patch: ProgressPatch) => {
      if (!isLoggedIn()) {
        router.push(`/login?next=/concepts/${conceptSlug}`);
        throw new Error("login");
      }
      const access = await ensureAccessToken();
      if (!access) {
        router.push(`/login?next=/concepts/${conceptSlug}`);
        throw new Error("login");
      }
      return apiAuthPatch<ProgressItem>("/api/learning/progress/", access, patch);
    },
    onSuccess: (data, variables) => {
      if (variables.status) {
        setMessage(`Marked as ${data.status.replace("_", " ")}`);
        setShowNext(data.status === "studied" && Boolean(nextConcept));
      } else if (variables.is_difficult !== undefined) {
        setMessage(
          data.is_difficult ? "Marked as difficult" : "Removed difficult flag",
        );
      }
      queryClient.invalidateQueries({ queryKey: ["progress"] });
      queryClient.invalidateQueries({ queryKey: ["revise-next"] });
    },
    onError: (err) => {
      if (err.message !== "login") setMessage("Could not update progress");
    },
  });

  const status = current?.status ?? "not_started";
  const isDifficult = Boolean(current?.is_difficult);

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap gap-2">
        <Button
          size="sm"
          variant={status === "studied" ? "default" : "outline"}
          onClick={() =>
            mutation.mutate({ concept_slug: conceptSlug, status: "studied" })
          }
          disabled={mutation.isPending}
        >
          Mark studied
        </Button>
        <Button
          size="sm"
          variant={status === "revise_later" ? "secondary" : "outline"}
          className={
            status === "revise_later"
              ? "bg-[var(--revise-soft)] text-[var(--revise)] hover:opacity-90"
              : undefined
          }
          onClick={() =>
            mutation.mutate({
              concept_slug: conceptSlug,
              status: "revise_later",
            })
          }
          disabled={mutation.isPending}
        >
          Revise later
        </Button>
        <Button
          size="sm"
          variant="outline"
          onClick={() =>
            mutation.mutate({
              concept_slug: conceptSlug,
              status: "not_started",
            })
          }
          disabled={mutation.isPending}
        >
          Reset
        </Button>
        <Button
          size="sm"
          variant="outline"
          className={cn(
            isDifficult &&
              "border-[var(--difficult)] bg-[var(--difficult-soft)] text-[var(--difficult)] hover:bg-[var(--difficult-soft)]",
          )}
          onClick={() =>
            mutation.mutate({
              concept_slug: conceptSlug,
              is_difficult: !isDifficult,
            })
          }
          disabled={mutation.isPending}
        >
          {isDifficult ? "Difficult ✓" : "Difficult"}
        </Button>
      </div>
      {message && (
        <p className="text-xs text-[var(--accent)]">{message}</p>
      )}
      {showNext && nextConcept && (
        <Link href={`/concepts/${nextConcept.slug}`}>
          <Button size="sm" className="w-full">
            Next: {nextConcept.title} →
          </Button>
        </Link>
      )}
    </div>
  );
}
