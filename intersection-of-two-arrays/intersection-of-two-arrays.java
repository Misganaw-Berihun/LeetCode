class Solution {
    public static boolean binarySearch(int [] nums,int target){
        int n = nums.length,left = 0,right = n - 1;
        
        while (left <= right){
            int mid = left + (right - left) / 2;
            
            if (nums[mid] > target){
                right = mid - 1;
            }else if(nums[mid] < target){
                left = mid + 1;
            }else{
                return true;
            }
        }
        
        return false;
    }
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> ans = new ArrayList<Integer>();
        Set<Integer> visited = new HashSet<Integer>();
        Arrays.sort(nums1);
        
        for(int num: nums2){
            if(!visited.contains(num) && binarySearch(nums1,num)){
                visited.add(num);
                ans.add(num);
            }
        }
        
        
        return ans.stream().mapToInt(i -> i).toArray();
    }
}