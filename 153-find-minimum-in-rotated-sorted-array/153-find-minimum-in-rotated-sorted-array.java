class Solution {
    public static int findPivot(int nums[]){
            int left = 1,right = nums.length - 1;
            int first_elt = nums[0];
            
            while (left < right){
                int mid = left + (right - left) / 2;
                
                if (nums[mid] >= first_elt){
                    left = mid + 1;
                }else{
                    right = mid;
                }
                
            }
    
        return right;
    
    }
    public int findMin(int[] nums) {
        int pivot = findPivot(nums);
        int first_elt = nums[0];
        
        return Math.min(first_elt,nums[pivot]);
    }
}