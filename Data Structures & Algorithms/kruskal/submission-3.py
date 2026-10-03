class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # At the start, every vertex is in its own group
        group = list(range(n))

        # Look at the cheapest edges first
        edges.sort(key=lambda edge: edge[2])

        total_cost = 0
        edges_used = 0
        for u, v, weight in edges:
            # Same group means already connected, so this edge would make a cycle
            if group[u] == group[v]:
                continue

            # Use this edge
            total_cost += weight
            edges_used += 1

            # Join the two groups: everyone in v's group moves to u's group
            old_group = group[v]
            new_group = group[u]
            for i in range(n):
                if group[i] == old_group:
                    group[i] = new_group

        # A spanning tree on n vertices always has exactly n - 1 edges
        if edges_used != n - 1:
            return -1
        return total_cost