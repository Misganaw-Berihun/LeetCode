class Solution {
    private static int dp(int m, int n , int [][]memo){
        if (memo[m][n] > 0){ return memo[m][n]; }
        if (m == 0 || n == 0){ return 0; }
        if (m == n && n == 1){ return 1; }
        
        memo[m][n ] = dp(m - 1, n, memo) + dp(m, n - 1, memo);
        return memo[m][n];
    }
    public int uniquePaths(int m, int n) {
        int [][]memo = new int[m + 1][n + 1];
        return dp(m, n , memo);
    }
}