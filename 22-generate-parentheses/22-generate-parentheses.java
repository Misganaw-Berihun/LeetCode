class Solution {
    private static void backtrack(int open, int close,int i, int n, StringBuilder sb, List<String> ans){
        if (open + close < 0 || open > n) return;
        if (open + close == 0 && i == 0){
            ans.add(sb.toString());
            return;
        }
        sb.append('(');
        backtrack(open + 1, close, i - 1, n, sb, ans);
        sb.deleteCharAt(sb.length() - 1);
        sb.append(')');
        backtrack(open, close - 1, i, n, sb, ans);
        sb.deleteCharAt(sb.length() - 1);
    }
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<String>();
        backtrack(0, 0, n, n, new StringBuilder(), ans);
        return ans;
    }
}