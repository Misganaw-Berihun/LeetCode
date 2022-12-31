class Solution:
    def inbound(self, curX, curY):
        valid = True
        if curX < 0 or curX >= self.ROWS:
            valid = False
            
        if curY < 0 or curY >= self.COLS:
            valid = False
            
        return valid
    
    def backtrack(self, curX, curY, visited):
        
        visited.add((curX, curY))
        if self.grid[curX][curY] == 2:
            if len(visited) == self.NUM_CELLS:
                return 1
            return 0
        
        ans = 0
        for dx, dy in self.DIR:
            newX, newY = curX + dx, curY + dy
            if not self.inbound(newX, newY):
                continue
            
            if (newX, newY) in visited:
                continue
            
            if self.grid[newX][newY] == -1:
                visited.add((newX, newY))
                continue
                
            ans += self.backtrack(newX, newY, visited)
            visited.remove((newX, newY))
        return ans
            
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.NUM_CELLS = self.ROWS * self.COLS
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == 1:
                    return self.backtrack(i, j, set())