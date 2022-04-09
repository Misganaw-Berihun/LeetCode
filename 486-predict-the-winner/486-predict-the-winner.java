class Solution {
    private int total = 0;
    private static int rec(int s , int e , int [] nums , int turn){
        if (s == e){
            return nums[s];
             }
        int a = turn * nums[s] + rec(s + 1,  e, nums , -turn);
        int b = turn* nums[e] + rec(s, e - 1, nums, -turn);
        return turn * Math.max(turn * a, turn * b);
    }
    public boolean PredictTheWinner(int[] nums) {
        return rec(0, nums.length - 1, nums , 1) >= 0;
    }
}