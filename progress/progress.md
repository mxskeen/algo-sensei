# Algo Sensei Progress Tracker 📊

> This file is maintained by Algo Sensei. At the start of each session, share it for personalized guidance.
> At the end of every session Algo Sensei updates it automatically — no need to ask.
> This is the single source of truth for your progress. Your personal pattern notes live in `docs/pattern-notes.md`.

---

## Profile

**Started:** 2026-07-17
**Primary Focus Stack:** [fill in — e.g. Python / Java / C++]  *(set this so hints match your language)*
**Goal:** Interview-ready DSA — rely solely on Algo Sensei. Cover the full pattern sheet end-to-end and retain it with real SM-2 spaced repetition.
**Self-assessed Level:** [Beginner / Intermediate / Advanced — fill in]
**Interview target date:** [fill in if you have one]

---

## Pattern Confidence Map

Rate: 🔴 Weak | 🟡 Learning | 🟢 Solid | ⭐ Mastered
Names match `docs/problem-bank.md` exactly (the sheet).

| Pattern | Confidence | Last Practiced | Notes |
|---------|------------|----------------|-------|
| Two Pointers | 🔴 Weak | - | - |
| Fast & Slow Pointers | 🔴 Weak | - | - |
| Sliding Window | 🔴 Weak | - | - |
| Kadane's Algorithm | 🔴 Weak | - | - |
| Prefix Sum | 🔴 Weak | - | - |
| Merge Intervals | 🔴 Weak | - | - |
| Cyclic Sort | 🔴 Weak | - | - |
| In-place Reversal of LinkedList | 🔴 Weak | - | - |
| Stack / Monotonic Stack | 🔴 Weak | - | - |
| Hash Maps | 🔴 Weak | - | - |
| Binary Search | 🔴 Weak | - | - |
| Graph BFS | 🔴 Weak | - | - |
| Island / Matrix Traversal | 🔴 Weak | - | - |
| Two Heaps | 🔴 Weak | - | - |
| Subsets / Backtracking | 🔴 Weak | - | - |
| Top K Elements (Heap) | 🔴 Weak | - | - |
| Greedy | 🔴 Weak | - | - |
| Dynamic Programming (0/1 Knapsack) | 🔴 Weak | - | - |
| Trie | 🔴 Weak | - | - |
| Topological Sort | 🔴 Weak | - | - |
| Union Find | 🔴 Weak | - | - |
| Ordered Set | 🔴 Weak | - | - |
| Bitwise XOR | 🔴 Weak | - | - |
| Binary Trees & BST | 🔴 Weak | - | - |
| Dynamic Programming (1-D / Fibonacci) | 🔴 Weak | - | - |
| Dynamic Programming (2-D / String) | 🔴 Weak | - | - |
| Advanced Graphs | 🔴 Weak | - | - |

---

## Curriculum Coverage

Full pattern sheet = `docs/problem-bank.md` (27 patterns, 170+ problems, easy→hard, LeetCode/GFG links).

- **Patterns:** 0 / 27 mastered (⭐)
- **Problems solved:** 0 / ~170  *(see Problems Solved below)*
- **Plan:** clear every pattern ⭐ before your interview. Daily Problem Mode walks the sheet in order: weakest untouched pattern → its Easy problem → Medium → Hard.

---

## Problems Solved

| # | Problem | Difficulty | Pattern | Solved Independently | Date | Notes |
|---|---------|------------|---------|----------------------|------|-------|

---

## SM-2 Review Queue

Real SuperMemo-2 state for every item scheduled for review — this is the spaced-repetition engine (the basis for Anki). The authoritative state lives in `progress/sm2_state.json`, managed by `scripts/sm2.py`. After each review, grade recall quality `q ∈ 0–5` and run:

```bash
python scripts/sm2.py review --item "<name>" --q <0-5>
```

Then paste the printed row below (or run `python scripts/sm2.py export-md` to regenerate this whole table).

| Item | Type | EF | Reps | Interval | Due | LastQ | Last Reviewed |
|------|------|----|----|----------|-----|-------|---------------|
| _(added automatically after each session — none yet)_ | | | | | | | |

---

## GPU / Systems Progress

### CUDA 100-Day Challenge
- **Started:** -
- **Current Day:** 0
- **Last kernel built:** -

| Day | What I Built | Concepts Learned | Notes |
|-----|-------------|-----------------|-------|

### Systems / Backend Foundations
| Topic | Status | Notes |
|-------|--------|-------|
| Memory model and lifecycle | 🔴 Not started | |
| Error handling strategy | 🔴 Not started | |
| Concurrency and synchronization | 🔴 Not started | |
| Filesystem and I/O behavior | 🔴 Not started | |
| Performance profiling basics | 🔴 Not started | |

---

<!-- Sessions will be appended here by Algo Sensei after each practice session -->

### Session Log

#### 2026-04-13 — Repo-Independent OSS Learning Workflow (approx. 35 min)

- **Topics covered:** AI-assisted learning strategy, OSS contribution loop, repo-independent coaching workflow, language-agnostic contribution habits.
- **What was built:** Added a new `OSS Contributor Mode` to Algo Sensei with anti-autopilot guardrails and a reusable contribution loop.
- **Outcome:** Successful. Skill routing + mode docs now support "learn while contributing" instead of blind issue patching.
- **Concepts that clicked:**
	- Contribution is a repeatable pipeline (recon → reproduce → design → thin slices → reflection).
	- AI should provide progressive hints and reviews, not immediate full fixes by default.
	- Repo-agnostic principles transfer across different languages and stacks.
- **Needs more work:**
	- Running this workflow on 1–2 real issues end-to-end.
	- Practicing writing a mini design note before implementation.
- **Review queue updates (next session):**
	- Pick one beginner-friendly OSS issue and score it on clarity/learning/risk.
	- Produce a 10-line architecture map before touching code.
	- Write one failing test first, then implement minimal fix.

#### 2026-04-13 — Repo Mapping Addendum (approx. 20 min)

- **Topics covered:** sample OSS repo architecture mapping, command/data flow analysis, identifying high-learning entry points.
- **What was learned:**
	- Healthy OSS codebases often separate entrypoints, command orchestration, and core backend logic.
	- TUI and CLI share core logic, making behavior parity and regression checks a good learning target.
	- Container + hierarchical index paths are advanced but well-documented and good for deeper systems learning later.
- **Next-step focus:** start with a narrow CLI/TUI parity or validation issue before touching container internals.

#### 2026-04-13 — Language-Neutralization Update (approx. 15 min)

- **Topics covered:** making OSS learning workflow fully language-agnostic and stack-agnostic.
- **What was changed:** removed explicit language references from OSS workflow docs and from progress template fields tied to systems/backend tracking.
- **Outcome:** the contribution-coaching workflow now generalizes cleanly across repositories, languages, and toolchains.
- **Review queue updates (next session):** validate the workflow on one non-DSA repo and confirm each phase (recon, reproduce, design, thin-slice, reflection) is actionable.

#### 2026-04-13 — First-Principles + Repo-Language Adaptation (approx. 15 min)

- **Topics covered:** first-principles debugging workflow, repository language detection, context-aware mentoring behavior.
- **What was changed:**
	- Added explicit first-principles rule at skill level.
	- Added repository-language detection phase in OSS contribution workflow.
	- Enforced invariant-driven design notes before implementation.
- **Outcome:** skill remains language-agnostic by default, but automatically adapts guidance to the repo's detected language and conventions.
- **Review queue updates (next session):** run one issue with the full sequence: detect stack → define invariant → reproduce → minimal fix → proof test.

#### 2026-04-13 — Full Mode First-Principles Audit (approx. 25 min)

- **Topics covered:** comprehensive skill-mode verification, first-principles enforcement consistency, mode-level reasoning contracts.
- **What was changed:**
	- Added a uniform `First-Principles Anchor` section to every file in `modes/`.
	- Added `Mode Execution Contract` in top-level skill router to enforce sequence before solutioning.
	- Verified coverage with search across all mode files.
- **Outcome:** all modes are now explicitly aligned with first-principles reasoning, while remaining repo/language-adaptive.
- **Review queue updates (next session):** run two different modes (one DSA + one non-DSA) and confirm responses start with objective/constraints/invariants/trade-offs.

#### 2026-04-13 — Full-Potential Usage Playbook (approx. 15 min)

- **Topics covered:** practical operating workflow for using Algo Sensei at maximum effectiveness.
- **What was learned:**
	- Best results come from short, repeatable loops: objective → constraints → attempt → feedback → reflection.
	- Mode switching should be intentional: Tutor/Hint early, Review/Pattern Notes after implementation, Progress Tracker at session close.
	- AI should be used as a reasoning accelerator, not as a direct answer generator.
- **Review queue updates (next session):** run one complete issue loop and record where the highest friction happened (repro, hypothesis, implementation, or test proof).

---

## Stats

- **Total problems solved:** 0
- **Total sessions:** 5
- **Current streak:** 0 days
- **Strongest pattern:** -
- **Needs most work:** -
