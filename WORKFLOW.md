# Workflow Orchestration & Task Management

## 1. Plan Mode (Default)
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions).
- If something goes sideways, **STOP and re-plan immediately** — don't keep pushing.
- Use plan mode for verification steps, not just building.
- Write detailed specs upfront to reduce ambiguity.

## 2. Subagent Strategy
- Use subagents liberally to keep main context window clean.
- Offload research, exploration, and parallel analysis to subagents.
- For complex problems, throw more compute at it via subagents.
- One task per subagent for focused execution.

## 3. Self-Improvement Loop
- After ANY correction from the user: update memory files with the pattern.
- Write rules that prevent the same mistake.
- Ruthlessly iterate on these lessons until mistake rate drops.
- Review lessons at session start for relevant projects.
- **Limit Repetition:** Do not repeat the same command more than three times without success. Investigate progress blockers instead.

## 4. Verification Before Done
- Never mark a task complete without proving it works.
- Diff behavior between main and changes when relevant.
- Ask: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness.

## 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution."
- Skip for simple/obvious fixes — don't over-engineer.
- Challenge your own work before presenting it.

## 6. Autonomous Bug Fixing
- Fix bug reports immediately without hand-holding.
- Point at logs, errors, or failing tests — then resolve them.
- Ensure zero context switching is required from the user.
- Fix failing CI tests autonomously.

# Task Management Workflow
1. **Plan First:** Write plan to `tasks/todo.md` with checkable items.
2. **Verify Plan:** Check in before starting implementation.
3. **Track Progress:** Mark items complete as you go.
4. **Explain Changes:** Provide high-level summaries at each step.
5. **Document Results:** Add a review section to `tasks/todo.md`.
6. **Capture Lessons:** Update `tasks/lessons.md` after corrections.

# Core Principles
- **Simplicity First:** Impact minimal code; keep changes as simple as possible.
- **No Laziness:** Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact:** Touch only what's necessary to avoid introducing regressions.
