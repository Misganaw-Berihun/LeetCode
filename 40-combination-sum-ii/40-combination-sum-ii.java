class Solution {
    private Map<Integer, Integer> counter = new HashMap<Integer, Integer>();
    private void backtrack(int[] candidates, int target, List<Integer> comb, List<List<Integer>>ans, int curIdx){
        if (target < 0) return;
        if (target == 0){
            ans.add(new ArrayList(comb));
            return;
        }
        for (int i = curIdx; i < candidates.length; i++){
            if (counter.get(candidates[i])  == 0){
                continue;
            }
            comb.add(candidates[i]);
            counter.put(candidates[i], counter.get(candidates[i]) - 1);
            backtrack(candidates, target - candidates[i], new ArrayList<Integer>(comb), ans, i);
            comb.remove(comb.size() - 1);
            counter.put(candidates[i], counter.get(candidates[i]) + 1);
        }
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans  = new ArrayList<List<Integer>>();
        for (int candidate: candidates){
            counter.putIfAbsent(candidate, 0);
            counter.put(candidate, counter.get(candidate) + 1);
        }
        int [] arr = new int[counter.size()];
        int i = 0;
        for(int key: counter.keySet()){
            arr[i++] = key;
        }
        backtrack(arr, target, new ArrayList<Integer>(), ans, 0);
        return ans;
    }
}