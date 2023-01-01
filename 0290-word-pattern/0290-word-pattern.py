class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = defaultdict(str)
        words = list(s.split())
        N = len(pattern)
        
        if len(words) != N:
            return False
        
        ok = True
        i = 0
        while ok and i < N:
            char = pattern[i]
            if char in match: 
                ok = match[char] == words[i]
                
            elif words[i] in match.values():
                ok = False
                
            else:
                match[char] = words[i]
             
            i += 1
        
        return ok