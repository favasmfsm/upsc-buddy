import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

import { academySlugFromHost } from "@/lib/academy";

export function middleware(request: NextRequest) {
  const host = request.headers.get("host") || "localhost";
  const slug = academySlugFromHost(host);
  const { pathname } = request.nextUrl;

  const requestHeaders = new Headers(request.headers);
  if (slug) {
    requestHeaders.set("x-academy-slug", slug);
  }

  // Apex: only allow landing + static; send learning routes home
  if (!slug) {
    const allowed =
      pathname === "/" ||
      pathname.startsWith("/_next") ||
      pathname.startsWith("/favicon");
    if (!allowed) {
      const url = request.nextUrl.clone();
      url.pathname = "/";
      return NextResponse.redirect(url);
    }
    return NextResponse.next({
      request: { headers: requestHeaders },
    });
  }

  // Tenant host: rewrite apex-style home stays; join/login available
  const response = NextResponse.next({
    request: { headers: requestHeaders },
  });
  response.cookies.set("academy_slug", slug, {
    path: "/",
    sameSite: "lax",
  });
  return response;
}

export const config = {
  matcher: [
    "/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};
