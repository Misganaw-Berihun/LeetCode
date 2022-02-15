class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums) - 1
        k = k % len(nums)
        temp = nums[-k:]
        
        for i in range(r - k, -1,-1):
            nums[i + k] = nums[i]
            
        for j in range(len(temp)):
            nums[j] = temp[j]
        
        return nums
                
                
        
        