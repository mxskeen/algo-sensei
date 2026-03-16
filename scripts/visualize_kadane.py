"""
Kadane's Algorithm Visualizer — maximum subarray sum
Usage: python visualize_kadane.py
"""
import time

def visualize_kadane(arr, delay=0.7):
    n = len(arr)
    max_sum = arr[0]
    curr_sum = arr[0]
    best_start = best_end = 0
    curr_start = 0

    print(f"\n{'='*55}")
    print(f"  Kadane's Algorithm  |  Max Subarray Sum")
    print(f"  Array: {arr}")
    print(f"{'='*55}")
    print(f"\nKey idea: at each index, decide —")
    print(f"  extend current subarray  OR  start fresh from here")

    def render(i, curr_start, best_start, best_end, curr_sum, max_sum):
        nums = "  "
        for j, v in enumerate(arr):
            nums += f"{v:^5}"
        print(f"\n{nums}")

        markers = "  "
        for j in range(n):
            if j == best_start == best_end == i:
                markers += f"{'B*':^5}"
            elif j == i:
                markers += f"{'*':^5}"
            elif best_start <= j <= best_end:
                markers += f"{'B':^5}"
            elif curr_start <= j <= i:
                markers += f"{'~':^5}"
            else:
                markers += f"{'':^5}"
        print(markers)
        print(f"\n  i={i}  val={arr[i]}  curr_sum={curr_sum}  max_sum={max_sum}")
        print(f"  Current window: arr[{curr_start}..{i}] = {arr[curr_start:i+1]}")
        print(f"  Best so far:    arr[{best_start}..{best_end}] = {arr[best_start:best_end+1]}  (sum={max_sum})")

    print(f"\n--- Start: i=0, val={arr[0]} ---")
    render(0, 0, 0, 0, curr_sum, max_sum)
    time.sleep(delay)

    for i in range(1, n):
        print(f"\n--- i={i}, val={arr[i]} ---")

        extend = curr_sum + arr[i]
        fresh = arr[i]

        print(f"  Extend: {curr_sum} + {arr[i]} = {extend}")
        print(f"  Fresh:  {arr[i]}")

        if fresh > extend:
            print(f"  → Start fresh (fresh={fresh} > extend={extend})")
            curr_sum = fresh
            curr_start = i
        else:
            print(f"  → Extend current window (extend={extend} >= fresh={fresh})")
            curr_sum = extend

        if curr_sum > max_sum:
            max_sum = curr_sum
            best_start = curr_start
            best_end = i
            print(f"  ★ New max found: {max_sum}")

        render(i, curr_start, best_start, best_end, curr_sum, max_sum)
        time.sleep(delay)

    print(f"\n{'='*55}")
    print(f"  Max subarray: {arr[best_start:best_end+1]}")
    print(f"  Indices: [{best_start}, {best_end}]")
    print(f"  Max sum: {max_sum}")
    print(f"  Time: O(n)  |  Space: O(1)")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Kadane's Algorithm Visualizer")
    print("------------------------------")
    raw = input("Enter array (space-separated): ").strip()
    arr = list(map(int, raw.split()))
    visualize_kadane(arr)
