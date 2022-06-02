class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        div = {}
        ret = [-1 for i in range(len(queries))]
        
        for i in range(len(equations)):
            a, b = equations[i]
            adjList[a].append(b)
            adjList[b].append(a)
            div[(a, b)] = values[i]
            div[(b, a)] = 1 / values[i]
        
        for j in range(len(queries)):
            x, y = queries[j]
            queue = deque()
            visited = set()
            queue.append((x, 1))
            visited.add(x)
        
            while (queue):
                cur = queue.popleft()
                if cur[0] not in adjList:
                    ret[j] = -1
                    continue
                if cur[0] == y:
                    ret[j] = cur[1]
                    break
                    
                for child in adjList[cur[0]]:
                    if child not in visited:
                        queue.append((child, cur[1] * div[(cur[0],  child)]))
                        visited.add(child)
        return ret
                
        