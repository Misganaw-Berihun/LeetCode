class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        number = defaultdict(list)
        
        for i in range(len(routes)):
            for stop in routes[i]:
                number[stop].append(i)
        
        queue = deque()
        visited = set()
        queue.append(source)
        level = 0
        
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                cur = queue.popleft()
                
                if cur == target:
                    return level
                
                for num in number[cur]:
                    if num not in visited:
                        for stop in routes[num]:
                            queue.append(stop)
                                
                    visited.add(num)
            level += 1
        
        return -1