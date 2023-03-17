class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def bk(i, path):
            if len(nums) == i:
                ans.append(path.copy())
                return
            
            bk(i + 1, path + [nums[i]])
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            
            bk(i + 1, path)
        
        ans = []
        nums.sort()
        bk(0, [])
        return ans
        