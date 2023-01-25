class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf') for i in range(n)]
        dist2 = [float('inf') for i in range(n)]
        queue = deque()
        visited = set()
        
        queue.append(node1)
        visited.add(node1)
        level = 0
        while queue:
            cur = queue.popleft()
            dist1[cur] = level
            if edges[cur] == -1 or edges[cur] in visited:
                continue

            visited.add(edges[cur])
            queue.append(edges[cur])
            level += 1
        
        level = 0
        queue.append(node2)
        visited = set()
        visited.add(node2)
        while queue:
            cur = queue.popleft()
            dist2[cur] = level
            
            if edges[cur] == -1 or edges[cur] in visited:
                continue
                
            queue.append(edges[cur])    
            visited.add(edges[cur])
            level += 1
        
        ans = float('inf')
        temp = float('inf')
        
        for i in range(n):
            max_distance = max(dist1[i], dist2[i])                
            if max_distance < temp:
                ans = i
                temp = max_distance
        
        if ans == float('inf'):
            ans = -1
            
        return ans