class Solution {
    public static int findPivot(int [] arr){
         int m,target = arr[0],l = 0,r = arr.length - 1;
        
        while (l <= r){
            m = l + (r-l)/2;
            
            if (arr[m] < target){
                r = m - 1;
            }else{
                l = m + 1;
            }
        }   
        return l; 
    }
    
    public static int binarySearch(int [] arr,int target,int l , int r){
        int m;
        
        while (l <= r){
            m = l + (r - l) / 2;
            
            if (arr[m] > target){
                r = m - 1;
            }else if ( arr[m] < target){
                l = m + 1;
            }else{
                return m;
            }
        }
        
        return  -1;
    }
    
    public int search(int[] nums, int target) {
        int n = nums.length - 1,pivot = findPivot(nums),ans = -1;
    
        if (target >= nums[0]){
            ans = binarySearch(nums,target,0,pivot - 1);
        }else{
            ans = binarySearch(nums,target,pivot,n);
        }
        
        return ans;
    }
}