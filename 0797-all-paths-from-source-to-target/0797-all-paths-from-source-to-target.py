class Solution:
    def dfs(self, cur, path, ans, dst, graph):
        if dst == cur:
            ans.append(path.copy())
            return 
        
        for nxt in graph[cur]:
            self.dfs(nxt, path + [nxt], ans, dst, graph)
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        size = len(graph)
        adjlist = defaultdict(list)
        for start in range(size):
            for dst in graph[start]:
                adjlist[start].append(dst)
        
        ans = []
        self.dfs(0, [0], ans, size - 1, graph)
        return ans