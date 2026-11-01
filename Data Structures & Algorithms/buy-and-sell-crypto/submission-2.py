class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b=prices[0]
        for i in range(len(prices)):
            if prices[i] < b:
                b = prices[i]
            p = max(p, prices[i]-b)
        return p



        