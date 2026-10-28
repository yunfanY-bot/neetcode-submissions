from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        # Pacific seeds: top row + left column
        q = deque()
        for c in range(n):
            pac[0][c] = True
            q.append((0, c))
        for r in range(m):
            if not pac[r][0]:
                pac[r][0] = True
                q.append((r, 0))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n
                        and not pac[nr][nc]
                        and heights[nr][nc] >= heights[r][c]):
                    pac[nr][nc] = True
                    q.append((nr, nc))

        # Atlantic seeds: bottom row + right column
        q = deque()
        for c in range(n):
            atl[m - 1][c] = True
            q.append((m - 1, c))
        for r in range(m):
            if not atl[r][n - 1]:
                atl[r][n - 1] = True
                q.append((r, n - 1))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n
                        and not atl[nr][nc]
                        and heights[nr][nc] >= heights[r][c]):
                    atl[nr][nc] = True
                    q.append((nr, nc))

        res = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res