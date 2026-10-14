import type { VisualBlock } from "@/lib/api";
import { MarkdownBody } from "@/components/MarkdownBody";

import { AnnotatedImageBlock } from "./AnnotatedImageBlock";
import { ArticleExplorerBlock } from "./ArticleExplorerBlock";
import { CalloutBlock } from "./CalloutBlock";
import { CaseNetworkBlock } from "./CaseNetworkBlock";
import { ComparisonBlock } from "./ComparisonBlock";
import { FlowchartBlock } from "./FlowchartBlock";
import { ImageBlock } from "./ImageBlock";
import { JourneyBlock } from "./JourneyBlock";
import { MapBlock } from "./MapBlock";
import { MemoryPalaceBlock } from "./MemoryPalaceBlock";
import { MentalModelBlock } from "./MentalModelBlock";
import { PillarsBlock } from "./PillarsBlock";
import { PyqHeatmapBlock } from "./PyqHeatmapBlock";
import { RelationGraphBlock } from "./RelationGraphBlock";
import { SimulatorBlock } from "./SimulatorBlock";
import { TimelineBlock } from "./TimelineBlock";
import { TreeBlock } from "./TreeBlock";

export function VisualBlocks({ blocks }: { blocks: VisualBlock[] }) {
  if (!blocks?.length) return null;

  return (
    <div className="space-y-6">
      {blocks.map((block) => {
        switch (block.type) {
          case "mental_model":
            return <MentalModelBlock key={block.id} {...block} />;
          case "pillars":
            return <PillarsBlock key={block.id} {...block} />;
          case "pyq_heatmap":
            return <PyqHeatmapBlock key={block.id} {...block} />;
          case "tree":
            return <TreeBlock key={block.id} {...block} />;
          case "timeline":
            return <TimelineBlock key={block.id} {...block} />;
          case "relation_graph":
            return <RelationGraphBlock key={block.id} {...block} />;
          case "journey":
            return <JourneyBlock key={block.id} {...block} />;
          case "article_explorer":
            return <ArticleExplorerBlock key={block.id} {...block} />;
          case "case_network":
            return <CaseNetworkBlock key={block.id} {...block} />;
          case "memory_palace":
            return <MemoryPalaceBlock key={block.id} {...block} />;
          case "simulator":
            return <SimulatorBlock key={block.id} {...block} />;
          case "map":
            return <MapBlock key={block.id} {...block} />;
          case "image":
            return <ImageBlock key={block.id} {...block} />;
          case "annotated_image":
            return <AnnotatedImageBlock key={block.id} {...block} />;
          case "flowchart":
            return <FlowchartBlock key={block.id} {...block} />;
          case "comparison":
            return <ComparisonBlock key={block.id} {...block} />;
          case "callout":
            return <CalloutBlock key={block.id} {...block} />;
          case "markdown":
            return (
              <div
                key={block.id}
                className="rounded-lg border border-[var(--line)] bg-white/60 p-5"
              >
                <MarkdownBody content={block.content} />
              </div>
            );
          default:
            return null;
        }
      })}
    </div>
  );
}
