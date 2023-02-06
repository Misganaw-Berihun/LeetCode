class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                # print(queue)
                x, v, l = queue.popleft()
                
                if x == target:
                    return l
                
                queue.append((x + v, 2 * v, l + 1))
                if (x + v > target and v > 0) or (x + v < target and v < 0):
                    val = -1 * (v // abs(v))
                    queue.append((x, val, l + 1))
                