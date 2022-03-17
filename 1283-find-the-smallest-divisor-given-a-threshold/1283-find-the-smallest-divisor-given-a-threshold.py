class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = 1e6
        
        while left <= right:
            mid = left + (right - left) // 2
            cnt = 0
            
            for v in nums:
                cnt += ceil(v/mid)
                
            if cnt <= threshold:
                right = mid - 1
                
            elif cnt > threshold:
                left = mid + 1
            
        return int(left)
        
        