class Solution {
    private static int dp(int m, int n , int [][]memo){
        if (memo[m][n] > 0){ return memo[m][n]; }
        if (m == 0 || n == 0){ return 0; }
        if (m == 1 && n == 1){ return 1; }
        
        memo[m][n ] = dp(m - 1, n, memo) + dp(m, n - 1, memo);
        return memo[m][n];
    }
    public int uniquePaths(int m, int n) {
        int dp[][] = new int[m + 1][n + 1];
        
        for (int i = 0; i <= m; i++){
            for(int j = 0; j <= n; j++){
                if (i == 1 && j == 1){
                    dp[i][j] = 1;
                }
                else if (i == 0 || j ==0){
                    dp[i][j] = 0;
                }else{
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }
        return   dp[m][n];     
    }
}