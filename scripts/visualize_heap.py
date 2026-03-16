"""
Min-Heap Visualizer — insert and extract-min with tree rendering
Usage: python visualize_heap.py
"""
import time

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i):
        steps = []
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            steps.append((i, p, self.heap[i], self.heap[p]))
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
        return steps

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def _bubble_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            l, r = self.left(i), self.right(i)
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


def render_heap(heap):
    if not heap:
        print("  (empty heap)")
        return
    n = len(heap)
    level = 0
    i = 0
    levels = []
    while i < n:
        count = 2 ** level
        levels.append(heap[i:i+count])
        i += count
        level += 1

    max_width = 2 ** (len(levels) - 1)
    for lvl, nodes in enumerate(levels):
        spacing = max_width // (2 ** lvl)
        pad = " " * (spacing * 2)
        gap = " " * (spacing * 4)
        row = pad + gap.join(f"{v:^3}" for v in nodes)
        print(f"  {row}")

    print(f"\n  Array: {heap}")


def visualize_heap_operations(values, delay=0.8):
    h = MinHeap()

    print(f"\n{'='*50}")
    print(f"  Min-Heap Visualizer")
    print(f"  Inserting: {values}")
    print(f"{'='*50}")

    # insertions
    for val in values:
        print(f"\n--- Insert {val} ---")
        h.heap.append(val)
        print(f"  Added {val} at end (index {len(h.heap)-1})")
        render_heap(h.heap[:])

        i = len(h.heap) - 1
        swapped = False
        while i > 0 and h.heap[h.parent(i)] > h.heap[i]:
            p = h.parent(i)
            print(f"\n  heap[{i}]={h.heap[i]} < heap[{p}]={h.heap[p]} (parent) → swap ↑")
            h.heap[i], h.heap[p] = h.heap[p], h.heap[i]
            i = p
            swapped = True
            render_heap(h.heap[:])
            time.sleep(delay / 2)

        if not swapped:
            print(f"  {val} is already in correct position — no swap needed")

        time.sleep(delay)

    print(f"\n{'='*50}")
    print(f"  Heap built. Min is always at index 0: {h.heap[0]}")
    print(f"{'='*50}")

    # extract-min
    print(f"\n--- Now extracting min values one by one ---")
    extracted = []
    while h.heap:
        min_val = h.heap[0]
        print(f"\n--- Extract Min ---")
        print(f"  Min = heap[0] = {min_val}")

        if len(h.heap) == 1:
            h.heap.pop()
            extracted.append(min_val)
            print(f"  Last element removed.")
            break

        last = h.heap.pop()
        h.heap[0] = last
        print(f"  Move last element ({last}) to root, remove old root")
        render_heap(h.heap[:])

        # bubble down
        i = 0
        while True:
            smallest = i
            l, r = 2*i+1, 2*i+2
            n = len(h.heap)
            if l < n and h.heap[l] < h.heap[smallest]:
                smallest = l
            if r < n and h.heap[r] < h.heap[smallest]:
                smallest = r
            if smallest == i:
                print(f"  {h.heap[i]} is in correct position — done")
                break
            print(f"  heap[{i}]={h.heap[i]} > heap[{smallest}]={h.heap[smallest]} → swap ↓")
            h.heap[i], h.heap[smallest] = h.heap[smallest], h.heap[i]
            i = smallest
            render_heap(h.heap[:])
            time.sleep(delay / 2)

        extracted.append(min_val)
        time.sleep(delay)

    print(f"\n{'='*50}")
    print(f"  Extracted order (sorted): {extracted}")
    print(f"  This is Heap Sort! O(n log n)")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    print("Min-Heap Visualizer")
    print("-------------------")
    raw = input("Enter values to insert (space-separated): ").strip()
    values = list(map(int, raw.split()))
    visualize_heap_operations(values)
