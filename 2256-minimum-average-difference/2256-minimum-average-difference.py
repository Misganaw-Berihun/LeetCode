class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        size = len(nums)
        prefix = [0 for i in range(size + 1)]
        
        for i in range(size - 1, -1, -1):
            prefix[i] = prefix[i + 1] + nums[i]
        
        cur = 0
        min_diff = inf
        min_idx = 0
        
        for i in range(size):
            cur += nums[i]
            first_ets = cur // (i + 1)
            last_ets = 0
            if (size - i - 1) > 0:
                last_ets = prefix[i+1] // (size - i - 1)
            diff = abs(first_ets - last_ets)
            
            if min_diff > diff:
                min_idx = i
                min_diff = diff
        
        return min_idx