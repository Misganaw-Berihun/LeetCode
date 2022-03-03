class Solution:            
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ret = 0
        ans = []
        i = 1
        
        while i < len(nums):
            dif = nums[i] - nums[i - 1]
            cnt = 1
            
            while i < len(nums) and nums[i] - nums[i-1] == dif:
                cnt += 1
                i += 1
                
            ans.append(cnt)
            
        for i in range(len(ans)):
            for j in range(3,ans[i] + 1):
                ret += ans[i] - j + 1

        return ret
                
            
                
                
                
            
        
        
        
        