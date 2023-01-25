class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf') for i in range(n)]
        dist2 = [float('inf') for i in range(n)]
        
        def bfs(node, dist):
            queue = deque()
            queue.append(node)
            visited.add(node)
            level = 0
            while queue:
                cur = queue.popleft()
                dist[cur] = level
                if edges[cur] == -1 or edges[cur] in visited:
                    continue

                visited.add(edges[cur])
                queue.append(edges[cur])
                level += 1
        
        visited = set()
        bfs(node1, dist1)
        visited = set()
        bfs(node2, dist2)
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