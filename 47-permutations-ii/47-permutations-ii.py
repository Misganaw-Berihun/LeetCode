class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def findPerm(i, temp):
            nonlocal ans
            if i >= len(nums) - 1:
                c = temp.copy()
                ans.add(tuple(c))
                return
            
            for k in range(i, len(nums)):
                temp[k], temp[i] = temp[i], temp[k]
                findPerm(i + 1, temp)
                temp[k], temp[i] = temp[i], temp[k]
            
        ans = set()
        findPerm(0, nums)
        return map(list,list(ans))
        