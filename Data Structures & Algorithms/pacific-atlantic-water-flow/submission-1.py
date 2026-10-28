from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_row, n_col = len(heights), len(heights[0])
        res = []

        p_queue = deque()
        a_queue = deque()

        p = set()
        a = set()

        for n in range(n_col):
            p_queue.append((0, n))
            a_queue.append((n_row-1, n))
        for m in range(n_row):
            p_queue.append((m, 0))
            a_queue.append((m, n_col-1))
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()
        while p_queue:
            cur0, cur1 = p_queue.popleft()
            visited.add((cur0, cur1))
            p.add((cur0, cur1))
            for d0, d1 in d:
                if 0<=d0+cur0<n_row and 0<=d1+cur1<n_col and (d0+cur0, d1+cur1) not in visited and heights[d0+cur0][d1+cur1] >= heights[cur0][cur1]:
                    p_queue.append((d0+cur0, d1+cur1))

        visited = set()
        while a_queue:
            cur0, cur1 = a_queue.popleft()
            visited.add((cur0, cur1))
            a.add((cur0, cur1))
            for d0, d1 in d:
                if 0<=d0+cur0<n_row and 0<=d1+cur1<n_col and (d0+cur0, d1+cur1) not in visited and heights[d0+cur0][d1+cur1] >= heights[cur0][cur1]:
                    a_queue.append((d0+cur0, d1+cur1))

        return list(p.intersection(a))


