class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        largest = 0
        next_smaller = [n for i in range(n)]
        prev_smaller = [-1 for i in range(n)]
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                next_smaller[top] = i
            
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        
        for i in range(n):
            width = next_smaller[i] - prev_smaller[i] - 1
            area = heights[i] * width
            largest = max(area, largest)
        return largest
        
        