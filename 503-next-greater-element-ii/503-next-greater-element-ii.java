class Solution {
    public int[] nextGreaterElements(int[] nums)
    {
        Stack<Integer> stk = new Stack<>();
        int n = nums.length;
        int [] ans  = new int[n];
        
        int[] temp = Arrays.copyOf(nums, 2 * n);
        for (int i = n; i < 2 * n; i++)
        {
                temp[i] = nums[i - n];
        }
        
        for(int i = 0; i < 2*n; ++i)
        {
                while (!stk.empty() && temp[stk.peek()] < temp[i])
                {
                        int top = stk.pop();
                        if (top < n)
                        {
                                ans[top] = temp[i];    
                        }
                }
                stk.push(i);
        }
        
        while (!stk.empty())
        {
                int top = stk.pop();
                if (top < n){
                    ans[top] = -1;
                }
        }        
        return ans;
    }
}