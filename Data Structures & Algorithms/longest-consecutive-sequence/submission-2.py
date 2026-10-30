class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        res = 0
        cur_length = 0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                cur_length += 1
                res = max(res, cur_length)
            elif nums[i] == nums[i+1]:
                continue
            else:
                res = max(res, cur_length)
                cur_length = 0
        return res+1
        
            

        