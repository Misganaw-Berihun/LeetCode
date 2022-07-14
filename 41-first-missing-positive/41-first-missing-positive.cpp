class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        vector<int> seen(n + 1, 1);
        
        for (int num : nums){
            if (1 <= num && num <= n){
                seen[num] = 0;
            }
        }
        
        int i = 1;
        while (i < n + 1 && seen[i] == 0) {i++;}
        return i;
        }
};