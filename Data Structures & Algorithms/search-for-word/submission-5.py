class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n_row = len(board)
        n_col = len(board[0])

        def dfs(cur_word, coor):
            if coor in visited:
                return False
            if coor[0]>=n_row or coor[0] < 0 or coor[1]>=n_col or coor[1]<0:
                return False

            if not word.startswith(cur_word):
                return False

            if cur_word+board[coor[0]][coor[1]] == word:
                return True

            # explore neighbour
            
            for d0, d1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                visited.add((coor[0], coor[1]))
                if dfs(cur_word+board[coor[0]][coor[1]], (coor[0]+d0, coor[1]+d1)):
                    return True
                visited.remove((coor[0], coor[1]))
            return False


        for i in range(n_row):
            for j in range(n_col):
                if dfs("", (i, j)):
                    return True
        return False

        

        
