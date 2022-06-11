class Solution {
    private void backtrack(LinkedList comb, List<List<Integer>> ans, int N, Map<Integer, Integer> counter){
        if (comb.size() == N){
            ans.add(new ArrayList(comb));
            return;
        }    
        
        for (Map.Entry<Integer, Integer> entry: counter.entrySet()){
            int num = entry.getKey();
            int value = entry.getValue();
            
            if (value == 0)
                continue;
            
            comb.addLast(num);
            counter.put(num, value - 1);
            backtrack(comb, ans, N, counter);
            counter.put(num, value);
            comb.removeLast();
        }
        
    }
    
    public List<List<Integer>> permuteUnique(int[] nums) {
        Map<Integer, Integer> counter = new HashMap();
        List<List<Integer>> ans = new ArrayList();
        LinkedList comb = new LinkedList();
        
        for (int num : nums){
            counter.put(num, counter.getOrDefault(num, 0)+ 1);    
        }
        
        backtrack(comb, ans, nums.length, counter);
        return ans;
    }
}