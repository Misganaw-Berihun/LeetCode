class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int idx = 0;
        int [] ret = new int[n];
        
        for(int num: nums){
            if (num < pivot){
                ret[idx++] = num;
            }
        }
        for (int num: nums){
            if (num == pivot){
                ret[idx++] = num;
            }
        }
        for (int num: nums){
            if (num > pivot){
                ret[idx++] = num;
            }
        }
        return ret;
    }
}