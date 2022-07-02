class Solution {
    private static boolean inbound(int i, int j, int m, int n){
        return i >= 0 && i < m && j >= 0 && j < n;
    }
    private static double dp(int i, int j, int moves, int m, int n, int [][] dir, double [][][]memo){
        if (!inbound(i, j, m, n)) return 1;
        if (memo[i][j][moves] != -1) return memo[i][j][moves];
        if (moves == 0) return 0;
        long res = 0;
        for (int [] d : dir){
            int r = i + d[0], c = j + d[1];
            res += dp(r, c, moves - 1, m, n, dir, memo);
        }
        memo[i][j][moves] = res %( Math.pow(10, 9) + 7);
        return memo[i][j][moves];
    }
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        final int [][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        double [][][]memo = new double[m][n][maxMove + 1];
        for (double[][] arr: memo){
            for (double[] a: arr){
                Arrays.fill(a, -1);
            }
        }
        int result = (int) dp(startRow, startColumn, maxMove, m, n, dir, memo);
        return  result;
        
    }
}