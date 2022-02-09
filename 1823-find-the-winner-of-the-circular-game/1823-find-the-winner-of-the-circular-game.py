class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        
        for i in range(1,n+1):
            queue.append(i)
            
        while len(queue) != 1:
            j = 1
            
            while j < k:
                queue.append(queue.popleft())
                j += 1 
                
            queue.popleft()
            
        return queue.popleft()