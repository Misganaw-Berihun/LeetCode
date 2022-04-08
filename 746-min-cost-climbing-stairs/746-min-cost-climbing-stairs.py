class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        temp = 0
        dp = [0 for i in range(n)]            
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i - 2] , dp[i - 1]) + cost[i]
        return min(dp[n - 1], dp[n - 2])
            
            
            
            
        