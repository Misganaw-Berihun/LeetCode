class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(node):
            nonlocal q, visited, graph, q_idx
            visited.add(node)
            
            if q >= quiet[node]:
                q_idx = node
                q = quiet[node]
                
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
                    
        graph = defaultdict(list)
        res = [0] * len(quiet) 
        
        for a, b in richer:
            graph[b].append(a)
            
        for i in range(len(quiet)):
                q = float('inf')
                q_idx = 0
                visited = set()
                dfs(i)
                res[i] = q_idx
            
        return res
            
            
        
                    
            
        