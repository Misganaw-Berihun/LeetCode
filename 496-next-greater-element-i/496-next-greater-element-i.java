class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stk = new Stack<>();
        HashMap<Integer,Integer> map = new HashMap<>();
        int [] ans = new int[nums1.length];
        
        for(int j = 0; j < nums2.length; ++j)
        {
                while (!stk.empty() && stk.peek() < nums2[j])
                {
                    map.put(stk.pop(),nums2[j]);
                }
                stk.push(nums2[j]);
        }
        
       for (int i = 0; i < nums1.length; ++i)
       {
           ans[i] = map.getOrDefault(nums1[i],-1);
       }
        return ans;
    }
}