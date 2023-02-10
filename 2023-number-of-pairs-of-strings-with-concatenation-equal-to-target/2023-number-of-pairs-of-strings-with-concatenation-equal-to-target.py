class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        length = len(nums)
        count = 0
        
        for i in range(length):
            for j in range(length):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        
        return count
        