class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
            [3, 0, 1]
            [0, 1, 3]
            
        '''
        missing = -1
        i = 0
        n = len(nums)
        
        while i < n:
            correct_index = nums[i]
            
            if correct_index == n:
                missing = i
                i += 1
            elif nums[correct_index] == nums[i]:
                i += 1
            
            else:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
        
        if missing == -1:
            missing = n
            
        return missing