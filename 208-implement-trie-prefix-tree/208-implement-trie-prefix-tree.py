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
        

    def search(self, word: str, prefix = False) -> bool:
        cur = self.root
        for let in word:
            if let not in cur.children:
                return False
            cur = cur.children[let]
        return cur.isword or prefix

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)