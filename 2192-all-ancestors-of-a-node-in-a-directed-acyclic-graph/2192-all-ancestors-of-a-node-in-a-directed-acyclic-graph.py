class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        queue = deque()
        adjList = defaultdict(list)
        children = defaultdict(list)
        indegree = defaultdict(int)
        ans = [set() for i in range(n)]
        
        for i in range(len(edges)):
            fro, to = edges[i]
            adjList[to].append(fro)
            children[fro].append(to)
            indegree[to] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            for p in adjList[cur]:
                ans[cur].add(p)
                ans[cur].update(ans[p]) 
            for neighbour in children[cur]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return [sorted(list(s)) for s in ans]
        
        
    
            
            
    
        