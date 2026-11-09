class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        all_char = set(s)
        for char in all_char:
            remaining_k = k
            l = 0
            for r in range(len(s)):
                if s[r] != char:
                    remaining_k -= 1
                while remaining_k < 0:
                    if s[l] != char:
                        remaining_k += 1
                    l += 1
                res = max(res, r-l+1)
        return res