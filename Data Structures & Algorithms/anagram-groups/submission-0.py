class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            d = [0] * 26
            for char in word:
                d[ord(char)-97]+=1
            res[tuple(d)].append(word)
        return list(res.values())
        