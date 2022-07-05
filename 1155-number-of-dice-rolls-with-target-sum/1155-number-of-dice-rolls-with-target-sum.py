class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def dp(rolls, sumTotal):
            if (rolls, sumTotal) in memo:
                return memo[(rolls, sumTotal)]
            
            if rolls == 0 and sumTotal == 0:
                return 1
            
            if rolls == 0 or sumTotal < 0:
                return 0
            
            ways = 0
            for i in range(1, k + 1):
                ways += dp(rolls - 1, sumTotal - i)
            memo[(rolls, sumTotal)] = ways
            return ways
        
        memo = {}
        return dp(n, target)  % (1000000007)