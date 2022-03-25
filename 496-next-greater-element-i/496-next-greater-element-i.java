class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stk = new Stack<>();
        HashMap<Integer,Integer> map = new HashMap<>();
        int [] ans = new int[nums1.length];
        
        for (int i = 0; i  < nums1.length; ++i)
        {
            map.put(nums1[i],i);
        }
        
        for(int j = 0; j < nums2.length; ++j)
        {
            if (stk.empty() || stk.peek() > nums2[j])
            {
                stk.push(nums2[j]);
            }
            else if (stk.peek() < nums2[j])
            {
                while (!stk.empty() && stk.peek() < nums2[j])
                {
                    int top = stk.pop();
                    if (map.containsKey(top))
                    {
                        ans[map.get(top)]  = nums2[j];
                    }
                }
                stk.push(nums2[j]);
            }
        }
        
        while (!stk.empty())
        {
            int top = stk.pop();
        
            if (map.containsKey(top))
            {
                ans[map.get(top)] = -1;
            }
        }
        return ans;
    }
}