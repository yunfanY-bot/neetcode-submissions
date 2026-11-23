from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def rob(n):
            if n >= len(nums):
                return 0
            return max(nums[n] + rob(n+2), rob(n+1))

        return rob(0)

        