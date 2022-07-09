class Solution {
    private static double dp(int A, int B, double [][] memo){
        if (A <= 0 && B <= 0) return 0.5;
        if (A <= 0) return 1;
        if (B <= 0) return 0;
        
        String key = A + ":" + B;
        if (memo[A][B] != -1) 
            return memo[A][B];
        
        double prob = 0;
        for (int ml = 1; ml <= 4; ml++){
            prob += 0.25 * dp(A - ml, B + ml - 4, memo);
        }
        
        memo[A][B] = prob;
        return prob;
    }
    public double soupServings(int n) {
        double [][]memo = new double[200][200];
        for (double [] m: memo)
            Arrays.fill(m, -1);
        if (n > 4800) return 1;
        return dp((n + 24) / 25, (n + 24) / 25, memo);
    }
}