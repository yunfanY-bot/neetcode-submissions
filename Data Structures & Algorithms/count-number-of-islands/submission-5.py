class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])

        q = deque()
        res = 0

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == "1":
                    res += 1
                    q.append((i, j))
                    grid[i][j] = "0"
                    while q:
                        # bfs
                        cur0, cur1 = q.popleft()
                        for d0, d1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if 0<=d0+cur0<n_row and 0<=d1+cur1<n_col and grid[d0+cur0][d1+cur1] == "1":
                                q.append((cur0+d0, cur1+d1))
                                grid[cur0+d0][cur1+d1] = "0"
        return res
