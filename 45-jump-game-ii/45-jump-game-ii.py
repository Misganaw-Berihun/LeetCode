class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, currentFar, curEnd = 0, 0, 0
        n = len(nums)
        for i in range(n - 1):
            currentFar = max(currentFar, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = currentFar
                
        return jumps