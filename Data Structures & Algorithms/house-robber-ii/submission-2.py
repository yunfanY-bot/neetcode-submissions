from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache()
        def r(i, first):
            if i >= len(nums):
                return 0
            if first and i == len(nums)-1:
                return 0
            return max(nums[i] + r(i+2, first), r(i+1, first))
        if len(nums) == 1:
            return nums[0]
        return max(r(0, True), r(1, False))
        
        