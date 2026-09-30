class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        adj2 = defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])


        total = 0

        heap = []
        visited = set()
        visited.add(0)

        for v, w in adj[0]:
            heapq.heappush(heap, (w, v))
        while heap:
            w, v = heapq.heappop(heap)
            if v not in visited:
                visited.add(v)
                total+=w
                for v, w in adj[v]:
                    heapq.heappush(heap, (w, v))

        if len(visited) < n:
            return -1
        return total



        
        