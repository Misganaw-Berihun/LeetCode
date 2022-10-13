class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        numRow, numCol = len(grid), len(grid[0])
        ans = 0
        curRow, curCol = numRow - 1, 0
        
        while (curRow >= 0 and curCol < numCol):
            if grid[curRow][curCol] < 0:
                ans += (numCol - curCol)
                curRow -= 1
            else:
                curCol += 1
        
        
        return ans