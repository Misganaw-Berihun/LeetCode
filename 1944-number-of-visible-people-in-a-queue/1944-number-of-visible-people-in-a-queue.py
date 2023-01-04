class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''
            
        '''
        size = len(heights)
        stack = []
        ans = [0 for i in range(size)]
        
        for i in range(size):
            while stack and heights[stack[-1]] < heights[i]:
                ans[stack.pop()] += 1
            
            if stack:
                ans[stack[-1]] += 1
            
            stack.append(i)
        
        return ans