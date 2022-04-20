class UnionFind:
    def __init__(self, max_row, max_col):
        self.parent = {}
        self.rank = {}
        for i in range(max_row):
            for j in range(max_col):
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
                
    def findAns(self):
        return max(self.cnt.values()) + 1
            
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        uf = UnionFind(len(grid), len(grid[0]))
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        inbound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        ans = defaultdict(int)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for d in direction:
                        r = i + d[0]
                        c = j + d[1]
                        
                        if inbound(r, c) and grid[r][c] == 1:
                            uf.union((i, j), (r, c))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans[uf.find((i,j))] += 1
        if len(ans) == 0:
            return 0
        return max(ans.values())
                
