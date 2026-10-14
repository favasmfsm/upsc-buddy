import ReactMarkdown from "react-markdown";

export function MarkdownBody({ content }: { content: string }) {
  return (
    <div className="prose-upsc space-y-3 text-[var(--ink)] leading-relaxed">
      <ReactMarkdown
        components={{
          h2: ({ children }) => (
            <h2 className="mt-6 font-[family-name:var(--font-display)] text-2xl">
              {children}
            </h2>
          ),
          h3: ({ children }) => (
            <h3 className="mt-4 font-[family-name:var(--font-display)] text-xl">
              {children}
            </h3>
          ),
          p: ({ children }) => <p className="text-[var(--ink-soft)]">{children}</p>,
          ul: ({ children }) => (
            <ul className="list-disc space-y-1 pl-5 text-[var(--ink-soft)]">
              {children}
            </ul>
          ),
          ol: ({ children }) => (
            <ol className="list-decimal space-y-1 pl-5 text-[var(--ink-soft)]">
              {children}
            </ol>
          ),
          strong: ({ children }) => (
            <strong className="font-semibold text-[var(--ink)]">{children}</strong>
          ),
          code: ({ children }) => (
            <code className="rounded bg-[var(--muted)] px-1 py-0.5 text-sm">
              {children}
            </code>
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
