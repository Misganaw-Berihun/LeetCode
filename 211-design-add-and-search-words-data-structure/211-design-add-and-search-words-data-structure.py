class TrieNode:
    def __init__(self):
        self.edges = {}
        self.is_word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.edges:
                cur.edges[w] = TrieNode()
            cur = cur.edges[w]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                if cur.is_word:
                    return True
                return False
            if word[i] in cur.edges:
                if dfs(i + 1, cur.edges[word[i]]):
                    return True
            elif word[i] == '.':
                for neig in cur.edges:
                    if dfs(i + 1, cur.edges[neig]):
                        return True
            return False
        return dfs(0, self.root)        
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)