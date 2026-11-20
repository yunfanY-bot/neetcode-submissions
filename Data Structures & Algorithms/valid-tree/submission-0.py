

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        count = 0
        visited = set()
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            nonlocal count
            if node in visited:
                return False
            visited.add(node)
            count += 1
            for nei in graph[node]:
                if nei !=  parent:
                    if not dfs(nei, node):
                        return False
            return True
        res = dfs(0, None)
        print(count)
        print(res)

        return res and count == len(edges)+1
        