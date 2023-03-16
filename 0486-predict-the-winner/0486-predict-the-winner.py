class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dp(i, n, turn):
            if i == n - 1:
                return nums[i]
            ans = 0
            a = turn * nums[i] + dp(i + 1, n, -turn)
            b = turn * nums[n - 1] + dp(i, n - 1, -turn)
            ans = turn*max(turn * a , turn * b)
            return ans
        return (dp(0, len(nums), 1)) >= 0
                
                    
        
        
        