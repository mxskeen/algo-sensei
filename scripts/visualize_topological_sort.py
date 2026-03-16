"""
Topological Sort Visualizer — Kahn's algorithm (BFS-based) with in-degree tracking
Usage: python visualize_topological_sort.py
"""
import time
from collections import defaultdict, deque

def visualize_topological_sort(graph, num_nodes, delay=0.8):
    # compute in-degrees
    in_degree = {i: 0 for i in range(num_nodes)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    print(f"\n{'='*55}")
    print(f"  Topological Sort (Kahn's Algorithm)")
    print(f"  Nodes: {num_nodes}  |  Edges: {dict(graph)}")
    print(f"{'='*55}")

    print(f"\nStep 1: Compute in-degrees")
    print(f"  (in-degree = number of prerequisites for each node)")
    for node in range(num_nodes):
        print(f"  Node {node}: in-degree = {in_degree[node]}")

    # find all nodes with in-degree 0
    queue = deque([n for n in range(num_nodes) if in_degree[n] == 0])
    print(f"\nStep 2: Start queue with all in-degree=0 nodes: {list(queue)}")
    time.sleep(delay)

    topo_order = []
    step = 3

    while queue:
        print(f"\n--- Step {step} ---")
        print(f"  Queue: {list(queue)}")

        node = queue.popleft()
        topo_order.append(node)
        print(f"  Dequeue node {node} → add to result")
        print(f"  Result so far: {topo_order}")

        neighbors = graph.get(node, [])
        if neighbors:
            print(f"  Reduce in-degree for neighbors of {node}: {neighbors}")
        else:
            print(f"  Node {node} has no outgoing edges")

        for neighbor in neighbors:
            in_degree[neighbor] -= 1
            print(f"    Node {neighbor}: in-degree {in_degree[neighbor]+1} → {in_degree[neighbor]}", end="")
            if in_degree[neighbor] == 0:
                print(f"  → enqueue {neighbor} ✅")
                queue.append(neighbor)
            else:
                print(f"  (still has prerequisites)")

        time.sleep(delay)
        step += 1

    print(f"\n{'='*55}")
    if len(topo_order) == num_nodes:
        print(f"  Topological Order: {topo_order}")
        print(f"  ✅ Valid — no cycle detected")
    else:
        print(f"  ❌ Cycle detected! Only processed {len(topo_order)}/{num_nodes} nodes")
        unprocessed = [n for n in range(num_nodes) if n not in topo_order]
        print(f"  Nodes in cycle: {unprocessed}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Topological Sort Visualizer")
    print("---------------------------")
    num_nodes = int(input("Number of nodes (0 to n-1): ").strip())
    print("Enter directed edges one per line as 'u v' (u must come before v)")
    print("Press Enter twice when done.\n")

    graph = defaultdict(list)

    while True:
        line = input("Edge (or blank to finish): ").strip()
        if not line:
            break
        u, v = map(int, line.split())
        graph[u].append(v)

    visualize_topological_sort(graph, num_nodes)
