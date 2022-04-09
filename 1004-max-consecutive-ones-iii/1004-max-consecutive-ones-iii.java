class Solution {
    private static int bs(int [] prefix,int s, int k){
        int l = s - 1,  r = prefix.length - 2;
        
        while (l < r){
            int m = l + (r - l + 1)/ 2;
            int size = m - s + 1;
             
            if (cntOnes(s,m,prefix) + k  < size){
                r = m - 1;
            }else{
                l = m;
            }
        }
        return  l - s + 1 ;
    }
    private static int cntOnes(int s, int e, int [] prefix){
        return prefix[e + 1] - prefix[s];
    }
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int [] prefix = new int[n + 1];
        int ans = 0;
        
        for (int i = 0; i < n; i++){
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        for (int i = 0; i < n; i++){
            ans = Math.max(ans, bs(prefix, i, k));
        }
        return ans;   
    }
}