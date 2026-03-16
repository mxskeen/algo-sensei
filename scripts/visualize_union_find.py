"""
Union Find (Disjoint Set Union) Visualizer — union by rank + path compression
Usage: python visualize_union_find.py
"""
import time

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x, path=[]):
        path.append(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x], path)  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x, []), self.find(y, [])
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True


def render_uf(uf, n):
    print(f"\n  Node:   " + "".join(f"{i:^5}" for i in range(n)))
    print(f"  Parent: " + "".join(f"{uf.parent[i]:^5}" for i in range(n)))
    print(f"  Rank:   " + "".join(f"{uf.rank[i]:^5}" for i in range(n)))

    # show components
    components = {}
    for i in range(n):
        root = uf.find(i, [])
        components.setdefault(root, []).append(i)
    print(f"\n  Components ({uf.components}):")
    for root, members in sorted(components.items()):
        print(f"    Root={root}: {members}")


def visualize_union_find(n, edges, delay=0.9):
    uf = UnionFind(n)

    print(f"\n{'='*55}")
    print(f"  Union Find Visualizer")
    print(f"  Nodes: {n}  |  Edges to process: {edges}")
    print(f"{'='*55}")
    print(f"\nKey ideas:")
    print(f"  find(x)  → find root of x's component (with path compression)")
    print(f"  union(x,y) → merge x and y's components (by rank)")

    print(f"\nInitial state (each node is its own component):")
    render_uf(uf, n)
    time.sleep(delay)

    for step, (u, v) in enumerate(edges, 1):
        print(f"\n--- Step {step}: union({u}, {v}) ---")

        path_u, path_v = [], []
        root_u = uf.find(u, path_u)
        root_v = uf.find(v, path_v)

        print(f"  find({u}): path = {path_u} → root = {root_u}")
        print(f"  find({v}): path = {path_v} → root = {root_v}")

        if root_u == root_v:
            print(f"  Same root ({root_u}) → already connected, skip")
            print(f"  ⚠️  This edge would create a CYCLE")
        else:
            merged = uf.union(u, v)
            if uf.rank[root_u] >= uf.rank[root_v]:
                print(f"  rank[{root_u}]={uf.rank[root_u]} >= rank[{root_v}] → {root_v} points to {root_u}")
            else:
                print(f"  rank[{root_v}]={uf.rank[root_v]} > rank[{root_u}] → {root_u} points to {root_v}")
            print(f"  ✅ Merged! Components: {uf.components}")

        render_uf(uf, n)
        time.sleep(delay)

    print(f"\n{'='*55}")
    print(f"  Final: {uf.components} connected component(s)")
    components = {}
    for i in range(n):
        root = uf.find(i, [])
        components.setdefault(root, []).append(i)
    for root, members in sorted(components.items()):
        print(f"  Component (root={root}): {members}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    print("Union Find Visualizer")
    print("---------------------")
    n = int(input("Number of nodes (0 to n-1): ").strip())
    print("Enter edges to union one per line as 'u v'. Press Enter twice when done.\n")

    edges = []
    while True:
        line = input("Edge (or blank to finish): ").strip()
        if not line:
            break
        u, v = map(int, line.split())
        edges.append((u, v))

    visualize_union_find(n, edges)
