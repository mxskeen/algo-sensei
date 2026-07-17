# Algo Sensei — Claude Code Instructions

## Auto-Save Rule (IMPORTANT — mandatory, do not merely offer)

At the end of every conversation where any learning/practice occurred:
- Automatically update `progress/progress.md` AND `docs/pattern-notes.md` — do NOT wait for the user to ask, and do NOT merely offer.
- This includes: DSA practice, CUDA kernel work, systems programming, GenAI study, interview prep — anything.
- If the user hasn't explicitly ended the session, update the files whenever you're about to give a final response.
- Always persist SM-2 state: after grading a review, run `python scripts/sm2.py review --item "<name>" --q <0-5>` and paste the printed row into the **SM-2 Review Queue** table of `progress/progress.md`. The authoritative state lives in `progress/sm2_state.json`.
- Always refresh **Curriculum Coverage** counts (patterns mastered, problems solved).

## What to log per session
- Date and duration (approximate)
- Topics covered (DSA patterns, CUDA concepts, C++/Rust/Go topics, etc.)
- Problems attempted and outcome
- Concepts that clicked vs concepts that need more work
- Any kernels written, bugs fixed, papers read
- Review queue updates (SM-2 state for what to revisit next session)

## Session Start Rule

If the user shares `progress/progress.md` at the start of a session:
- Read it (and `docs/pattern-notes.md`) immediately and generate a personalized session brief.
- For DSA: check what's due for review in the SM-2 Review Queue (`python scripts/sm2.py due`), recommend weak patterns.
- For GPU/systems: check where they left off in the 100-day challenge or learning path.
- Recommend focus areas based on previous session notes.

## Memory / Single Source of Truth

Algo Sensei's value is cumulative — it must remember the user across sessions. Treat these files as the single source of truth and keep them current:

- `progress/progress.md` — Profile, Pattern Confidence Map (the 26 patterns from `docs/problem-bank.md`), Curriculum Coverage, Problems Solved, **SM-2 Review Queue** (real SuperMemo-2 state), Session Log, Stats.
- `progress/sm2_state.json` — the machine-readable SM-2 engine state (managed by `scripts/sm2.py`). One source of truth for scheduling.
- `docs/pattern-notes.md` — the user's personal pattern encyclopedia, appended after every solved problem.

Rules:
- Load these files at session start; personalize every response from them.
- Write them at session end (including SM-2 state rows and coverage counts). Just save and say "📝 Progress saved." — no need to ask.
- If any file is missing, create it from the template before ending the session.

## Skill Location

This skill is installed at `~/.claude/skills/algo-sensei/`
Progress file: `progress/progress.md` (relative to wherever the user copied it)
