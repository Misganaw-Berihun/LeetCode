class Solution {
    private static double dp(int A, int B, Map<String, Double> memo){
        if (A <= 0 && B <= 0) return 0.5;
        if (A <= 0) return 1;
        if (B <= 0) return 0;
        
        String key = A + ":" + B;
        if (memo.containsKey(key)) 
            return memo.get(key);
        
        double prob = 0;
        for (int ml = 25; ml <= 100; ml += 25){
            prob += 0.25 * dp(A - ml, B + ml - 100, memo);
        }
        
        memo.put(key, prob);
        return prob;
    }
    public double soupServings(int n) {
        Map<String, Double> memo = new HashMap<String, Double>();
        if (n > 4800) return 1;
        return dp(n, n, memo);
    }
}