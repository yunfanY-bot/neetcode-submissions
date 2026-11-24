from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for c in range(len(s)):
            for i, j in ((c,c), (c,c+1)):
                while i>=0 and j < len(s) and s[i] == s[j]:
                    res += 1
                    i -= 1
                    j += 1
        return res

            

        