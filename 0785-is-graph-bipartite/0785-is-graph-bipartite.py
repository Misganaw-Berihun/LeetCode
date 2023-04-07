class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0 for i in range(n)]
        
        def dfs(node, cur_color):
            if color[node] != 0 and color[node] != cur_color:
                return False
            
            # print(color)
            color[node] = cur_color
            for nxt in graph[node]:
                if color[nxt] != 0 and color[nxt] == cur_color:
                    return False
                
                if color[nxt] == 0 and not dfs(nxt, -1 * cur_color):
                    return False
            
            return True
        
        for i in range(n):
            if color[i] == 0 and not dfs(i, 1):
                return False
        
        return True