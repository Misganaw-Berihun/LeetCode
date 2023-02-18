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
        total = sum(nums)
        
        ans = [0 for i in range(n)]
        left_sum = 0
        for i in range(n):
            right_sum = (total - left_sum - nums[i])
            x = nums[i] * i
            y = nums[i] * (n - i - 1)
            cur_ans = x - left_sum
            cur_ans += right_sum - y
            left_sum += nums[i]
            ans[i] = cur_ans
        
        return ans