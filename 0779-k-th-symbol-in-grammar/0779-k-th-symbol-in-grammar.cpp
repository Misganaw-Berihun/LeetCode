class Solution {
public:
    
    int solve(int n , int k){
        if(n == 1){
            return 0;
        }
        if(n == 2){
            if(k == 1){
                return 0;
            }
            return 1;
        }
        
        
        int length = pow(2, n-1);
        int mid = length / 2;
        
        int res = 0;
        if(k > mid){
            res = solve(n-1, k - mid);
            if(res == 0){
                res = 1;
            }
            else{
                res = 0;
            }
        }
        else{
            res = solve(n-1, k);
        }
        
        return res;
    }
    
    int kthGrammar(int n, int k) {
        
        return solve(n, k);
    }
};