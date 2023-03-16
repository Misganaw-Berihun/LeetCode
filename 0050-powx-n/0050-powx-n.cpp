class Solution {
public:
    double myPow(double x, int n) {
        double res = 1.0;
        double cur = x;
        int temp = abs(n);
        while( temp > 0){
            if (temp & 1 == 1){
                res *= 1.0 * cur;
            }
            cur *= cur;
            temp >>= 1;
        }
        if (n < 0){
            res = 1.0 / res;
        }
        return res;
    }
};