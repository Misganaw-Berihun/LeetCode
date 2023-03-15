class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        mins = [0 for i in range(n)]
        mins[0] = nums[0]
        
        for i in range(1, n):
            mins[i] = min(nums[i], mins[i-1])
        
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack:
                top = stack[-1]
                if top > 0 and mins[top - 1] < nums[i]:
                    return True
            stack.append(i)
        
        return False