class Solution:
    def jump(self, nums: List[int]) -> int:
        def dp(i , memo = {}):
            if i in memo:
                return memo[i]
            
            if i >= len(nums) - 1:
                return 0
            
            ans = len(nums)
            for k in range(1, nums[i]+1):
                ans = min(dp(i + k), ans)
            
            memo[i] = ans + 1
            return memo[i]
        
        return dp(0)
        