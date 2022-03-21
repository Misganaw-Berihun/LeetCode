class Solution {
    public static int binarySearch(int [] nums,int target,boolean isLeft){
        int left = 0,right = nums.length - 1 ;
        int mid;
        
        if (nums.length == 0 ) return -1;
        
        while(left + 1 < right){
            mid = left + (right - left) / 2;
            
            if (nums[mid] > target){
                right = mid  - 1;
            }else if (nums[mid] < target){
                left = mid + 1;
            }else{
                if (isLeft){
                    right = mid;
                }else{
                    left = mid;
                }
            }
        }
        
        if (nums[left] == target && nums[right] == target){
            return isLeft? left: right;
        } 
        if (nums[left] == target) return left;
        if (nums[right] == target) return right;
        return -1;
    }
    public int[] searchRange(int[] nums, int target) {
        int [] ans = new int[2];
        ans[0] = binarySearch(nums,target,true);
        ans[1] = binarySearch(nums,target,false);
        
        return ans;
        
    }
}