class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dp(i, j):
            if memo[i][j] != -200:
                return memo[i][j]
            
            if i == n - 1:
                return matrix[i][j]
            
            minsum = float('inf')
            for x, y in direction:
                nr, nc = x + i, y + j
                if not inbound(nr, nc):
                    continue
                minsum = min(minsum,matrix[i][j] + dp(nr, nc))
            memo[i][j] = minsum
            return minsum
        
        n = len(matrix)
        memo = [[-200 for i in range(n)] for j in range(n)]
        direction =  [(1, -1), (1, 0), (1, 1)]
        inbound = lambda r, c: 0 <= r < n and 0 <= c < n
        ans = float('inf')
        for i in range(n):
            ans = min(ans, dp(0, i))
        return ans