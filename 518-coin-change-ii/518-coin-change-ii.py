class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp (cur, amt_left):
            if (cur, amt_left) in memo:
                return memo[(cur, amt_left)]
            
            if amt_left < 0:
                return 0
            if amt_left == 0:
                return 1
            
            ways = 0
            for i in range(cur, len(coins)):
                ways += dp(i, amt_left - coins[i])
            memo[(cur, amt_left)] = ways
            return ways
        memo = {}
        coins.sort(reverse=True)
        return dp(0, amount)
        