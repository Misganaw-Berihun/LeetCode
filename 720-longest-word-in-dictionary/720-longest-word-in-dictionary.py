class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = ""
    
    def insert(self, word):
        cnt = 0
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            if cur.is_word:
                cnt += 1
            cur = cur.children[w]
        
        cur.is_word = True
        if cnt == len(word) - 1:
            temp = word
            if len(temp) > len(self.ans):
                self.ans = temp
            else:
                self.ans = min(self.ans, temp) 
            
    def getAns(self):
        return self.ans
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        node = Trie()
        
        for word in words:
            node.insert(word)
            
        return node.getAns()
        