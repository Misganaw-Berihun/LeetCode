class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def dp(i, prev, memo = {}):
            if i >= len(prices):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            if prev == 'B':
                memo[(i, prev)] =  max(prices[i] + dp(i + 1, 'S') - fee, dp(i + 1, 'B'))
            elif prev == 'S':
                memo[(i, prev)] = max(-prices[i] + dp(i + 1, 'B') , dp(i + 1, 'S'))
            return memo[(i, prev)]
            
        return dp(0, "S");
            
        