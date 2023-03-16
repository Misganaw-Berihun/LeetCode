class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def solve(n, k):
            if n == 1:
                return 0
            if n == 2:
                return 0 if k == 1 else 1
            
            length = 2 ** (n-1)
            mid = length // 2
            
            if k > mid:
                res = solve(n-1, k - mid)
                res = 0 if res == 1 else 1
            else:
                res = solve(n-1, k)
            
            return res
            
            
        
        
        return solve(n, k)
            
            