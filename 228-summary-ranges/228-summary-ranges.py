class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        temp = nums[0]
        j = 0
        ans = []
        
        while j < len(nums) - 1:
            if  nums[j+1] - nums[j] > 1:
                if nums[j] != temp:
                    ans.append(str(temp) + "->" + str(nums[j]))
                else:
                    ans.append(str(temp))
                    
                temp = nums[j+1]
                
            j += 1
            
        if temp == nums[j]:
            ans.append(str(temp))
        else:
            ans.append(str(temp) + "->" + str(nums[j]))
            
        return ans
                
        
        
                
        