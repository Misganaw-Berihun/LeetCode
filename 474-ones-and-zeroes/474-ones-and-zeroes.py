class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dp(i, one, zero):
            if i >= len(strs):
                if one <= n and zero <= m:
                    return 0
                return float("-inf")
            
            if one > n or zero > m:
                return float("-inf")
            
            if memo[i][zero][one] != -1:
                return memo[i][zero][one]
            include = 1 + dp(i + 1, one + strs[i].count("1"), zero + strs[i].count("0"))
            exclude = dp(i + 1, one, zero)
            memo[i][zero][one] = max(include, exclude)
            return memo[i][zero][one]
        length = len(strs)
        memo = [[[-1 for i in range(n + 1)] for j in range(m + 1)] for k in range(length + 1)]
        ans =  dp(0, 0, 0)
        return ans if ans != float("-inf") else 0