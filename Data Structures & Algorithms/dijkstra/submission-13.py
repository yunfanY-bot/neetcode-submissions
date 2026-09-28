class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {}
        heap = [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:          
                continue
            dist[u] = d
            for v, w in adj[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))

        return {i: dist.get(i, -1) for i in range(n)}
        
