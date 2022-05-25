class MapSum:

    def __init__(self):
        self.score = {}
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        pre = ""
        for c in key:
            pre += c
            self.score[pre] = self.score.get(pre, 0) + delta        
        
    def sum(self, prefix: str) -> int:
        return self.score.get(prefix, 0)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)