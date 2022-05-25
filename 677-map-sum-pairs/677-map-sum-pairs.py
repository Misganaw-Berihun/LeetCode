class TrieNode:
    def  __init__(self):
        self.children = {}
        self.value = 0
        self.isword = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.summ = 0
        
    def insert(self, word, val):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True
        cur.value = val
        
    def findPrefix(self, prefix):
        cur = self.root
        for let in prefix:
            if let not in cur.children:
                return None
            cur = cur.children[let]
        return cur
    
    def dfs(self, start):
        if not start:
            return
        if start.isword:
            self.summ += start.value 
        for child in start.children:
            self.dfs(start.children[child])
        
class MapSum:

    def __init__(self):
        self.theTrie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.theTrie.insert(key, val)
        

    def sum(self, prefix: str) -> int:
        self.theTrie.summ = 0
        self.theTrie.dfs(self.theTrie.findPrefix(prefix))
        return self.theTrie.summ
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)