class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = [matrix[0][i] for i in range(n)]
        cur = prev.copy()
        
        for i in range(1, n):
            for j in range(n):
                    if  j == 0:
                        cur[j] = min(prev[j + 1], prev[j]) + matrix[i][j]
                    elif j == n - 1:
                        cur[j] = min(prev[j - 1], prev[j]) + matrix[i][j]
                    else:
                        cur[j] = min(prev[j - 1], prev[j], prev[j + 1]) + matrix[i][j]
                    
            prev = cur.copy()       
        return min(cur)