class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i, prev, trans, memo = {}):
            if (i, prev, trans) in memo:
                return memo[(i, prev, trans)]
            if i >= len(prices) or trans == 2:
                return 0
            ans = 0
            if prev == 1:
                ans = max(dp(i + 1, 1, trans, memo), dp(i + 1, 0, trans + 1, memo) + prices[i])
            else:
                ans = max(dp(i + 1, 0, trans, memo), dp(i + 1, 1, trans, memo) -  prices[i])
            memo[(i, prev, trans)] = ans
            return ans
        return dp(0, 0, 0)
        
        