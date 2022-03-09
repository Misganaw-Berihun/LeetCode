class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(i,j):
            visited.add((i,j))
            cnt = 0
            
            for d in DIR:
                new_row = i + d[0]
                new_col = j + d[1]
                
                if (new_row,new_col) in visited or \
                     not in_bound(new_row,new_col):
                    continue
                
                if board[new_row][new_col] == 'M':
                    cnt += 1
            
            if cnt == 0:
                board[i][j] = 'B'
                for d in DIR:
                    new_row = i + d[0]
                    new_col = j + d[1]

                    if (new_row,new_col) in visited or \
                         not in_bound(new_row,new_col):
                        continue
                    dfs(new_row,new_col)
            else:
                board[i][j] = str(cnt)
        
        visited = set()
        DIR = [[0,1],[1,0],[-1,0],[0,-1], 
                [1,1],[-1,1],[1,-1],[-1,-1]]
        
        n = len(board)
        m = len(board[0])
        
        in_bound = lambda row,col: 0 <= row < n and 0 <= col < m
        
        checked = board[click[0]][click[1]]
        
        if checked == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click[0],click[1])
            
        return board
        
                
        