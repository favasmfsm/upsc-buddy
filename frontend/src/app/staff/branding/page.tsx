"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  ensureAccessToken,
  fetchAuthMe,
  fetchAcademyBrandingAdmin,
  updateAcademyBranding,
} from "@/lib/api";
import { isAdminRole, isLoggedIn, setRole } from "@/lib/auth";

function normalizeHex(value: string): string {
  const trimmed = value.trim();
  if (!trimmed) return "";
  return trimmed.startsWith("#") ? trimmed : `#${trimmed}`;
}

export default function StaffBrandingPage() {
  const router = useRouter();
  const queryClient = useQueryClient();
  const [token, setToken] = useState<string | null>(null);
  const [allowed, setAllowed] = useState(false);
  const [displayName, setDisplayName] = useState("");
  const [tagline, setTagline] = useState("");
  const [primaryColor, setPrimaryColor] = useState("");
  const [logoFile, setLogoFile] = useState<File | null>(null);
  const [faviconFile, setFaviconFile] = useState<File | null>(null);
  const [logoPreview, setLogoPreview] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    if (!isLoggedIn()) {
      router.replace("/login?next=/staff/branding");
      return;
    }
    ensureAccessToken()
      .then((access) => {
        if (!access) {
          router.replace("/login?next=/staff/branding");
          return null;
        }
        setToken(access);
        return fetchAuthMe(access);
      })
      .then((me) => {
        if (!me) return;
        setRole(me.role);
        if (!isAdminRole(me.role)) {
          router.replace("/staff/current-affairs");
          return;
        }
        setAllowed(true);
      })
      .catch(() => {
        router.replace("/login?next=/staff/branding");
      });
  }, [router]);

  const brandingQuery = useQuery({
    queryKey: ["academy-branding-admin"],
    queryFn: () => fetchAcademyBrandingAdmin(token!),
    enabled: Boolean(token && allowed),
  });

  useEffect(() => {
    const data = brandingQuery.data;
    if (!data) return;
    setDisplayName(data.display_name || data.name || "");
    setTagline(data.tagline || "");
    setPrimaryColor(data.primary_color || "");
    setLogoPreview(data.logo_url || null);
  }, [brandingQuery.data]);

  useEffect(() => {
    if (!logoFile) return;
    const url = URL.createObjectURL(logoFile);
    setLogoPreview(url);
    return () => URL.revokeObjectURL(url);
  }, [logoFile]);

  const saveMutation = useMutation({
    mutationFn: () =>
      updateAcademyBranding(token!, {
        display_name: displayName.trim(),
        tagline: tagline.trim(),
        primary_color: normalizeHex(primaryColor),
        logo: logoFile,
        favicon: faviconFile,
      }),
    onSuccess: (data) => {
      setError(null);
      setSaved(true);
      setLogoFile(null);
      setFaviconFile(null);
      setLogoPreview(data.logo_url || null);
      setPrimaryColor(data.primary_color || "");
      queryClient.setQueryData(["academy-branding-admin"], data);
      queryClient.invalidateQueries({ queryKey: ["academy-branding-admin"] });
    },
    onError: (e: Error) => {
      setSaved(false);
      setError(e.message);
    },
  });

  if (!token || !allowed) {
    return (
      <p className="text-sm text-[var(--ink-soft)]">Checking access…</p>
    );
  }

  const colorForPicker =
    /^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/.test(primaryColor)
      ? primaryColor.length === 4
        ? `#${primaryColor[1]}${primaryColor[1]}${primaryColor[2]}${primaryColor[2]}${primaryColor[3]}${primaryColor[3]}`
        : primaryColor
      : "#1a4d3e";

  return (
    <div className="mx-auto max-w-xl space-y-8">
      <div className="flex items-end justify-between gap-4">
        <div>
          <p className="text-xs uppercase tracking-[0.2em] text-[var(--accent)]">
            Academy admin
          </p>
          <h1 className="mt-1 font-[family-name:var(--font-display)] text-3xl text-[var(--ink)]">
            Branding
          </h1>
          <p className="mt-2 text-sm text-[var(--ink-soft)]">
            Logo, tagline, favicon, and primary color for this academy.
          </p>
        </div>
        <Link
          href="/staff/current-affairs"
          className="text-sm text-[var(--accent)]"
        >
          Staff library
        </Link>
      </div>

      {brandingQuery.isLoading ? (
        <p className="text-sm text-[var(--ink-soft)]">Loading…</p>
      ) : brandingQuery.isError ? (
        <p className="rounded-md bg-[var(--accent-soft)] px-4 py-3 text-sm text-[var(--accent)]">
          Could not load branding settings.
        </p>
      ) : (
        <form
          className="space-y-6"
          onSubmit={(e) => {
            e.preventDefault();
            setSaved(false);
            saveMutation.mutate();
          }}
        >
          <label className="block space-y-2">
            <span className="text-sm font-medium text-[var(--ink)]">
              Display name
            </span>
            <Input
              value={displayName}
              onChange={(e) => setDisplayName(e.target.value)}
              required
              maxLength={120}
            />
          </label>

          <label className="block space-y-2">
            <span className="text-sm font-medium text-[var(--ink)]">
              Tagline
            </span>
            <Input
              value={tagline}
              onChange={(e) => setTagline(e.target.value)}
              maxLength={200}
              placeholder="Short line under your academy name"
            />
          </label>

          <div className="space-y-2">
            <span className="text-sm font-medium text-[var(--ink)]">
              Primary color
            </span>
            <div className="flex items-center gap-3">
              <input
                type="color"
                value={colorForPicker}
                onChange={(e) => setPrimaryColor(e.target.value)}
                className="h-10 w-12 cursor-pointer rounded border border-[var(--line)] bg-transparent p-1"
                aria-label="Pick primary color"
              />
              <Input
                value={primaryColor}
                onChange={(e) => setPrimaryColor(e.target.value)}
                placeholder="#1a4d3e"
                className="font-mono"
              />
            </div>
            <p className="text-xs text-[var(--ink-soft)]">
              Hex color used for the header brand and accent.
            </p>
          </div>

          <div className="space-y-2">
            <span className="text-sm font-medium text-[var(--ink)]">Logo</span>
            {logoPreview ? (
              // eslint-disable-next-line @next/next/no-img-element
              <img
                src={logoPreview}
                alt="Logo preview"
                className="h-16 w-auto max-w-[12rem] object-contain"
              />
            ) : (
              <p className="text-sm text-[var(--ink-soft)]">No logo uploaded.</p>
            )}
            <Input
              type="file"
              accept="image/png,image/jpeg,image/webp,image/gif"
              onChange={(e) => setLogoFile(e.target.files?.[0] || null)}
            />
          </div>

          <div className="space-y-2">
            <span className="text-sm font-medium text-[var(--ink)]">
              Favicon
            </span>
            {brandingQuery.data?.favicon_url && !faviconFile ? (
              // eslint-disable-next-line @next/next/no-img-element
              <img
                src={brandingQuery.data.favicon_url}
                alt="Favicon preview"
                className="h-8 w-8 object-contain"
              />
            ) : null}
            <Input
              type="file"
              accept=".ico,image/png,image/svg+xml,image/webp"
              onChange={(e) => setFaviconFile(e.target.files?.[0] || null)}
            />
            {faviconFile ? (
              <p className="text-xs text-[var(--ink-soft)]">
                Selected: {faviconFile.name}
              </p>
            ) : null}
          </div>

          {error ? (
            <p className="rounded-md bg-[var(--accent-soft)] px-4 py-3 text-sm text-[var(--accent)]">
              {error}
            </p>
          ) : null}
          {saved ? (
            <p className="text-sm text-[var(--accent)]">Branding saved.</p>
          ) : null}

          <Button type="submit" disabled={saveMutation.isPending}>
            {saveMutation.isPending ? "Saving…" : "Save branding"}
          </Button>
        </form>
      )}
    </div>
  );
}
