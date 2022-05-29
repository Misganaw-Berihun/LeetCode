class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occured = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in occured:
                return [occured[diff], i]
            occured[num] = i
            
        return []
                
        