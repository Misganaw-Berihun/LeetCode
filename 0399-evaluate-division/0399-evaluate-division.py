class Solution:
    def dfs(self, cur, target, graph, visited):
        if cur == target:
            return 1
        
        visited.add(cur)
        for nxt, value in graph[cur]:
            if nxt not in visited:
                d = self.dfs(nxt, target, graph, visited)
                if d != -1:
                    return d * value
        
        return -1
            
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        num_equations = len(equations)
        graph = defaultdict(list)
        
        for i in range(num_equations):
            num, den = equations[i]
            graph[num].append((den, values[i]))
            graph[den].append((num, 1 / values[i]))
        
        ans = []
        for num, den in queries:
            if num in graph and den in graph:
                ans.append(self.dfs(num, den, graph, set()))
            else:
                ans.append(-1)
        
        return ans
        