class Solution {
    private void backtrack(int[] candidates, int target, List<Integer> comb, List<List<Integer>>ans, int curIdx){
        if (target < 0) return;
        if (target == 0){
            ans.add(new ArrayList(comb));
            return;
        }
        for (int i = curIdx; i < candidates.length; i++){
            if (i > curIdx && candidates[i] == candidates[ i - 1])
                continue;
            comb.add(candidates[i]);
            backtrack(candidates, target - candidates[i], new ArrayList<Integer>(comb), ans, i + 1);
            comb.remove(comb.size() - 1);
        }
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans  = new ArrayList<List<Integer>>();
        Arrays.sort(candidates);
        backtrack(candidates, target, new ArrayList<Integer>(), ans, 0);
        return ans;
    }
}