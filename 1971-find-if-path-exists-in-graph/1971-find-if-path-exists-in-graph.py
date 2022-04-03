class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(adj_list, src):
            visited.add(src)
            
            for edge in adj_list[src]:
                if edge == destination:
                    visited.add(edge)
                    break
                if edge not in visited:
                    dfs(adj_list, edge)
                    
        visited = set()
        adjacency_list = defaultdict(list)
        
        for i in range(len(edges)):
                adjacency_list[edges[i][0]].append(edges[i][1])
                adjacency_list[edges[i][1]].append(edges[i][0])
        
        dfs(adjacency_list, source)
        return destination in visited;
      
        
        
                
                