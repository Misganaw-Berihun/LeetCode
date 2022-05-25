class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True
    
    def helper(self, prefix):
        cur = self.root
        for let in prefix:
            if let not in cur.children:
                return None
            cur = cur.children[let]
        return cur
        
    def search(self, word: str) -> bool:
        node = self.helper(word)
        return node != None and node.isword; 
        
    def startsWith(self, prefix: str) -> bool:
        node = self.helper(prefix)
        return node != None
      


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)