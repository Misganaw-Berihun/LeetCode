class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(src, dest):
            nonlocal visited
            if src not in adjList:
                return -1 
            
            if src == dest:
                return 1
            visited.add(src)
            for nei in adjList[src]:
                if nei not in visited:
                    tmp = dfs(nei, dest)
                    if  tmp and tmp == -1:
                        continue
                    return div[(src, nei)] * tmp
            return -1
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
            visited = set()
            x, y = queries[j]
            ret[j] = dfs(x, y)
        return ret
                
        