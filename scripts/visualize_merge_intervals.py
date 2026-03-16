"""
Merge Intervals Visualizer — shows intervals on a number line, merging step by step
Usage: python visualize_merge_intervals.py
"""
import time

def render_number_line(intervals, merged, current=None, width=60):
    if not intervals and not merged:
        return
    all_vals = [x for iv in intervals + merged for x in iv]
    if current:
        all_vals += list(current)
    lo, hi = min(all_vals), max(all_vals)
    span = max(hi - lo, 1)
    scale = width / span

    def to_pos(v):
        return int((v - lo) * scale)

    print(f"\n  {lo}" + " " * (width - len(str(lo)) - len(str(hi))) + f"{hi}")
    print(f"  |" + "-" * (width - 2) + "|")

    for iv in intervals:
        l, r = to_pos(iv[0]), to_pos(iv[1])
        line = " " * l + "=" * max(r - l, 1)
        print(f"  {line:<{width}}  [{iv[0]}, {iv[1]}]")

    if current:
        l, r = to_pos(current[0]), to_pos(current[1])
        line = " " * l + "█" * max(r - l, 1)
        print(f"  {line:<{width}}  ← merging into [{current[0]}, {current[1]}]")

    if merged:
        print(f"\n  Merged so far:")
        for iv in merged:
            l, r = to_pos(iv[0]), to_pos(iv[1])
            line = " " * l + "▓" * max(r - l, 1)
            print(f"  {line:<{width}}  [{iv[0]}, {iv[1]}]")


def visualize_merge_intervals(intervals, delay=0.9):
    print(f"\n{'='*55}")
    print(f"  Merge Intervals Visualizer")
    print(f"  Input: {intervals}")
    print(f"{'='*55}")

    # sort
    intervals = sorted(intervals, key=lambda x: x[0])
    print(f"\nStep 1: Sort by start time → {intervals}")
    render_number_line(intervals, [])
    time.sleep(delay)

    merged = []
    step = 2

    for i, interval in enumerate(intervals):
        print(f"\n--- Step {step}: Process {interval} ---")

        if not merged:
            merged.append(list(interval))
            print(f"  First interval — add directly: {interval}")
            render_number_line(intervals[i+1:], merged)
        else:
            last = merged[-1]
            if interval[0] <= last[1]:
                # overlap
                old = last[:]
                last[1] = max(last[1], interval[1])
                print(f"  {interval} overlaps with {old} → merge into {last}")
                render_number_line(intervals[i+1:], merged[:-1], tuple(last))
            else:
                # no overlap
                print(f"  {interval} does NOT overlap with {last} (gap exists) → add separately")
                merged.append(list(interval))
                render_number_line(intervals[i+1:], merged)

        time.sleep(delay)
        step += 1

    result = [tuple(m) for m in merged]
    print(f"\n{'='*55}")
    print(f"  Result: {result}")
    print(f"  Reduced {len(intervals)} intervals → {len(result)} merged intervals")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Merge Intervals Visualizer")
    print("--------------------------")
    print("Enter intervals one per line as 'start end' (e.g. '1 3')")
    print("Press Enter twice when done.\n")

    intervals = []
    while True:
        line = input("Interval (or blank to finish): ").strip()
        if not line:
            break
        a, b = map(int, line.split())
        intervals.append((a, b))

    visualize_merge_intervals(intervals)
