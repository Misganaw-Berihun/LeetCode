class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row,col):
            queue = deque()
            queue.append((row,col))
            visited.add((row,col))
        
            while queue:
                l = len(queue)
                
                for i in range(l):
                    cur = queue.popleft()
                     
                    for d in direction:
                        new_row = cur[0] + d[0]
                        new_col = cur[1] + d[1]

                        if in_bound(new_row,new_col) and (new_row,new_col) not in visited and \
                                            grid[new_row][new_col] == "1":
                            visited.add((new_row,new_col))
                            queue.append((new_row,new_col))
                                
        visited = set()
        n = len(grid)
        m = len(grid[0])
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        in_bound = lambda row,col: 0 <= row < n and 0 <= col < m
        islands = 0
        
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    islands += 1
                    
        return islands
                                
                        
                            
        