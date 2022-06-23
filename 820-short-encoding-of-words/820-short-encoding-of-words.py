class TrieNode:
    def __init__(self):
        self.edges = {}
        self.isword = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = 0
    
    def insert(self, word):
        cur = self.root
        for i in range(len(word) - 1, -1, -1):
            w = word[i]
            if w not in cur.edges:
                cur.edges[w] = TrieNode()
            cur = cur.edges[w]  
        cur.isword = True
    
    def check(self, word):
        cur = self.root
        for i in range(len(word) - 1, -1, -1):
            w = word[i]
            if w not in cur.edges:
                return False
            cur = cur.edges[w]
        return len(cur.edges) == 0 and cur.isword

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        node = Trie()
        ans = 0
        visited = set()
        for word in words:
            node.insert(word)
            
        for word in words:
            if node.check(word) and word not in visited:
                visited.add(word)
                ans += len(word) + 1
        
        return ans
                
                
            
        

            
        