class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache
        def dp(i, j, k):
            if i > j:
                return 0
            
            if memo[i][j][k] > 0:
                return memo[i][j][k]
            
            i0, k0 = i, k
            while i + 1 <= j and boxes[i + 1] == boxes[i]:
                k += 1
                i += 1
            
            res = (k + 1) * (k + 1)  + dp(i + 1, j, 0)
            for t in range(i + 1, j + 1):
                if boxes[i] == boxes[t]:
                    res = max(res, dp(i + 1, t - 1, 0) + dp(t, j, k + 1))
            memo[i0][j][k0] = res
            return res
        
        N = len(boxes)
        memo = [[[0 for i in range(N)] for j in range(N)] for k in range(N)]
        return dp(0, N - 1, 0)
                
        