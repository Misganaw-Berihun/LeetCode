class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        heap = []
        max_sliding_window = []
        
        for right in range(size):
            heappush(heap, (-nums[right], right))
            while heap and right - heap[0][1] + 1 > k:
                heappop(heap)
            
            if (right >= k - 1):
                curMax, curMaxIdx = heap[0]
                max_sliding_window.append(-curMax)
        
        return max_sliding_window
        