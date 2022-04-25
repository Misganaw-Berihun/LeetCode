class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def dp(pos: int, bought: bool) -> int:
            if pos == len(prices):
                return 0  # base case

            max_profit = 0

            if not bought:
                # Buy stock
                max_profit = max(max_profit, dp(pos + 1, True) - prices[pos] - fee)
            else:
                # Sell stock
                max_profit = max(max_profit, dp(pos + 1, False) + prices[pos])

            # Do nothing
            max_profit = max(max_profit, dp(pos + 1, bought))

            return max_profit

        return dp(0, False)