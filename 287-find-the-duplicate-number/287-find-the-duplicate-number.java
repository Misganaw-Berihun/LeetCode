class Solution {
    public int findDuplicate(int[] nums) {
        int slow =  nums[0];
        int fast = nums[0];
        
       for (int i = 0 ; i < nums.length; i++){
           slow = nums[slow];
           fast = nums[nums[fast]];
           
           if (slow == fast) break;
       }
        
        slow = nums[0];
        
        while (slow != fast){
            fast = nums[fast];
            slow = nums[slow];
        }
               
        return fast;
    }
}