class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res
        