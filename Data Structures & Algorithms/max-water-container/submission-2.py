class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        res = (j-i) * min(heights[i], heights[j])
        while i<=j:
            cur_water= (j-i) * min(heights[i], heights[j])
            res = max(cur_water,res)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return res
