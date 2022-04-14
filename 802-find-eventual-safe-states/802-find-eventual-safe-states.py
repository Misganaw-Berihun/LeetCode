class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outgoing = [0] * len(graph)
        ans, queue = [], deque()
        adjacencyList = defaultdict(list)
        
        for i in range(len(graph)):
            outgoing[i] = len(graph[i])
            for j in range(len(graph[i])):
                adjacencyList[graph[i][j]].append(i)
        
        for i in range(len(graph)):
            if outgoing[i] == 0:
                queue.append(i)
            
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for neigh in adjacencyList[cur]:
                outgoing[neigh] -= 1
                if outgoing[neigh] == 0:
                    queue.append(neigh)
                    
        return sorted(ans)
                    
            
        
        
            
        
        