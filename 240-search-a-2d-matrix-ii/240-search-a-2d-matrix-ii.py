class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j, i = len(matrix[0]) - 1, 0
        
        while i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        
        while i < len(matrix):
            if matrix[i][0] == target:
                return True
            i += 1
            
        while j >= 0:
            if matrix[len(matrix) - 1][j] == target:
                return True
            j -= 1
        
        return False
        