class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        res = 0
        i = 0
        cur_length = 0
        while i < len(nums)-1:
            if nums[i]+1 == nums[i+1]:
                cur_length += 1
                i+=1
                res = max(res, cur_length)
            elif nums[i] == nums[i+1]:
                i+=1
            else:
                res = max(res, cur_length)
                cur_length = 0
                i+=1
        return res+1
        
            

        