class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, prev):
            if i >= len(prices):
                return 0
            if prev == 'B':
                return max(prices[i] + dp(i + 1, 'S') - fee, dp(i + 1, 'B'))
            elif prev == 'S':
                return max(-prices[i] + dp(i + 1, 'B') , dp(i + 1, 'S'))
            
        return dp(0, "S");
            
        