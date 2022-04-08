class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(step):
            nonlocal memo
            if step in memo:
                return memo[step]
            if step == 0 or step == 1:
                return cost[step]
            memo[step] = cost[step] + min(dp(step - 1), dp(step - 2))
            return memo[step]
        memo = {}
        return min(dp(len(cost) - 1) , dp(len(cost) - 2))
            
            
            
        