const BASE_DOMAIN = (
  process.env.NEXT_PUBLIC_BASE_DOMAIN || "upscbuddy.com"
).toLowerCase();

// Used on hosts outside BASE_DOMAIN (e.g. the *.up.railway.app preview URL)
// so the site is usable before a custom domain is connected.
const DEFAULT_ACADEMY =
  process.env.NEXT_PUBLIC_DEFAULT_ACADEMY?.toLowerCase() || null;

/**
 * Resolve academy slug from hostname.
 * fortuneias.upscbuddy.com / fortuneias.localhost → fortuneias
 * Apex (localhost, upscbuddy.com, www) → null
 */
export function academySlugFromHost(hostname: string): string | null {
  const host = hostname.split(":")[0].toLowerCase();

  if (
    host === "localhost" ||
    host === "127.0.0.1" ||
    host === BASE_DOMAIN ||
    host === `www.${BASE_DOMAIN}`
  ) {
    return null;
  }

  if (host.endsWith(".localhost")) {
    const sub = host.slice(0, -".localhost".length);
    return sub && !sub.includes(".") ? sub : null;
  }

  if (host.endsWith(`.${BASE_DOMAIN}`)) {
    const sub = host.slice(0, -(BASE_DOMAIN.length + 1));
    if (!sub || sub === "www" || sub === "api" || sub.includes(".")) {
      return null;
    }
    return sub;
  }

  return DEFAULT_ACADEMY;
}

export function isApexHost(hostname: string): boolean {
  return academySlugFromHost(hostname) === null;
}
