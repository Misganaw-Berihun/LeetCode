class Solution {
public:
    long long numberOfWays(string s) {
        int size = s.length();
        int nOnes = 0, nZeros = size, curOnes = 0;
        long long ans = 0;
        
        for (int i = 0; i < size; i++){
            nOnes += (s[i] == '1');
        }
        nZeros -= nOnes;
        for (int i = 0; i < size; i++){
            if (s[i] == '1'){
                curOnes++;
                int curZeros = i + 1 - curOnes;
                int otherZeros = nZeros - curZeros;
                ans += (curZeros) * (otherZeros);
            }else{
                ans += (curOnes) * (nOnes - curOnes);
            }
        }
        return ans;
    }
};