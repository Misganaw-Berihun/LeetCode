class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = dict()
        longest = 0
        idx = 0
        
        for i,ch in enumerate(s):
            if ch in occur.keys():
                longest = max(longest , i - idx)
                
                if occur[ch] >= idx:
                    idx = occur[ch] + 1
            
            occur[ch] = i
        
        longest = max(longest,len(s) - idx)
                
        return longest
        