class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False for i in range(n)]
        adj_list = defaultdict(list)
        
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        stack = [source]
        
        while stack:
            cur = stack.pop()
            visited[cur] = True
            
            if cur == destination:
                return True
            
            for nxt in adj_list[cur]:
                if not visited[nxt]:
                    stack.append(nxt)
        
        return False