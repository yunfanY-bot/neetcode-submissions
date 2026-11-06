class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cur_set = set()
        res = 0
        for r in range(len(s)):
            while s[r] in cur_set:
                cur_set.remove(s[l])
                l += 1
            cur_set.add(s[r])
            res = max(res, r-l+1)
        return res


            
