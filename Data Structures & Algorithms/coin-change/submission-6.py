"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        cur_num = 0
        def dfs(cur_total):
            if cur_total == amount:
                return 0
            if cur_total > amount:
                return float('inf')
            res = float('inf')
            for coin in coins:
                res = min(res, 1+dfs(cur_total+coin))
            return res
        res = dfs(0)
        return -1 if res == float('inf') else res
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        return -1 if dp[-1] == float('inf') else dp[-1]




