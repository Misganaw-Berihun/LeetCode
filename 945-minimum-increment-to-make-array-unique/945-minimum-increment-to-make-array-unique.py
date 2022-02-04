class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        queue = deque()
        ans = 0
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                queue.append(nums[i])
            else:
                if queue and nums[i] - nums[i-1]  != 1:
                    val = nums[i-1] + 1
                    while queue and val < nums[i]:
                        ans += (val - queue.popleft())
                        val += 1
           
        val = nums[len(nums) - 1] + 1
        while queue:
            ans += val - queue.popleft()
            val += 1
            
        return ans
            
                        
                        
            
       
                
        
            
                
        
        
                
        