class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.prefixes = defaultdict(list)
    
    def insert(self, word):
        cur = self.root
        pre = ""
        for w in word:
            pre += w
            if w not in cur.children:
                cur.children[w] = TrieNode()
            self.prefixes[pre].append(word)
        cur = cur.children[w]
        cur.is_word = True
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        node = Trie()
        t = ""
        ans = []
        for product in products:
            node.insert(product)
        
        for let in searchWord:
            t += let
            temp = sorted(node.prefixes[t])
            ans.append(temp[:3])
                
        return ans
            
            
        
            
        