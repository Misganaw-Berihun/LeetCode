class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.index = -1
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, idx):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.is_word = True
        cur.index = idx
        
    def search_word(self, word):
        cur = self.root
        for w in word:
            if cur.is_word:
                return cur.index
            if w not in cur.children:
                return -1
            cur = cur.children[w]
        return -1
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = ""
        node = Trie()
        idx = 0
        
        for word in dictionary:
            node.insert(word, idx)
            idx += 1
        
        for word in sentence.split():
            i = node.search_word(word)
            if len(ans) != 0:
                ans += " "
            if i == -1:
                ans += word
            else:
                ans += dictionary[i]
        
        return ans
                
        
        