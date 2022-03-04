class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums.copy()
        heapq.heapify(self.nums)
        for i in range(k,len(nums)):
            heapq.heappop(self.nums)
        self.k = k
        
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        elif self.nums[0] < val:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums,val)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)