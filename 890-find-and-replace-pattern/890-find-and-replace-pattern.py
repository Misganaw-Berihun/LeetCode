class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans, N = [], len(pattern)
        
        for word in words:
            fault = False
            rep = {}
            
            for i in range(N):
                p, w = pattern[i], word[i]
                if (p in rep and rep[p] != w) or (p not in rep and w in rep.values()):
                    fault = True
                    break
                    
                if p not in rep:
                    rep[p] = w
            
            if not fault:
                ans.append(word)
        
        return ans
        