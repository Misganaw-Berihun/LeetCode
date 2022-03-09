class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def isValid(i,j):
            return (i,j) not in visited and grid[i][j] == 1
            
        def dfs(i,j):
            visited.add((i,j))
            
            for d in DIR:
                new_row = i + d[0]
                new_col = j + d[1]
                
                if (new_row,new_col) in visited or not in_bound(new_row,new_col) \
                            or grid[new_row][new_col] == 0:
                        continue
                        
                dfs(new_row,new_col)
            
        visited = set()
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        n = len(grid)
        m = len(grid[0])
        in_bound = lambda row,col: 0 <= row < n and 0 <= col < m
        cnt = 0
        
        
        for i in range(n):
            if isValid(i,0):
                dfs(i,0)
            if isValid(i,m-1):
                dfs(i,m-1)
                
        for i in range(m):
            if isValid(0,i):
                dfs(0,i)
            if isValid(n-1,i):
                dfs(n-1,i)
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    cnt += 1
                    
        return cnt
        