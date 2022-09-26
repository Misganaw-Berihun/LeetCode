class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in visited:
                        return False
                    visited.add(board[i][j])
            
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in visited:
                        return False
                    visited.add(board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] != '.':
                            if board[k][l] in visited:
                                return False
                            visited.add(board[k][l])
        return True
                    