class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = [1 for i in range(len(nums) + 2)]
        
        for num in nums: 
            if 0 <= num <= len(nums):
                seen[num] = -1
        
        for i in range(1, len(seen)):
            if seen[i] >= 0:
                return i