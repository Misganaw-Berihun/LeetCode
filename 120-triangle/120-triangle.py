class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dp(i, j):
            nonlocal memo
            if (i, j) in memo:
                return memo[(i,j)]
            if (i == len(triangle) - 1):
                return triangle[i][j]
            
            memo[(i,j)] = triangle[i][j] + min( dp(i + 1, j) , dp(i + 1, j + 1))
            return memo[(i,j)]
        
        memo = {}
        return dp(0,0)
            