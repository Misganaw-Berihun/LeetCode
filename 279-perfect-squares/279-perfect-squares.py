class Solution:
    def numSquares(self, n: int) -> int:
        perfect = []
        queue = deque()
        queue.append(n)
        depth = 0
        while queue:
            depth += 1
            m = len(queue)
            
            for k in range(m):
                cur = queue.popleft()
                for l in range(1, int(sqrt(n)) + 1):
                    dif = cur - l * l
                    if dif == 0:
                        return depth
                    if dif > 0:
                        queue.append(dif)
                        
        return depth
        
        