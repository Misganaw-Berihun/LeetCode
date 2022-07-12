class Solution:
    def minSteps(self, n: int) -> int:
        def dp(copied, m):
            if m == n:
                return 0
            
            if m > n:
                return float("inf")
            
            if (copied, m) in memo:
                return memo[(copied, m)]
            
            copy = dp(m, m + m) + 1
            paste = dp(copied, m + copied)
            memo[(copied, m)] = 1 + min(copy, paste)
            return memo[(copied, m)]
        
        memo = {}
        if n == 1:
            return 0
        return dp(1, 1) + 1