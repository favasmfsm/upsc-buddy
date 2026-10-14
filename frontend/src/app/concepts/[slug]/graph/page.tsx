import Link from "next/link";
import { notFound } from "next/navigation";

import { ConceptGraphView } from "@/components/visuals/RelationGraphBlock";
import { Badge } from "@/components/ui/badge";
import { fetchConceptGraph } from "@/lib/api";

export default async function ConceptGraphPage({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ depth?: string }>;
}) {
  const { slug } = await params;
  const sp = await searchParams;
  const depth = Math.min(4, Math.max(0, Number(sp.depth ?? 2) || 2));

  let payload: Awaited<ReturnType<typeof fetchConceptGraph>>;
  try {
    payload = await fetchConceptGraph(slug, depth);
  } catch {
    notFound();
  }

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-2 text-sm text-[var(--ink-soft)]">
        <Badge>Root: {slug}</Badge>
        <span>{payload.nodes.length} nodes</span>
        <span>{payload.edges.length} edges</span>
        <Link
          href={`/concepts/${slug}`}
          className="text-[var(--accent)] hover:underline"
        >
          Back to concept
        </Link>
      </div>
      <h1 className="font-[family-name:var(--font-display)] text-3xl">
        Relationship graph
      </h1>
      <ConceptGraphView payload={payload} />
    </div>
  );
}
