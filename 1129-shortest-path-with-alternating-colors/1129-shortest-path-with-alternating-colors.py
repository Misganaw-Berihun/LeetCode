class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def bfs(isRed, dest):
            queue = deque()
            visited = set([(0, isRed)])
            queue.append(0)
            level = 0
            while queue:
                l = len(queue)
                for i in range(l):
                    cur = queue.popleft()
                    if dest == cur:
                        if res[cur] != -1:
                            res[cur] = min(level, res[cur])
                        else:
                            res[cur] = level
                    
                    if isRed:
                        for next in blue_adjList[cur]:
                            if (next, isRed) not in visited:
                                queue.append(next)
                                visited.add((next, isRed))
                    else:
                        for next in red_adjList[cur]:
                            if (next, isRed) not in visited:
                                queue.append(next)
                                visited.add((next, isRed))
                level += 1
                isRed = not isRed

            
        isRed = False
        res = [-1 for i in range(n)]
        red_adjList = defaultdict(list)
        blue_adjList = defaultdict(list)
        
        for start, end in redEdges:
            red_adjList[start].append(end)
        
        
        for start, end in blueEdges:
            blue_adjList[start].append(end)
        
        for i in range(n):
            bfs(False, i)
            bfs(True, i)
        return res