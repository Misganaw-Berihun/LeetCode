class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        ans = []
        ans.append(triangle[-1])
        
        for j in range(N - 2, -1, -1):
            temp = []
            for k in range(0,len(ans[-1]) - 1):
                min_val = triangle[j][k] + min(ans[-1][k] , ans[-1][k + 1])
                temp.append(min_val)
            ans.append(temp)
        return ans[-1][-1]
            