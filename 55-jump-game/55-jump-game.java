class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int dest = n - 1;
        for (int i = n - 2; i >= 0; i--){
           if (dest - i <= nums[i]){
            dest = i;
           } 
        }
        return dest == 0;
    }
}