class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i, prev, trans):
            if (i, prev, trans) in memo:
                return memo[(i, prev, trans)]
            if i >= len(prices) or trans == 2:
                return 0
            ans = 0
            if prev == 1:
                ans = max(dp(i + 1, 1, trans), dp(i + 1, 0, trans + 1) + prices[i])
            else:
                ans = max(dp(i + 1, 0, trans), dp(i + 1, 1, trans) -  prices[i])
            memo[(i, prev, trans)] = ans
            return ans
        memo = {}
        return dp(0, 0, 0)
        
        