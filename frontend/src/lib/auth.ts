"use client";

const ACCESS_KEY = "upsc_buddy_access";
const REFRESH_KEY = "upsc_buddy_refresh";
const ROLE_KEY = "upsc_buddy_role";

/** Refresh access when fewer than this many seconds remain. */
const REFRESH_SKEW_SECONDS = 60;

export function getAccessToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(ACCESS_KEY);
}

export function getRefreshToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(REFRESH_KEY);
}

export function getRole(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(ROLE_KEY);
}

export function setRole(role: string | null | undefined) {
  if (typeof window === "undefined") return;
  if (role) localStorage.setItem(ROLE_KEY, role);
  else localStorage.removeItem(ROLE_KEY);
}

export function setTokens(
  access: string,
  refresh: string,
  role?: string | null,
) {
  localStorage.setItem(ACCESS_KEY, access);
  localStorage.setItem(REFRESH_KEY, refresh);
  if (role !== undefined) setRole(role);
}

export function setAccessToken(access: string) {
  localStorage.setItem(ACCESS_KEY, access);
}

export function clearTokens() {
  localStorage.removeItem(ACCESS_KEY);
  localStorage.removeItem(REFRESH_KEY);
  localStorage.removeItem(ROLE_KEY);
}

export function isLoggedIn() {
  return Boolean(getAccessToken() || getRefreshToken());
}

export function isStaffRole(role: string | null | undefined) {
  return role === "admin" || role === "staff";
}

export function isAdminRole(role: string | null | undefined) {
  return role === "admin";
}

/** Decode JWT payload without verifying signature (client-side expiry hint only). */
export function readJwtExp(token: string): number | null {
  try {
    const part = token.split(".")[1];
    if (!part) return null;
    const json = atob(part.replace(/-/g, "+").replace(/_/g, "/"));
    const payload = JSON.parse(json) as { exp?: number };
    return typeof payload.exp === "number" ? payload.exp : null;
  } catch {
    return null;
  }
}

export function isAccessTokenExpiringSoon(
  token: string | null,
  skewSeconds = REFRESH_SKEW_SECONDS,
): boolean {
  if (!token) return true;
  const exp = readJwtExp(token);
  if (exp == null) return false;
  return exp * 1000 <= Date.now() + skewSeconds * 1000;
}
