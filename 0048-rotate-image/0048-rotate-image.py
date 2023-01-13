class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        HALF = ROWS // 2
    
        
        for i in range(HALF):
            idx = ROWS - i - 1
            topRight = topLeft = i  
            bottomLeft = bottomRight = idx
            
            for j in range(i, idx):
                a = matrix[i][topLeft]
                b = matrix[topRight][idx]
                c = matrix[idx][bottomRight]
                d = matrix[bottomLeft][i]
                
                matrix[i][topLeft] = d
                matrix[topRight][idx] = a
                matrix[idx][bottomRight] = b
                matrix[bottomLeft][i] = c
                topLeft += 1
                topRight += 1
                bottomRight -= 1
                bottomLeft -= 1
