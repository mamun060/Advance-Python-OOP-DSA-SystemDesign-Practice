# Interview Question Bank (with Model Answers)
### ISP Billing & CRM Platform — Frontend & Backend Engineer Roles

Organized by architectural layer: **Client (Frontend) → Service (Backend) → Data (Database)**
Each question includes a model answer — use it as a benchmark, not a script. A candidate doesn't need to say it word-for-word; they need to demonstrate the same underlying understanding. Push with "why" / "what if" follow-ups regardless of how polished the first answer sounds.

---

## 🖥️ 1. CLIENT LAYER (Frontend Role)

### A. React / Next.js Fundamentals

**1. Explain SSR, SSG, ISR, and CSR. When would you use each for a billing page vs. an admin dashboard?**
- SSR: page rendered on the server per request — good for pages needing fresh, user-specific data (e.g., "my current invoice").
- SSG: rendered once at build time — good for static content (marketing pages, help docs).
- ISR: static but regenerated in the background on a timer/revalidation — good for content that changes but not on every request (e.g., a public "service plans" page).
- CSR: rendered in the browser — good for highly interactive, auth-gated dashboards where SEO doesn't matter.
- For a billing page: SSR or CSR (needs fresh, per-user data). For an internal admin dashboard: CSR is usually fine since it's behind auth and SEO is irrelevant.

**2. App Router vs Pages Router — why the move to Server Components?**
- App Router supports layouts, nested routing, streaming, and React Server Components natively; Pages Router doesn't.
- Server Components let you fetch data and render on the server without shipping that logic/JS to the client — smaller bundles, faster initial load, safer (secrets/DB calls never reach the browser).

**3. What are Server Components, and what can't you do inside one?**
- Server Components render on the server and send HTML (not JS) to the client. No `useState`, `useEffect`, event handlers, or browser-only APIs — those require a Client Component (`"use client"`).
- In a billing dashboard: fetching and displaying invoice data → Server Component. A filter dropdown or a "mark as paid" button → Client Component.

**4. Walk through what happens when a user hits `/invoice/[id]`.**
- Next.js matches the route → runs the Server Component (and any `generateMetadata`) → fetches data (DB/API call) → renders HTML on the server → streams HTML + minimal JS to the browser → client hydrates interactive parts (Client Components) → page becomes interactive.

**5. Purpose of Next.js middleware — RBAC example.**
- Middleware runs before a request completes, at the edge — used for redirects, header rewriting, and auth checks before the page even renders.
- RBAC example: middleware reads the auth token/session, checks the user's role, and redirects to `/unauthorized` or `/login` if they lack access to `/admin/billing`, before the page loads.

**6. Route handlers vs traditional API routes — when to build one vs. calling the backend directly?**
- Route handlers are the App Router's way of building API endpoints (`route.ts`) — same concept as old `pages/api`, but with more control over Request/Response.
- Use a route handler when you need a thin proxy/BFF layer (e.g., combining/transforming data from multiple backend services, hiding API keys). Call the Django/FastAPI backend directly when the frontend can consume it as-is.

### B. State Management

**7. RTK, RTK Query, vs TanStack Query — when to use which, and can you justify not using all three?**
- Redux Toolkit: client-only/UI state (modals, filters, multi-step form state) not tied to server data.
- RTK Query: server state, when you're already using Redux and want caching/data-fetching integrated into the same store.
- TanStack Query: server state, framework-agnostic, often preferred if the app isn't otherwise Redux-heavy.
- A strong candidate should say: **you generally don't need both RTK Query and TanStack Query in the same app** — they solve the same problem (server-state caching). Picking both without reason is a red flag; a good reason would be legacy migration or team preference in different modules.

**8. RTK Query caching/invalidation — how would you invalidate subscriber data after a payment webhook?**
- RTK Query uses `tags` — each query provides tags, mutations invalidate tags, triggering automatic refetch.
- Since a webhook happens outside the frontend, the frontend needs to learn about it — via a socket event that triggers a manual `dispatch(api.util.invalidateTags(['Subscriber']))`, or simple polling/refetch-on-focus as a fallback.

**9. Optimistic updates for a manual payment entry, with rollback on failure.**
- Immediately update the UI/cache assuming success (e.g., show balance reduced) before the server confirms, using `onQueryStarted` in RTK Query or `onMutate` in TanStack Query.
- Store the previous state; if the request fails, roll back to it and show an error toast. Candidate should mention this needs care for money — some teams intentionally avoid optimistic UI for payment amounts and prefer a pending/spinner state instead.

**10. Avoiding prop-drilling / re-renders in a large permission-gated dashboard.**
- Use context or Redux selectors for permissions rather than passing props down many levels.
- Memoize components (`React.memo`), use selector hooks that only subscribe to the specific slice of state needed, and split large components so unrelated state changes don't re-render the whole tree.

### C. Real-Time & Integration

**11. Architecting a socket for live subscriber session status — reconnection and stale state.**
- Establish socket connection on dashboard mount, subscribe to relevant subscriber/session channels, update local state (Redux/Zustand/local) on incoming events.
- Handle reconnection with exponential backoff; on reconnect, re-sync state via a REST fetch (don't trust that you didn't miss events while disconnected) rather than assuming the socket stream was continuous.

**12. WebSocket vs polling vs webhook-driven UI — when is polling the right choice?**
- Polling is simpler, doesn't need persistent connections, and is the right choice when update frequency is low, near-real-time isn't critical, or infrastructure (e.g., load balancers) makes long-lived sockets painful. Good candidates recognize polling isn't "worse," just a different trade-off (simplicity/cost vs. latency).

**13. How does the frontend consume a webhook that lands on the backend?**
- The frontend never receives the webhook directly — the backend receives it, processes it, and then needs to notify the frontend via a socket push, Server-Sent Events, or the frontend polls/refetches. A candidate who says "the frontend listens for the webhook" doesn't understand the architecture — this is a good filtering question.

**14. Consuming gRPC from Next.js — limitations.**
- Browsers can't speak raw gRPC (HTTP/2 trailers aren't accessible) — need grpc-web + a proxy (e.g., Envoy) or a REST/gRPC gateway that translates. Many teams instead expose REST publicly and use gRPC only for internal service-to-service calls, which the frontend never touches directly.

### D. RBAC / Permissions

**15. Permission-aware UI — hide vs. disable vs. block route. Trade-offs?**
- Hide: cleanest UX, but user might not understand why a feature is "missing."
- Disable (greyed out): communicates the feature exists but isn't accessible — usually best for discoverability.
- Route-block: necessary for direct URL access, independent of what's rendered in nav/buttons.
- Best practice: combine — hide/disable in UI for polish, but always enforce at the route/middleware level too.

**16. Why can't frontend-only permission checks be trusted?**
- Frontend code is fully visible/modifiable by the client (browser devtools, direct API calls). Real enforcement must happen server-side on every request; frontend checks are UX convenience only.

**17. Structuring permissions in frontend state for multi-role users with overlapping/conflicting permissions.**
- Normalize permissions into a flat set/object at login (e.g., merge all roles' permissions into one effective permission list) rather than checking "does user have role X" scattered everywhere. Store as a single source of truth in Redux/Context; components check against that flattened set. For conflicts, define an explicit precedence rule (e.g., explicit deny wins over allow).

### E. Performance / Practical

**18. Diagnosing poor Core Web Vitals on a large-table admin dashboard.**
- Check LCP (is a large table rendering synchronously?), check for large unoptimized JS bundles (code-split, lazy-load), check for layout shift from late-loading data, use React DevTools Profiler for re-render issues, ensure images are optimized (`next/image`).

**19. Pagination/virtualization for a 10k+ row subscriber table.**
- Server-side pagination (don't fetch all rows) combined with client-side virtualization (e.g., `react-window`/`react-virtual`) so only visible rows are in the DOM at once.

**20. Live task: build a component showing live connection status via socket, falling back to polling if disconnected.**
- Look for: `useEffect` socket setup/teardown, connection state tracking, a fallback `setInterval` REST poll that activates only when the socket is down, and cleanup on unmount to avoid leaks. Care about correctness (no duplicate polling + socket updates at once) matters more than syntax perfection.

---

## ⚙️ 2. SERVICE LAYER (Backend Role)

### A. Python / Django / FastAPI Fundamentals

**1. Django request-response lifecycle and where middleware fits.**
- Request → URL routing → middleware (in order, e.g., auth, CSRF, session) → view → (middleware again, in reverse, on the way out) → response. Middleware is the hook point for cross-cutting concerns like auth checks, logging, or RBAC enforcement.

**2. FastAPI vs Django — when to introduce FastAPI alongside an existing Django monolith?**
- FastAPI shines for high-throughput, async-heavy, or lightweight services (e.g., a webhook receiver, a real-time telemetry ingestion service) where Django's overhead isn't needed. Good answer acknowledges the cost of running two frameworks (shared auth, duplicated models) and that it should be a deliberate choice, not default.

**3. `select_related` vs `prefetch_related` — billing example.**
- `select_related`: SQL JOIN, for single-valued relations (ForeignKey/OneToOne) — e.g., invoice → subscriber.
- `prefetch_related`: separate query + Python-side join, for multi-valued relations (ManyToMany/reverse FK) — e.g., invoice → payments (multiple partial payments).
- Using `select_related` on a reverse FK, or `prefetch_related` on a single FK, causes either an error or N+1 queries / wasted overhead.

**4. Structuring Django apps for bounded contexts (Billing, Subscriber, Partner/Commission).**
- Each bounded context as its own Django app with its own models, serializers, services — minimal cross-app model imports; communicate via well-defined service functions or events rather than reaching directly into another app's models/tables.

### B. Async, Queues & Event-Driven Architecture

**5. How Celery works, and what happens if a worker crashes mid-task.**
- Producer (Django) pushes a task message to the broker (RabbitMQ/Redis) → a worker picks it up → executes → writes result to a result backend (optional).
- If a worker crashes mid-task: depends on ack settings. With late acknowledgment (`task_acks_late=True`), the message isn't acked until the task finishes, so a crash means the message gets redelivered to another worker — but this requires the task to be idempotent, or it'll run twice.

**6. RabbitMQ vs Redis as a Celery broker.**
- RabbitMQ: proper message queue, supports complex routing, acknowledgments, durability — better for reliability-critical flows (payments).
- Redis: simpler, faster for low-latency/low-durability needs, but weaker delivery guarantees. For payment/activation pipelines, RabbitMQ is the safer choice; Redis is fine for caching or less-critical background jobs.

**7. Outbox pattern — implementing it for a bKash payment confirmation.**
- Instead of writing the payment record AND publishing an event as two separate operations (risking one succeeding without the other), write the payment record and an "outbox" event row in the same DB transaction. A separate poller/relay process reads unpublished outbox rows and publishes them to RabbitMQ, then marks them published — guaranteeing the event is eventually published if and only if the DB write succeeded.

**8. Ensuring idempotency for duplicate payment gateway webhooks.**
- Enforce a unique DB constraint on the gateway's transaction ID. When a webhook arrives, attempt to insert/process using that ID — if it already exists, treat it as a no-op/already-processed rather than double-crediting the subscriber.

**9. Design: payment succeeds but activation fails — how do you avoid a broken state?**
- Use a task chain (Celery chain) or saga: payment confirmed → publish event → activation worker consumes it → on failure, retry with backoff → after max retries, move to a dead-letter queue and alert ops, while the subscriber's status stays "payment received, activation pending" (never silently lost). Avoid marking the subscriber active until RADIUS confirms.

**10. At-least-once vs exactly-once delivery.**
- Most brokers guarantee at-least-once (messages may be redelivered) — true exactly-once is very hard/costly. The practical solution is designing consumers to be idempotent (via unique constraints, dedup checks) so at-least-once delivery behaves like exactly-once in effect.

### C. API Design

**11. REST vs gRPC — when to choose gRPC internally?**
- gRPC: efficient binary protocol (protobuf), strong typing, good for high-throughput internal service-to-service calls (e.g., billing service ↔ RADIUS service). Downsides: harder to debug/inspect, no native browser support, added tooling complexity. REST: better for public/partner-facing APIs and anything the frontend calls directly.

**12. Versioning a REST API without breaking existing consumers.**
- URL versioning (`/api/v1/`, `/api/v2/`) or header-based versioning; maintain backward compatibility for a deprecation window, communicate breaking changes ahead of time, avoid changing response shapes in place.

**13. API contract between billing and partner/commission services.**
- Billing publishes a `payment.confirmed` (or similar) event with subscriber ID, amount, timestamp; commission service subscribes and calculates commission independently, rather than billing directly calling into commission service synchronously — keeps the services loosely coupled and lets commission service replay/recalculate from history if needed.

**14. Designing webhook endpoints for bKash/Nagad — authenticity and replay protection.**
- Verify signatures/checksums provided by the gateway (or do a server-side "Query" call back to the gateway to confirm the transaction rather than trusting the payload). Use HTTPS only, validate source IPs where possible, and use the unique transaction ID + idempotency check to prevent replay from being processed twice.

### D. Security & Auth

**15. Implementing RBAC at the API layer with scoped permissions, not just role strings.**
- Model permissions as (action, resource) pairs, not just role names — e.g., `billing.invoice.view`, `billing.invoice.refund`. Check specific permissions in each view/endpoint via a decorator or permission class, rather than `if role == "admin"` scattered through the code.

**16. Securely storing/rotating payment gateway credentials.**
- Use a secrets manager (not `.env` committed to git) — environment variables injected at deploy time, or a vault service. Rotate keys periodically, use separate credentials per environment (sandbox vs. production), and never log full credentials.

**17. Preventing SQL injection, IDOR, CSRF on webhooks.**
- SQL injection: use ORM/parameterized queries, never raw string-formatted SQL.
- IDOR: always check that the requesting user owns/has permission for the specific resource ID, not just that they're authenticated.
- CSRF on webhooks: webhook endpoints should be exempt from Django's CSRF (since there's no browser session) but instead protected by signature verification — this is a good "gotcha" question to see if the candidate understands CSRF only applies to browser-based session auth.

**18. Verifying a webhook is really from bKash/Nagad with no logged-in user.**
- Signature/HMAC verification using a shared secret, IP allowlisting if the gateway publishes static IPs, and/or a server-initiated verification call (query the transaction status directly from the gateway's API) rather than trusting the webhook payload alone — this is the strongest guarantee.

### E. Infrastructure / Deployment

**19. Docker setup for Django + Celery + Redis + RabbitMQ.**
- Separate containers: Django/gunicorn (web), Celery worker(s), Celery beat (if scheduled tasks), Redis, RabbitMQ, and often nginx in front — orchestrated via `docker-compose` (dev) or similar in production. Services communicate over an internal Docker network by service name.

**20. CI/CD pipeline for a Django service.**
- On push/PR: run linting + automated tests → build Docker image → (on merge to main) push image to registry → run migrations → deploy with a strategy that avoids downtime (rolling deploy, or blue-green) → smoke test / health check post-deploy.

**21. Zero-downtime migrations for a live billing system.**
- Use backward-compatible migrations (add nullable columns first, backfill, then enforce constraints in a later migration) so the old code can still run against the new schema during rollout. Avoid long-locking migrations on large tables during peak hours; consider tools like `django-migration-linter` or manual review for risky migrations.

**22. Debugging: payments succeed at gateway but don't reflect in-system for ~5% of transactions.**
- Check webhook delivery logs (gateway side) for failures/timeouts, check for silent exceptions in the webhook handler, check if the idempotency check is incorrectly rejecting valid new transactions, check Celery task failures/dead-letter queue, and reconcile against the gateway's transaction list (Query API) to find the gap directly rather than guessing.

---

## 🗄️ 3. DATA LAYER (Both Roles — Backend-Weighted)

### A. Schema & Modeling

**1. Modeling subscriber → invoice → payment for partial payments.**
- `Invoice` (amount_due, status) → has many `Payment` rows (amount, method, gateway_txn_id, timestamp). Invoice status derived from sum(payments) vs amount_due, or maintained via a trigger/service logic — never assume one invoice = one payment.

**2. Self-referencing partner hierarchy with a commission-pool constraint.**
- `Partner` table with a nullable `parent_id` FK to itself. The constraint ("child's pool ≤ parent's pool") is best enforced at the application/service layer during writes (since it requires comparing against a related row, which plain CHECK constraints can't easily do across rows) — though a DB-level trigger is also valid for stricter guarantees. Good candidates should recognize this needs either app-level validation in a transaction, or a trigger — a plain column CHECK constraint alone can't do it.

**3. MySQL vs PostgreSQL for a billing system.**
- PostgreSQL generally favored for billing: stronger transactional integrity guarantees, better support for complex queries, JSONB support, and better handling of concurrent writes at scale. MySQL is a fine choice too and widely used in production billing systems — the candidate should be able to argue either way with real trade-offs, not just preference.

**4. Where would a time-series DB actually help?**
- Bandwidth/usage logs, OLT/network telemetry (e.g., signal strength over time), session duration metrics — high-volume, timestamp-indexed data where you mostly query "value over a time range." Regular PostgreSQL can work at moderate scale, but a time-series DB (e.g., TimescaleDB) offers better compression and time-bucketed query performance at high volume.

### B. Transactions & Integrity

**5. ACID with a billing example.**
- If "deduct balance" and "create payment record" aren't atomic (in one transaction), a crash between the two steps could deduct money without recording the payment, or record a payment without deducting balance — leading to a subscriber being charged twice or the company losing revenue.

**6. Isolation level for concurrent payments on the same account.**
- At least `READ COMMITTED` is Postgres's default; for critical balance updates, you often want row-level locking (`SELECT ... FOR UPDATE`) or `SERIALIZABLE` isolation to prevent a race where two concurrent payments both read the same starting balance and one overwrites the other's update (lost update problem).

**7. Preventing double-processing when multiple workers might pick up the same event.**
- Unique constraint on the gateway transaction ID (as in Q8 above) is the primary defense; additionally, use a distributed lock (e.g., Redis lock) or database-level `SELECT FOR UPDATE` on the subscriber row during processing to prevent concurrent workers from processing conflicting updates simultaneously.

### C. Performance

**8. Indexing for filtering invoices by subscriber, date range, status at ~1M subscriber scale.**
- A composite index on `(subscriber_id, status, created_at)` (order matters — most selective/most-queried-together columns first) rather than separate single-column indexes, which Postgres/MySQL can't combine as efficiently for multi-column filters.

**9. Optimizing a slow "revenue by partner this month" report query.**
- Check the query plan (`EXPLAIN ANALYZE`), ensure proper indexes exist, consider a materialized view or a pre-aggregated summary table updated incrementally (rather than aggregating raw transactional data on every dashboard load) if this report is queried frequently.

**10. Archiving/partitioning old billing data.**
- Table partitioning by date range (e.g., yearly/monthly partitions) so old partitions can be archived or excluded from hot-path queries; move very old data to a cheaper archive store while keeping recent data in the primary fast-access tables. Reporting on historical data can query archive tables separately or via a union view.

### D. Consistency Across Services

**11. Eventual consistency between billing and commission services.**
- Commission service subscribes to payment events and recalculates asynchronously — there's a small window where billing reflects a payment before commission is updated. This is an acceptable trade-off if the UI clearly shows "processing" state, and the system guarantees eventual convergence (not indefinite staleness).

**12. Commission service down for an hour when `invoice.paid` fires — how do you ensure correctness once it's back?**
- The message broker (RabbitMQ) holds/retries the message until a consumer acks it — as long as commission service comes back up and resumes consuming, it processes the backlog. This relies on the broker retaining unacked messages and the consumer being idempotent in case of any redelivery.

---

## 🧭 How to Use This in the Interview

- **Junior/mid (2–3 yrs):** Focus on Section A/B fundamentals in each layer + 1 live coding/design task.
- **Senior (4–5 yrs):** Weight toward C/D/E — architecture, trade-offs, failure scenarios. Push on "what breaks in production" questions.
- **Strong signal:** Candidate asks clarifying questions before answering design questions (e.g., "what's the expected transaction volume?"), and pushes back on parts of the model answer where reasonable (e.g., arguing MySQL over Postgres with valid reasons).
- **Red flag:** Candidate can name technologies (RabbitMQ, RBAC, gRPC) but can't explain a concrete failure mode or trade-off for any of them, or gives an answer that contradicts itself under a follow-up "what if" question.
