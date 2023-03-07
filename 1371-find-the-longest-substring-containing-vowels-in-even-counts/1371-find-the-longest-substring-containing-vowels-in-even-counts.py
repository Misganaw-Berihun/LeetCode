class Solution:        
    def findTheLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        n = len(s)
        seen[0] = -1
        ans = 0
        
        bit = 0
        for i in range(n):
            if s[i] in "aeiou":                
                bit ^= (1 << (ord(s[i]) - ord('a')))
            
            if bit in seen:
                ans = max(ans, i - seen[bit])
            else:
                seen[bit] = i
        
        return ans
