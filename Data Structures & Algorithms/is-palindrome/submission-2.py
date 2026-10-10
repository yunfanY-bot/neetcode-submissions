class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alph = []
        for char in s:
            if ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
                s_alph.append(char)
            if ord('A') <= ord(char) <= ord('Z'):
                s_alph.append(char.lower())

        print(s_alph)
        i, j = 0, len(s_alph)-1
        while i <= j:
            if s_alph[i] != s_alph[j]:
                return False

            i+=1
            j-=1

        return True

        