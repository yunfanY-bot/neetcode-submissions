class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r) // 2
            res = min(res, nums[mid])
            
            if nums[l] > nums[mid]:
                r = mid - 1

            elif nums[mid] > nums[r]:
                l = mid + 1                                

        return res