class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binarySearch(row):
            left = 0
            right = len(grid[row]) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if grid[row][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left
            
        count = 0
        for i in range(len(grid)):
            count += len(grid[0]) - binarySearch(i)
                    
        return count
                
        