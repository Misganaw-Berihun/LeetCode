class Solution {
    public int maxDepth(String s) {
        Stack<Character> stk = new Stack<Character>();
        int ans = 0;
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            
            if (ch == '('){
                stk.push(ch);
            }
            if (ch == ')' ){
                stk.pop();
            }
            
            ans = Math.max(ans,stk.size());
        }
        
        return ans;
    }
}