class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for j in range(n)]
        l, r, t, d = -1, n , -1, n
        i, j = 0, 0
        cnt = 1
        
        while True:
            while j  < r:
                ans[i][j] = cnt
                cnt += 1
                j += 1
            j -= 1
            i += 1
            t += 1
            if cnt == n * n + 1:
                return  ans
            while i < d:
                ans[i][j] = cnt
                i += 1
                cnt += 1
            i -= 1
            j -= 1
            r -= 1
            if cnt == n * n + 1:
                return ans
            while j > l:
                ans[i][j] = cnt
                j -= 1
                cnt += 1
            j += 1
            i -= 1
            d -= 1
            if cnt == n *n + 1 :
                return  ans
            while i > t:
                ans[i][j] = cnt
                i -= 1
                cnt += 1
            i += 1
            j += 1
            l += 1
            if cnt == n * n + 1:
                return ans