class Solution:

    def __init__(self, w: List[int]):
        self.prefix = w.copy()
        for i in range(1, len(w)):
            self.prefix[i] += self.prefix[i-1]
        self.minn = 1
        self.maxx = self.prefix[len(w) - 1]
        

    def pickIndex(self) -> int:
        l = -1
        r = len(self.prefix)
        rand = randint(self.minn, self.maxx)
        
        while l + 1 < r:
            m = (l + r) // 2
            
            if self.prefix[m] < rand:
                l = m
            else:
                r = m
        
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()