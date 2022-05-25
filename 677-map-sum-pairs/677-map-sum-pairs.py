class MapSum:

    def __init__(self):
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        

    def sum(self, prefix: str) -> int:
        ret = 0
        for k in self.map.keys():
            if k.startswith(prefix):
                ret += self.map[k]
        return ret
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)