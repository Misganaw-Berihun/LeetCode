class Solution {
    public int minPathSum(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        int [] memo = new int[m];
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (i == 0 && j == 0){
                    memo[j] = grid[i][j];
                }
                else if (i == 0) {
                    memo[j] = grid[i][j] + memo[j - 1];
                }
               else if (j == 0){
                    memo[j] = grid[i][j] + memo[j];
                }
                else{
                    memo[j] = grid[i][j] + Math.min(memo[j], memo[j - 1]);
                }
            }
        }        
        return memo[m - 1];
    }
}