class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dp(target_sum):
            if target_sum in memo:
                return memo[target_sum]
            if target_sum < 0:
                return 0
            if target_sum == 0:
                return 1
            
            ans = 0
            for num in nums:
                ans += dp(target_sum - num)
            
            memo[target_sum] = ans
            return ans
        memo = {}
        return dp(target)
        