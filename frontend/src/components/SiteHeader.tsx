"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useCallback, useEffect, useId, useState } from "react";

import {
  clearTokens,
  getAccessToken,
  getRefreshToken,
  getRole,
  isAdminRole,
  isLoggedIn,
  isStaffRole,
  setRole,
} from "@/lib/auth";
import {
  ensureAccessToken,
  fetchAuthMe,
  fetchCurrentAcademy,
  logoutRequest,
  type AcademyBranding,
} from "@/lib/api";
import { academySlugFromHost } from "@/lib/academy";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

type NavKey = "revise" | "practice" | "progress" | "staff" | "branding" | "concepts";

function navActive(pathname: string, key: NavKey): boolean {
  if (key === "revise") {
    return (
      pathname === "/subjects" ||
      pathname.startsWith("/subjects/") ||
      pathname === "/polity" ||
      pathname.startsWith("/chapters/") ||
      pathname.startsWith("/concepts")
    );
  }
  if (key === "practice") {
    return pathname.startsWith("/current-affairs");
  }
  if (key === "progress") {
    return pathname === "/progress" || pathname.startsWith("/progress/");
  }
  if (key === "staff") {
    return pathname.startsWith("/staff/current-affairs");
  }
  if (key === "branding") {
    return pathname.startsWith("/staff/branding");
  }
  if (key === "concepts") {
    return pathname.startsWith("/concepts");
  }
  return false;
}

function linkClass(active: boolean) {
  return cn(
    "transition-colors hover:text-[var(--ink)]",
    active ? "font-medium text-[var(--ink)]" : "text-[var(--ink-soft)]",
  );
}

function applyAcademyTheme(academy: AcademyBranding | null) {
  if (typeof document === "undefined") return;
  const root = document.documentElement;
  if (academy?.primary_color) {
    root.style.setProperty("--accent", academy.primary_color);
  } else {
    root.style.removeProperty("--accent");
  }

  const existing = document.getElementById("academy-favicon");
  if (academy?.favicon_url) {
    let link = existing as HTMLLinkElement | null;
    if (!link) {
      link = document.createElement("link");
      link.id = "academy-favicon";
      link.rel = "icon";
      document.head.appendChild(link);
    }
    link.href = academy.favicon_url;
  } else if (existing) {
    existing.remove();
  }
}

export function SiteHeader() {
  const pathname = usePathname();
  const drawerTitleId = useId();
  const [loggedIn, setLoggedIn] = useState(false);
  const [showStaff, setShowStaff] = useState(false);
  const [showBranding, setShowBranding] = useState(false);
  const [academy, setAcademy] = useState<AcademyBranding | null>(null);
  const [isApex, setIsApex] = useState(true);
  const [loggingOut, setLoggingOut] = useState(false);
  const [drawerOpen, setDrawerOpen] = useState(false);

  useEffect(() => {
    const logged = isLoggedIn();
    setLoggedIn(logged);
    setShowStaff(isStaffRole(getRole()));
    setShowBranding(isAdminRole(getRole()));

    const slug = academySlugFromHost(window.location.host);
    setIsApex(!slug);
    if (slug) {
      fetchCurrentAcademy()
        .then((data) => {
          setAcademy(data);
          applyAcademyTheme(data);
        })
        .catch(() => {
          setAcademy(null);
          applyAcademyTheme(null);
        });
    }

    if ((getAccessToken() || getRefreshToken()) && slug) {
      ensureAccessToken()
        .then((token) => {
          if (!token) {
            setLoggedIn(false);
            setShowStaff(false);
            setShowBranding(false);
            return null;
          }
          return fetchAuthMe(token);
        })
        .then((me) => {
          if (!me) return;
          setLoggedIn(true);
          setRole(me.role);
          setShowStaff(isStaffRole(me.role));
          setShowBranding(isAdminRole(me.role));
        })
        .catch(() => {
          if (!isLoggedIn()) {
            setLoggedIn(false);
            setShowStaff(false);
            setShowBranding(false);
          }
        });
    }
  }, []);

  useEffect(() => {
    setDrawerOpen(false);
  }, [pathname]);

  useEffect(() => {
    if (!drawerOpen) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setDrawerOpen(false);
    };
    window.addEventListener("keydown", onKey);
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", onKey);
      document.body.style.overflow = prev;
    };
  }, [drawerOpen]);

  const handleLogout = useCallback(async () => {
    setLoggingOut(true);
    try {
      await logoutRequest();
    } finally {
      clearTokens();
      setLoggedIn(false);
      setShowStaff(false);
      setShowBranding(false);
      setDrawerOpen(false);
      window.location.href = "/";
    }
  }, []);

  const brand = academy?.display_name || academy?.name || "UPSC Buddy";

  const authLinks = loggedIn ? (
    <Button
      size="sm"
      variant="outline"
      disabled={loggingOut}
      onClick={handleLogout}
    >
      Log out
    </Button>
  ) : (
    <>
      <Link href="/join" className={linkClass(false)} onClick={() => setDrawerOpen(false)}>
        Join
      </Link>
      <Link href="/login" className={linkClass(false)} onClick={() => setDrawerOpen(false)}>
        Log in
      </Link>
    </>
  );

  const primaryLinks = (
    <>
      <Link
        href="/subjects"
        className={linkClass(navActive(pathname, "revise"))}
        onClick={() => setDrawerOpen(false)}
      >
        Revise
      </Link>
      <Link
        href="/concepts"
        className={cn(
          "text-xs",
          linkClass(navActive(pathname, "concepts")),
        )}
        onClick={() => setDrawerOpen(false)}
      >
        Concepts
      </Link>
      <Link
        href="/current-affairs"
        className={linkClass(navActive(pathname, "practice"))}
        onClick={() => setDrawerOpen(false)}
      >
        Practice
      </Link>
      <Link
        href="/progress"
        className={linkClass(navActive(pathname, "progress"))}
        onClick={() => setDrawerOpen(false)}
      >
        Progress
      </Link>
      {showStaff && (
        <Link
          href="/staff/current-affairs"
          className={linkClass(navActive(pathname, "staff"))}
          onClick={() => setDrawerOpen(false)}
        >
          Staff
        </Link>
      )}
      {showBranding && (
        <Link
          href="/staff/branding"
          className={linkClass(navActive(pathname, "branding"))}
          onClick={() => setDrawerOpen(false)}
        >
          Branding
        </Link>
      )}
    </>
  );

  return (
    <header className="sticky top-0 z-40 border-b border-[var(--line)] bg-[var(--paper)]/90 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6">
        <Link
          href="/"
          className="flex items-center gap-2.5 font-[family-name:var(--font-display)] text-2xl tracking-tight text-[var(--ink)]"
          style={
            academy?.primary_color
              ? { color: academy.primary_color }
              : undefined
          }
        >
          {academy?.logo_url ? (
            // eslint-disable-next-line @next/next/no-img-element
            <img
              src={academy.logo_url}
              alt=""
              className="h-8 w-auto max-w-[2.5rem] object-contain"
            />
          ) : null}
          <span>{brand}</span>
        </Link>
        {isApex ? (
          <nav className="text-sm text-[var(--ink-soft)]">
            Academy access only
          </nav>
        ) : (
          <>
            <nav className="hidden items-center gap-5 text-sm md:flex md:gap-6">
              {primaryLinks}
              {authLinks}
            </nav>
            <Button
              type="button"
              size="sm"
              variant="outline"
              className="md:hidden"
              aria-expanded={drawerOpen}
              aria-controls="site-nav-drawer"
              onClick={() => setDrawerOpen((o) => !o)}
            >
              {drawerOpen ? "Close" : "Menu"}
            </Button>
          </>
        )}
      </div>

      {!isApex && drawerOpen && (
        <>
          <button
            type="button"
            className="fixed inset-0 z-40 bg-[var(--ink)]/30 md:hidden"
            aria-label="Close menu"
            onClick={() => setDrawerOpen(false)}
          />
          <div
            id="site-nav-drawer"
            role="dialog"
            aria-modal="true"
            aria-labelledby={drawerTitleId}
            className="fixed inset-y-0 right-0 z-50 flex w-[min(20rem,100%)] flex-col border-l border-[var(--line)] bg-[var(--paper)] px-5 py-6 shadow-lg md:hidden"
          >
            <div className="mb-6 flex items-center justify-between">
              <p
                id={drawerTitleId}
                className="font-[family-name:var(--font-display)] text-lg text-[var(--ink)]"
              >
                Menu
              </p>
              <Button
                type="button"
                size="sm"
                variant="ghost"
                onClick={() => setDrawerOpen(false)}
              >
                Close
              </Button>
            </div>
            <nav className="flex flex-col gap-4 text-base">{primaryLinks}</nav>
            <div className="mt-8 flex flex-wrap items-center gap-4 border-t border-[var(--line)] pt-6 text-sm">
              {authLinks}
            </div>
          </div>
        </>
      )}
    </header>
  );
}
