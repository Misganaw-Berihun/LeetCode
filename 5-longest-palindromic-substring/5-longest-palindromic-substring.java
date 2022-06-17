class Solution {
    public String longestPalindrome(String s) {
        int n = s.length(), cur = 0, ans = 0;
        String ret = "";
        for(int i = 0 ; i < n; i++){
            int j = i, k = i;
            while (j >= 0 && k < n && s.charAt(j) == s.charAt(k)){
                j--;  k++;
            }
            j++; k--;
            
            if (ans < (k - j + 1)){
                ans = k - j + 1;
                ret = s.substring(j, k + 1);
            }
            
            j = i; k = i + 1;
             while (j >= 0 && k < n && s.charAt(j) == s.charAt(k)){
                j--;
                k++;
            }
            j++;
            k--;
           if (ans < (k - j + 1)){
                ans = k - j + 1;
               ret = s.substring(j, k + 1);
            }
            }
            return ret;        
    }
}