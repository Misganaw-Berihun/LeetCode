class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for i in range(n)]
        adjList = defaultdict(list)
        indegree = [0 for i in range(n)]
        queue = deque()
        
        for fro, to in edges:
            adjList[fro].append(to)
            indegree[to]+=1
            
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            
            for next in adjList[cur]:
                ans[next].add(cur)
                ans[next].update(ans[cur])
        
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)
        return [sorted(ans[i]) for i in range(n)]