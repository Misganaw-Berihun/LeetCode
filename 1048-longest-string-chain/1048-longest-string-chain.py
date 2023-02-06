class Solution:    
    def longestStrChain(self, words: List[str]) -> int:
        key = lambda a: len(a)
        words.sort(key = key)
        count = defaultdict(int)
        ans = 1
        
        for word in words:
            n = len(word)
            count[word]  = max(count[word], 1);
            for i in range(n):
                s = word[:i] + word[i+1:]
                if s in count:
                    count[word] = max(count[word], 1 + count[s])
                    ans = max(count[word], ans)
        
        return ans
                
            
        
        