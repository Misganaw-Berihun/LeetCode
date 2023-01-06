class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        num_words = len(words)
        max_word_len = 0
        ans = []
        
        for word in words:
            max_word_len = max(max_word_len, len(word))
        
        for i in range(max_word_len):
            temp = []
            for j in range(num_words):
                ch = " "
                
                if i < len(words[j]):
                    ch = words[j][i]
                    
                temp.append(ch)
                
            while temp[-1] == " ":
                temp.pop()
                
            ans.append(''.join(temp))
        
        return ans
        