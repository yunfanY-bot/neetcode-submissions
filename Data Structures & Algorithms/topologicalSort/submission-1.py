class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)

        res = []
        visited = set()
        visiting = set()

        def dfs(n):
            if n in visited:
                return True
            if n in visiting:
                return False


            visiting.add(n)
            for nei in adj[n]:
                if not dfs(nei):
                    return False
            visiting.remove(n)
            res.append(n)
            visited.add(n)
            return True

        for i in range(n):
            if not dfs(i):
                return []
        res.reverse()
        return res


    


        