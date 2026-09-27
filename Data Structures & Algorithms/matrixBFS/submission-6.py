class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        n_row = len(grid)
        n_col = len(grid[0])

        q = deque()
        q.append((0, 0))
        visited = set()

        dist = 0
        while q:
            for _ in range(len(q)):
                point = q.popleft()
                
                i, j = point[0], point[1]
                if i < 0 or i >= n_row or j < 0 or j >= n_col:
                    continue
                if point in visited:
                    continue
                if grid[i][j] == 1:
                    continue
                if i == n_row-1 and j == n_col-1:
                    return dist
                visited.add(point)
                for d in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    q.append((i+d[0], j+d[1]))
            dist += 1

        return -1

        