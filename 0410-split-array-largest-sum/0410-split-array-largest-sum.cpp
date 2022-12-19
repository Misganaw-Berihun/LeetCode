class Solution {
public:
    bool canSplit(int k, int largestSum, vector<int> &nums){
        int groups = 1;
        int cur = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] > largestSum) return false;
            cur += nums[i];
            if (cur > largestSum){
                cur = nums[i];
                groups++;   
            }
        }
        return groups <= k;
    }
    int splitArray(vector<int>& nums, int k) {
        int left = -1;
        int right = 1000'000'001;
        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            
            if (!canSplit(k, mid, nums)){
                left = mid;
            }else{
                right = mid;
            }
        }
        return right;
    }
};