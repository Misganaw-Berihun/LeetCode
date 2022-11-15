class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr_len = len(nums)
        nums.sort()
        perimeter = 0
        
        for i in range(arr_len - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                perimeter = max(nums[i] + nums[i+1] + nums[i+2], perimeter)
        
        return perimeter