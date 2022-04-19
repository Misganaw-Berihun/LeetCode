class UnionFind:
    def __init__(self, size):
        self.cnt = size
        self.parent = {i : i  for i in range(size)}
        self.rank = {i: 0 for i in range(size)}
        
    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
        
    def union(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a !=  par_b:
            self.cnt -= 1
            if self.rank[par_a] < self.rank[par_b]:
                par_a, par_b = par_a, par_b
            self.parent[par_b] = par_a
            if self.rank[par_a] == self.rank[par_b]:
                self.rank[par_b] += 1
        
    def getCnt(self):
        return self.cnt
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.getCnt();
        