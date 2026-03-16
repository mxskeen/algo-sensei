"""
Two Pointers Visualizer — finds all pairs summing to target
Usage: python visualize_two_pointers.py
"""
import time

def visualize_two_pointers(arr, target, delay=0.7):
    arr = sorted(arr)
    n = len(arr)
    left, right = 0, n - 1
    step = 1
    pairs = []

    print(f"\n{'='*50}")
    print(f"  Two Pointers  |  Target sum: {target}")
    print(f"  Array (sorted): {arr}")
    print(f"{'='*50}")

    def render(left, right):
        nums = ""
        for i, val in enumerate(arr):
            nums += f"{val:^5}"
        print(f"\n  {nums}")

        ptrs = ""
        for i in range(n):
            if i == left == right:
                ptrs += f"{'LR':^5}"
            elif i == left:
                ptrs += f"{'L':^5}"
            elif i == right:
                ptrs += f"{'R':^5}"
            else:
                ptrs += f"{'':^5}"
        print(f"  {ptrs}")

    while left < right:
        print(f"\n--- Step {step} ---")
        render(left, right)
        current_sum = arr[left] + arr[right]
        print(f"\n  arr[L={left}]={arr[left]} + arr[R={right}]={arr[right]} = {current_sum}", end="")

        if current_sum == target:
            print(f"  =  {target}  →  PAIR FOUND ✅ ({arr[left]}, {arr[right]})")
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            print(f"  <  {target}  →  move L right (need bigger sum)")
            left += 1
        else:
            print(f"  >  {target}  →  move R left (need smaller sum)")
            right -= 1

        step += 1
        time.sleep(delay)

    print(f"\n{'='*50}")
    if pairs:
        print(f"  Pairs found: {pairs}")
    else:
        print(f"  No pairs found that sum to {target}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    print("Two Pointers Visualizer")
    print("-----------------------")
    raw = input("Enter array (space-separated): ").strip()
    arr = list(map(int, raw.split()))
    target = int(input("Enter target sum: ").strip())
    visualize_two_pointers(arr, target)
