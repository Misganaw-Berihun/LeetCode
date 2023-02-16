class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        ans = 0
        
        found = False
        index = 0
        middle_index = -1
        while index < n and not found:
            
            right_sum = (total_sum - left_sum - nums[index])
            if left_sum == right_sum:
                found = True
                middle_index = index
            
            left_sum += nums[index]
            index += 1
        
        return middle_index