# Visualization Scripts 🎬

Run these locally to see algorithms animate step-by-step in your terminal.
No external libraries needed — pure Python 3 standard library.

## Usage

```bash
cd algo-sensei/scripts
python visualize_<pattern>.py
# Follow the prompts to enter your input
```

## All Scripts

| Script | Pattern | What it shows |
|--------|---------|---------------|
| `visualize_binary_search.py` | Binary Search | L/M/R pointers, which half gets eliminated |
| `visualize_two_pointers.py` | Two Pointers | L/R converging, pair detection |
| `visualize_sliding_window.py` | Sliding Window | Window expanding/shrinking, distinct char tracking |
| `visualize_kadane.py` | Kadane's Algorithm | extend vs fresh decision at each index |
| `visualize_prefix_sum.py` | Prefix Sum | prefix array build + O(1) range queries |
| `visualize_merge_intervals.py` | Merge Intervals | intervals on number line, overlap detection |
| `visualize_cyclic_sort.py` | Cyclic Sort | each number swapping to its correct index |
| `visualize_monotonic_stack.py` | Monotonic Stack | stack state, next greater element |
| `visualize_bfs.py` | BFS | level-by-level traversal, queue state |
| `visualize_dfs.py` | DFS | recursive call stack, backtracking |
| `visualize_topological_sort.py` | Topological Sort | in-degree tracking, Kahn's algorithm |
| `visualize_union_find.py` | Union Find | parent/rank arrays, path compression |
| `visualize_backtracking.py` | Backtracking | decision tree, pruning, combination sum |
| `visualize_heap.py` | Heap | bubble-up on insert, bubble-down on extract |
| `visualize_linked_list_reversal.py` | LinkedList Reversal | prev/curr/next pointer movement |
| `visualize_dp_knapsack.py` | DP (0/1 Knapsack) | DP table filling cell by cell |

## Speed Control

Each script has a `delay` parameter (default 0.6–0.9s per step).
To run faster, edit the script and lower the delay:
```python
visualize_binary_search(arr, target, delay=0.2)
```
