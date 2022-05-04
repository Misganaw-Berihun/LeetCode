class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True

    def search(self, word: str, prefix = False) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.isWord or prefix

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)