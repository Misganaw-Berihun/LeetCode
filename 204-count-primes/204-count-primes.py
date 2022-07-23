class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [True for i in range(n)]
        ans = 0
        i = 2
        while i * i < n:
            if not nums[i]:
                i += 1
                continue
            for j in range((i*i), n, i):
                nums[j] = False
            i += 1
        
        for j in range(2, len(nums)):
            if nums[j] == True:
                ans += 1
                
        return ans
                    
        