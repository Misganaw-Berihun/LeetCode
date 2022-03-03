class Solution:            
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        ans = 0
        cnt = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] - nums[i] == nums[i] - nums[i+1]:
                cnt += 1
            else:
                cnt = 0
            
            ans += cnt
                        
        return ans
                
            
                
                
                
            
        
        
        
        