class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for j in range(ROWS)]
        inbound = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS
        
        directions = {
                1: [(0, 1), (0, -1)],
                2: [(1, 0), (-1, 0)],
                3: [(1, 0), (0, -1)],
                4: [(1, 0), (0, 1)],
                5: [(0, -1), (-1, 0)],
                6: [(-1, 0), (0, 1)]
        }
        
        def dfs(row, col):
            if row == ROWS - 1 and col == COLS - 1:
                return True
            
            visited[row][col] = True
            for dx, dy in directions[grid[row][col]]:
                nx, ny = row + dx, col + dy
                
                
                if not inbound(nx, ny):
                    continue
                    
                if visited[nx][ny]:
                    continue
                
                if (-dx, -dy) in directions[grid[nx][ny]] and dfs(nx, ny):
                        return True
            
            return False
        
        return dfs(0, 0)
                    