class UnionFind:
    def __init__(self, size):
        self.num_sets = size
        self.rep = {i: i for i in range(size)}
        self.rank = {i: 0 for i in range(size)}
        
    def find(self, v):
        if v != self.rep[v]:
            self.rep[v] = self.find(self.rep[v])
        return self.rep[v]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u != v:
            self.num_sets -= 1
            if self.rank[u] > self.rank[v]:
                u, v = v, u
            self.rep[u] = v
            if self.rank[u] == self.rank[v]:
                self.rank[v] += 1
    
    def check(self, u, v):
        return self.find(u) == self.find(v)
                
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(len(graph[i])):
                if uf.check(i, graph[i][j]):
                    return False
                uf.union(graph[i][0], graph[i][j])
        return True
                    
                    
                
            
        