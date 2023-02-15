class Solution:
    def convertToTitle(self, columnNumber: int) -> str:        
        BASE = 26
        num = columnNumber
        title = []
        
        while (num > 0):
            num -= 1
            temp = num % BASE
            char = chr(temp + ord('A'))
            title.append(char)
            num //= BASE
        
        return ''.join(title[::-1])
        