class Solution:
    def calculate(self, node):
        self.visited[node] = True
        tot_dist, num_nodes = 0, 0
        
        for nxt in self.adjlist[node]:
            if not self.visited[nxt]:
                dist, n_nodes = self.calculate(nxt)
                tot_dist += (n_nodes + dist)
                num_nodes += n_nodes
        self.memo[node] = (tot_dist, num_nodes)
        return tot_dist, num_nodes + 1
    
    def dfs(self, node, n):
        self.visited[node] = True
        
        for nxt in self.adjlist[node]:
            if not self.visited[nxt]:
                my_dist, my_nodes = self.memo[nxt]
                
                dist = self.memo[node][0] - (my_nodes + 1)
                dist += (n - (my_nodes + 1))
                self.ans[nxt] = dist
                self.memo[nxt] = dist, my_nodes
                self.dfs(nxt, n)
        self.ans[0] = self.memo[0][0]
        
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.adjlist = defaultdict(list)
        for src,dst in edges:
            self.adjlist[src].append(dst)
            self.adjlist[dst].append(src)
        
        self.memo = {}
        self.ans = [0 for i in range(n)]
        self.visited = [False for i in range(n)]
        self.calculate(0)
        self.visited = [False for i in range(n)]
        self.dfs(0, n)
        return self.ans
        
        
        