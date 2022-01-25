class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack1 = []
        stack2 = []
        left = len(nums)
        right = -1
        
        
        for i in range(len(nums)):
            while stack1 and nums[stack1[-1]] > nums[i]:
                    left = min(stack1.pop(),left)
            stack1.append(i)
    
                    
        for j in range(len(nums) - 1, -1,-1):
            while stack2 and nums[stack2[-1]] <nums[j]:
                    right = max(stack2.pop(),right)
            
            stack2.append(j)
                    
        if right == -1 and left == len(nums):
            return 0
        
        return right - left + 1
            
                    
                    
                    
                
        
                    
                    
        