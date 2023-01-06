class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ROWS =  COLS = len(grid)
        count = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                equal = True
                c = 0
                while equal and c < COLS:
                    if grid[row][c] != grid[c][col]:
                        equal = False
                    c += 1

                if equal:
                    count += 1
            
        return count
                