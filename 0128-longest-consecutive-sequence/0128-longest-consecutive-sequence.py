class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
        
    def makeSet(self, val):
        self.parent[val] = val
        self.size[val] = 1
        
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
        return self.size[u]
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        occur = set(nums)
        n = len(nums)
        uf = UnionFind()
        ans = 1
        
        for i in range(n):
            uf.makeSet(nums[i])
        
        for i in range(n):
            if (nums[i] + 1) in occur:
                ans = max(ans, uf.union(nums[i] + 1, nums[i]))
        return ans
      
    
        
        
        