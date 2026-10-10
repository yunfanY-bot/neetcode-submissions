class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s,p = 0,1,0
        while s < len(prices):
            if prices[s] > prices[b]:
                p = max(p, prices[s] - prices[b])
            else:
                b = s
            s+=1
        return p


        