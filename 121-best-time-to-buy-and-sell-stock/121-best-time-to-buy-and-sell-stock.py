class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_sofar = prices[n- 1]
        ans = 0

        for i in range(n - 2,  -1, -1):
            max_sofar = max(max_sofar , prices[i])
            ans = max(ans, max_sofar - prices[i])
            
        return ans
            
        