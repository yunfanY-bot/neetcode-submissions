"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def r(i, first):
            if i >= len(nums):
                return 0
            if first and i == len(nums)-1:
                return 0
            return max(nums[i] + r(i+2, first), r(i+1, first))
        if len(nums) == 1:
            return nums[0]
        return max(r(0, True), r(1, False))
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[0]*(len(nums)+2), [0]*(len(nums)+2)]

        for i in range(2):
            if i == 0:
                for j in range(2, len(dp[i])-1):
                    dp[i][j] = max(dp[i][j-2]+nums[j-2], dp[i][j-1])
            if i == 1:
                for j in range(3, len(dp[i])):
                    dp[i][j] = max(dp[i][j-2]+nums[j-2], dp[i][j-1])

        return max(dp[0][-2], dp[1][-1])
        