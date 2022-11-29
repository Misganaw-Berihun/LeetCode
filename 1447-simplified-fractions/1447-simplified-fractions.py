class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            if (a < b):
                a, b = b, a
            
            while b:
                a %= b
                a, b = b, a
            
            return a
        
        ans = []
        for i in range(1, n):
            for j in range(n, i, -1):
                g =  gcd(i, j)
                if (g == 1):
                    ans.append(str(i) + "/" + str(j))
        return ans
        