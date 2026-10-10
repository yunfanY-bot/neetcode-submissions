class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b = 0
        for i in range(len(prices)):
            p = max(p, prices[i]-prices[b])
            if prices[i] < prices[b]:
                b = i
        return p




        