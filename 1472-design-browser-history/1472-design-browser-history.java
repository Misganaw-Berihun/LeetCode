class BrowserHistory {
    private Stack<String> backward_stk;
    private Stack<String> forward_stk;

    public BrowserHistory(String homepage) {
        backward_stk = new Stack<>();
        forward_stk = new Stack<>();
        backward_stk.push(homepage);        
    }
    
    public void visit(String url) {
        backward_stk.push(url);
        while ( !forward_stk.empty() ){
            forward_stk.pop();
        }
    }
    
    public String back(int steps) {
        while (backward_stk.size()  >  1 &&  steps  >  0){
            forward_stk.push(backward_stk.pop());
            steps--;
        }
        return backward_stk.peek();
    }
    
    public String forward(int steps) {
        while (forward_stk.size() > 0 && steps > 0){
            backward_stk.push(forward_stk.pop());
            steps--;
        }
        return backward_stk.peek();
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */