class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            if n == 1:
                return x
            elif n % 2 != 0:
                return self.myPow(x**2, n // 2) * x
            else:
                return self.myPow(x*x, n // 2) 
        else:
            return 1 / self.myPow(x , -1 * n)
            
    