class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word = word
        
    def replace(self, word):
        cur, rep = self.root, []
        for w in word:
            if w not in cur.children or len(cur.word) > 0:
                break
            rep.append(w)
            cur = cur.children[w]
        return cur.word if len(cur.word)>0 else word
            
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        ans, n = "", len(words)
        for root in dictionary:
            self.insert(root)
        
        return ' '.join(map(self.replace, words))
        
        
        
        
        