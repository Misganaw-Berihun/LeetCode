class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        '''
            1 1 2
            
        '''
        def backtrack(i, path):
            if i >= len(nums):
                ans.append(path)
                return
            
            backtrack(i + 1, path + [nums[i]])
            swapped_with = set()
            for j in range(i + 1, len(nums)):
                if (nums[i] != nums[j] and nums[j] not in swapped_with):
                    swapped_with.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    backtrack(i + 1, path + [nums[i]])
                    nums[i], nums[j] = nums[j],nums[i]
        ans = []
        backtrack(0, [])
        return ans