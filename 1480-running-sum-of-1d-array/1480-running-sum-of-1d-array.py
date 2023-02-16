class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        ans = []
        
        for num in nums:
            running += num
            ans.append(running)
        
        return ans
            