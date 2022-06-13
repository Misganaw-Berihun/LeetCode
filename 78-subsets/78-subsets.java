class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(new ArrayList<Integer>());
        for (int num : nums){
            List<List<Integer>> subsets = new ArrayList<List<Integer>>();
            for (int i = 0; i < res.size(); i++){
                List<Integer> list = new ArrayList<Integer>(res.get(i));
                list.add(num);
                subsets.add(list);
            }
            for(List<Integer> ls: subsets){
                res.add(ls);
            }
        }
        return res;
    }
}