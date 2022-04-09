class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(i, prev, is_bought):
            nonlocal n
            ans = 0
            if i >= n:
                return ans
            
            sell = dp(i + 1, "s", False) + prices[i]
            buy = dp(i + 1, "b", True) - prices[i]
            jmp = dp(i + 1, "j", is_bought)
            
            if prev == "s":
                ans = max(ans, jmp)
            elif prev == "b":
                ans = max(sell, jmp)
            elif prev == "j":
                if is_bought:
                    ans = max(sell, jmp)
                else:
                    ans = max(jmp, buy)
            return ans
        
        return dp(0, "j", False)
                
            
            
                    
        