import type { GraphPayload } from "@/lib/api";

export type LaidOutNode = {
  slug: string;
  title: string;
  summary: string;
  x: number;
  y: number;
  isRoot: boolean;
  depth: number;
};

export type LaidOutEdge = {
  id: number;
  source_slug: string;
  target_slug: string;
  relation_type: string;
};

const COL_W = 200;
const ROW_H = 88;

export function layoutGraph(payload: GraphPayload): {
  nodes: LaidOutNode[];
  edges: LaidOutEdge[];
  width: number;
  height: number;
} {
  const parentEdges = payload.edges.filter((e) => e.relation_type === "parent");
  const children = new Map<string, string[]>();
  for (const edge of parentEdges) {
    const list = children.get(edge.source_slug) ?? [];
    list.push(edge.target_slug);
    children.set(edge.source_slug, list);
  }

  const slugSet = new Set(payload.nodes.map((n) => n.slug));
  const depth = new Map<string, number>();
  const queue: string[] = [payload.root];
  depth.set(payload.root, 0);

  while (queue.length) {
    const current = queue.shift()!;
    const d = depth.get(current) ?? 0;
    for (const child of children.get(current) ?? []) {
      if (!slugSet.has(child) || depth.has(child)) continue;
      depth.set(child, d + 1);
      queue.push(child);
    }
  }

  let maxDepth = 0;
  for (const d of depth.values()) maxDepth = Math.max(maxDepth, d);
  for (const node of payload.nodes) {
    if (!depth.has(node.slug)) depth.set(node.slug, maxDepth + 1);
  }

  const byDepth = new Map<number, string[]>();
  for (const [slug, d] of depth) {
    const list = byDepth.get(d) ?? [];
    list.push(slug);
    byDepth.set(d, list);
  }

  const positions = new Map<string, { x: number; y: number }>();
  let maxX = 0;
  for (const [d, slugs] of byDepth) {
    const sorted = [...slugs].sort();
    const rowWidth = Math.max(0, (sorted.length - 1) * COL_W);
    sorted.forEach((slug, i) => {
      const x = i * COL_W - rowWidth / 2 + 100;
      positions.set(slug, { x, y: d * ROW_H });
      maxX = Math.max(maxX, x + 160);
    });
  }

  const nodes: LaidOutNode[] = payload.nodes.map((node) => {
    const pos = positions.get(node.slug) ?? { x: 0, y: 0 };
    return {
      slug: node.slug,
      title: node.title,
      summary: node.summary,
      x: pos.x,
      y: pos.y,
      isRoot: node.slug === payload.root,
      depth: depth.get(node.slug) ?? 0,
    };
  });

  const minX = Math.min(...nodes.map((n) => n.x), 0);
  const shifted = nodes.map((n) => ({ ...n, x: n.x - minX + 16 }));
  const width = Math.max(320, ...shifted.map((n) => n.x + 180));
  const height = Math.max(200, (maxDepth + 2) * ROW_H);

  return {
    nodes: shifted,
    edges: payload.edges.map((e) => ({
      id: e.id,
      source_slug: e.source_slug,
      target_slug: e.target_slug,
      relation_type: e.relation_type,
    })),
    width: Math.max(width, maxX - minX + 40),
    height,
  };
}
