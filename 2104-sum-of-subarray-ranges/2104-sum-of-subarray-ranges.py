class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ret = 0
        
        for i in range(len(nums)):
            max_,min_ = float('-inf'), float('inf')
            for j in range(i,len(nums)):
                max_ = max(max_,nums[j])
                min_ = min(min_,nums[j])
                
                ret += (max_ - min_)
                
        return ret
                
                    
    
        