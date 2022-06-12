class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> comb = new ArrayList<List<Integer>>();
        List<Integer> arr = new ArrayList<Integer>(Collections.nCopies(k, 0));
        int i = 0;
        while (i >= 0){
            arr.set(i, arr.get(i) + 1);
            if (arr.get(i) > n) i--;
            else if (i == k - 1) comb.add(new ArrayList(arr));
            else{
                i++;
                arr.set(i, arr.get(i - 1));
            }
        }
        return comb;        
    }
}