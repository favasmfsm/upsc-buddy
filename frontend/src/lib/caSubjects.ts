/** Canonical CA subject tags — keep in sync with current_affairs/subjects.py */
export const CA_SUBJECT_TAGS = [
  "Polity",
  "Economy",
  "IR",
  "Environment",
  "S&T",
  "Geography",
  "Defence",
  "History",
  "Society",
  "Other",
] as const;

export type CASubjectTag = (typeof CA_SUBJECT_TAGS)[number];

export const CA_QUESTION_LIMIT_PRESETS = [10, 20, 30] as const;
