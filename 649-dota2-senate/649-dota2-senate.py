class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue, d_queue = deque(), deque()
        n = len(senate)
        
        for i in range(n):
            if senate[i] == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
                
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(r + n)  
            else:
                d_queue.append(d + n)
                
        if len(r_queue) == 0:
            return "Dire"
        else:
            return "Radiant"
        
                