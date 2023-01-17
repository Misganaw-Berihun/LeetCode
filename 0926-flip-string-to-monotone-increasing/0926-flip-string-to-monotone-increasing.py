class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        length = len(s)
        one = 0
        zeros = 0
        
        for char in s:
            if char == '1':
                one += 1
        
        zeros = length - one
        ans = min(one, zeros)
        cur_ones = 0
        
        for i in range(length):
            if s[i] == '1':
                cur_ones += 1
            
            rest_zeros = (zeros - (i + 1 - cur_ones))
            ans = min(cur_ones + rest_zeros, ans)
        
        return ans
            