"""
Backtracking Visualizer — Combination Sum (find all combos that sum to target)
Usage: python visualize_backtracking.py
"""
import time

def visualize_backtracking(candidates, target, delay=0.6):
    candidates = sorted(candidates)
    results = []
    call_count = [0]

    print(f"\n{'='*55}")
    print(f"  Backtracking — Combination Sum")
    print(f"  Candidates: {candidates}  |  Target: {target}")
    print(f"{'='*55}")
    print(f"\nKey idea: at each step, choose a candidate or backtrack")
    print(f"  Decision tree: branch for each candidate, prune when sum > target\n")

    def render_path(path, remaining, depth, chosen=None, action=""):
        indent = "  " + "  " * depth
        path_str = f"[{', '.join(map(str, path))}]" if path else "[]"
        print(f"{indent}{action} path={path_str}  remaining={remaining}", end="")
        if chosen is not None:
            print(f"  trying {chosen}", end="")
        print()

    def backtrack(start, path, remaining, depth):
        call_count[0] += 1
        indent = "  " + "  " * depth

        if remaining == 0:
            results.append(path[:])
            print(f"{indent}✅ FOUND: {path}  (sum = {target})")
            time.sleep(delay)
            return

        if remaining < 0:
            print(f"{indent}❌ PRUNE: sum exceeded target (remaining={remaining})")
            time.sleep(delay / 2)
            return

        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                print(f"{indent}⏭  {c} > remaining={remaining}, skip rest (sorted)")
                break

            print(f"\n{indent}→ Choose {c}  (path so far: {path + [c]}, remaining: {remaining - c})")
            path.append(c)
            time.sleep(delay / 2)
            backtrack(i, path, remaining - c, depth + 1)
            path.pop()
            print(f"{indent}← Backtrack: remove {c}  (path: {path})")
            time.sleep(delay / 2)

    print(f"  Starting backtracking...\n")
    backtrack(0, [], target, 0)

    print(f"\n{'='*55}")
    print(f"  All combinations that sum to {target}:")
    for r in results:
        print(f"    {r}  (sum={sum(r)})")
    if not results:
        print(f"    None found")
    print(f"\n  Total recursive calls: {call_count[0]}")
    print(f"  Results found: {len(results)}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Backtracking Visualizer — Combination Sum")
    print("------------------------------------------")
    raw = input("Enter candidates (space-separated, e.g. 2 3 6 7): ").strip()
    candidates = list(map(int, raw.split()))
    target = int(input("Enter target sum: ").strip())
    visualize_backtracking(candidates, target)
