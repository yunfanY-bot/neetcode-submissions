class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            graph[src].append(dst)
        def has_cycle(node):
            if node in visited:
                return False
            if node in visiting:
                return True
            visiting.add(node)
            for nei in graph[node]:
                if has_cycle(nei):
                    return True
            visited.add(node)
            return False
        visited = set()
        for i in range(numCourses):
            visiting = set()
            if i not in visited:
                if has_cycle(i):
                    return False
        return True
