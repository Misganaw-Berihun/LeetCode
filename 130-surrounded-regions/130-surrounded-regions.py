class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            visited.add((i,j))
            
            for d in DIR:
                new_row = i + d[0]
                new_col = j + d[1]
                
                if (new_row,new_col) in visited or not in_bound(new_row,new_col) \
                            or board[new_row][new_col] == 'X':
                        continue
                        
                dfs(new_row,new_col)
            
        visited = set()
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        n = len(board)
        m = len(board[0])
        in_bound = lambda row,col: 0 <= row < n and 0 <= col < m
        
        
        for i in range(n):
            if (i,0) not in visited and board[i][0] == 'O':
                dfs(i,0)
                
        for i in range(m):
            if (0,i) not in visited and board[0][i] == 'O':
                dfs(0,i)
                
        for i in range(n):
            if (i,m-1) not in visited and board[i][m-1] and board[i][m-1] == 'O':
                dfs(i,m-1)
            
        for i in range(m):
            if (n-1,i) not in visited and board[n-1][i] == 'O':
                dfs(n-1,i)
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
                    
        
                
                
                