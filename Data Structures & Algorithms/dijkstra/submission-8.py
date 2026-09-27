class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        unvisited = set(i for i in range(n))
        dist = {}
        for i in range(n):
            dist[i] = [float('inf'), None]
        dist[src] = [0, None] 

        while unvisited:
            print(unvisited)
            cur = self.findmin_node(unvisited, dist)
            for edge in edges:
                if edge[0] == cur:
                    if dist[edge[1]][0] > dist[cur][0] + edge[2]:
                        dist[edge[1]][0] = dist[cur][0]+edge[2]
                        dist[edge[1]][1] = cur
            unvisited.remove(cur)
        
        to_return = {}
        for key in dist.keys():
            if dist[key][0] == float('inf'):
                to_return[key] = -1
            else:
                to_return[key] = dist[key][0]
        return to_return

    def findmin_node(self, unvisited, dist):
        min_dist = float('inf')
        min_node = list(unvisited)[0]
        for node in unvisited:
            if dist[node][0] < min_dist:
                min_dist = dist[node][0]
                min_node = node
        return min_node

 
