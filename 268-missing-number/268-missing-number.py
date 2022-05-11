class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor, n = 0, len(nums)
        for i in range(n):
            xor = xor ^ nums[i] ^ i
        return xor ^ n
        
        