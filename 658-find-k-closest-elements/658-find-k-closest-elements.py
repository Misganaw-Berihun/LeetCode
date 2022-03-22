class Solution {
    public static int binarySearch(int [] arr,int target){
        int left = 0,right = arr.length - 1;
        
        while (left <= right){
            int mid = left +( right - left )/ 2;
            
            if (arr[mid] > target){
                right  = mid - 1;
            }
            else if (arr[mid] < target){
                left = mid + 1;
            }else{
                return mid;
            }
        }
        
        return left;
    }
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int pivot = binarySearch(arr,x);
        int n = arr.length;
        List<Integer> ans = new ArrayList<Integer>();
        int left_ptr = 0, right_ptr = n - 1;
        
        if (pivot  < 0){pivot = 0;}
        else if (pivot == n){pivot = n - 1;}
        
        if (arr[pivot] == x){left_ptr = pivot;right_ptr = pivot + 1;}
        else if(arr[pivot] != x){left_ptr = pivot - 1 ;right_ptr = pivot;}
        
        while ((left_ptr >= 0 && right_ptr < n)  && k > 0){
            int left_dist = Math.abs(arr[left_ptr] - x);
            int right_dist = Math.abs(arr[right_ptr] - x);
            
            if (left_dist <= right_dist){
                left_ptr--;
            }else{
                right_ptr++;
            }
            k--;
        }
       
        while (k > 0 && left_ptr >= 0){
            left_ptr--;
            k--;
        }
        
        while(k>0 && right_ptr < n){
            right_ptr++;
            k--;
        }
        
        left_ptr = left_ptr >= 0? left_ptr: -1;
        right_ptr = right_ptr < n? right_ptr: n;
        
        for(int i = left_ptr + 1; i < right_ptr; i++){
            ans.add(arr[i]);
        }
     return ans;   
    }
}