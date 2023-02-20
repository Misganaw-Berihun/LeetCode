class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        '''
         "dddiiiinnssssssoooo"
        ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
        
        '''
        count = 0
        n = len(s)
        
        for word in words:
            m = len(word)
            
            if n < m:
                continue
                
            i, j = 0, 0
            k, l = 0, 0
            valid = True
            
            while valid and i < n and j < m and s[i] == word[j]:
                c1, c2 = 0, 0
                
                while k < n and s[k] == s[i]:
                    k += 1
                    c1 += 1
                    
                while l < m and word[l] == word[j]:
                    l += 1
                    c2 += 1
                
                if (c2 > c1) or (c1 != c2 and c1 <= 2):
                    valid = False
                
                i, j = k, l
            
            if valid and i >= n and j >= m:
                count += 1
        
        return count
        