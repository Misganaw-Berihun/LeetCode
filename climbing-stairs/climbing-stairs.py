class Solution:
    def climbStairs(self, n: int) -> int:
        def steps(num):
            if num <= 2:
                return num
            elif num not in cache:
                cache[num] = steps(num - 1) + steps(num - 2)
                
            return cache[num]
        
        cache = {}
        return steps(n)