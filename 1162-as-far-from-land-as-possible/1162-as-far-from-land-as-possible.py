class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def bfs():
            level = -1
            
            while queue:
                n = len(queue)
                level += 1
                for k in range(n):
                    cur = queue.popleft()
                    for d in direction:
                        r = cur[0] + d[0]
                        c = cur[1] + d[1]
                        
                        if (r,c) in seen or not in_bound(r, c):
                            continue
                        queue.append((r, c))
                        seen.add((r, c))
            return level
        
        m = len(grid)
        seen = set()
        queue = deque()
        in_bound = lambda r, c:  0 <= r < m and 0 <= c < m
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for i in range(m):
            for j in range(m):
                if grid[i][j] == 1:
                    seen.add((i, j))
                    queue.append((i, j))
        
        if len(queue) == 0 or len(queue) == m * m:
            return -1
        
        return bfs()
            
    
    
    
        
    
        
                    