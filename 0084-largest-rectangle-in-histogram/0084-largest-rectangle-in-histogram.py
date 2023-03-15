class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        stack = []
        largest = 0
        
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                top = stack.pop()
            
                width = i - stack[-1] - 1 if stack else i
                area = width * heights[top]
                largest = max(area, largest)
                    
            stack.append(i)
        return largest
        
        