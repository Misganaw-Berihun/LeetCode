class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = dict()
        longest = 0
        idx = 0
        
        for i,ch in enumerate(s):
            if ch in occur.keys() and occur[ch] >= idx:
                idx = occur[ch] + 1
            else:
                longest = max(longest,i-idx + 1)
            
            occur[ch] = i
        
                
        return longest
        