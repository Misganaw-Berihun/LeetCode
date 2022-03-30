class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ret = [0 for i in range(len(nums))]
        i = 0
        
        for num in nums:
            if num < pivot:
                ret[i] = num
                i += 1
        
        for num in nums:
            if num == pivot:
                ret[i] = num
                i += 1
                
        for num in nums:
            if num > pivot:
                ret[i] = num
                i += 1
                
        return ret
        