class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dp(i):
            nonlocal memo
            if i in memo: return memo[i]
            if i >= len(questions): return 0
            solve_cur = questions[i][0] + dp(i + questions[i][1] + 1)
            skip_cur = dp(i + 1)
            memo[i] = max(solve_cur, skip_cur)
            return memo[i]
        memo = {}
        return dp(0)
        