class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left = 0
        right = N - 1
        best = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[0] <= target:
                if nums[mid] < nums[0] or nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    best = mid
                    break
            else:
                if nums[mid] >= nums[0] or nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    best = mid
                    break
        return best
                
                    
        
            