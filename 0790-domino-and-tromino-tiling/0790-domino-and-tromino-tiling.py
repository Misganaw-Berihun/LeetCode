class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] += (dp[i - 1] + dp[i - 2])
            for j in range(3, i + 1):
                if i >= j:
                    dp[i] += (dp[i - j] * 2)
        
        return dp[n] % 1_000_000_007