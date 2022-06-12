class Solution {
    private static void findComb(List<List<Integer>> comb, int i, int n, int k, ArrayList<Integer> c){
        if (k == 0){
            comb.add(new ArrayList(c));
            return;
        }
        
        if (i + k -1 <= n){
            findComb(comb, i + 1, n, k, c);
            c.add(i);
            findComb(comb, i + 1, n, k -1 , new ArrayList(c));
            c.remove(c.size() - 1);
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> comb = new ArrayList<List<Integer>>();
        findComb(comb, 1, n, k, new ArrayList<Integer>());
        return comb;
    }
}