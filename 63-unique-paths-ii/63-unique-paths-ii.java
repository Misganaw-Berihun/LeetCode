class Solution {    
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int n = obstacleGrid.length, m = obstacleGrid[0].length;
        if (obstacleGrid[0][0] == 1 || obstacleGrid[n - 1][m - 1] == 1){
            return 0;
        }
        int [][] dp = new int[n + 1][m + 1];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if (i == 0 && j == 0) {
                    dp[i + 1][j + 1] = 1;
                }else if(obstacleGrid[i][j] == 1){
                    dp[i + 1][j + 1] = 0;
                }
                else{
                    dp[i + 1][j + 1] = dp[i + 1][j] + dp[i ][j + 1];
                } 
            }
        }
        return dp[n][m];
    }
}