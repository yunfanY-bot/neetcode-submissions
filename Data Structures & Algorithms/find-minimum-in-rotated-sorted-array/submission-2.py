class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2 - 1

        if nums[0] > nums[mid]:
            return self.findMin(nums[1:mid+1])
        elif nums[mid]>nums[-1]:
            return self.findMin(nums[mid+1:])
        else:
            return nums[0]


        

        