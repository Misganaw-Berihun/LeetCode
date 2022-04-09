class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        temp = [0 for i in range(n)]
        temp[n - 1] = prices[n- 1]
        ans = temp[n - 1] - prices[n - 1]
        
        for i in range(n - 2,  -1, -1):
            temp[i] = max(temp[i + 1] , prices[i])
            ans = max(ans, temp[i] - prices[i])
            
        return ans
            
        