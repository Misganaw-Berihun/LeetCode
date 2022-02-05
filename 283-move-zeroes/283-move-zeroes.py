class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        p = i
        
        if p == len(nums):
            return nums
        
        for j in range(i + 1,len(nums)):
            if nums[j] != 0:
                nums[p] = nums[j]
                nums[j] = 0
                
                while p < len(nums) and nums[p] != 0:
                    p += 1
            
            
            
        