class Solution:
    def dp(self, nums1, nums2, idx1, idx2, memo):
        if idx1 >= len(nums1) or idx2 >= len(nums2):
            return 0
        
        if memo[idx1][idx2] != -1:
            return memo[idx1][idx2]
        
        ans = 0
        if nums1[idx1] == nums2[idx2]:
            ans = 1 + self.dp(nums1, nums2, idx1 + 1, idx2 + 1, memo)
        else:
            inc_nums1 = self.dp(nums1, nums2, idx1 + 1, idx2, memo)
            inc_nums2 = self.dp(nums1, nums2, idx1, idx2 + 1, memo)
            ans = max(inc_nums1, inc_nums2)
        memo[idx1][idx2] = ans
        return ans
            
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[-1 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        return self.dp(nums1, nums2, 0, 0, memo)
        