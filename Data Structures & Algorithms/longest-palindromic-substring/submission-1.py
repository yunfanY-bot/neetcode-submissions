class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_word = ""
        for i in range(len(s)):
            l=r=i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > res:
                    res = (r-l+1)
                    res_word = s[l:r+1]
                res = max(l-r+1, res)
                l-=1
                r+=1
            m = i
            n = i+1
            while m>=0 and n < len(s) and s[m] == s[n]:
                if (n-m+1) > res:
                    res = (n-m+1)
                    res_word = s[m:n+1]
                res = max(n-m+1, res)
                m-=1
                n+=1
        return res_word

        