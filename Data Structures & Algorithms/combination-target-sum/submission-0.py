class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start_idx, cur_sum, cur_nums):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur_nums.copy())
                return

            for i in range(start_idx, len(nums)):
                cur_nums.append(nums[i])
                dfs(i, cur_sum+nums[i], cur_nums)
                cur_nums.pop()
                
        
        dfs(0, 0, [])
        
        return res