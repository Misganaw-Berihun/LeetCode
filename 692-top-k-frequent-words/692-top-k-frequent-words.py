class TrieNode:
    def __init__(self):
        self.children= {}
        self.is_word = False
        self.cnt = 0
        self.idx = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.idx_cnt = {}
        
    def insert(self, word, idx):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.cnt += 1
        if not cur.is_word:
            cur.is_word = True
            cur.idx = idx
        self.idx_cnt[cur.idx] = cur.cnt
        
    def get_idx_cnt(self):
        return self.idx_cnt
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        node = Trie()
        idx = 0
        for word in words:
            node.insert(word, idx)
            idx += 1
        cnt = node.get_idx_cnt()
        items = list(sorted(cnt.items(), key = lambda c: (-c[1], c[0])))
        return list(map(lambda c: words[c[0]], items[:k]))
        