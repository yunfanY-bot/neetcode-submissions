class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Finds the root of x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        # Connects x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            return True
        return False

class Solution:
    # Implementation for Kruskal's algorithm to compute Minimum Spanning Trees
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key = lambda edge:edge[2])
        total = 0
        components = n
        union_find = UnionFind(n)
        for u,v,w in edges:
            if components == 1:
                break
            if union_find.find(u) == union_find.find(v):
                continue
            union_find.union(u, v)
            total+=w
            components-=1
        return total if components == 1 else -1
            



