class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1 == 1:
            return False
        s //= 2
        N = len(nums)
        dp = [[False for i in range(s + 1)] for j in range(N + 1)]
        dp[0][0] = True
        
        for j in range(1, N + 1):
            for i in range(s + 1):
                dp[j][i] = dp[j - 1][i]
                if i - nums[j - 1] >= 0:
                    dp[j][i] = (dp[j - 1][i - nums[j - 1]] or dp[j][i])
        return dp[N][s]
                    