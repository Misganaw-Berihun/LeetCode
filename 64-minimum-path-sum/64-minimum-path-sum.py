class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return float('inf')
            
            ans = grid[i][j] + min(dp(i -1, j), dp(i , j - 1))
            return ans
            
        return dp(len(grid) - 1, len(grid[0]) - 1)
            
                
            
        