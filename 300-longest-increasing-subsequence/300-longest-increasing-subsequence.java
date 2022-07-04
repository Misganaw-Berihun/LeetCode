class Solution {
    private static int dp(int [] nums, int curIdx, int [] memo){
        if (memo[curIdx] != 0) return memo[curIdx];
        if (curIdx >= nums.length) return 0;
        int ans = 1;
        for (int i = curIdx + 1; i < nums.length; i++){
            if (nums[i] > nums[curIdx]){
                ans = Math.max(ans, 1 + dp(nums, i, memo));
            }
        }
        memo[curIdx] = ans;
        return ans;
    }
    public int lengthOfLIS(int[] nums) {
        int ans = 1, n = nums.length;
        int [] memo = new int[n];
        for (int i = 0; i < nums.length; i++){
            int ret = dp(nums, i, memo);
            ans = Math.max(ans, ret);
        }
        return ans;
    }
}