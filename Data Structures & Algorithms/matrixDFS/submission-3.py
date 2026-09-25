class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.cp_helper(grid, 0, 0, set())

    def cp_helper(self, grid, i, j, visited):

        if not grid or len(grid) == 0:
            return 0
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited:
            return 0

        if grid[i][j] == 1:
            return 0
        if i == len(grid)-1 and j == len(grid[0])-1:
            return 1
        count = 0 
        visited.add((i, j))

        count = self.cp_helper(grid, i+1, j, visited) + self.cp_helper(grid, i, j+1, visited) + self.cp_helper(grid, i-1, j, visited) + self.cp_helper(grid, i, j-1, visited)

        visited.remove((i,j))
        
        return count

        
        
        