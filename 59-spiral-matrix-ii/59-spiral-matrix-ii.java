class Solution {
    public int[][] generateMatrix(int n) {
        int [][] result = new int[n][n];
        int dir[][] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int d = 0, row = 0, col = 0, cnt = 1;
        
        while (cnt <= n * n){
            result[row][col] = cnt++;
             
            int r = Math.floorMod(row + dir[d][0], n);
            int c = Math.floorMod(col + dir[d][1], n);
            
            if (result[r][c] != 0) d = (d + 1) % 4;
            
            row += dir[d][0];
            col += dir[d][1];
        }
        return result;
    }
}