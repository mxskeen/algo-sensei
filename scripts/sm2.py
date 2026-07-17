#!/usr/bin/env python3
"""Real SuperMemo-2 (SM-2) spaced-repetition engine for Algo Sensei.

This is the AUTHORITATIVE state owner for spaced repetition. It is the same
algorithm Anki's original scheduler is based on: every item tracks an ease
factor (EF), a repetition count, and an interval, and after each review you
grade recall quality q in 0..5.

    EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)),  floor 1.3
    if q < 3:   reps = 0,  interval = 1            # lapse -> relearn tomorrow
    else:       reps += 1
                interval = 1   if reps == 1
                         = 6   if reps == 2
                         = round(interval_prev * EF')   otherwise  # grows forever

State lives in progress/sm2_state.json (single source of truth). The LLM just
runs commands and pastes the printed markdown -- no hand arithmetic, so the
schedule can never silently drift.

Commands:
    python sm2.py init
    python sm2.py add --item "Two Sum" --type Problem
    python sm2.py review --item "Two Sum" --q 4
    python sm2.py due
    python sm2.py export-md
    python sm2.py --self-test
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

DEFAULT_EF = 2.5
MIN_EF = 1.3

DEFAULT_STATE = (Path(__file__).resolve().parent.parent / "progress" / "sm2_state.json")


def next_state(ef, reps, interval, q, today=None):
    if today is None:
        today = dt.date.today()
    q = int(q)
    if not 0 <= q <= 5:
        raise ValueError("quality q must be in 0..5")
    ef_new = ef + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    if ef_new < MIN_EF:
        ef_new = MIN_EF
    if q < 3:
        reps_new = 0
        interval_new = 1
    else:
        reps_new = reps + 1
        if reps_new == 1:
            interval_new = 1
        elif reps_new == 2:
            interval_new = 6
        else:
            interval_new = round(interval * ef_new)
    due = today + dt.timedelta(days=interval_new)
    return ef_new, reps_new, interval_new, due


def load_state(path):
    if path.exists():
        return json.loads(path.read_text())
    return {}


def save_state(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def row_md(name, item):
    return (
        f"| {name} | {item.get('type', '')} | {item['ef']:.2f} | {item['reps']} "
        f"| {item['interval']} | {item['due']} | {item.get('last_q', '')} "
        f"| {item.get('last_reviewed', '')} |"
    )


def cmd_init(args):
    save_state(args.state, load_state(args.state) or {})
    print(f"Initialized state file: {args.state}")


def cmd_add(args):
    state = load_state(args.state)
    if args.item in state:
        print(f"Item '{args.item}' already exists.")
        return
    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    state[args.item] = {
        "type": args.type or "",
        "ef": DEFAULT_EF,
        "reps": 0,
        "interval": 0,
        "due": today.isoformat(),
        "last_q": "",
        "last_reviewed": today.isoformat(),
    }
    save_state(args.state, state)
    print(f"Added '{args.item}'. Review it with: python sm2.py review --item \"{args.item}\" --q <0-5>")


def cmd_review(args):
    state = load_state(args.state)
    if args.item not in state:
        print(f"Unknown item '{args.item}'. Add it first: python sm2.py add --item \"{args.item}\" --type <Problem|Pattern>")
        sys.exit(1)
    item = state[args.item]
    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    ef_n, reps_n, int_n, due = next_state(item["ef"], item["reps"], item["interval"], args.q, today)
    item.update(ef=round(ef_n, 4), reps=reps_n, interval=int_n,
                due=due.isoformat(), last_q=args.q, last_reviewed=today.isoformat())
    state[args.item] = item
    save_state(args.state, state)
    print(f"## Review recorded: {args.item}")
    print(f"- Quality q: {args.q}/5")
    print(f"- EF: {item['ef']:.2f}  Reps: {item['reps']}  Interval: {item['interval']} day(s)  Next due: {item['due']}")
    print("\nPaste-ready row for `progress/progress.md` SM-2 Review Queue:")
    print(row_md(args.item, item))


def cmd_due(args):
    state = load_state(args.state)
    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    due_items = [(n, it) for n, it in state.items() if dt.date.fromisoformat(it["due"]) <= today]
    due_items.sort(key=lambda kv: kv[1]["due"])
    if not due_items:
        print("Nothing due.")
        return
    print(f"## Due for review (as of {today.isoformat()}):")
    for n, it in due_items:
        print(f"- {n}  (due {it['due']}, interval {it['interval']}d, EF {it['ef']:.2f})")


def cmd_export_md(args):
    state = load_state(args.state)
    print("| Item | Type | EF | Reps | Interval | Due | LastQ | Last Reviewed |")
    print("|------|------|----|----|----------|-----|-------|---------------|")
    for n, it in sorted(state.items(), key=lambda kv: kv[1]["due"]):
        print(row_md(n, it))


def self_test():
    cases = [
        (2.5, 0, 0, 5, (2.6, 1, 1)),
        (2.6, 1, 1, 5, (2.7, 2, 6)),
        (2.7, 2, 6, 4, (2.7, 3, 16)),
        (2.7, 3, 16, 3, (2.56, 4, 41)),
        (2.5, 2, 6, 0, (1.7, 0, 1)),
    ]
    ok = True
    for ef, reps, interval, q, (ef_e, reps_e, int_e) in cases:
        ef_n, reps_n, int_n, _ = next_state(ef, reps, interval, q)
        passed = (round(ef_n, 4) == round(ef_e, 4) and reps_n == reps_e and int_n == int_e)
        ok = ok and passed
        print(f"q={q}: ef={ef_n:.4f} reps={reps_n} interval={int_n} -> {'OK' if passed else f'FAIL (exp {ef_e},{reps_e},{int_e})'}")
    print("SELF-TEST", "PASSED" if ok else "FAILED")
    sys.exit(0 if ok else 1)


def main():
    p = argparse.ArgumentParser(description="Algo Sensei real SM-2 spaced-repetition engine")
    p.add_argument("--state", type=Path, default=DEFAULT_STATE, help="path to sm2 state JSON")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("init")
    pa = sub.add_parser("add")
    pa.add_argument("--item", required=True)
    pa.add_argument("--type", default="")
    pa.add_argument("--date", default=None)
    pr = sub.add_parser("review")
    pr.add_argument("--item", required=True)
    pr.add_argument("--q", type=int, required=True)
    pr.add_argument("--date", default=None)
    pd = sub.add_parser("due")
    pd.add_argument("--date", default=None)
    sub.add_parser("export-md")
    p.add_argument("--self-test", action="store_true")

    args = p.parse_args()
    if args.self_test:
        self_test()
    if not args.cmd:
        p.print_help()
        sys.exit(1)
    {"init": cmd_init, "add": cmd_add, "review": cmd_review,
     "due": cmd_due, "export-md": cmd_export_md}[args.cmd](args)


if __name__ == "__main__":
    main()
