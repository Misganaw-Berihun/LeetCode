class Solution:
    def checker(self, img1, img2, row_shift, col_shift):
        n = len(img1)
        count = 0
        
        for i in range(n):
            for j in range(n):
                nx = i + row_shift
                ny = j + col_shift
                
                if 0 <= nx < n and 0 <= ny < n:
                    pixel = img2[nx][ny]
                    
                    if img1[i][j] == 1 and pixel == 1:
                        count += 1
        
        return count
                
                
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        
        for k in range(1 - n, n):
            for l in range(1 - n, n):
                ans = max(ans, self.checker(img1, img2, k , l))
        
        return ans
        