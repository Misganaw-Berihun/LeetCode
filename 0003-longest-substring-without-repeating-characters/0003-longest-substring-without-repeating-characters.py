class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        window = 0
        n = len(s)
        
        left = 0
        for right in range(n):
            seen[s[right]] += 1
            if seen[s[right]] == 1:
                window += 1
            
            if right - left + 1 - window > 0:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    window -= 1
                left += 1
        
        return n - left
                
        