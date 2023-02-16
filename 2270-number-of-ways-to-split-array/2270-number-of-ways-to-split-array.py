class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        count = 0
        
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum = (total_sum - left_sum)
            if left_sum >= right_sum:
                count += 1
        
        return count
            
        