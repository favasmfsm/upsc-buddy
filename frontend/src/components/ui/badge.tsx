import { cva, type VariantProps } from "class-variance-authority";
import * as React from "react";

import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex items-center rounded-md px-2 py-0.5 text-xs font-medium",
  {
    variants: {
      variant: {
        default: "bg-[var(--accent-soft)] text-[var(--accent)]",
        muted: "bg-[var(--muted)] text-[var(--ink-soft)]",
        outline: "border border-[var(--line)] text-[var(--ink-soft)]",
        studied: "bg-[var(--studied-soft)] text-[var(--studied)]",
        revise: "bg-[var(--revise-soft)] text-[var(--revise)]",
        difficult: "bg-[var(--difficult-soft)] text-[var(--difficult)]",
      },
    },
    defaultVariants: { variant: "default" },
  },
);

export function Badge({
  className,
  variant,
  ...props
}: React.HTMLAttributes<HTMLSpanElement> &
  VariantProps<typeof badgeVariants>) {
  return (
    <span className={cn(badgeVariants({ variant }), className)} {...props} />
  );
}
