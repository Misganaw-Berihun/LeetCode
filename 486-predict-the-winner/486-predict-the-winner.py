class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(i, n, is_plr_1):
            if i == n - 1:
                return nums[i]
            ans = 0
            if is_plr_1:
                ans = max(nums[i] + dp(i + 1, n, False), nums[n - 1] + dp(i , n - 1, False))
            else:
                ans = min(dp(i + 1, n, True) - nums[i], dp(i, n - 1, True) - nums[n - 1])
            return ans
        return (dp(0, len(nums), True)) >= 0
                
                    
        
        
        