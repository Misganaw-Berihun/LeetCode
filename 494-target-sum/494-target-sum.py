class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        mx, mn = s, -1 * (s + 1)
        N = mx - mn
        M = len(nums)
        inc = (s + 1)
        dp = [[0 for i in range(N + 1 + max(nums))] for j in range(M+1)]
        dp[0][inc] = 1
        
        for i in range(1, M+1):
            for j in range(mn, mx + 1):
                dp[i][j + inc] = (dp[i-1][j-nums[i-1] + inc] + 
                                    dp[i-1][j+nums[i-1] + inc])
        return dp[M][target + inc]
        
        
                