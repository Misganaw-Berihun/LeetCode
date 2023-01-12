class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        ans = 0
        for num in nums:
            heappush(heap, -num)
            
        while k:
            top = -heappop(heap)
            ans += top
            
            replacement = ceil(top / 3)
            heappush(heap, -replacement)
            k -= 1
        
        return ans
            
            