from functools import lru_cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [0] * (capacity + 1)
        dp[0] = 0

        for c in range(1, capacity + 1):
            res = 0
            for i in range(n):
                if weight[i] <= c:
                    res = max(res, profit[i] + dp[c - weight[i]])
            dp[c] = res
        return dp[-1]