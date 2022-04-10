class Solution {
    private static int dp(int [][]obstacleGrid, int r, int c, HashMap<String, Integer> memo){
        String key = r + "," + c;
        if (memo.containsKey(key)) return memo.get(key);
        if (r == 0 && c == 0) return 1;
        if (r < 0 || c < 0) return 0;
        int a = 0, b = 0;
        if ( r >= 1 && obstacleGrid[r - 1][c] == 0){
            a = dp(obstacleGrid, r - 1, c, memo);
        }
        if ( c >= 1 && obstacleGrid[r][c - 1] == 0){
            b = dp(obstacleGrid, r, c - 1, memo);
        }
        memo.put(key, a + b);
        return memo.get(key);
    }
    
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int n = obstacleGrid.length, m = obstacleGrid[0].length;
        HashMap<String, Integer> memo = new HashMap<String, Integer>();
        if (obstacleGrid[0][0] == 1|| obstacleGrid[n - 1][m - 1] == 1 ){
            return 0;
        }
        return dp(obstacleGrid, n - 1 , m - 1, memo);
    }
}