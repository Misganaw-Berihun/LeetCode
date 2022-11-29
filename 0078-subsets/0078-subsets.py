class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        
        for i in range(1 << N):
            temp = []
            for j in range(N):
                if (i & (1 << j) > 0):
                    temp.append(nums[j])
            ans.append(temp)
        
        return ans