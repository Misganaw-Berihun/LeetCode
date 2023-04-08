class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ret = [[0 for i in range(m)] for j in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        queue = deque()
        visited = set()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
    
        level = 0
        while queue:
            size = len(queue)
            
            for i in range(size):
                x, y = queue.popleft()
                
                if mat[x][y] == 1:
                    ret[x][y] = level
                
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if not inbound(nx, ny):
                        continue

                    if (nx, ny) in visited:
                        continue

                    queue.append((nx, ny))
                    visited.add((nx, ny))
            
            level += 1
                
        return ret
    
                                
                                
                                
        
        