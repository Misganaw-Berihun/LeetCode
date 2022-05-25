class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0      
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        for k in key:
            if k not in cur.children:
                cur.children[k] = TrieNode()
            cur = cur.children[k]
            cur.score += delta
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return 0
            cur = cur.children[p]
        return cur.score
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)