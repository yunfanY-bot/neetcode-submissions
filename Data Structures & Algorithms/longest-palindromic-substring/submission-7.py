from functools import lru_cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        @lru_cache(maxsize=None)
        def is_pali(l, r):
            if l >= r:
                return True
            return s[l] == s[r] and is_pali(l + 1, r - 1)

        start, best = 0, 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if j - i + 1 > best and is_pali(i, j):
                    start, best = i, j - i + 1
        return s[start:start + best]