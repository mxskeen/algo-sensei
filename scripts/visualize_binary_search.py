"""
Binary Search Visualizer
Usage: python visualize_binary_search.py
"""
import time

def visualize_binary_search(arr, target, delay=0.6):
    n = len(arr)
    left, right = 0, n - 1
    step = 1

    print(f"\n{'='*50}")
    print(f"  Binary Search  |  Target: {target}")
    print(f"{'='*50}")

    def render(left, right, mid):
        # number row
        nums = ""
        for i, val in enumerate(arr):
            nums += f"{val:^5}"
        print(f"\n  {nums}")

        # pointer row
        ptrs = ""
        for i in range(n):
            if i == left == right == mid:
                ptrs += f"{'LMR':^5}"
            elif i == left == mid:
                ptrs += f"{'LM':^5}"
            elif i == right == mid:
                ptrs += f"{'MR':^5}"
            elif i == left == right:
                ptrs += f"{'LR':^5}"
            elif i == left:
                ptrs += f"{'L':^5}"
            elif i == right:
                ptrs += f"{'R':^5}"
            elif i == mid:
                ptrs += f"{'M':^5}"
            else:
                ptrs += f"{'':^5}"
        print(f"  {ptrs}")

    while left <= right:
        mid = left + (right - left) // 2
        print(f"\n--- Step {step} ---")
        render(left, right, mid)
        print(f"\n  arr[mid={mid}] = {arr[mid]}", end="")

        if arr[mid] == target:
            print(f"  →  FOUND ✅  (index {mid})")
            print(f"\n{'='*50}\n")
            return mid
        elif arr[mid] < target:
            print(f"  <  {target}  →  move L right")
            left = mid + 1
        else:
            print(f"  >  {target}  →  move R left")
            right = mid - 1

        step += 1
        time.sleep(delay)

    print(f"\n  NOT FOUND ❌")
    print(f"\n{'='*50}\n")
    return -1


if __name__ == "__main__":
    print("Binary Search Visualizer")
    print("------------------------")
    raw = input("Enter sorted array (space-separated): ").strip()
    arr = list(map(int, raw.split()))
    target = int(input("Enter target: ").strip())
    visualize_binary_search(arr, target)
