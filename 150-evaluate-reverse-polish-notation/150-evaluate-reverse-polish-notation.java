class Solution {
    public int evalRPN(String[] tokens) {
        ArrayDeque stk = new ArrayDeque();
        for (String token: tokens){
            char first = token.charAt(0);
            
            if (Character.isDigit(first)){
                    stk.addLast(Integer.parseInt(token));
            }else if (token.length() > 1){
                     stk.addLast(-1 * Integer.parseInt(token.substring(1)));
            }else{
                int val1 = (int) stk.pollLast();
                int val2 = (int) stk.pollLast();
                
                switch(first){
                    case '+':
                        stk.addLast(val1 + val2);
                        break;
                    case '-':
                        stk.addLast(val2 - val1);
                        break;
                    case '*':
                         stk.addLast(val1 * val2);
                        break;
                    default:
                        stk.addLast(val2 / val1);
                }
                
            }
        }
        
        return (int) stk.getLast();
    }
}