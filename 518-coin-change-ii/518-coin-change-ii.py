class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0 for i in range(amount + 1)] for j in range(N + 1)]
        for i in range(N+1):
            dp[i][0] = 1
        
        for i in range(1, N + 1):
            for j in range(amount + 1):
                if j + coins[i-1] <= amount:
                    dp[i][j + coins[i-1]] += (dp[i][j])
                if i + 1 <= N:
                        dp[i+1][j] = dp[i][j]
        return dp[N][amount]
        