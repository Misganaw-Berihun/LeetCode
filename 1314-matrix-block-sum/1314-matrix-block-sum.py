class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        prefix = [[0 for i in range(COLS + 1)] for j in range(ROWS + 1)]
        output = [[0 for i in range(COLS)] for j in range(ROWS)]
        
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + mat[i-1][j-1] - prefix[i-1][j-1]
            
        for i in range(ROWS):
            for j in range(COLS):
                sx = max(0, i - k) + 1
                sy = max(0, j - k) + 1
                ex = min(ROWS - 1, i + k) + 1
                ey = min(COLS - 1, j + k) + 1
                
                output[i][j] = prefix[ex][ey] - prefix[ex][sy - 1] - prefix[sx - 1][ey] + prefix[sx - 1][sy - 1]
        
        return output
                
            
                
        