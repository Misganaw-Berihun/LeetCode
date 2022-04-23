class UnionFind:
    def __init__(self, size):
        self.parent = {i + 1 : i + 1 for i in range(size)}
        self.rank = {i + 1: 0 for i in range(size)}
        
    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
        
    def union(self, node1, node2):
        node1_par = self.find(node1)
        node2_par = self.find(node2)
        
        if (node1_par == node2_par):
            return False
        
        if (self.rank[node1_par] > self.rank[node2_par]):
            node1_par, node2_par = node2_par, node1_par
        self.parent[node1_par] = node2_par
        if self.rank[node1_par] == self.rank[node2_par]:
            self.rank[node2_par] += 1
        
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        res = []
        
        for x, y in edges:
            if not uf.union(x, y):
                res = [x, y]
                
        return res
                
        