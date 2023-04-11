class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        queue = deque()
        
        if grid[0][0] == 1:
            return -1
        
        queue.append((0, 0))
        visited.add((0, 0))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        distance = 0
        inbound = lambda r, c: 0 <= r < n and 0 <= c < n
        
        while queue:
            length = len(queue)
            
            for i in range(length):
                x, y = queue.popleft()
                
                if x == n - 1 and y == n - 1:
                    return distance + 1
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if inbound(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        
            distance += 1
        return -1
                
                