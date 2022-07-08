class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        def dp(pos, steps_left):
            if (pos, steps_left) in memo:
                return memo[(pos, steps_left)]
            if pos < 0 or pos >= arrLen:
                return 0
            if steps_left == 0:
                if pos == 0:
                    return 1
                return 0
            right_move = dp(pos + 1, steps_left - 1)
            left_move = dp(pos - 1, steps_left - 1)
            stay = dp(pos, steps_left - 1)
            memo[(pos, steps_left)] = right_move + left_move + stay
            return memo[(pos, steps_left)]
        
        memo = {}
        return dp(0, steps) % (1000000007)