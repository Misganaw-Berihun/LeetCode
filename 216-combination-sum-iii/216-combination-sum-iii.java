class Solution {
    private static void backtrack(int k, 
                                                            int n,
                                                            List<Integer> comb,
                                                            List<List<Integer>> result,
                                                            int cur
                                                            ){
        if (n < 0) return;
        if (k == 0 && n == 0){
            result.add(new ArrayList<Integer>(comb));
            return;
        }
        
        for (int i = cur; i <= 9; i++){
            comb.add(i);
            backtrack(k - 1, n - i, new ArrayList<Integer>(comb), result, i + 1);
            comb.remove(comb.size() - 1);
        }
    }
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        backtrack(k, n, new ArrayList<Integer>(), res, 1);
        return res;
    }
}