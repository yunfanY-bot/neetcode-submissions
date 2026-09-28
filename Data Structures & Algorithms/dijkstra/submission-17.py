class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        visited = set()
        dist = {}
        dist[src]=0
        heap = [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            for v, w in adj[u]:
                if v not in visited and d + w < dist.get(v, float('inf')):
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        
        return {i: dist.get(i, -1) for i in range(n)}