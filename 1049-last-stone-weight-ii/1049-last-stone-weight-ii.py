class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def dp(start, last):
            if start == len(stones):
                if (last >= 0):
                    return last
                else:
                    return float('inf')
            if (start, last) in memo:
                return memo[(start, last)]
            memo[(start, last)] = min(
                    dp(start + 1, last + stones[start]),
                    dp(start + 1, last - stones[start])
                    )
            return memo[(start, last)]
        memo = {}
        return dp(0, 0)