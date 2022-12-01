class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1 == 1:
            return False
        s //= 2
        N = len(nums)
        dp = [False for i in range(s + 1)]
        dp[0] = True
        
        for j in range(1, N + 1):
            new_row = [False for i in range(s + 1)]
            for i in range(s + 1):
                new_row[i] = dp[i]
                if i - nums[j - 1] >= 0:
                    new_row[i] = (dp[i - nums[j - 1]] or new_row[i])
            dp = new_row
        return dp[s]
                    