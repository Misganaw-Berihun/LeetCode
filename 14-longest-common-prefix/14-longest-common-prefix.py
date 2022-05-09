class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True
        
    def commonPrefix(self):
        cur = self.root
        pre = ""
        while len(cur.children) == 1 and not cur.isword:
            p = list(cur.children.keys())[0]
            pre += p
            cur = cur.children[p]
        return pre
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        node = Trie()
        for i in range(len(strs)):
            if strs[i] == "":
                return ""
            node.insert(strs[i])
            
        return node.commonPrefix()
        