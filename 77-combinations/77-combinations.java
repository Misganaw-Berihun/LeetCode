class Solution {
    private List<List<Integer>> combinations = new ArrayList<List<Integer>>();
    private void findComb(int n, int k, List<Integer> comb){
        if (k == 0){
            combinations.add(new ArrayList(comb));
            return;
        }
        
        for (int i = n; i >= 1; i--){
            comb.add(i);
            findComb(i - 1, k - 1, new ArrayList<Integer>(comb));
            comb.remove(comb.size() - 1);
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        findComb(n, k, new ArrayList<Integer>());
        return combinations;
    }
}