class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        start = 1
        for i in range(32):
            if (n & start) > 0:
                ans += 1
            start = start << 1
        return ans
            
            
        