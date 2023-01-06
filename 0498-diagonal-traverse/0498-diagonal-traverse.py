class Solution:    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        diagonal_order = []
        reverse = False
        
        for row in range(ROWS):
            temp = []
            cur_col = 0
            cur_row = row
            ''
            while cur_row >= 0 and cur_col < COLS:
                temp.append(mat[cur_row][cur_col])
                cur_col += 1
                cur_row -= 1
            
            if reverse:
                temp = temp[::-1]
            
            diagonal_order.extend(temp)
            reverse = not reverse
        
        for col in range(1, COLS):
            temp = []
            cur_row = ROWS - 1
            cur_col = col
            
            while cur_col < COLS and cur_row >= 0:
                temp.append(mat[cur_row][cur_col])
                cur_row -= 1
                cur_col += 1
            
            if reverse:
                temp = temp[::-1]
            
            diagonal_order.extend(temp)
            reverse = not reverse
            
        return diagonal_order
        
        