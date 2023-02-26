class Solution:
    def getIndex(self, char):
         return ord(char) - ord('a')
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
    
        s1_count = [0 for _ in range(26)]
        s2_count = [0 for _ in range(26)]
        for char in s1:
            index = self.getIndex(char)
            s1_count[index] += 1
        
        cnt = 0
        for i in range(n):
            char = s2[i]
            index = self.getIndex(char)
            s2_count[index] += 1
          
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                cnt += 1
        
        for i in range(n, m):
            if cnt == 26:
                return True
            
            index = self.getIndex(s2[i])
            s2_count[index] += 1                
            if s2_count[index] == s1_count[index]:
                cnt += 1
            
            elif s2_count[index] == s1_count[index] + 1:
                cnt -= 1
                
            index = self.getIndex(s2[i - n])
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                cnt += 1
            elif s2_count[index] == s1_count[index] - 1:
                cnt -= 1
        
        return (cnt == 26)