class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countOf = defaultdict(int)
        ans = 0
        left = 0
        mxCnt, freqChar = 0, 0
        strLen = len(s)
        
        for right in range(strLen):
            countOf[s[right]] += 1
            if countOf[s[right]] > mxCnt:
                mxCnt = countOf[s[right]]
                freqChar = s[right]
            curLen = right - left + 1
            charAtLeft = s[left]
            while left < right and curLen - mxCnt > k:
                countOf[charAtLeft] -= 1
                left += 1
                charAtLeft = s[left]
                curLen = right - left + 1
            ans = max(ans, curLen)
        
        return ans                