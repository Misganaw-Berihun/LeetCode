class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        first_on_bit = 0
        shift = 0
        res1, res2 = 0, 0
        
        for num in nums:
            xor = xor ^ num
        
        
        while (xor & (1 << shift) == 0):
            shift += 1
            
        for num in nums:
            if (num & (1 << shift) > 0):
                res1 ^= num
            else:
                res2 ^= num
        
        return [res1, res2]