import type { Metadata } from "next";
import { Fraunces, Source_Sans_3 } from "next/font/google";
import { Providers } from "@/components/Providers";
import { SiteHeader } from "@/components/SiteHeader";
import "./globals.css";

const display = Fraunces({
  subsets: ["latin"],
  variable: "--font-display",
});

const body = Source_Sans_3({
  subsets: ["latin"],
  variable: "--font-body",
});

export const metadata: Metadata = {
  title: "UPSC Buddy",
  description:
    "UPSC made visual — chapter maps, flowcharts, and connected concepts for faster UPSC revision.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${display.variable} ${body.variable} font-[family-name:var(--font-body)] antialiased`}
      >
        <Providers>
          <SiteHeader />
          <main className="mx-auto max-w-6xl px-4 py-10 sm:px-6">{children}</main>
        </Providers>
      </body>
    </html>
  );
}
