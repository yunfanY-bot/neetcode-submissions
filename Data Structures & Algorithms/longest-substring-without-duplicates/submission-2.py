class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        cur_set = set()
        res = 0
        while r < len(s):
            if s[r] not in cur_set:
                cur_set.add(s[r])
                r+=1
            else:
                while s[l] != s[r]:
                    cur_set.remove(s[l])
                    l += 1
                cur_set.add(s[r])
                l += 1
                r += 1
            res = max(res, r-l)
        return res


            
