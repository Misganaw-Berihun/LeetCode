class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int size = nums.size();
        int ans = INT_MIN;
        int cur = 0;
        
        for (int i = 0; i < size; i++){
            cur = max(cur + nums[i], nums[i]);
            ans = max(cur, ans);
        }
        
        vector<int> forwardPrefix(size + 1, 0);
        vector<int> backwardPrefix(size + 1, 0);
        
        for (int i = 1; i <= size; i++){
            forwardPrefix[i] = forwardPrefix[i-1] + nums[i - 1];
        }
        
        for (int i = size - 1; i >= 0; i--){
            backwardPrefix[i] = backwardPrefix[i + 1] + nums[i];
        }
        
        for (int i = 2; i <= size; i++){
            forwardPrefix[i] = max(forwardPrefix[i-1], forwardPrefix[i]);
        }
        
        for (int i = size - 2; i >=0; i--){
            backwardPrefix[i] = max(backwardPrefix[i+1], backwardPrefix[i]);
        }
        
        for (int i = 2; i < size; i++){
            int cur = (backwardPrefix[i] + forwardPrefix[i - 1]);
            ans = max(cur, ans);
        }
        
        return ans;
    }
};