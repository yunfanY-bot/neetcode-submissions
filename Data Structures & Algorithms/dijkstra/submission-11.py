class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        visited = set()
        dist = {}

        for i in range(n):
            dist[i] =float('inf')
        dist[src] = 0
        heap = [(0, src)] 

        while heap:
            _, u = heapq.heappop(heap)
            visited.add(u)
            for edge in adj[u]:
                v, w = edge[0], edge[1]
                if v not in visited:
                    dist[v] = min(dist[v], dist[u]+w)
                    heapq.heappush(heap, (dist[v], v))
        for key in dist.keys():
            if dist[key] == float('inf'):
                dist[key] = -1
        return dist
        
