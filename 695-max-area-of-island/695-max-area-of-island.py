class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            visited.add((row,col))
            self.cnt += 1
            
            for d in DIR:
                newRow = row + d[0]
                newCol = col + d[1]
                
                if (newRow,newCol) in visited or not in_bound(newRow,newCol) \
                            or grid[newRow][newCol] != 1:
                    continue
                dfs(newRow,newCol)
        
        max_area = 0
        visited = set()
        m = len(grid)
        n = len(grid[0])
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        in_bound = lambda row,col: 0 <= row < m and 0 <= col < n
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    self.cnt = 0
                    dfs(i,j)
                    max_area = max(max_area,self.cnt)
                    
                    
        return max_area
        
        
        
                
            
                
                
                
            
        