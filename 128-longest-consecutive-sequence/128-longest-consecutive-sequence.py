class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.max_size = 0
        
    def makeSet(self, val):
        self.parent[val] = val
        self.size[val] = 1
        self.max_size = 1
        
    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u != v:
            if self.size[u] < self.size[v]:
                u, v = v, u
            self.parent[v] = u
            self.size[u] += self.size[v]
            self.max_size = max(self.max_size, self.size[u])
    
    def get_max_size(self):
        return self.max_size
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occur = set(nums)
        n = len(nums)
        uf = UnionFind()
        
        for i in range(n):
            uf.makeSet(nums[i])
        
        for i in range(n):
            if (nums[i] - 1) in occur:
                uf.union(nums[i] - 1, nums[i])
            if (nums[i] + 1) in occur:
                uf.union(nums[i] + 1, nums[i])
        return uf.get_max_size()
      
    
        
        
        