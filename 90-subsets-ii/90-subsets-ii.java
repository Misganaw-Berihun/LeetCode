class Solution {
        private static void backtrack(int [] nums, int i, List<Integer> temp, Set<List<Integer>> visited){
        if (i >= nums.length){
            visited.add(new ArrayList<Integer>(temp));
            return;
        }
        backtrack(nums, i + 1, new ArrayList<Integer>(temp), visited);
        temp.add(nums[i]);
        backtrack(nums, i + 1, new ArrayList<Integer>(temp), visited);
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Set<List<Integer>> visited = new HashSet<List<Integer>>();
        Arrays.sort(nums);
        backtrack(nums, 0, new ArrayList<Integer>(), visited);
        return new ArrayList<List<Integer>>(visited);
    }
}