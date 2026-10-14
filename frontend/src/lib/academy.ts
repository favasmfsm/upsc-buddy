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
    host === "upscbuddy.com" ||
    host === "www.upscbuddy.com"
  ) {
    return null;
  }

  if (host.endsWith(".localhost")) {
    const sub = host.slice(0, -".localhost".length);
    return sub && !sub.includes(".") ? sub : null;
  }

  if (host.endsWith(".upscbuddy.com")) {
    const sub = host.slice(0, -".upscbuddy.com".length);
    if (!sub || sub === "www" || sub === "api" || sub.includes(".")) {
      return null;
    }
    return sub;
  }

  return null;
}

export function isApexHost(hostname: string): boolean {
  return academySlugFromHost(hostname) === null;
}
