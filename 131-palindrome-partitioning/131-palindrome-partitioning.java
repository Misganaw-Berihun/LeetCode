class Solution {
    private static boolean isPalindrome(String s){
        int left = 0, right = s.length() - 1;
        while (left <= right){
            if (s.charAt(left++) != s.charAt(right--))
                return false;
        }
        return true;
    }
    private static void backtrack(StringBuilder sb, List<String> comb, List<List<String>> res, int cur){
        if (cur >= sb.length()) return;
        for (int i = cur; i < sb.length() - 1 ; i++){
            String s1 = sb.substring(cur, i + 1);
            String s2 = sb.substring(i + 1, sb.length());
            if (isPalindrome(s1))
                comb.add(s1);
            else{
                continue;
            }
            if (isPalindrome(s2)){
                comb.add(s2);
                res.add(new ArrayList<String>(comb));
                comb.remove(comb.size() - 1);
            }
            backtrack(sb, new ArrayList<String>(comb), res, i + 1);
            if (comb.size() >= 1 && isPalindrome(s1)){
                comb.remove(comb.size() - 1);
            }
        }
    }
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<List<String>>();
        backtrack(new StringBuilder(s), new ArrayList<String>(), res, 0);
        if (isPalindrome(s)){
            List<String> temp = new ArrayList<String>();
            temp.add(s);
            res.add(temp);
        }
        return res;
    }
}