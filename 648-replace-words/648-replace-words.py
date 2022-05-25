class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words  = sentence.split()
        ans = ""
        dictionary.sort(reverse = True)
        for i in range(len(words)):
            word = words[i] 
            tmp = word
            for root in dictionary:
                if word.startswith(root):
                    tmp = root
            
            ans += tmp
            if i != len(words) - 1:
                ans += " "
        return ans
        
        
        