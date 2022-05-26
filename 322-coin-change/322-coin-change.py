class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(target):
            if target in memo:
                return memo[target]
            if target == 0:
                return 0
            if target < 0:
                return  target

            shortest = float('inf')
            for i in range(len(coins)):
                rec = dp(target - coins[i])
                if coins[i] <= target and rec >= 0:
                        shortest = min(shortest, rec + 1)
            memo[target] = shortest
            return shortest
        memo = {}
        ans = dp(amount)
        if ans == float('inf'):
            return  -1
        return ans