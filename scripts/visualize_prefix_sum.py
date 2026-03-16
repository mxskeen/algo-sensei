"""
Prefix Sum Visualizer — building prefix array and answering range sum queries
Usage: python visualize_prefix_sum.py
"""
import time

def visualize_prefix_sum(arr, queries, delay=0.7):
    n = len(arr)
    prefix = [0] * (n + 1)

    print(f"\n{'='*55}")
    print(f"  Prefix Sum Visualizer")
    print(f"  Array: {arr}")
    print(f"{'='*55}")

    print(f"\nStep 1: Build prefix sum array")
    print(f"  prefix[i] = sum of arr[0..i-1]")
    print(f"  prefix[0] = 0  (empty prefix)")

    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]

        # render
        orig = "  Original: " + "".join(f"{v:^5}" for v in arr)
        pfx  = "  Prefix:   " + "".join(f"{prefix[j]:^5}" for j in range(i+1))

        print(f"\n  prefix[{i}] = prefix[{i-1}] + arr[{i-1}] = {prefix[i-1]} + {arr[i-1]} = {prefix[i]}")
        print(orig)
        print(pfx)
        time.sleep(delay / 2)

    print(f"\n  Final prefix array: {prefix}")
    print(f"  Index:              {list(range(n+1))}")

    print(f"\n{'='*55}")
    print(f"Step 2: Answer range sum queries in O(1)")
    print(f"  sum(l, r) = prefix[r+1] - prefix[l]")
    print(f"{'='*55}")

    for l, r in queries:
        result = prefix[r+1] - prefix[l]
        print(f"\n  Query: sum(arr[{l}..{r}])")
        print(f"  = prefix[{r+1}] - prefix[{l}]")
        print(f"  = {prefix[r+1]} - {prefix[l]}")
        print(f"  = {result}")
        print(f"  Subarray: {arr[l:r+1]}")
        print(f"  Verify:   {sum(arr[l:r+1])} ✅" if sum(arr[l:r+1]) == result else f"  ❌ mismatch")
        time.sleep(delay)

    print(f"\n{'='*55}")
    print(f"  Without prefix sum: each query = O(n)")
    print(f"  With prefix sum:    build O(n), each query O(1)")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Prefix Sum Visualizer")
    print("---------------------")
    raw = input("Enter array (space-separated): ").strip()
    arr = list(map(int, raw.split()))

    queries = []
    print("Enter range queries as 'l r' (0-indexed). Press Enter twice when done.")
    while True:
        line = input("Query (or blank to finish): ").strip()
        if not line:
            break
        l, r = map(int, line.split())
        queries.append((l, r))

    if not queries:
        queries = [(0, len(arr)-1)]

    visualize_prefix_sum(arr, queries)
