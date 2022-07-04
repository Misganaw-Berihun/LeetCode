class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def dp(r, c, moves):
            if (r, c, moves) in memo:
                return memo[(r, c, moves)]
            if moves == 0:
                return 1
            prob = 0
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if inbound(nr, nc):
                    prob += (0.125 * dp(nr, nc, moves - 1))
            memo[(r,c, moves)] = prob
            return prob
        
        directions = [(-1, 2), (-1, -2), (1, 2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
        inbound = lambda r, c : 0 <= r < n and 0 <= c < n
        memo = {}
        return dp(row, column, k)
                    
                    
    
        