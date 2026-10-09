class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for cha in s:
            dict_s[cha]+=1
        for cha in t:
            dict_t[cha]+=1
        return dict_s==dict_t


        