class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = t = -1
        r = len(matrix[0])
        b = len(matrix)
        i = j = 0
        ans = []
        
        while b - t > 1 and r - l > 1:
            if i == t + 1 and j == l + 1 :
                while j < r:
                    ans.append(matrix[i][j])
                    j += 1
                j -= 1
                i += 1
                t += 1
            elif i == t + 1 and j == r - 1:
                while i < b:
                    ans.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                r -= 1
            elif i == b - 1 and j == r - 1:
                while j > l:
                    ans.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                b -= 1
            elif i == b - 1 and j == l + 1:
                while i > t:
                    ans.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                l += 1
                
        return ans
                
                
                
                
                
                    
        
        