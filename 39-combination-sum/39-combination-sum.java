class Solution {
    private List<List<Integer>> combinations = new ArrayList<List<Integer>>();
    private void findComb(int [] candidates, int target, List<Integer> comb){
        if (target < 0){
            return;
        }
        if (target == 0) {
            combinations.add(new ArrayList(comb));
            return;
        }
        for (int candidate: candidates){
            if (comb.size() >= 1 && comb.get(comb.size() - 1) > candidate)
                continue;
            comb.add(candidate);
            findComb(candidates, target - candidate, new ArrayList(comb));
            comb.remove(comb.size() - 1);
        }
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        findComb(candidates, target, new ArrayList());
        return combinations;
    }
}