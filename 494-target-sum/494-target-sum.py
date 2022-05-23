class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i, amt, memo = {}):
            if (i, amt) in memo:
                return memo[(i, amt)]
            if i < 0 and amt == 0:
                return 1
            if i < 0:
                return  0
            
            memo[(i, amt)] =  dp(i - 1, amt - nums[i]) + dp(i - 1, amt + nums[i])
            return memo[(i, amt)]
            
        n = len(nums)
        return dp(n - 1, target)
            
                
            
        