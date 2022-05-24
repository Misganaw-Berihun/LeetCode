class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            visited.add((i, j))
            if k == len(word):
                return True
        
            for x, y in DIR:
                r, c = x + i, y + j
                if in_bound(r,c) and (r, c) not in visited and board[r][c] == word[k]:
                    if dfs(r, c, k + 1):
                        return True
            visited.remove((i, j))
            return False

        n , m = len(board), len(board[0])
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
        visited = set()
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False