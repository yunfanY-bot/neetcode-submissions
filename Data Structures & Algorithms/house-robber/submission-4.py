"""
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def rob(n):
            if n >= len(nums):
                return 0
            return max(nums[n] + rob(n+2), rob(n+1))

        return rob(0)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+2)
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], nums[i-2]+dp[i-2])
        return dp[-1]
        