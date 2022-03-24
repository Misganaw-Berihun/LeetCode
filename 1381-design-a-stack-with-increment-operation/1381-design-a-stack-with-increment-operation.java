class CustomStack {
    private int [] stk;
    private int maxSize;
    private int top;
    
    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        stk = new int[maxSize];
        top = -1;
    }
    
    public void push(int x) {
        if (top < maxSize - 1){
            stk[++top] = x; 
        }
    }
    
    public int pop() {
         if (top != -1){
             return stk[top--];
         }
        return -1;
    }
    
    public void increment(int k, int val) {
        int range = Math.min(k,top + 1);
        
        for(int i = 0 ; i < range; i++){
            stk[i] = stk[i] + val;
        }
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */