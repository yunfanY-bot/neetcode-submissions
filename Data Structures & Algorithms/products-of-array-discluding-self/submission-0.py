class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]
        post_fix = [1]
        output = []

        for i in range(1, len(nums)):
            pref.append(pref[i-1]*nums[i-1])

        for i in range(len(nums)-2, -1, -1): 
            post_fix.append(post_fix[len(nums)-2-i]*nums[i+1])

        for pre, post in zip(pref, reversed(post_fix)):
            output.append(pre*post)

        return output



        