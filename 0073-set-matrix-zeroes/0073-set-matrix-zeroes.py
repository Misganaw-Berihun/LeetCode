class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        inbound = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS
        
        for row in range(ROWS):
            for col in range(COLS):
                
                if matrix[row][col] != 0:
                    continue
                    
                for dx, dy in directions:
                    cur_row , cur_col = row, col

                    while inbound(cur_row, cur_col):
                        if matrix[cur_row][cur_col] != 0:
                            matrix[cur_row][cur_col] = inf
                        cur_row += dx
                        cur_col += dy
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == inf:
                    matrix[row][col] = 0
                    