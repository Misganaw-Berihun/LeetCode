class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre1 = [1]*(len(nums) + 1)
        pre2 = [1]*(len(nums) + 1)
        
        for i in range(1,len(nums) + 1):
            pre1[i] = pre1[i-1] * nums[i-1]
            
        for j in range(1,len(nums) + 1):
            pre2[j] = pre2[j - 1] * nums[len(nums) - j]
            
        for k in range(1,len(pre1)):
            nums[k-1] = pre1[k - 1] * pre2[len(pre2) - k - 1]
            
        return nums
            
        
            
        
        
        