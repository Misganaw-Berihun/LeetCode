class Solution:
    def musk(self, word):
        num = 0
        
        for ch in word:
            shift = ord(ch) - ord('a')
            num = num | (1 << shift)
        
        return num
        
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        
        for word in words:
            cur_musk = self.musk(word)
            arr.append((cur_musk, len(word)))
        
        ans = 0
        for el1 in arr:
            for el2 in arr:
                if (el1[0] & el2[0]) == 0:
                    ans = max(ans, el1[1] * el2[1])
        return ans