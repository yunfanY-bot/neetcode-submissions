class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        n_row = len(grid)
        n_col = len(grid[0])
        if grid[0][0] == 1 or grid[n_row - 1][n_col - 1] == 1:
            return -1
        q = deque()
        q.append((0, 0)) 
        visited = set()
        visited.add((0,0))

        dist = 0
        while q:
            for _ in range(len(q)):
                point = q.popleft()
                i, j = point[0], point[1]
                if i == n_row-1 and j == n_col-1:
                    return dist
                for d in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    nei_i = i+d[0]
                    nei_j = j+d[1]
                    if nei_i < 0 or nei_i >= n_row or nei_j < 0 or nei_j >= n_col:
                        continue
                    if (nei_i, nei_j) in visited:
                        continue
                    if grid[nei_i][nei_j] == 1:
                        continue

                    q.append((nei_i, nei_j))
                    visited.add((nei_i, nei_j))

            dist += 1

        return -1

        