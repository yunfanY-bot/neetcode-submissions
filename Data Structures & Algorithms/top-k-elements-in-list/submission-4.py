class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}
        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0) 

        heap = []
        for key,val in num_dict.items():
            heapq.heappush_max(heap, (val,key))
        res = []
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        return res
        

        
        