"""
BFS (Breadth-First Search) Visualizer — level-by-level graph traversal
Usage: python visualize_bfs.py
"""
import time
from collections import deque, defaultdict

def visualize_bfs(graph, start, delay=0.8):
    visited = set()
    queue = deque([start])
    visited.add(start)
    level = 0

    print(f"\n{'='*50}")
    print(f"  BFS Traversal  |  Start node: {start}")
    print(f"  Graph: {dict(graph)}")
    print(f"{'='*50}")

    bfs_order = []

    while queue:
        level_size = len(queue)
        level_nodes = []

        print(f"\n--- Level {level} ---")
        print(f"  Queue: {list(queue)}")

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node)
            bfs_order.append(node)

            print(f"\n  Dequeue: {node}")
            print(f"  Neighbors of {node}: {graph[node]}")

            new_neighbors = []
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    new_neighbors.append(neighbor)

            if new_neighbors:
                print(f"  → Enqueue unvisited: {new_neighbors}")
            else:
                print(f"  → No new neighbors to enqueue")

            time.sleep(delay / 2)

        print(f"\n  Level {level} nodes: {level_nodes}")
        print(f"  Visited so far: {bfs_order}")
        print(f"  Queue after level: {list(queue)}")
        level += 1
        time.sleep(delay)

    print(f"\n{'='*50}")
    print(f"  BFS Order: {bfs_order}")
    print(f"  Total levels: {level}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    print("BFS Visualizer")
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

    # ensure all nodes exist in graph even if no outgoing edges
    for node in list(nodes):
        if node not in graph:
            graph[node] = []

    start = int(input("Start node: ").strip())
    visualize_bfs(graph, start)
