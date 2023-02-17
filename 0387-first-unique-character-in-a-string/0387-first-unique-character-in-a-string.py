class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        
        found = False
        i = 0
        ans = -1
        
        while not found and i < n:
            if count[s[i]] == 1:
                found = True
                ans = i
            i += 1
        
        return ans