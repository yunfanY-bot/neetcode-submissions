class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for dst, src in prerequisites:
            adj[src].append(dst)

        visited = set()
        visiting = set()
        def has_cycle(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            for dst in adj[node]:
                if has_cycle(dst):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        for i in range(numCourses):
            if i not in visited:
                if has_cycle(i):
                    return False
        return True