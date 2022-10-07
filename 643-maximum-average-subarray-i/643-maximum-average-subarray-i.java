class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int strt, end;
        double winSum = 0, maxSum = Integer.MIN_VALUE, avrg = 0;
        
        for(strt = 0; strt < k; strt++) {
            winSum += nums[strt];
        }
        maxSum = winSum;
        for(end = k; end < nums.length; end++) {
            winSum += (nums[end] - nums[end - k]);
            maxSum = Math.max(maxSum, winSum);
        }
        avrg = (maxSum/k);
        return (avrg);
    }
}