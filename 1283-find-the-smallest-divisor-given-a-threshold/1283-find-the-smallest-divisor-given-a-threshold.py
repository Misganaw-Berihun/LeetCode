class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = float('inf')
        left = 1
        right = max(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            cnt = 0
            
            for v in nums:
                cnt += ceil(v/mid)
                
            if cnt <= threshold:
                ans = min(ans,mid)
                right = mid - 1
                
            elif cnt > threshold:
                left = mid + 1
            
            
        return ans