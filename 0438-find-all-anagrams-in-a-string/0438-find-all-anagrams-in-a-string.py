class Solution:
    def getIndex(self, char):
        return ord(char) - ord('a')
        
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        
        if n < m:
            return []
        
        s_count = [0 for _ in range(26)]
        p_count = [0 for _ in range(26)]
        cnt = 0
        
        for ch in p:
            index = self.getIndex(ch)
            p_count[index] += 1
        
        ans = []
        for i in range(m):
            ch = s[i]
            index = self.getIndex(ch)
            s_count[index] += 1
            
        for i in range(26):
            if s_count[i] == p_count[i]:
                cnt += 1
            
        if cnt == 26:
            ans.append(0)
        
        for i in range(m, n):
            ch = s[i]
            index = self.getIndex(ch)
            s_count[index] += 1
                
            if s_count[index] == p_count[index]:
                cnt += 1
                
            elif s_count[index] == p_count[index] + 1:
                cnt -= 1
              
            ch = s[i - m]
            index = self.getIndex(ch)
            s_count[index] -= 1
            
            if s_count[index] == p_count[index]:
                cnt += 1
                
            elif s_count[index] == p_count[index] - 1:
                cnt -= 1
                
            if cnt == 26:
                ans.append(i - m + 1)
        
            
        return ans
            
            
        