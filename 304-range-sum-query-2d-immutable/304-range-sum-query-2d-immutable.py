class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.mat = []
        n = len(matrix[0]) + 1
        m = len(matrix) + 1
        self.tot = [[0 for _ in range(n)] for a in range(m)]
        
        for i in range(len(matrix)):
            cols = []
            
            for j in range(len(matrix[0])):
                cols.append(matrix[i][j])
                
            self.mat.append(cols)
            
        for i in range(1,m):
            for j in range(1,n):
                self.tot[i][j] = self.mat[i-1][j-1] + self.tot[i][j-1] + \
                            self.tot[i-1][j] - self.tot[i-1][j-1]
    
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum1 = self.tot[row2 + 1][col2 + 1]+ self.tot[row1][col1]
        sum2 = self.tot[row2 + 1][col1] + self.tot[row1][col2 + 1]
      
        return sum1 - sum2