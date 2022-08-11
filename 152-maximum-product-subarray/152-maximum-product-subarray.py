class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        maxx = 1
        minn = 1
        ans = float('-inf')
        
        for i in range(1, N + 1):
            pro1, pro2 = maxx * nums[i-1], minn * nums[i - 1]
            maxx = max(pro1,pro2,nums[i-1])
            minn = min(pro1,pro2,nums[i-1])
            ans = max(ans, maxx)
        return ans
                
  