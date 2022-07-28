class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if not in_bound(i, j) or visited[i][j] != -1 or grid[i][j] == 0:
                return 0
            
            visited[i][j] = 1
            ret = max(dfs(i+1, j), dfs(i, j+1) , dfs(i-1,j), dfs(i, j-1)) + grid[i][j]
            visited[i][j] = -1
            return ret
        n, m = len(grid), len(grid[0])
        in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
        visited = [[-1 for i in range(m)] for j in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans