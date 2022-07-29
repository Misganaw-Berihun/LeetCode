class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = [0 for i in range(len(nums))]
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     if i == 1:
        #         dp[i] = max(dp[i-1], nums[i])
        #     else:
        #         dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # return dp[len(nums) - 1]
        
#         a, b = 0, 0
#         temp = 0
        
#         for i in range(len(nums)):
#             temp = max(a)
#         print(a, b)
#         return max(a, b)
        a, b = 0, nums[0]
        for i in range(1, len(nums)):
            temp = 0
            if i == 1:
                temp = max(b, nums[i])
            else:
                temp = max(a + nums[i], b)
            a = b
            b = temp
        
        return b
            
        