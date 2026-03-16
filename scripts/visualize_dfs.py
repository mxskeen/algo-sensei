"""
DFS (Depth-First Search) Visualizer — recursive graph traversal with call stack
Usage: python visualize_dfs.py
"""
import time
from collections import defaultdict

def visualize_dfs(graph, start, delay=0.7):
    visited = set()
    dfs_order = []
    call_stack = []

    print(f"\n{'='*50}")
    print(f"  DFS Traversal  |  Start node: {start}")
    print(f"  Graph: {dict(graph)}")
    print(f"{'='*50}")

    def render_stack():
        if call_stack:
            print(f"  Call stack (top = current): {call_stack}")
        else:
            print(f"  Call stack: []")

    def dfs(node, depth):
        visited.add(node)
        dfs_order.append(node)
        call_stack.append(node)

        indent = "  " + "  " * depth
        print(f"\n{indent}→ Visit {node}  (depth {depth})")
        render_stack()
        print(f"  Visited so far: {dfs_order}")
        time.sleep(delay)

        unvisited = [n for n in graph[node] if n not in visited]
        if unvisited:
            print(f"{indent}  Neighbors to explore: {unvisited}")
        else:
            print(f"{indent}  No unvisited neighbors — backtrack")

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, depth + 1)

        call_stack.pop()
        print(f"\n{indent}← Return from {node}  (backtrack)")
        render_stack()
        time.sleep(delay / 2)

    dfs(start, 0)

    print(f"\n{'='*50}")
    print(f"  DFS Order: {dfs_order}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    print("DFS Visualizer")
    print("--------------")
    print("Enter edges one per line (e.g. '1 2' means edge from 1 to 2).")
    print("Press Enter twice when done.\n")

    graph = defaultdict(list)
    nodes = set()

    while True:
        line = input("Edge (or blank to finish): ").strip()
        if not line:
            break
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)
        nodes.add(u)
        nodes.add(v)

    for node in list(nodes):
        if node not in graph:
            graph[node] = []

    start = int(input("Start node: ").strip())
    visualize_dfs(graph, start)
