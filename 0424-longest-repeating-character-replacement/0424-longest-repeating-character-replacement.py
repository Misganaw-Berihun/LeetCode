class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0 for i in range(26)]
        left = 0
        ans = 0
        left = 0
        freqChar = 0
        strLen = len(s)
        
        for right in range(strLen):
            count[ord(s[right]) - 65] += 1       
            cur_len = right - left + 1
            
            while left < right and cur_len - max(count) > k:
                char_left = s[left]
                count[ord(char_left) - 65] -= 1
                left += 1
                cur_len = right - left + 1
            ans = max(ans, cur_len)
        
        return ans  
        