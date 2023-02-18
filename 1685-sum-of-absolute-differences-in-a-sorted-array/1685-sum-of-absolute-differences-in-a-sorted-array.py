class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        '''
            1   4   6   8   10
            3 + 5 + 7 + 9 = 24
            2 + 4 + 6 = 12
            2 + 2 = 4
            2 = 2
            
            
            |nums[0] - nums[1]| + |nums[0] - nums[2]| + |nums[0] - nums[3]|
            
        '''
        n = len(nums)
        right_sum = sum(nums)
        
        ans = [0 for i in range(n)]
        left_sum = 0
        for i in range(n):
            ans[i] = (nums[i] * (i) - left_sum) + (right_sum - nums[i] * (n - i))  
            left_sum += nums[i]
            right_sum -= nums[i]
        
        return ans