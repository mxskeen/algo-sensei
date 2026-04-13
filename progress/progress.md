# Algo Sensei Progress Tracker 📊

> This file is maintained by Algo Sensei. At the start of each session, share this file for personalized guidance.
> At the end of each session, ask Algo Sensei to update it.

---

## Profile

**Started:** [date]
**Primary Focus Stack:** [language(s)/framework(s)/domain]
**Goal:** [e.g., FAANG prep, general DSA, specific interview date]
**Self-assessed Level:** [Beginner/Intermediate/Advanced]

---

## Pattern Confidence Map

Rate: 🔴 Weak | 🟡 Learning | 🟢 Solid | ⭐ Mastered

| Pattern | Confidence | Last Practiced | Notes |
|---------|------------|----------------|-------|
| Two Pointers | 🔴 Weak | - | - |
| Fast & Slow Pointers | 🔴 Weak | - | - |
| Sliding Window | 🔴 Weak | - | - |
| Kadane's Algorithm | 🔴 Weak | - | - |
| Prefix Sum | 🔴 Weak | - | - |
| Binary Search | 🔴 Weak | - | - |
| Hash Map / Set | 🔴 Weak | - | - |
| Stack / Monotonic Stack | 🔴 Weak | - | - |
| Merge Intervals | 🔴 Weak | - | - |
| Cyclic Sort | 🔴 Weak | - | - |
| LinkedList Reversal | 🔴 Weak | - | - |
| Queue / BFS | 🔴 Weak | - | - |
| DFS / Matrix Traversal | 🔴 Weak | - | - |
| Backtracking / Subsets | 🔴 Weak | - | - |
| Dynamic Programming | 🔴 Weak | - | - |
| Greedy | 🔴 Weak | - | - |
| Heap / Top K Elements | 🔴 Weak | - | - |
| Two Heaps | 🔴 Weak | - | - |
| Trie | 🔴 Weak | - | - |
| Topological Sort | 🔴 Weak | - | - |
| Union Find | 🔴 Weak | - | - |
| Bitwise XOR | 🔴 Weak | - | - |
| Ordered Set | 🔴 Weak | - | - |

---

## Problems Solved

| # | Problem | Difficulty | Pattern | Solved Independently | Date | Notes |
|---|---------|------------|---------|----------------------|------|-------|

---

## Review Queue

Problems/patterns scheduled for review (from spaced repetition):

| Item | Type | Due Date | Priority |
|------|------|----------|----------|

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

---

## Stats

- **Total problems solved:** 0
- **Total sessions:** 4
- **Current streak:** 0 days
- **Strongest pattern:** -
- **Needs most work:** -
