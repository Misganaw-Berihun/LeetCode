class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = 0
        word_len = len(word)
        
        for i in range(word_len):
            if word[i].isupper():
                cnt += 1
            
            else:
                cnt -= 1
        
        
        
        correct_usage = False
        if cnt == (2 - word_len) and word[0].isupper():
            correct_usage = True
        
        elif abs(cnt) == word_len:
            correct_usage = True
            
        return correct_usage