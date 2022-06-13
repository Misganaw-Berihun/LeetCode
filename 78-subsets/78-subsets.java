class Solution {
    private static void backtrack(int [] nums, int i, List<Integer> temp, List<List<Integer>> ans){
        if (i >= nums.length){
            ans.add(new ArrayList(temp));
            return;
        }
        backtrack(nums, i + 1, temp, ans);
        temp.add(nums[i]);
        backtrack(nums, i + 1, new ArrayList(temp), ans);
        temp.remove(temp.size() - 1);
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        backtrack(nums, 0, new ArrayList<Integer>(), ans);
        return ans;
    }
}