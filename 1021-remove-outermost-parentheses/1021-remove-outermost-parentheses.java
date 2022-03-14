class Solution {
    public String removeOuterParentheses(String s) {
        Stack<Character> stk  = new Stack<>();
        String temp = "";
        String ret = "";
        int balance = 0;
        
        for (int i = 0; i < s.length(); ++i){
            char ch = s.charAt(i);
            
            if (ch == '('){
                stk.push(ch);
                balance += 1;
            }
            else if (ch == ')'){
                balance -= 1;
                stk.push(ch);
            }
            
            if (balance == 0){
                temp = "";
                stk.pop();
                while (stk.size() > 1){
                    temp = String.valueOf(stk.pop()) + temp;
                }
                stk.pop();
                ret += temp;
            }
        }
        
        return ret;
    }
}