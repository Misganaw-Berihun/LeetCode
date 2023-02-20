class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        n = len(nums)
        ans = -inf
        
        for i in range(1, n):
            if nums[i] > min_so_far:
                ans = max(ans, nums[i] - min_so_far)
            min_so_far = min(min_so_far, nums[i])
        
        if ans == -inf:
            ans = -1
        
        return ans
        