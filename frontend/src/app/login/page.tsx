"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { Suspense, useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import { Card, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { loginRequest } from "@/lib/api";
import { setTokens } from "@/lib/auth";

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8, "At least 8 characters"),
});

type FormValues = z.infer<typeof schema>;

function LoginForm() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const next = searchParams.get("next") || "/progress";
  const [error, setError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
  });

  const onSubmit = handleSubmit(async (values) => {
    setError(null);
    try {
      const tokens = await loginRequest(values.email, values.password);
      setTokens(tokens.access, tokens.refresh, tokens.role);
      router.push(next);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong");
    }
  });

  return (
    <Card className="mx-auto max-w-md">
      <CardTitle>Log in</CardTitle>
      <p className="mt-2 text-sm text-[var(--ink-soft)]">
        Sign in with your academy account to track progress.
      </p>
      <form onSubmit={onSubmit} className="mt-6 space-y-4">
        <div>
          <Input type="email" placeholder="Email" {...register("email")} />
          {errors.email && (
            <p className="mt-1 text-xs text-red-700">{errors.email.message}</p>
          )}
        </div>
        <div>
          <Input
            type="password"
            placeholder="Password"
            {...register("password")}
          />
          {errors.password && (
            <p className="mt-1 text-xs text-red-700">{errors.password.message}</p>
          )}
        </div>
        {error && <p className="text-sm text-red-700">{error}</p>}
        <Button type="submit" className="w-full" disabled={isSubmitting}>
          {isSubmitting ? "Please wait…" : "Log in"}
        </Button>
      </form>
      <p className="mt-4 text-sm text-[var(--ink-soft)]">
        Have an invite code?{" "}
        <Link href="/join" className="text-[var(--accent)] underline">
          Join this academy
        </Link>
      </p>
      <p className="mt-4 text-xs text-[var(--ink-soft)]">
        <Link href="/" className="underline">
          Back home
        </Link>
      </p>
    </Card>
  );
}

export default function LoginPage() {
  return (
    <Suspense fallback={<p className="text-sm text-[var(--ink-soft)]">Loading…</p>}>
      <LoginForm />
    </Suspense>
  );
}
