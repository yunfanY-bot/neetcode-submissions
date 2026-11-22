from functools import lru_cache

class Solution:
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+3)
        dp[0] = 0
        dp[1] = 0

        for i in range(3, n+3):
            dp[i] = dp[i-1]+dp[i-2]

        print(dp)
        return dp[-1]
        