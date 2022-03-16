class Solution:        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        start = -1
        end = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > target or \
                        (mid >= 1 and nums[mid] == target and nums[mid - 1] == target):
                    right = mid - 1
            elif nums[mid] < target:
                    left = mid + 1
            else:
                    start = mid
                    break
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > target:
                    right = mid - 1
            elif nums[mid] < target or \
                            (mid + 1 < len(nums) and nums[mid] == target and nums[mid + 1] == target ):
                    left = mid + 1
            else:
                    end = mid
                    break
            
        return [start,end]
                    
                    
        