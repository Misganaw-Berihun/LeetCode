class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False for i in range(n)]
        adj_list = defaultdict(list)
        
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        def dfs(node):
            if node == destination:
                return True
            
            visited[node] = True
            for next in adj_list[node]:
                if not visited[next] and dfs(next):
                    return True
            
            return False
        
        return dfs(source)