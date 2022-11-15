class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr_len = len(nums)
        nums.sort()
        perimeter = 0
        found = False
        i = arr_len - 3
        
        while i >= 0 and not found:
            if (nums[i] + nums[i+1]) > nums[i+2]:
                perimeter = nums[i] + nums[i+1] + nums[i+2]
                found = True
            i -= 1
        return perimeter