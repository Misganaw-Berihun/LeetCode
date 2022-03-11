class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> stk = new Stack<>();
        
        for (int i = 0; i< s.length(); i++){
            
           if (s.charAt(i) == '('){
                stk.push(s.charAt(i));
            }
            else if (!stk.empty() && s.charAt(i) == ')'  && stk.peek() == '('){
                stk.pop();
            }else{
                stk.push(s.charAt(i));
            }
        }
        
        return stk.size();
    }
}