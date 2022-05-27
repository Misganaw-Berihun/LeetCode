class Stk{
    private ArrayDeque<Integer> stk;
    public Stk(){
        stk = new ArrayDeque();
    }
    
    public void push(int val){
        stk.push(val);
    }
    
    public void pop(){
        stk.pop();
    }
    
    public int top(){
        return stk.peek();
    }
}

class MinStack extends Stk {
    private ArrayDeque<Integer> minStack;
    public MinStack() {
        minStack = new ArrayDeque();
    }
    
    public void push(int val) {
        super.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()){
            minStack.push(val);
        }
    }
    
    public void pop() {
        int poped = super.top();
        super.pop();
        if (poped == minStack.peek()){
            minStack.pop();
        }
    }
    
    public int top() {
        return super.top();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */