class Solution {
    public boolean isValid(String s) {
        ArrayDeque<Character> stk = new ArrayDeque();
        for (int i = 0; i < s.length(); i++){
            char val = s.charAt(i);
            
            if (val == '(' || val == '{' || val == '['){
                stk.push(val);
            }else
            {
                if (stk.isEmpty()) return false;
                char p = stk.pop();
                if ( (val == ')' && p != '(') || (val == '}' && p != '{') || (val == ']' && p != '[') ){
                    return false;
                }
            }
    }
    return stk.isEmpty();
}
}