class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        
        #find the prefix sum
        for i in range(1,len(nums) + 1):
            prefix[i] = prefix[i-1] + nums[i - 1]
            
        k = len(prefix) - 1
        
        #loop and return pivot if found
        for j in range(1,len(prefix)):
            if prefix[k] - prefix[j] == prefix[j-1]:
                return j - 1
            
        return -1
            
            
            
        
            
