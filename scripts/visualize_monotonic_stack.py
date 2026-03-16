"""
Monotonic Stack Visualizer — Next Greater Element
Usage: python visualize_monotonic_stack.py
"""
import time

def visualize_monotonic_stack(arr, delay=0.8):
    n = len(arr)
    result = [-1] * n
    stack = []  # stores indices

    print(f"\n{'='*55}")
    print(f"  Monotonic Stack — Next Greater Element")
    print(f"  Array: {arr}")
    print(f"{'='*55}")
    print(f"\nKey idea: maintain a stack of indices whose")
    print(f"  next greater element hasn't been found yet.")
    print(f"  When arr[i] > arr[stack.top], we found the answer for stack.top")

    def render(i, stack, result):
        nums = "  " + "".join(f"{v:^5}" for v in arr)
        print(f"\n{nums}")

        markers = "  "
        for k in range(n):
            if k == i:
                markers += f"{'→':^5}"
            elif k in stack:
                markers += f"{'[S]':^5}"
            else:
                markers += f"{'':^5}"
        print(markers)

        res_row = "  "
        for k in range(n):
            res_row += f"{result[k] if result[k] != -1 else '?':^5}"
        print(f"  Result: {res_row}")
        print(f"  Stack (indices): {stack}  → values: {[arr[s] for s in stack]}")

    for i in range(n):
        print(f"\n--- i={i}, arr[i]={arr[i]} ---")

        while stack and arr[i] > arr[stack[-1]]:
            top = stack.pop()
            result[top] = arr[i]
            print(f"  arr[{i}]={arr[i]} > arr[{top}]={arr[top]} → Next Greater for {arr[top]} is {arr[i]} ✅")

        stack.append(i)
        print(f"  Push index {i} (val={arr[i]}) onto stack")
        render(i, stack[:], result[:])
        time.sleep(delay)

    # remaining in stack have no next greater
    while stack:
        top = stack.pop()
        result[top] = -1
        print(f"\n  Index {top} (val={arr[top]}) left in stack → no next greater → -1")

    print(f"\n{'='*55}")
    print(f"  Input:          {arr}")
    print(f"  Next Greater:   {result}")
    print(f"\n  Explanation:")
    for i in range(n):
        if result[i] == -1:
            print(f"    arr[{i}]={arr[i]} → no greater element to the right")
        else:
            print(f"    arr[{i}]={arr[i]} → next greater is {result[i]}")
    print(f"\n  Time: O(n)  |  Space: O(n)")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Monotonic Stack Visualizer — Next Greater Element")
    print("--------------------------------------------------")
    raw = input("Enter array (space-separated): ").strip()
    arr = list(map(int, raw.split()))
    visualize_monotonic_stack(arr)
