class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        outdegree = [[0 for i in range(m)] for j in range(n)]
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        in_bound  = lambda r, c: 0 <= r< n and 0 <= c < m
        queue = deque()
        ans = 0
        
        for i in range(n):
            for j in range(m):
                for d in direction:
                    nei_r, nei_c = i + d[0], j + d[1]
                    if in_bound(nei_r, nei_c) and matrix[nei_r][nei_c] > matrix[i][j]:
                        outdegree[i][j] += 1
     
        for i in range(n):
            for j in range(m):
                if outdegree[i][j] == 0:
                    queue.append((i, j, 1))
                    
        while queue:
            r, c, l = queue.popleft()
            ans = l
            for d in direction:
                nei_r, nei_c = r + d[0], c + d[1]
                if in_bound(nei_r, nei_c) and matrix[r][c] > matrix[nei_r][nei_c]:
                    outdegree[nei_r][nei_c] -= 1
                    if outdegree[nei_r][nei_c] == 0:
                        queue.append((nei_r, nei_c, l + 1))
                        
        return ans        
        