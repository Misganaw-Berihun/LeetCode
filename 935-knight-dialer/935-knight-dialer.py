class Solution:
    def knightDialer(self, n: int) -> int:         
        moves = [(2, 1), (2, -1), (1, 2), (1, -2),
                 (-1, 2), (-1, -2), (-2, 1), (-2, -1)] 
        
        prev = [[1 for i in range(3)] for j in range(4)]
        cur = [[0 for i in range(3)] for j in range(4)]
        prev[3][0] = prev[3][2] = 0
        
        for k in range(1, n):       
            for i in range(4):
                for j in range(3):
                    if i == 3 and (j == 0 or j == 2):
                        continue
                    for move in moves:
                        r, c = i + move[0], j + move[1]
                        if (r < 0 or c < 0 or c >= 3 or r >= 4 or \
                            (r == 3 and (c == 0 or c == 2))):
                            continue
                        cur[i][j] += prev[r][c]
            prev = cur.copy()
            cur = [[0 for i in range(3)] for j in range(4)]
        
        return sum([sum(prev[i]) for i in range(len(prev))]) % 1000000007
        
                    
        