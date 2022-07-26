class Solution {
public:
    int countSubstrings(string s) {
        int palindromes = 0, N = s.length();
        
        for (int i = 0; i < N; i++){
            int l = i - 1, r = i + 1;
            palindromes++;
            while (l >= 0 && r < N && s[l] == s[r]){
                palindromes++;
                l--; r++;
            }
        }
        
        for (int i = 0; i < N; i++){
            int l = i, r = i + 1;
            while (l>= 0 && r < N && s[l] == s[r]){
                palindromes++;
                l--; r++;
            }
        }
        
        return palindromes;
    }
};