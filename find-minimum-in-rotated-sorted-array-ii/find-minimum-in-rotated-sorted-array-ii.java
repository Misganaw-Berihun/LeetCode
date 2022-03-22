class Solution {
    public static int binarySearch(int [] arr){
        int n = arr.length , left = 0, right = n - 1,temp = arr[0];
        
        while (left < n && arr[0] == arr[n-1] && arr[left] == arr[0]){
            left++;
        }
        
        if (left == n) return 0;
        
        while(right > 0 &&arr[n-1] == arr[0] && arr[right] == arr[n-1]){
            right--;
        }
        
        while (left <= right){
            int mid = left + (right - left) / 2;
            
            if ( arr[mid] >= temp){
                left = mid + 1;   
            }else{
                right = mid - 1;
            }
        }
        
        return left;
    }
    public int findMin(int[] nums) {
        int m = nums.length;
        int ans = binarySearch(nums);
        
        return ans != m?Math.min(nums[ans],nums[0]): nums[0];
    }
}