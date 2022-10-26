class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_nums = [1, 2]
        
        while fib_nums[-1] <= k:
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        
        count = 0
        i = len(fib_nums) - 2

        while k > 0:
            if k >= fib_nums[i]:
                k -= fib_nums[i]
                count += 1 
            i -= 1
        
        return count
        
        
        