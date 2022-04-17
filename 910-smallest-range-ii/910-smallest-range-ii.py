class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = nums[n - 1] - nums[0]
        print(nums)
        for i in range(n - 1):
            high = max(nums[n - 1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i + 1] - k)
            print(high, low)
            ans = min(ans, high - low)
        return ans
        
        