class Solution {
    private int total = 0;
    private static int rec(int s , int e , int [] nums , int turn, 
                                            HashMap<Pair<Integer, Integer>, Integer> memo){
        Pair<Integer, Integer> cur = new Pair(s, e);
        if (memo.containsKey(cur)){
            return memo.get(cur);
        }
        if (s == e){
            return nums[s];
             }
        int a = turn * nums[s] + rec(s + 1,  e, nums , -turn, memo);
        int b = turn* nums[e] + rec(s, e - 1, nums, -turn, memo);
        memo.put(cur,turn * Math.max(turn * a, turn * b));
        return memo.get(cur);
    }
    public boolean PredictTheWinner(int[] nums) {
        HashMap<Pair<Integer, Integer>, Integer> memo = 
                new HashMap<Pair<Integer, Integer>, Integer>();
        return rec(0, nums.length - 1, nums , 1, memo) >= 0;
    }
}