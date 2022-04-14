class Solution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long [] dp = new long[n + 1];
        
        for (int i = n - 1; i >= 0; i--){
            int pt = questions[i][0], jmp = questions[i][1];
            dp[i] = Math.max(dp[i + 1] , dp[Math.min(i + jmp + 1, n)] + pt);
        }
        return dp[0];
    }
}