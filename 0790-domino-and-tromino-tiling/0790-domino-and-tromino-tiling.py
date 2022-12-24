class Solution:
    def mul(self, num1, num2):
        return (num1 * num2) % self.MOD

    def add(self, num1, num2):
        res = num1 + num2
        if res >= self.MOD:
            res -= self.MOD
        return res
    
    def numTilings(self, n: int) -> int:
        self.MOD = 1_000_000_007
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = self.add(dp[i], self.add(dp[i - 1], dp[i - 2]))
            for j in range(3, n + 1):
                if i >= j:
                    dp[i] = self.add(dp[i], self.mul(dp[i - j], 2))
        
        return dp[n] 