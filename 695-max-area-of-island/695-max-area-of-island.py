class UnionFind:
    def __init__(self, max_row, max_col, grid):
        self.parent = {}
        self.rank = {}
        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == 1:
                    self.parent[(i,j)] = (i, j)
                    self.rank[(i, j)] = 0
    
    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)
        
        if par_a != par_b:
            if self.rank[par_a] > self.rank[par_b]:
                par_a, par_b = par_b, par_a
            self.parent[par_a] = par_b
            if self.rank[par_a] == self.rank[par_b]:
                self.rank[par_b] += 1
                
    def getParent(self):
        return self.parent
            
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        uf = UnionFind(len(grid), len(grid[0]), grid)
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        inbound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        ans = defaultdict(int)
        ret = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for d in direction:
                        r = i + d[0]
                        c = j + d[1]
                        if inbound(r, c) and grid[r][c] == 1:
                            uf.union((i, j), (r, c))
        
        for k in uf.getParent():
            ans[uf.find(k)] += 1
            ret = max(ret, ans[uf.find(k)])
        return ret
                
