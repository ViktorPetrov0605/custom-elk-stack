# Search Instructions for SearXNG Tool

## Core Search Strategy

When researching a topic, use an **iterative, multi-query approach** with self-evaluation. Don't settle for the first search.

---

## Phase 1: Query Design (Multi-Query Strategy)

Break complex queries into **2-5 targeted searches**:

| Type | Example | Purpose |
|------|---------|---------|
| **Broad** | `docker compose tutorial best practices` | General overview |
| **Specific** | `docker compose healthcheck restart policy` | Deep dive |
| **Official** | `site:docs.docker.com compose file reference` | Authoritative source |
| **Recent** | `docker compose new features 2025` | Latest updates |
| **Troubleshooting** | `docker compose "container exit code 1" debug` | Problem-solving |

---

## Phase 2: SearXNG Search Operators

### Engine/Category Modifiers (SearXNG-specific)
- `!wp <query>` — Search Wikipedia only
- `!ddg <query>` — Search DuckDuckGo only
- `!images <query>` — Image search
- `!videos <query>` — Video search
- `!news <query>` — News search
- `!map paris` — Maps
- `!it <query>` — IT/tech category
- `!science <query>` — Science papers
- **Chainable**: `!map !ddg !wp paris` (searches maps + DDG + Wikipedia)

### Language Filter
- `:fr !wp <query>` — French Wikipedia
- `:de <query>` — German results
- `:en <query>` — English results (default)

### External Bangs (Direct external search)
- `!!wfr <query>` — DuckDuckGo bang to Wikipedia FR
- `!!a <query>` — Amazon search
- `!!yt <query>` — YouTube search
- ⚠️ **Warning**: Bypasses SearXNG privacy protection

### Automatic Redirect (I'm Feeling Lucky)
- `!! <query>` — Redirects to first result
- ⚠️ **Use sparingly** — skips trust verification

---

## Phase 3: Standard Search Operators (Passed to Engines)

| Operator | Example | Effect |
|----------|---------|--------|
| `"phrase"` | `"machine learning" tutorial` | Exact phrase match |
| `site:` | `site:github.com docker compose` | Restrict to domain |
| `filetype:` | `filetype:pdf kubernetes guide` | Specific file type |
| `-term` | `python -snake` | Exclude term |
| `OR` | `docker OR podman tutorial` | Either term |
| `*` wildcard | `docker * compose` | Wildcard match |
| `intitle:` | `intitle:docker compose` | Title contains |
| `inurl:` | `inurl:github docker` | URL contains |
| `after:2024` | `docker updates after:2024` | After date |
| `before:2023` | `docker history before:2023` | Before date |

---

## Phase 4: Self-Iteration & Source Evaluation

After each search, **evaluate results against user intent**:

### Relevance Scoring (1-5 scale)
```
5 = Perfect match — exactly what user asked
4 = Strong match — covers main topic well
3 = Related — useful context but off-target
2 = Weak — tangential relevance
1 = Miss — unrelated or wrong topic
```

### Quality Indicators
| Positive Signals | Negative Signals |
|------------------|------------------|
| ✅ Official documentation | ❌ SEO spam farms |
| ✅ Recent date (< 1 year for tech) | ❌ Outdated (3+ years old) |
| ✅ Author credentials visible | ❌ No author/source |
| ✅ References/citations | ❌ Unsupported claims |
| ✅ Technical depth | ❌ Surface-level fluff |
| ✅ Known domain (.edu, .gov, major orgs) | ❌ Clickbait domains |

### Iteration Rules
1. **If top 3 results all score < 4**: Refine query with operators
2. **If mixed quality**: Note best sources, search for more like them
3. **If official docs missing**: Add `site:` operator for authoritative sources
4. **If outdated info**: Add date filters (`after:2024`)
5. **If too broad**: Add exclusion terms (`-beginner -tutorial`)

---

## Phase 5: Result Synthesis

### Output Format
```
## Search Summary
- Queries run: N
- Best sources: (list top 3 with scores)
- Gaps found: (what's still missing)

## Key Findings
(Bullet points from evaluated sources)

## Sources
1. [Title](URL) — Score: 5/5 — Official docs, current
2. [Title](URL) — Score: 4/5 — Good tutorial, 2024
...
```

---

## Example Full Workflow

**User asks**: "How do I set up Docker Compose healthchecks properly?"

### Query 1: Broad
`docker compose healthcheck tutorial`
- Results: Mostly basic, score 2-3
- Finding: Need official reference

### Query 2: Official  
`site:docs.docker.com compose healthcheck`
- Results: Strong match, score 5
- Finding: Good base docs

### Query 3: Best Practices  
`"docker compose" healthcheck best practices "depends_on" OR "condition"`
- Results: Real-world examples, score 4
- Finding: Covers advanced patterns

### Query 4: Recent Issues  
`docker compose healthcheck "not working" after:2024`
- Results: Troubleshooting tips, score 3
- Finding: Common pitfalls identified

### Synthesis
- Combined knowledge from 4 sources
- Official docs (5/5) + community examples (4/5) + troubleshooting (3/5)
- Deliver comprehensive answer with citations

---

## Quick Reference Cheatsheet

```bash
# Multiple targeted searches
node searxng_local.js "broad topic" --limit 10
node searxng_local.js "specific aspect" --limit 10
node searxng_local.js "site:official.docs.com topic" --limit 10

# Engine-specific
node searxng_local.js "!wp topic" --limit 5      # Wikipedia
node searxng_local.js "!it topic" --limit 10     # Tech category

# With operators in the query string itself:
node searxng_local.js '"exact phrase" site:domain.com -exclude filetype:pdf'
```

---

## Remember

1. **One query rarely suffices** — use 2-5 variations
2. **Operators are your friend** — they filter noise
3. **Score every source** — don't present junk
4. **Iterate when weak** — refine and search again
5. **Cite the best** — user deserves quality sources
