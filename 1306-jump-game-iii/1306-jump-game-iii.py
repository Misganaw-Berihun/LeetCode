class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def bfs():
            queue = deque()
            visited = set()
            queue.append(start)
            visited.add(start)
            
            while queue:
                n = len(queue)
                
                for i in range(n):
                    cur = queue.popleft()
                    
                    if arr[cur] == 0:
                        return True
                    
                    idx_1 = cur - arr[cur]
                    idx_2 = cur + arr[cur]
                    
                    if in_bound(idx_1) and idx_1 not in visited:
                        queue.append(idx_1)
                        visited.add(idx_1)
                    if in_bound(idx_2) and idx_2 not in visited:
                        queue.append(idx_2)
                        visited.add(idx_2)
                        
            return False
        
        in_bound = lambda idx: 0 <= idx < len(arr)
        
        return bfs()
        