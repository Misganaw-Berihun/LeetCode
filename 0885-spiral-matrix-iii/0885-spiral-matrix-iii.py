class Solution:
    def in_bound(self, row, col, num_rows, num_cols):
        if 0 <= row < num_rows and 0 <= col < num_cols:
            return True
        return False
    
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        coordinates = []
        cur_row = rStart
        cur_col = cStart
        cur = 1
        num = 1
        step = 1
    
        while num <= rows * cols:
            for col in range(cur_col, cur_col + cur, step):
                if self.in_bound(cur_row, col, rows, cols):
                    coordinates.append([cur_row, col])
                    num += 1
            
            cur_col += cur
            for row in range(cur_row, cur_row + cur, step):
                if self.in_bound(row, cur_col, rows, cols):
                    coordinates.append([row, cur_col])
                    num += 1
            
            cur_row += cur
            if cur >= 0:
                cur += 1
            else:
                cur -= 1
            cur *= -1
            step *= -1
        
        return coordinates
            