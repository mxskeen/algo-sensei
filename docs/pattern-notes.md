# Pattern Notes 📓

> Your personal pattern encyclopedia — built from your actual solved problems.
> Grows automatically as you practice. Share this file with Algo Sensei to get pattern-aware guidance.

---

<!-- PATTERN NOTES ARE ADDED HERE BY ALGO SENSEI AFTER EACH SOLVED PROBLEM -->
<!-- Format: one section per pattern, updated incrementally -->

## Two Pointers

**Trigger Words / Clues**
- "sorted array", "pair that sums to", "remove duplicates in-place", "reverse", "palindrome check"
- Input is sorted OR can be sorted first
- Need to find a pair/triplet with a condition

**Brute Force → Why It's Slow**
- Nested loops checking all pairs → O(n²)
- Two pointers eliminates the inner loop → O(n)

**Key Insight**
- If sum too small → move left pointer right (increase sum)
- If sum too big → move right pointer left (decrease sum)
- Works because array is sorted — moving pointers is deterministic

**Reusable Template**
```python
left, right = 0, len(arr) - 1
while left < right:
    current = arr[left] + arr[right]
    if current == target:
        # found
        left += 1
        right -= 1
    elif current < target:
        left += 1
    else:
        right -= 1
```

**Common Mistakes**
- Forgetting to sort first
- Using `left < right` vs `left <= right` (usually `<` for pairs)
- Not handling duplicates when all unique pairs needed

**Problems Solved**
<!-- Added automatically by Algo Sensei -->

---

## Fast & Slow Pointers

**Trigger Words / Clues**
- "cycle in linked list", "find middle", "palindrome linked list"
- LinkedList problems where you need to detect loops or find midpoints

**Key Insight**
- Fast moves 2 steps, slow moves 1 step
- If cycle exists, they will meet
- When fast reaches end, slow is at middle

**Reusable Template**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:  # cycle detected
        break
```

**Common Mistakes**
- Not checking `fast.next` before `fast.next.next` → null pointer
- Confusing cycle detection with cycle start finding (need second phase)

**Problems Solved**
<!-- Added automatically by Algo Sensei -->

---

## Sliding Window

**Trigger Words / Clues**
- "contiguous subarray/substring", "longest/shortest with condition"
- "at most K distinct", "no repeating characters", "max sum subarray of size K"

**Brute Force → Why It's Slow**
- Check all subarrays → O(n²) or O(n³)
- Sliding window reuses previous computation → O(n)

**Key Insight**
- Expand right to grow window
- Shrink left when window violates condition
- Track window state with a hash map or counter

**Reusable Template**
```python
left = 0
window = {}  # or Counter
result = 0
for right in range(len(s)):
    # add s[right] to window
    window[s[right]] = window.get(s[right], 0) + 1
    # shrink while invalid
    while window_is_invalid(window):
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        left += 1
    # update result
    result = max(result, right - left + 1)
return result
```

**Common Mistakes**
- Forgetting to shrink the window (infinite loop)
- Off-by-one in window size: `right - left + 1`
- Not cleaning up zero-count entries from hash map

**Problems Solved**
<!-- Added automatically by Algo Sensei -->

---

## Binary Search

**Trigger Words / Clues**
- "sorted array", "find minimum X such that condition holds"
- "rotated sorted", "search in matrix", "koko eating bananas" type problems
- Any monotonic search space (not just arrays)

**Key Insight**
- Standard: find exact value
- Advanced: binary search on the *answer space* (minimize/maximize)
- Always ask: "Is my search space monotonic?"

**Reusable Template**
```python
# Standard
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: left = mid + 1
    else: right = mid - 1

# Answer space (find minimum valid X)
left, right = min_possible, max_possible
while left < right:
    mid = (left + right) // 2
    if condition(mid):
        right = mid      # mid works, try smaller
    else:
        left = mid + 1   # mid doesn't work, go bigger
return left
```

**Common Mistakes**
- `left + right // 2` instead of `left + (right - left) // 2` → overflow
- Wrong boundary: `left <= right` vs `left < right` depends on template
- Not identifying that it's an answer-space binary search

**Problems Solved**
<!-- Added automatically by Algo Sensei -->

---

## Kadane's Algorithm

**Trigger Words / Clues**
- "maximum subarray sum", "contiguous subarray", "max product subarray"

**Key Insight**
- At each index: extend current subarray OR start fresh
- Start fresh when `arr[i] > curr_sum + arr[i]` i.e. `curr_sum < 0`

**Reusable Template**
```python
max_sum = curr_sum = arr[0]
for i in range(1, len(arr)):
    curr_sum = max(arr[i], curr_sum + arr[i])
    max_sum = max(max_sum, curr_sum)
return max_sum
```

**Common Mistakes**
- Initializing `max_sum = 0` breaks for all-negative arrays
- Forgetting to handle empty array

**Problems Solved**
<!-- Added automatically by Algo Sensei -->

---

## Prefix Sum

**Trigger Words / Clues**
- "subarray sum equals K", "range sum query", "number of subarrays with sum"
- Need to answer multiple range queries efficiently

**Key Insight**
- `sum(l, r) = prefix[r+1] - prefix[l]`
- Build once O(n), answer each query O(1)
- Combined with hash map: find subarrays with exact sum

**Reusable Template**
```python
prefix = [0] * (len(arr) + 1)
for i, v in enumerate(arr):
    prefix[i+1] = prefix[i] + v
# query
def range_sum(l, r):
    return prefix[r+1] - prefix[l]
```

**Common Mistakes**
- Off-by-one: `prefix[r+1] - prefix[l]` not `prefix[r] - prefix[l]`
- Forgetting `prefix[0] = 0` base case

**Problems Solved**
<!-- Added automatically by Algo Sensei -->

---

<!-- More patterns will be added as you solve problems -->
<!-- Patterns not yet encountered: Merge Intervals, Cyclic Sort, Stack, Hash Maps, -->
<!-- Graph BFS/DFS, Two Heaps, Subsets, Top K, Greedy, DP, Backtracking, Trie, -->
<!-- Topological Sort, Union Find, Ordered Set, Bitwise XOR -->
