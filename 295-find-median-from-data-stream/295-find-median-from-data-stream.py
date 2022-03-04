class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if len(self.left) > len(self.right):
            temp = heapq.heappushpop(self.left,-num)
            heapq.heappush(self.right,-temp)
        else:
            temp = heapq.heappushpop(self.right,num)
            heapq.heappush(self.left,-temp)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-1*self.left[0] + self.right[0]) / 2
        else:
            return (-1 * self.left[0])
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()