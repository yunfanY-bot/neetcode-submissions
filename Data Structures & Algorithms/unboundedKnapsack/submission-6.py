from functools import lru_cache

class Solution:
    """
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        @lru_cache
        def dfs(cur_weight):
            res = 0
            for i in range(n):
                if cur_weight+weight[i]<=capacity:
                    res = max(res, profit[i] + dfs(cur_weight+weight[i]))
            return res

        return dfs(0)
    """
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [0]*(capacity+1)
        dp[0] = 0
        for c in range(0, capacity+1):
            for i in range(n):
                if weight[i]<=c:
                    dp[c] = max(dp[c], profit[i]+dp[c-weight[i]])
        return dp[-1]
