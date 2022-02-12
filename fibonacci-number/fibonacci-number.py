class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n < 2:
                return n
            elif n not in cache:
                cache[n] = f(n-1) + f(n-2)
                
            return cache[n]
        
        cache = {}
        
        return f(n)
        