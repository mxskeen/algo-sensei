# Algo Sensei — Claude Code Instructions

## Auto-Save Rule (IMPORTANT)

At the end of every conversation where any learning/practice occurred:
- Automatically update `progress/progress.md` with the session data
- This includes: DSA practice, CUDA kernel work, systems programming, GenAI study, interview prep — anything
- Do NOT wait for the user to ask — do it proactively before the session ends
- If the user hasn't explicitly ended the session, update the file whenever you're about to give a final response

## What to log per session
- Date and duration (approximate)
- Topics covered (DSA patterns, CUDA concepts, C++/Rust/Go topics, etc.)
- Problems attempted and outcome
- Concepts that clicked vs concepts that need more work
- Any kernels written, bugs fixed, papers read
- Review queue updates (what to revisit next session)

## Session Start Rule

If the user shares `progress/progress.md` at the start of a session:
- Read it immediately and generate a personalized session brief
- For DSA: check what's due for review in the Review Queue, recommend weak patterns
- For GPU/systems: check where they left off in the 100-day challenge or learning path
- Recommend focus areas based on previous session notes

## Skill Location

This skill is installed at `~/.claude/skills/algo-sensei/`
Progress file: `progress/progress.md` (relative to wherever the user copied it)
