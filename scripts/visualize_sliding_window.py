"""
Sliding Window Visualizer — longest substring with at most K distinct characters
Usage: python visualize_sliding_window.py
"""
import time
from collections import defaultdict

def visualize_sliding_window(s, k, delay=0.7):
    n = len(s)
    left = 0
    char_count = defaultdict(int)
    max_len = 0
    best_window = (0, 0)
    step = 1

    print(f"\n{'='*55}")
    print(f"  Sliding Window  |  String: '{s}'  |  Max distinct: {k}")
    print(f"{'='*55}")

    def render(left, right, window_valid):
        chars = "  " + "  ".join(f"{c:^1}" for c in s)
        print(f"\n{chars}")

        ptrs = "  "
        for i in range(n):
            if left <= i <= right:
                ptrs += f"{'█':^3}"
            else:
                ptrs += f"{'·':^3}"
        print(ptrs)

        ptr_labels = "  "
        for i in range(n):
            if i == left == right:
                ptr_labels += f"{'LR':^3}"
            elif i == left:
                ptr_labels += f"{'L':^3}"
            elif i == right:
                ptr_labels += f"{'R':^3}"
            else:
                ptr_labels += f"{'':^3}"
        print(ptr_labels)

        window_str = s[left:right+1]
        distinct = len(set(window_str))
        status = "✅ valid" if window_valid else "❌ shrink"
        print(f"\n  Window: '{window_str}'  |  Distinct chars: {distinct}/{k}  |  {status}")
        print(f"  Char counts: {dict(char_count)}")

    for right in range(n):
        char_count[s[right]] += 1

        window_valid = len(char_count) <= k

        print(f"\n--- Step {step}: expand R to '{s[right]}' (index {right}) ---")
        render(left, right, window_valid)

        while len(char_count) > k:
            time.sleep(delay / 2)
            print(f"\n  Too many distinct chars → shrink: remove '{s[left]}' at L={left}")
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
            render(left, right, len(char_count) <= k)

        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len
            best_window = (left, right)
            print(f"\n  ★ New best window: '{s[left:right+1]}' (length {max_len})")

        step += 1
        time.sleep(delay)

    print(f"\n{'='*55}")
    print(f"  Longest window with ≤{k} distinct chars: '{s[best_window[0]:best_window[1]+1]}'")
    print(f"  Length: {max_len}  |  Indices: [{best_window[0]}, {best_window[1]}]")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Sliding Window Visualizer")
    print("-------------------------")
    s = input("Enter string: ").strip()
    k = int(input("Max distinct characters allowed: ").strip())
    visualize_sliding_window(s, k)
