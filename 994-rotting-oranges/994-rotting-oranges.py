class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs():
            queue = deque()
            visited = set()
            count = 0
            direction = [(-1,0),(1,0),(0,-1),(0,1)]
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        queue.append((i,j))
                        visited.add((i,j))

            while queue:
                n = len(queue)
                l = len(visited)
                
                for i in range(n):
                    cur = queue.popleft()
                    
                    for d in direction:
                        new_row = cur[0] + d[0]
                        new_col = cur[1] + d[1]
                     
                        if (new_row,new_col) in visited or \
                            not in_bound(new_row,new_col) or \
                            grid[new_row][new_col] != 1:
                            continue
                      
                        visited.add((new_row,new_col))
                        queue.append((new_row,new_col))
                        
                if (l < len(visited)):
                    count += 1
                
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i,j) not in visited:
                        return -1
                
            return count 
        
        m = len(grid)
        n = len(grid[0])
        in_bound = lambda row,col: 0 <= row < m and 0 <= col < n
        return bfs()
                        
                
            
        