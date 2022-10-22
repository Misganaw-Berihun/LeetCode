class Solution:

    def __init__(self, w: List[int]):
        self.total_sum = sum(w)
        self.size = len(w)
        self.prefix = [0 for i in range(self.size + 1)]
        for i in range(1, self.size + 1):
            self.prefix[i] = self.prefix[i-1] + w[i-1]
        
    def binary_search(self, target):
        left = 1
        right = self.size
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.prefix[mid] < target:
                left = mid + 1
            else:
                right = mid
                 
        return left - 1
        
    def pickIndex(self) -> int:
        rand = randint(1, self.total_sum)
        return self.binary_search(rand)
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()