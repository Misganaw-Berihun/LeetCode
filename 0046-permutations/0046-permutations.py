class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, path):
            if i >= len(nums):
                ans.append(path)
                return
        
            backtrack(i + 1, path + [nums[i]])
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1, path + [nums[i]])
                nums[i], nums[j] = nums[j], nums[i]
                
        backtrack(0, [])
        return ans