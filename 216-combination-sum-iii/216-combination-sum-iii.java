class Solution {
    private static void backtrack(int k, 
                                                            int n,
                                                            List<Integer> comb,
                                                            List<List<Integer>> result,
                                                            int cur,
                                                            int [] candidates
                                                            ){
        if (k == 0 && n == 0){
            result.add(comb);
            return;
        }
        if (cur >= 9 || n < 0 || k < 0) return;
        backtrack(k, n, new ArrayList<Integer>(comb), result, cur + 1, candidates);
        comb.add(candidates[cur]);
        backtrack(k - 1, n - candidates[cur], new ArrayList<Integer>(comb), result, cur + 1, candidates);
    }
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        int [] candidates = {1,2,3,4,5,6,7,8,9};
        backtrack(k, n, new ArrayList<Integer>(), res, 0, candidates);
        return res;
    }
}