class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        product = 1
        1 + 2 + 3 
        left = 0
        for right in range(n):
            product *= nums[right]
            
            while left < right and product >= k:
                product //= nums[left]
                left += 1
                
            if product < k:       
                ans += (right - left + 1)
        
        return ans
        