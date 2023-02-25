class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        
        left = 0
        cur_sum = 0
        for right in range(n):
            cur_sum += nums[right]
            
            while cur_sum >= target:
                cur_sum -= nums[left]
                left += 1
            
            if left > 0:
                ans = min(ans, right - left + 2)
        
        if ans == inf:
            ans = 0
            
        return ans