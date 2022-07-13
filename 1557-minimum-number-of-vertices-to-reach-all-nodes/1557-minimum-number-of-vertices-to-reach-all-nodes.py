class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = [0 for i in range(n)]
        ans = []
        
        for i in range(len(edges)):
            fro, to = edges[i]
            adjList[fro].append(to)
            indegree[to] += 1
            
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
        
        return ans
        
        