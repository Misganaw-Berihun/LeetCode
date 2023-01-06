class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        size = len(nums)
        sum_of_evens = 0
        res = []
        
        for i in range(size):
            if nums[i] % 2 == 0:
                sum_of_evens += nums[i]
                
        for add, index in queries:
            val = nums[index]
            if val % 2 == 0:
                sum_of_evens -= val
            
            nums[index] += add
            val = nums[index]
            if val % 2 == 0:
                sum_of_evens += val
                
            res.append(sum_of_evens)
        
        return res