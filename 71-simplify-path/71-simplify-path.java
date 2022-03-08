class Solution {
    public String simplifyPath(String path) {
        Stack <Character> stk = new Stack<>();
        int count ;
        int n = path.length();
        char [] temp = path.toCharArray();
        String ret = "";
        
        for (int i = 0; i < n; i++)
        {   
            char ch =  temp[i];
            count = 0;
            
            stk.push(ch);
            
            if (stk.size() > 1 && (ch == '/' || i == n - 1)){
                if (stk.peek() == '/'){
                    stk.pop();
                }
                
                switch(stk.peek()){
                    case '/':
                        continue;
                    case '.':
                        while (stk.peek() == '.'){
                            count++;
                            stk.pop();
                        } 

                        if (stk.peek() == '/' && count <= 2){
                            while (count > 0 && stk.size() > 1){
                                if (stk.peek() == '/'){
                                    count--;
                                }
                                stk.pop();
                            }
                        }else{
                            while (count > 0){
                                stk.push('.');
                                count--;
                            }
                        }

                }

                if(stk.empty() || (stk.peek() != '/' && i != n-1)){
                    stk.push('/');
                }
            }
        }
        
        if (stk.size() > 1 && !stk.empty() && stk.peek() == '/'){
            stk.pop();
        }
        
        
        while (!stk.empty()){
            ret = stk.pop() + ret;
        }
        
        return ret;
    }
}