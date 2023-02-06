class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point
        keys = self.points.keys()
        
        for x2, y2 in keys:
            if y2 != y1 or x2 == x1:
                continue
                
            length = abs(x2 - x1)

            x3 = x2
            y3 = y2 - length
            x4 = x1
            y4 = y1 - length
            
            if (x3, y3) in self.points and (x4, y4) in self.points:
                count += (self.points[(x3, y3)] * self.points[(x4, y4)] * self.points[(x2, y2)])

            x3 = x2
            y3 = y2 + length
            x4 = x1
            y4 = y1 + length
            if (x3, y3) in self.points and (x4, y4) in self.points:
                count += (self.points[(x3, y3)] * self.points[(x4, y4)] * self.points[(x2, y2)])
        
        return count
                


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)