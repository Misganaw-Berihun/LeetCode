class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def findPerm(i, temp):
            if i >= len(nums) - 1:
                ans.append(temp[:])
                return
            
            for k in range(i, len(temp)):
                temp[i], temp[k] = temp[k], temp[i]
                findPerm(i + 1, temp)
                temp[i], temp[k] = temp[k], temp[i]
            
        ans = []
        findPerm(0, nums)
        return ans
        