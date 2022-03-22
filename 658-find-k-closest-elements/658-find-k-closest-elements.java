class Solution {
    public static int binarySearch(int [] arr,int target,int k){
        int left = 0,right = arr.length - k;
        
        while (left < right){
            int mid = left +( right - left )/ 2;
            
            if (target - arr[mid]  <= arr[mid + k] - target){
                right  = mid;
            }else{
                left = mid + 1;
            }
        }
        
        return left;
    }
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
     int left_ptr = binarySearch(arr,x,k);
     List<Integer> ans = new ArrayList<Integer>();
        
    for(int i = left_ptr; i < left_ptr + k; i++){
        ans.add(arr[i]);
    }
     return ans;   
    }
}