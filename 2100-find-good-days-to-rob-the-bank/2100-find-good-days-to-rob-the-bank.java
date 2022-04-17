class Solution {
    private static int dp(int i, int dr, Map<String, Integer> memo, int n, int [] security){
        String key = i + " , " + dr;
        if (memo.containsKey(key)) return memo.get(key);
        if (0 <= i + dr && i + dr < n &&  security[i  + dr] >= security[i]){
            memo.put(key ,1 + dp(i + dr, dr, memo, n, security));
            return memo.get(key);
        }
        return 0;
    }
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        List<Integer> ans = new ArrayList<Integer>();
        int n = security.length;
        Map<String, Integer> memo = new HashMap<>();
        for(int i = 0; i < n; i++){
            int first = dp(i, 1, memo, n, security);
            int second = dp(i, -1, memo, n, security);
            if (first >= time && second >= time){
                ans.add(i);
            }
        }
        return ans;
    }
}