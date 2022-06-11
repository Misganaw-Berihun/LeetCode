class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def findPerm(i, temp):
            nonlocal ans, used
            if i >= len(nums) - 1:
                c = temp.copy()
                j = tuple(c)
                if j not in used:
                    ans.append(c)
                    used.add(j)
                return
            
            for k in range(i, len(nums)):
                temp[k], temp[i] = temp[i], temp[k]
                findPerm(i + 1, temp)
                temp[k], temp[i] = temp[i], temp[k]
            
        ans = []
        used = set()
        findPerm(0, nums)
        return ans
        