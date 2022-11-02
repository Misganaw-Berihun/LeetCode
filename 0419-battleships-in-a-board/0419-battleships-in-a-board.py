class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        answer = 0
        
        for r in range(n):
            for c in range(m):
                left = board[r][c-1] if c - 1 >= 0 else "."
                up = board[r-1][c] if r - 1 >= 0 else "."
                
                if (left != "X" and up != "X") and board[r][c] == "X":
                    answer += 1
        
        return answer