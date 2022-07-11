class Solution:
    def knightDialer(self, n: int) -> int:
        def dp(i, j, jmps):
            if i < 0 or j < 0 or i >= 4 or j >= 3 or \
                (i == 3 and (j == 0 or j == 2)):
                return 0
            
            if jmps == 0:
                return 1
            
            if memo[i][j][jmps] != -1:
                return memo[i][j][jmps]
            
            ans = 0
            for move in moves:
                x, y = i + move[0], j + move[1]
                ans += dp(x, y, jmps - 1)
            memo[i][j][jmps] = ans % 1000000007
            return memo[i][j][jmps]
                
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1) , (2, 1)] 
        
        memo = [[[-1 for i in range(n)] for j in range(3)] for k in range(4)]
        ans = 0
        for i in range(4):
            for j in range(3):
                if i == 3 and (j == 0 or j == 2):
                    continue
                ans += dp(i, j, n - 1) 
                
        return ans % 1000000007