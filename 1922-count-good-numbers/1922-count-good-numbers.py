class Solution:
    def mul_mod(self, a, b, MOD):
        return (a * b) % MOD
        
    def pow_mod(self, a, b, MOD):
        res = 1
        while b:
            if b & 1 == 1:
                res = self.mul_mod(res, a, MOD)
            b >>= 1
            a = self.mul_mod(a, a, MOD)
        return res
            
    def countGoodNumbers(self, n: int) -> int:
        odd_pow = n // 2
        even_pow = (n + 1) // 2 
        MOD = 1_000_000_007
        
        ans = self.mul_mod(self.pow_mod(5, even_pow, MOD), self.pow_mod(4, odd_pow, MOD), MOD)
        return ans 