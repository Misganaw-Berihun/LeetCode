class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        num_ones_in_row = [0 for i in range(ROWS)]
        num_ones_in_col = [0 for i in range(COLS)]
        ans = [[0 for i in range(COLS)] for j in range(ROWS)] 
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    num_ones_in_row[i] += 1
                    num_ones_in_col[j] += 1
            
        for i in range(ROWS):
            for j in range(COLS):
                temp = 2*(num_ones_in_row[i] + num_ones_in_col[j])
                ans[i][j] =  temp - (ROWS + COLS)
        
        return ans
                
        