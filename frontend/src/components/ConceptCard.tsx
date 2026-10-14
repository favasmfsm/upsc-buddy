import Link from "next/link";

import type { ConceptListItem } from "@/lib/api";
import { progressCardToneClass } from "@/components/ProgressStatusBadges";
import { Badge } from "@/components/ui/badge";
import { Card, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";

export function ConceptCard({ concept }: { concept: ConceptListItem }) {
  const tone = progressCardToneClass(
    concept.progress_status,
    concept.is_difficult,
  );

  return (
    <Link href={`/concepts/${concept.slug}`} className="block transition hover:-translate-y-0.5">
      <Card className={cn("h-full", tone)}>
        <div className="mb-2 flex items-center gap-2">
          <Badge>{concept.subject_slug}</Badge>
        </div>
        <CardTitle>{concept.title}</CardTitle>
        <p className="mt-2 line-clamp-3 text-sm text-[var(--ink-soft)]">
          {concept.summary}
        </p>
      </Card>
    </Link>
  );
}
