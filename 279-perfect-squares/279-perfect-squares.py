class Solution:
    def numSquares(self, n: int) -> int:
        perfect = []
        i = 1
        queue = deque()
        while i * i <= n:
            perfect.append(i * i)
            i += 1
          
        queue.append(n)
        depth = 0
        while queue:
            depth += 1
            m = len(queue)
            
            for k in range(m):
                cur = queue.popleft()
                for l in range(len(perfect)):
                    dif = cur - perfect[l]
                    if dif == 0:
                        return depth
                    if dif > 0:
                        queue.append(dif)
                        
        return depth
        
        