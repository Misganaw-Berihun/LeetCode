class Solution:
    def inbound(self, row, col, ROWS, COLS):
        return (0 <= row < ROWS) and (0 <= col < COLS)
    
    def bfs(self, forest, startRow, startCol, endRow, endCol):
        queue = deque()
        visited = set()
        queue.append((startRow, startCol))
        visited.add((startRow, startCol))
        cur_dist = 0
        
        #found (startRow, startCol)  .... (endRow, endCol) -- return cur_dist
        #not found === -1
        while queue:
            n = len(queue)
            
            for i in range(n):
                row, col = queue.popleft()
                
                if row == endRow and col == endCol:
                    return cur_dist
                
                for dx, dy in self.DIRECTION:
                    newRow, newCol = row + dx, col + dy
                    
                    if (newRow, newCol) in visited:
                        continue
                    
                    if not (self.inbound(newRow, newCol, len(forest), len(forest[0]))):
                        continue
                    
                    if forest[newRow][newCol] == 0:
                        continue
                    
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
                    
            cur_dist += 1
        
        return -1
        
    def cutOffTree(self, forest: List[List[int]]) -> int:
        '''
            3 0 2 
            1 6 4
            
            2 2 1 1 ... 6
            
            0, 0 ----- short the first min (minx, minY)
            (minx, miny) .... short dist the second min
            
            
            (0, 0) .... (x, y)
            
            num_rows = 50
            num_cols = 50
            
            total elements = n * m
            
            O(n * m) --- BFS
            O(n^2* m^2) = O((nm)^2)   
            
            cur_min = x
            (0, 0)
            heap = (value, row, col)
            
            (val, row, col)
            next_min
            heappop()
            next minimum
            
            log ((n * m) * (n * m))
            O((nm)^2 log(nm^2))
            
        '''
        self.DIRECTION = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        matrix_values = []
        cur_min = 0
        ROWS, COLS = len(forest), len(forest[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                #add (value, row, col)
                value = forest[row][col]
                matrix_values.append((value, row, col))
        
        matrix_values.sort()
        length = len(matrix_values)
        #let's find a cell which has a value != 1 and value != 0
        while cur_min < length and matrix_values[cur_min][0] < 2:
            cur_min += 1
        
        
        curx, cury = 0, 0
        ans = 0
        for i in range(cur_min, length):
            x, y = matrix_values[i][1], matrix_values[i][2]
            value = self.bfs(forest, curx, cury, x, y)
            if value == -1:
                return -1
            
            ans += value
            curx, cury = x, y
        
        return ans
        # (0, 0) ---- first_min
        # (first_min) .... second_min
        #  ....
        # cut all tress or until it is not possible
        #  (x1, y1) ..... (x2, y2) 
        
        
        
        
        