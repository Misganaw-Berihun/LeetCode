class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int size = nums.size();
        int closest = INT_MAX;
        int offset = INT_MAX;
        int left, right, curSum;
        
        sort(nums.begin(), nums.end());
        for (int i = 0; i < size - 2; i++){
            int firstNumber = nums[i];
            left = i + 1; 
            right = size - 1;
            
            while (left < right){
                curSum = (nums[left] + nums[right] + firstNumber);
                
                if (abs(curSum - target) < offset){
                    closest = curSum;
                    offset = abs(curSum - target);
                }
                
                if (curSum < target){
                    left++;
                }else{
                    right--;
                }                
            }
        }
        
        return closest;
    }
};