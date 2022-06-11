class Solution {
    private static void swap(int i, int j, int [] nums){
        int  temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    private static void findPermutation(int i , int[] nums, List<List<Integer>> ans){
        if (i >= nums.length - 1){
            ArrayList<Integer> temp = new ArrayList();
            for (int k = 0; k < nums.length; k++){
                temp.add(nums[k]);
            }
            ans.add(temp);
            return;
        }
        for (int j = i; j < nums.length; j++){
            swap(i, j, nums);
            findPermutation(i + 1, nums, ans);
            swap(i, j, nums);
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        findPermutation(0, nums, ans);
        return ans;
    }
}