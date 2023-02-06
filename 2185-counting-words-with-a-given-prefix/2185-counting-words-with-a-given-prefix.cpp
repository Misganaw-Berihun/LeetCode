class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int ans = 0;
        for (string word: words){
            if (pref.length() <= word.length()){
                int i = 0;
                while (i < pref.length() && pref[i] == word[i]){
                    i++;   
                }
                
                if (i == pref.length()){
                    ans++;
                }
            }
            
        }
        return ans;
    }
};