class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        List<Integer> temp = new ArrayList();
        temp.add(nums[0]);
        ans.add(temp);
        for (int i = 1; i < nums.length; i++){
            List<List<Integer>> new_ans = new ArrayList();
            for (int j = 0; j <= i; j++){
                for (List<Integer> l: ans){
                    List<Integer> cur = new ArrayList(l);
                    cur.add(j, nums[i]);
                    new_ans.add(cur);
                }
            }
            ans = new_ans;
        }
        return ans;
    }
}