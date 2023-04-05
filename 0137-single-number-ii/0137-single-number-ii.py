class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        neg_cnt = 0
        
        for num in nums:
            if num < 0:
                neg_cnt += 1
                
        for i in range(32):
            bit = 0
            for num in nums:
                num = abs(num)
                if num & (1 << i):
                    bit += 1
            
            if bit % 3:
                ans |= (1 << i)
        
        if neg_cnt % 3 != 0:
            ans *= -1
        
        return ans
        