class Solution:
    def maxArea(self, height: List[int]) -> int:
        left ,right = 0,len(height) - 1
        max_area = 0
        
        while left < right:
            min_height = min(height[left],height[right])
            cur_area = (right - left) * min_height
            
            if cur_area > max_area:
                max_area = cur_area
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return max_area
            
            
            
        