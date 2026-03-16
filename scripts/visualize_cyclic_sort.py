"""
Cyclic Sort Visualizer — places each number at its correct index
Usage: python visualize_cyclic_sort.py
"""
import time

def visualize_cyclic_sort(arr, delay=0.8):
    n = len(arr)
    nums = arr[:]

    print(f"\n{'='*55}")
    print(f"  Cyclic Sort Visualizer")
    print(f"  Input: {nums}  (values 1 to {n})")
    print(f"{'='*55}")
    print(f"\nKey idea: each number X belongs at index X-1")
    print(f"  If nums[i] != i+1, swap nums[i] with nums[nums[i]-1]")

    def render(i=None, j=None):
        row = "  "
        for k, v in enumerate(nums):
            row += f"{v:^5}"
        print(f"\n{row}")

        idx_row = "  "
        for k in range(n):
            idx_row += f"{'['+str(k)+']':^5}"
        print(idx_row)

        if i is not None:
            ptr = "  "
            for k in range(n):
                if k == i and k == j:
                    ptr += f"{'i=j':^5}"
                elif k == i:
                    ptr += f"{'i':^5}"
                elif k == j:
                    ptr += f"{'j':^5}"
                else:
                    ptr += f"{'':^5}"
            print(ptr)

        correct = "  "
        for k, v in enumerate(nums):
            correct += f"{'✅' if v == k+1 else '  ':^5}"
        print(correct)

    print(f"\nInitial state:")
    render()
    time.sleep(delay)

    i = 0
    step = 1
    while i < n:
        j = nums[i] - 1  # correct index for nums[i]

        print(f"\n--- Step {step}: i={i}, nums[i]={nums[i]} ---")
        print(f"  nums[{i}]={nums[i]} belongs at index {j}")

        if nums[i] != nums[j]:
            print(f"  nums[{i}]={nums[i]} ≠ nums[{j}]={nums[j]} → swap")
            render(i, j)
            nums[i], nums[j] = nums[j], nums[i]
            print(f"  After swap:")
            render(i, j)
        else:
            print(f"  nums[{i}]={nums[i]} already in correct place (or duplicate) → move i forward")
            render(i, j)
            i += 1

        step += 1
        time.sleep(delay)

    print(f"\n{'='*55}")
    print(f"  Sorted: {nums}")

    missing = [i+1 for i in range(n) if nums[i] != i+1]
    if missing:
        print(f"  Missing numbers: {missing}")
    else:
        print(f"  All numbers 1..{n} present ✅")
    print(f"  Time: O(n)  |  Space: O(1)")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Cyclic Sort Visualizer")
    print("----------------------")
    print("Enter an array containing numbers from 1 to n (may have missing/duplicates)")
    raw = input("Array (space-separated): ").strip()
    arr = list(map(int, raw.split()))
    visualize_cyclic_sort(arr)
