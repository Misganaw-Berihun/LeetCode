class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        
        if n >= 1:
            dp[1] = 1
        
        if n >= 2:
            dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = 2 * dp[i-1] + dp[i-3]

        return dp[n] % 1_000_000_007