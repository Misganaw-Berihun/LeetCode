class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        jug1, jug2 = 0, 0
        queue = deque()
        queue.append((0, 0))
        visited = set()
        
        while queue:
            n =  len(queue)
            for i in range(n):
                j1, j2 = queue.popleft()
                if j1 == targetCapacity or j2 == targetCapacity or j1 + j2 == targetCapacity:
                    return True
                
                if (jug1Capacity, j2) not in visited and j1 ==0:
                    queue.append((jug1Capacity, j2))
                    visited.add((jug1Capacity, j2))
                if (j1, jug2Capacity) not in visited and j2 == 0:
                    queue.append((j1, jug2Capacity))
                    visited.add((j1, jug2Capacity))
                    
                if (0, j2) not in visited:
                    queue.append((0, j2))
                    visited.add((0, j2))
                if (j1, 0) not in visited:
                    queue.append((j1, 0))
                    visited.add((j1, 0))
                temp = j1
                minn = min(j1 + j2, jug1Capacity)
                
                if (minn, max(0, jug2Capacity - (minn - temp))) not in visited:
                    queue.append((minn, max(0, jug2Capacity - (minn - temp))))
                    visited.add((minn, max(0, jug2Capacity - (minn - temp))))
                temp = j2
                minn = min(j1 + j2, jug2Capacity)
                
                if (max(0, jug1Capacity - (minn - temp)), minn) not in visited:
                    queue.append((max(0, jug1Capacity - (minn - temp)), minn))
                    visited.add((max(0, jug1Capacity - (minn - temp)), minn))
        return False
                