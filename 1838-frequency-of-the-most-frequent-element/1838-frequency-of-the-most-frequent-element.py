class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        count = 1
        max_freq = 1
        diff = 0
        
        for j in range(1,len(nums)):
            p = (nums[j] - nums[j-1]) * count
            diff = diff + p
            count += 1
            
            while diff > k and i <= j:
                if count != 1:
                    count -= 1
                diff -= (nums[j] - nums[i])
                i += 1
          
            max_freq = max(max_freq,count)               
            
        return max_freq
                
                
        