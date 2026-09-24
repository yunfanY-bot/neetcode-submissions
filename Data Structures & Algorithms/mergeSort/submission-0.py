# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        if n==1 or n==0:
            return pairs
        res = []
        a = self.mergeSort(pairs[: n//2])
        b = self.mergeSort(pairs[n//2:])


        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i].key <= b[j].key:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1

        while i < len(a):
            res.append(a[i])
            i+=1
        while j < len(b):
            res.append(b[j])
            j+=1
        return res
