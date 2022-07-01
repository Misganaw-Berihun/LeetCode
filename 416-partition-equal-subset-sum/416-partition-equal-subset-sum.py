class Solution:
    def canPartition(self, nums: List[int]) -> bool:        
        totalSum = sum(nums)
        if totalSum & 1 == 1:
            return False
        
        partition = totalSum // 2
        memo = set()
        memo.add(0)
        
        for i in range(len(nums)):
            possibleSums = list(memo)
            for s in possibleSums:
                memo.add(s + nums[i])
        
        return partition in memo