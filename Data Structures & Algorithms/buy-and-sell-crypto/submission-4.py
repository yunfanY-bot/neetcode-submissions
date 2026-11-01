class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        min_b=prices[0]
        for i in range(len(prices)):
            if prices[i] < min_b:
                min_b = prices[i]
            p = max(p, prices[i]-min_b)
        return p



        