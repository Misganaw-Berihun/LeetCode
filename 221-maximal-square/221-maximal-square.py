class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        grid = [[0 for i in range(m + 1)] for j in range(n + 1)]
        inbound = lambda i, j : 0 <= i <= n and 0 <= j <= m
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1] + int(matrix[i - 1][j - 1])
          
        for i in range(n + 1):
            for k in range(m + 1):
                for j in range(1, max(n, m) + 1):
                    nr, nc = i + j, k + j
                    if not inbound(nr, nc):
                        continue
                    val = grid[nr][nc] - grid[nr][k] - grid[i][nc] + grid[i][k]
                    if val == min(n, m) ** 2:
                        return val
                    if val < j * j:
                        break
                    if val == j * j:
                        ans = max(ans, val)
  
        return ans