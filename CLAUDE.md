# Algo Sensei — Claude Code Instructions

## Auto-Save Rule (IMPORTANT)

At the end of every conversation where DSA practice occurred:
- Automatically update `progress/progress.md` with the session data
- Do NOT wait for the user to ask — do it proactively before the session ends
- If the user hasn't explicitly ended the session, update the file whenever you're about to give a final response

## Session Start Rule

If the user shares `progress/progress.md` at the start of a session:
- Read it immediately and generate a personalized session brief
- Check what's due for review in the Review Queue
- Recommend focus areas based on weak patterns

## Skill Location

This skill is installed at `~/.claude/skills/algo-sensei/`
Progress file: `progress/progress.md` (relative to wherever the user copied it)
