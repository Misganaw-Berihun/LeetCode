class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def perimeter(x, y):
            nonlocal peri
            visited.add((x, y))
            
            for dx, dy in direction:
                nr, nc = x + dx, y + dy
                if (not inbound(nr, nc) or grid[nr][nc] == 0):
                    peri += 1
                    continue
                if (nr, nc) in visited:
                    continue
                perimeter(nr, nc)
            
        peri = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N, M = len(grid), len(grid[0])
        inbound = lambda i, j: 0 <= i < N and 0 <= j < M
        visited = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    perimeter(i, j)
                    return peri
        