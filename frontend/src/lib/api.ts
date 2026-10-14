import { academySlugFromHost } from "@/lib/academy";
import {
  clearTokens,
  getAccessToken,
  getRefreshToken,
  isAccessTokenExpiringSoon,
  setAccessToken,
  setTokens,
} from "@/lib/auth";

export const API_URL =
  process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "") || "http://127.0.0.1:8300";

let refreshInFlight: Promise<string | null> | null = null;

async function refreshAccessToken(): Promise<string | null> {
  if (refreshInFlight) return refreshInFlight;

  const run = async (): Promise<string | null> => {
    const refresh = getRefreshToken();
    if (!refresh) return null;

    try {
      const academyHeaders = await academyRequestHeaders();
      const res = await fetch(`${API_URL}/api/auth/token/refresh/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...academyHeaders,
        },
        body: JSON.stringify({ refresh }),
      });
      if (!res.ok) {
        clearTokens();
        return null;
      }
      const data = (await res.json()) as {
        access: string;
        refresh?: string;
      };
      if (data.refresh) {
        setTokens(data.access, data.refresh);
      } else {
        setAccessToken(data.access);
      }
      return data.access;
    } catch {
      clearTokens();
      return null;
    }
  };

  refreshInFlight = run().finally(() => {
    refreshInFlight = null;
  });
  return refreshInFlight;
}

/** Return a usable access token, refreshing proactively near expiry. */
export async function ensureAccessToken(
  preferred?: string | null,
): Promise<string | null> {
  const current = preferred || getAccessToken();
  if (current && !isAccessTokenExpiringSoon(current)) {
    return current;
  }
  if (!getRefreshToken()) {
    return current;
  }
  return (await refreshAccessToken()) || current;
}

export async function logoutRequest(): Promise<void> {
  // Refresh first so logout auth succeeds even if access expired.
  // Read refresh after ensure — rotation may have replaced it.
  const access = await ensureAccessToken();
  const refresh = getRefreshToken();
  if (access && refresh) {
    try {
      const academyHeaders = await academyRequestHeaders();
      await fetch(`${API_URL}/api/auth/logout/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${access}`,
          ...academyHeaders,
        },
        body: JSON.stringify({ refresh }),
      });
    } catch {
      /* still clear local session */
    }
  }
  clearTokens();
}

async function authorizedFetch(
  path: string,
  init: RequestInit = {},
  token?: string | null,
): Promise<Response> {
  const academyHeaders = await academyRequestHeaders();
  let access = await ensureAccessToken(token);

  const buildHeaders = (bearer: string | null): HeadersInit => {
    const headers: Record<string, string> = {
      ...academyHeaders,
      ...(init.headers as Record<string, string> | undefined),
    };
    if (bearer) {
      headers.Authorization = `Bearer ${bearer}`;
    }
    return headers;
  };

  let res = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: buildHeaders(access),
  });

  if (res.status === 401 && getRefreshToken()) {
    const refreshed = await refreshAccessToken();
    if (refreshed) {
      res = await fetch(`${API_URL}${path}`, {
        ...init,
        headers: buildHeaders(refreshed),
      });
    }
  }

  if (res.status === 401) {
    clearTokens();
  }

  return res;
}

export type AcademyBranding = {
  id: number;
  name: string;
  slug: string;
  display_name: string;
  tagline: string;
  logo_url: string;
  favicon_url: string;
  primary_color: string;
  is_active: boolean;
};

async function resolveAcademySlug(): Promise<string | null> {
  if (typeof window !== "undefined") {
    return academySlugFromHost(window.location.host);
  }
  try {
    const { headers } = await import("next/headers");
    const h = await headers();
    const fromHeader = h.get("x-academy-slug");
    if (fromHeader) return fromHeader.toLowerCase();
  } catch {
    /* not in a Next request context */
  }
  return null;
}

async function academyRequestHeaders(): Promise<Record<string, string>> {
  const slug = await resolveAcademySlug();
  return slug ? { "X-Academy-Slug": slug } : {};
}

export type Subject = {
  id: number;
  name: string;
  slug: string;
  description: string;
  sort_order: number;
  is_active: boolean;
};

export type ChapterListItem = {
  id: number;
  title: string;
  slug: string;
  sort_order: number;
  book_ref: string;
  summary: string;
  is_published: boolean;
  subject_slug: string;
  section_slug: string | null;
  section_title: string | null;
  concept_count: number;
  updated_at: string;
};

export type SectionWithChapters = {
  id: number;
  title: string;
  slug: string;
  sort_order: number;
  summary: string;
  is_published: boolean;
  chapters: ChapterListItem[];
};

export type ChapterConcept = {
  id: number;
  title: string;
  slug: string;
  summary: string;
  sort_order: number;
};

export type ChapterDetail = {
  id: number;
  title: string;
  slug: string;
  sort_order: number;
  book_ref: string;
  summary: string;
  is_published: boolean;
  subject_slug: string;
  section_slug: string | null;
  section_title: string | null;
  concepts: ChapterConcept[];
  created_at: string;
  updated_at: string;
};

export type ConceptListItem = {
  id: number;
  title: string;
  slug: string;
  summary: string;
  subject_slug: string;
  chapter_slug?: string | null;
  sort_order?: number;
  status: string;
  updated_at: string;
  progress_status?: string;
  is_difficult?: boolean;
};

export type ConceptArticle = {
  id: number;
  ref: string;
  excerpt: string;
  sort_order: number;
};

export type RelatedEdge = {
  id: number;
  relation_type: string;
  target: {
    id: number;
    title: string;
    slug: string;
    summary: string;
  };
};

export type PYQ = {
  id: number;
  year: number;
  question: string;
  answer_key: string;
};

export type VisualMapNode = {
  id: string;
  label: string;
  detail?: string;
  slug?: string;
};

export type VisualMapEdge = {
  from: string;
  to: string;
};

export type VisualFlowOption = {
  label: string;
  next: string;
};

export type VisualFlowStep = {
  id: string;
  label: string;
  detail?: string;
  next?: string;
  options?: VisualFlowOption[];
};

export type VisualComparisonColumn = {
  id: string;
  heading: string;
  points: string[];
};

export type CategorySpineTone =
  | "teal"
  | "olive"
  | "gold"
  | "orange"
  | "terracotta"
  | "maroon";

export type CategorySpineItem = {
  id: string;
  articles: string;
  label: string;
  slug: string;
  detail?: string;
  tone: CategorySpineTone;
};

export type PillarItem = CategorySpineItem;

export type PyqHeatmapItem = {
  concept_slug: string;
  label: string;
  count?: number;
};

export type TreeNode = {
  id: string;
  label: string;
  detail?: string;
  slug?: string;
  children?: TreeNode[];
};

export type TimelineEvent = {
  id: string;
  year: number;
  label: string;
  detail?: string;
};

export type JourneyStage = {
  id: string;
  label: string;
  detail?: string;
  slug?: string;
  case_slug?: string;
};

export type ArticleExplorerStage = {
  id: string;
  label: string;
  detail?: string;
};

export type CaseNetworkCase = {
  id: string;
  label: string;
  year?: number;
  detail?: string;
  case_slug?: string;
};

export type MemoryLocus = {
  id: string;
  place: string;
  association: string;
  detail?: string;
};

export type SimulatorChoice = {
  label: string;
  next: string;
};

export type SimulatorNode = {
  prompt: string;
  choices: SimulatorChoice[];
};

export type ImageMarker = {
  id: string;
  /** Horizontal position as a percentage (0–100) of the image width. */
  x: number;
  /** Vertical position as a percentage (0–100) of the image height. */
  y: number;
  label: string;
  detail?: string;
};

export type CaseLaw = {
  id: number;
  title: string;
  slug: string;
  parties: string;
  year: number;
  court: string;
  summary: string;
  holding: string;
};

export type ConstitutionalAmendment = {
  id: number;
  number: number;
  year: number;
  title: string;
  summary: string;
  effect: string;
};

export type VisualBlock =
  | {
      id: string;
      type: "markdown";
      content: string;
    }
  | {
      id: string;
      type: "map";
      title?: string;
      nodes: VisualMapNode[];
      edges?: VisualMapEdge[];
    }
  | {
      id: string;
      type: "image";
      title?: string;
      src: string;
      alt: string;
      caption?: string;
      /** Attribution / licence line shown under the caption. */
      source?: string;
    }
  | {
      id: string;
      type: "annotated_image";
      title?: string;
      src: string;
      alt: string;
      caption?: string;
      source?: string;
      markers: ImageMarker[];
    }
  | {
      id: string;
      type: "flowchart";
      title?: string;
      root?: string;
      steps: VisualFlowStep[];
    }
  | {
      id: string;
      type: "comparison";
      title?: string;
      columns: VisualComparisonColumn[];
    }
  | {
      id: string;
      type: "callout";
      title?: string;
      body: string;
      tone?: "tip" | "trap" | "note";
    }
  | {
      id: string;
      type: "mental_model";
      title?: string;
      metaphor?: string;
      /** Big topic name under the metaphor (e.g. Fundamental Rights, Salient Features). */
      topic_label?: string;
      subject_label: string;
      /** Line above the list — default "Protects you from". */
      relation_label?: string;
      protects_from: string[];
      insight?: string;
    }
  | {
      id: string;
      type: "pillars";
      title?: string;
      items: PillarItem[];
    }
  | {
      id: string;
      type: "pyq_heatmap";
      title?: string;
      items: PyqHeatmapItem[];
    }
  | {
      id: string;
      type: "tree";
      title?: string;
      root: TreeNode;
    }
  | {
      id: string;
      type: "timeline";
      title?: string;
      events: TimelineEvent[];
    }
  | {
      id: string;
      type: "relation_graph";
      title?: string;
      root_slug: string;
      depth?: number;
    }
  | {
      id: string;
      type: "journey";
      title?: string;
      stages: JourneyStage[];
    }
  | {
      id: string;
      type: "article_explorer";
      title?: string;
      article_ref: string;
      stages: ArticleExplorerStage[];
    }
  | {
      id: string;
      type: "case_network";
      title?: string;
      hub_label: string;
      cases: CaseNetworkCase[];
    }
  | {
      id: string;
      type: "memory_palace";
      title?: string;
      setting: string;
      loci: MemoryLocus[];
    }
  | {
      id: string;
      type: "simulator";
      title?: string;
      start: string;
      nodes: Record<string, SimulatorNode>;
    };

export type ConceptDetail = {
  id: number;
  title: string;
  slug: string;
  summary: string;
  body: string;
  visual_blocks: VisualBlock[];
  subject_slug: string;
  chapter_slug: string | null;
  chapter_title: string | null;
  sort_order: number;
  status: string;
  articles: ConceptArticle[];
  related: RelatedEdge[];
  pyqs: PYQ[];
  case_laws: CaseLaw[];
  amendments: ConstitutionalAmendment[];
  created_at: string;
  updated_at: string;
};

export type GraphPayload = {
  root: string;
  depth: number;
  nodes: { id: number; title: string; slug: string; summary: string }[];
  edges: {
    id: number;
    source_slug: string;
    target_slug: string;
    relation_type: string;
  }[];
};

export type ProgressItem = {
  id: number;
  concept: number;
  concept_slug: string;
  concept_title: string;
  status: "not_started" | "studied" | "revise_later";
  is_difficult: boolean;
  last_studied_at: string | null;
  updated_at: string;
};

export type Paginated<T> = {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
};

async function apiGet<T>(
  path: string,
  token?: string | null,
  init?: RequestInit,
): Promise<T> {
  const academyHeaders = await academyRequestHeaders();
  const headers: HeadersInit = {
    ...academyHeaders,
    ...(init?.headers ?? {}),
  };
  if (token) {
    (headers as Record<string, string>).Authorization = `Bearer ${token}`;
  }
  const { headers: _ignored, ...rest } = init ?? {};
  const res = await fetch(`${API_URL}${path}`, {
    next: rest.cache || rest.next ? undefined : { revalidate: 30 },
    ...rest,
    headers,
  });
  if (!res.ok) {
    throw new Error(`API ${path} failed: ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export function fetchSubjects() {
  return apiGet<Subject[]>("/api/subjects/");
}

export function fetchChapters(subjectSlug: string) {
  return apiGet<ChapterListItem[]>(
    `/api/subjects/${subjectSlug}/chapters/`,
  );
}

export function fetchSections(subjectSlug: string) {
  return apiGet<SectionWithChapters[]>(
    `/api/subjects/${subjectSlug}/sections/`,
  );
}

export function fetchChapter(slug: string) {
  return apiGet<ChapterDetail>(`/api/chapters/${slug}/`);
}

export function fetchConcepts(params?: { subject?: string; q?: string }) {
  const search = new URLSearchParams();
  if (params?.subject) search.set("subject", params.subject);
  if (params?.q) search.set("q", params.q);
  const qs = search.toString();
  return apiGet<Paginated<ConceptListItem>>(
    `/api/concepts/${qs ? `?${qs}` : ""}`,
  );
}

export function fetchConcept(slug: string) {
  return apiGet<ConceptDetail>(`/api/concepts/${slug}/`, null, {
    cache: "no-store",
  });
}

export function fetchConceptGraph(slug: string, depth = 2) {
  return apiGet<GraphPayload>(
    `/api/concepts/${slug}/graph/?depth=${depth}`,
    null,
    { cache: "no-store" },
  );
}

function formatApiError(data: unknown, fallback: string): string {
  if (!data || typeof data !== "object") return fallback;
  const obj = data as Record<string, unknown>;
  if ("detail" in obj) return String(obj.detail);
  for (const key of Object.keys(obj)) {
    const v = obj[key];
    if (Array.isArray(v) && v.length) return String(v[0]);
    if (typeof v === "string") return v;
  }
  return fallback;
}

export async function apiAuthGet<T>(path: string, token: string): Promise<T> {
  const res = await authorizedFetch(
    path,
    { cache: "no-store" },
    token,
  );
  if (!res.ok) {
    throw new Error(`API ${path} failed: ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export async function apiAuthPatch<T>(
  path: string,
  token: string,
  body: unknown,
): Promise<T> {
  const res = await authorizedFetch(
    path,
    {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    },
    token,
  );
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(
      formatApiError(data, `API ${path} failed: ${res.status}`),
    );
  }
  return res.json() as Promise<T>;
}

export async function apiAuthPost<T>(
  path: string,
  token: string,
  body: unknown,
): Promise<T> {
  const res = await authorizedFetch(
    path,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    },
    token,
  );
  if (!res.ok) {
    let detail = `API ${path} failed: ${res.status}`;
    try {
      const data = await res.json();
      if (data && typeof data === "object" && "detail" in data) {
        detail = String((data as { detail: string }).detail);
      }
    } catch {
      /* ignore */
    }
    throw new Error(detail);
  }
  return res.json() as Promise<T>;
}

export type CADocument = {
  id: number;
  doc_type: "daily" | "monthly";
  title: string;
  source_date: string;
  period_start: string;
  period_end: string;
  status: string;
  question_count: number;
  generated_at: string | null;
};

export type StaffCADocument = CADocument & {
  error_message: string;
  published_question_count: number;
  created_at: string;
  updated_at: string;
};

export type StaffCAQuestion = {
  id: number;
  stem: string;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  correct_option: "A" | "B" | "C" | "D";
  explanation: string;
  subject_tag: string;
  source_topic: string;
  is_published: boolean;
  sort_order: number;
};

export type CAQuestionPublic = {
  id: number;
  stem: string;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  subject_tag: string;
  source_topic: string;
  sort_order: number;
};

export type CAQuestionResult = CAQuestionPublic & {
  correct_option: "A" | "B" | "C" | "D";
  explanation: string;
  selected: string | null;
  is_correct: boolean;
};

export type QuizAttemptSummary = {
  id: number;
  mode: "daily" | "monthly" | "range";
  period_start: string;
  period_end: string;
  score: number | null;
  total: number;
  completed_at: string | null;
  created_at: string;
};

export type QuizStartResponse = {
  id: number;
  mode: "daily" | "monthly" | "range";
  period_start: string;
  period_end: string;
  total: number;
  questions: CAQuestionPublic[];
};

export type QuizAttemptDetail = QuizAttemptSummary & {
  questions: CAQuestionPublic[];
  results: CAQuestionResult[] | null;
  answers: Record<string, string>;
};

export type CASubjectAccuracy = {
  subject_tag: string;
  correct: number;
  total: number;
  accuracy_pct: number | null;
};

export type CAWeakTopic = {
  source_topic: string;
  subject_tag: string;
  correct: number;
  total: number;
  accuracy_pct: number | null;
};

export type CAScorePoint = {
  attempt_id: number;
  completed_at: string | null;
  score: number;
  total: number;
  accuracy_pct: number | null;
  mode: "daily" | "monthly" | "range";
};

export type CAStudentAnalytics = {
  days: number;
  summary: {
    attempts: number;
    questions_answered: number;
    accuracy_pct: number | null;
    avg_score_pct: number | null;
  };
  score_series: CAScorePoint[];
  by_subject: CASubjectAccuracy[];
  weak_topics: CAWeakTopic[];
};

export type CAAcademyStudentRow = {
  user_id: number;
  email: string;
  attempts: number;
  accuracy_pct: number | null;
  last_attempt_at: string | null;
};

export type CAAcademyAnalytics = {
  days: number;
  summary: {
    active_students: number;
    total_attempts: number;
    avg_accuracy_pct: number | null;
  };
  by_subject: CASubjectAccuracy[];
  students: CAAcademyStudentRow[];
};

export function fetchCADocuments(docType?: "daily" | "monthly") {
  const qs = docType ? `?doc_type=${docType}` : "";
  return apiGet<CADocument[]>(`/api/current_affairs/documents/${qs}`);
}

export function startCAQuiz(
  token: string,
  body:
    | {
        mode: "daily" | "monthly";
        date: string;
        limit?: number;
        subject_tags?: string[];
      }
    | {
        mode: "range";
        start: string;
        end: string;
        limit?: number;
        subject_tags?: string[];
      },
) {
  return apiAuthPost<QuizStartResponse>(
    "/api/current_affairs/quizzes/start/",
    token,
    body,
  );
}

export function fetchCAQuiz(token: string, id: number) {
  return apiAuthGet<QuizAttemptDetail>(
    `/api/current_affairs/quizzes/${id}/`,
    token,
  );
}

export function submitCAQuiz(
  token: string,
  id: number,
  answers: Record<string, "A" | "B" | "C" | "D">,
) {
  return apiAuthPost<QuizAttemptDetail>(
    `/api/current_affairs/quizzes/${id}/submit/`,
    token,
    { answers },
  );
}

export function fetchCAAttempts(token: string) {
  return apiAuthGet<QuizAttemptSummary[]>(
    "/api/current_affairs/attempts/",
    token,
  );
}

export function fetchCAMyAnalytics(token: string, days = 90) {
  return apiAuthGet<CAStudentAnalytics>(
    `/api/current_affairs/analytics/me/?days=${days}`,
    token,
  );
}

export function fetchCAAcademyAnalytics(token: string, days = 90) {
  return apiAuthGet<CAAcademyAnalytics>(
    `/api/current_affairs/analytics/academy/?days=${days}`,
    token,
  );
}

export function fetchCAAcademyStudentAnalytics(
  token: string,
  userId: number,
  days = 90,
) {
  return apiAuthGet<CAStudentAnalytics>(
    `/api/current_affairs/analytics/academy/students/${userId}/?days=${days}`,
    token,
  );
}

export function fetchStaffCADocuments(
  token: string,
  docType?: "daily" | "monthly",
) {
  const qs = docType ? `?doc_type=${docType}` : "";
  return apiAuthGet<StaffCADocument[]>(
    `/api/current_affairs/staff/documents/${qs}`,
    token,
  );
}

export function fetchStaffCADocument(token: string, id: number) {
  return apiAuthGet<StaffCADocument>(
    `/api/current_affairs/staff/documents/${id}/`,
    token,
  );
}

export async function uploadStaffCADocument(
  token: string,
  body: {
    doc_type: "daily" | "monthly";
    title: string;
    source_date: string;
    file: File;
  },
): Promise<StaffCADocument> {
  const form = new FormData();
  form.append("doc_type", body.doc_type);
  form.append("title", body.title);
  form.append("source_date", body.source_date);
  form.append("file", body.file);
  const res = await authorizedFetch(
    "/api/current_affairs/staff/documents/",
    { method: "POST", body: form },
    token,
  );
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(formatApiError(data, `Upload failed: ${res.status}`));
  }
  return res.json() as Promise<StaffCADocument>;
}

export function regenerateStaffCADocument(token: string, id: number) {
  return apiAuthPost<StaffCADocument>(
    `/api/current_affairs/staff/documents/${id}/regenerate/`,
    token,
    {},
  );
}

export type StaffFinderSyncResponse = {
  task_id: string;
  start: string;
  end: string;
  regenerate: boolean;
  message: string;
};

export async function syncStaffFinderRange(
  token: string,
  body: { start: string; end: string; regenerate?: boolean },
): Promise<StaffFinderSyncResponse> {
  const res = await authorizedFetch(
    "/api/current_affairs/staff/finder/sync/",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    },
    token,
  );
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(formatApiError(data, `FINDER sync failed: ${res.status}`));
  }
  return data as StaffFinderSyncResponse;
}

export async function deleteStaffCADocument(
  token: string,
  id: number,
): Promise<void> {
  const res = await authorizedFetch(
    `/api/current_affairs/staff/documents/${id}/`,
    { method: "DELETE" },
    token,
  );
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(formatApiError(data, `Delete failed: ${res.status}`));
  }
}

export async function replaceStaffCADocument(
  token: string,
  id: number,
  body: { file: File; title?: string },
): Promise<StaffCADocument> {
  const form = new FormData();
  form.append("file", body.file);
  if (body.title?.trim()) {
    form.append("title", body.title.trim());
  }
  const res = await authorizedFetch(
    `/api/current_affairs/staff/documents/${id}/`,
    { method: "PATCH", body: form },
    token,
  );
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(formatApiError(data, `Replace failed: ${res.status}`));
  }
  return res.json() as Promise<StaffCADocument>;
}

export function fetchStaffCAQuestions(token: string, documentId: number) {
  return apiAuthGet<StaffCAQuestion[]>(
    `/api/current_affairs/staff/documents/${documentId}/questions/`,
    token,
  );
}

export function patchStaffCAQuestion(
  token: string,
  questionId: number,
  body: { is_published: boolean },
) {
  return apiAuthPatch<StaffCAQuestion>(
    `/api/current_affairs/staff/questions/${questionId}/`,
    token,
    body,
  );
}

export async function fetchAuthMe(token: string) {
  return apiAuthGet<{
    user: { id: number; email: string; username: string };
    academy: AcademyBranding | null;
    role: string | null;
  }>("/api/auth/me/", token);
}

export function fetchCurrentAcademy() {
  return apiGet<AcademyBranding>("/api/academies/current/", null, {
    cache: "no-store",
  });
}

export function fetchAcademyBrandingAdmin(token: string) {
  return apiAuthGet<AcademyBranding>("/api/academies/current/branding/", token);
}

export async function updateAcademyBranding(
  token: string,
  body: {
    display_name?: string;
    tagline?: string;
    primary_color?: string;
    logo?: File | null;
    favicon?: File | null;
  },
): Promise<AcademyBranding> {
  const form = new FormData();
  if (body.display_name !== undefined) {
    form.append("display_name", body.display_name);
  }
  if (body.tagline !== undefined) {
    form.append("tagline", body.tagline);
  }
  if (body.primary_color !== undefined) {
    form.append("primary_color", body.primary_color);
  }
  if (body.logo) {
    form.append("logo", body.logo);
  }
  if (body.favicon) {
    form.append("favicon", body.favicon);
  }
  const res = await authorizedFetch(
    "/api/academies/current/branding/",
    { method: "PATCH", body: form },
    token,
  );
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error(formatApiError(data, `Update failed: ${res.status}`));
  }
  return res.json() as Promise<AcademyBranding>;
}

export async function loginRequest(email: string, password: string) {
  const academyHeaders = await academyRequestHeaders();
  const res = await fetch(`${API_URL}/api/auth/token/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...academyHeaders,
    },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    const detail =
      typeof data === "object" && data && "detail" in data
        ? String((data as { detail: string }).detail)
        : Array.isArray((data as { non_field_errors?: string[] }).non_field_errors)
          ? String((data as { non_field_errors: string[] }).non_field_errors[0])
          : "Invalid email or password";
    throw new Error(detail);
  }
  return res.json() as Promise<{
    access: string;
    refresh: string;
    academy?: AcademyBranding;
    role?: string;
  }>;
}

export async function joinAcademyRequest(
  email: string,
  password: string,
  inviteCode: string,
  username?: string,
) {
  const academyHeaders = await academyRequestHeaders();
  const res = await fetch(`${API_URL}/api/auth/join/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...academyHeaders,
    },
    body: JSON.stringify({
      email,
      password,
      invite_code: inviteCode,
      username: username || email,
    }),
  });
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    let message = "Could not join academy";
    if (typeof data === "object" && data) {
      if ("detail" in data) message = String((data as { detail: string }).detail);
      else if ("invite_code" in data) {
        const v = (data as { invite_code: string | string[] }).invite_code;
        message = Array.isArray(v) ? v[0] : String(v);
      } else if ("email" in data) {
        const v = (data as { email: string | string[] }).email;
        message = Array.isArray(v) ? v[0] : String(v);
      }
    }
    throw new Error(message);
  }
  return res.json() as Promise<{
    access: string;
    refresh: string;
    academy?: AcademyBranding;
    role?: string;
  }>;
}

/** @deprecated Public signup disabled — use joinAcademyRequest */
export async function signupRequest(
  _email: string,
  _password: string,
  _username?: string,
) {
  throw new Error("Public signup is disabled. Use an invite code to join.");
}
