class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countOf = defaultdict(int)
        strLen = len(s)
        
        left = 0
        for right in range(strLen):
            countOf[s[right]] += 1
            max_val = max(countOf.values())
            
            if right - left + 1 - max_val > k:
                countOf[s[left]] -= 1
                left += 1
        
        return strLen - left
        
                       