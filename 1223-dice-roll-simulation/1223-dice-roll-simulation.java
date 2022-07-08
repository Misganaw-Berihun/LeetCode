class Solution {
    private static long dp(int rolls_left, int [] rollMax, int last, int last_freq, long [][][] memo){
        if (last > 0 && rollMax[last - 1] < last_freq) return 0;
        if (rolls_left  == 0) return 1;
        if (memo[rolls_left][last][last_freq] != -1) 
            return memo[rolls_left][last][last_freq];
        
        long ret = 0;
        for (int roll = 1;  roll <= 6;  roll++){
            if (roll != last){
                ret += dp(rolls_left - 1, rollMax, roll, 1, memo);
            }else{
                ret += dp(rolls_left - 1, rollMax, last, last_freq + 1, memo);
            }
        }
        memo[rolls_left][last][last_freq] = ret % 1000000007;
        return memo[rolls_left][last][last_freq];
    }
    public int dieSimulator(int n, int[] rollMax) {
        long [][][] memo = new long[n + 1][7][16];
        
        for(long [][] arr: memo){
            for(long [] a: arr)
                Arrays.fill(a, -1);
        }
        
        return (int) dp(n, rollMax, 0, 1, memo);
    }
}