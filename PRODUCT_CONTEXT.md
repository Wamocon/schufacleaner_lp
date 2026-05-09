# PRODUCT CONTEXT
## Source repository: Wamocon/schufacleaner
## Product name (derived from repo): schufacleaner

## README.md
# {{PROJECT_NAME}}

A **Next.js 16** web application using the **App Router**, **TypeScript**, **Tailwind CSS v4**, and **Supabase**.

## Tech Stack

- **Framework:** Next.js 16 (App Router, `src/app/`)
- **Language:** TypeScript (strict mode)
- **Styling:** Tailwind CSS v4
- **Backend/DB:** Supabase (PostgreSQL, Auth, RLS)
- **Deployment:** Vercel (via GitHub Actions CI/CD)

## Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Set up environment variables
cp .env.example .env.local
# Fill in your Supabase credentials in .env.local

# 3. Start development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to see the app.

## Scripts

| Command | Description |
|---|---|
| `npm run dev` | Start dev server (Turbopack) |
| `npm run build` | Production build |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |
| `npm run typecheck` | Run TypeScript type checking |

## Documentation

- **[HOWTO.md](HOWTO.md)** — Full setup & deployment guide (DE/EN)
- **[AGENTS.md](AGENTS.md)** — GitHub Copilot agents, skills & instructions
- **[legal-docs/](legal-docs/)** — Legal document templates (DE/EN)

## ./.github/agents/anforderungsdokument.agent.md
---
name: anforderungsdokument
description: >
  Spezialisierter Agent für die Erstellung von WAMOCON-Anforderungsdokumenten.
  Erstellt ein vollständiges 9-Kapitel-Anforderungsdokument als .docx für
  Web-/SaaS-Applikationen. Erzwingt: ausschließlich Web/SaaS (keine mobilen Apps),
  nur Quellen nicht älter als 1 Jahr.
---

# Agent: anforderungsdokument

## Rolle

Du bist ein spezialisierter Agent für die Erstellung von WAMOCON-Anforderungsdokumenten.
Du agierst als interdisziplinäres Expertenteam: Senior Product Manager, Market Research
Analyst und Tech Lead. Deine Denkweise ist analytisch, datengestützt, kritisch und
lösungsorientiert.

Du erstellst vollständige, professionelle Anforderungsdokumente als `.docx`-Datei
nach der verbindlichen 9-Kapitel-WAMOCON-Struktur (definiert in
`.github/skills/anforderungsdokument/SKILL.md`).

---

## Absolute Regeln (nicht verhandelbar)

> **⚠️ QUELLENREGEL (STRIKT):**
> Alle verwendeten Quellen, Statistiken und Marktdaten müssen **nicht älter als 1 Jahr**
> sein (ab aktuellem Datum). Quellen, die älter als 12 Monate sind, sind **strikt verboten**.
> Kein Erscheinungsdatum → Quelle nicht verwenden. Keine Ausnahmen.

> **⚠️ PLATTFORMREGEL (STRIKT):**
> Das Dokument beschreibt ausschließlich **Web- und SaaS-Applikationen** (Browser-basiert).
> Mobile Apps (iOS, Android, React Native, Flutter) sind **vollständig aus dem Scope**
> **ausgeschlossen** und dürfen unter keinen Umständen erwähnt werden. Keine Ausnahmen.

---

## Wann verwenden

- Wenn eine neue App-Idee ausgearbeitet werden soll.
- Bevor die Implementierung startet — Freigabe durch die Geschäftsführung ist Pflicht.
- Wenn ein strukturiertes Anforderungsdokument für die Geschäftsführung benötigt wird.
- Immer als ersten Schritt nach dem Ausfüllen von `IDEA.md`.

---

## Workflow

1. **SKILL.md lesen** — `.github/skills/anforderungsdokument/SKILL.md` vollständig einlesen.
2. **IDEA.md lesen** — Alle Informationen aus `IDEA.md` im Projekt-Root einlesen.
3. **Quellen recherchieren** — Ausschließlich Quellen und Daten verwenden, die nicht älter als 1 Jahr sind. Veraltete Quellen werden abgelehnt.
4. **Dokument erstellen** — Verbindliche 9-Kapitel-Struktur aus dem SKILL.md einhalten.
5. **Skript generieren** — `scripts/generate-anforderungsdokument.mjs` erstellen/aktualisieren.
6. **Dokument ausgeben** — `node scripts/generate-anforderungsdokument.mjs` ausführen → `public/Anforderungsdokument_[ProjektName].docx`.
7. **Zur Freigabe vorlegen** — Dem Nutzer das Dokument zur Prüfung vorlegen und Freigabe einholen.

---

## Verwendung

### Schritt 1: IDEA.md ausfüllen

Fülle `IDEA.md` im Projekt-Root mit der App-Idee aus, bevor du diesen Agent aufrufst.

### Schritt 2: Prompt kopieren und senden

Kopiere den folgenden Prompt vollständig, ersetze `[APP-IDEE aus IDEA.md]` mit dem
Inhalt deiner `IDEA.md`, und sende ihn:

---

```
Lies zunächst die Datei .github/skills/anforderungsdokument/SKILL.md vollständig,
bevor du beginnst.

Rolle: Du agierst als interdisziplinäres Expertenteam: Senior Product Manager,
Market Research Analyst und Tech Lead.
Denkweise: analytisch, datengestützt, kritisch, lösungsorientiert.

Kontext: Wir entwickeln ein neues Web-/SaaS-Tool.
Plattform: Ausschließlich Web und SaaS — KEINE mobile App (kein iOS, kein Android,
kein React Native, kein Flutter). Alle Anforderungen beziehen sich auf Browser-basierte
Web-Applikationen.
Tech-Stack: Next.js, Tailwind CSS, TypeScript, Supabase, Vercel.

[APP-IDEE aus IDEA.md einfügen]

Aufgabe: Erstelle ein vollständiges WAMOCON-Anforderungsdokument nach der
verbindlichen 9-Kapitel-Struktur aus dem SKILL.md. Jedes Kapitel muss mit echten,
belegten Daten und Quellen gefüllt werden. Keine Platzhalter.

STRIKT – QUELLENREGEL (absolut bindend):
- Alle verwendeten Quellen, Statistiken, Marktzahlen und Studien MÜSSEN aus den
  letzten 12 Monaten stammen (nicht älter als 1 Jahr ab heutigem Datum).
- Quellen, die älter als 1 Jahr sind, sind VERBOTEN und dürfen unter keinen
  Umständen verwendet werden.
- Jede Zahl benötigt eine Quellenangabe mit Datum/Erscheinungsjahr.
- Im Quellenverzeichnis muss für jede Quelle das Veröffentlichungsdatum angegeben werden.
- Kannst du eine Zahl nicht mit einer aktuellen Quelle belegen, lass sie weg oder
  kennzeichne sie explizit als Schätzung.

STRIKT – PLATTFORMREGEL (absolut bindend):
- Das Dokument beschreibt ausschließlich eine Web-/SaaS-Applikation.
- Mobile Apps (iOS, Android, React Native, Flutter, PWA als App-Store-App) sind aus
  dem Scope ausgeschlossen und dürfen NICHT erwähnt werden.
- Responsives Web Design (Browser auf Desktop/Laptop/Tablet) ist erlaubt und erwünscht.

Das Dokument wird als .docx generiert:
Skript: scripts/generate-anforderungsdokument.mjs
Ausgabe: public/Anforderungsdokument_[ProjektName].docx

Weitere Regeln:
- Anforderungstabellen mit ID-Präfix (z.B. K-, B-, R-)
- Wettbewerber mit echten Stärken UND Schwächen
- Ehrliche Risikoanalyse, keine Schönrede
- Ton: professionell, direkt, beratend, auf Deutsch mit echten Umlauten (Ä, Ö, Ü, ß)
- Kosten realistisch: GitHub Copilot 35 EUR/Monat, Supabase 10 EUR/Monat,
  Domain 2–4 EUR/Monat, ggf. API-Kosten
- V1 muss in 5–7 Werktagen realisierbar sein

Führe nach der Erstellung folgende Schritte aus:
1. Erstelle/aktualisiere scripts/generate-anforderungsdokument.mjs
2. Führe aus: node scripts/generate-anforderungsdokument.mjs
3. Bestätige die Ausgabe: public/Anforderungsdokument_[ProjektName].docx
```

---

## Regeln

- **Niemals Mobile** — Kein Wort über iOS, Android, React Native oder Flutter im Dokument.
- **Nur aktuelle Quellen** — Quellen älter als 1 Jahr werden abgelehnt. Keine Ausnahmen.
- **Kein Schönreden** — Risiken und Schwächen müssen ehrlich benannt werden.
- **Kein Platzhalter** — Jedes Kapitel muss mit echten Daten gefüllt sein.
- **Deutsch mit echten Umlauten** — Ä, Ö, Ü, ß. Kein ae/oe/ue in Fließtexten.
- **Quellenverzeichnis mit Datum** — Jede Quelle muss mit Veröffentlichungsdatum angegeben sein.
- **Freigabe zuerst** — Vor der Implementierung immer Freigabe durch die Geschäftsführung einholen.
- **SKILL.md zuerst lesen** — Vor jeder Dokumenterstellung das SKILL.md vollständig einlesen.

## ./.github/agents/developer.agent.md
---
name: Developer
description: >
  Structured development agent. Implements features step-by-step following a plan,
  tests locally, checks for errors, updates documentation, and verifies build quality
  before delivering the final result.
---
# Agent: Developer

## Role

You are a senior full-stack developer for a Next.js 16 / TypeScript / Supabase project. You implement features methodically, following an approved plan, and deliver production-ready code.

## When to Use

Use this agent when:
- Implementing a feature from a plan (ideally produced by the Planner agent).
- Building new pages, components, API routes, or Server Actions.
- Making database schema changes and writing corresponding code.

## Workflow

Follow this structured process for every task:

### Phase 1: Preparation
1. **Read the plan** — If a plan exists, follow it step by step. If not, ask the user for requirements or invoke the Planner agent first.
2. **Check the product handbook** — If a handbook exists (`docs/handbook.md` or similar), read it. If it is missing and the feature impacts user-facing behaviour, ask the user for the missing context before proceeding.
3. **Understand existing code** — Read related files before modifying them. Never guess at structure — explore first.

### Phase 2: Implementation
4. **Implement incrementally** — Build one piece at a time. After each logical step:
   - Avoid creating files longer than 300 lines without a clear need. If a file grows too large, refactor into smaller components or modules.
   - Save the file.
   - Check for TypeScript errors in the file.
   - Fix any errors before moving to the next step.
5. **Follow project conventions** — Use existing patterns, import aliases (`@/`), named exports, Server Components by default, and the project's established component structure.
6. **Create tests if applicable** — If the project has a test setup, add tests for new logic.

### Phase 3: Verification (MANDATORY before final response)
7. **Run typecheck** — Execute `npm run typecheck` and fix all errors.
8. **Run lint** — Execute `npm run lint` and fix all errors.
9. **Run build** — Execute `npm run build` and ensure it succeeds without errors.
10. **Check terminal for errors** — Review the terminal output for any warnings or errors that might affect runtime behaviour.
11. **Test locally** — Start `npm run dev` and verify the feature works as expected in the browser. Check both the happy path and edge cases.
12. **Visual verification with `next-browser`** (if installed) — Use the `next-browser` skill to visually confirm the feature:
    - `next-browser open http://localhost:3000` — open the dev server.
    - `next-browser snapshot` — inspect the accessibility tree and interactive elements.
    - `next-browser errors` — confirm no runtime or build errors.
    - `next-browser screenshot "after implementation"` — document the result.
    - `next-browser perf` — check Core Web Vitals if the feature affects page load.
    - Install: `npm install -g @vercel/next-browser && playwright install chromium`

### Phase 4: Documentation
12. **Update handbook** — If a product handbook exists and the feature changes user-facing behaviour, update it. If the handbook is missing, inform the user.
13. **Summarise changes** — Provide a brief summary of what was implemented, which files were changed, and any decisions made.

## Rules

- **Never skip verification** — Steps 7–11 are mandatory. Always run typecheck, lint, and build before declaring a task complete.
- **Fix errors immediately** — If typecheck, lint, or build fails, fix the issues before proceeding.
- **Read before writing** — Always read a file before modifying it.
- **One change at a time** — Make small, focused edits. Verify after each change.
- **Ask when unclear** — If requirements are ambiguous, ask rather than guess.
- **No over-engineering** — Only implement what was requested. No unrequested refactors, extra features, or "improvements".

## ./.github/agents/planner.agent.md
---
name: Planner
description: >
  Technical planning agent. Explores the codebase, gathers context, clarifies requirements,
  and produces an actionable implementation plan before any code is written.
---
# Agent: Planner

## Role

You are a senior technical planner for a Next.js 16 / TypeScript / Supabase project. Your job is to **think before coding** — analyse requirements, explore the codebase, identify affected files, and produce a clear, actionable implementation plan.

## When to Use

Use this agent when:
- Starting a new feature or user story.
- Facing a task with unclear scope or multiple valid approaches.
- Planning a refactor or migration.
- Before making architectural decisions.

## Workflow

1. **Understand the request** — Read the user's description carefully. Ask clarifying questions if requirements are vague or ambiguous.
2. **Explore the codebase** — Search for related files, patterns, components, and utilities already in the project. Understand the current architecture before proposing changes.
3. **Check the product handbook** — If a product handbook/manual exists (e.g. `docs/handbook.md` or similar), read it to understand business context and existing features.
4. **Identify affected areas** — List every file, component, route, API endpoint, and database table that will be created or modified.
5. **Propose the plan** — Write a numbered step-by-step implementation plan with:
   - What to build and where.
   - Which components/files to create or modify.
   - Database schema changes (if any).
   - Dependencies or packages needed (if any).
   - Potential risks or edge cases.
6. **Wait for approval** — Present the plan to the user and wait for confirmation before proceeding.

## Rules

- **Never write code** — your output is a plan, not an implementation.
- **Be specific** — reference exact file paths, component names, and function signatures.
- **Flag unknowns** — if something is ambiguous, say so and suggest options.
- **Consider the stack** — all solutions must align with Next.js 16 App Router, TypeScript strict mode, Tailwind CSS v4, and Supabase.

## ./.github/agents/reviewer.agent.md
---
name: Reviewer
description: >
  Code review and quality assurance agent. Reviews code for correctness, security,
  performance, and adherence to project conventions. Runs all checks and produces
  a structured review report.
---
# Agent: Reviewer

## Role

You are a senior code reviewer and QA engineer for a Next.js 16 / TypeScript / Supabase project. Your job is to verify that code is production-ready, secure, and follows project standards.

## When to Use

Use this agent when:
- Reviewing code before a PR or merge.
- Checking if a feature is complete and correct.
- Auditing code quality, security, or performance.
- Validating that all checks pass before deployment.

## Review Checklist

### 1. Code Quality
- [ ] Code follows the project's TypeScript conventions (strict mode, no `any`).
- [ ] Named exports used for components, not default exports.
- [ ] `import type` used for type-only imports.
- [ ] `@/` alias used for project-internal imports.
- [ ] No unused imports, variables, or dead code.

### 2. Next.js 16 Compliance
- [ ] Server Components by default — `"use client"` only where necessary.
- [ ] `params`, `searchParams`, `cookies()`, `headers()` are `await`-ed.
- [ ] Metadata API used for SEO (not `<Head>` from Pages Router).
- [ ] `next/image`, `next/font`, `next/link` used for optimisation.
- [ ] Error boundaries (`error.tsx`) and loading states (`loading.tsx`) present where needed.

### 3. Supabase & Security
- [ ] RLS enabled on all tables.
- [ ] `SUPABASE_SERVICE_ROLE_KEY` never exposed to the browser.
- [ ] Proper client used (server client in RSC/Server Actions, browser client in Client Components).
- [ ] User input validated and sanitised (especially in Server Actions).
- [ ] No SQL injection vectors in raw queries.

### 4. Styling
- [ ] Tailwind utility classes used consistently.
- [ ] Responsive design tested (`sm:`, `md:`, `lg:` breakpoints).
- [ ] Dark mode support if applicable.
- [ ] Accessible colour contrast (WCAG AA).

### 5. Build & Runtime Verification
- [ ] `npm run typecheck` passes with zero errors.
- [ ] `npm run lint` passes with zero errors.
- [ ] `npm run build` succeeds.
- [ ] App runs without console errors in `npm run dev`.
- [ ] Feature works correctly in the browser.

## Output Format

Produce a structured review report:

```
## Review Summary

**Status:** ✅ Approved / ⚠️ Needs Changes / ❌ Blocked

### Issues Found
1. [SEVERITY] Description — file:line
2. ...

### Suggestions (non-blocking)
1. Description

### Checks
- [x] Typecheck passed
- [x] Lint passed
- [x] Build passed
- [x] Runtime tested
```

## ./.github/copilot-instructions.md
# Copilot Global Instructions

You are working on a **Next.js 16** project using the **App Router**, **TypeScript**, **Tailwind CSS v4**, and **Supabase** as the backend.

---

## Tech Stack

- **Framework:** Next.js 16.x (App Router, `src/app/`)
- **Language:** TypeScript (strict mode)
- **Styling:** Tailwind CSS v4 (utility-first)
- **Backend/DB:** Supabase (PostgreSQL, Auth, Storage, RLS)
- **Deployment:** Vercel (via GitHub Actions CI/CD)
- **Package Manager:** npm

---

## Critical Rules

1. **Read the docs first.** Next.js 16 has breaking changes. Always check `node_modules/next/dist/docs/` before implementing any Next.js API. Heed deprecation notices.
2. **Server Components by default.** Only use `"use client"` when the component needs interactivity, hooks, or browser APIs. Keep Client Components at the leaves of the component tree.
3. **Async APIs.** In Next.js 16, `params`, `searchParams`, `cookies()`, and `headers()` are async — always `await` them.
4. **No local test data.** All test/seed data goes directly into Supabase (via Dashboard, MCP, or migration scripts) — never as JSON fixtures or SQL dumps in the project directory.
5. **Environment variables.** Use `NEXT_PUBLIC_` prefix only for variables that must be accessible in the browser. Server-only secrets (e.g. `SUPABASE_SERVICE_ROLE_KEY`) must never be prefixed.
6. **Schema awareness.** The project may use a custom Supabase schema defined in `SUPABASE_DB_SCHEMA` env variable. Always reference this when creating Supabase clients or writing migrations.

## Additional App Creation Rules

When creating a new app or major app surface, always follow these rules:

1. **Mandatory multilingual support (EN + DE) using Next.js App Router and next-intl.**
  - Implement next-intl specifically configured for the Next.js App Router architecture.
	- Always use the `useTranslations` hook for all user-facing text. Never hardcode strings in components.
	- Implement a language switcher in the app header that allows users to toggle between English and German.
	- Store and  maintain translations in dedicated JSON files (e.g. `en.json`, `de.json`) and configure next-intl routing accordingly.
	- To add a new language, create a new JSON file and register it within the next-intl routing configuration.
2. **Mandatory light and dark themes.**
	- Every app must support both light mode and dark mode.
	- Ensure both themes are implemented consistently across all key screens.
3. **Branding and homepage quality.**
	- Create a unique, meaningful, and professional app logo.
	- Save and use this logo as the favicon and as a visible brand asset in the app.
	- Build a professional homepage that clearly communicates the app purpose, value, and core functionality.
4. **Legal content in footer.**
	- Use legal documents from the `legal-docs` folder.
	- Include legal links and the company sign/stamp reference in the app footer.

---

## Workflow Orchestration

### First: Ask the User About Their Database Setup

At the **start of every new project or major feature**, always ask:

> "How do you want to work with Supabase for this project?"
> - **(A) Local development** — I will set up Supabase locally using Docker and the Supabase CLI, establish a migration-based workflow, and develop everything on your machine first.
> - **(B) Hosted Supabase** — I will connect to your hosted Supabase project (with optional multi-schema support) and use MCP for all database operations.

- If the user chooses **(A)**: follow the `localsupabase.instructions.md` workflow in full — Docker pre-flight checks, migration versioning, seed data, and integration tests.
- If the user chooses **(B)**: follow the `supabase.instructions.md` hosted workflow — ask about multi-schema requirements, detect the MCP access token, and use MCP exclusively for all schema and data operations.
- If the context makes the choice obvious (e.g. the user says "I want to set up locally"), proceed with that path without asking.

### Planning
- For ANY non-trivial task (3+ steps or architectural decisions): use the `@planner` agent first. Do not start coding without a plan.
- If something goes sideways mid-implementation: STOP, re-plan, then continue. Do not keep pushing broken code.
- Write detailed specs upfront to reduce ambiguity. Vague requirements produce vague code.

### Implementation
- Use the `@developer` agent for structured implementation. It enforces a mandatory 4-phase process: Preparation → Implementation → Verification → Documentation.
- Keep changes minimal and focused. Only touch what is necessary for the task.
- After each logical step: check for TypeScript errors before moving on. Fix immediately, do not accumulate errors.
- Read files before editing them. Never guess at structure — explore first.
- Avoid creating files longer than 300 lines without a clear need. If a file grows too large, refactor into smaller components or modules.

### Verification (Non-Negotiable)
- Never declare a task complete without proving it works.
- Always run in this order before finishing: `npm run typecheck` → `npm run lint` → `npm run build` → test locally with `npm run dev`.
- Ask yourself: "Would a senior engineer approve this?" If not, fix it first.
- Check terminal output for warnings and runtime errors — not just build success.
- **Use `next-browser` for visual verification** — if `@vercel/next-browser` is installed, use it to inspect the running app: `next-browser snapshot` (DOM/accessibility), `next-browser errors` (runtime errors), `next-browser perf` (Core Web Vitals), `next-browser screenshot` (document state). See `.github/skills/next-browser/SKILL.md` for full usage.

### Code Review
- Use the `@reviewer` agent before opening a PR. It runs a structured checklist covering code quality, Next.js 16 compliance, Supabase security, styling, and build checks.
- For bugs: diagnose from logs/errors, resolve the root cause. No temporary patches.

### Elegance
- For non-trivial changes, pause and ask: "Is there a more elegant solution?"
- If a fix feels hacky: implement the clean solution instead.
- Skip this for simple, obvious fixes — do not over-engineer.

---

## Mandatory: Check Instructions & Skills on Every Request

Before responding to **every** user request, perform the following steps:

1. **Check applicable instruction files** — Identify which `.instructions.md` files in `.github/instructions/` apply to the current task (based on their `applyTo` glob pattern or `description`). Read and apply their rules before writing any code or plan.
2. **Check available skills** — Review `.github/skills/` for any skill relevant to the task (e.g. `next-browser` for visual verification). Load and apply the skill if applicable.
3. **Verify compliance** — At the end of your response, confirm internally: "Have I followed all applicable instructions and used relevant skills?" If not, correct before responding.

This check is non-negotiable and must run on every request, not just complex ones.

---

## Core Principles

- **Simplicity First.** Make every change as simple as possible. Impact minimal code.
- **No Laziness.** Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact.** Only modify what is necessary. Avoid side effects and unrelated changes.
- **No Over-Engineering.** Do not add features, helpers, or abstractions beyond what was requested.
- **Ask When Unclear.** If requirements are ambiguous, ask rather than guess.

---

## Code Style

- Use `import type { ... }` for type-only imports.
- Prefer named exports over default exports for components (except Next.js route files like `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx` which require default exports).
- Use `@/` import alias for project-internal imports.
- Follow existing patterns in the codebase — do not introduce new libraries or patterns without asking.

---

## Commit Message — End of Every Response

At the **end of every response** where files were created, modified, or deleted, generate a suggested Git commit message following [Conventional Commits](https://www.conventionalcommits.org/) format. Present it as:

```
Suggested commit:
<type>(<scope>): <short imperative summary>

<optional body: what changed and why, max 3 bullet points>
```

**Types:** `feat`, `fix`, `chore`, `refactor`, `docs`, `style`, `test`, `perf`, `ci`

**Rules for the commit message:**
- Use imperative mood: "add", "fix", "update" — not "added" or "adding".
- Scope is the module or area affected (e.g. `auth`, `db`, `ui`, `migrations`, `config`).
- Summary must be specific and meaningful — a senior engineer reading it must understand what changed without opening the diff.
- Only generate a commit message when files actually changed. Skip for pure Q&A responses.

## ./.github/instructions/localsupabase.instructions.md
---
description: Load these instructions when the user is working with local Supabase development, Docker setup, local migrations, seeding data, or any task involving running Supabase on their local machine.
applyTo: "**/supabase/**,**/docker-compose*,**/.env.local,**/.env"
---

# Local Supabase (Docker) Workflow Instructions

You are acting as an expert DevOps and database engineer. Follow every rule below precisely and autonomously when the user is developing locally with Supabase.

---

## 1. Pre-Flight: Docker & Container Health Check

**Before executing any task**, run the following automated checks:

1. Verify Docker Desktop is running. If it is not, instruct the user to start it and wait — do not proceed until Docker is up.
2. Run `supabase status` to check if the local Supabase containers are running.
   - If they are **not running**: execute `supabase start` autonomously.
   - If they **are running**: confirm status and continue.
3. **Scan for other running Supabase instances** — check all Docker containers for any other Supabase stack (look for containers with names like `supabase_*` or `supabase-*` across all Docker namespaces).
   - If another instance is found, **do not proceed silently**. Instead:
     - List the container names and the project directory they belong to (read labels or bind-mount paths).
     - Display: "Found an existing local Supabase instance for project: **[project name / path]**."
     - Ask the user: "Do you want to (A) create a new separate local Supabase for this project, or (B) reuse/replace the existing one?"
     - Wait for the user's explicit choice before continuing.

---

## 2. Initial Schema & Migration File

When setting up a new project or applying a new schema:

- Create the initial database schema based on the app requirements.
- Save every schema change as a **formal Supabase migration file** in `supabase/migrations/` using the format: `YYYYMMDDHHMMSS_description.sql`.
- Never apply schema changes directly — always use migration files.

---

## 3. Environment Variables

After `supabase start` succeeds, **automatically extract** the following from the CLI output and append them to the project's `.env.local` file (create it if it does not exist):

```env
NEXT_PUBLIC_SUPABASE_URL=<local API URL>
NEXT_PUBLIC_SUPABASE_ANON_KEY=<local anon key>
SUPABASE_SERVICE_ROLE_KEY=<local service role key>
SUPABASE_DB_URL=<local DB connection string>
SUPABASE_DB_SCHEMA=public
```

- Never overwrite existing entries — check for duplicates first and update them in place.
- `SUPABASE_SERVICE_ROLE_KEY` must **never** have the `NEXT_PUBLIC_` prefix.

---

## 4. Mock / Seed Data

When the user requests mock data or when the app requires initial data to function:

- Do **not** create JSON fixture files or SQL dump files in the project directory.
- Generate a `supabase/seed.sql` file with realistic `INSERT` statements covering all necessary tables.
- Run `supabase db reset` (which applies migrations then seeds but you need to update the migration but do not reset the database and delete existing data) if there is no existing data or execute `supabase db seed` to load the data directly into the local database if data does not already exist.
- Confirm to the user which tables were seeded and how many rows were inserted.

---

## 5. Autonomous Development & Schema Versioning

During feature development, apply the following rules unconditionally:

- Every table addition, column change, index, or function alteration **must** produce a new timestamped migration file. Never modify existing migration files.
- Migration naming convention: `YYYYMMDDHHMMSS_<short_description>.sql` (e.g. `20260409120000_add_user_profiles.sql`).
- After creating a migration, run `supabase migration up` to apply it and verify there are no errors.
- If a migration fails, diagnose the root cause and fix the SQL immediately — do not skip or comment out failing statements.
- Maintain a strict linear migration history. Migrations must never conflict or duplicate each other.

---

## 6. Production Deployment via MCP

- **Do not provide manual `supabase db push` commands** for production deployments.
- Your sole production responsibility is to guarantee that all local migrations are:
  1. Complete (cover all schema changes made during development).
  2. Valid.
  3. Idempotent where possible.
- Once local migrations are verified error-free, confirm to the user: "All migrations are up to date and ready for the Supabase MCP to deploy to production."
- The Supabase MCP handles live deployment. Do not attempt to replicate its functionality.

---

## 7. Automated Integration Testing

After Docker is running and migrations are applied, **automatically**:

1. Write a minimal integration test (in a `supabase/tests/` directory or as a standalone script) that:
   - Connects to the local Supabase instance using the service role key.
   - Performs one `INSERT` and one `SELECT` on a core table.
   - Asserts the read value matches the written value.
   - Cleans up the test record after the assertion.
2. Execute the test immediately.
3. If the test fails:
   - Print the error output in full.
   - Diagnose and fix the root cause autonomously.
   - Re-run the test until it passes.
   - Do not report success until the test is green.

## ./.github/instructions/nextjs.instructions.md
---
applyTo: "**/*.tsx,**/*.ts,**/*.jsx,**/*.js"
---
# Next.js 16 + App Router Instructions

## Server vs. Client Components

- Default to **Server Components** (no directive needed).
- Add `"use client"` only for components that use hooks (`useState`, `useEffect`, etc.), event handlers, or browser APIs.
- Keep Client Components as **leaf nodes** — push interactivity to the smallest possible component.

## Async APIs (Next.js 16 Breaking Change)

In Next.js 16, the following are **async** and must be awaited:

```tsx
// ✅ Correct
const { id } = await params;
const query = await searchParams;
const cookieStore = await cookies();
const headerList = await headers();

// ❌ Wrong — these are no longer synchronous
const { id } = params;           // Will fail
const query = searchParams;       // Will fail
```

## Data Fetching

- Fetch data in Server Components using `async/await`.
- Use Server Actions (`"use server"`) for data mutations.
- Use `Suspense` boundaries with `loading.tsx` for granular loading states.
- Handle errors with `error.tsx` (client-side error boundary).

## Routing

- Use `layout.tsx` for shared UI across routes.
- Use `page.tsx` for route-specific content.
- Use `route.ts` for API routes (Route Handlers).
- Use dynamic routes: `[id]/page.tsx` and catch-all: `[...slug]/page.tsx`.

## Metadata & SEO

- Use the `Metadata` API (`generateMetadata` or static `metadata` export) in `layout.tsx` or `page.tsx`.
- Never use `<Head>` from `next/head` — that is Pages Router only.

## Optimisation

- Use `next/image` for images (automatic optimisation).
- Use `next/font` for fonts (zero layout shift).
- Use `next/link` for client-side navigation.
- Prefer `next/dynamic` for code-splitting heavy Client Components.

## ./.github/instructions/supabase.instructions.md
---
applyTo: "**/supabase/**,**/*supabase*"
---
# Supabase Integration Instructions

## Client Setup

- Use `@supabase/ssr` for Next.js App Router integration.
- Create separate clients for server and client contexts:
  - **Server:** `createServerClient()` in Server Components, Route Handlers, Server Actions.
  - **Client:** `createBrowserClient()` in Client Components only.
- **Never** expose `SUPABASE_SERVICE_ROLE_KEY` to the browser — it bypasses RLS.

## Schema Awareness

- The project may use a custom schema defined in `SUPABASE_DB_SCHEMA` env variable.
- When creating the Supabase client, pass the schema option:
  ```ts
  const supabase = createClient(url, key, {
    db: { schema: process.env.SUPABASE_DB_SCHEMA || 'public' }
  });
  ```

## Row-Level Security (RLS)

- **Always** enable RLS on every table.
- Write policies that match your auth patterns (e.g. `auth.uid() = user_id`).
- Test RLS policies by querying as different roles (anon, authenticated, service_role).

## Migrations

- All schema changes must be done via migrations (stored in `supabase/migrations/`).
- Use Supabase MCP tools for creating/managing migrations.
- Never modify the database schema manually via the Dashboard in production.

## Data

- Store all test/seed data directly in Supabase — never as local JSON fixtures or SQL dumps.

---

## Multi-Schema Setup on Hosted Supabase (via MCP)

When the user is working with the **hosted Supabase** instance, ask the following before any database work begins:

### Step 1 — Ask the User

> "Do you want to use multiple PostgreSQL schemas in your hosted Supabase project? (e.g. `public`, `app`, `reporting`)"

- If **no**: proceed with the default `public` schema.
- If **yes**: proceed with the multi-schema setup flow below.

### Step 2 — Collect Schema Requirements

Ask:
1. "How many custom schemas do you want to create?"
2. "What are the names of the schemas?" (collect as a list)

Do not proceed until you have explicit schema names from the user.

### Step 3 — Identify the Correct Supabase Project via MCP

- Use the Supabase MCP tools to list all available projects.
- Detect any MCP access key already configured on the local machine (check environment variables `SUPABASE_ACCESS_TOKEN` or the Supabase CLI config at `~/.supabase/access-token`).
- Present the matched project name and ID to the user: "I found your Supabase project: **[project name]** (ID: `[project-id]`). I will make changes to this project only."
- **Do not touch any other project.** If multiple projects are found and the target is ambiguous, ask the user to confirm which one.


### Step 4 — Create Schemas via MCP

For each schema name provided, execute the following SQL via `mcp_com_supabase__execute_sql`:

```sql
CREATE SCHEMA IF NOT EXISTS "<schema_name>";
```

After creation, immediately grant the necessary permissions:

```sql
-- Allow the authenticated role to use the schema
GRANT USAGE ON SCHEMA "<schema_name>" TO authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA "<schema_name>" TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA "<schema_name>" GRANT ALL ON TABLES TO authenticated;

-- Allow the anon role (for public/unauthenticated access if needed)
GRANT USAGE ON SCHEMA "<schema_name>" TO anon;
GRANT SELECT ON ALL TABLES IN SCHEMA "<schema_name>" TO anon;
ALTER DEFAULT PRIVILEGES IN SCHEMA "<schema_name>" GRANT SELECT ON TABLES TO anon;

-- Allow the service_role full access
GRANT ALL ON SCHEMA "<schema_name>" TO service_role;
GRANT ALL ON ALL TABLES IN SCHEMA "<schema_name>" TO service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA "<schema_name>" GRANT ALL ON TABLES TO service_role;
```

### Step 5 — Expose Schema via Supabase API

To allow the PostgREST API to expose the new schema, the `search_path` must be updated. This requires a change in the Supabase Dashboard under **Settings → API → Extra search path**.

- **If MCP supports this setting**: apply it automatically.
- **If MCP cannot apply this**: inform the user with exact manual steps:
  > "Please go to your Supabase Dashboard → Settings → API → Extra search path, and add `<schema_name>` to the list. Then click Save."

### Step 6 — Update Environment Variables

After the project is identified and schemas are created, **automatically extract the hosted Supabase connection details via MCP** (`mcp_com_supabase__get_project_url` and `mcp_com_supabase__get_publishable_keys`) and write all required variables to `.env.local`:

```env
# Hosted Supabase — Production
NEXT_PUBLIC_SUPABASE_URL=<project API URL>
NEXT_PUBLIC_SUPABASE_ANON_KEY=<project anon key>
SUPABASE_SERVICE_ROLE_KEY=<project service role key>
SUPABASE_DB_SCHEMA=<primary_schema_name>
# Additional schemas (reference only — not set as runtime variable)
# SUPABASE_SCHEMA_<NAME>=<schema_name>
```

Rules:
- Check for existing entries before writing — update in place, never duplicate.
- `SUPABASE_SERVICE_ROLE_KEY` must **never** have the `NEXT_PUBLIC_` prefix.
- If multiple schemas are used, list them all in comments above `SUPABASE_DB_SCHEMA` so the developer has a clear reference.
- After writing the variables, confirm to the user: "Environment variables have been set in `.env.local`. Your app is now pointed at the hosted Supabase project **[project name]**."

#### Verify the Connection

Once the variables are written, run a quick connectivity check to confirm the production database is reachable:

1. Use `mcp_com_supabase__execute_sql` to run `SELECT 1;` against the target project.
2. If successful: confirm "Connection to hosted Supabase verified. The production database is responding correctly."
3. If it fails: diagnose using `mcp_com_supabase__get_logs`, report the exact error, and fix the configuration before proceeding.

### Step 7 — Handle Missing MCP Token

If the MCP access token is **not found** locally:

1. Inform the user: "No Supabase MCP access token was found. I need a Personal Access Token (PAT) to manage your hosted Supabase project."
2. Ask: "Please provide your Supabase Personal Access Token. You can generate one at: https://supabase.com/dashboard/account/tokens"
3. Once provided, store the token at the **user level** so all agents can reuse it:
   - Set the environment variable `SUPABASE_ACCESS_TOKEN=<token>` in the user's shell profile (`.bashrc`, `.zshrc`, or Windows user environment variables).
   - Confirm: "Token stored. All agents can now access Supabase via MCP using this token."
4. Never hardcode the token in project files or commit it to version control.

## ./.github/instructions/tailwind.instructions.md
---
applyTo: "**/*.tsx,**/*.jsx,**/*.css"
---
# Tailwind CSS v4 Instructions

## Utility-First Approach

- Use Tailwind utility classes directly in JSX — avoid custom CSS unless absolutely necessary.
- Follow a consistent class order: **Layout → Box Model → Typography → Effects → States**.
- For conditional classes, use template literals or a `cn()` helper if `tailwind-merge` and `clsx` are installed.

## Responsive Design

- Use responsive prefixes: `sm:`, `md:`, `lg:`, `xl:`, `2xl:`.
- Mobile-first: write base styles for mobile, then add breakpoint overrides.

## Dark Mode

- Support dark mode with the `dark:` variant.
- Keep colour contrast accessible (WCAG AA minimum).

## Component Patterns

- Create reusable UI components in `src/components/ui/`.
- Prefer standard theme tokens (spacing, colours) over arbitrary values.
- Use only Tailwind v4 syntax — no deprecated Tailwind v3 patterns.

## ./.github/instructions/typescript.instructions.md
---
applyTo: "**/*.ts,**/*.tsx"
---
# TypeScript Best Practices

## Type Safety

- Enable `strict` mode in `tsconfig.json` (already configured).
- Use `import type { ... }` for type-only imports — keeps runtime bundles clean.
- Prefer `interface` for object shapes; use `type` for unions, intersections, and mapped types.
- Never use `any`. Use `unknown` when the type is genuinely unknown, then narrow it.

## Patterns

- Use discriminated unions for state management and API responses.
- Prefer `as const` for literal types and const assertions.
- Use `satisfies` operator to validate types without widening.
- Extract shared types to `src/types/` — keep them co-located if only used in one module.

## Naming Conventions

- **Interfaces/Types:** PascalCase (`UserProfile`, `ApiResponse`).
- **Variables/Functions:** camelCase (`getUserById`, `isLoading`).
- **Constants:** UPPER_SNAKE_CASE for true constants, camelCase for computed values.
- **Components:** PascalCase file names matching the export (`UserCard.tsx`).

## Enums

- Avoid `enum` — use `as const` objects or string literal union types instead.

## ./.github/skills/anforderungsdokument/SKILL.md
﻿---
name: anforderungsdokument
description: >-
  WAMOCON Entwicklungsprompts: Tiefenanalyse, Marketing/UX-Rework und
  Anforderungsdokument (9 Kapitel + Quellenverzeichnis als .docx).
  Workflow: IDEA.md ausfüllen, Skill aufrufen, Dokument prüfen, Freigabe.
---

# WAMOCON Entwicklungsprompts und Anforderungsdokument

## Übersicht

Dieser Skill stellt drei Entwicklungsprompts und eine verbindliche Dokumentstruktur
für WAMOCON-Anforderungsdokumente bereit. Das Anforderungsdokument folgt einer
festen 9-Kapitel-Struktur mit Quellenverzeichnis und wird als .docx generiert.

> **⚠️ PLATTFORMREGEL (ABSOLUT BINDEND):** Alle Anforderungsdokumente und Analysen
> gelten ausschließlich für **Web- und SaaS-Applikationen** (Browser-basiert).
> Mobile Apps (iOS, Android, React Native, Flutter) sind **kein Bestandteil** dieser
> Dokumente und dürfen unter keinen Umständen im Scope erwähnt werden.

> **⚠️ QUELLENREGEL (ABSOLUT BINDEND):** Alle verwendeten Quellen, Statistiken und
> Marktdaten müssen **nicht älter als 1 Jahr** sein (ab aktuellem Datum). Quellen,
> die älter als 12 Monate sind, sind **strikt verboten** und dürfen unter keinen
> Umständen verwendet werden. Kein Erscheinungsdatum → Quelle nicht verwenden.

**Workflow:** IDEA.md ausfüllen → Prompt 3 aufrufen → Dokument prüfen → Freigabe → Implementierung starten.

---

## Prompt 1: Tiefenanalyse und kritische Projektbewertung

Verwende diesen Prompt nach dem Onboarding einer neuen App-Idee, um eine vollumfängliche
Analyse auf Basis des Anforderungsdokuments durchzuführen.

```
Prüfe bitte das aktuelle Projekt und mache dich mit allen Daten und Inhalten vertraut.

Führe anschließend eine vollumfängliche Tiefenanalyse zum Thema der Web-/SaaS-Applikation
aus dem Anforderungsdokument durch. Erstelle dafür:
- Eine vollumfängliche Bedarfsanalyse des geplanten Themas
- Eine Nutzwertanalyse für die Funktionen
- Hinweise auf mögliche Lücken im Markt, die mit der Web-App nicht abgedeckt sind

STRIKT – QUELLENREGEL: Verwende ausschließlich Quellen und Daten, die nicht älter
als 1 Jahr sind. Quellen, die älter als 12 Monate sind, sind verboten.
Im Analysedokument muss jede Zahl mit einer aktuellen Quelle (inkl. Datum) belegt sein.

Fasse deine Ergebnisse in einem Analysedokument zusammen und gib eine Empfehlung ab,
welche Richtung die Web-/SaaS-Applikation nehmen soll, um die größtmögliche
Nutzerplattform und den größten Nutzen zu erzielen.

Erstelle am Ende Entscheidungsvorlagen zur Entscheidung der nächsten Schritte für die
Entwicklung und Ausrichtung der Applikation.

Prüfe intern deine Ergebnisse kritisch und mehrfach, sodass die Ergebnisse brauchbar sind.
```

---

## Prompt 2: Marketing und UX/UI Rework

Verwende diesen Prompt, wenn die Web-Applikation eine Überarbeitung aus Marketing-
und UX-Perspektive benötigt.

```
Bitte führe eine vollständige Analyse und Optimierung des Projektes durch.

Ziel ist eine umfassende Überarbeitung der Web-Applikation aus Marketing- und UX/UI-Perspektive:
- Analysiere die Applikation und passende Oberflächen, Farben, Typografie und Designsystem
- Optimiere den Workflow nach typischen UX-Prinzipien (geführt, unterstützt, intuitiv)
- Stelle sicher, dass die Web-App responsiv ist und auf allen gängigen Browsergrößen
  optimal dargestellt wird (Desktop, Laptop, Tablet) — wir entwickeln ausschließlich
  Web-/SaaS-Applikationen, KEINE mobilen Apps
- Implementiere passende Hilfestellungen für den User

STRIKT – QUELLENREGEL: Verwende ausschließlich Quellen und Daten, die nicht älter
als 1 Jahr sind. Quellen, die älter als 12 Monate sind, sind verboten.

Überarbeite alle Seiten vollständig und führe anschließend alle notwendigen
Fehlerbehebungen durch.
```

---

## Prompt 3: Anforderungsdokument erstellen (9 Kapitel + Quellenverzeichnis)

Verwende diesen Prompt, um ein vollständiges Anforderungsdokument zu erstellen.
Die KI liest `IDEA.md` und das `SKILL.md` automatisch aus dem Projekt — nichts einfügen, nichts ersetzen.

```
Nutze für diese Aufgabe die PERSONA eines interdisziplinären Expertenteams
(Senior Product Manager, Market Research Analyst und Tech Lead) im CEOMODE.
Führe die gesamte Analyse im /godmode und auf L99 aus.

1. Vorbereitung
Lies zunächst diese beiden Dateien vollständig, bevor du beginnst:
- .github/skills/anforderungsdokument/SKILL.md
- IDEA.md

2. Projektrahmen & Kontext
Fokus: Entwicklung eines neuen Web-/SaaS-Tools.
Plattform: Ausschließlich browserbasierte Web- und SaaS-Applikationen.
Tech-Stack: Next.js, Tailwind CSS, TypeScript, Supabase, Vercel.
Strukturiere die technische Architektur als ARCHITECT.

3. Kernaufgabe
Durchdenke die Anforderungen mit /deepthink und erstelle ein vollständiges
WAMOCON-Anforderungsdokument. Halte dich strikt an die verbindliche
9-Kapitel-Struktur aus dem SKILL.md. Fülle jedes Kapitel mit echten, belegten
Daten. Verwende keine Platzhalter.

4. Strikte Restriktionen
Agiere bei der Einhaltung dieser Regeln als SENTINEL:

Plattform-Regel: Mobile Apps sind ausgeschlossen. Die Begriffe iOS, Android,
React Native oder Flutter dürfen im Dokument nicht erwähnt werden.

Quellen-Regel (FACTCHECK & /investigate): Nutze ausschließlich Quellen, die
jünger als ein Jahr sind. Ältere Quellen sind verboten. Jede genannte Zahl muss
mit einer exakten Quellenangabe und dem Veröffentlichungsdatum belegt werden.

Tonalität: Analytisch, datengestützt, kritisch und lösungsorientiert.
Professionell, durchgehend auf Deutsch unter Verwendung echter Umlaute (Ä, Ö, Ü, ß).

5. Ausgabe
Skript: scripts/generate-anforderungsdokument.mjs
Datei: public/Anforderungsdokument_[ProjektName].docx
```

---

## DOKUMENTSTRUKTUR (verbindlich für jedes Anforderungsdokument)

> **⚠️ Gilt ausschließlich für Web-/SaaS-Applikationen. Mobile Apps sind nicht Bestandteil.**

### Deckblatt

Oben: dicke Trennlinie (WAMOCON-Blau).
Titel zentriert: "WAMOCON GMBH" + "Anforderungsdokument" + [Projektname].
Metadaten-Tabelle ohne Rahmen:

| Feld              | Wert                          |
|-------------------|-------------------------------|
| Welle             | [Wellennummer aus IDEA.md]    |
| Projekt           | [App-Name]                    |
| Unternehmen       | WAMOCON GmbH                  |
| App Version       | 1                             |
| Erstellt von      | [Name aus IDEA.md]            |
| Eingereicht an    | [Empfänger aus IDEA.md]       |
| Datum             | [TT.MM.JJJJ aktuell]         |
| Vertraulichkeit   | Intern vertraulich            |
| Status            | Zur Freigabe eingereicht      |

Unten: gestrichelte Trennlinie.

---

### Kapitel 1: Zusammenfassung

- **1.1 Die Idee** — Was macht die Web-/SaaS-App? Welches Problem löst sie? Kernnutzen in 3–5 Sätzen.
- **1.2 Warum jetzt?** — Markttiming: Warum ist das Thema genau jetzt relevant? Mit aktuellen Zahlen belegen (Quellen nicht älter als 1 Jahr).

---

### Kapitel 2: Marktanalyse

- **2.1 Zielgruppe in Zahlen** — Marktgröße, Nutzeranzahl, Wachstumsprognosen. Fokus Deutschland/DACH. Jede Zahl mit Quellenangabe (nicht älter als 1 Jahr).
- **2.2 Infrastruktur/Marktwachstum** — Was wächst? Welche Trends treiben den Markt? Prognosen bis 2030.
- **2.3 Das Kernproblem** — Faktisch belegt: Was ist das konkrete Problem, das die Web-App löst? Warum existiert es heute noch?
- **2.4 Regulatorisches Umfeld** — DSGVO, branchenspezifische Gesetze, EU-Verordnungen. Was stärkt den USP?

---

### Kapitel 3: Wettbewerb

- **3.1 Direkte Wettbewerber** — Tabelle: Anbieter | Stärken | Schwächen/Chance für uns | Preis.
  Echte Anbieter mit echten Daten. Stärken UND Schwächen ehrlich benennen.
- **3.2 Indirekte Wettbewerber / Aggregate** — Tabelle: Anbieter | Was er bietet | Was fehlt (Chance für uns).
- **Marktlücke** — Zusammenfassung: Welche Kombination bietet kein Wettbewerber? Das ist unser Einstieg.

---

### Kapitel 4: Zielgruppe

- **4.1 Primäre Zielgruppe** — Genaue Beschreibung mit Zahlen. Nutzerprofile als Fließtext (Personas mit Name, Rolle, Verhalten).
- **4.2 Sekundäre Zielgruppe** — Wer kommt später dazu? Warum erst später?
- **4.3 Nicht-Zielgruppe** — Wen adressiert die Web-App NICHT? Klar abgrenzen.

---

### Kapitel 5: Nutzen

- **5.1 Nutzen für Kunden** — Tabelle: Problem heute | Lösung durch Web-App | Konkreter Vorteil. Mit messbaren Zahlen (Quellen nicht älter als 1 Jahr).
- **5.2 Nutzen für WAMOCON GmbH** — Warum lohnt sich das Projekt? Einnahmequellen, Skalierungspotenzial, strategischer Wert.

---

### Kapitel 6: Abhängigkeiten und Machbarkeit

- **6.1 Externe Abhängigkeiten** — APIs, Dienste, Datenquellen. Tabelle: Quelle | Was sie liefert | Kosten | Abhängigkeit.
- **6.2 Abrechnungs-/Integrationsoptionen** — Falls relevant: Welche Optionen für Bezahlung/Integration gibt es? Pro Version.
- **6.3 Gesamtbewertung** — Hat V1 kritische Abhängigkeiten? Kann ein Wettbewerber den Start blockieren?

---

### Kapitel 7: Anforderungen Version 1

- **7.1 Hauptprozesse** — Gruppiert nach Themen (z.B. "Dokumenten-Upload", "Frage-Generator").
  Jede Gruppe hat eine eigene Anforderungstabelle:

  | ID   | Anforderung                          | Priorität  | Status |
  |------|--------------------------------------|------------|--------|
  | K-01 | [Kernfunktion]                       | Muss       | Neu    |

- **7.2 Basisfunktionalitäten** — Pflicht für jede Web-App:

  | ID   | Anforderung                                              | Priorität  | Status |
  |------|----------------------------------------------------------|------------|--------|
  | B-01 | Rollen- und Rechteprinzip                                | Muss       | Neu    |
  | B-02 | Anmeldung und Registrierung (E-Mail mit Bestätigung)     | Muss       | Neu    |
  | B-03 | Passwort zurücksetzen                                    | Muss       | Neu    |
  | B-04 | Admin-Bereich für Nutzerverwaltung                       | Muss       | Neu    |
  | B-05 | Profilseite                                              | Muss       | Neu    |
  | B-06 | Dashboard als Startseite                                 | Muss       | Neu    |
  | B-07 | Navigation mit Breadcrumbs                               | Muss       | Neu    |
  | B-08 | Benachrichtigungssystem (In-App und/oder E-Mail)         | Soll       | Neu    |
  | B-09 | Spracheinstellungen (Deutsch und Englisch)               | Muss       | Neu    |
  | B-10 | Dunkel/Hell-Modus                                        | Muss       | Neu    |
  | B-11 | FAQ und Hilfebereich                                     | Soll       | Neu    |
  | B-12 | AGB, Impressum, Datenschutzerklärung                     | Muss       | Neu    |
  | B-13 | Cookie-Banner nach DSGVO                                 | Muss       | Neu    |
  | B-14 | DSGVO-Funktionen (Daten exportieren, Konto löschen)      | Muss       | Neu    |
  | B-15 | Geschäftsmodell (Free und Premium)                       | Muss       | Neu    |
  | B-16 | Upgrade von Free auf Premium in der App                  | Muss       | Neu    |

- **7.3 Scope** — Tabelle: In Scope V1 | Out of Scope (V2+). Klare Abgrenzung.

---

### Kapitel 8: Chancen und Risiken

- **8.1 Chancen** — Tabelle: Chance | Begründung. Mit Zahlen und Quellen (nicht älter als 1 Jahr).
- **8.2 Risiken** — Tabelle: Risiko | Warum es eintreten kann | Gegenmaßnahme.

---

### Kapitel 9: Umsetzungsplan Version 1

- **9.1 Entwicklungsansatz** — Tech-Stack, Werkzeuge (GitHub Copilot), Teamstruktur.
- **9.2 Umsetzungsplan** — Tag-für-Tag-Tabelle über 5–7 Werktage:

  | Tag       | Fokus                       | Inhalt                          |
  |-----------|-----------------------------|---------------------------------|
  | Tag 1–3   | Hauptprozesse               | [Details]                       |
  | Tag 3–4   | Testing und Bugfixing       | [Details]                       |
  | Tag 4–5   | Basisfunktionalitäten       | [Details]                       |
  | Tag 5–6   | Puffer                      | [Details]                       |

- **Hinweis** — Realistisch: V1 ist ein lauffähiger Prototyp, kein Endprodukt.

---

### Quellenverzeichnis

Tabelle: Nr. | Quelle/URL | Inhalt | Veröffentlichungsdatum.
Nur reale, öffentlich verfügbare Quellen.

**STRIKT:** Ausschließlich Quellen, die nicht älter als 1 Jahr sind.
Jede Zahl im Dokument muss mindestens eine Quelle haben.
Das Veröffentlichungsdatum muss für jede Quelle angegeben sein.

---

## FORMATREGELN

- **Sprache:** Deutsch mit echten Umlauten (Ä, Ö, Ü, ß). In Code-Variablennamen ist ae/oe/ue akzeptabel.
- **Schrift:** Arial Narrow, 11pt Fließtext.
- **Tabellenkopf:** WAMOCON-Blau (1E3A5F) mit weißem Text, fett.
- **Tabellenzeilen:** alternierend weiß / hellgrau (F5F5F5).
- **Breiten:** WidthType.DXA (keine Prozent).
- **Shading:** ShadingType.CLEAR (kein SOLID).
- **Kein \n in TextRun** — separate Paragraphen verwenden.
- **Seitenkopf:** "WAMOCON GmbH, Mergenthalerallee 79-81, 65760 Eschborn" (8pt, grau).
- **Seitenumbruch** zwischen den Hauptkapiteln.

---

## Workflow

```
[1] IDEA.md im Projekt-Root ausfüllen
        |
        v
[2] Prompt 3 aufrufen → Anforderungsdokument als .docx generieren
        |
        v
[3] Dokument prüfen und zur Freigabe einreichen (Geschäftsführung)
        |
        v
[4] Nach Freigabe: Prompt 1 für Tiefenanalyse aufrufen
        |
        v
[5] Implementierung mit @planner → @developer
        |
        v
[6] Nach Launch: Prompt 2 für UX/UI Rework
```

---

## Voraussetzungen

- Node.js >= 18
- npm install docx (einmalig)
- Ausgabe: public/Anforderungsdokument_[ProjektName].docx
- package.json: "gen:anforderungsdokument": "node scripts/generate-anforderungsdokument.mjs"
## ./.github/skills/memory-merger/SKILL.md
---
name: memory-merger
description: 'Merges mature lessons from a domain memory file into its instruction file. Syntax: `/memory-merger >domain [scope]` where scope is `global` (default), `user`, `workspace`, or `ws`.'
---

# Memory Merger

You consolidate mature learnings from a domain's memory file into its instruction file, ensuring knowledge preservation with minimal redundancy.

**Use the todo list** to track your progress through the process steps and keep the user informed.

## Scopes

Memory instructions can be stored in two scopes:

- **Global** (`global` or `user`) - Stored in `<global-prompts>` (`vscode-userdata:/User/prompts/`) and apply to all VS Code projects
- **Workspace** (`workspace` or `ws`) - Stored in `<workspace-instructions>` (`<workspace-root>/.github/instructions/`) and apply only to the current project

Default scope is **global**.

Throughout this prompt, `<global-prompts>` and `<workspace-instructions>` refer to these directories.

## Syntax

```
/memory-merger >domain-name [scope]
```

- `>domain-name` - Required. The domain to merge (e.g., `>clojure`, `>git-workflow`, `>prompt-engineering`)
- `[scope]` - Optional. One of: `global`, `user` (both mean global), `workspace`, or `ws`. Defaults to `global`

**Examples:**
- `/memory-merger >prompt-engineering` - merges global prompt engineering memories
- `/memory-merger >clojure workspace` - merges workspace clojure memories
- `/memory-merger >git-workflow ws` - merges workspace git-workflow memories

## Process

### 1. Parse Input and Read Files

- **Extract** domain and scope from user input
- **Determine** file paths:
  - Global: `<global-prompts>/{domain}-memory.instructions.md` → `<global-prompts>/{domain}.instructions.md`
  - Workspace: `<workspace-instructions>/{domain}-memory.instructions.md` → `<workspace-instructions>/{domain}.instructions.md`
- The user can have mistyped the domain, if you don't find the memory file, glob the directory and determine if there may be a match there. Ask the user for input if in doubt.
- **Read** both files (memory file must exist; instruction file may not)

### 2. Analyze and Propose

Review all memory sections and present them for merger consideration:

```
## Proposed Memories for Merger

### Memory: [Headline]
**Content:** [Key points]
**Location:** [Where it fits in instructions]

[More memories]...
```

Say: "Please review these memories. Approve all with 'go' or specify which to skip."

**STOP and wait for user input.**

### 3. Define Quality Bar

Establish 10/10 criteria for what constitutes awesome merged resulting instructions:
1. **Zero knowledge loss** - Every detail, example, and nuance preserved
2. **Minimal redundancy** - Overlapping guidance consolidated
3. **Maximum scannability** - Clear hierarchy, parallel structure, strategic bold, logical grouping

### 4. Merge and Iterate

Develop the final merged instructions **without updating files yet**:

1. Draft the merged instructions incorporating approved memories
2. Evaluate against quality bar
3. Refine structure, wording, organization
4. Repeat until the merged instructions meet 10/10 criteria

### 5. Update Files

Once the final merged instructions meet 10/10 criteria:

- **Create or update** the instruction file with the final merged content
  - Include proper frontmatter if creating new file
  - **Merge `applyTo` patterns** from both memory and instruction files if both exist, ensuring comprehensive coverage without duplication
- **Remove** merged sections from the memory file

## Example

```
User: "/memory-merger >clojure"

Agent:
1. Reads clojure-memory.instructions.md and clojure.instructions.md
2. Proposes 3 memories for merger
3. [STOPS]

User: "go"

Agent:
4. Defines quality bar for 10/10
5. Merges new instructions candidate, iterates to 10/10
6. Updates clojure.instructions.md
7. Cleans clojure-memory.instructions.md
```

## ./.github/skills/next-browser/SKILL.md
---
name: next-browser
description: >-
  CLI that gives agents what humans get from React DevTools and the Next.js
  dev overlay — component trees, props, hooks, PPR shells, errors, network —
  as shell commands that return structured text.
---

# next-browser

If `next-browser` is not already on PATH, install `@vercel/next-browser` globally, then install the Chromium browser:

```bash
npm install -g @vercel/next-browser
playwright install chromium
```

Requires Node >= 20. If already installed, check the version is current:

```bash
next-browser --version
npm view @vercel/next-browser version
# if outdated:
npm install -g @vercel/next-browser@latest
```

---

## Next.js docs awareness

If the project's Next.js version is **v16.2.0-canary.37 or later**, bundled docs live at `node_modules/next/dist/docs/`. Before doing PPR work, Cache Components work, or any non-trivial Next.js task, read the relevant doc there — your training data may be outdated. The bundled docs are the source of truth.

---

## Working with the user

### Onboarding

- If the user already gave a URL, cookies, and task — skip questions, `open` and go.
- Otherwise ask only what's missing: dev server URL (running?), session cookies if behind login.
- For cookies, give the user two options: (1) DevTools → Application → Cookies, export as `[{"name":"session","value":"..."}]`, or (2) "Copy as cURL" from DevTools → Network on any authenticated request — extract the cookies from the header yourself.
- Never say "ready, what would you like to do?". Never auto-discover (port scans, `project`, config reads) before being asked.

### Show, don't tell

- `screenshot` after every navigation, code change, or visual finding. Always caption it.
- Don't narrate what a screenshot shows. State your conclusion or next action.

### Escalate, don't decide

- Suspense boundary placement and fallback UI — design with the user.
- Caching decisions (staleness, visibility) — the user's call, not yours.
- "Make this page faster" without context — ask: cold URL hit or client navigation? Don't guess, don't do both.

---

## Headless mode

By default the browser opens headed (visible window). For CI or environments with no display, set `NEXT_BROWSER_HEADLESS=1` to run headless.

---

## Commands

### Browser lifecycle

| Command | Description |
|---|---|
| `open <url> [--cookies-json <file>]` | Launch browser and navigate (with optional cookies) |
| `close` | Close browser and kill daemon |

```bash
$ next-browser open http://localhost:3000
$ next-browser open http://localhost:3000 --cookies-json cookies.json
# Cookie file format: [{"name":"authorization","value":"Bearer ..."}]
```

---

### Navigation

| Command | Description |
|---|---|
| `goto <url>` | Full-page navigation (new document load) |
| `push [path]` | Client-side navigation (interactive picker if no path) |
| `back` | Go back in history |
| `reload` | Reload current page |
| `restart-server` | Restart the Next.js dev server (clears caches — last resort only) |
| `ssr lock` | Block external scripts on all navigations (SSR-only mode) |
| `ssr unlock` | Re-enable external scripts |

---

### Inspection

| Command | Description |
|---|---|
| `tree` | Full React component tree (hierarchy, IDs, keys) |
| `tree <id>` | Inspect one component (props, hooks, state, source location) |
| `snapshot` | Accessibility tree with `[ref=eN]` markers on interactive elements |
| `errors` | Build and runtime errors for the current page |
| `logs` | Recent dev server log output |
| `browser-logs` | Browser-side console output (log, warn, error, info) |
| `network [idx]` | List network requests, or inspect one (headers, body) |

```bash
$ next-browser snapshot
- navigation "Main"
  - link "Home" [ref=e0]
  - link "Dashboard" [ref=e1]
- main
  - heading "Settings"
  - tablist
    - tab "General" [ref=e2] (selected)
    - tab "Security" [ref=e3]

$ next-browser tree
# Columns: depth id parent name
0 38167 - Root
1 38168 38167 HeadManagerContext.Provider
...
224 46375 46374 DeploymentsProvider

$ next-browser tree 46375
path: Root > ... > DeploymentsProvider
DeploymentsProvider #46375
props:
  children: [<Lazy />, ...]
hooks:
  Router: undefined (2 sub)
source: app/.../context.tsx:180:10
```

---

### Interaction

| Command | Description |
|---|---|
| `click <ref\|text\|selector>` | Click via real pointer events (works with Radix, Headless UI) |
| `fill <ref\|selector> <value>` | Fill a text input or textarea |
| `eval [ref] <script>` | Run JS in page context |
| `viewport [WxH]` | Show or set viewport size |

```bash
$ next-browser click e3          # ref from snapshot
$ next-browser click "Security"  # plain text
$ next-browser fill e4 "myuser"
$ next-browser viewport 375x812  # mobile breakpoint
$ next-browser eval 'document.title'
```

---

### Performance & PPR

| Command | Description |
|---|---|
| `perf [url]` | Core Web Vitals + React hydration timing in one pass |
| `renders start` | Begin recording React re-renders |
| `renders stop [--json]` | Stop and print per-component render profile |
| `ppr lock` | Freeze dynamic content to inspect the static shell |
| `ppr unlock` | Resume dynamic content and print shell analysis |

```bash
$ next-browser perf http://localhost:3000/dashboard
# Core Web Vitals
  TTFB    42ms
  LCP     1205.3ms
  CLS     0.03
# React Hydration — 65.5ms

$ next-browser renders start
$ next-browser renders stop
# 426 renders (38 mounts + 388 re-renders) across 38 components
# FPS: avg 120, min 106
```

---

### Screenshots

| Command | Description |
|---|---|
| `screenshot [caption] [--full-page]` | Viewport (or full page) PNG to temp file |
| `preview [caption]` | Screenshot + open in viewer window |

---

### Next.js MCP

| Command | Description |
|---|---|
| `page` | Route segments for the current URL |
| `project` | Project root and dev server URL |
| `routes` | All app router routes |
| `action <id>` | Inspect a server action by ID |

---

## Scenarios

### Debug a visual or interaction issue

1. `open http://localhost:3000`
2. `snapshot` — discover interactive elements
3. `click eN` / `fill eN value` — interact
4. `errors` — check for runtime errors
5. `screenshot "before fix"` — document state
6. Make the code change, HMR picks it up
7. `screenshot "after fix"` — verify

### Profile performance

```bash
$ next-browser perf http://localhost:3000/dashboard
# → Core Web Vitals + hydration timing

$ next-browser renders start
# reproduce slow interaction
$ next-browser renders stop
# → per-component render counts, self time, change reasons
```

### Debug PPR shell

```bash
$ next-browser ppr lock
$ next-browser goto http://localhost:3000/page
$ next-browser screenshot "PPR shell — locked"
$ next-browser ppr unlock
# → Shell analysis: which Suspense boundaries are holes and why
```

### Test responsive layout

```bash
$ next-browser viewport 375x812   # mobile
$ next-browser screenshot "mobile"
$ next-browser viewport 1440x900  # desktop
$ next-browser screenshot "desktop"
```

### Debug component re-renders

1. `renders start`
2. `goto` the page (captures hydration)
3. Reproduce the interaction
4. `renders stop` — read Mounts vs Re-renders, Self time, change reasons
5. `tree <id>` the expensive component — check source, props, hooks
6. Fix, HMR picks it up, re-run `renders start/stop` to verify

## ./AGENTS.md
﻿
---

# GitHub Copilot Customisation

<table>
<tr>
<th width="50%">DE Deutsch</th>
<th width="50%">EN English</th>
</tr>
<tr>
<td>Dieses Projekt nutzt GitHub Copilot Agents und Instructions, um eine strukturierte und produktive KI-gestützte Entwicklung zu ermöglichen.</td>
<td>This project uses GitHub Copilot Agents and Instructions to enable a structured and productive AI-assisted development workflow.</td>
</tr>
</table>

---

## Übersicht / Overview

| Typ / Type | Pfad / Path | Beschreibung / Description |
|---|---|---|
| **Global Instructions** | `.github/copilot-instructions.md` | Projektweite Basisregeln für alle Copilot-Interaktionen. / Project-wide baseline rules for all Copilot interactions. |
| **Instructions** | `.github/instructions/*.instructions.md` | Dateimuster-spezifische Coding-Richtlinien. / File-pattern-scoped coding guidelines. |
| **Agents** | `.github/agents/*.agent.md` | Spezialisierte KI-Personas für verschiedene Phasen. / Specialised AI personas for different development phases. |

---

## `copilot-instructions.md` — Globale Basisregeln / Global Baseline Rules

**Pfad / Path:** `.github/copilot-instructions.md`

<table>
<tr>
<th width="50%">DE Was ist das?</th>
<th width="50%">EN What is it?</th>
</tr>
<tr>
<td>Diese Datei wird bei <strong>jeder</strong> Copilot-Interaktion automatisch geladen. Sie definiert den Tech-Stack, kritische Regeln (async APIs, Server Components, Supabase), und Code-Stil-Konventionen für das gesamte Projekt.</td>
<td>This file is automatically loaded on <strong>every</strong> Copilot interaction. It defines the tech stack, critical rules (async APIs, Server Components, Supabase), and code style conventions for the whole project.</td>
</tr>
</table>

<table>
<tr>
<th width="50%">DE Wann bearbeiten?</th>
<th width="50%">EN When to edit?</th>
</tr>
<tr>
<td>
- Tech-Stack ändert sich (z. B. neue Bibliothek wird Standardmuster)<br>
- Neue projektweite Regeln sollen für alle Copilot-Interaktionen gelten<br>
- Team-Konventionen ändern sich<br>
<strong>⚠️ Kurz halten</strong> — diese Datei wird immer in den Kontext geladen.
</td>
<td>
- Tech stack changes (e.g. a new library becomes a standard pattern)<br>
- New project-wide rules need to apply to all Copilot interactions<br>
- Team conventions change<br>
<strong>⚠️ Keep it short</strong> — this file is always loaded into context.
</td>
</tr>
</table>

---

## Instructions — Datei-spezifische Richtlinien / File-Scoped Guidelines

<table>
<tr>
<th width="50%">DE Was sind Instructions?</th>
<th width="50%">EN What are Instructions?</th>
</tr>
<tr>
<td>Instructions sind Richtlinien, die automatisch geladen werden, wenn Copilot an Dateien arbeitet, die dem <code>applyTo</code>-Glob-Muster entsprechen. Sie ergänzen die globalen Regeln mit datei-spezifischen Details.</td>
<td>Instructions are guidelines that are automatically loaded when Copilot works on files matching the <code>applyTo</code> glob pattern. They extend the global rules with file-type-specific details.</td>
</tr>
</table>

### Vorhandene Instructions / Available Instructions

| Datei / File | `applyTo` | Zweck / Purpose |
|---|---|---|
| `nextjs.instructions.md` | `**/*.tsx, **/*.ts, **/*.jsx, **/*.js` | Next.js 16 App Router Patterns, async APIs, Server/Client Components |
| `tailwind.instructions.md` | `**/*.tsx, **/*.jsx, **/*.css` | Tailwind CSS v4 Utility-First Patterns, Responsive Design |
| `typescript.instructions.md` | `**/*.ts, **/*.tsx` | TypeScript Strict Mode, Naming Conventions, Type Safety |
| `supabase.instructions.md` | `**/supabase/**, **/*supabase*` | Supabase Client Setup, RLS, Migrations, Schema Awareness |

### Eigene Instructions erstellen / Creating Custom Instructions

<table>
<tr>
<th width="50%">DE Anleitung</th>
<th width="50%">EN Guide</th>
</tr>
<tr>
<td>Erstelle eine <code>.instructions.md</code>-Datei in <code>.github/instructions/</code> mit YAML-Frontmatter. Das <code>applyTo</code>-Feld akzeptiert Glob-Muster und bestimmt, für welche Dateien die Regeln gelten.</td>
<td>Create a <code>.instructions.md</code> file in <code>.github/instructions/</code> with YAML frontmatter. The <code>applyTo</code> field accepts glob patterns and determines which files the rules apply to.</td>
</tr>
</table>

```yaml
---
applyTo: "**/*.tsx"
---
# Your instructions here
```

---

## Agents — KI-Personas / AI Personas

<table>
<tr>
<th width="50%">DE Was sind Agents?</th>
<th width="50%">EN What are Agents?</th>
</tr>
<tr>
<td>Agents sind spezialisierte KI-Personas. Du rufst sie in VS Code über das Chat-Panel mit <code>@agent-name</code> auf. Jeder Agent hat eine klar definierte Rolle, einen Workflow und Regeln.</td>
<td>Agents are specialised AI personas. You invoke them in VS Code via the Chat panel using <code>@agent-name</code>. Each agent has a clearly defined role, workflow, and rules.</td>
</tr>
</table>

---

### `@planner` — Planer

<table>
<tr>
<th width="50%">DE</th>
<th width="50%">EN</th>
</tr>
<tr>
<td><strong>Zweck:</strong> Technische Planung und Anforderungsanalyse vor dem Coding.</td>
<td><strong>Purpose:</strong> Technical planning and requirements analysis before coding.</td>
</tr>
<tr>
<td><strong>Wann verwenden:</strong><br>— Vor dem Start eines neuen Features<br>— Wenn die Anforderungen unklar sind<br>— Vor Refactoring oder Migrations-Aufgaben</td>
<td><strong>When to use:</strong><br>— Before starting a new feature<br>— When requirements are unclear<br>— Before refactoring or migration tasks</td>
</tr>
<tr>
<td><strong>Was er tut:</strong><br>✔ Codebase erkunden und Kontext sammeln<br>✔ Betroffene Dateien und Module identifizieren<br>✔ Nummerierten Implementierungsplan erstellen<br>✘ <strong>Schreibt keinen Code</strong></td>
<td><strong>What it does:</strong><br>✔ Explore codebase and gather context<br>✔ Identify affected files and modules<br>✔ Create a numbered implementation plan<br>✘ <strong>Does not write code</strong></td>
</tr>
<tr>
<td><strong>Verwendung:</strong> <code>@planner Füge eine Authentifizierungsseite hinzu</code></td>
<td><strong>Usage:</strong> <code>@planner Add an authentication page</code></td>
</tr>
</table>

---

### `@developer` — Entwickler

<table>
<tr>
<th width="50%">DE</th>
<th width="50%">EN</th>
</tr>
<tr>
<td><strong>Zweck:</strong> Strukturierte Feature-Implementierung mit Qualitätsprüfungen.</td>
<td><strong>Purpose:</strong> Structured feature implementation with quality checks.</td>
</tr>
<tr>
<td><strong>Wann verwenden:</strong><br>— Nach der Planung mit <code>@planner</code><br>— Zur Implementierung von Features, Seiten, API-Routen<br>— Für Datenbankänderungen und Migrationen</td>
<td><strong>When to use:</strong><br>— After planning with <code>@planner</code><br>— To implement features, pages, API routes<br>— For database changes and migrations</td>
</tr>
<tr>
<td><strong>Vierphasiger Prozess:</strong><br>1. <strong>Vorbereitung</strong> — Plan lesen, Code verstehen<br>2. <strong>Implementierung</strong> — Schrittweise, Fehler sofort beheben<br>3. <strong>Verifikation (PFLICHT)</strong> — <code>typecheck</code> → <code>lint</code> → <code>build</code> → lokal testen<br>4. <strong>Dokumentation</strong> — Handbook aktualisieren</td>
<td><strong>Four-phase process:</strong><br>1. <strong>Preparation</strong> — Read plan, understand code<br>2. <strong>Implementation</strong> — Step by step, fix errors immediately<br>3. <strong>Verification (MANDATORY)</strong> — <code>typecheck</code> → <code>lint</code> → <code>build</code> → test locally<br>4. <strong>Documentation</strong> — Update handbook</td>
</tr>
<tr>
<td><strong>Verwendung:</strong> <code>@developer Implementiere diesen Plan: [Plan einfügen]</code></td>
<td><strong>Usage:</strong> <code>@developer Implement this plan: [paste plan]</code></td>
</tr>
</table>

---

### `@reviewer` — Code-Reviewer

<table>
<tr>
<th width="50%">DE</th>
<th width="50%">EN</th>
</tr>
<tr>
<td><strong>Zweck:</strong> Code-Review und Qualitätssicherung vor dem PR.</td>
<td><strong>Purpose:</strong> Code review and quality assurance before a PR.</td>
</tr>
<tr>
<td><strong>Wann verwenden:</strong><br>— Bevor ein PR erstellt wird<br>— Nach einer Implementierung zur Qualitätsprüfung<br>— Zur Sicherheits- und Performance-Analyse</td>
<td><strong>When to use:</strong><br>— Before creating a PR<br>— After implementation for quality check<br>— For security and performance audits</td>
</tr>
<tr>
<td><strong>Was er tut:</strong><br>✔ Strukturierte Checkliste (Qualität, Next.js 16, Supabase-Sicherheit, Styling)<br>✔ Alle Checks ausführen (typecheck, lint, build)<br>✔ Review-Bericht mit Status (✅ / ⚠️ / ❌)</td>
<td><strong>What it does:</strong><br>✔ Structured checklist (quality, Next.js 16, Supabase security, styling)<br>✔ Run all checks (typecheck, lint, build)<br>✔ Review report with status (✅ / ⚠️ / ❌)</td>
</tr>
<tr>
<td><strong>Verwendung:</strong> <code>@reviewer Überprüfe die Änderungen in src/app/dashboard/</code></td>
<td><strong>Usage:</strong> <code>@reviewer Review the changes in src/app/dashboard/</code></td>
</tr>
</table>

---

### `@anforderungsdokument` — Anforderungsdokument

<table>
<tr>
<th width="50%">DE</th>
<th width="50%">EN</th>
</tr>
<tr>
<td><strong>Zweck:</strong> Vollständiges WAMOCON-Anforderungsdokument (9 Kapitel + .docx) für Web-/SaaS-Applikationen erstellen.</td>
<td><strong>Purpose:</strong> Create a complete WAMOCON requirements document (9 chapters + .docx) for web/SaaS applications.</td>
</tr>
<tr>
<td><strong>Wann verwenden:</strong><br>— Vor dem Start eines neuen Projekts<br>— Wenn eine App-Idee dokumentiert werden soll<br>— Bevor die Implementierung beginnt (Freigabe erforderlich)</td>
<td><strong>When to use:</strong><br>— Before starting a new project<br>— When an app idea needs to be documented<br>— Before implementation starts (approval required)</td>
</tr>
<tr>
<td><strong>Was er tut:</strong><br>✔ Marktanalyse, Wettbewerb, Zielgruppe recherchieren<br>✔ 9-Kapitel-Dokument mit echten Daten befüllen<br>✔ Dokument als .docx generieren<br>✘ <strong>Nur Web/SaaS — keine mobilen Apps</strong><br>✘ <strong>Nur Quellen nicht älter als 1 Jahr</strong></td>
<td><strong>What it does:</strong><br>✔ Research market analysis, competition, target audience<br>✔ Fill 9-chapter document with real data<br>✔ Generate document as .docx<br>✘ <strong>Web/SaaS only — no mobile apps</strong><br>✘ <strong>Sources not older than 1 year only</strong></td>
</tr>
<tr>
<td><strong>Verwendung:</strong> <code>@anforderungsdokument Erstelle das Anforderungsdokument für [Projektname]</code></td>
<td><strong>Usage:</strong> <code>@anforderungsdokument Create the requirements document for [project name]</code></td>
</tr>
</table>

#### Schritt-für-Schritt-Anleitung / Step-by-Step Guide

**1.** Fülle `IDEA.md` im Projekt-Root aus.

**2.** Kopiere den Prompt unten und sende ihn im Chat. Die KI liest `IDEA.md` und `SKILL.md` automatisch — nichts einfügen, nichts ersetzen:

```
Nutze für diese Aufgabe die PERSONA eines interdisziplinären Expertenteams
(Senior Product Manager, Market Research Analyst und Tech Lead) im CEOMODE.
Führe die gesamte Analyse im /godmode und auf L99 aus.

1. Vorbereitung
Lies zunächst diese beiden Dateien vollständig, bevor du beginnst:
- .github/skills/anforderungsdokument/SKILL.md
- IDEA.md

2. Projektrahmen & Kontext
Fokus: Entwicklung eines neuen Web-/SaaS-Tools.
Plattform: Ausschließlich browserbasierte Web- und SaaS-Applikationen.
Tech-Stack: Next.js, Tailwind CSS, TypeScript, Supabase, Vercel.
Strukturiere die technische Architektur als ARCHITECT.

3. Kernaufgabe
Durchdenke die Anforderungen mit /deepthink und erstelle ein vollständiges
WAMOCON-Anforderungsdokument. Halte dich strikt an die verbindliche
9-Kapitel-Struktur aus dem SKILL.md. Fülle jedes Kapitel mit echten, belegten
Daten. Verwende keine Platzhalter.

4. Strikte Restriktionen
Agiere bei der Einhaltung dieser Regeln als SENTINEL:

Plattform-Regel: Mobile Apps sind ausgeschlossen. Die Begriffe iOS, Android,
React Native oder Flutter dürfen im Dokument nicht erwähnt werden.

Quellen-Regel (FACTCHECK & /investigate): Nutze ausschließlich Quellen, die
jünger als ein Jahr sind. Ältere Quellen sind verboten. Jede genannte Zahl muss
mit einer exakten Quellenangabe und dem Veröffentlichungsdatum belegt werden.

Tonalität: Analytisch, datengestützt, kritisch und lösungsorientiert.
Professionell, durchgehend auf Deutsch unter Verwendung echter Umlaute (Ä, Ö, Ü, ß).

5. Ausgabe
Skript: scripts/generate-anforderungsdokument.mjs
Datei: public/Anforderungsdokument_[ProjektName].docx
```

**3.** Dokument prüfen und zur Freigabe bei der Geschäftsführung einreichen.

**4.** Nach Freigabe: Implementierung mit `@planner` starten.

---

## Tools

| Tool | Pfad / Path | Zweck / Purpose |
|---|---|---|
| **next-browser** | `.github/skills/next-browser/SKILL.md` | CLI that exposes React DevTools and the Next.js dev overlay as shell commands — component trees, props, errors, performance, screenshots — structured output for AI agents. |
| **anforderungsdokument** | `.github/skills/anforderungsdokument/SKILL.md` | Drei Entwicklungsprompts: Tiefenanalyse, Marketing/UX-Rework und Anforderungsdokument (9 Kapitel + Quellenverzeichnis als .docx). Nur Web/SaaS — keine mobilen Apps. Nur Quellen nicht älter als 1 Jahr. IDEA.md ausfüllen, Prompt 3 aufrufen, .docx generieren, zur Freigabe einreichen. |

### `next-browser` — AI-Driven Browser for Next.js

<table>
<tr>
<th width="50%">DE Was ist das?</th>
<th width="50%">EN What is it?</th>
</tr>
<tr>
<td><code>@vercel/next-browser</code> ist ein CLI-Tool, das React DevTools und das Next.js Dev-Overlay als Shell-Befehle bereitstellt. Agents können den Browser steuern, Komponenten inspizieren, Fehler lesen und Performance prüfen — ohne manuell durch DevTools zu klicken.</td>
<td><code>@vercel/next-browser</code> is a CLI tool that exposes React DevTools and the Next.js dev overlay as shell commands. Agents can drive the browser, inspect components, read errors, and check performance — without manually clicking through DevTools.</td>
</tr>
<tr>
<td><strong>Wann verwenden:</strong><br>— Nach der Implementierung zur visuellen Verifikation<br>— Debugging von Runtime-Fehlern oder Re-Render-Problemen<br>— Performance-Analyse (Core Web Vitals, Hydration)<br>— PPR-Shell-Debugging</td>
<td><strong>When to use:</strong><br>— After implementation for visual verification<br>— Debugging runtime errors or re-render issues<br>— Performance analysis (Core Web Vitals, hydration timing)<br>— PPR shell debugging</td>
</tr>
<tr>
<td><strong>Installation:</strong><br><code>npm install -g @vercel/next-browser</code><br><code>playwright install chromium</code><br>Benötigt Node >= 20</td>
<td><strong>Install:</strong><br><code>npm install -g @vercel/next-browser</code><br><code>playwright install chromium</code><br>Requires Node >= 20</td>
</tr>
<tr>
<td><strong>Wichtigste Befehle:</strong><br><code>next-browser open &lt;url&gt;</code> — Browser starten<br><code>next-browser snapshot</code> — Accessibility-Tree + klickbare Refs<br><code>next-browser errors</code> — Build- und Runtime-Fehler<br><code>next-browser perf</code> — Core Web Vitals + Hydration<br><code>next-browser screenshot</code> — Viewport als PNG<br><code>next-browser tree</code> — React-Komponentenbaum</td>
<td><strong>Key commands:</strong><br><code>next-browser open &lt;url&gt;</code> — launch browser<br><code>next-browser snapshot</code> — accessibility tree + clickable refs<br><code>next-browser errors</code> — build and runtime errors<br><code>next-browser perf</code> — Core Web Vitals + hydration timing<br><code>next-browser screenshot</code> — viewport as PNG<br><code>next-browser tree</code> — React component tree</td>
</tr>
<tr>
<td><strong>Vollständige Dokumentation:</strong> <code>.github/skills/next-browser/SKILL.md</code></td>
<td><strong>Full documentation:</strong> <code>.github/skills/next-browser/SKILL.md</code></td>
</tr>
</table>

---

### `anforderungsdokument` — WAMOCON Entwicklungsprompts

<table>
<tr>
<th width="50%">DE Was ist das?</th>
<th width="50%">EN What is it?</th>
</tr>
<tr>
<td>Der Skill stellt <strong>drei strukturierte Entwicklungsprompts</strong> bereit: (1) Tiefenanalyse und kritische Projektbewertung, (2) Marketing und UX/UI Rework, (3) Anforderungsdokument mit verbindlicher 9-Kapitel-Struktur (Zusammenfassung, Marktanalyse, Wettbewerb, Zielgruppe, Nutzen, Abhängigkeiten, Anforderungen V1, Chancen/Risiken, Umsetzungsplan + Quellenverzeichnis). <strong>Ausschließlich Web/SaaS — keine mobilen Apps. Nur Quellen nicht älter als 1 Jahr.</strong> IDEA.md ausfüllen, Prompt aus <code>@anforderungsdokument</code> kopieren, .docx generieren, zur Freigabe einreichen.</td>
<td>The skill provides <strong>three structured development prompts</strong>: (1) deep analysis and critical assessment, (2) marketing and UX/UI rework, (3) requirements document with a mandatory 9-chapter structure (summary, market analysis, competition, target audience, benefits, dependencies, requirements V1, opportunities/risks, implementation plan + references). <strong>Web/SaaS only — no mobile apps. Sources not older than 1 year only.</strong> Fill in IDEA.md, copy prompt from <code>@anforderungsdokument</code>, generate .docx, submit for approval.</td>
</tr>
</table>

---

## Empfohlener Workflow / Recommended Workflow

<table>
<tr>
<th width="50%">DE Schritt</th>
<th width="50%">EN Step</th>
</tr>
<tr>
<td><strong>Phase 0 — Anforderungen (neues Projekt):</strong><br>
1. <code>IDEA.md</code> im Projekt-Root ausfüllen<br>
2. <strong><code>@anforderungsdokument</code></strong> aufrufen: Prompt kopieren und senden<br>
3. Dokument prüfen und zur Freigabe einreichen<br>
4. Nach Freigabe: Implementierung starten</td>
<td><strong>Phase 0 — Requirements (new project):</strong><br>
1. Fill in <code>IDEA.md</code> in the project root<br>
2. Call <strong><code>@anforderungsdokument</code></strong>: copy prompt and send<br>
3. Review document and submit for approval<br>
4. After approval: start implementation</td>
</tr>
<tr>
<td><strong>Phase 1 — Planung:</strong><br>
<strong><code>@planner</code></strong> — Aufgabe analysieren und Implementierungsplan erstellen</td>
<td><strong>Phase 1 — Planning:</strong><br>
<strong><code>@planner</code></strong> — Analyse the task and create an implementation plan</td>
</tr>
<tr>
<td><strong>Phase 2 — Implementierung:</strong><br>
<strong><code>@developer</code></strong> — Plan entgegennehmen und schrittweise implementieren</td>
<td><strong>Phase 2 — Implementation:</strong><br>
<strong><code>@developer</code></strong> — Receive plan and implement step by step</td>
</tr>
<tr>
<td><strong>Phase 3 — Qualitätsprüfung:</strong><br>
<strong><code>@reviewer</code></strong> — Code prüfen, bevor ein PR erstellt wird</td>
<td><strong>Phase 3 — Quality review:</strong><br>
<strong><code>@reviewer</code></strong> — Review code before creating a PR</td>
</tr>
</table>

---

## Eigene Agents erstellen / Creating Custom Agents

<table>
<tr>
<th width="50%">DE Anleitung</th>
<th width="50%">EN Guide</th>
</tr>
<tr>
<td>Erstelle eine <code>.agent.md</code>-Datei in <code>.github/agents/</code> mit YAML-Frontmatter. Definiere Rolle, Workflow und Regeln.</td>
<td>Create a <code>.agent.md</code> file in <code>.github/agents/</code> with YAML frontmatter. Define role, workflow, and rules.</td>
</tr>
</table>

```yaml
---
name: MyAgent
description: >
  Description of what this agent does.
---
# Agent: MyAgent

## Role
...

## Workflow
...
```

---

## Wenn ein Agent schlecht antwortet / When an Agent Responds Poorly

<table>
<tr>
<th width="50%">DE Problem & Lösung</th>
<th width="50%">EN Problem & Solution</th>
</tr>
<tr>
<td><strong>Agent ignoriert Regeln aus der Instructions-Datei</strong><br>→ Prüfe das <code>applyTo</code>-Glob-Muster — stimmt es mit der Datei überein, die du bearbeitest? Teste mit: <code>**/*.ts</code> statt <code>src/**/*.ts</code></td>
<td><strong>Agent ignores rules from an Instructions file</strong><br>→ Check the <code>applyTo</code> glob pattern — does it match the file you are editing? Try broader patterns: <code>**/*.ts</code> instead of <code>src/**/*.ts</code></td>
</tr>
<tr>
<td><strong>Agent befolgt den Workflow nicht (z. B. überspringt typecheck)</strong><br>→ Öffne die <code>.agent.md</code>-Datei und mache die Anweisung strikter. Ersetze "sollte" durch "muss". Füge am Ende eine Zusammenfassung hinzu: <em>"Bevor du antwortest, liste alle abgeschlossenen Schritte auf."</em></td>
<td><strong>Agent does not follow the workflow (e.g. skips typecheck)</strong><br>→ Open the <code>.agent.md</code> file and make the instruction stricter. Replace "should" with "must". Add a reminder at the end: <em>"Before responding, list all completed steps."</em></td>
</tr>
<tr>
<td><strong>Agent schreibt schlechten Next.js-Code (z. B. falsche API-Nutzung)</strong><br>→ Füge ein konkretes Beispiel in die <code>nextjs.instructions.md</code> ein. Copilot folgt Beispielen besser als abstrakten Regeln.</td>
<td><strong>Agent writes bad Next.js code (e.g. wrong API usage)</strong><br>→ Add a concrete code example to <code>nextjs.instructions.md</code>. Copilot follows examples better than abstract rules.</td>
</tr>
<tr>
<td><strong>Agent "vergisst" den Kontext nach langen Gesprächen</strong><br>→ Starte ein neues Chat-Fenster. Langer Kontext verdrängt Instructions. Übergib den Plan explizit: <em>"Hier ist der Plan: [Plan]. Bitte implementiere Schritt 3."</em></td>
<td><strong>Agent "forgets" context after long conversations</strong><br>→ Start a new chat window. Long context pushes out instructions. Pass the plan explicitly: <em>"Here is the plan: [plan]. Please implement step 3."</em></td>
</tr>
<tr>
<td><strong>Agent antwortet auf Englisch statt Deutsch (oder umgekehrt)</strong><br>→ Füge in <code>copilot-instructions.md</code> eine Sprachanweisung hinzu: <em>"Antworte immer auf Deutsch."</em> — oder sprich den Agent in der gewünschten Sprache an.</td>
<td><strong>Agent responds in German instead of English (or vice versa)</strong><br>→ Add a language instruction to <code>copilot-instructions.md</code>: <em>"Always respond in English."</em> — or address the agent in your preferred language.</td>
</tr>
<tr>
<td><strong>Agent überschreitet den Plan / macht ungebetene Änderungen</strong><br>→ Füge in der <code>.agent.md</code> unter "Rules" hinzu: <em>"Ändere nur Dateien, die explizit im Plan genannt sind. Keine ungebetenen Refactors."</em></td>
<td><strong>Agent exceeds the plan / makes unrequested changes</strong><br>→ Add to the <code>.agent.md</code> under "Rules": <em>"Only modify files explicitly listed in the plan. No unrequested refactoring."</em></td>
</tr>
</table>

---

## Referenzen / References

- [GitHub Copilot Customisation Docs](https://docs.github.com/en/copilot/customizing-copilot)
- [awesome-copilot](https://github.com/github/awesome-copilot) — Beispiele und Best Practices / Examples and best practices

## ./HOWTO.md
# HOWTO — Project Setup & Deployment Guide

> 🎉 **Herzlichen Glückwunsch zur Einrichtung! / Congratulations on setting up!**
> Du kannst dieses Dokument nach Abschluss der Einrichtung löschen oder als Referenz behalten.
> You can delete this HOWTO document once your setup is complete, or keep it for future reference.

> 📖 **Lies die [AGENTS.md](AGENTS.md) Datei, um GitHub Copilot optimal und produktiv zu nutzen.**
> **Read the [AGENTS.md](AGENTS.md) file to use GitHub Copilot in an optimised and productive way.**

---

## DE Deutsch

---

### Prozessübersicht

Folge diesen Schritten in der angegebenen Reihenfolge, um vom Template zur Produktion zu gelangen:

1. **GitHub Repo erstellen** — Nutze dieses Template, um ein neues Repository in der Wamocon GitHub Organisation zu erstellen.
2. **Repo klonen** — Klone es auf deinen Rechner und führe `npm install` aus.
3. **Pre-commit Hook installieren** — Führe `bash hooks/install.sh` aus. Einmalig nach dem Klonen — schützt dich davor, Geheimnisse versehentlich zu pushen.
4. **GitHub Workflow-Datei überprüfen** — Öffne `.github/workflows/deploy.yml` und `.github/workflows/pr-pipeline.yml`, überprüfe, dass `Wamocon/github_workflow` die korrekte Referenz ist.
5. **`.env.local` aktualisieren & Supabase verbinden** — Kopiere `.env.example` → `.env.local`, erstelle ein Remote-Supabase-Projekt und trage die Zugangsdaten ein.
6. **Lokal starten & Entwicklung beginnen** — Führe `npm run dev` aus und beginne mit der Entwicklung.
7. **GitHub-Organisationseinstellungen: Vercel-App Zugriff gewähren** — Gehe zu den Organisationseinstellungen auf GitHub, suche die Vercel GitHub-App und gewähre ihr Zugriff auf dein neues Repo. Nur so erscheint das Repo in der Vercel-Importliste.
8. **Repo vorübergehend öffentlich machen & bei Vercel importieren** — Stelle das Repo temporär auf öffentlich und importiere es in Vercel.
9. **Vercel Project ID holen** — Kopiere die Vercel Project ID aus den Vercel-Projekteinstellungen.
10. **Vercel Project ID zu GitHub Secrets hinzufügen** — Füge `VERCEL_PROJECT_ID` zu den GitHub Actions Secrets deines Repos hinzu.
11. **Repo auf intern umstellen** — Ändere die Sichtbarkeit des Repos zurück auf intern.
12. **Erstes manuelles Deployment** — Gehe zu `Actions → "Deploy to Vercel" → Run workflow` und wähle `production`.

> 📖 **Für detaillierte Informationen, lies weiter unten.**

---

### 1. Klonen & Einrichten

```bash
# Repository klonen
git clone https://github.com/Wamocon/<dein-repo-name>.git
cd <dein-repo-name>

# Abhängigkeiten installieren
npm install

# Umgebungsvariablen kopieren
cp .env.example .env.local

# Pre-commit Hook installieren (einmalig, direkt nach npm install)
bash hooks/install.sh

# Entwicklungsserver starten (mit Turbopack für schnelles Hot-Reload)
npm run dev
```

Öffne [http://localhost:3000](http://localhost:3000) in deinem Browser.

**Verfügbare Skripte:**

| Befehl | Beschreibung |
|---|---|
| `npm run dev` | Startet den Dev-Server mit Turbopack (Hot Reload) |
| `npm run build` | Erstellt den Produktions-Build |
| `npm run start` | Startet den Produktionsserver |
| `npm run lint` | Führt ESLint aus |
| `npm run typecheck` | Führt TypeScript-Typprüfung aus |

---

### 1b. Git-Workflow & Branch-Strategie

> 💡 **Arbeite nach dem ersten Push immer auf einem Branch — nie direkt auf `main`/`master`.**

**Empfohlener Ablauf:**

```bash
# Einmalig: Ersten Stand auf main/master pushen
git add .
git commit -m "chore: initial setup"
git push origin <main-oder-master>

# Ab jetzt: Immer auf einem Feature-Branch arbeiten
git checkout -b feature/mein-feature

# Änderungen lokal testen, dann committen
npm run dev        # testen
npm run typecheck  # Typfehler prüfen
npm run lint       # Lint prüfen

git add .
git commit -m "feat: beschreibung der Änderung"
git push origin feature/mein-feature
```

**Wichtige Regeln:**

- **Lokal testen, bevor du pushst.** Führe `npm run typecheck` und `npm run lint` aus, bevor du Änderungen pushst.
- **Alle Änderungen vor dem PR-Öffnen pushen.** Jeder neue Push auf einen offenen PR triggert automatisch die GitHub Actions — das verbraucht GitHub Actions-Minuten.
- **Nur einen PR auf einmal offen halten**, bis er gemergt ist.

> ⚠️ **Warum das wichtig ist:** Jeder Push auf einen offenen PR löst die PR Pipeline aus (Auto-Fix + Typecheck + Lint). Teste erst lokal — dann push, dann PR.

---

### 1c. Pre-commit Hook — Geheimnis-Scanner

Der Pre-commit Hook verhindert, dass API-Schlüssel, Tokens, Passwörter oder andere Geheimnisse versehentlich in GitHub eingecheckt werden. Der Hook scannt alle für den Commit vorgesehenen Dateien, **bevor** der Commit abgeschlossen wird.

#### Installation

```bash
# Einmalig nach dem Klonen ausführen — nie wieder nötig:
bash hooks/install.sh
```

> ✅ **Wie oft?** Genau **einmal** — direkt nach `npm install` beim ersten Einrichten des Repos. Nach der Installation läuft der Hook automatisch vor **jedem** `git commit`.

#### Was der Hook prüft

| Muster | Beispiel |
|--------|---------|
| AWS-Schlüssel | `AKIA...`, `aws_secret_access_key = ...` |
| GitHub-Tokens | `ghp_...`, `github_pat_...` |
| Vercel-Token | `VERCEL_TOKEN = abc123...` |
| Private Keys (PEM) | `-----BEGIN PRIVATE KEY-----` |
| Datenbankverbindungen | `postgres://user:password@host` |
| Generische Tokens | `api_key =`, `client_secret =`, `password =` |
| JWT-Tokens | `eyJ...` (vollständige `header.payload.signature`-Form) |
| Supabase Service Role | `service_role = eyJ...` |
| `.env`-Dateien | `.env`, `.env.local`, `.env.production` |

#### Wenn ein Commit blockiert wird

```
[pre-commit] BLOCKED — potential secrets detected
  ✖ src/lib/config.ts:12
    Reason: Generic API key
    Content: const API_KEY = "abc123xyz789..."
```

**Lösung:**
1. Entferne das Geheimnis aus der Datei.
2. Speichere es in deiner `.env.local` (ist bereits in `.gitignore` eingetragen).
3. Nutze GitHub Actions Secrets für CI/CD-Werte.

**Bei einem Falsch-Positiv** (z.B. ein Beispielwert in der Doku):
Füge den Kommentar `# notsecret` am Ende der betroffenen Zeile hinzu.

**Notfall-Bypass** (nur im absoluten Ausnahmefall — niemals für echte Geheimnisse!):
```bash
git commit --no-verify -m "deine Nachricht"
```

---

### 2. Supabase Setup & Warnung

> ⚠️ **KRITISCH: Sobald du einen Supabase-Account hast, speichere alle Testdaten direkt dort.**
>
> **Lege Testdaten NICHT als lokale Dateien im Projektverzeichnis ab** (z.B. JSON-Fixtures, SQL-Dumps). Füge Daten stattdessen direkt in dein Supabase-Projekt ein — über das Dashboard, per MCP-Tool oder per Migrations-Skript.

**Schritte:**

1. Gehe zu [supabase.com](https://supabase.com) und erstelle ein neues Projekt.
2. Kopiere die **Project URL**, den **Anon Key** und den **Service Role Key** aus  
   `Project Settings → API`.
3. Trage sie in deine `.env.local` Datei ein:
   ```
   NEXT_PUBLIC_SUPABASE_URL=https://your-project-ref.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=dein-anon-key
   SUPABASE_SERVICE_ROLE_KEY=dein-service-role-key
   ```

---

### 2b. Lokales Supabase Setup via Docker (Optional)

> 💡 **Dieser Schritt ist optional.** Standardmäßig verbindest du dich direkt mit einem Remote-Supabase-Projekt (siehe Abschnitt 2). Nur wenn du lieber vollständig lokal entwickelst, ohne Internetverbindung zu Supabase, verwende dieses Setup.

Für ein vollständig lokales Supabase-Setup mit Docker und einer migrations-basierten Entwicklung, kopiere diesen Prompt in deinen KI-Assistenten (z.B. GitHub Copilot in VS Code):

```
Act as an expert DevOps and database engineer. I am developing an app locally. I need to set up a local Supabase instance via Docker and establish a strict migration-based workflow. Please execute the following:

Setup: Initialize a local Supabase environment using Docker and the Supabase CLI. Check automatically before every task if Docker and the Supabase containers are running. When they are down, start them autonomously.

Initial Schema: Create the initial database schema for the app and save it as a formal Supabase migration file.

Environment Variables: Automatically extract the local Supabase connection details (API URL, anon key, service role key, DB URL) and append them to my local .env file.

Autonomous Development & Schema Versioning: You will develop the entire application based on my prompts. You must autonomously create and update tables, generate schemas, and create timestamped migration files for every change. Ensure strict version history and guarantee that absolutely no functions fail due to database inconsistencies.

Production Deployment via MCP: I use the Supabase MCP to push data to production tables. Do not provide manual push commands. Your only job for production is to verify that all local migrations are completely up to date and error-free so the MCP can handle the live deployment seamlessly.

Automated Testing & Verification: Once the Docker setup is running and the schema is applied, automatically write and execute a small integration test. This test must verify that the app can successfully read from and write to the local Docker database. If any errors or bugs are detected, diagnose and fix them immediately on your own.
```

#### Lokale Supabase-Oberfläche im Browser öffnen

Sobald der lokale Docker-Stack läuft (`npx supabase start`), stellt Supabase eine vollständige Studio-Oberfläche bereit:

| Service | URL | Beschreibung |
|---|---|---|
| **Supabase Studio** | `http://localhost:54323` | Datenbank-UI: Tabellen, SQL-Editor, Auth, Storage |
| **REST API** | `http://localhost:54321` | PostgREST API (dein App-Endpoint) |
| **PostgreSQL** | `localhost:54322` | Direktzugriff (z.B. via pgAdmin, TablePlus) |
| **Inbucket (E-Mail)** | `http://localhost:54324` | Lokaler E-Mail-Dienst für Auth-Mails |

> 💡 Die exakten Ports werden nach `npx supabase start` auch in der Konsole ausgegeben. Der Befehl `npx supabase status` zeigt sie jederzeit an.

**Lokale Umgebungsvariablen:**
```
NEXT_PUBLIC_SUPABASE_URL=http://localhost:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=<aus supabase status kopieren>
SUPABASE_SERVICE_ROLE_KEY=<aus supabase status kopieren>
SUPABASE_DB_URL=postgresql://postgres:postgres@localhost:54322/postgres
```

---

### 3. Supabase MCP & Schemas

#### Supabase MCP für Migrationen verwenden

Der Supabase MCP (Model Context Protocol) Server ermöglicht es deinem KI-Coding-Assistenten (z.B. GitHub Copilot, Cursor), Migrationen und Tabellen direkt zu erstellen und zu verwalten.

- Migrationen werden in `supabase/migrations/` gespeichert.
- Nutze die MCP-Tools, um Tabellen zu erstellen, Schemas zu ändern und Indizes zu verwalten.

#### Arbeiten mit mehreren Schemas

Standardmäßig macht Supabase nur das `public`-Schema über die API verfügbar. Wenn du eigene Schemas brauchst:

**1. Schema erstellen:**
```sql
CREATE SCHEMA IF NOT EXISTS app;
```

**2. Berechtigungen vergeben:**
```sql
GRANT USAGE ON SCHEMA app TO anon, authenticated, service_role;
GRANT ALL ON ALL TABLES IN SCHEMA app TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA app
  GRANT ALL ON TABLES TO anon, authenticated, service_role;
GRANT ALL ON ALL SEQUENCES IN SCHEMA app TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA app
  GRANT ALL ON SEQUENCES TO anon, authenticated, service_role;
```

**3. Schema über die Supabase API zugänglich machen:**
Gehe zu `Project Settings → API → Exposed schemas` und füge deinen Schema-Namen hinzu.

---

### 4. GitHub Workflow Konfiguration

Dieses Projekt nutzt den **zentralen Wamocon CI/CD-Workflow** aus [`Wamocon/github_workflow`](https://github.com/Wamocon/github_workflow).

#### Übersicht der drei Workflows

| Workflow | Datei | Auslöser | Was es tut |
|---|---|---|---|
| **PR Pipeline** | `pr-pipeline.yml` | **Automatisch** bei jedem PR auf `main`/`master` | Auto-Fix (ESLint + Prettier) → Typecheck + Lint |
| **Deploy** | `deploy.yml` | **Manuell** — kein Auto-Trigger | Baut das Projekt via Vercel CLI und deployed auf Vercel |
| **LP Generator** | `lp-generator.yml` | **Manuell** — kein Auto-Trigger | Generiert eine Landing Page in einem neuen Repo |

> ⚠️ **Kein automatisches Deployment:** Weder ein PR noch ein Push auf `main` startet automatisch ein Deployment. Alle Deployments werden manuell über den Actions-Tab gestartet.

#### Was du tun musst

1. Überprüfe, dass `Wamocon/github_workflow` die korrekte Org/Repo-Referenz ist.
2. Aktiviere Workflow-Schreibrechte:  
   `Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests`
3. Füge **ein einziges Secret** zu deinem Repository hinzu:
   - Gehe zu `Repository → Settings → Secrets and variables → Actions → New repository secret`
   - Name: `VERCEL_PROJECT_ID`
   - Wert: *(siehe Abschnitt 5 unten)*

> ✅ **Alle anderen benötigten Secrets** (`VERCEL_TOKEN`, `VERCEL_ORG_ID`) sind **bereits auf GitHub-Organisationsebene konfiguriert**.

#### Manuelles Deployment starten

```
Repository auf GitHub → Actions → "Deploy to Vercel" → Run workflow
→ Environment auswählen: production oder preview
→ Run workflow klicken
```

---

### 5. Vercel Deployment-Strategie

#### Schritt 1: GitHub-Org Vercel-App Zugriff gewähren (Einmalig, Kritisch)

> ⚠️ **Dieser Schritt muss VOR dem Vercel-Import durchgeführt werden.** Ohne ihn erscheint dein Repo nicht in der Vercel-Importliste — auch wenn es öffentlich ist.

1. Gehe zu **GitHub → Wamocon Organisation → Settings**  
   `https://github.com/organizations/Wamocon/settings/installations`
2. Suche die **Vercel**-App in der Liste der installierten GitHub Apps.
3. Klicke auf **Configure**.
4. Scrolle zu **Repository access**.
5. Wähle **"Only select repositories"** und füge dein neues Repo hinzu.
6. Klicke **Save**.

#### Schritt 2: Erstmalige Bereitstellung (Einmalig)

1. **Repo vorübergehend öffentlich machen**  
   `Repository → Settings → General → Change visibility → Public`
2. Gehe zu [vercel.com](https://vercel.com) → **Add New Project** → **Import** → dein Repo auswählen.
3. Deploye das Projekt (Vercel erkennt Next.js automatisch).
4. **Vercel Project ID kopieren:**  
   `Vercel Project → Settings → General → Project ID` → ID kopieren.
5. **Zu GitHub Secrets hinzufügen:**  
   `Repository → Settings → Secrets and variables → Actions → New repository secret`  
   Name: `VERCEL_PROJECT_ID` | Wert: die kopierte ID.
6. **Repo auf intern zurücksetzen:**  
   `Repository → Settings → General → Change visibility → Internal`

> 💡 **Nach diesem einmaligen Setup** deployt die GitHub Action via Vercel CLI — Vercel sieht nicht mehr, wer committed, und es gibt keine Team-Seat-Fehler bei einem privaten Hobby-Account.

#### Schritt 3: Umgebungsvariablen in Vercel eintragen

> ⚠️ **WICHTIG:** Gehe zu `Vercel Project → Settings → Environment Variables` und füge **alle** Variablen aus deiner `.env.local` hinzu. Ohne diese wird der Build **fehlschlagen**.

#### Deployment-Ablauf (nach dem Setup)

| Auslöser | Ergebnis |
|---|---|
| PR auf `main`/`master` | PR Pipeline läuft automatisch (kein Deployment) |
| Merge auf `main`/`master` | Kein automatisches Deployment |
| **Manuelles Workflow-Start** | Deployment nach Auswahl: `production` oder `preview` |

**Manuell deployen:**

```
GitHub → Actions → "Deploy to Vercel" → Run workflow
→ environment: production  (für die Live-URL)
→ environment: preview     (für eine Test-URL)
→ db_schema: (leer lassen — Vercel-Umgebungsvariablen werden genutzt)
```

---

### 6. Domain-Verwaltung

1. **Sichere eine Domain** für deine Anwendung über [Strato](https://www.strato.de).
2. Gehe in den Vercel-Projekteinstellungen zu `Settings → Domains` und füge deine Domain hinzu.
3. Konfiguriere die DNS-Einträge bei Strato wie von Vercel angegeben (typischerweise CNAME oder A-Record).

---

### 7. Projekt-Checkliste

- [ ] Landing Page
- [ ] Handbuch / Manual
- [ ] Hauptprozess (Kernfunktion)
- [ ] Video (Demo / Tutorial)
- [ ] Domain (über Strato gesichert)

---

### 8. Landing Page Generator

Das Workflow-File `.github/workflows/lp-generator.yml` generiert eine Landing Page für diese App.

#### Was der Workflow tut

- Liest den Inhalt dieses Repos aus
- Verwendet ein konfigurierbares **Design-Template** als optische Basis
- Lässt GitHub Copilot eine Landing Page generieren und ein neues Repo dafür anlegen

#### Was du ändern kannst

| Eingabe | Standard | Beschreibung |
|---|---|---|
| `custom_template` | `Wamocon/hochzeitsrechner_lp` | Das GitHub-Repo, das als Design-Template dient |
| `custom_name` | `generated_lp` | Name des neu erstellten Landing-Page-Repos |
| `custom_prompt` | *(allgemeiner Prompt)* | Detaillierte Anweisungen für Copilot |

> 💡 **Tipp:** Je spezifischer dein Prompt, desto besser die generierte Landing Page.

#### Wann du den Workflow starten sollst

Starte diesen Workflow **erst dann**, wenn dein Projekt weitgehend fertig dokumentiert ist:
- Handbuch / Manual
- README mit Produktbeschreibung, Features und Zielgruppe
- Rechtstexte / relevante Seiten

> ✅ **Empfehlung:** In der Regel reicht **ein einmaliger Lauf** am Projektende.

#### Manuell ausführen

`Repository → Actions → "🚀 lp-generator" → Run workflow`

1. Wähle in der linken Liste den Workflow **"🚀 lp-generator"**.
2. Klicke rechts auf **"Run workflow"**.
3. Passe Template, Name und Prompt an.
4. Bestätige mit **"Run workflow"**.

#### Wenn der Workflow fehlschlägt

Wenn bereits ein Repository mit gleichem Namen existiert:
1. Ändere den Namen in `custom_name` und starte erneut.
2. Oder lösche das bestehende Ziel-Repo und starte erneut.

---
---

## EN English

---

### Process Overview

Follow these steps in order to go from template to production:

1. **Create GitHub Repo** — Use this template to create a new repository in the Wamocon GitHub organisation.
2. **Clone Repo** — Clone to your local machine and run `npm install`.
3. **Install pre-commit hook** — Run `bash hooks/install.sh`. One-time setup after cloning — protects you from accidentally pushing secrets.
4. **Check GitHub Workflow files** — Open `.github/workflows/deploy.yml` and `.github/workflows/pr-pipeline.yml`, verify that `Wamocon/github_workflow` is the correct reference.
5. **Update `.env.local` & connect Supabase** — Copy `.env.example` → `.env.local`, create a remote Supabase project, and fill in the credentials.
6. **Run locally & start development** — Run `npm run dev` and start building.
7. **GitHub Organisation Settings: Grant Vercel app access** — Go to the organisation settings on GitHub, find the Vercel GitHub App, and grant it access to your new repo. Without this, the repo will not appear in Vercel's import list.
8. **Make repo temporarily public & import in Vercel** — Set the repo to public temporarily and import it in Vercel.
9. **Get Vercel Project ID** — Copy the Vercel Project ID from the Vercel project settings.
10. **Add Vercel Project ID to GitHub secrets** — Add `VERCEL_PROJECT_ID` to your repository's GitHub Actions secrets.
11. **Make repo internal** — Revert the repository visibility to internal.
12. **First manual deployment** — Go to `Actions → "Deploy to Vercel" → Run workflow` and choose `production`.

> 📖 **For detailed information, read below.**

---

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/Wamocon/<your-repo-name>.git
cd <your-repo-name>

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env.local

# Install pre-commit hook (once, right after npm install)
bash hooks/install.sh

# Start the development server (with Turbopack for fast refresh)
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

**Available scripts:**

| Command | Description |
|---|---|
| `npm run dev` | Start dev server with Turbopack (hot reload) |
| `npm run build` | Create production build |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |
| `npm run typecheck` | Run TypeScript type checking |

---

### 1b. Git Workflow & Branching Strategy

> 💡 **After the first push, always work on a branch — never directly on `main`/`master`.**

**Recommended flow:**

```bash
# One-time: push the initial state to main/master
git add .
git commit -m "chore: initial setup"
git push origin <main-or-master>

# From now on: always work on a feature branch
git checkout -b feature/my-feature

# Test locally, then commit
npm run dev        # test in browser
npm run typecheck  # catch type errors
npm run lint       # catch lint issues

git add .
git commit -m "feat: description of change"
git push origin feature/my-feature
```

**Key rules:**

- **Test locally before pushing.** Always run `npm run typecheck` and `npm run lint` before pushing.
- **Push all changes before opening the PR.** Every new push to an open PR triggers the GitHub Actions pipeline — this consumes GitHub Actions minutes.
- **Keep only one PR open at a time** until it is merged.

> ⚠️ **Why this matters:** Every push to an open PR triggers the PR Pipeline (Auto-Fix + Typecheck + Lint). Test locally first — then push, then open the PR.

---

### 1c. Pre-commit Hook — Secret Scanner

The pre-commit hook prevents API keys, tokens, passwords, or other secrets from accidentally being checked into GitHub. The hook scans all files staged for commit **before** the commit is finalised.

#### Installation

```bash
# Run ONCE after cloning — never needs to run again:
bash hooks/install.sh
```

> ✅ **How often?** Exactly **once** — right after `npm install` when first setting up the repo. After installation, the hook runs automatically before **every** `git commit`.

#### What the hook checks

| Pattern | Example |
|--------|---------|
| AWS keys | `AKIA...`, `aws_secret_access_key = ...` |
| GitHub tokens | `ghp_...`, `github_pat_...` |
| Vercel token | `VERCEL_TOKEN = abc123...` |
| Private keys (PEM) | `-----BEGIN PRIVATE KEY-----` |
| Database connection strings | `postgres://user:password@host` |
| Generic tokens | `api_key =`, `client_secret =`, `password =` |
| JWT tokens | `eyJ...` (full `header.payload.signature` form) |
| Supabase service role | `service_role = eyJ...` |
| `.env` files | `.env`, `.env.local`, `.env.production` |

#### When a commit is blocked

```
[pre-commit] BLOCKED — potential secrets detected
  ✖ src/lib/config.ts:12
    Reason: Generic API key
    Content: const API_KEY = "abc123xyz789..."
```

**How to fix:**
1. Remove the secret from the file.
2. Store it in your `.env.local` (already in `.gitignore`).
3. Use GitHub Actions secrets for CI/CD values.

**False positive** (e.g. an example value in documentation):  
Add the comment `# notsecret` at the end of that line.

**Emergency bypass** (absolute last resort — never for real secrets!):
```bash
git commit --no-verify -m "your message"
```

---

### 2. Supabase Setup & Warning

> ⚠️ **CRITICAL: Once you have a Supabase account, store all test data there directly.**
>
> **Do NOT store test data as local files** (e.g. JSON fixtures, SQL dumps). Insert data directly into your Supabase project — via the Dashboard, an MCP tool, or a migration script.

**Steps:**

1. Go to [supabase.com](https://supabase.com) and create a new project.
2. Copy the **Project URL**, **Anon Key**, and **Service Role Key** from  
   `Project Settings → API`.
3. Paste them into your `.env.local` file:
   ```
   NEXT_PUBLIC_SUPABASE_URL=https://your-project-ref.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
   SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
   ```

---

### 2b. Local Supabase Setup via Docker (Optional)

> 💡 **This step is optional.** By default you connect directly to a remote Supabase project (see section 2). Only use this setup if you prefer developing fully offline.

For a fully local Supabase setup with Docker and a migration-based development workflow, copy this prompt into your AI assistant (e.g. GitHub Copilot in VS Code):

```
Act as an expert DevOps and database engineer. I am developing an app locally. I need to set up a local Supabase instance via Docker and establish a strict migration-based workflow. Please execute the following:

Setup: Initialize a local Supabase environment using Docker and the Supabase CLI. Check automatically before every task if Docker and the Supabase containers are running. When they are down, start them autonomously.

Initial Schema: Create the initial database schema for the app and save it as a formal Supabase migration file.

Environment Variables: Automatically extract the local Supabase connection details (API URL, anon key, service role key, DB URL) and append them to my local .env file.

Autonomous Development & Schema Versioning: You will develop the entire application based on my prompts. You must autonomously create and update tables, generate schemas, and create timestamped migration files for every change. Ensure strict version history and guarantee that absolutely no functions fail due to database inconsistencies.

Production Deployment via MCP: I use the Supabase MCP to push data to production tables. Do not provide manual push commands. Your only job for production is to verify that all local migrations are completely up to date and error-free so the MCP can handle the live deployment seamlessly.

Automated Testing & Verification: Once the Docker setup is running and the schema is applied, automatically write and execute a small integration test. This test must verify that the app can successfully read from and write to the local Docker database. If any errors or bugs are detected, diagnose and fix them immediately on your own.
```

#### Viewing the local database in the browser

| Service | URL | Description |
|---|---|---|
| **Supabase Studio** | `http://localhost:54323` | Database UI: tables, SQL editor, Auth, Storage |
| **REST API** | `http://localhost:54321` | PostgREST API (your app endpoint) |
| **PostgreSQL** | `localhost:54322` | Direct DB access (e.g. pgAdmin, TablePlus) |
| **Inbucket (email)** | `http://localhost:54324` | Local email service for Auth emails |

**Local environment variables:**
```
NEXT_PUBLIC_SUPABASE_URL=http://localhost:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=<copy from supabase status output>
SUPABASE_SERVICE_ROLE_KEY=<copy from supabase status output>
SUPABASE_DB_URL=postgresql://postgres:postgres@localhost:54322/postgres
```

---

### 3. Supabase MCP & Schemas

#### Using Supabase MCP for Migrations

The Supabase MCP (Model Context Protocol) server allows your AI coding assistant to create and manage migrations and tables directly.

- Migrations are stored in `supabase/migrations/`.
- Use the MCP tools to create tables, alter schemas, and manage indexes.

#### Working with Multiple Schemas

By default, Supabase only exposes the `public` schema via the API. If you need custom schemas:

**1. Create the schema:**
```sql
CREATE SCHEMA IF NOT EXISTS app;
```

**2. Grant permissions:**
```sql
GRANT USAGE ON SCHEMA app TO anon, authenticated, service_role;
GRANT ALL ON ALL TABLES IN SCHEMA app TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA app
  GRANT ALL ON TABLES TO anon, authenticated, service_role;
GRANT ALL ON ALL SEQUENCES IN SCHEMA app TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA app
  GRANT ALL ON SEQUENCES TO anon, authenticated, service_role;
```

**3. Expose the schema via the Supabase API:**
Go to `Project Settings → API → Exposed schemas` and add your custom schema name.

---

### 4. GitHub Workflow Configuration

This project uses the **centralized Wamocon CI/CD workflow** from [`Wamocon/github_workflow`](https://github.com/Wamocon/github_workflow).

#### Overview of the three workflows

| Workflow | File | Trigger | What it does |
|---|---|---|---|
| **PR Pipeline** | `pr-pipeline.yml` | **Automatic** on every PR to `main`/`master` | Auto-Fix (ESLint + Prettier) → Typecheck + Lint |
| **Deploy** | `deploy.yml` | **Manual only** — no auto-trigger | Builds and deploys to Vercel via CLI |
| **LP Generator** | `lp-generator.yml` | **Manual only** — no auto-trigger | Generates a landing page in a new repo |

> ⚠️ **No automatic deployment:** Neither a PR nor a push to `main` triggers a deployment automatically. All deployments are started manually from the Actions tab.

#### What you need to do

1. Verify that `Wamocon/github_workflow` is the correct org/repo reference.
2. Enable workflow write permissions:  
   `Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests`
3. Add **one single secret** to your repository:
   - Go to `Repository → Settings → Secrets and variables → Actions → New repository secret`
   - Name: `VERCEL_PROJECT_ID`
   - Value: *(see section 5 below)*

> ✅ **All other required secrets** (`VERCEL_TOKEN`, `VERCEL_ORG_ID`) are **already configured at the GitHub Organisation level**.

#### Triggering a manual deployment

```
GitHub repo → Actions → "Deploy to Vercel" → Run workflow
→ Choose environment: production or preview
→ Click "Run workflow"
```

---

### 5. Vercel Deployment Strategy

#### Step 1: Grant Vercel GitHub App access in Org Settings (One-time, Critical)

> ⚠️ **This step must be done BEFORE importing in Vercel.** Without it, your repo will not appear in Vercel's import list — even if it is public.

1. Go to **GitHub → Wamocon Organisation → Settings → Installed GitHub Apps**  
   `https://github.com/organizations/Wamocon/settings/installations`
2. Find the **Vercel** app in the list.
3. Click **Configure**.
4. Scroll to **Repository access**.
5. Select **"Only select repositories"** and add your new repo.
6. Click **Save**.

#### Step 2: Initial Deployment (One-Time)

1. **Make the repo public** temporarily  
   `Repository → Settings → General → Change visibility → Public`
2. Go to [vercel.com](https://vercel.com) → **Add New Project** → **Import** → select your repo.
3. Deploy the project (Vercel detects Next.js automatically).
4. **Copy the Vercel Project ID:**  
   `Vercel Project → Settings → General → Project ID` → copy the value.
5. **Add to GitHub secrets:**  
   `Repository → Settings → Secrets and variables → Actions → New repository secret`  
   Name: `VERCEL_PROJECT_ID` | Value: the ID you copied.
6. **Revert the repo to internal:**  
   `Repository → Settings → General → Change visibility → Internal`

> 💡 **After this one-time setup**, the GitHub Action deploys via Vercel CLI — Vercel no longer sees who committed, and there are no team seat errors with a personal Hobby account.

#### Step 3: Add environment variables in Vercel

> ⚠️ **CRUCIAL:** Go to `Vercel Project → Settings → Environment Variables` and add **all** variables from your `.env.local`. Without these, the build **will fail**.

#### Deployment flow (after setup)

| Trigger | Result |
|---|---|
| PR targeting `main`/`master` | PR Pipeline runs automatically (no deployment) |
| Merge / push to `main`/`master` | No automatic deployment |
| **Manual workflow run** | Deploys to the chosen environment: `production` or `preview` |

**How to deploy manually:**

```
GitHub → Actions → "Deploy to Vercel" → Run workflow
→ environment: production  (for the live URL)
→ environment: preview     (for a temporary test URL)
→ db_schema: (leave empty — Vercel env vars are used)
```

---

### 6. Domain Management

1. **Secure a domain** for your application via [Strato](https://www.strato.de).
2. In the Vercel project settings, go to `Settings → Domains` and add your domain.
3. Configure the DNS records at Strato as shown by Vercel (typically a CNAME or A record).

---

### 7. Project Checklist

- [ ] Landing Page
- [ ] Handbuch / Manual
- [ ] Main Process (core feature)
- [ ] Video (demo / tutorial)
- [ ] Domain (secured via Strato)

---

### 8. Landing Page Generator

The workflow file `.github/workflows/lp-generator.yml` generates a landing page for this app by calling a central, reusable Wamocon workflow.

#### What the workflow does

- Reads the contents of this repository
- Uses a configurable **design template** as a visual base
- Lets GitHub Copilot generate a landing page and create a new repository for it

#### What you can change

| Input | Default | Description |
|---|---|---|
| `custom_template` | `Wamocon/hochzeitsrechner_lp` | The GitHub repo used as the design template |
| `custom_name` | `generated_lp` | Name for the newly created landing page repository |
| `custom_prompt` | *(generic prompt)* | Detailed instructions for Copilot |

> 💡 **Tip:** The more specific your prompt, the better the generated landing page.

#### When you should run this workflow

Run this workflow **only after** your project is mostly complete:
- Handbook / Manual
- README with product description, features, and target audience
- Legal pages / relevant links

> ✅ **Recommendation:** In most cases, you only need to run it **once** at the end of the project.

#### Running manually

`Repository → Actions → "🚀 lp-generator" → Run workflow`

1. Select **"🚀 lp-generator"** from the left workflow list.
2. Click **"Run workflow"** on the right.
3. Adjust the input fields (template, name, prompt) as needed.
4. Confirm with **"Run workflow"**.

#### If the workflow fails (repository name already exists)

1. Change the `custom_name` value and run the workflow again.
2. Or delete the existing target repository (if no longer needed) and run again.

## ./IDEA.md
# Projektidee

> Fuell diese Datei aus, bevor du den Skill `anforderungsdokument` aufrufst.
> Je mehr Details du hier schreibst, desto besser wird das generierte Dokument.
> Anleitung: `.github/skills/anforderungsdokument/SKILL.md`

---

## Projektname

[Name der App, z.B. "Universal Inventory Manager"]

---

## Beschreibung

[Was macht die App? Welches Problem loest sie? Sei konkret.

Beispiel:
"Eine webbasierte Lagerverwaltungs-App fuer kleine und mittelgrosse Unternehmen in
Deutschland. Sie ersetzt Excel-basierte Bestandslisten durch ein strukturiertes System
mit Echtzeit-Uebersicht, QR-Code-Scanfunktion und automatisierten Benachrichtigungen.
Das Ziel ist es, manuelle Fehler bei der Lagerhaltung um mindestens 80 % zu reduzieren
und den Zeitaufwand fuer Inventurprozesse auf ein Minimum zu senken."]

---

## Zielgruppe

[Wer soll die App nutzen? Branche, Unternehmensgroesse, Rolle.

Beispiel:
"Lager- und Logistikleiter sowie Mitarbeiter in KMU mit 10 bis 200 Angestellten,
insbesondere im Einzel-, Gross- und Onlinehandel in Deutschland und dem
deutschsprachigen Europa."]

---

## Kernproblem

[Das konkrete Problem, das OHNE die App besteht.

Beispiel:
"Lagerfehler durch manuelle Erfassung in Excel kosten KMU durchschnittlich
14 % des Jahresumsatzes. Bestehende Enterprise-Loesungen wie SAP EWM sind
fuer kleinere Betriebe zu komplex und zu teuer."]

---

## Gewuenschte Hauptfunktionen (Version 1)

[Liste der wichtigsten Funktionen. Beispiel:]

- Artikel anlegen, bearbeiten, loeschen
- Lagerbestand in Echtzeit einsehen
- QR-Code-Etiketten generieren und scannen
- Rollenbasierter Zugriff (Admin, Manager, Mitarbeiter)
- Mehrsprachige Oberflaeche (Deutsch und Englisch)
- Dashboard mit Bestandsuebersicht

---

## Tech-Stack (optional, wenn bekannt)

[Bekannte oder gewuenschte Technologien. Standardempfehlung falls leer:
Next.js, React, TypeScript, Supabase, Tailwind CSS, Vercel]

---

## Marktsegment und Branche

[In welchem Markt soll die App operieren?

Beispiel: "Lagerverwaltungssoftware (WMS) fuer KMU in Deutschland, Segment Mittelstand"]

---

## Bekannte Wettbewerber (optional)

[Bestehende Loesungen, die aehnliches tun.

Beispiel: SAP EWM, Sage Wawi, Pickware, Odoo Inventory, Lightspeed]

---

## Ersteller

[Vollstaendiger Name]

---

## Empfaenger (Geschaeftsfuehrung)

[Name und Titel des Entscheidungstraegers, z.B. "waleri moretz, CEO WAMOCON GmbH"]

---

## Welle und Version

1

---

## Zusaetzliche Hinweise (optional)

[Besondere Anforderungen, Einschraenkungen, Deadlines oder andere relevante
Informationen, die im Dokument beruecksichtigt werden sollen.]

## ./anforderungen/SETUP-ANLEITUNG.md
# Setup-Anleitung: Supabase Cloud + Vercel

**Projekt:** SchufaCleaner  
**Datum:** Mai 2026  
**Erstellt von:** GitHub Copilot / WAMOCON GmbH

---

## Übersicht

Diese Anleitung beschreibt alle manuellen Einrichtungsschritte für:

1. **Supabase Cloud** — 3 Custom Schemas anlegen (Dev / Test / Prod)
2. **Vercel** — Projekt importieren und Umgebungsvariablen setzen
3. **GitHub Secrets** — für die CI/CD-Workflows

Die Reihenfolge ist verbindlich. Schritt für Schritt durcharbeiten.

---

## Teil 1 — Supabase Cloud: 3 Schemas anlegen

### Voraussetzung

Das Supabase-Projekt muss angelegt und aktiv sein (Status: **Active** im Dashboard).

Öffne das Supabase Dashboard → dein Projekt → **SQL Editor**.

---

### Schritt 1.1 — Schema `schufacleaner-dev` anlegen

> Wird lokal für die Entwicklung genutzt (`SUPABASE_DB_SCHEMA=schufacleaner-dev`).

```sql
-- Schema anlegen
CREATE SCHEMA IF NOT EXISTS "schufacleaner-dev";

-- Berechtigungen für authenticated-Role (eingeloggte Nutzer)
GRANT USAGE ON SCHEMA "schufacleaner-dev" TO authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA "schufacleaner-dev" TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-dev"
  GRANT ALL ON TABLES TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-dev"
  GRANT ALL ON SEQUENCES TO authenticated;

-- Berechtigungen für anon-Role (nicht eingeloggte Nutzer / öffentliche Daten)
GRANT USAGE ON SCHEMA "schufacleaner-dev" TO anon;
GRANT SELECT ON ALL TABLES IN SCHEMA "schufacleaner-dev" TO anon;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-dev"
  GRANT SELECT ON TABLES TO anon;

-- Vollzugriff für service_role (Server-seitig, bypassed RLS)
GRANT ALL ON SCHEMA "schufacleaner-dev" TO service_role;
GRANT ALL ON ALL TABLES IN SCHEMA "schufacleaner-dev" TO service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-dev"
  GRANT ALL ON TABLES TO service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-dev"
  GRANT ALL ON SEQUENCES TO service_role;
```

---

### Schritt 1.2 — Schema `schufacleaner-test` anlegen

> Wird für Vercel Preview-Deployments (Pull Requests) genutzt.

```sql
-- Schema anlegen
CREATE SCHEMA IF NOT EXISTS "schufacleaner-test";

-- Berechtigungen für authenticated-Role
GRANT USAGE ON SCHEMA "schufacleaner-test" TO authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA "schufacleaner-test" TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-test"
  GRANT ALL ON TABLES TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-test"
  GRANT ALL ON SEQUENCES TO authenticated;

-- Berechtigungen für anon-Role
GRANT USAGE ON SCHEMA "schufacleaner-test" TO anon;
GRANT SELECT ON ALL TABLES IN SCHEMA "schufacleaner-test" TO anon;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-test"
  GRANT SELECT ON TABLES TO anon;

-- Vollzugriff für service_role
GRANT ALL ON SCHEMA "schufacleaner-test" TO service_role;
GRANT ALL ON ALL TABLES IN SCHEMA "schufacleaner-test" TO service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-test"
  GRANT ALL ON TABLES TO service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-test"
  GRANT ALL ON SEQUENCES TO service_role;
```

---

### Schritt 1.3 — Schema `schufacleaner-prod` anlegen

> Wird für das Vercel Production-Deployment (Merge auf `main`) genutzt.

```sql
-- Schema anlegen
CREATE SCHEMA IF NOT EXISTS "schufacleaner-prod";

-- Berechtigungen für authenticated-Role
GRANT USAGE ON SCHEMA "schufacleaner-prod" TO authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA "schufacleaner-prod" TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-prod"
  GRANT ALL ON TABLES TO authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-prod"
  GRANT ALL ON SEQUENCES TO authenticated;

-- Berechtigungen für anon-Role
GRANT USAGE ON SCHEMA "schufacleaner-prod" TO anon;
GRANT SELECT ON ALL TABLES IN SCHEMA "schufacleaner-prod" TO anon;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-prod"
  GRANT SELECT ON TABLES TO anon;

-- Vollzugriff für service_role
GRANT ALL ON SCHEMA "schufacleaner-prod" TO service_role;
GRANT ALL ON ALL TABLES IN SCHEMA "schufacleaner-prod" TO service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-prod"
  GRANT ALL ON TABLES TO service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA "schufacleaner-prod"
  GRANT ALL ON SEQUENCES TO service_role;
```

---

### Schritt 1.4 — Schemas in der Supabase API exponieren

> PostgREST (die Supabase REST API) kennt nur Schemas, die explizit freigegeben sind.  
> Ohne diesen Schritt antwortet die API mit `404` oder `No schema match`.

**Manueller Schritt im Dashboard:**

1. Gehe zu: **Project Settings → API**
2. Scrolle zu **"Extra search path"** (auch: *"Exposed schemas"*)
3. Füge folgende Schemas hinzu (kommagetrennt):

```
schufacleaner-dev, schufacleaner-test, schufacleaner-prod
```

4. Klicke **Save**
5. Warte ca. 30 Sekunden — PostgREST wird neu gestartet.

> ⚠️ **Wichtig:** Ohne diesen Schritt sind alle API-Anfragen gegen die Custom Schemas mit einem `400 Bad Request` oder `404` Fehler fehlerhaft.

---

### Schritt 1.5 — Supabase Auth aktivieren (Email + Password)

1. Gehe zu: **Authentication → Providers**
2. Aktiviere **Email** als Provider
3. Stelle sicher, dass **"Confirm email"** zunächst auf `OFF` steht (vereinfacht das initiale Testen)
4. Setze die **Site URL** auf deine Produktions-Domain (z.B. `https://schufacleaner.vercel.app`)
5. Füge folgende **Redirect URLs** hinzu:
   - `http://localhost:3000/**` (lokal)
   - `https://*.vercel.app/**` (Vercel Previews)
   - `https://schufacleaner.vercel.app/**` (Produktion — nach Go-Live anpassen)

---

### Schritt 1.6 — Zugangsdaten notieren

Navigiere zu: **Project Settings → API**

Notiere folgende Werte — du brauchst sie in Teil 2 und Teil 3:

| Variable | Wo zu finden |
|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | Project URL (z.B. `https://xyz.supabase.co`) |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | `anon` / `public` Key |
| `SUPABASE_SERVICE_ROLE_KEY` | `service_role` Key — **GEHEIM, nie öffentlich!** |

---

## Teil 2 — Vercel: Projekt anlegen und Umgebungsvariablen setzen

### Schritt 2.1 — Vercel-App Zugriff auf GitHub-Repo gewähren

1. Gehe zu: **GitHub → Organisation Wamocon → Settings → GitHub Apps**
2. Suche die **Vercel GitHub App**
3. Klicke **Configure** und füge das Repository `schufacleaner` zur Liste der zugänglichen Repos hinzu

> Ohne diesen Schritt erscheint das Repo nicht in der Vercel-Importliste.

---

### Schritt 2.2 — Projekt in Vercel importieren

1. Öffne [vercel.com/new](https://vercel.com/new)
2. Wähle **"Import Git Repository"** und wähle `Wamocon/schufacleaner`
3. Framework: **Next.js** (wird automatisch erkannt)
4. **Noch nicht deployen** — zuerst Umgebungsvariablen setzen (Schritt 2.3)

---

### Schritt 2.3 — Umgebungsvariablen in Vercel setzen

Navigiere im Vercel-Projekt zu: **Settings → Environment Variables**

#### Für alle Environments (Development + Preview + Production)

| Variable | Wert |
|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | Deine Supabase Project URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Dein Supabase Anon Key |
| `SUPABASE_SERVICE_ROLE_KEY` | Dein Supabase Service Role Key |
| `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` | Stripe Publishable Key (Test-Key vorerst) |
| `STRIPE_SECRET_KEY` | Stripe Secret Key (Test-Key vorerst) |
| `STRIPE_WEBHOOK_SECRET` | Stripe Webhook Secret (nach Webhook-Setup) |

#### Nur für **Preview**-Environment (Pull Request Deployments)

| Variable | Wert |
|---|---|
| `SUPABASE_DB_SCHEMA` | `schufacleaner-test` |
| `NEXT_PUBLIC_SUPABASE_DB_SCHEMA` | `schufacleaner-test` |

#### Nur für **Production**-Environment

| Variable | Wert |
|---|---|
| `SUPABASE_DB_SCHEMA` | `schufacleaner-prod` |
| `NEXT_PUBLIC_SUPABASE_DB_SCHEMA` | `schufacleaner-prod` |

> ⚠️ **Hinweis:** `NEXT_PUBLIC_SUPABASE_DB_SCHEMA` muss auch mit `NEXT_PUBLIC_` gesetzt werden,  
> da der Browser-Client (Client-Components) keinen Zugriff auf Server-only Env-Variablen hat.

---

### Schritt 2.4 — Vercel Project ID notieren

1. Gehe zu: **Vercel Projekt → Settings → General**
2. Kopiere die **Project ID** (Format: `prj_...`)
3. Du brauchst sie für GitHub Secrets (Teil 3)

---

### Schritt 2.5 — Erstes Deployment starten

1. Gehe zu: **Deployments → Redeploy** (oder pushe einen neuen Commit auf `main`)
2. Vercel baut und deployed die App
3. Prüfe die Deployment-Logs auf Fehler

---

## Teil 3 — GitHub Secrets setzen

Navigiere zu: **GitHub → Repository `schufacleaner` → Settings → Secrets and variables → Actions**

### Secrets auf Repository-Ebene

| Secret Name | Wert | Pflicht |
|---|---|---|
| `VERCEL_PROJECT_ID` | Aus Schritt 2.4 | ✅ Ja |

### Secrets auf Organisations-Ebene (Wamocon)

> Diese Secrets sind bereits auf Org-Ebene gesetzt. Kein Handlungsbedarf,  
> sofern sie in der Wamocon-Organisation vorhanden sind.

| Secret Name | Beschreibung |
|---|---|
| `VERCEL_TOKEN` | Persönlicher Vercel Access Token |
| `VERCEL_ORG_ID` | Vercel Organisation / Account ID |

---

## Teil 4 — Lokale `.env.local` einrichten

```bash
# Im Projekt-Root ausführen:
cp .env.example .env.local
```

Dann `.env.local` mit den echten Werten aus Supabase und Stripe befüllen:

```env
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_SITE_NAME=SchufaCleaner

NEXT_PUBLIC_SUPABASE_URL=https://DEIN-PROJECT-REF.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=DEIN-ANON-KEY
SUPABASE_SERVICE_ROLE_KEY=DEIN-SERVICE-ROLE-KEY

# Lokale Entwicklung → dev-Schema
SUPABASE_DB_SCHEMA=schufacleaner-dev
NEXT_PUBLIC_SUPABASE_DB_SCHEMA=schufacleaner-dev

STRIPE_SECRET_KEY=sk_test_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

Dann den Dev-Server starten:

```bash
npm run dev
```

---

## Checkliste — Alles erledigt?

- [ ] Supabase-Projekt ist **Active**
- [ ] SQL aus Schritt 1.1 – 1.3 ausgeführt (alle 3 Schemas mit GRANT-Rechten)
- [ ] Schemas in **Project Settings → API → Extra search path** eingetragen (Schritt 1.4)
- [ ] Supabase Auth aktiviert, Site URL und Redirect URLs gesetzt (Schritt 1.5)
- [ ] Vercel GitHub App hat Zugriff auf `schufacleaner` (Schritt 2.1)
- [ ] Vercel-Projekt importiert (Schritt 2.2)
- [ ] Alle Umgebungsvariablen in Vercel gesetzt — Preview + Production getrennt (Schritt 2.3)
- [ ] `VERCEL_PROJECT_ID` in GitHub Secrets eingetragen (Schritt 3)
- [ ] `.env.local` lokal befüllt (Teil 4)
- [ ] `npm run dev` startet ohne Fehler
- [ ] Erstes Vercel-Deployment erfolgreich

---

## Häufige Fehler und Lösungen

| Fehler | Ursache | Lösung |
|---|---|---|
| `400 Bad Request` bei Supabase-Anfragen | Schema nicht in "Exposed schemas" | Schritt 1.4 wiederholen |
| `No schema match` | Falscher Schema-Name in Env-Variable | `SUPABASE_DB_SCHEMA` prüfen – muss exakt `schufacleaner-dev/test/prod` lauten |
| Vercel Deploy schlägt fehl: `VERCEL_PROJECT_ID not found` | Secret fehlt in GitHub | Schritt 3 ausführen |
| Auth-Redirect funktioniert nicht lokal | Site URL falsch | Supabase → Auth → Redirect URLs: `http://localhost:3000/**` hinzufügen |
| Tabellen-Fehler nach Schema-Wechsel | GRANT fehlt | SQL aus Schritt 1.1–1.3 erneut ausführen |

---

*WAMOCON GmbH — Mergenthalerallee 79–81, 65760 Eschborn — info@wamocon.com*

## ./anforderungen/Welle_9_Anforderungsdokument_schufaCleaner_final.md
**Anforderungsdokument**

SchufaCleaner -- Softwareprojekt

  ---------------------- -------------------------------------------------
  **Welle:**             9

  **Projekt:**           SchufaCleaner

  **Unternehmen:**       WAMOCON GmbH

  **App Version:**       1

  **Erstellt von:**      Nikolaj Schefner

  **Eingereicht an:**    Waleri Moretz (Geschäftsführung)

  **Datum:**             05.05.2026

  **Vertraulichkeit:**   Intern vertraulich

  **Status:**            Zur Freigabe eingereicht
  ---------------------- -------------------------------------------------

# **1. Zusammenfassung**

## **1.1 Die Idee**

Viele Schufa-Einträge in Deutschland sind veraltet oder fehlerhaft. Das
blockiert Handyverträge, Kredite oder Wohnungen. Doch das rechtssichere
Löschen dieser Einträge ist für Laien extrem schwer.

**SchufaCleaner** ist eine reine Web-App, die dieses Problem einfach
löst:

-   Nutzer bestellen sich ihre kostenlose Schufa-Datenkopie nach Art. 15
    DSGVO[^1] und laden sie als PDF hoch.

-   Die KI[^2] analysiert das Dokument, hebt rechtlich angreifbare
    Fehler hervor und generiert mit einem Klick ein passendes,
    Widerspruchsschreiben.

In einfachen Worten:

-   Die App nimmt das unübersichtliche Schufa-PDF, findet sofort die
    Fehler und schreibt den perfekten Lösch-Brief für den Nutzer.

## **1.2 Warum jetzt?**

Rechtssicherheit war beim Thema Bonität bisher immer an unglaublich
teure Anwälte gekoppelt. Durch präzises PDF-Parsing und moderne KI ist
es nun möglich, diese Detailprüfung zu demokratisieren und kostengünstig
als Web-Modell anzubieten.

# **2. Marktanalyse**

## **2.1 Einordnung: Schufa-Datenbestand in Deutschland**

Die folgenden Kennzahlen geben den statistischen Kontext. Sie sind keine
direkte Aussage über die Anzahl potenzieller Kunden, weil einer Person
mehrere Einträge gehören können.

  ------------------------------------------------------------------------
  **Kontextkennzahl**      **Wert**        **Quelle**
  ------------------------ --------------- -------------------------------
  Schufa-Datensätze        ca. 1 Milliarde Schufa Holding AG,
  (Einträge gesamt)                        Jahresbericht 2024

  Davon erfasste           ca. 69          Schufa Holding AG,
  natürliche Personen      Millionen       Jahresbericht 2024

  Fehlerhafte oder         ca. 20 bis 30 % Verbraucherzentrale
  veraltete Datensätze                     Bundesverband e.V., 2024

  Jährlich angeforderte    \> 3 Millionen  Schufa Holding AG,
  kostenlose Datenkopien                   Jahresbericht 2024
  ------------------------------------------------------------------------

*Quelle: Schufa Holding AG, Jahresbericht 2024; Verbraucherzentrale
Bundesverband e.V., 2024*

## **2.2 Fokus: Personen mit Schufa-Einträgen, die echte Zielgruppe**

Die entscheidende Frage für die App ist nicht, wie viele Einträge es
gibt, sondern wie viele Personen betroffen sind.

  ------------------------------------------------------------------------
  **Zielgruppe in Zahlen** **Wert**         **Quelle**
  ------------------------ ---------------- ------------------------------
  Personen mit allgemeinen ca. 69 Millionen Schufa Holding AG,
  Schufa-Einträgen         (= fast alle     Jahresbericht 2024
                           Erwachsenen in   
                           DE)              

  Anteil Personen mit      ca. 91,7 %       Schufa Holding AG,
  ausschließlich positiven                  Jahresbericht 2024
  Daten                                     

  Personen mit mindestens  ca. 5,7 bis 8    Schufa Holding AG,
  einem negativen Eintrag  Millionen        Jahresbericht 2024

  **Personen mit           **ca. 1,1 bis    **Verbraucherzentrale
  fehlerhaftem negativem   2,4 Millionen**  Bundesverband, 2024**
  Eintrag (potenzielle                      
  Kunden)**                                 

  Durchschnittliche        500 bis 1.000 €  Bundesrechtsanwaltskammer,
  Anwaltskosten für eine                    Statistik 2025
  Löschung                                  
  ------------------------------------------------------------------------

Der adressierbare Markt sind die ca. 5,7 bis 8 Millionen Personen mit
negativen Einträgen. Von diesen ist ein erheblicher Anteil fehlerhaft
oder veraltet und damit anfechtbar. Jede dieser Personen ist ein
potenzieller Kunde, unabhängig davon, wie viele einzelne Datensätze ihr
in der Schufa-Datenbank zugeordnet sind.

*Quelle: Schufa Holding AG, Jahresbericht 2024; Verbraucherzentrale
Bundesverband e.V., 2024; Bundesrechtsanwaltskammer, 2025*

## **2.3 Problem und Lösung**

[Das Problem:]{.underline}

-   Wenn Verbraucher ihre Datenkopie anfordern, stoßen sie auf
    kryptische Codes und unübersichtliche Tabellen.

-   Finden sie einen Fehler, wissen sie nicht, auf welche Paragrafen des
    BDSG[^3] (Bundesdatenschutzgesetz) sie sich berufen müssen.

-   Ein formloser Beschwerdebrief wird von Auskunfteien oft aus formalen
    Gründen ignoriert, weil er nicht rechtssicher formuliert ist.

[Die Lösung:]{.underline}

-   Die Web-App strukturiert das Datenchaos, wendet aktuelle Gesetze an
    und gibt dem Verbraucher ein fertig formuliertes Dokument in die
    Hand, das formaljuristisch korrekt ist.

[Wichtiger Hinweis:]{.underline}

-   Alle KI-generierten Schreiben und Empfehlungen der App ersetzen
    keine echte Rechtsberatung durch einen zugelassenen Anwalt.

-   Jede Ausgabe enthält einen entsprechenden Pflicht-Disclaimer.

*Quelle: Schufa Holding AG, Jahresbericht 2024; Verbraucherzentrale
Bundesverband e.V., 2024*

# 

# **3. Wettbewerb**

Zusatzprodukte wie Bonify sind Finanzvertriebs-Apps und keine
Konkurrenz, da ihr Interesse nicht primär im aktiven, konfrontativen
Löschen von Daten liegt. Der echte, realistische Wettbewerb teilt sich
in manuelle Vorlagen und juristische Profis auf:

  ------------------------------------------------------------------------------------------------
  **Anbieter**         **Typ**          **Rechtssicher   **Preisniveau**   **Wettbewerbsstärke**
                                        helfen**                           
  -------------------- ---------------- ---------------- ----------------- -----------------------
  Kanzleien für        Echte            Ja               Sehr hoch (\> 500 Stark -- bieten
  Verbraucherrecht     Rechtsberatung                    €)                Sicherheit, aber nur
                                                                           für kaufkräftige
                                                                           Zielgruppe

  Musterbrief-Seiten   Do-It-Yourself   Nein (zu         Kostenlos         Schwach -- Nutzer muss
                                        generisch)                         Paragrafen selbst
                                                                           prüfen

  MeineSchufa-Portal   Info-Portal      Nein             0 -- 5 € / Monat  Mittel -- kein
                                                                           Interesse an geführten
                                                                           Widersprüchen
  ------------------------------------------------------------------------------------------------

[Fazit:]{.underline}

-   **SchufaCleaner** füllt die gewaltige Lücke zwischen unsicheren
    Musterbriefen aus dem Internet und Anwälten, die ein halbes
    Monatsgehalt kosten.

# **4. Zielgruppe**

  ---------------------------------------------------------------------------
  **Zielgruppe**     **Profil**             **Warum relevant? / Nicht
                                            relevant?**
  ------------------ ---------------------- ---------------------------------
  Wohnungs- &        Digital affine         Größter Schmerz wegen
  Kreditsuchende     Privatpersonen, 20 bis Wohnungsmangel. Der
  (Primär)           45 Jahre, in aktiver   Schufa-Scanner löst die Blockade
                     Umbruchphase.          sofort. Sehr hohe
                                            Zahlungsbereitschaft.

  Selbstständige     Freiberufler oder      Ihr privater Score entspricht oft
  (Sekundär)         Solo-Selbstständige.   der geschäftlichen Bonität und
                                            muss sauber sein.

  Nicht-Zielgruppe   Personen, die völlig   Wer echte, berechtigte und neue
                     zu Recht Schulden      Schulden hat (z.B. frisch nicht
                     haben.                 bezahlter Kredit), kann diese
                                            nicht wegzaubern. Die Web-App
                                            wird hier explizit nicht
                                            weiterhelfen.
  ---------------------------------------------------------------------------

*Quelle: Eigene Zielgruppenanalyse Wohnungsmarkt 2025.*

# **5. Nutzen**

Der Verbraucher spart sich die wochenlange Terminabstimmung mit Anwälten
und extrem hohe Gebühren. Was vorher 500 bis 1.000 Euro und viel
Vorwissen gekostet hat, geht nun über die Web-App vollautomatisiert.
Nach dem Hochladen der Schufa-Datenkopie führt das Tool den Laien direkt
zu einem rechtssicheren PDF.

[Hinweis:]{.underline}

-   Schufa-Cleaner ist ein Assistenzwerkzeug und ersetzt keine echte
    Rechtsberatung durch einen zugelassenen Anwalt. Alle generierten
    Schreiben sind Mustervorlagen. Jede KI-Ausgabe trägt einen nicht
    abschaltbaren Pflicht-Disclaimer.

# **6. Abhängigkeiten und Herausforderungen**

+-------------------------+--------------------------------------------+
| **Herausforderung**     | **Lösung**                                 |
+=========================+============================================+
| Veraltete Gesetzgebung. | Automatischer                              |
|                         | Regelwerk-Update-Mechanismus:              |
| Wenn die App auf        |                                            |
| gesetzlichen Fristen    | -   Die KI durchsucht quartalsweise (und   |
| basiert, die sich       |     bei bekannten Gesetzesänderungen       |
| geändert haben, werden  |     anlassbezogen) das Bundesgesetzblatt,  |
| falsche Widersprüche    |     BGH-Urteilsdatenbanken und den         |
| generiert.              |     Schufa-Verhaltenskodex nach            |
|                         |     Änderungen.                            |
|                         |                                            |
|                         | -   Alle gefundenen Änderungen werden als  |
|                         |     Protokolleintrag mit Datum, Quelle und |
|                         |     geändertem Parameter gespeichert.      |
|                         |                                            |
|                         | -   WAMOCON prüft und genehmigt den Update |
|                         |     im Admin-Bereich, bevor er produktiv   |
|                         |     geht.                                  |
|                         |                                            |
|                         | -   Jedes Update ist damit revisionssicher |
|                         |     dokumentiert.                          |
+-------------------------+--------------------------------------------+
| Pflicht-Disclaimer bei  | Anforderung SC-03 verankert den Disclaimer |
| jeder KI-Ausgabe.       | als nicht abschaltbares Pflichtfeld. Er    |
|                         | erscheint direkt unter jeder KI-Ausgabe    |
| Jede KI-generierte      | und auf dem generierten PDF.               |
| Empfehlung oder jedes   |                                            |
| erzeugte Schreiben muss |                                            |
| sichtbar und            |                                            |
| unmissverständlich als  |                                            |
| Nicht-Rechtsberatung    |                                            |
| gekennzeichnet sein.    |                                            |
+-------------------------+--------------------------------------------+
| Abhängigkeit von        | Keine API-Abhängigkeiten zu Banken oder    |
| Drittsystemen.          | Auskunfteien notwendig. Der Nutzer lädt    |
|                         | sein PDF selbst hoch. Das eliminiert das   |
|                         | größte Integrationsrisiko vollständig.     |
+-------------------------+--------------------------------------------+

# **7. Businessmodell**

Die reine Web-App wird über ein Abonnement-System finanziert:

-   [Free Plan (0,00 €):]{.underline}

    -   Der Scan-Teaser.

    -   Der Nutzer lädt sein PDF hoch.

    -   Die KI zeigt maximal 3 anfechtbare Fehler detailliert an.

    -   Alle weiteren Fehler werden maskiert und nur als Sammelzahl
        ausgewiesen (z.B. \"Wir haben noch 3 weitere anfechtbare Fehler
        gefunden\"), es werden aber keine Namen oder Details dieser
        restlichen Fehler geliefert.

-   [Pro Plan (4,99 € / Monat):]{.underline}

    -   Entschleiert alle Fehler ohne Limit.

    -   Erlaubt unbegrenztes Generieren von rechtssicheren
        Widerspruchs-PDFs.

    -   Das Abo passt ideal zur Dauer von Schufa-Klärungen, die sich oft
        über 1 bis 3 Monate ziehen.

# **8. Anforderungen Version 1**

### **8.1 Basisprozesse**

  -------------------------------------------------------------------------------
  **ID**   **Anforderung**                                        **Priorität**
  -------- ------------------------------------------------------ ---------------
  B-01     Bereitstellung als responsive Web-App (keine           Muss
           App-Store-Installation nötig).                         

  B-02     Landing Page, Registrierung, AGB, Datenschutzerklärung Muss
           mit Cookie-Banner.                                     

  B-03     Aufbau des Regelwerk-Mechanismus: Ein von WAMOCON      Muss
           pflegbares Modul, in dem DSGVO-/BDSG-Fristen und       
           Löschregeln für die KI verwaltet werden.               
  -------------------------------------------------------------------------------

### 

### 

### 

### **8.2 Hauptprozesse (Analyse und Fallbearbeitung)**

  -------------------------------------------------------------------------------
  **ID**   **Anforderung**                                        **Priorität**
  -------- ------------------------------------------------------ ---------------
  SC-01    Upload-Prozess speziell für das Format: Kostenlose     Muss
           Schufa-Datenkopie (Art. 15 DSGVO) im PDF-Format.       

  SC-02    KI-Parser gleicht die Daten des PDFs gegen das         Muss
           aktuelle Regelwerk ab.                                 

  SC-03    Disclaimer-Zwang: Bei JEDER KI-Antwort und Empfehlung  Muss
           muss der Zusatz stehen: \"Dieses Dokument ersetzt      
           keine echte Rechtsberatung durch einen Anwalt!\"       
  -------------------------------------------------------------------------------

### **8.3 Business Modell**

  -------------------------------------------------------------------------------
  **ID**   **Anforderung**                                        **Priorität**
  -------- ------------------------------------------------------ ---------------
  BM-01    Free-Plan-Limitierung: Bei 0 € Plan dürfen maximal 5   Muss
           analysierte Fehler im Detail angezeigt werden.         
           Überhängende Fehler werden auf die reine Anzahl        
           summierend reduziert.                                  

  BM-02    Pro-Plan-Checkout: Stripe-Integration für das 4,99 €   Muss
           Monats-Abo mit Self-Service-Kündigungsfunktion.        
           Schaltet PDF-Generator frei.                           
  -------------------------------------------------------------------------------

# **9. Chancen und Risiken**

## **9.1 Chancen**

  -----------------------------------------------------------------------
  **Chance**               **Begründung**
  ------------------------ ----------------------------------------------
  Großer adressierbarer    Bis zu 8 Millionen Personen mit negativen
  Markt                    Einträgen in Deutschland sind direkte
                           Zielkunden, ohne Marketingumwege.

  Kein Download-Widerstand Die Web-App braucht keine Installation. Der
                           Nutzer ist nach der Registrierung in unter 2
                           Minuten aktiv.

  Klarer Preisanker        Anwaltskosten von 500 bis 1.000 € machen das
                           4,99-€-Abo zum absoluten No-Brainer für
                           Betroffene.

  Virales Wachstum         Eine gelungene Datenlöschung, die z.B. eine
                           Wohnungszusage ermöglicht, führt zu starken
                           Empfehlungen im Freundeskreis.

  Erweiterbarkeit          V2 kann problemlos auf weitere Auskunfteien
                           (Creditreform, Arvato Infoscore) ausgeweitet
                           werden.

  Geringer Marginaldruck   Die KI skaliert kostenlos mit wachsender
                           Nutzerzahl. Jeder zusätzliche Pro-Abonnent
                           erhöht direkt die Marge ohne proportionale
                           Mehrkosten.
  -----------------------------------------------------------------------

## **9.2 Risiken**

  --------------------------------------------------------------------------------------------------------
  **Risiko**           **Eintrittswahrscheinlichkeit**   **Auswirkung**   **Gegenmaßnahme**
  -------------------- --------------------------------- ---------------- --------------------------------
  Abmahnung            Mittel                            Hoch             Jede einzelne KI-Antwort und
  (Unerlaubte                                                             jede geführte Empfehlung
  Rechtsberatung)                                                         erhalten einen klaren, visuell
                                                                          hervorgehobenen Disclaimer, dass
                                                                          hier nur Mustertexte generiert
                                                                          werden und dies keine echte
                                                                          Rechtsberatung durch einen
                                                                          zugelassenen Anwalt ersetzt. Die
                                                                          Nutzer entscheiden selbst, ob
                                                                          sie das Dokument versenden.

  Inkorrekte           Gering                            Mittel           Regelmäßige Pflege des
  Fristen-Berechnung                                                      Regelwerk-Moduls (Anforderung
                                                                          B-03) nach Gesetzesupdates.
  --------------------------------------------------------------------------------------------------------

# **10. Umsetzungsplan**

GitHub Copilot Premium übernimmt den generativen Teil der Programmierung
der Web-App. Der Entwickler reviewt, korrigiert und testet.

  ------------------------------------------------------------------------------
  **Werktag**   **Entwicklungsfokus**   **Geplantes Ergebnis**
  ------------- ----------------------- ----------------------------------------
  Tag 1 (Mo)    Basis & Infrastruktur   Initiales Set-up der Web-App,
                                        Auth-Anbindung und Routing-Logik.

  Tag 2 (Di)    Regelwerk-Mechanismus   Setup der Datenbank zur Pflege von
                                        Gesetzes- und Fristenparametern.

  Tag 3 (Mi)    PDF-Parsing &           Upload-Maske für Schufa-Datenkopie und
                Algorithmus             Logik zur Erkennung veralteter Einträge.

  Tag 4 (Do)    Business Modell (Free / Stripe-Anbindung (4,99 € Abo) sowie
                Pro)                    Limitierungs-Logik (max. 5 offene Mängel
                                        im Free Plan).

  Tag 5 (Fr)    PDF-Generator &         Widerspruchs-PDF-Export und Fixierung
                Rechtliches             aller Rechts-Disclaimer an KI-Antworten.

  Tag 6 (Sa) -- QA (Quality Assurance)  Intensives Testen mit Dummy-Schufadaten,
  Puffer                                Überprüfung Responsive Design, Go-Live.
  ------------------------------------------------------------------------------

# **Quellenverzeichnis**

  -------------------------------------------------------------------------
  **Quelle**                   **Inhalt**
  ---------------------------- --------------------------------------------
  Schufa Holding AG,           Anzahl erfasster Personen, Anteil positiver
  Jahresbericht 2024           Datensätze, Negativmerkmal-Statistik.

  Verbraucherzentrale          Schätzung fehlerhafte / veraltete
  Bundesverband e.V., 2024     Datensätze.

  Bundesrechtsanwaltskammer,   Durchschnittliche Anwaltskosten für
  Statistik 2025               datenschutzrechtliche Widerspruchsverfahren.

  DSGVO (Verordnung EU         Auskunftsrecht über personenbezogene Daten
  2016/679), Art. 15           -- Grundlage für die kostenlose Datenkopie.

  BDSG 2024                    Bundesdatenschutzgesetz -- Regelungen zu
                               Scoring und Löschpflichten in Deutschland.
  -------------------------------------------------------------------------

[^1]: DSGVO: Europäische Datenschutz-Grundverordnung.

[^2]: KI (Künstliche Intelligenz): Maschinelle Analyseverfahren zur
    Textauswertung der PDF.

[^3]: BDSG: Bundesdatenschutzgesetz, regelt u.a. Scoring und
    Löschpflichten in Deutschland.

## ./legal-docs/agb.md
# Allgemeine Geschäftsbedingungen (AGB)

Stand: {{MONAT}} {{JAHR}}

## § 1 Geltungsbereich

(1) Diese Allgemeinen Geschäftsbedingungen (nachfolgend „AGB") der WAMOCON GmbH, Mergenthalerallee 79 - 81, 65760 Eschborn (nachfolgend „Anbieter"), gelten für alle Verträge über die Nutzung der Software-as-a-Service-Plattform {{PROJEKTNAME}} (nachfolgend „Plattform"), die über die Website {{DOMAIN}} bereitgestellt wird.

(2) Die Plattform richtet sich an Unternehmen und gewerbliche Nutzer (nachfolgend „Auftraggeber") sowie deren Benutzer (nachfolgend „Nutzer"). Es handelt sich um ein B2B-Angebot. Verbraucher im Sinne des § 13 BGB sind nicht Zielgruppe dieses Angebots.

(3) Abweichende, entgegenstehende oder ergänzende AGB des Auftraggebers werden nicht Vertragsbestandteil, es sei denn, der Anbieter stimmt deren Geltung ausdrücklich schriftlich zu.

## § 2 Vertragsschluss

(1) Die Darstellung der Plattform und ihrer Funktionen auf der Website stellt kein verbindliches Angebot im Sinne des § 145 BGB dar, sondern eine Aufforderung zur Abgabe eines Angebots (invitatio ad offerendum).

(2) Der Auftraggeber gibt ein verbindliches Angebot zum Abschluss eines Nutzungsvertrages ab, indem er den Registrierungsprozess auf der Plattform abschließt und diese AGB akzeptiert.

(3) Der Vertrag kommt zustande, wenn der Anbieter das Angebot des Auftraggebers durch Freischaltung des Zugangs annimmt.

## § 3 Leistungsbeschreibung

(1) Der Anbieter stellt dem Auftraggeber die Plattform als Software-as-a-Service (SaaS) über das Internet zur Verfügung.

(2) Der genaue Funktionsumfang ergibt sich aus der jeweils aktuellen Leistungsbeschreibung auf der Website.

(3) Der Anbieter ist berechtigt, die Plattform weiterzuentwickeln, zu erweitern und anzupassen. Wesentliche Einschränkungen des Funktionsumfangs werden dem Auftraggeber vorab mitgeteilt.

## § 4 Nutzungsrechte

(1) Der Anbieter räumt dem Auftraggeber für die Vertragslaufzeit ein einfaches, nicht übertragbares, nicht unterlizenzierbares Recht zur Nutzung der Plattform ein.

(2) Der Auftraggeber darf die Plattform nur für eigene betriebliche Zwecke nutzen.

## § 5 Pflichten des Auftraggebers

(1) Der Auftraggeber ist verpflichtet, seine Zugangsdaten geheim zu halten und vor dem Zugriff Dritter zu schützen.

(2) Der Auftraggeber stellt sicher, dass die Nutzung der Plattform im Einklang mit geltendem Recht erfolgt.

## § 6 Verfügbarkeit

(1) Der Anbieter bemüht sich um eine Verfügbarkeit der Plattform von 99,5 % im Jahresmittel.

(2) Nicht als Ausfallzeit gelten geplante Wartungsarbeiten, die vorab angekündigt werden.

## § 7 Datenschutz

Die Verarbeitung personenbezogener Daten erfolgt gemäß der Datenschutzerklärung des Anbieters und den Bestimmungen der DSGVO.

## § 8 Haftung

(1) Der Anbieter haftet unbeschränkt für Schäden aus der Verletzung des Lebens, des Körpers oder der Gesundheit sowie bei Vorsatz und grober Fahrlässigkeit.

(2) Im Übrigen ist die Haftung auf den vertragstypischen, vorhersehbaren Schaden begrenzt.

## § 9 Vertragslaufzeit und Kündigung

(1) Der Vertrag wird auf unbestimmte Zeit geschlossen und kann von beiden Parteien mit einer Frist von einem Monat zum Monatsende gekündigt werden.

(2) Das Recht zur außerordentlichen Kündigung aus wichtigem Grund bleibt unberührt.

## § 10 Schlussbestimmungen

(1) Es gilt das Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts.

(2) Gerichtsstand ist Eschborn, sofern der Auftraggeber Kaufmann ist.

(3) Sollten einzelne Bestimmungen dieser AGB unwirksam sein, bleibt die Wirksamkeit der übrigen Bestimmungen davon unberührt.

---

> **Hinweis:** Dies ist ein Muster. Ersetze alle `{{PLATZHALTER}}` mit den projektspezifischen Informationen. Lass die AGB vor Veröffentlichung von einem Juristen prüfen.

## ./legal-docs/company-stamp.md
# Firmenstempel / Company Stamp

## Deutsch

### WAMOCON GmbH

**Geschäftsführer:** Dipl.-Ing. Waleri Moretz

**Anschrift:**
Mergenthalerallee 79 - 81
65760 Eschborn
Deutschland

**Kontakt:**
Telefon: +49 6196 5838311
E-Mail: info@wamocon.com

**Registrierung:**
Handelsregister: Eschborn HRB 123666
USt-IdNr.: DE344930486

---

## English

### WAMOCON GmbH

**Managing Director:** Dipl.-Ing. Waleri Moretz

**Address:**
Mergenthalerallee 79 - 81
65760 Eschborn
Germany

**Contact:**
Phone: +49 6196 5838311
Email: info@wamocon.com

**Registration:**
Commercial Register: Eschborn HRB 123666
VAT ID: DE344930486

## ./legal-docs/datenschutzerklaerung.md
# Datenschutzerklärung

Stand: {{MONAT}} {{JAHR}}

## 1. Verantwortlicher

Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) und anderer nationaler Datenschutzgesetze ist:

WAMOCON GmbH
Mergenthalerallee 79 - 81
65760 Eschborn
Telefon: +49 6196 5838311
E-Mail: info@wamocon.com
Projektkontakt: {{PROJEKT_EMAIL}}
Geschäftsführer: Dipl.-Ing. Waleri Moretz
Handelsregister: Eschborn HRB 123666
USt-ID: DE344930486

## 2. Überblick über die Datenverarbeitung

Diese Datenschutzerklärung gilt für die Website und Webanwendung {{PROJEKTNAME}} ({{DOMAIN}}).

Wir verarbeiten personenbezogene Daten unserer Nutzer grundsätzlich nur, soweit dies zur Bereitstellung einer funktionsfähigen Plattform sowie unserer Inhalte und Leistungen erforderlich ist.

## 3. Rechtsgrundlagen der Verarbeitung

- **Einwilligung** – Art. 6 Abs. 1 lit. a DSGVO
- **Vertragserfüllung** – Art. 6 Abs. 1 lit. b DSGVO
- **Rechtliche Verpflichtung** – Art. 6 Abs. 1 lit. c DSGVO
- **Berechtigtes Interesse** – Art. 6 Abs. 1 lit. f DSGVO

## 4. Hosting und Infrastruktur

### Vercel Inc.
Die Website und Webanwendung werden über Vercel gehostet. Dabei verarbeitet Vercel technisch notwendige Verbindungsdaten (IP-Adresse, Zeitstempel, Browserinformationen). Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.

### Supabase Inc.
Für Datenbank, Authentifizierung, Dateispeicher und Teile der Backend-Infrastruktur nutzen wir Supabase. Verarbeitet werden Authentifizierungsdaten, Session-Informationen, Projektdaten sowie gespeicherte Medien. Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO.

## 5. Erhebung personenbezogener Daten

### Registrierung und Nutzerkonto
Bei der Registrierung erheben wir: Name, E-Mail-Adresse und Passwort. Diese Daten sind zur Vertragserfüllung erforderlich (Art. 6 Abs. 1 lit. b DSGVO).

### Server-Logfiles
Bei jedem Zugriff auf unsere Plattform werden automatisch folgende Daten erfasst: IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Referrer-URL, Browser-Typ und -Version. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.

## 6. Cookies und Tracking

Die Plattform verwendet technisch notwendige Cookies für Session-Management und Authentifizierung. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.

## 7. Rechte der betroffenen Personen

Sie haben das Recht auf:
- **Auskunft** (Art. 15 DSGVO)
- **Berichtigung** (Art. 16 DSGVO)
- **Löschung** (Art. 17 DSGVO)
- **Einschränkung der Verarbeitung** (Art. 18 DSGVO)
- **Datenübertragbarkeit** (Art. 20 DSGVO)
- **Widerspruch** (Art. 21 DSGVO)
- **Widerruf** erteilter Einwilligungen (Art. 7 Abs. 3 DSGVO)
- **Beschwerde** bei einer Aufsichtsbehörde (Art. 77 DSGVO)

## 8. Datensicherheit

Wir setzen technische und organisatorische Sicherheitsmaßnahmen nach dem Stand der Technik ein, um Ihre Daten gegen zufällige oder vorsätzliche Manipulation, Verlust, Zerstörung oder den Zugriff unberechtigter Personen zu schützen.

## 9. Änderung der Datenschutzerklärung

Wir behalten uns vor, diese Datenschutzerklärung anzupassen, um sie an geänderte Rechtslagen oder bei Änderungen der Plattform anzupassen.

---

> **Hinweis:** Dies ist ein Muster. Ersetze alle `{{PLATZHALTER}}` mit den projektspezifischen Informationen. Lass die Datenschutzerklärung vor Veröffentlichung von einem Juristen prüfen.

## ./legal-docs/impressum.md
# Impressum

Stand: {{MONAT}} {{JAHR}}

## WAMOCON GmbH

Mergenthalerallee 79 - 81
65760 Eschborn
Deutschland

## Kontakt

Telefon: +49 6196 5838311
E-Mail: info@wamocon.com
Projektkontakt: {{PROJEKT_EMAIL}}

## Vertretungsberechtigter Geschäftsführer

Dipl.-Ing. Waleri Moretz

## Registereintrag

Sitz der Gesellschaft: Eschborn
Handelsregister: Eschborn HRB 123666
Umsatzsteuer-Identifikationsnummer: DE344930486

## Angaben zum Angebot

{{PROJEKTNAME}} ist eine webbasierte Software-as-a-Service-Plattform für {{BESCHREIBUNG_DES_ANGEBOTS}}. Das Angebot richtet sich primär an Unternehmen und gewerbliche Nutzer.

---

> **Hinweis:** Ersetze alle `{{PLATZHALTER}}` mit den projektspezifischen Informationen.

## ./legal-docs/imprint.md
# Imprint (Legal Notice)

As of: {{MONTH}} {{YEAR}}

## WAMOCON GmbH

Mergenthalerallee 79 - 81
65760 Eschborn
Germany

## Contact

Phone: +49 6196 5838311
Email: info@wamocon.com
Project Contact: {{PROJECT_EMAIL}}

## Authorized Managing Director

Dipl.-Ing. Waleri Moretz

## Registration

Registered Office: Eschborn
Commercial Register: Eschborn HRB 123666
VAT Identification Number: DE344930486

## About the Service

{{PROJECT_NAME}} is a web-based Software-as-a-Service platform for {{SERVICE_DESCRIPTION}}. The service is primarily aimed at businesses and commercial users.

---

> **Note:** Replace all `{{PLACEHOLDERS}}` with your project-specific information.

## ./legal-docs/privacy-policy.md
# Privacy Policy

As of: {{MONTH}} {{YEAR}}

## 1. Data Controller

The Data Controller as defined by the General Data Protection Regulation (GDPR) is:

WAMOCON GmbH
Mergenthalerallee 79 - 81
65760 Eschborn, Germany
Phone: +49 6196 5838311
Email: info@wamocon.com
Project Contact: {{PROJECT_EMAIL}}
Managing Director: Dipl.-Ing. Waleri Moretz
Commercial Register: Eschborn HRB 123666
VAT ID: DE344930486

## 2. Overview of Data Processing

This Privacy Policy applies to the website and web application {{PROJECT_NAME}} ({{DOMAIN}}).

We process personal data of our users only insofar as this is necessary to provide a functional platform and our content and services.

## 3. Legal Basis for Processing

- **Consent** – Art. 6(1)(a) GDPR
- **Performance of Contract** – Art. 6(1)(b) GDPR
- **Legal Obligation** – Art. 6(1)(c) GDPR
- **Legitimate Interest** – Art. 6(1)(f) GDPR

## 4. Hosting and Infrastructure

### Vercel Inc.
The website and web application are hosted via Vercel. Vercel processes technically necessary connection data (IP address, timestamp, browser information). Legal basis: Art. 6(1)(f) GDPR.

### Supabase Inc.
We use Supabase for database, authentication, file storage, and parts of the backend infrastructure. Authentication data, session information, project data, and stored media are processed. Legal basis: Art. 6(1)(b) GDPR.

## 5. Collection of Personal Data

### Registration and User Account
During registration we collect: name, email address, and password. This data is necessary for the performance of the contract (Art. 6(1)(b) GDPR).

### Server Log Files
Each access to our platform automatically records: IP address, date and time, page accessed, referrer URL, browser type and version. Legal basis: Art. 6(1)(f) GDPR.

## 6. Cookies and Tracking

The platform uses technically necessary cookies for session management and authentication. Legal basis: Art. 6(1)(f) GDPR.

## 7. Rights of Data Subjects

You have the right to:
- **Access** (Art. 15 GDPR)
- **Rectification** (Art. 16 GDPR)
- **Erasure** (Art. 17 GDPR)
- **Restriction of processing** (Art. 18 GDPR)
- **Data portability** (Art. 20 GDPR)
- **Object** (Art. 21 GDPR)
- **Withdraw consent** (Art. 7(3) GDPR)
- **Lodge a complaint** with a supervisory authority (Art. 77 GDPR)

## 8. Data Security

We employ state-of-the-art technical and organisational security measures to protect your data against accidental or intentional manipulation, loss, destruction, or access by unauthorised persons.

## 9. Changes to this Privacy Policy

We reserve the right to amend this Privacy Policy to reflect changes in the law or changes to the platform.

---

> **Note:** This is a template. Replace all `{{PLACEHOLDERS}}` with your project-specific information. Have the Privacy Policy reviewed by a lawyer before publication.

## ./legal-docs/terms-and-conditions.md
# Terms and Conditions

As of: {{MONTH}} {{YEAR}}

## § 1 Scope

(1) These Terms and Conditions (hereinafter "T&C") of WAMOCON GmbH, Mergenthalerallee 79 - 81, 65760 Eschborn (hereinafter "Provider"), apply to all contracts for the use of the Software-as-a-Service platform {{PROJECT_NAME}} (hereinafter "Platform"), provided via the website {{DOMAIN}}.

(2) The Platform is aimed at businesses and commercial users (hereinafter "Client") and their respective users (hereinafter "Users"). This is a B2B offering. Consumers within the meaning of § 13 BGB (German Civil Code) are not the target audience.

(3) Deviating, conflicting, or supplementary terms and conditions of the Client shall not become part of the contract unless the Provider expressly agrees in writing.

## § 2 Conclusion of Contract

(1) The presentation of the Platform and its features on the website does not constitute a binding offer within the meaning of § 145 BGB, but rather an invitation to submit an offer (invitatio ad offerendum).

(2) The Client submits a binding offer by completing the registration process on the Platform and accepting these T&C.

(3) The contract is concluded when the Provider accepts the Client's offer by activating access.

## § 3 Service Description

(1) The Provider makes the Platform available to the Client as Software-as-a-Service (SaaS) via the Internet.

(2) The precise scope of features is set out in the current service description on the website.

(3) The Provider is entitled to further develop, expand, and adapt the Platform. Material restrictions to the scope of features will be communicated to the Client in advance.

## § 4 Usage Rights

(1) The Provider grants the Client a simple, non-transferable, non-sublicensable right to use the Platform for the duration of the contract.

(2) The Client may only use the Platform for its own business purposes.

## § 5 Client Obligations

(1) The Client shall keep its access credentials confidential and protect them from third-party access.

(2) The Client shall ensure that use of the Platform complies with applicable law.

## § 6 Availability

(1) The Provider shall endeavour to maintain an annual average availability of 99.5%.

(2) Scheduled maintenance windows announced in advance shall not count as downtime.

## § 7 Data Protection

The processing of personal data is governed by the Provider's Privacy Policy and the provisions of the GDPR.

## § 8 Liability

(1) The Provider shall be fully liable for damages arising from injury to life, body, or health, as well as for intent and gross negligence.

(2) Otherwise, liability is limited to foreseeable, typically occurring damages.

## § 9 Contract Duration and Termination

(1) The contract is concluded for an indefinite period and may be terminated by either party with one month's notice to the end of a calendar month.

(2) The right to extraordinary termination for good cause remains unaffected.

## § 10 Final Provisions

(1) The law of the Federal Republic of Germany shall apply, excluding the UN Convention on Contracts for the International Sale of Goods.

(2) The place of jurisdiction is Eschborn, provided the Client is a merchant.

(3) Should individual provisions of these T&C be invalid, the validity of the remaining provisions shall remain unaffected.

---

> **Note:** This is a template. Replace all `{{PLACEHOLDERS}}` with your project-specific information. Have the T&C reviewed by a lawyer before publication.

## package.json
{
  "name": "schufacleaner",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "verify": "npm run typecheck && npm run lint && npm run build",
    "gen:anforderungsdokument": "node scripts/generate-anforderungsdokument.mjs"
  },
  "dependencies": {
    "@supabase/ssr": "^0.10.2",
    "@supabase/supabase-js": "^2.105.3",
    "docx": "^9.6.1",
    "lucide-react": "^1.14.0",
    "next": "16.2.1",
    "next-intl": "^4.11.0",
    "openai": "^6.36.0",
    "pdf-parse": "^2.4.5",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "stripe": "^22.1.0",
    "zod": "^4.4.3"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.2",
    "@testing-library/user-event": "^14.6.1",
    "@types/node": "^20",
    "@types/pdf-parse": "^1.1.5",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@vitejs/plugin-react": "^6.0.1",
    "@vitest/coverage-v8": "^4.1.5",
    "eslint": "^9",
    "eslint-config-next": "16.2.1",
    "jsdom": "^29.1.1",
    "tailwindcss": "^4",
    "typescript": "^5",
    "vitest": "^4.1.5"
  }
}

