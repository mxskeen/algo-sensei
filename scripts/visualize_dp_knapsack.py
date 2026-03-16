"""
Dynamic Programming Visualizer — 0/1 Knapsack DP table fill
Usage: python visualize_dp_knapsack.py
"""
import time

def visualize_knapsack(weights, values, capacity, delay=0.5):
    n = len(weights)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    print(f"\n{'='*60}")
    print(f"  0/1 Knapsack DP  |  Capacity: {capacity}")
    print(f"  Items: {list(zip(weights, values))}  (weight, value)")
    print(f"{'='*60}")

    def render_table(highlight_row=None, highlight_col=None):
        # header
        header = f"  {'':>8} |"
        for w in range(capacity + 1):
            header += f" {w:>3}"
        print(f"\n{header}")
        print(f"  {'-'*8}-+" + "-" * (4 * (capacity + 1)))

        for i in range(n + 1):
            if i == 0:
                label = f"  {'no items':>8} |"
            else:
                label = f"  {'item'+str(i)+'(w='+str(weights[i-1])+')':>8} |"

            row = label
            for w in range(capacity + 1):
                val = dp[i][w]
                if i == highlight_row and w == highlight_col:
                    row += f"[{val:>2}]"
                else:
                    row += f" {val:>3}"
            print(row)

    print("\nInitial DP table (all zeros):")
    render_table()
    time.sleep(delay)

    for i in range(1, n + 1):
        item_weight = weights[i - 1]
        item_value = values[i - 1]

        print(f"\n--- Item {i}: weight={item_weight}, value={item_value} ---")

        for w in range(capacity + 1):
            # don't take item i
            dont_take = dp[i-1][w]

            if item_weight <= w:
                # take item i
                take = item_value + dp[i-1][w - item_weight]
                dp[i][w] = max(dont_take, take)
                decision = f"max(don't take={dont_take}, take={item_value}+dp[{i-1}][{w-item_weight}]={take}) = {dp[i][w]}"
            else:
                dp[i][w] = dont_take
                decision = f"can't fit (weight {item_weight} > capacity {w}) → {dont_take}"

            print(f"  dp[{i}][{w}] = {decision}")
            time.sleep(delay / 3)

        print(f"\nTable after item {i}:")
        render_table(highlight_row=i)
        time.sleep(delay)

    print(f"\n{'='*60}")
    print(f"  Maximum value: {dp[n][capacity]}")

    # backtrack to find which items were taken
    taken = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            taken.append(i)
            w -= weights[i-1]
    taken.reverse()
    print(f"  Items taken: {taken}  (item numbers, 1-indexed)")
    print(f"  Total weight: {sum(weights[i-1] for i in taken)}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    print("0/1 Knapsack DP Visualizer")
    print("--------------------------")
    n = int(input("Number of items: ").strip())
    weights = list(map(int, input(f"Weights ({n} values): ").strip().split()))
    values = list(map(int, input(f"Values ({n} values): ").strip().split()))
    capacity = int(input("Knapsack capacity: ").strip())
    visualize_knapsack(weights, values, capacity)
