class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def perimeter(x, y):
            if not inbound(x, y) or grid[x][y] == 0:
                return 1
            
            visited.add((x, y))
            ans = 0
            for dx, dy in direction:
                nr, nc = x + dx, y + dy
                if (nr, nc) in visited:
                    continue
                ans += perimeter(nr, nc)
            return ans
            
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(grid), len(grid[0])
        inbound = lambda i, j: 0 <= i < N and 0 <= j < M
        visited = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    return perimeter(i, j)
                    
        