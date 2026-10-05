class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)

        memo = {}
        def dfs(i, cur_cap):
            if (i, cur_cap) in memo:
                return memo[(i, cur_cap)]
            if i >= n:
                return 0
            # include current item
            res = 0 
            if cur_cap-weight[i]>=0:
                res = dfs(i+1, cur_cap-weight[i]) + profit[i]
            # exclude current item
            res = max(dfs(i+1, cur_cap), res)
            memo[(i, cur_cap)]=res
            return res

        return dfs(0, capacity)