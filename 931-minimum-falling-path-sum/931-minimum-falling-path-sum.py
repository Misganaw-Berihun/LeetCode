class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf') for i in range(n)] for j in range(n)]
        direction =  [(-1, 0), (-1, 1), (-1, -1)]
        
        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, n):
            for j in range(n):
                for x, y in direction:
                    r, c = x + i, y + j
                    if r < 0 or c < 0 or c >= n or r >= n:
                        continue
                    dp[i][j] = min(dp[i][j], dp[r][c] + matrix[i][j])
                    
        return min(dp[n - 1])