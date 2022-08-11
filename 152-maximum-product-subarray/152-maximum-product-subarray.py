class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        maxx = [1 for i in range(N + 1)]
        minn = [1 for j in range(N + 1)]
        ans = float('-inf')
        
        for i in range(1, N + 1):
            pro1, pro2 = maxx[i-1] * nums[i-1], minn[i-1] * nums[i - 1]
            maxx[i] = max(pro1,pro2,nums[i-1])
            minn[i] = min(pro1,pro2,nums[i-1])
            ans = max(ans, maxx[i])
        return ans
                
  