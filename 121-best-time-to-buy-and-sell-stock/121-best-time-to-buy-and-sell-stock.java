class Solution {
    public int maxProfit(int[] prices) {
        int left = 0, ans = 0;
        for (int i = 1; i  < prices.length; ++i){
            if (prices[i] < prices[left]){ 
                left = i;
            }else{
                ans = Math.max(ans, prices[i] - prices[left]);
            }
        }
        return ans;
    }
}