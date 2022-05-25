class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True
        
    def replace(self, word):
        cur, rep = self.root, []
        for w in word:
            if w not in cur.children:
                return None
            rep.append(w)
            cur = cur.children[w]
            if cur.isword:
                return ''.join(rep)
            
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        ans, n = "", len(words)
        for root in dictionary:
            self.insert(root)
        
        for i in range(n):
            word = words[i]
            rep = self.replace(word)
            
            if rep:
                ans += rep
            else:
                ans += word
                
            if i != n - 1:
                ans += ' '
                
        return ans
        
        
        
        
        