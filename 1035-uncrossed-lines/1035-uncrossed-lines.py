class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        dp = [[0 for i in range(len_nums1 + 1)] for j in range(len_nums2 + 1)]
        for i in range(len_nums2 - 1, -1, -1):
            for j in range(len_nums1 - 1, -1, -1):
                if nums2[i] == nums1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
        