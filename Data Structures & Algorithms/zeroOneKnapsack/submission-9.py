from functools import lru_cache

class Solution:
    """
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)

        @lru_cache(None)
        def dfs(i, cur_cap):
            if i >= n:
                return 0
            # include current item
            res = 0 
            if cur_cap-weight[i]>=0:
                res = dfs(i+1, cur_cap-weight[i]) + profit[i]
            # exclude current item
            res = max(dfs(i+1, cur_cap), res)
            return res

        return dfs(0, capacity)
    """
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N+1)]

        # Fill the first column and row to reduce edge cases
        for i in range(N+1):
            dp[i][0] = 0
        for c in range(M + 1):
            dp[0][c] = 0
        for i in range(1, N+1):
            for c in range(1, M + 1):
                skip = dp[i-1][c]
                include = 0
                if c - weight[i-1] >= 0:
                    include = profit[i-1] + dp[i-1][c - weight[i-1]]
                dp[i][c] = max(include, skip)
        return dp[N][M]
        