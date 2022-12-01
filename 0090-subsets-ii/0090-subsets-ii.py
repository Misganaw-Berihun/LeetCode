class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        
        ans = [[]]
        visited = set()
        for i in range(N):
            l = len(ans)
            for j in range(l):
                t = ans[j] + [nums[i]]
                tup = tuple(t)
                if tup not in visited:
                    ans.append(t)
                    visited.add(tup)
        return ans
        