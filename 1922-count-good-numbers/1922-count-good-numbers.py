class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        i = n // 2
        res = pow(20,i,1000000007)
        
        if n%2:
            res = res * 5  % 1000000007
        
        return res
        
        
        