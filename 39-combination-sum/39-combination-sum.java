class Solution {
    private List<List<Integer>> combinations = new ArrayList<List<Integer>>();
    private void findComb(int [] candidates, int target, List<Integer> comb, int curIdx){
        if (target < 0){
            return;
        }
        if (target == 0) {
            combinations.add(new ArrayList(comb));
            return;
        }
        for (int i = curIdx; i < candidates.length ; i++){
            comb.add(candidates[i]);
            findComb(candidates, target - candidates[i], new ArrayList(comb), i);
            comb.remove(comb.size() - 1);
        }
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        findComb(candidates, target, new ArrayList(), 0);
        return combinations;
    }
}