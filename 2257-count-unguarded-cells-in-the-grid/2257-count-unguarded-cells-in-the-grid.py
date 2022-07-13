class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:            
        grid = [[1 for i in range(n)] for i in range(m)]
        for x, y in walls:
            grid[x][y] = -1
            
        for x, y in guards:
            grid[x][y] = -1
            
        for x, y in guards:
            for i in range(y + 1, n):
                if grid[x][i] == -1:
                    break
                grid[x][i] = 0
                
            for i in range(y - 1 , -1, -1):
                if grid[x][i] == -1:
                    break
                grid[x][i] = 0
            
            for i in range(x - 1, -1, -1):
                if grid[i][y] == -1:
                    break
                grid[i][y] = 0
            for i in range(x + 1, m):
                if grid[i][y] == -1:
                    break
                grid[i][y] = 0
            
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1
        
        return ans
        