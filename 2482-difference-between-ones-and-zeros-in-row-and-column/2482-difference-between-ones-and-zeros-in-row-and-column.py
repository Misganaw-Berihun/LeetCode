class Solution:
    def countOnes(self, grid, outer_range, inner_range, array, row_outer):
        for i in range(outer_range):
            one_cnt = 0
            for j in range(inner_range):
                if row_outer and grid[i][j] == 1:
                    one_cnt += 1
                elif not row_outer and grid[j][i] == 1:
                    one_cnt += 1
            
            array[i] = one_cnt
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        num_ones_in_row = [0 for i in range(ROWS)]
        num_ones_in_col = [0 for i in range(COLS)]
        ans = [[0 for i in range(COLS)] for j in range(ROWS)] 
        
        self.countOnes(grid, ROWS, COLS, num_ones_in_row, True)
        self.countOnes(grid, COLS, ROWS, num_ones_in_col, False)
        
        for i in range(ROWS):
            for j in range(COLS):
                temp = 2*(num_ones_in_row[i] + num_ones_in_col[j])
                ans[i][j] =  temp - (ROWS + COLS)
        
        return ans
                
        