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
import { joinAcademyRequest } from "@/lib/api";
import { setTokens } from "@/lib/auth";

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8, "At least 8 characters"),
  invite_code: z.string().min(4, "Invite code required"),
});

type FormValues = z.infer<typeof schema>;

function JoinForm() {
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
    defaultValues: {
      invite_code: searchParams.get("code") || "",
    },
  });

  const onSubmit = handleSubmit(async (values) => {
    setError(null);
    try {
      const tokens = await joinAcademyRequest(
        values.email,
        values.password,
        values.invite_code,
      );
      setTokens(tokens.access, tokens.refresh, tokens.role);
      router.push(next);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong");
    }
  });

  return (
    <Card className="mx-auto max-w-md">
      <CardTitle>Join with invite</CardTitle>
      <p className="mt-2 text-sm text-[var(--ink-soft)]">
        Enter the invite code from your academy to create a student account.
      </p>
      <form onSubmit={onSubmit} className="mt-6 space-y-4">
        <div>
          <Input
            type="text"
            placeholder="Invite code"
            autoCapitalize="characters"
            {...register("invite_code")}
          />
          {errors.invite_code && (
            <p className="mt-1 text-xs text-red-700">
              {errors.invite_code.message}
            </p>
          )}
        </div>
        <div>
          <Input type="email" placeholder="Email" {...register("email")} />
          {errors.email && (
            <p className="mt-1 text-xs text-red-700">{errors.email.message}</p>
          )}
        </div>
        <div>
          <Input
            type="password"
            placeholder="Password (min 8 characters)"
            {...register("password")}
          />
          {errors.password && (
            <p className="mt-1 text-xs text-red-700">{errors.password.message}</p>
          )}
        </div>
        {error && <p className="text-sm text-red-700">{error}</p>}
        <Button type="submit" className="w-full" disabled={isSubmitting}>
          {isSubmitting ? "Please wait…" : "Join academy"}
        </Button>
      </form>
      <p className="mt-4 text-sm text-[var(--ink-soft)]">
        Already joined?{" "}
        <Link href="/login" className="text-[var(--accent)] underline">
          Log in
        </Link>
      </p>
    </Card>
  );
}

export default function JoinPage() {
  return (
    <Suspense fallback={<p className="text-sm text-[var(--ink-soft)]">Loading…</p>}>
      <JoinForm />
    </Suspense>
  );
}
