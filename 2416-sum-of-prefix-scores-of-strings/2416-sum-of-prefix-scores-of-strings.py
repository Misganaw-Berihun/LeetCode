class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
            cur.count += 1
    
    def find(self, word):
        cur = self.root
        ret = 0
        for w in word:
            cur = cur.children[w]
            ret += cur.count
        return ret
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        ans = [0 for i in range(len(words))]
        for word in words:
            trie.insert(word)
            
        for i in range(len(words)):
            ans[i] = trie.find(words[i])
            
        return ans 
            
        