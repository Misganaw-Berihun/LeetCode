class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i,j):
            return (i,j) not in visited and board[i][j] == 'O'
            
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
            if isValid(i,0):
                dfs(i,0)
            if isValid(i,m-1):
                dfs(i,m-1)
                
        for i in range(m):
            if isValid(0,i):
                dfs(0,i)
            if isValid(n-1,i):
                dfs(n-1,i)
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
                    
        
                
                
                