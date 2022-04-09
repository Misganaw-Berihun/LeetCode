class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(i, prev, is_bought):
            nonlocal n
            ans = 0
            if i == n - 1:
                if prev == "b" or (prev == "j" and is_bought):
                    ans = max(ans, prices[i])#sell
                return ans
            
            sell = dp(i + 1, "s", False) + prices[i]
            buy = dp(i + 1, "b", True) - prices[i]
            jmp = dp(i + 1, "j", is_bought)
            
            if prev == "s":
                ans = max(ans, jmp)
            elif prev == "b":
                ans = max(ans, sell, jmp)
            elif prev == "j":
                if is_bought:
                    ans = max(ans, sell, jmp)
                else:
                    ans = max(ans, jmp, buy)
            return ans
        
        return dp(0, "j", False)
                
            
            
                    
        