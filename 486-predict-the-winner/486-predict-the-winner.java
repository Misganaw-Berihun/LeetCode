class Solution {
    private int total = 0;
    private static int rec(int s , int e , int [] nums , 
                                            HashMap<Pair<Integer, Integer>, Integer> memo){
        Pair<Integer, Integer> cur = new Pair(s, e);
        if (memo.containsKey(cur)){
            return memo.get(cur);
        }
        if (s == e){
            return nums[s];
             }
        int a = nums[s] - rec(s + 1,  e, nums , memo);
        int b = nums[e] - rec(s, e - 1, nums,  memo);
        memo.put(cur,Math.max(a, b));
        return memo.get(cur);
    }
    public boolean PredictTheWinner(int[] nums) {
        HashMap<Pair<Integer, Integer>, Integer> memo = 
                new HashMap<Pair<Integer, Integer>, Integer>();
        return rec(0, nums.length - 1, nums , memo) >= 0;
    }
}