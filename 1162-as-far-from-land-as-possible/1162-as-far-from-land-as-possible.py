class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def bfs():
            temp = []
            dist = 0
            
            while queue:
                n = len(queue)
                for k in range(n):
                    cur = queue.popleft()
                    for d in direction:
                        r = cur[0] + d[0]
                        c = cur[1] + d[1]
                        
                        if (r,c) in seen or not in_bound(r, c):
                            continue
                        queue.append((r, c))
                        seen.add((r, c))
                        temp.append((r, c))
            if not temp:
                return (-1 , -1)
            return temp[-1]
        
        m = len(grid)
        seen = set()
        queue = deque()
        in_bound = lambda r, c:  0 <= r < m and 0 <= c < m
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        result =  float('inf')
        temp = []
        
        for i in range(m):
            for j in range(m):
                if grid[i][j] == 1:
                    seen.add((i, j))
                    queue.append((i, j))
                    temp.append((i , j))
        
        d = bfs();
        if (d[0] == -1 or d[1] == -1):
            return  -1
        
        for i in range(len(temp)):
            t = abs(d[0] - temp[i][0]) + abs(d[1] - temp[i][1])
            result = min(result, t)
        
        return result
            
    
    
    
        
    
        
                    