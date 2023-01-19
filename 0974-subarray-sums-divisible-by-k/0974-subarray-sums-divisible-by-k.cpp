class Solution {
public:
    int calculateMod(int num, int k){
        int res = (num  % k);
        if (res < 0){
            res += k;
        }
        return res;
    }
    int subarraysDivByK(vector<int>& nums, int k) {
        int size = nums.size();
        map<int, int> count;
        count[0] = 1;
        int ans = 0;
        
        int cur = 0;
        for (int i = 0; i < size; i++){
            cur += nums[i];
            int mod = calculateMod(cur, k);
            ans += (count[mod]);
            count[mod]++;
        }
        return ans;
    }
};