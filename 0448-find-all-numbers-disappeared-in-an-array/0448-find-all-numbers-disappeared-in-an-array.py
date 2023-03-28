class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        i = 0
        while i < n:
            pos = nums[i] - 1
            
            if nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        
        ret = []
        for i in range(n):
            if nums[i] - 1 != i:
                ret.append(i + 1)
        
        return ret
        