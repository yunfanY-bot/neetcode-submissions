class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        cur_set = set()
        res = 0
        while r < len(s):
            if s[r] in cur_set:
                while s[l] != s[r]:
                    cur_set.remove(s[l])
                    l += 1
                l += 1
            cur_set.add(s[r])
            r += 1
            res = max(res, r-l)
        return res


            
