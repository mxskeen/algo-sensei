"""
Linked List Reversal Visualizer — shows prev/curr/next pointers moving step by step
Usage: python visualize_linked_list_reversal.py
"""
import time

def render_list(nodes, prev_i=None, curr_i=None, next_i=None, reversed_up_to=None):
    n = len(nodes)
    if n == 0:
        print("  (empty list)")
        return

    # draw nodes
    row = "  "
    for i, val in enumerate(nodes):
        row += f"[{val}]"
        if i < n - 1:
            if reversed_up_to is not None and i < reversed_up_to:
                row += " ← "   # reversed arrow
            else:
                row += " → "
    row += " → None"
    print(row)

    # draw pointer labels
    labels = "  "
    for i, val in enumerate(nodes):
        cell = ""
        tags = []
        if i == prev_i: tags.append("prev")
        if i == curr_i: tags.append("curr")
        if i == next_i: tags.append("next")
        label = "/".join(tags) if tags else ""
        # align under node (each node is [X] = 3 chars + arrow = 3 chars = 6 total)
        labels += f"{label:^3}"
        if i < n - 1:
            labels += "   "
    print(labels)


def visualize_reversal(values, delay=0.8):
    n = len(values)

    print(f"\n{'='*55}")
    print(f"  Linked List Reversal Visualizer")
    print(f"  Input: {values}")
    print(f"{'='*55}")

    print(f"\nOriginal list:")
    render_list(values)
    time.sleep(delay)

    print(f"\nAlgorithm: 3-pointer approach (prev, curr, next)")
    print(f"  prev = None  (will become new tail)")
    print(f"  curr = head  (start here)")
    time.sleep(delay)

    prev = None   # index
    curr = 0      # index
    step = 1

    while curr < n:
        next_node = curr + 1 if curr + 1 < n else None

        print(f"\n--- Step {step} ---")
        render_list(values, prev_i=prev, curr_i=curr, next_i=next_node, reversed_up_to=curr)

        print(f"\n  curr = {values[curr]}")
        if next_node is not None:
            print(f"  1. Save next: next = {values[next_node]}")
        else:
            print(f"  1. Save next: next = None (end of list)")

        if prev is not None:
            print(f"  2. Reverse pointer: [{values[curr]}] → [{values[prev]}]")
        else:
            print(f"  2. Reverse pointer: [{values[curr]}] → None  (curr becomes new tail)")

        print(f"  3. Move prev to curr: prev = {values[curr]}")
        if next_node is not None:
            print(f"  4. Move curr to next: curr = {values[next_node]}")
        else:
            print(f"  4. Move curr to next: curr = None  (done!)")

        prev = curr
        curr = next_node if next_node is not None else n
        step += 1
        time.sleep(delay)

    # show reversed
    reversed_vals = list(reversed(values))
    print(f"\n{'='*55}")
    print(f"  Reversal complete!")
    print(f"\n  Reversed list:")
    render_list(reversed_vals)
    print(f"\n  Original: {values}")
    print(f"  Reversed: {reversed_vals}")
    print(f"  Time: O(n)  |  Space: O(1)")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Linked List Reversal Visualizer")
    print("--------------------------------")
    raw = input("Enter linked list values (space-separated): ").strip()
    values = list(map(int, raw.split()))
    visualize_reversal(values)
