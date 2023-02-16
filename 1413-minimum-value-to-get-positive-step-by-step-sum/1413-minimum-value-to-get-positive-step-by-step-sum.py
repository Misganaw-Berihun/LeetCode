class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur = 0
        minn = 0
        for num in nums:
            cur += num
            minn = min(minn, cur)            
    
        return abs(minn) + 1
        