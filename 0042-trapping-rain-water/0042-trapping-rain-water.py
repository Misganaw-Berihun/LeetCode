class Solution:
    def trap(self, height: List[int]) -> int:
        num_bars = len(height)
        stack = []
        trapped_water = 0
        
        for bar in range(num_bars):
            while stack and height[stack[-1]] <= height[bar]:
                top = stack.pop()
                if stack:
                    cur_height = min(height[bar], height[stack[-1]]) - height[top]
                    width = (bar - stack[-1] - 1)
                    trapped_water += (cur_height * width)
            
            stack.append(bar)
        
        return trapped_water
        