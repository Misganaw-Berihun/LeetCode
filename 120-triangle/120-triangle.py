class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        ans = triangle[-1]

        for j in range(N - 2, -1, -1):
            for k in range(len(triangle[j])):
                ans[k] = triangle[j][k] + min(ans[k] , ans[k + 1])
        return ans[0]
            